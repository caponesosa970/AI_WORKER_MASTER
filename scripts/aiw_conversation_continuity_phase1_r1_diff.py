from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path


AUTHORIZED = {263, 273, 282, 309, 317, 320, 324, 325}
ADDED = {327}
PHONE_PROVEN = {71, 199, 223, 225, 226, 227, 230, 231}


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def blocks(text: str, tag: str, key_pattern: str) -> dict[int, str]:
    result: dict[int, str] = {}
    for match in re.finditer(rf"<{tag}\b.*?</{tag}>", text, re.DOTALL):
        key = re.search(key_pattern, match.group(0), re.DOTALL)
        if key:
            result[int(key.group(1))] = match.group(0)
    return result


def task_map(root: ET.Element) -> dict[int, ET.Element]:
    return {int(task.findtext("id", "-1")): task for task in root.findall("Task")}


def action_number(action: ET.Element) -> int:
    return int((action.get("sr") or "act-1")[3:])


def actions(task: ET.Element) -> list[ET.Element]:
    return sorted(task.findall("Action"), key=action_number)


def normalized_action(action: ET.Element) -> str:
    text = ET.tostring(action, encoding="unicode")
    return re.sub(r'sr="act\d+"', 'sr="act#"', text, count=1)


def action_detail(action: ET.Element) -> dict[str, object]:
    code = int(action.findtext("code", "-1"))
    strings = {node.get("sr", ""): node.text or "" for node in action.findall("Str")}
    conditions = [
        {"lhs": node.findtext("lhs", ""), "op": node.findtext("op", ""), "rhs": node.findtext("rhs", "")}
        for node in action.findall("ConditionList/Condition")
    ]
    kind = {
        130: "PerformTask", 547: "VariableSet", 549: "VariableClear", 37: "If",
        43: "Else", 38: "EndIf", 39: "For", 40: "EndFor", 30: "Wait",
        126: "Stop", 1810865467: "AutoSheetsGet", 1461810131: "AutoSheetsUpdate",
    }.get(code, "Action")
    detail: dict[str, object] = {"sr": action.get("sr"), "code": code, "kind": kind}
    if strings:
        detail["strings"] = strings
    if conditions:
        detail["conditions"] = conditions
    parameters = action.findtext("Bundle/Vals/parameters")
    if parameters:
        try:
            parsed = json.loads(parameters)
            detail["plugin"] = {
                "sheet": parsed.get("_spreadSheet", {}).get("sheetName"),
                "range": parsed.get("output", {}).get("range"),
                "reference": parsed.get("referenceCell"),
                "create_sheet_if_needed": parsed.get("createSheetIfNeeded"),
                "update_later_if_offline": parsed.get("updateLaterIfOffline"),
            }
        except json.JSONDecodeError:
            detail["plugin"] = {"parameters_parse": "FAIL"}
    return detail


