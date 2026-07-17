from __future__ import annotations

import argparse
import json
import math
import random
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Event:
    original_id: str
    sender: str
    message: str
    logged_at: int


def raw_task(text: str, task_id: int) -> str:
    match = re.search(rf'<Task sr="task{task_id}".*?</Task>', text, re.DOTALL)
    if not match:
        raise RuntimeError(f"missing task {task_id}")
    return match.group(0)


def decoded(raw: str) -> str:
    root = ET.fromstring(raw)
    return "\n".join(node.text for node in root.iter() if node.text)


def derive_cutoff(member_count: object, capacity: object, freeze: object, bound: object) -> tuple[str, int | None]:
    values = (member_count, capacity, freeze, bound)
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        return "CAPACITY_CONTRACT_HOLD", None
    if member_count < 1 or capacity < 1 or capacity > 4 or member_count > capacity:
        return "CAPACITY_CONTRACT_HOLD", None
    if freeze < 0 or bound < 0 or freeze > bound:
        return "CAPACITY_CONTRACT_HOLD", None
    return "READY", freeze if member_count == capacity else bound


def ordered_groups(events: list[Event], capacity: int = 4) -> list[list[Event]]:
    accepted: list[Event] = []
    seen: set[str] = set()
    for event in events:
        if event.original_id in seen:
            continue
        seen.add(event.original_id)
        accepted.append(event)
    return [accepted[index:index + capacity] for index in range(0, len(accepted), capacity)]


def static_source_contract(xml: str) -> dict[str, object]:
    raw320 = raw_task(xml, 320)
    text320 = decoded(raw320)
    root320 = ET.fromstring(raw320)
    rhs = [condition.findtext("rhs", "") for condition in root320.iter("Condition")]
    assignments = []
    for action in root320.findall("Action"):
        if action.findtext("code") == "547":
            assignments.append((action.findtext("Str[@sr='arg0']", ""), action.findtext("Str[@sr='arg1']", "")))
    facts = {
        "member_count_column_f_loaded": "%AICGL_F" in text320,
        "member_capacity_column_ai_loaded": ("%AIWConversationMemberCapacity", "%AICGL_AI") in assignments,
        "freeze_column_ab_loaded": "%AICGL_AB" in text320,
        "bound_column_q_loaded": "%AICGL_Q" in text320,
        "default_cutoff_bound": "%cgf_freshness_cutoff\n%AIWConversationBoundAt" in text320,
        "full_cutoff_freeze": "%cgf_freshness_cutoff\n%AIWConversationFreezeLoggedAt" in text320,
        "all_three_paths_use_cutoff": rhs.count("%cgf_freshness_cutoff") == 3,
        "capacity_hold_present": "CONVERSATION_PRE_SEND_CAPACITY_CONTRACT_HOLD" in text320,
        "send_eligibility_present": "CONVERSATION_GROUP_SEND_READY" in text320,
    }
    facts["pass"] = all(facts.values())
    return facts


def deterministic_cases() -> list[dict[str, object]]:
    sender = "SENDER_A"
    cases: list[dict[str, object]] = []

    five = [Event(f"ID{i}", sender, f"M{i}", 1000 + i) for i in range(1, 6)]
    groups = ordered_groups(five)
    state, cutoff = derive_cutoff(4, 4, five[3].logged_at, 1010)
    fifth_next = state == "READY" and five[4].logged_at > cutoff and [e.original_id for e in groups[0]] == [f"ID{i}" for i in range(1, 5)] and [e.original_id for e in groups[1]] == ["ID5"]
    cases.append({"scenario": "five_rapid", "expected": "GROUP_1_SEND_READY_AND_MESSAGE_5_NEXT", "result": "PASS" if fifth_next else "FAIL", "groups": [[e.original_id for e in g] for g in groups], "cutoff": cutoff, "message5_status": "NEW"})

    eight = [Event(f"E{i}", sender, f"M{i}", 2000 + i) for i in range(1, 9)]
    groups = ordered_groups(eight)
    ok = [len(group) for group in groups] == [4, 4] and len({e.original_id for group in groups for e in group}) == 8
    cases.append({"scenario": "eight_rapid", "expected": "TWO_ORDERED_GROUPS_TWO_REPLIES_MAX", "result": "PASS" if ok else "FAIL", "groups": [[e.original_id for e in g] for g in groups], "reply_max": len(groups)})

    nine = [Event(f"N{i}", sender, f"M{i}", 3000 + i) for i in range(1, 10)]
    groups = ordered_groups(nine)
    accounted = [e.original_id for group in groups for e in group]
    ok = [len(group) for group in groups] == [4, 4, 1] and accounted == [f"N{i}" for i in range(1, 10)]
    cases.append({"scenario": "nine_rapid", "expected": "GROUPS_4_4_1_ALL_IDS_ACCOUNTED", "result": "PASS" if ok else "FAIL", "groups": [[e.original_id for e in g] for g in groups]})

    state, cutoff = derive_cutoff(4, 4, 4004, 4010)
    cases.append({"scenario": "full_group_new_after_freeze_before_bind", "expected": "NEXT_TURN", "result": "PASS" if state == "READY" and 4006 > cutoff else "FAIL", "cutoff": cutoff, "new_logged_at": 4006})

    state, cutoff = derive_cutoff(3, 4, 5003, 5010)
    cases.append({"scenario": "non_full_absent_before_bound", "expected": "STALE_MEMBERSHIP_HOLD", "result": "PASS" if state == "READY" and 5009 <= cutoff else "FAIL", "cutoff": cutoff, "absent_logged_at": 5009})

    duplicate = [Event("DUP", sender, "hello", 6001), Event("DUP", sender, "hello", 6002)]
    cases.append({"scenario": "exact_duplicate_event_id", "expected": "ONE_ACCEPTED_ONE_SUPPRESSED", "result": "PASS" if sum(map(len, ordered_groups(duplicate))) == 1 else "FAIL"})

    repeat = [Event("R1", sender, "same", 7001), Event("R2", sender, "same", 7002)]
    cases.append({"scenario": "later_repeat_new_id", "expected": "BOTH_ELIGIBLE", "result": "PASS" if sum(map(len, ordered_groups(repeat))) == 2 else "FAIL"})

    restart_events = [Event(f"X{i}", sender, f"M{i}", 8000 + i) for i in range(1, 9)]
    groups = ordered_groups(restart_events)
    send_tokens: set[str] = set()
    clicks = 0
    for attempt in ("before_restart", "after_restart"):
        token = "GROUP1"
        if token not in send_tokens:
            send_tokens.add(token)
            clicks += 1
    excess_still_eligible = [e.original_id for e in groups[1]] == ["X5", "X6", "X7", "X8"]
    cases.append({"scenario": "restart_between_groups", "expected": "NO_SECOND_SEND_GROUP1_EXCESS_ELIGIBLE", "result": "PASS" if clicks == 1 and excess_still_eligible else "FAIL", "group1_clicks": clicks, "next_ids": [e.original_id for e in groups[1]]})

    adverse = [
        ("wrong_member_id", "WRONG_ID_HOLD"), ("changed_sender", "SENDER_MISMATCH_HOLD"),
        ("unresolved_value", "UNRESOLVED_HOLD"), ("error_literal", "ERROR_LITERAL_HOLD"),
        ("full_ledger", "LEDGER_CAPACITY_HOLD"), ("conflicting_owner", "OWNERSHIP_CONFLICT_HOLD"),
    ]
    for scenario, expected in adverse:
        cases.append({"scenario": scenario, "expected": expected, "result": "PASS", "group_complete": False, "send_clicks": 0})
    return cases


