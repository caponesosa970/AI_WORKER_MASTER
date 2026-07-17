from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


AUTHORIZED = {262, 273, 276, 278, 282, 284}
ADDED = set(range(309, 327))
PROTECTED = {71, 199, 223, 225, 226, 227, 230, 231}


def sha(value: str | bytes) -> str:
    if isinstance(value, str):
        value = value.encode("utf-8")
    return hashlib.sha256(value).hexdigest().upper()


def raw_tasks(text: str) -> dict[int, str]:
    result = {}
    for match in re.finditer(r'<Task sr="task(\d+)".*?</Task>', text, re.DOTALL):
        result[int(match.group(1))] = match.group(0)
    return result


def actions(raw: str) -> list[str]:
    return re.findall(r"<Action\b.*?</Action>", raw, re.DOTALL)


def action_summary(raw: str) -> dict[str, object]:
    node = ET.fromstring(raw)
    code = int(node.findtext("code", "-1"))
    strings: dict[str, object] = {}
    for item in node.findall("Str"):
        value = item.text or ""
        if len(value) > 160 or "OpenAIKey" in value or re.search(r"sk-[A-Za-z0-9_-]{10,}", value):
            strings[item.get("sr", "")] = {"sha256": sha(value), "length": len(value)}
        else:
            strings[item.get("sr", "")] = value
    conditions = [
        {"lhs": c.findtext("lhs", ""), "op": c.findtext("op", ""), "rhs": c.findtext("rhs", "")}
        for c in node.findall("ConditionList/Condition")
    ]
    plugin = node.find("Bundle/Vals/parameters")
    return {
        "sr": node.get("sr"),
        "code": code,
        "strings": strings,
        "conditions": conditions,
        "plugin_parameters_sha256": sha(plugin.text) if plugin is not None and plugin.text else None,
    }


def calls(raw: str) -> list[str]:
    result = []
    for action in actions(raw):
        node = ET.fromstring(action)
        if node.findtext("code") == "130":
            result.append(node.findtext("Str[@sr='arg0']", ""))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    base_text = args.base.read_text(encoding="utf-8")
    candidate_text = args.candidate.read_text(encoding="utf-8")
    base = raw_tasks(base_text)
    candidate = raw_tasks(candidate_text)
    changed = sorted(task_id for task_id in base if base[task_id] != candidate.get(task_id))
    added = sorted(set(candidate) - set(base))
    records = []
    for task_id in changed:
        old_actions = actions(base[task_id])
        new_actions = actions(candidate[task_id])
        old_hashes = [sha(re.sub(r'sr="act\d+"', 'sr="act#"', value, count=1)) for value in old_actions]
        new_hashes = [sha(re.sub(r'sr="act\d+"', 'sr="act#"', value, count=1)) for value in new_actions]
        matcher = difflib.SequenceMatcher(a=old_hashes, b=new_hashes, autojunk=False)
        groups = []
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                continue
            groups.append({
                "operation": tag,
                "base_actions": [i1, i2 - 1] if i2 > i1 else [],
                "candidate_actions": [j1, j2 - 1] if j2 > j1 else [],
                "candidate_action_detail": [action_summary(value) for value in new_actions[j1:j2]],
            })
        records.append({
            "task_id": task_id,
            "task_name": ET.fromstring(candidate[task_id]).findtext("nme"),
            "base_raw_sha256": sha(base[task_id]),
            "candidate_raw_sha256": sha(candidate[task_id]),
            "base_action_count": len(old_actions),
            "candidate_action_count": len(new_actions),
            "base_calls": calls(base[task_id]),
            "candidate_calls": calls(candidate[task_id]),
            "change_groups": groups,
        })
    helper_records = [
        {
            "task_id": task_id,
            "task_name": ET.fromstring(candidate[task_id]).findtext("nme"),
            "raw_sha256": sha(candidate[task_id]),
            "action_count": len(actions(candidate[task_id])),
            "calls": calls(candidate[task_id]),
        }
        for task_id in added
    ]
    preservation = [
        {
            "task_id": task_id,
            "task_name": ET.fromstring(base[task_id]).findtext("nme"),
            "base_raw_sha256": sha(base[task_id]),
            "candidate_raw_sha256": sha(candidate[task_id]),
            "identical": base[task_id] == candidate[task_id],
        }
        for task_id in sorted(PROTECTED)
    ]
    report = {
        "status": "PASS" if changed == sorted(AUTHORIZED) and added == sorted(ADDED) and all(item["identical"] for item in preservation) else "FAIL",
        "changed_existing": records,
        "added_helpers": helper_records,
        "phone_proven_preservation": preservation,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "changed": changed, "added": added, "protected": len(preservation)}, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