def call_graph(tasks: dict[int, ET.Element]) -> dict[int, set[int]]:
    by_name = {task.findtext("nme", ""): task_id for task_id, task in tasks.items()}
    result: dict[int, set[int]] = defaultdict(set)
    for task_id, task in tasks.items():
        for action in actions(task):
            if action.findtext("code") == "130":
                name = action.findtext("Str[@sr='arg0']", "")
                if name in by_name:
                    result[task_id].add(by_name[name])
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    base_text = args.base.read_text(encoding="utf-8")
    candidate_text = args.candidate.read_text(encoding="utf-8")
    base_root = ET.fromstring(base_text)
    candidate_root = ET.fromstring(candidate_text)
    base_tasks = task_map(base_root)
    candidate_tasks = task_map(candidate_root)
    base_raw = blocks(base_text, "Task", r"<id>(\d+)</id>")
    candidate_raw = blocks(candidate_text, "Task", r"<id>(\d+)</id>")
    changed = sorted(task_id for task_id in base_tasks if base_raw[task_id] != candidate_raw.get(task_id))
    added = sorted(set(candidate_tasks) - set(base_tasks))
    task_deltas: list[dict[str, object]] = []
    for task_id in changed:
        before_actions = actions(base_tasks[task_id])
        after_actions = actions(candidate_tasks[task_id])
        matcher = difflib.SequenceMatcher(a=[normalized_action(a) for a in before_actions], b=[normalized_action(a) for a in after_actions], autojunk=False)
        opcodes = [
            {"operation": tag, "base_actions": [i1, i2 - 1] if i2 > i1 else [], "candidate_actions": [j1, j2 - 1] if j2 > j1 else []}
            for tag, i1, i2, j1, j2 in matcher.get_opcodes() if tag != "equal"
        ]
        task_deltas.append({
            "task_id": task_id,
            "name": candidate_tasks[task_id].findtext("nme"),
            "base_action_count": len(before_actions),
            "candidate_action_count": len(after_actions),
            "base_raw_sha256": sha(base_raw[task_id]),
            "candidate_raw_sha256": sha(candidate_raw[task_id]),
            "aligned_changed_ranges": opcodes,
            "candidate_action_inventory": [action_detail(action) for action in after_actions],
        })
    for task_id in added:
        after_actions = actions(candidate_tasks[task_id])
        task_deltas.append({
            "task_id": task_id,
            "name": candidate_tasks[task_id].findtext("nme"),
            "base_action_count": 0,
            "candidate_action_count": len(after_actions),
            "base_raw_sha256": None,
            "candidate_raw_sha256": sha(candidate_raw[task_id]),
            "aligned_changed_ranges": [{"operation": "insert", "base_actions": [], "candidate_actions": [0, len(after_actions) - 1]}],
            "candidate_action_inventory": [action_detail(action) for action in after_actions],
        })

    before_graph = call_graph(base_tasks)
    after_graph = call_graph(candidate_tasks)
    edges_before = {(caller, callee) for caller, targets in before_graph.items() for callee in targets}
    edges_after = {(caller, callee) for caller, targets in after_graph.items() for callee in targets}
    profile_before = blocks(base_text, "Profile", r"<id>(\d+)</id>")
    profile_after = blocks(candidate_text, "Profile", r"<id>(\d+)</id>")
    scenes_before = {m.group(1): m.group(0) for m in re.finditer(r'<Scene sr="([^"]+)".*?</Scene>', base_text, re.DOTALL)}
    scenes_after = {m.group(1): m.group(0) for m in re.finditer(r'<Scene sr="([^"]+)".*?</Scene>', candidate_text, re.DOTALL)}
    preserved_ids = sorted(set(base_tasks) - AUTHORIZED)
    preserved_failures = [task_id for task_id in preserved_ids if base_raw[task_id] != candidate_raw[task_id]]
    report = {
        "status": "PASS" if changed == sorted(AUTHORIZED) and added == sorted(ADDED) and not preserved_failures and profile_before == profile_after and scenes_before == scenes_after else "FAIL",
        "changed_existing": changed,
        "added_tasks": added,
        "task_deltas": task_deltas,
        "call_graph_delta": {
            "added_edges": [{"caller": caller, "callee": callee} for caller, callee in sorted(edges_after - edges_before)],
            "removed_edges": [{"caller": caller, "callee": callee} for caller, callee in sorted(edges_before - edges_after)],
        },
        "raw_preservation": {
            "preserved_existing_count": len(preserved_ids),
            "failures": preserved_failures,
            "phone_proven": {str(task_id): base_raw[task_id] == candidate_raw[task_id] for task_id in sorted(PHONE_PROVEN)},
            "task254": base_raw[254] == candidate_raw[254],
            "task255": base_raw[255] == candidate_raw[255],
            "task262": base_raw[262] == candidate_raw[262],
            "profiles": profile_before == profile_after,
            "scenes": scenes_before == scenes_after,
        },
        "project_registry_delta": {"added_task_ids": added, "profiles_changed": profile_before != profile_after, "scenes_changed": scenes_before != scenes_after},
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "changed": changed, "added": added, "preserved_existing": len(preserved_ids), "call_edges_added": len(report["call_graph_delta"]["added_edges"]), "call_edges_removed": len(report["call_graph_delta"]["removed_edges"])}, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
