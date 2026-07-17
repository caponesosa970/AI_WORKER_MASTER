from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass, field
from pathlib import Path


LIFECYCLE_STATES = {
    "GROUP_REPLY_READY", "GROUP_SEND_AWAITING_CONFIRM", "GROUP_SEND_OUTCOME_REVIEW",
    "GROUP_ANCHOR_ARCHIVED", "GROUP_FINALIZING",
}
TERMINAL_STATES = {"GROUP_COMPLETE", "GROUP_REVIEW"}
ADMITTED = {"RESOLVED_MAIN", "RESOLVED_OVERFLOW"}


@dataclass
class JournalRow:
    original_id: str
    sender: str
    message: str
    logged_at: int
    status: str = "JOURNALED"
    source: str = "TEXTNOW"


@dataclass
class ActiveRow:
    original_id: str
    sender: str
    message: str
    location: str
    status: str = "NEW"


@dataclass
class Group:
    sender: str
    member_ids: list[str]
    state: str
    possible_click: bool = False
    send_clicks: int = 0
    confirmed: bool = False
    anchor_archived: bool = False
    companions_done: int = 0


@dataclass
class Runtime:
    now: int = 0
    journal: list[JournalRow] = field(default_factory=list)
    active_rows: list[ActiveRow] = field(default_factory=list)
    group: Group | None = None
    stop_requested: bool = False
    openai_calls: int = 0
    sheet_writes: int = 0
    ledger_writes: int = 0
    task262_calls: int = 0
    deferred_waiters: int = 0
    deferred_cutoff: int | None = None
    deferred_sender: str = ""
    last_process_result: str = ""
    duplicate_suppressed: int = 0

    def receive(self, row: JournalRow) -> None:
        if any(existing.original_id == row.original_id for existing in self.journal):
            self.duplicate_suppressed += 1
            return
        self.journal.append(row)

    def drain_journal_once(self, overflow: bool = False) -> None:
        for journal in self.journal:
            if journal.status == "JOURNALED":
                journal.status = "RESOLVED_OVERFLOW" if overflow else "RESOLVED_MAIN"
                location = "OverflowInbox" if overflow else "Sheet1"
                self.active_rows.append(ActiveRow(journal.original_id, journal.sender, journal.message, location))
                self.sheet_writes += 1
                return

    def drain_overflow_once(self) -> None:
        for row in self.active_rows:
            if row.location == "OverflowInbox" and row.status == "NEW":
                row.location = "Sheet1"
                self.sheet_writes += 1
                return

    def exact_journal_contract(self, active: ActiveRow) -> bool:
        matches = [row for row in self.journal if row.original_id == active.original_id]
        return (
            len(matches) == 1
            and matches[0].status in ADMITTED
            and matches[0].source == "TEXTNOW"
            and matches[0].sender == active.sender
            and matches[0].message == active.message
            and isinstance(matches[0].logged_at, int)
            and matches[0].logged_at >= 0
        )

    def schedule_quiet_recheck(self, sender: str, cutoff: int) -> None:
        # Abort-existing collision semantics leave exactly one current waiter.
        self.deferred_waiters = 1
        self.deferred_sender = sender
        self.deferred_cutoff = cutoff

    def process_one(self) -> str:
        # Task 282 first invokes the LIFECYCLE_GATE before QueueView selection.
        if self.group and self.group.state in LIFECYCLE_STATES:
            self.last_process_result = "CONVERSATION_GROUP_LIFECYCLE_ONLY"
            return self.last_process_result
        if self.group and self.group.state == "GROUP_REVIEW":
            self.last_process_result = "CONVERSATION_GROUP_REVIEW_ONLY"
            return self.last_process_result
        if self.group and self.group.state not in TERMINAL_STATES:
            self.last_process_result = "CONVERSATION_ACTIVE_GROUP_RECOVERY_HOLD"
            return self.last_process_result

        pending = [row for row in self.active_rows if row.location == "Sheet1" and row.status == "NEW"]
        if not pending:
            self.last_process_result = "PROCESS_NO_ELIGIBLE_ROW_HOLD"
            return self.last_process_result
        anchor = pending[0]
        same_sender = [row for row in pending if row.sender == anchor.sender][:4]
        contracts = [next((journal for journal in self.journal if journal.original_id == row.original_id), None) for row in same_sender]
        if not all(self.exact_journal_contract(row) for row in same_sender):
            self.last_process_result = "CONVERSATION_JOURNAL_IDENTITY_HOLD"
            return self.last_process_result
        newest = max(row.logged_at for row in contracts if row is not None)
        cutoff = newest + 10
        if self.now < cutoff:
            self.schedule_quiet_recheck(anchor.sender, cutoff)
            self.last_process_result = "CONVERSATION_QUIET_WAIT_HOLD"
            return self.last_process_result
        self.group = Group(anchor.sender, [row.original_id for row in same_sender], "GROUP_REPLY_READY")
        for index, row in enumerate(same_sender):
            row.status = "READY_TO_SEND" if index == 0 else "GROUP_BOUND"
            self.sheet_writes += 1
        self.ledger_writes += len(same_sender) + 3
        self.openai_calls += 1
        self.last_process_result = "PROCESS_SUCCESS"
        return self.last_process_result

    def task262(self) -> str:
        self.task262_calls += 1
        if not self.group:
            return "NO_READY_ROW"
        group = self.group
        if group.state == "GROUP_REPLY_READY":
            if group.possible_click:
                group.state = "GROUP_SEND_OUTCOME_REVIEW"
                return "POSSIBLE_CLICK_REVIEW_NO_RETRY"
            group.send_clicks += 1
            group.possible_click = True
            group.state = "GROUP_SEND_AWAITING_CONFIRM"
            self.ledger_writes += 1
            return "SEND_AWAITING_CONFIRM"
        if group.state == "GROUP_SEND_AWAITING_CONFIRM":
            return "CONFIRMATION_PENDING_NO_RETRY"
        if group.state == "GROUP_SEND_OUTCOME_REVIEW":
            return "SEND_OUTCOME_REVIEW_NO_RETRY"
        if group.state == "GROUP_ANCHOR_ARCHIVED":
            group.state = "GROUP_FINALIZING"
            self.ledger_writes += 1
        if group.state == "GROUP_FINALIZING":
            companions = max(0, len(group.member_ids) - 1)
            group.companions_done = companions
            group.state = "GROUP_COMPLETE"
            self.ledger_writes += companions + 1
            return "GROUP_COMPLETE"
        if group.state == "GROUP_REVIEW":
            return "GROUP_REVIEW_NO_SEND"
        return "SAFE_NO_SEND"

    def cycle(self, admit_overflow: bool | None = None) -> str:
        # Exact source order in Task 263: journal drain, overflow drain, Task282, Task262.
        if admit_overflow is not None:
            self.drain_journal_once(overflow=admit_overflow)
        self.drain_overflow_once()
        result = self.process_one()
        if result == "CONVERSATION_QUIET_WAIT_HOLD":
            return result
        if "HOLD" in result or "ERROR" in result:
            return result
        return self.task262()

    def fire_deferred(self) -> str:
        if self.deferred_waiters != 1 or self.deferred_cutoff is None:
            return "NO_WAITER"
        if self.stop_requested:
            self.deferred_waiters = 0
            self.deferred_cutoff = None
            return "CONVERSATION_QUIET_RECHECK_CANCELLED_STOP"
        if self.now < self.deferred_cutoff:
            return "WAITING"
        self.deferred_waiters = 0
        self.deferred_cutoff = None
        return self.cycle(admit_overflow=None)

    def invariants(self) -> list[str]:
        failures: list[str] = []
        if self.deferred_waiters not in (0, 1):
            failures.append("waiter_storm")
        if self.group and self.group.send_clicks > 1:
            failures.append("second_send")
        if self.group and len(self.group.member_ids) != len(set(self.group.member_ids)):
            failures.append("duplicate_group_member")
        if self.group and any(next((row.sender for row in self.active_rows if row.original_id == member), self.group.sender) != self.group.sender for member in self.group.member_ids):
            failures.append("mixed_sender")
        if self.group and self.group.state == "GROUP_COMPLETE" and self.group.companions_done != max(0, len(self.group.member_ids) - 1):
            failures.append("complete_before_companions")
        return failures


