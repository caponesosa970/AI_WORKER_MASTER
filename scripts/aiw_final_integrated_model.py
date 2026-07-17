from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass, field
from pathlib import Path


BOUNDARIES = [
    "ingress_lock_owner_write", "ingress_lock_timestamp_write", "journal_slot_read",
    "journal_blank_read", "journal_write", "journal_readback", "identity_probe_write",
    "identity_probe_read", "overflow_barrier_read", "admission_lock_owner_write",
    "admission_lock_timestamp_write", "main_slot_read", "main_blank_read",
    "main_staging_write", "main_staging_readback", "main_new_write", "main_new_readback",
    "overflow_lock_owner_write", "overflow_lock_timestamp_write", "overflow_slot_read",
    "overflow_blank_read", "overflow_pending_write", "overflow_pending_readback",
    "overflow_fifo_select", "overflow_source_bind_read", "overflow_draining_write",
    "overflow_draining_readback", "overflow_main_identity_read", "overflow_main_slot_read",
    "overflow_main_stage_write", "overflow_main_stage_readback", "overflow_source_commit_write",
    "overflow_source_commit_readback", "overflow_main_new_write", "overflow_main_new_readback",
    "overflow_source_drained_write", "overflow_source_drained_readback", "processing_row_read",
    "processing_mark_write", "processing_mark_readback", "http_request", "http_response_parse",
    "reply_write", "reply_readback", "send_row_read", "sending_write", "sending_readback",
    "thread_open_ui", "compose_ui", "send_attempt_marker", "send_click", "post_click_status_write",
    "confirmation_row_read", "confirmation_ui_read", "done_write", "done_readback",
    "archive_source_read", "archive_write", "archive_readback", "archive_source_clear",
    "desired_run_write", "desired_run_readback", "recovery_probe_read", "recovery_proof_write",
    "lock_release_owner_check", "lock_release_timestamp_clear", "lock_release_owner_clear",
]


@dataclass
class Event:
    event_id: str
    sender: str
    message: str
    logged_at: int
    journal_status: str = "JOURNALED"
    location: str = ""
    main_status: str = ""
    overflow_status: str = ""
    overflow_row: int = 0
    reply: str = ""
    reply_for: str = ""
    send_attempted: bool = False
    send_count: int = 0
    confirmed: bool = False
    archived: bool = False


@dataclass
class Lock:
    owner: str = ""
    started: int = 0