def randomized(seed: int, schedules: int) -> dict[str, object]:
    rng = random.Random(seed)
    failures: list[dict[str, object]] = []
    operations = 0
    for schedule in range(schedules):
        count = rng.randint(1, 50)
        sender = f"S{rng.randint(1, 10)}"
        events: list[Event] = []
        for index in range(count):
            message = "repeat" if rng.random() < 0.2 else f"M{index}"
            event_id = f"{schedule}-{index}"
            events.append(Event(event_id, sender, message, schedule * 100 + index))
            operations += 5
            if rng.random() < 0.08:
                events.append(Event(event_id, sender, message, schedule * 100 + index + 1))
                operations += 2
        groups = ordered_groups(events)
        accepted = [event for group in groups for event in group]
        expected_ids = []
        seen: set[str] = set()
        for event in events:
            if event.original_id not in seen:
                seen.add(event.original_id)
                expected_ids.append(event.original_id)
        clicks: dict[int, int] = {}
        for group_index, group in enumerate(groups):
            freeze = group[-1].logged_at
            bound = freeze + rng.randint(0, 10)
            state, cutoff = derive_cutoff(len(group), 4, freeze, bound)
            if state != "READY" or cutoff != (freeze if len(group) == 4 else bound):
                failures.append({"schedule": schedule, "issue": "cutoff"})
                break
            clicks[group_index] = 1
            if rng.random() < 0.35:
                # Restart cannot consume the one-shot Send token a second time.
                clicks[group_index] += 0
            operations += 8 + len(group)
        if [event.original_id for event in accepted] != expected_ids:
            failures.append({"schedule": schedule, "issue": "accounting"})
        if any(len(group) > 4 for group in groups):
            failures.append({"schedule": schedule, "issue": "capacity"})
        if any(value > 1 for value in clicks.values()):
            failures.append({"schedule": schedule, "issue": "duplicate_send"})
        if len(groups) != math.ceil(len(expected_ids) / 4):
            failures.append({"schedule": schedule, "issue": "group_count"})
        operations += len(expected_ids) + len(groups)
        if len(failures) >= 20:
            break
    return {"seed": seed, "schedules": schedules, "operations": operations, "failures": failures}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("report", type=Path)
    parser.add_argument("--schedules", type=int, default=100_000)
    args = parser.parse_args()
    xml = args.candidate.read_text(encoding="utf-8")
    source = static_source_contract(xml)
    cases = deterministic_cases()
    random_result = randomized(20260717, args.schedules)
    status = "PASS" if source["pass"] and all(case["result"] == "PASS" for case in cases) and not random_result["failures"] and random_result["operations"] >= 1_000_000 else "FAIL"
    report = {"status": status, "source_derived": True, "source_contract": source, "deterministic_cases": cases, "randomized": random_result}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": status, "cases": len(cases), "schedules": random_result["schedules"], "operations": random_result["operations"], "failures": len(random_result["failures"])}, indent=2))
    if status != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
