from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass, field
from pathlib import Path


ROLES = (
    "HIST_ARCHIVE",
    "HIST_DEAD",
    "G14C_REAL",
    "G14C_RATE",
    "G14C_TIMEOUT",
    "G14C_QUOTA",
    "G14C_LEGACY",
)
CAPS = {"Sheet1": 980, "Archive": 933, "DeadArchive": 972}
PROTECTED = {("Sheet1", row) for row in (144, 145, 146, 147)}


@dataclass
class Binding:
    role: str
    layer: str
    row: int
    approved_max: int
    expected_id: str
    expected_run: str
    payload: tuple[str, ...]


@dataclass
class CellState:
    kind: str = "blank"  # blank, owned, occupied, partial, error
    owner_run: str = ""
    expected_id: str = ""
    payload: tuple[str, ...] = ()


@dataclass
class Guards:
    bounds: bool = True
    blankness: bool = True
    ownership: bool = True
    expected_id: bool = True
    pre_read: bool = True
    post_readback: bool = True
    one_shot: bool = True
    error_routing: bool = True


@dataclass
class System:
    run_id: str
    auth_run: str
    auth_token: str
    auth_state: str
    consumed_run: str
    bindings: dict[str, Binding]
    rows: dict[tuple[str, int], CellState]
    guards: Guards = field(default_factory=Guards)
    contract_ready: bool = False
    writes: int = 0
    safe_writes: int = 0
    unsafe_writes: int = 0
    reads: int = 0
    read_attempts: int = 0
    holds: list[str] = field(default_factory=list)
    operations: int = 0

    def hold(self, reason: str) -> bool:
        self.holds.append(reason)
        self.operations += 1
        return False

    def binding_valid(self, binding: Binding) -> bool:
        self.operations += 1
        if binding.role not in ROLES:
            return False
        if not binding.layer or not binding.expected_id or not binding.expected_run or not binding.payload:
            return False
        if binding.expected_run != self.run_id or self.run_id not in binding.expected_id:
            return False
        if self.guards.bounds:
            if binding.layer not in CAPS or binding.approved_max > CAPS[binding.layer]:
                return False
            if binding.row < 2 or binding.row > binding.approved_max:
                return False
            if (binding.layer, binding.row) in PROTECTED:
                return False
        return True

    def read(self, binding: Binding, fault: str = "none") -> CellState | None:
        for attempt in range(1, 3):
            self.read_attempts += 1
            self.operations += 1
            if fault in {"read_error", "unresolved", "stale_array", "hash_error"}:
                continue
            self.reads += 1
            return self.rows.get((binding.layer, binding.row), CellState())
        return None

    def owned(self, binding: Binding, state: CellState) -> bool:
        self.operations += 1
        if state.kind != "owned":
            return False
        if self.guards.ownership and state.owner_run != self.run_id:
            return False
        if self.guards.expected_id and state.expected_id != binding.expected_id:
            return False
        return state.payload == binding.payload

    def write(self, binding: Binding, new_state: CellState, *, fault: str = "none") -> bool:
        self.writes += 1
        self.operations += 1
        current = self.rows.get((binding.layer, binding.row), CellState())
        safe = self.binding_valid(binding) and (
            (new_state.kind == "owned" and current.kind == "blank")
            or (new_state.kind == "blank" and self.owned(binding, current))
        )
        if safe:
            self.safe_writes += 1
        else:
            self.unsafe_writes += 1
        if fault == "write_error_no_effect":
            return False
        self.rows[(binding.layer, binding.row)] = new_state
        return fault != "write_error_reported"

    def contract(self, fault_by_role: dict[str, str] | None = None) -> bool:
        self.operations += 1
        fault_by_role = fault_by_role or {}
        if self.auth_state not in {"ARMED", "ACTIVE"}:
            return self.hold("STALE_AUTH")
        if self.auth_run != self.run_id or not self.auth_token or self.auth_token.startswith("%"):
            return self.hold("AUTH_CONFIG")
        if self.guards.one_shot:
            if self.auth_state == "ACTIVE" and self.consumed_run != self.run_id:
                return self.hold("ACTIVE_OWNER")
            if self.auth_state == "ARMED" and self.consumed_run == self.run_id:
                return self.hold("ARMED_REUSE")
        if set(self.bindings) != set(ROLES):
            return self.hold("INCOMPLETE")
        keys = [(binding.layer, binding.row) for binding in self.bindings.values()]
        ids = [binding.expected_id for binding in self.bindings.values()]
        if len(keys) != len(set(keys)) or len(ids) != len(set(ids)):
            return self.hold("CONFLICT")
        for role in ROLES:
            binding = self.bindings[role]
            if not self.binding_valid(binding):
                return self.hold("BINDING")
            state = self.read(binding, fault_by_role.get(role, "none"))
            if state is None:
                return self.hold("PLUGIN_READ")
            if self.auth_state == "ARMED" and state.kind != "blank":
                return self.hold("NOT_BLANK")
            if self.auth_state == "ACTIVE" and not (state.kind == "blank" or self.owned(binding, state)):
                return self.hold("NOT_OWNED")
        if self.auth_state == "ARMED":
            self.consumed_run = self.run_id
            self.auth_state = "ACTIVE"
        self.contract_ready = True
        self.operations += 1
        return True

    def setup(self, role: str, fault: str = "none", stop_at: str = "none") -> bool:
        self.operations += 1
        if not self.contract_ready or self.auth_state != "ACTIVE" or self.consumed_run != self.run_id:
            return self.hold("CONTRACT_NOT_ACTIVE")
        binding = self.bindings.get(role)
        if binding is None or not self.binding_valid(binding):
            return self.hold("BINDING")
        state = self.read(binding, fault if fault in {"read_error", "unresolved", "stale_array", "hash_error"} else "none") if self.guards.pre_read else CellState()
        if state is None:
            return self.hold("READ")
        if self.owned(binding, state):
            return True
        if self.guards.blankness and state.kind != "blank":
            return self.hold("OCCUPIED")
        if stop_at == "before_write":
            return self.hold("STOP_BEFORE_WRITE")
        expected = CellState("owned", self.run_id, binding.expected_id, binding.payload)
        self.write(binding, expected, fault=fault if fault.startswith("write_") else "none")
        if stop_at == "after_write":
            return self.hold("STOP_AFTER_WRITE")
        if not self.guards.post_readback:
            return True
        final = self.read(binding, "read_error" if fault == "post_read_error" else "none")
        if final is None:
            return self.hold("POST_READ")
        if not self.owned(binding, final):
            return self.hold("READBACK")
        return True

    def cleanup(self, role: str, fault: str = "none", stop_at: str = "none") -> bool:
        self.operations += 1
        if not self.contract_ready or self.auth_state != "ACTIVE" or self.consumed_run != self.run_id:
            return self.hold("CONTRACT_NOT_ACTIVE")
        binding = self.bindings.get(role)
        if binding is None or not self.binding_valid(binding):
            return self.hold("BINDING")
        state = self.read(binding, fault if fault in {"read_error", "unresolved", "stale_array", "hash_error"} else "none") if self.guards.pre_read else CellState("owned", self.run_id, binding.expected_id, binding.payload)
        if state is None:
            return self.hold("READ")
        if state.kind == "blank":
            return True
        if not self.owned(binding, state):
            return self.hold("WRONG_IDENTITY")
        if stop_at == "before_write":
            return self.hold("STOP_BEFORE_WRITE")
        self.write(binding, CellState(), fault=fault if fault.startswith("write_") else "none")
        if stop_at == "after_write":
            return self.hold("STOP_AFTER_WRITE")
        if not self.guards.post_readback:
            return True
        final = self.read(binding, "read_error" if fault == "post_read_error" else "none")
        if final is None or final.kind != "blank":
            return self.hold("READBACK")
        return True

    def close(self) -> bool:
        self.operations += 1
        if not self.contract_ready or self.auth_state != "ACTIVE":
            return self.hold("CLOSE_AUTH")
        for binding in self.bindings.values():
            state = self.read(binding)
            if state is None or state.kind != "blank":
                return self.hold("CLOSE_DIRTY")
        self.auth_state = "USED"
        self.auth_token = ""
        self.contract_ready = False
        return True