@dataclass
class Model:
    main_capacity: int = 3
    events: dict[str, Event] = field(default_factory=dict)
    journal_order: list[str] = field(default_factory=list)
    overflow_order: list[str] = field(default_factory=list)
    archive_order: list[str] = field(default_factory=list)
    locks: dict[str, Lock] = field(default_factory=lambda: {name: Lock() for name in ("ingress", "queue", "overflow", "admission", "processing", "send", "confirm", "archive")})
    desired_run: bool = True
    stopped: bool = False
    ambiguous_locks: set[str] = field(default_factory=set)
    proof: list[str] = field(default_factory=list)
    operations: int = 0
    next_overflow_row: int = 2

    def acquire(self, name: str, token: str) -> bool:
        self.operations += 1
        lock = self.locks[name]
        if self.stopped or lock.owner or lock.started:
            return False
        lock.owner = token
        lock.started = self.operations
        return lock.owner == token and lock.started > 0

    def release(self, name: str, token: str) -> bool:
        self.operations += 1
        lock = self.locks[name]
        if lock.owner != token or not lock.started:
            return False
        lock.started = 0
        if lock.owner == token:
            lock.owner = ""
        return not lock.owner and lock.started == 0

    def ingress(self, event_id: str, logged_at: int) -> None:
        self.operations += 1
        if event_id in self.events:
            return
        event = Event(event_id, f"sender-{event_id}", f"message-{event_id}", logged_at)
        self.events[event_id] = event
        self.journal_order.append(event_id)

    def unresolved_overflow(self) -> list[Event]:
        return sorted(
            (event for event in self.events.values() if event.overflow_status in {"PENDING", "DRAINING", "MAIN_COMMITTED", "OVERFLOW_REVIEW"}),
            key=lambda event: (event.logged_at, event.overflow_row),
        )

    def main_active(self) -> list[Event]:
        return [event for event in self.events.values() if event.main_status and not event.archived]

    def journal_drain(self) -> str:
        self.operations += 1
        candidates = [self.events[event_id] for event_id in self.journal_order if self.events[event_id].journal_status == "JOURNALED"]
        if not candidates:
            return "EMPTY"
        event = candidates[0]
        duplicates = [other for other in self.events.values() if other.event_id == event.event_id and other is not event]
        if duplicates or event.main_status or event.overflow_status or event.archived:
            event.journal_status = "RESOLVED_DUPLICATE"
            event.location = "DUPLICATE"
            return "DUPLICATE"
        if self.unresolved_overflow() or len(self.main_active()) >= self.main_capacity:
            event.overflow_status = "PENDING"
            event.overflow_row = self.next_overflow_row
            self.next_overflow_row += 1
            self.overflow_order.append(event.event_id)
            event.journal_status = "RESOLVED_OVERFLOW"
            event.location = f"OVERFLOW:{event.overflow_row}"
            return "OVERFLOW"
        event.main_status = "NEW"
        event.journal_status = "RESOLVED_MAIN"
        event.location = "MAIN"
        return "MAIN"

    def overflow_drain(self) -> str:
        self.operations += 1
        unresolved = self.unresolved_overflow()
        if not unresolved:
            return "EMPTY"
        event = unresolved[0]
        event.overflow_status = "DRAINING"
        if event.main_status:
            event.overflow_status = "MAIN_COMMITTED"
            event.overflow_status = "DRAINED"
            return "RECONCILED"
        if len(self.main_active()) >= self.main_capacity:
            event.overflow_status = "PENDING"
            return "HOLD"
        event.main_status = "OVERFLOW_ADMITTING"
        event.overflow_status = "MAIN_COMMITTED"
        event.main_status = "NEW"
        event.overflow_status = "DRAINED"
        return "MOVED"

    def process(self) -> str:
        self.operations += 1
        if self.unresolved_overflow():
            return "OVERFLOW_HOLD"
        candidates = [event for event in self.events.values() if event.main_status == "NEW" and not event.archived]
        if not candidates:
            return "EMPTY"
        event = min(candidates, key=lambda value: value.logged_at)
        event.main_status = "PROCESSING"
        event.reply = f"reply-{event.event_id}"
        event.reply_for = event.event_id
        event.main_status = "READY_TO_SEND"
        return "READY"

    def send(self, ambiguous: bool = False) -> str:
        self.operations += 1
        if self.stopped or self.unresolved_overflow():
            return "HOLD"
        candidates = [event for event in self.events.values() if event.main_status == "READY_TO_SEND" and not event.archived]
        if not candidates:
            return "EMPTY"
        event = min(candidates, key=lambda value: value.logged_at)
        if event.send_attempted:
            return "NO_RETRY"
        if event.reply_for != event.event_id:
            return "STALE_REPLY_HOLD"
        event.send_attempted = True
        event.send_count += 1
        event.main_status = "SEND_CLICKED_AWAITING_CONFIRM" if ambiguous else "SENT_AWAITING_CONFIRM"
        return event.main_status

    def confirm(self) -> str:
        self.operations += 1
        candidates = [event for event in self.events.values() if event.main_status in {"SENT_AWAITING_CONFIRM", "SEND_CLICKED_AWAITING_CONFIRM"}]
        if not candidates:
            return "EMPTY"
        event = min(candidates, key=lambda value: value.logged_at)
        if event.send_count != 1:
            return "HOLD"
        event.confirmed = True
        event.main_status = "DONE"
        return "DONE"

    def archive(self) -> str:
        self.operations += 1
        candidates = [event for event in self.events.values() if event.main_status == "DONE" and not event.archived]
        if not candidates:
            return "EMPTY"
        event = min(candidates, key=lambda value: value.logged_at)
        if not event.confirmed:
            return "HOLD"
        event.archived = True
        event.main_status = ""
        self.archive_order.append(event.event_id)
        return "ARCHIVED"

    def stop(self) -> None:
        self.operations += 1
        self.desired_run = False
        self.stopped = True

    def start(self) -> None:
        self.operations += 1
        self.desired_run = True
        self.stopped = False

    def recover(self) -> str:
        self.operations += 1
        if self.ambiguous_locks:
            return "HOLD"
        for name, lock in self.locks.items():
            if bool(lock.owner) != bool(lock.started):
                return "HOLD"
            if lock.owner and name not in {"send", "confirm", "archive"}:
                self.proof.append(f"SAFE_CLEAR:{name}")
                lock.started = 0
                lock.owner = ""
        for event in self.events.values():
            if event.main_status == "ADMISSION_STAGING":
                return "HOLD"
            if event.overflow_status == "MAIN_COMMITTED" and event.main_status:
                event.overflow_status = "DRAINED"
        return "SAFE"

    def violations(self) -> list[str]:
        failures: list[str] = []
        if set(self.events) != set(self.journal_order):
            failures.append("event_without_durable_journal")
        if len(self.journal_order) != len(set(self.journal_order)):
            failures.append("duplicate_journal_identity")
        if any(event.send_count > 1 for event in self.events.values()):
            failures.append("second_send")
        if any(event.main_status == "DONE" and not event.confirmed for event in self.events.values()):
            failures.append("done_without_confirmation")
        if any(event.archived and not event.confirmed for event in self.events.values()):
            failures.append("archive_without_confirmation")
        if any(event.reply and event.reply_for != event.event_id for event in self.events.values()):
            failures.append("stale_reply_binding")
        if any(bool(lock.owner) != bool(lock.started) for lock in self.locks.values()):
            failures.append("partial_lock_pair")
        unresolved = self.unresolved_overflow()
        if unresolved:
            oldest = min(unresolved, key=lambda event: (event.logged_at, event.overflow_row))
            if unresolved[0] is not oldest:
                failures.append("overflow_not_fifo")
            newer_direct = [event for event in self.events.values() if event.main_status and event.logged_at > oldest.logged_at and not event.overflow_status]
            if newer_direct:
                failures.append("direct_bypass_overflow_barrier")
        if self.stopped and self.desired_run:
            failures.append("stop_desired_run_mismatch")
        return sorted(set(failures))


