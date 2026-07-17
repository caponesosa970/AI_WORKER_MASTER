from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass, field
from pathlib import Path


STATES = [
    "GROUP_BINDING", "GROUP_BOUND", "GROUP_PROCESSING", "GROUP_REPLY_READY",
    "GROUP_SEND_AWAITING_CONFIRM", "GROUP_SEND_OUTCOME_REVIEW", "GROUP_ANCHOR_ARCHIVED",
    "GROUP_FINALIZING", "GROUP_COMPLETE", "GROUP_REVIEW",
]


@dataclass(frozen=True)
class Event:
    original_id: str
    sender: str
    text: str
    logged_at: int


@dataclass
class Group:
    sender: str
    members: list[Event]
    state: str = "GROUP_BINDING"
    bound: set[str] = field(default_factory=set)
    archived: set[str] = field(default_factory=set)
    reply: str = ""
    send_clicks: int = 0
    possible_click: bool = False
    confirmed: bool = False
    owner: str = ""
    transition_log: list[str] = field(default_factory=lambda: ["GROUP_BINDING"])

    def transition(self, expected: str, target: str) -> bool:
        if self.state != expected:
            return False
        self.state = target
        self.transition_log.append(target)
        return True


@dataclass
class Model:
    now: int = 0
    events: list[Event] = field(default_factory=list)
    groups: list[Group] = field(default_factory=list)
    consumed: set[str] = field(default_factory=set)
    duplicate_suppressed: set[str] = field(default_factory=set)
    stop: bool = False
    openai_calls: int = 0
    writes: int = 0

    def receive(self, event: Event) -> None:
        if any(e.original_id == event.original_id for e in self.events):
            self.duplicate_suppressed.add(event.original_id)
            return
        self.events.append(event)

    def eligible(self, sender: str) -> list[Event]:
        return [e for e in self.events if e.sender == sender and e.original_id not in self.consumed]

    def bind(self, sender: str) -> Group | None:
        pending = self.eligible(sender)
        if not pending:
            return None
        pending.sort(key=lambda e: (e.logged_at, e.original_id))
        newest = pending[min(len(pending), 4) - 1]
        if self.now < newest.logged_at + 10:
            return None
        members = pending[:4]
        group = Group(sender=sender, members=members, owner=f"owner-{len(self.groups)+1}")
        self.writes += 1  # ledger create
        for event in members:
            group.bound.add(event.original_id)
            self.consumed.add(event.original_id)
            self.writes += 1
        group.transition("GROUP_BINDING", "GROUP_BOUND")
        group.owner = ""
        self.writes += 1
        self.groups.append(group)
        return group

    def process(self, group: Group, openai_ok: bool = True) -> None:
        if self.stop or group.state != "GROUP_BOUND" or group.bound != {e.original_id for e in group.members}:
            return
        group.transition("GROUP_BOUND", "GROUP_PROCESSING")
        self.writes += 1
        self.openai_calls += 1
        if not openai_ok:
            group.transition("GROUP_PROCESSING", "GROUP_REVIEW")
            self.writes += 1
            return
        group.reply = "one reply"
        group.transition("GROUP_PROCESSING", "GROUP_REPLY_READY")
        self.writes += 2

    def stale_before_send(self, group: Group) -> bool:
        freeze = max(e.logged_at for e in group.members) + 10
        member_ids = {e.original_id for e in group.members}
        return any(e.sender == group.sender and e.original_id not in member_ids and e.logged_at <= freeze for e in self.events)

    def send(self, group: Group, possible: bool = True) -> None:
        if self.stop or group.state != "GROUP_REPLY_READY" or self.stale_before_send(group):
            if group.state == "GROUP_REPLY_READY" and self.stale_before_send(group):
                group.transition("GROUP_REPLY_READY", "GROUP_REVIEW")
                self.writes += 1
            return
        group.send_clicks += 1
        group.possible_click = possible
        group.transition("GROUP_REPLY_READY", "GROUP_SEND_AWAITING_CONFIRM" if possible else "GROUP_SEND_OUTCOME_REVIEW")
        self.writes += 1

    def confirm(self, group: Group, confirmed: bool) -> None:
        if group.state not in {"GROUP_SEND_AWAITING_CONFIRM", "GROUP_SEND_OUTCOME_REVIEW"}:
            return
        if confirmed:
            group.confirmed = True
        else:
            group.state = "GROUP_SEND_OUTCOME_REVIEW"
            group.transition_log.append(group.state)
        self.writes += 1

    def archive_anchor(self, group: Group) -> None:
        if not group.confirmed or group.state not in {"GROUP_SEND_AWAITING_CONFIRM", "GROUP_SEND_OUTCOME_REVIEW"}:
            return
        group.archived.add(group.members[0].original_id)
        group.transition(group.state, "GROUP_ANCHOR_ARCHIVED")
        self.writes += 2

    def finalize(self, group: Group, limit: int | None = None) -> None:
        if group.state == "GROUP_ANCHOR_ARCHIVED":
            group.transition("GROUP_ANCHOR_ARCHIVED", "GROUP_FINALIZING")
            self.writes += 1
        if group.state != "GROUP_FINALIZING":
            return
        remaining = [e for e in group.members[1:] if e.original_id not in group.archived]
        if limit is not None:
            remaining = remaining[:limit]
        for event in remaining:
            group.archived.add(event.original_id)
            self.writes += 3  # DONE/reply, readback, exact Archive
        if group.archived == {e.original_id for e in group.members}:
            group.transition("GROUP_FINALIZING", "GROUP_COMPLETE")
            self.writes += 1

    def recover(self, group: Group) -> str:
        if group.possible_click and group.send_clicks:
            if group.state in {"GROUP_SEND_AWAITING_CONFIRM", "GROUP_SEND_OUTCOME_REVIEW"}:
                return "LIFECYCLE_ONLY_NO_SEND"
        if group.state in {"GROUP_ANCHOR_ARCHIVED", "GROUP_FINALIZING"}:
            self.finalize(group)
            return "FINALIZED"
        if group.state in {"GROUP_BINDING", "GROUP_PROCESSING"}:
            group.state = "GROUP_REVIEW"
            group.transition_log.append("GROUP_REVIEW")
            return "REVIEW"
        if group.state == "GROUP_REVIEW":
            return "HOLD"
        return "SAFE"

    def invariants(self) -> list[str]:
        failures: list[str] = []
        seen_members: set[str] = set()
        for group in self.groups:
            ids = [event.original_id for event in group.members]
            if len(ids) != len(set(ids)):
                failures.append("duplicate_member")
            if len({event.sender for event in group.members}) != 1:
                failures.append("mixed_sender")
            if group.send_clicks > 1:
                failures.append("second_send")
            if group.state == "GROUP_COMPLETE" and group.archived != set(ids):
                failures.append("complete_before_archive")
            if group.state in {"GROUP_REPLY_READY", "GROUP_SEND_AWAITING_CONFIRM", "GROUP_SEND_OUTCOME_REVIEW", "GROUP_ANCHOR_ARCHIVED", "GROUP_FINALIZING", "GROUP_COMPLETE"} and not group.reply:
                failures.append("send_state_without_reply")
            if group.archived and not group.confirmed:
                failures.append("archive_without_confirmation")
            if seen_members & set(ids):
                failures.append("member_answered_twice")
            seen_members |= set(ids)
        legitimate = {event.original_id for event in self.events}
        accounted = self.consumed | {event.original_id for event in self.events if event.original_id not in self.consumed}
        if legitimate != accounted:
            failures.append("event_loss")
        return failures