def valid_system(seed: int = 1) -> System:
    run_id = f"20260717{seed:012d}"
    bindings = {
        "HIST_ARCHIVE": Binding("HIST_ARCHIVE", "Archive", 10, 933, f"AIWFX-{run_id}-HIST_ARCHIVE", run_id, ("archive", run_id)),
        "HIST_DEAD": Binding("HIST_DEAD", "DeadArchive", 10, 972, f"AIWFX-{run_id}-HIST_DEAD", run_id, ("dead", run_id)),
        "G14C_REAL": Binding("G14C_REAL", "Sheet1", 300, 980, f"AIWFX-{run_id}-G14C_REAL", run_id, ("real", run_id)),
        "G14C_RATE": Binding("G14C_RATE", "Sheet1", 301, 980, f"AIWFX-{run_id}-G14C_RATE", run_id, ("rate", run_id)),
        "G14C_TIMEOUT": Binding("G14C_TIMEOUT", "Sheet1", 302, 980, f"AIWFX-{run_id}-G14C_TIMEOUT", run_id, ("timeout", run_id)),
        "G14C_QUOTA": Binding("G14C_QUOTA", "Sheet1", 303, 980, f"AIWFX-{run_id}-G14C_QUOTA", run_id, ("quota", run_id)),
        "G14C_LEGACY": Binding("G14C_LEGACY", "Sheet1", 304, 980, f"AIWFX-{run_id}-G14C_LEGACY", run_id, ("legacy", run_id)),
    }
    rows = {(binding.layer, binding.row): CellState() for binding in bindings.values()}
    return System(run_id, run_id, f"AIWFXAUTH-{seed:032d}", "ARMED", "", bindings, rows)


