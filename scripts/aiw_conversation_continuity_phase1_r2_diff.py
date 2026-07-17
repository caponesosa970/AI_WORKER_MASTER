from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import aiw_conversation_continuity_phase1_r1_diff as r1diff


AUTHORIZED = {273, 320, 325}


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


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
    base_tasks = r1diff.task_map(base_root)
    candidate_tasks = r1diff.task_map(candidate_root)
    base_raw = r1diff.blocks(base_text, "Task", r"<id>(\d+)</id>")
    candidate_raw = r1diff.blocks(candidate_text, "Task", r"<id>(\d+)</id>")
    changed = sorted(i for i in base_raw if base_raw[i] != candidate_raw.get(i))
    added = sorted(set(candidate_raw) - set(base_raw))

    deltas: list[dict[str, object]] = []
    for task_id in changed:
        before = [r1diff.normalized_action(a) for a in r1diff.actions(base_tasks[task_id])]
        after = [r1diff.normalized_action(a) for a in r1diff.actions(candidate_tasks[task_id])]
        matcher = __import__("difflib").SequenceMatcher(a=before, b=after, autojunk=False)
        ranges = []
        for operation, i1, i2, j1, j2 in matcher.get_opcodes():
            if operation == "equal":
                continue
            ranges.append({
                "operation": operation,
                "base_actions": [i1, i2 - 1] if i2 > i1 else [],
                "candidate_actions": [j1, j2 - 1] if j2 > j1 else [],
            })
        deltas.append({
            "task_id": task_id,
            "name": candidate_tasks[task_id].findtext("nme", ""),
            "base_action_count": len(before),
            "candidate_action_count": len(after),
            "base_raw_sha256": digest(base_raw[task_id]),
            "candidate_raw_sha256": digest(candidate_raw[task_id]),
            "aligned_changed_ranges": ranges,
            "candidate_action_inventory": [r1diff.action_detail(a) for a in r1diff.actions(candidate_tasks[task_id])],
        })

    report = {
        "status": "PASS" if changed == sorted(AUTHORIZED) and not added else "FAIL",
        "changed_existing": changed,
        "added_tasks": added,
        "task_deltas": deltas,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "changed": changed, "added": added}, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