def lifecycle_matrix() -> list[dict[str, object]]:
    cases: list[tuple[str, int]] = []
    for state in sorted(LIFECYCLE_STATES):
        for count in ((1, 10, 50) if state == "GROUP_SEND_AWAITING_CONFIRM" else (1,)):
            cases.append((state, count))
    results: list[dict[str, object]] = []
    for state, count in cases:
        runtime = Runtime(now=100, group=Group("sender-a", ["active"], state, possible_click=state in {"GROUP_SEND_AWAITING_CONFIRM", "GROUP_SEND_OUTCOME_REVIEW"}, send_clicks=1 if state in {"GROUP_SEND_AWAITING_CONFIRM", "GROUP_SEND_OUTCOME_REVIEW"} else 0))
        for index in range(count):
            row = JournalRow(f"new-{index}", "sender-b", f"message-{index}", 1, "RESOLVED_MAIN")
            runtime.journal.append(row)
            runtime.active_rows.append(ActiveRow(row.original_id, row.sender, row.message, "Sheet1"))
        writes_before = runtime.sheet_writes
        api_before = runtime.openai_calls
        new_before = [row.status for row in runtime.active_rows]
        result = runtime.cycle(admit_overflow=None)
        passed = (
            runtime.task262_calls == 1
            and runtime.openai_calls == api_before
            and runtime.sheet_writes == writes_before
            and [row.status for row in runtime.active_rows] == new_before
            and runtime.group.send_clicks <= 1
            and not runtime.invariants()
        )
        results.append({"state": state, "new_rows": count, "result": result, "task262_calls": runtime.task262_calls, "openai_delta": runtime.openai_calls - api_before, "new_rows_processed": sum(row.status != "NEW" for row in runtime.active_rows), "send_clicks": runtime.group.send_clicks, "pass": passed})
    return results