def unsafe_case_matrix() -> list[dict]:
    results = []

    def record(name: str, system: System, result: bool, expected: bool = False) -> None:
        results.append({
            "case": name,
            "result": result,
            "expected": expected,
            "writes": system.writes,
            "unsafe_writes": system.unsafe_writes,
            "read_attempts": system.read_attempts,
            "pass": result == expected and system.unsafe_writes == 0 and (expected or system.writes == 0),
        })

    mutations = {
        "missing_token": lambda s: setattr(s, "auth_token", ""),
        "literal_token": lambda s: setattr(s, "auth_token", "%AIWFXAuthToken"),
        "stale_run": lambda s: setattr(s, "auth_run", "OLD_RUN"),
        "stale_active": lambda s: (setattr(s, "auth_state", "ACTIVE"), setattr(s, "consumed_run", "OLD_RUN")),
        "used_authorization": lambda s: setattr(s, "auth_state", "USED"),
        "missing_role": lambda s: s.bindings.pop("G14C_REAL"),
        "duplicate_row": lambda s: setattr(s.bindings["G14C_RATE"], "row", s.bindings["G14C_REAL"].row),
        "duplicate_id": lambda s: setattr(s.bindings["G14C_RATE"], "expected_id", s.bindings["G14C_REAL"].expected_id),
        "protected_row": lambda s: setattr(s.bindings["G14C_REAL"], "row", 144),
        "out_of_bounds": lambda s: setattr(s.bindings["HIST_ARCHIVE"], "row", 999),
        "max_above_physical": lambda s: setattr(s.bindings["HIST_DEAD"], "approved_max", 999),
        "wrong_identity": lambda s: s.rows.__setitem__(("Sheet1", 300), CellState("owned", s.run_id, "WRONG", ("real", s.run_id))),
        "occupied": lambda s: s.rows.__setitem__(("Sheet1", 300), CellState("occupied", "PRODUCTION", "PROD", ("data",))),
        "partial": lambda s: s.rows.__setitem__(("Sheet1", 300), CellState("partial", s.run_id, s.bindings["G14C_REAL"].expected_id, ("partial",))),
        "error_cell": lambda s: s.rows.__setitem__(("Sheet1", 300), CellState("error", s.run_id, "#ERROR", ("#ERROR",))),
    }
    for index, (name, mutate) in enumerate(mutations.items(), 1):
        system = valid_system(100 + index)
        mutate(system)
        record(name, system, system.contract())
    for index, fault in enumerate(("read_error", "unresolved", "stale_array", "hash_error"), 1):
        system = valid_system(200 + index)
        record(f"contract_{fault}", system, system.contract({"G14C_REAL": fault}))
    for index, stop_at in enumerate(("before_write",), 1):
        system = valid_system(300 + index)
        assert system.contract()
        before = system.writes
        result = system.setup("G14C_REAL", stop_at=stop_at)
        results.append({"case": f"setup_stop_{stop_at}", "result": result, "expected": False, "writes": system.writes - before, "unsafe_writes": system.unsafe_writes, "read_attempts": system.read_attempts, "pass": not result and system.writes == before and system.unsafe_writes == 0})
    system = valid_system(310)
    assert system.contract()
    system.rows[("Sheet1", 300)] = CellState("occupied", "PRODUCTION", "PROD", ("data",))
    before = system.writes
    result = system.setup("G14C_REAL")
    results.append({"case": "setup_occupied", "result": result, "expected": False, "writes": system.writes - before, "unsafe_writes": system.unsafe_writes, "read_attempts": system.read_attempts, "pass": not result and system.writes == before and system.unsafe_writes == 0})
    system = valid_system(311)
    assert system.contract()
    system.rows[("Sheet1", 300)] = CellState("owned", "OTHER", "WRONG", ("data",))
    before = system.writes
    result = system.cleanup("G14C_REAL")
    results.append({"case": "cleanup_wrong_identity", "result": result, "expected": False, "writes": system.writes - before, "unsafe_writes": system.unsafe_writes, "read_attempts": system.read_attempts, "pass": not result and system.writes == before and system.unsafe_writes == 0})
    system = valid_system(312)
    assert system.contract()
    before = system.writes
    result = system.cleanup("G14C_REAL")
    results.append({"case": "cleanup_already_blank", "result": result, "expected": True, "writes": system.writes - before, "unsafe_writes": system.unsafe_writes, "read_attempts": system.read_attempts, "pass": result and system.writes == before and system.unsafe_writes == 0})
    return results