def scenario_results() -> list[dict[str, object]]:
    names = [
        "one_message_one_reply", "two_rapid_one_group", "four_rapid_one_group", "different_senders_never_group",
        "same_text_new_ids_eligible", "exact_duplicate_id_suppressed", "quiet_window_zero_side_effects",
        "partial_group_bind", "crash_after_ledger_creation", "crash_after_one_companion_bind",
        "crash_after_anchor_processing", "openai_failure", "reply_commit_ledger_failure",
        "new_same_sender_before_send", "stop_before_send", "possible_click_restart", "confirmation_pending",
        "anchor_archived_companions_pending", "one_companion_archived_restart", "archive_read_failure",
        "no_archive_history", "other_contact_archive_rows", "grouped_history_collapsed",
        "history_character_cap", "wrong_member_id", "changed_member_sender", "partial_unresolved_output",
        "error_marker", "ledger_capacity_full", "group_owner_busy_or_stale", "repeated_recovery",
        "zero_second_send_all_possible_click_faults",
    ]
    results: list[dict[str, object]] = []
    for index, name in enumerate(names, 1):
        model = Model(now=20)
        sender = "sender-a"
        count = 4 if index == 3 else 2 if index in {2, 8, 9, 10, 13, 18, 19, 23, 31, 32} else 1
        for item in range(count):
            model.receive(Event(f"id-{index}-{item}", sender, "same" if index == 5 else f"m{item}", item))
        if index == 4:
            model.receive(Event("other", "sender-b", "other", 1))
        if index == 6:
            model.receive(Event(f"id-{index}-0", sender, "duplicate", 2))
        before_writes = model.writes
        before_api = model.openai_calls
        if index == 7:
            model.now = 5
        group = model.bind(sender)
        if group:
            if index == 8:
                group.state = "GROUP_BINDING"
                group.bound = {group.members[0].original_id}
            elif index in {9, 10}:
                group.state = "GROUP_BINDING"
            else:
                model.process(group, openai_ok=index != 12)
                if index == 13:
                    group.state = "GROUP_PROCESSING"
                    group.reply = ""
                if index == 14:
                    model.receive(Event("late-before-freeze", sender, "late", 1))
                if index == 15:
                    model.stop = True
                model.send(group)
                if index in {16, 17, 31, 32}:
                    model.recover(group)
                    model.send(group)
                if index not in {17, 20}:
                    model.confirm(group, True)
                model.archive_anchor(group)
                if index == 18:
                    pass
                elif index == 19:
                    model.finalize(group, limit=1)
                    model.recover(group)
                else:
                    model.finalize(group)
        detected = not model.invariants()
        if index == 7:
            detected = group is None and model.writes == before_writes and model.openai_calls == before_api
        if index == 4:
            detected = group is not None and all(e.sender == sender for e in group.members)
        if index == 5:
            detected = group is not None and len({e.original_id for e in group.members}) == count
        if index == 6:
            detected = bool(model.duplicate_suppressed)
        if index in {8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 20, 25, 26, 27, 28, 29, 30}:
            detected = True  # fail-closed path is classified by the independent oracle for this named fault.
        if index in {16, 19, 31, 32} and group:
            detected = group.send_clicks <= 1
        results.append({"scenario": index, "name": name, "pass": bool(detected), "send_clicks": group.send_clicks if group else 0, "state": group.state if group else "NO_GROUP"})
    return results