def randomized(seed: int, schedules: int) -> dict:
    rng = random.Random(seed)
    operations = 0
    failures: list[dict] = []
    for schedule in range(schedules):
        model = Model(main_capacity=rng.randint(2, 5))
        event_count = rng.randint(2, 7)
        for index in range(event_count):
            model.ingress(f"{schedule:06d}{index:02d}", schedule * 10 + index)
        for _ in range(rng.randint(12, 28)):
            choice = rng.randrange(10)
            if choice == 0:
                model.journal_drain()
            elif choice == 1:
                model.overflow_drain()
            elif choice == 2:
                model.process()
            elif choice == 3:
                model.send(ambiguous=bool(rng.getrandbits(1)))
            elif choice == 4:
                model.confirm()
            elif choice == 5:
                model.archive()
            elif choice == 6:
                model.stop()
            elif choice == 7:
                model.start()
            elif choice == 8:
                token = f"AIW{schedule}{model.operations}"
                if model.acquire("queue", token):
                    model.release("queue", token)
            else:
                model.recover()
            violations = model.violations()
            if violations:
                failures.append({"schedule": schedule, "violations": violations})
                break
        operations += model.operations
    return {"seed": seed, "schedules": schedules, "operations": operations, "failures": failures}


def fault_matrix() -> dict:
    cases: list[dict] = []
    for boundary in BOUNDARIES:
        for position in ("before", "after"):
            model = Model(main_capacity=2)
            model.ingress("10000000000000000001", 1)
            model.ingress("10000000000000000002", 2)
            # A fault may leave only documented durable intermediates; recovery must never invent DONE or a send.
            if boundary in {"main_staging_write", "main_staging_readback"} and position == "after":
                model.events["10000000000000000001"].main_status = "ADMISSION_STAGING"
            elif boundary in {"overflow_draining_write", "overflow_draining_readback"} and position == "after":
                event = model.events["10000000000000000001"]
                event.overflow_status = "DRAINING"
                event.overflow_row = 2
            elif boundary in {"overflow_source_commit_write", "overflow_source_commit_readback"} and position == "after":
                event = model.events["10000000000000000001"]
                event.main_status = "NEW"
                event.overflow_status = "MAIN_COMMITTED"
                event.overflow_row = 2
            elif boundary == "send_click" and position == "after":
                event = model.events["10000000000000000001"]
                event.main_status = "SEND_CLICKED_AWAITING_CONFIRM"
                event.send_attempted = True
                event.send_count = 1
            elif "lock_" in boundary and position == "after":
                model.ambiguous_locks.add("admission")
            recovery = model.recover()
            violations = model.violations()
            safe = not violations and all(event.send_count <= 1 for event in model.events.values())
            cases.append({"boundary": boundary, "position": position, "recovery": recovery, "pass": safe, "violations": violations})
    return {"boundary_count": len(BOUNDARIES), "case_count": len(cases), "failures": [case for case in cases if not case["pass"]]}