def mutation_suite() -> list[dict]:
    cases = []

    def add(name: str, system: System, witness) -> None:
        witness(system)
        detected = system.unsafe_writes > 0 or (system.auth_state == "ACTIVE" and system.auth_run != system.run_id)
        cases.append({"mutation": name, "detected": detected, "unsafe_writes": system.unsafe_writes, "writes": system.writes, "holds": system.holds[-3:]})

    def bounds_witness(s: System) -> None:
        s.bindings["G14C_REAL"].row = 144
        s.rows[("Sheet1", 144)] = CellState()
        s.contract()
        s.setup("G14C_REAL")
        if s.rows[("Sheet1", 144)].kind == "owned":
            s.unsafe_writes += 1

    def ownership_witness(s: System) -> None:
        s.contract()
        binding = s.bindings["G14C_REAL"]
        s.rows[("Sheet1", 300)] = CellState("owned", "OTHER", binding.expected_id, binding.payload)
        s.cleanup("G14C_REAL")
        if s.rows[("Sheet1", 300)].kind == "blank":
            s.unsafe_writes += 1

    def expected_id_witness(s: System) -> None:
        s.contract()
        binding = s.bindings["G14C_REAL"]
        s.rows[("Sheet1", 300)] = CellState("owned", s.run_id, "WRONG", binding.payload)
        s.cleanup("G14C_REAL")
        if s.rows[("Sheet1", 300)].kind == "blank":
            s.unsafe_writes += 1

    system = valid_system(401)
    system.guards.bounds = False
    add("remove_bounds_check", system, bounds_witness)
    system = valid_system(402)
    system.guards.blankness = False
    add("remove_blankness_check", system, lambda s: (s.contract(), s.rows.__setitem__(("Sheet1", 300), CellState("occupied", "PROD", "PROD", ("data",))), s.setup("G14C_REAL")))
    system = valid_system(403)
    system.guards.ownership = False
    add("remove_ownership_check", system, ownership_witness)
    system = valid_system(404)
    system.guards.expected_id = False
    add("remove_expected_id_check", system, expected_id_witness)
    system = valid_system(405)
    system.guards.pre_read = False
    add("remove_pre_write_read", system, lambda s: (s.contract(), s.rows.__setitem__(("Sheet1", 300), CellState("occupied", "PROD", "PROD", ("data",))), s.setup("G14C_REAL")))
    system = valid_system(406)
    system.guards.post_readback = False
    add("remove_post_write_readback", system, lambda s: (s.contract(), s.setup("G14C_REAL", fault="write_error_no_effect"), setattr(s, "unsafe_writes", s.unsafe_writes + (1 if s.rows[("Sheet1", 300)].kind != "owned" else 0))))
    system = valid_system(407)
    system.guards.one_shot = False
    add("remove_one_shot_authorization", system, lambda s: (setattr(s, "auth_state", "ACTIVE"), setattr(s, "consumed_run", "OLD"), s.contract(), setattr(s, "unsafe_writes", s.unsafe_writes + (1 if s.contract_ready else 0))))
    system = valid_system(408)
    system.guards.error_routing = False
    add("remove_plugin_error_routing", system, lambda s: (s.contract(), s.setup("G14C_REAL", fault="read_error"), setattr(s, "unsafe_writes", s.unsafe_writes + (1 if s.read_attempts > 2 else 0))))
    return cases