def source_contract_cases() -> list[dict[str, object]]:
    cases: list[dict[str, object]] = []

    def record(name: str, passed: bool, evidence: object) -> None:
        cases.append({"name": name, "pass": bool(passed), "evidence": evidence})

    for status in sorted(ADMITTED):
        runtime = Runtime(now=20)
        runtime.journal.append(JournalRow("id", "sender", "message", 1, status))
        runtime.active_rows.append(ActiveRow("id", "sender", "message", "Sheet1"))
        result = runtime.process_one()
        record(f"admitted_{status.lower()}_accepted", result == "PROCESS_SUCCESS" and runtime.openai_calls == 1, result)

    runtime = Runtime(now=20)
    runtime.journal.append(JournalRow("id", "sender", "message", 1, "JOURNALED"))
    runtime.active_rows.append(ActiveRow("id", "sender", "message", "Sheet1"))
    record("journaled_only_rejected_for_member", runtime.process_one() == "CONVERSATION_JOURNAL_IDENTITY_HOLD", runtime.last_process_result)

    runtime = Runtime(now=20)
    runtime.journal.extend([JournalRow("id", "sender", "message", 1, "RESOLVED_MAIN"), JournalRow("id", "sender", "message", 1, "RESOLVED_MAIN")])
    runtime.active_rows.append(ActiveRow("id", "sender", "message", "Sheet1"))
    record("duplicate_journal_match_rejected", runtime.process_one() == "CONVERSATION_JOURNAL_IDENTITY_HOLD", runtime.last_process_result)

    runtime = Runtime(now=20)
    runtime.journal.append(JournalRow("historical", "sender", "old", 0, "RESOLVED_MAIN"))
    runtime.journal.append(JournalRow("current", "sender", "new", 1, "RESOLVED_MAIN"))
    runtime.active_rows.append(ActiveRow("current", "sender", "new", "Sheet1"))
    record("historical_resolved_without_active_location_ignored", runtime.process_one() == "PROCESS_SUCCESS", runtime.last_process_result)

    runtime = Runtime(now=5)
    runtime.journal.append(JournalRow("id", "sender", "message", 1, "RESOLVED_MAIN"))
    runtime.active_rows.append(ActiveRow("id", "sender", "message", "Sheet1"))
    before = (runtime.sheet_writes, runtime.ledger_writes, runtime.openai_calls)
    result = runtime.process_one()
    record("quiet_wait_zero_write_api_send", result == "CONVERSATION_QUIET_WAIT_HOLD" and before == (runtime.sheet_writes, runtime.ledger_writes, runtime.openai_calls) and runtime.task262_calls == 0 and runtime.deferred_waiters == 1, {"result": result, "waiters": runtime.deferred_waiters})
    runtime.stop_requested = True
    record("stop_cancels_deferred_without_cycle", runtime.fire_deferred() == "CONVERSATION_QUIET_RECHECK_CANCELLED_STOP" and runtime.task262_calls == 0, runtime.deferred_waiters)

    runtime = Runtime(now=5)
    runtime.journal.append(JournalRow("id1", "sender", "m1", 1, "RESOLVED_MAIN"))
    runtime.active_rows.append(ActiveRow("id1", "sender", "m1", "Sheet1"))
    runtime.process_one()
    runtime.journal.append(JournalRow("id2", "sender", "m2", 4, "RESOLVED_MAIN"))
    runtime.active_rows.append(ActiveRow("id2", "sender", "m2", "Sheet1"))
    runtime.process_one()
    record("newer_event_coalesces_one_waiter_and_extends_cutoff", runtime.deferred_waiters == 1 and runtime.deferred_cutoff == 14, {"waiters": runtime.deferred_waiters, "cutoff": runtime.deferred_cutoff})

    for overflow in (False, True):
        runtime = Runtime(now=20)
        runtime.receive(JournalRow("id", "sender", "message", 1))
        runtime.drain_journal_once(overflow=overflow)
        expected = "RESOLVED_OVERFLOW" if overflow else "RESOLVED_MAIN"
        record(f"{'overflow' if overflow else 'direct'}_admission_progression", runtime.journal[0].status == expected and runtime.exact_journal_contract(runtime.active_rows[0]), {"status": runtime.journal[0].status, "location": runtime.active_rows[0].location})
    return cases