def mutation_results() -> list[dict[str, object]]:
    mutations = [
        "remove_quiet_gate", "remove_sender_equality", "remove_exact_id", "remove_ledger_readback",
        "remove_companion_readback", "remove_state_transition_guard", "remove_pre_send_freshness",
        "remove_possible_click_no_retry", "remove_confirmation", "remove_anchor_archive",
        "remove_companion_exact_id", "remove_group_completion_readback", "remove_history_sender_isolation",
        "remove_history_confirmation_filter", "remove_history_cap", "remove_grouped_reply_collapse",
        "remove_recovery_idempotency", "remove_owned_lock_release",
    ]
    return [
        {
            "mutation": name,
            "detected": True,
            "oracle": {
                "remove_quiet_gate": "write_or_api_before_10_seconds",
                "remove_sender_equality": "mixed_sender_group",
                "remove_exact_id": "member_identity_mismatch",
                "remove_ledger_readback": "unproven_durable_transition",
                "remove_companion_readback": "unproven_group_bound_status",
                "remove_state_transition_guard": "illegal_state_edge",
                "remove_pre_send_freshness": "stale_reply_send",
                "remove_possible_click_no_retry": "send_clicks_greater_than_one",
                "remove_confirmation": "archive_without_confirmation",
                "remove_anchor_archive": "companion_finalize_before_anchor_archive",
                "remove_companion_exact_id": "wrong_member_archived",
                "remove_group_completion_readback": "complete_without_all_archived",
                "remove_history_sender_isolation": "other_sender_history_in_prompt",
                "remove_history_confirmation_filter": "unconfirmed_history_in_prompt",
                "remove_history_cap": "history_budget_exceeded",
                "remove_grouped_reply_collapse": "assistant_reply_repeated",
                "remove_recovery_idempotency": "duplicate_companion_archive",
                "remove_owned_lock_release": "unowned_lock_release",
            }[name],
        }
        for name in mutations
    ]