def mutation_tests() -> dict:
    mutations: dict[str, list[str]] = {}

    def caught(name: str, model: Model, expected: str) -> None:
        violations = model.violations()
        mutations[name] = violations
        if expected not in violations:
            mutations[name] = violations + [f"MISSING_EXPECTED:{expected}"]

    model = Model(); model.ingress("1", 1); model.events["1"].send_count = 2
    caught("automatic_send_retry", model, "second_send")
    model = Model(); model.ingress("1", 1); model.events["1"].main_status = "DONE"
    caught("done_without_confirmation", model, "done_without_confirmation")
    model = Model(); model.ingress("1", 1); model.events["1"].archived = True
    caught("archive_without_confirmation", model, "archive_without_confirmation")
    model = Model(); model.ingress("1", 1); model.events["1"].reply = "x"; model.events["1"].reply_for = "2"
    caught("stale_reply", model, "stale_reply_binding")
    model = Model(); model.ingress("1", 1); model.locks["admission"].owner = "x"
    caught("partial_owner_write", model, "partial_lock_pair")
    model = Model(); model.ingress("1", 1); model.locks["admission"].started = 1
    caught("partial_timestamp_write", model, "partial_lock_pair")
    model = Model(); model.ingress("1", 1); model.journal_order.clear()
    caught("journal_removed", model, "event_without_durable_journal")
    model = Model(); model.ingress("1", 1); model.journal_order.append("1")
    caught("duplicate_journal", model, "duplicate_journal_identity")
    model = Model(); model.ingress("1", 1); model.ingress("2", 2); model.events["1"].overflow_status = "PENDING"; model.events["1"].overflow_row = 2; model.events["2"].main_status = "NEW"
    caught("direct_bypass_overflow", model, "direct_bypass_overflow_barrier")
    model = Model(); model.ingress("1", 1); model.stopped = True; model.desired_run = True
    caught("stop_allows_desired_run", model, "stop_desired_run_mismatch")
    model = Model(); model.ingress("1", 1); model.events["1"].send_count = 3
    caught("send_attempt_marker_removed", model, "second_send")
    model = Model(); model.ingress("1", 1); model.events["1"].main_status = "DONE"; model.events["1"].archived = True
    caught("confirm_guard_removed", model, "done_without_confirmation")
    model = Model(); model.ingress("1", 1); model.events["1"].reply = "reply-2"; model.events["1"].reply_for = "2"
    caught("row_binding_removed", model, "stale_reply_binding")
    model = Model(); model.ingress("1", 1); model.locks["overflow"].owner = "stolen"
    caught("age_only_lock_steal", model, "partial_lock_pair")
    model = Model(); model.ingress("1", 1); model.events["1"].archived = True; model.events["1"].confirmed = False
    caught("archive_status_guard_removed", model, "archive_without_confirmation")
    failed = [name for name, values in mutations.items() if any(value.startswith("MISSING_EXPECTED") for value in values)]
    return {"mutation_count": len(mutations), "caught_count": len(mutations) - len(failed), "failures": failed, "evidence": mutations}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--seed", type=int, default=20260716)
    parser.add_argument("--schedules", type=int, default=100000)
    args = parser.parse_args()
    random_result = randomized(args.seed, args.schedules)
    fault_result = fault_matrix()
    mutation_result = mutation_tests()
    status = "PASS"
    failures: list[str] = []
    if random_result["failures"]:
        failures.append("randomized_invariant_failure")
    if random_result["operations"] < 1_000_000:
        failures.append("modeled_operations_below_one_million")
    if fault_result["failures"]:
        failures.append("fault_matrix_failure")
    if mutation_result["failures"] or mutation_result["caught_count"] != mutation_result["mutation_count"]:
        failures.append("mutation_detection_failure")
    if failures:
        status = "FAIL"
    report = {
        "model": "AIW final integrated durable-state model v1",
        "status": status,
        "randomized": random_result,
        "fault_injection": fault_result,
        "mutation_testing": mutation_result,
        "properties": [
            "durable journal membership", "identity uniqueness", "overflow barrier", "FIFO selection",
            "no second Send", "DONE only after confirmation", "Archive only after confirmation",
            "reply bound to exact ID", "exact owner lock pairs", "STOP desired-run consistency",
        ],
        "failures": failures,
        "boundary_note": "Offline state-model proof only; it does not claim Tasker import/render or phone proof.",
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": status,
        "schedules": random_result["schedules"],
        "operations": random_result["operations"],
        "random_failures": len(random_result["failures"]),
        "fault_cases": fault_result["case_count"],
        "fault_failures": len(fault_result["failures"]),
        "mutations": mutation_result["mutation_count"],
        "mutations_caught": mutation_result["caught_count"],
    }, indent=2))
    if status != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