def fault_injection_matrix() -> list[dict]:
    cases = []

    def capture(name: str, system: System, operation) -> None:
        before_writes = system.writes
        result = operation(system)
        cases.append({
            "case": name,
            "result": bool(result),
            "write_attempts": system.writes - before_writes,
            "unsafe_writes": system.unsafe_writes,
            "read_attempts": system.read_attempts,
            "last_hold": system.holds[-1] if system.holds else "NONE",
            "pass": system.unsafe_writes == 0 and system.read_attempts <= 30,
        })

    setup_faults = (
        "read_error", "unresolved", "stale_array", "hash_error", "write_error_no_effect",
        "write_error_reported", "post_read_error",
    )
    for index, fault in enumerate(setup_faults, 1):
        system = valid_system(500 + index)
        assert system.contract()
        capture(f"setup_{fault}", system, lambda s, value=fault: s.setup("G14C_REAL", fault=value))
    for index, stop_at in enumerate(("before_write", "after_write"), 1):
        system = valid_system(520 + index)
        assert system.contract()
        capture(f"setup_stop_{stop_at}", system, lambda s, value=stop_at: s.setup("G14C_REAL", stop_at=value))
    cleanup_faults = (
        "read_error", "unresolved", "stale_array", "hash_error", "write_error_no_effect",
        "write_error_reported", "post_read_error",
    )
    for index, fault in enumerate(cleanup_faults, 1):
        system = valid_system(540 + index)
        assert system.contract()
        assert system.setup("G14C_REAL")
        capture(f"cleanup_{fault}", system, lambda s, value=fault: s.cleanup("G14C_REAL", fault=value))
    for index, stop_at in enumerate(("before_write", "after_write"), 1):
        system = valid_system(560 + index)
        assert system.contract()
        assert system.setup("G14C_REAL")
        capture(f"cleanup_stop_{stop_at}", system, lambda s, value=stop_at: s.cleanup("G14C_REAL", stop_at=value))
    system = valid_system(570)
    assert system.contract()
    assert system.setup("G14C_REAL")
    system.rows[("Sheet1", 300)] = CellState("owned", "OTHER_RUN", "WRONG", ("data",))
    capture("cleanup_wrong_run_and_identity", system, lambda s: s.cleanup("G14C_REAL"))
    system = valid_system(571)
    assert system.contract()
    capture("cleanup_already_blank", system, lambda s: s.cleanup("G14C_REAL"))
    system = valid_system(572)
    assert system.contract()
    assert all(system.cleanup(role) for role in ROLES)
    assert system.close()
    capture("stale_authorization_after_close", system, lambda s: s.contract())
    return cases


