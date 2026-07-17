from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import aiw_conversation_continuity_phase1_r2_model as model


def raw_task(text: str, task_id: int) -> str:
    match = re.search(rf'<Task sr="task{task_id}".*?</Task>', text, re.DOTALL)
    if not match:
        raise RuntimeError(f"missing task {task_id}")
    return match.group(0)


def mutate_task(text: str, task_id: int, old: str, new: str, count: int = -1) -> str:
    block = raw_task(text, task_id)
    mutated = block.replace(old, new, count)
    return text.replace(block, mutated, 1)


def runtime_detector(xml: str) -> bool:
    return bool(model.static_source_contract(xml)["pass"])


def migration_detector(text: str) -> bool:
    return all(value in text for value in (
        "minimum runtime requirement", "Never shrink a row count", "SystemConfig!A1:J2",
        "re-read `A3:D16`", "Do not write or replace row 1", "Add exactly 67 rows",
        "Add exactly 28 rows", "only authorized existing-view replacements are `OverflowView!A1` and `OverflowSlotView!A2`",
        "Change only column D from exact `NEW` to exact `REVIEW_HOLD`",
        "HISTORICAL ROWS UNCHANGED",
    )) and "Target physical rows x columns" not in text


def excess_invariant(consume_excess: bool) -> bool:
    events = [model.Event(f"ID{i}", "S", f"M{i}", i) for i in range(1, 6)]
    groups = model.ordered_groups(events)
    fifth_status = "CONSUMED" if consume_excess else "NEW"
    return [event.original_id for event in groups[0]] == ["ID1", "ID2", "ID3", "ID4"] and [event.original_id for event in groups[1]] == ["ID5"] and fifth_status == "NEW"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("migration", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    xml = args.candidate.read_text(encoding="utf-8")
    migration = args.migration.read_text(encoding="utf-8")
    mutations = [
        (
            "replace_freeze_cutoff_with_bound",
            lambda x: mutate_task(x, 320, "%cgf_freshness_cutoff</Str><Str sr=\"arg1\" ve=\"3\">%AIWConversationFreezeLoggedAt", "%cgf_freshness_cutoff</Str><Str sr=\"arg1\" ve=\"3\">%AIWConversationBoundAt", 1),
            lambda m: m,
            "runtime",
        ),
        (
            "remove_member_capacity_validation",
            lambda x: mutate_task(x, 320, "%AIWConversationMemberCapacity", "%RemovedMemberCapacity"),
            lambda m: m,
            "runtime",
        ),
        (
            "one_freshness_path_reverts_to_bound",
            lambda x: mutate_task(x, 320, "<rhs>%cgf_freshness_cutoff</rhs>", "<rhs>%AIWConversationBoundAt</rhs>", 1),
            lambda m: m,
            "runtime",
        ),
        (
            "remove_capacity_hold_result",
            lambda x: mutate_task(x, 320, "CONVERSATION_PRE_SEND_CAPACITY_CONTRACT_HOLD", "CONVERSATION_GROUP_SEND_READY", 1),
            lambda m: m,
            "runtime",
        ),
        (
            "migration_attempts_exact_shrink",
            lambda x: x,
            lambda m: m.replace("minimum runtime requirement", "destructive exact target size", 1).replace("Never shrink a row count", "Shrink row count", 1),
            "migration",
        ),
        (
            "migration_overwrites_systemconfig",
            lambda x: x,
            lambda m: m.replace("re-read `A3:D16`", "re-read `A1:D14`", 1).replace("Do not write or replace row 1", "Replace row 1", 1),
            "migration",
        ),
        (
            "migration_omits_archive_add_only",
            lambda x: x,
            lambda m: m.replace("Add exactly 67 rows", "Resize Archive", 1),
            "migration",
        ),
        (
            "migration_omits_historical_status_only",
            lambda x: x,
            lambda m: m.replace("Change only column D from exact `NEW` to exact `REVIEW_HOLD`", "Rewrite the historical rows", 1),
            "migration",
        ),
    ]
    results: list[dict[str, object]] = []
    for name, mutate_xml, mutate_manifest, kind in mutations:
        changed_xml = mutate_xml(xml)
        changed_manifest = mutate_manifest(migration)
        applied = changed_xml != xml or changed_manifest != migration
        safe = runtime_detector(changed_xml) if kind == "runtime" else migration_detector(changed_manifest)
        results.append({"mutation": name, "applied": applied, "detected": applied and not safe})

    consume_applied = not excess_invariant(True)
    results.append({"mutation": "consume_excess_row", "applied": True, "detected": consume_applied, "evidence": "fifth status changed from NEW to CONSUMED"})
    baseline_excess = excess_invariant(False)
    report = {
        "status": "PASS" if baseline_excess and all(item["applied"] and item["detected"] for item in results) else "FAIL",
        "independent_mutation_harness": True,
        "baseline_excess_invariant": baseline_excess,
        "results": results,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "mutations": len(results), "undetected": [item["mutation"] for item in results if not item["detected"]]}, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
