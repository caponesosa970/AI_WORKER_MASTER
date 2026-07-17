from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


def raw_task(text: str, task_id: int) -> str:
    match = re.search(rf'<Task sr="task{task_id}".*?</Task>', text, re.DOTALL)
    if not match:
        raise RuntimeError(f"missing task {task_id}")
    return match.group(0)


def task_element(text: str, task_id: int) -> ET.Element:
    return ET.fromstring(raw_task(text, task_id))


def mutate_task(text: str, task_id: int, old: str, new: str, count: int = -1) -> str:
    block = raw_task(text, task_id)
    mutated = block.replace(old, new, count)
    return text.replace(block, mutated, 1)


def decoded(task: ET.Element) -> str:
    return "\n".join(value for node in task.iter() if (value := node.text))


def performs(task: ET.Element) -> list[str]:
    return [action.findtext("Str[@sr='arg0']", "") for action in task.findall("Action") if action.findtext("code") == "130"]


def detector(name: str, xml_text: str, migration: str) -> bool:
    t263 = task_element(xml_text, 263)
    t282 = task_element(xml_text, 282)
    t309 = task_element(xml_text, 309)
    t317 = task_element(xml_text, 317)
    t320 = task_element(xml_text, 320)
    t327 = task_element(xml_text, 327)
    d263, d309, d317, d320, d327 = map(decoded, (t263, t309, t317, t320, t327))
    if name == "journaled_only_member_contract":
        return "^(RESOLVED_MAIN|RESOLVED_OVERFLOW)$" in d309 and "JOURNALED" not in d309
    if name == "arbitrary_journal_status":
        return ".*ARBITRARY_STATUS.*" not in d309 and "^(RESOLVED_MAIN|RESOLVED_OVERFLOW)$" in d309
    if name == "remove_exact_one_match":
        return all(f"%cgq_idmatch{i}" in d309 and f"%cgq_valid{i}" in d309 for i in range(1, 5))
    if name == "active_lifecycle_busy_hold":
        return "CONVERSATION_GROUP_LIFECYCLE_ONLY" in d317 and "CONVERSATION_ACTIVE_GROUP_BUSY_HOLD" not in d317
    if name == "restore_task263_starvation":
        calls = performs(t282)
        return calls and calls[0] == "AIW Conversation Prepare Group" and calls[1] == "PROCESS Queue Health"
    if name == "remove_quiet_recheck_schedule":
        return performs(t263).count("AIW Conversation Deferred Recheck") == 1
    if name == "hold_lock_while_waiting":
        return not ({"AIW Queue Owner", "AIW Conversation Owner", "PROCESS Lock Acquire"} & set(performs(t327)))
    if name == "duplicate_deferred_waiters":
        return t327.findtext("rty") == "1"
    if name == "remove_stop_cancellation":
        return "%AIWStopRequested" in d327 and "%AIWorkerOn" in d327 and "CONVERSATION_QUIET_RECHECK_CANCELLED_STOP" in d327
    if name == "omit_required_migration_formula":
        return '=IFERROR(MATCH(TRUE,INDEX(ConversationGroups!A2:A1000="",0),0)+1,"FULL")' in migration and "TEXTJOIN(\"|\",FALSE,ConversationGroups!A1:AP1)" in migration
    if name == "historical_resolved_global_stale":
        return "PROCESS Load Queue Globals" in d320 and "OverflowInbox" in d320 and "A2:N%AIWConversationJournalMax" in d320
    raise KeyError(name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("migration", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    xml = args.candidate.read_text(encoding="utf-8")
    migration = args.migration.read_text(encoding="utf-8")
    mutations = [
        ("journaled_only_member_contract", lambda x: mutate_task(x, 309, "^(RESOLVED_MAIN|RESOLVED_OVERFLOW)$", "JOURNALED", 1), lambda m: m),
        ("arbitrary_journal_status", lambda x: mutate_task(x, 309, "^(RESOLVED_MAIN|RESOLVED_OVERFLOW)$", ".*ARBITRARY_STATUS.*", 1), lambda m: m),
        ("remove_exact_one_match", lambda x: mutate_task(x, 309, "%cgq_idmatch1", "%removed_idmatch1"), lambda m: m),
        ("active_lifecycle_busy_hold", lambda x: mutate_task(x, 317, "CONVERSATION_GROUP_LIFECYCLE_ONLY", "CONVERSATION_ACTIVE_GROUP_BUSY_HOLD", 1), lambda m: m),
        ("restore_task263_starvation", lambda x: mutate_task(x, 282, "AIW Conversation Prepare Group", "AIW Removed Lifecycle Gate", 1), lambda m: m),
        ("remove_quiet_recheck_schedule", lambda x: mutate_task(x, 263, "AIW Conversation Deferred Recheck", "AIW Removed Deferred Recheck", 1), lambda m: m),
        ("hold_lock_while_waiting", lambda x: mutate_task(x, 327, "AIW Integrated Queue Cycle", "AIW Queue Owner", 1), lambda m: m),
        ("duplicate_deferred_waiters", lambda x: mutate_task(x, 327, "<rty>1</rty>", "<rty>2</rty>", 1), lambda m: m),
        ("remove_stop_cancellation", lambda x: mutate_task(x, 327, "%AIWStopRequested", "%RemovedStopRequested"), lambda m: m),
        ("omit_required_migration_formula", lambda x: x, lambda m: m.replace('=IFERROR(MATCH(TRUE,INDEX(ConversationGroups!A2:A1000="",0),0)+1,"FULL")', "FORMULA_REMOVED")),
        ("historical_resolved_global_stale", lambda x: mutate_task(x, 320, "PROCESS Load Queue Globals", "REMOVED_ACTIVE_QUEUE_AUTHORITY", 1), lambda m: m),
    ]
    results: list[dict[str, object]] = []
    for name, mutate_xml, mutate_migration in mutations:
        mutated_xml = mutate_xml(xml)
        mutated_migration = mutate_migration(migration)
        changed = mutated_xml != xml or mutated_migration != migration
        detected = changed and not detector(name, mutated_xml, mutated_migration)
        results.append({"mutation": name, "applied": changed, "detected": detected})
    report = {
        "status": "PASS" if all(item["applied"] and item["detected"] for item in results) else "FAIL",
        "independent_mutation_harness": True,
        "results": results,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "mutations": len(results), "undetected": [item["mutation"] for item in results if not item["detected"]]}, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