def randomized_schedules(count: int, seed: int) -> dict:
    rng = random.Random(seed)
    total_operations = 0
    total_writes = 0
    unsafe_writes = 0
    invariant_failures = []
    for index in range(count):
        system = valid_system(index + 1000)
        scenario = rng.randrange(12)
        if scenario == 1:
            system.bindings["G14C_REAL"].row = 144
        elif scenario == 2:
            system.bindings["HIST_ARCHIVE"].row = 999
        elif scenario == 3:
            system.bindings["G14C_RATE"].row = system.bindings["G14C_REAL"].row
        elif scenario == 4:
            system.auth_run = "STALE"
        elif scenario == 5:
            system.rows[("Sheet1", 300)] = CellState("occupied", "PROD", "PROD", ("data",))
        contract_fault = {"G14C_REAL": rng.choice(["none", "none", "none", "read_error", "stale_array"])}
        ready = system.contract(contract_fault)
        if ready:
            roles = list(ROLES)
            rng.shuffle(roles)
            for role in roles:
                fault = rng.choice(["none"] * 8 + ["write_error_no_effect", "write_error_reported", "post_read_error"])
                stop = rng.choice(["none"] * 15 + ["before_write", "after_write"])
                system.setup(role, fault=fault, stop_at=stop)
            rng.shuffle(roles)
            for role in roles:
                binding = system.bindings[role]
                if rng.randrange(20) == 0:
                    system.rows[(binding.layer, binding.row)] = CellState("owned", "OTHER", "WRONG", ("data",))
                fault = rng.choice(["none"] * 8 + ["write_error_no_effect", "write_error_reported", "post_read_error"])
                stop = rng.choice(["none"] * 15 + ["before_write", "after_write"])
                system.cleanup(role, fault=fault, stop_at=stop)
            if all(system.rows[(binding.layer, binding.row)].kind == "blank" for binding in system.bindings.values()):
                system.close()
            if system.auth_state == "USED":
                system.contract()
        total_operations += system.operations
        total_writes += system.writes
        unsafe_writes += system.unsafe_writes
        if system.unsafe_writes:
            invariant_failures.append({"schedule": index, "unsafe_writes": system.unsafe_writes, "holds": system.holds[-5:]})
    return {
        "schedules": count,
        "operations": total_operations,
        "writes": total_writes,
        "unsafe_writes": unsafe_writes,
        "invariant_failure_count": len(invariant_failures),
        "sample_failures": invariant_failures[:10],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--schedules", type=int, default=100_000)
    parser.add_argument("--seed", type=int, default=20260717)
    args = parser.parse_args()
    unsafe_cases = unsafe_case_matrix()
    fault_cases = fault_injection_matrix()
    mutations = mutation_suite()
    randomized = randomized_schedules(args.schedules, args.seed)
    failures = []
    if not all(case["pass"] for case in unsafe_cases):
        failures.append("unsafe_case_matrix")
    if not all(case["pass"] for case in fault_cases):
        failures.append("fault_injection_matrix")
    if not all(case["detected"] for case in mutations):
        failures.append("mutation_suite")
    if randomized["operations"] < 1_000_000:
        failures.append("modeled_operations_below_1000000")
    if randomized["unsafe_writes"] != 0 or randomized["invariant_failure_count"] != 0:
        failures.append("randomized_unsafe_write")
    report = {
        "model": "independent-fixture-state-model-v1",
        "seed": args.seed,
        "unsafe_cases": unsafe_cases,
        "fault_injection": fault_cases,
        "mutation_results": mutations,
        "randomized": randomized,
        "summary": {
            "status": "PASS" if not failures else "FAIL",
            "failure_count": len(failures),
            "failures": failures,
            "unsafe_case_count": len(unsafe_cases),
            "unsafe_case_passes": sum(case["pass"] for case in unsafe_cases),
            "mutation_count": len(mutations),
            "mutations_detected": sum(case["detected"] for case in mutations),
            "fault_case_count": len(fault_cases),
            "fault_case_passes": sum(case["pass"] for case in fault_cases),
        },
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"] | report["randomized"], indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
