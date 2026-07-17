from __future__ import annotations

import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path


def sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("xml", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("task_ids", nargs="+", type=int)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    root = ET.fromstring(args.xml.read_bytes())
    tasks = {int(task.findtext("id", "-1")): task for task in root.findall("Task")}
    for task_id in args.task_ids:
        task = tasks[task_id]
        records = []
        for action in sorted(task.findall("Action"), key=lambda node: int((node.get("sr") or "act-1").replace("act", ""))):
            strings = {node.get("sr", ""): node.text or "" for node in action.findall("Str")}
            integers = {node.get("sr", ""): node.get("val") for node in action.findall("Int")}
            conditions = []
            for condition in action.findall("ConditionList/Condition"):
                conditions.append(
                    {
                        "lhs": condition.findtext("lhs"),
                        "op": condition.findtext("op"),
                        "rhs": condition.findtext("rhs"),
                    }
                )
            params = action.findtext("Bundle/Vals/parameters")
            blurb = action.findtext("Bundle/Vals/com.twofortyfouram.locale.intent.extra.BLURB")
            records.append(
                {
                    "sr": action.get("sr"),
                    "code": int(action.findtext("code", "-1")),
                    "label": action.findtext("label"),
                    "se": action.findtext("se"),
                    "strings": strings,
                    "integers": integers,
                    "conditions": conditions,
                    "plugin_blurb": blurb,
                    "plugin_parameters_sha256": sha256(params) if params else None,
                }
            )
        output = {
            "id": task_id,
            "name": task.findtext("nme"),
            "rty": task.findtext("rty"),
            "priority": task.findtext("pri"),
            "stay_awake": task.findtext("stayawake"),
            "action_count": len(records),
            "actions": records,
        }
        (args.out_dir / f"TASK_{task_id}.json").write_text(
            json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"TASK={task_id}|NAME={output['name']}|ACTIONS={len(records)}")


if __name__ == "__main__":
    main()
