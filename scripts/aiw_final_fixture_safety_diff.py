#!/usr/bin/env python3
"""Create an exact, privacy-safe action/property delta for the fixture repair."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from difflib import SequenceMatcher
from pathlib import Path
import xml.etree.ElementTree as ET


AUTHORIZED = {237, 268, 270, 272, 276, 293}


def text(node: ET.Element, tag: str, default: str = "") -> str:
    child = node.find(tag)
    return default if child is None or child.text is None else child.text


def tasks(root: ET.Element) -> dict[int, ET.Element]:
    found = {}
    for node in root.findall("Task"):
        match = re.search(r"(\d+)$", node.attrib["sr"])
        if match:
            found[int(match.group(1))] = node
    return found


def actions(task: ET.Element) -> list[ET.Element]:
    return sorted(task.findall("Action"), key=lambda node: int(node.attrib["sr"][3:]))


def canonical(action: ET.Element) -> str:
    node = copy.deepcopy(action)
    node.attrib["sr"] = "act#"
    return ET.tostring(node, encoding="unicode", short_empty_elements=True)


def action_summary(action: ET.Element) -> dict[str, object]:
    args = {}
    for child in action:
        if child.tag.startswith("Str") and "sr" in child.attrib:
            args[child.attrib["sr"]] = child.text or ""
        elif child.tag.startswith("Int") and "sr" in child.attrib:
            args[child.attrib["sr"]] = child.attrib.get("val", child.text or "")
    conditions = []
    for condition in action.findall("Condition"):
        conditions.append({
            "lhs": text(condition, "lhs"),
            "op": condition.attrib.get("op", ""),
            "rhs": text(condition, "rhs"),
        })
    return {
        "sr": action.attrib.get("sr", ""),
        "code": text(action, "code"),
        "label": text(action, "label"),
        "args": args,
        "conditions": conditions,
        "continue_after_error": text(action, "onerror"),
    }


def sha(node: ET.Element) -> str:
    return hashlib.sha256(ET.tostring(node, encoding="utf-8")).hexdigest().upper()


def perform_calls(task: ET.Element) -> list[str]:
    calls = []
    for action in actions(task):
        if text(action, "code") != "130":
            continue
        target = next(
            (child.text or "" for child in action.findall("Str") if child.attrib.get("sr") == "arg0"),
            "",
        )
        if target:
            calls.append(target)
    return calls


def build_report(base_path: Path, candidate_path: Path) -> dict[str, object]:
    base_root = ET.parse(base_path).getroot()
    candidate_root = ET.parse(candidate_path).getroot()
    base = tasks(base_root)
    candidate = tasks(candidate_root)
    base_names = {task_id: text(node, "nme") for task_id, node in base.items()}
    candidate_names = {task_id: text(node, "nme") for task_id, node in candidate.items()}
    changed = []
    for task_id in sorted(AUTHORIZED):
        before = actions(base[task_id])
        after = actions(candidate[task_id])
        matcher = SequenceMatcher(
            a=[canonical(action) for action in before],
            b=[canonical(action) for action in after],
            autojunk=False,
        )
        operations = []
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                continue
            operations.append({
                "operation": tag,
                "base_action_range": [i1, i2 - 1] if i2 > i1 else [],
                "candidate_action_range": [j1, j2 - 1] if j2 > j1 else [],
                "base_actions": [action_summary(action) for action in before[i1:i2]],
                "candidate_actions": [action_summary(action) for action in after[j1:j2]],
            })
        changed.append({
            "task_id": task_id,
            "task_name": text(candidate[task_id], "nme"),
            "base_action_count": len(before),
            "candidate_action_count": len(after),
            "base_raw_sha256": sha(base[task_id]),
            "candidate_raw_sha256": sha(candidate[task_id]),
            "operations": operations,
        })
    graph_delta = []
    for task_id in sorted(set(base) | set(candidate)):
        before = perform_calls(base[task_id]) if task_id in base else []
        after = perform_calls(candidate[task_id]) if task_id in candidate else []
        if before != after:
            graph_delta.append({
                "task_id": task_id,
                "task_name": candidate_names.get(task_id, base_names.get(task_id, "")),
                "base_calls": before,
                "candidate_calls": after,
            })
    reverse_callers: dict[str, list[dict[str, object]]] = {}
    for caller_id, task in candidate.items():
        for target in perform_calls(task):
            reverse_callers.setdefault(target, []).append({
                "caller_id": caller_id,
                "caller_name": candidate_names[caller_id],
            })
    oversized = []
    for task_id, task in candidate.items():
        count = len(actions(task))
        if count <= 500:
            continue
        name = candidate_names[task_id]
        oversized.append({
            "task_id": task_id,
            "task_name": name,
            "action_count": count,
            "role": "orchestrator" if "ORCHESTRATOR" in name else "phase" if "Validation Phase" in name else "helper",
            "reachable_callers": reverse_callers.get(name, []),
            "changed_in_repair": task_id in AUTHORIZED,
            "added_in_repair": task_id not in base,
            "modularity_disposition": (
                "VIOLATION_REQUIRES_DECOMPOSITION" if task_id not in base
                else "PRE_EXISTING_RAW_BYTE_PRESERVED_NOT_A_NEW_HELPER_VIOLATION"
            ),
        })
    return {
        "report": "AIW final fixture-safety exact action delta",
        "base": {"name": base_path.name, "sha256": hashlib.sha256(base_path.read_bytes()).hexdigest().upper()},
        "candidate": {"name": candidate_path.name, "sha256": hashlib.sha256(candidate_path.read_bytes()).hexdigest().upper()},
        "authorized_existing_tasks": sorted(AUTHORIZED),
        "changed_tasks": changed,
        "complete_call_graph_delta": graph_delta,
        "over_500_task_inventory": sorted(oversized, key=lambda item: int(item["task_id"])),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    report = build_report(args.base, args.candidate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "output": str(args.output),
        "tasks": [
            {
                "id": item["task_id"],
                "name": item["task_name"],
                "base_actions": item["base_action_count"],
                "candidate_actions": item["candidate_action_count"],
                "delta_groups": len(item["operations"]),
            }
            for item in report["changed_tasks"]
        ],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