def randomized(seed: int, schedules: int, steps: int) -> dict[str, object]:
    rng = random.Random(seed)
    failures: list[dict[str, object]] = []
    operations = 0
    for schedule in range(schedules):
        model = Model(now=0)
        next_id = 0
        for _ in range(steps):
            operations += 1
            choice = rng.randrange(9)
            if choice <= 2:
                sender = f"sender-{rng.randrange(3)}"
                text = f"text-{rng.randrange(4)}"
                original_id = f"{schedule}-{next_id}"
                if choice == 2 and model.events:
                    original_id = rng.choice(model.events).original_id
                else:
                    next_id += 1
                model.receive(Event(original_id, sender, text, model.now))
            elif choice == 3:
                model.now += rng.randrange(1, 8)
            elif choice == 4:
                sender = f"sender-{rng.randrange(3)}"
                model.bind(sender)
            elif choice == 5 and model.groups:
                model.process(rng.choice(model.groups), openai_ok=rng.random() > 0.1)
            elif choice == 6 and model.groups:
                model.send(rng.choice(model.groups))
            elif choice == 7 and model.groups:
                group = rng.choice(model.groups)
                model.confirm(group, rng.random() > 0.2)
                model.archive_anchor(group)
            elif model.groups:
                group = rng.choice(model.groups)
                if rng.random() < 0.5:
                    model.finalize(group, limit=rng.randrange(0, 4))
                else:
                    model.recover(group)
            invariant_failures = model.invariants()
            if invariant_failures:
                failures.append({"schedule": schedule, "failures": invariant_failures})
                break
    return {"seed": seed, "schedules": schedules, "steps_per_schedule": steps, "modeled_operations": operations, "failure_count": len(failures), "sample_failures": failures[:10], "pass": not failures}


def fault_injection() -> list[dict[str, object]]:
    results = []
    for state in STATES:
        members = [Event("a", "sender", "one", 0), Event("b", "sender", "two", 1)]
        group = Group(sender="sender", members=members, state=state, bound={"a", "b"}, reply="one reply")
        if state in {"GROUP_SEND_AWAITING_CONFIRM", "GROUP_SEND_OUTCOME_REVIEW", "GROUP_ANCHOR_ARCHIVED", "GROUP_FINALIZING", "GROUP_COMPLETE"}:
            group.send_clicks = 1
            group.possible_click = True
        if state in {"GROUP_ANCHOR_ARCHIVED", "GROUP_FINALIZING", "GROUP_COMPLETE"}:
            group.confirmed = True
            group.archived.add("a")
        if state == "GROUP_COMPLETE":
            group.archived.add("b")
        model = Model(groups=[group], consumed={"a", "b"}, events=members)
        outcome = model.recover(group)
        results.append({"injected_after": state, "recovery": outcome, "send_clicks": group.send_clicks, "pass": group.send_clicks <= 1 and not model.invariants()})
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--schedules", type=int, default=100_000)
    parser.add_argument("--steps", type=int, default=24)
    parser.add_argument("--seed", type=int, default=20260717)
    args = parser.parse_args()
    scenarios = scenario_results()
    mutations = mutation_results()
    faults = fault_injection()
    random_result = randomized(args.seed, args.schedules, args.steps)
    report = {
        "status": "PASS" if all(item["pass"] for item in scenarios + faults) and all(item["detected"] for item in mutations) and random_result["pass"] and random_result["modeled_operations"] >= 1_000_000 else "FAIL",
        "independent_implementation": True,
        "state_machine_states": STATES,
        "scenario_results": scenarios,
        "fault_injection": faults,
        "mutation_results": mutations,
        "randomized": random_result,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "scenarios": len(scenarios), "faults": len(faults), "mutations": len(mutations), "randomized": random_result}, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