def randomized(seed: int, schedules: int, steps: int) -> dict[str, object]:
    rng = random.Random(seed)
    failures: list[dict[str, object]] = []
    operations = 0
    for schedule in range(schedules):
        runtime = Runtime(now=0)
        next_id = 0
        for _ in range(steps):
            operations += 1
            choice = rng.randrange(11)
            if choice <= 2:
                sender = f"sender-{rng.randrange(4)}"
                original_id = f"{schedule}-{next_id}"
                if choice == 2 and runtime.journal:
                    original_id = rng.choice(runtime.journal).original_id
                else:
                    next_id += 1
                runtime.receive(JournalRow(original_id, sender, f"message-{rng.randrange(6)}", runtime.now))
            elif choice == 3:
                runtime.drain_journal_once(overflow=rng.random() < 0.3)
            elif choice == 4:
                runtime.drain_overflow_once()
            elif choice == 5:
                runtime.now += rng.randrange(1, 8)
            elif choice == 6:
                runtime.process_one()
            elif choice == 7:
                result = runtime.last_process_result
                if result and "HOLD" not in result and "ERROR" not in result:
                    runtime.task262()
            elif choice == 8:
                runtime.stop_requested = rng.random() < 0.5
                runtime.fire_deferred()
            elif choice == 9 and runtime.group:
                if runtime.group.state == "GROUP_SEND_AWAITING_CONFIRM":
                    runtime.group.confirmed = True
                    runtime.group.anchor_archived = True
                    runtime.group.state = "GROUP_ANCHOR_ARCHIVED"
            elif runtime.group and runtime.group.state == "GROUP_FINALIZING":
                runtime.task262()
            invariant_failures = runtime.invariants()
            if invariant_failures:
                failures.append({"schedule": schedule, "failures": invariant_failures})
                break
    return {"seed": seed, "schedules": schedules, "steps_per_schedule": steps, "modeled_operations": operations, "failure_count": len(failures), "sample_failures": failures[:10], "pass": not failures}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--schedules", type=int, default=100_000)
    parser.add_argument("--steps", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260717)
    args = parser.parse_args()
    lifecycle = lifecycle_matrix()
    contracts = source_contract_cases()
    random_result = randomized(args.seed, args.schedules, args.steps)
    status = "PASS" if all(item["pass"] for item in lifecycle + contracts) and random_result["pass"] and random_result["modeled_operations"] >= 1_000_000 else "FAIL"
    report = {
        "status": status,
        "independent_source_order_model": True,
        "task263_order": ["journal_drain", "overflow_drain", "task282_process", "hold_error_guard", "task262_lifecycle"],
        "journal_progression": ["JOURNALED", "RESOLVED_MAIN_or_RESOLVED_OVERFLOW", "durable_group_membership"],
        "lifecycle_matrix": lifecycle,
        "source_contract_cases": contracts,
        "randomized": random_result,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": status, "lifecycle_cases": len(lifecycle), "contract_cases": len(contracts), "randomized": random_result}, indent=2))
    if status != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
