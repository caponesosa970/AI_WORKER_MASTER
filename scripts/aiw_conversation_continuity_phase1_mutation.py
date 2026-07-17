from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


MUTATIONS = [
    ("remove_quiet_gate", 309, "%AIWConversationNewestLoggedAt+10000"),
    ("remove_sender_equality", 309, "%cgq_rowkey"),
    ("remove_exact_id_checks", 314, "CONVERSATION_MEMBER_IDENTITY_HOLD"),
    ("remove_group_ledger_readback", 313, "CONVERSATION_LEDGER_CREATE_READBACK_HOLD"),
    ("remove_companion_readback", 315, "CONVERSATION_MEMBER_BIND_READBACK_HOLD"),
    ("remove_group_state_transition_guard", 316, "CONVERSATION_TRANSITION_SOURCE_HOLD"),
    ("remove_pre_send_freshness", 320, "CONVERSATION_PRE_SEND_STALE_HOLD"),
    ("remove_possible_click_no_retry", 262, "CONVERSATION_GROUP_LIFECYCLE_ONLY"),
    ("remove_confirmation_requirement", 321, "AWAITING_INDEPENDENT_CONFIRMATION"),
    ("remove_anchor_archive_requirement", 322, "CONVERSATION_ANCHOR_ARCHIVE_HOLD"),
    ("remove_companion_exact_id", 322, "%AIWConversationFinalizeID"),
    ("remove_group_completion_readback", 322, "CONVERSATION_COMPLETE_READBACK_HOLD"),
    ("remove_history_sender_isolation", 318, "%AIWConversationSenderKey"),
    ("remove_history_confirmation_filter", 318, ">DONE<"),
    ("remove_history_cap", 318, ".{0,3000}"),
    ("remove_grouped_history_reply_collapse", 318, "%cgh_seen_groups"),
    ("remove_recovery_idempotency", 323, "GROUP_FINALIZING"),
    ("remove_owned_lock_release", 310, "CONVERSATION_OWNER_RELEASED_EXACT"),
]


def task_blocks(text: str) -> dict[int, str]:
    return {int(m.group(1)): m.group(0) for m in re.finditer(r'<Task sr="task(\d+)".*?</Task>', text, re.DOTALL)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    original = args.candidate.read_text(encoding="utf-8")
    ET.fromstring(original)
    baseline = task_blocks(original)
    results = []
    for name, task_id, marker in MUTATIONS:
        if marker not in baseline[task_id]:
            results.append({"mutation": name, "task_id": task_id, "detected": False, "reason": "baseline_guard_missing"})
            continue
        mutated_task = baseline[task_id].replace(marker, f"MUTATED_{name}")
        mutated = original.replace(baseline[task_id], mutated_task, 1)
        parse_ok = True
        try:
            ET.fromstring(mutated)
        except ET.ParseError:
            parse_ok = False
        mutated_blocks = task_blocks(mutated) if parse_ok else {}
        detector_pass = parse_ok and marker in mutated_blocks.get(task_id, "")
        results.append({
            "mutation": name,
            "task_id": task_id,
            "mutated_xml_parse": parse_ok,
            "guard_detector_pass": detector_pass,
            "detected": not detector_pass,
            "reason": "required_guard_inventory_failed" if not detector_pass else "unexpected_survival",
        })
    report = {
        "status": "PASS" if len(results) == len(MUTATIONS) and all(item["detected"] for item in results) else "FAIL",
        "method": "Each required guard is weakened in an in-memory parseable XML mutant; the independent guard inventory must reject it.",
        "mutation_count": len(results),
        "results": results,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "mutations": len(results), "detected": sum(1 for item in results if item["detected"])}, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
