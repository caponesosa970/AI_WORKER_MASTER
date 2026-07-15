# AIW Codex Accountability Report

Accountability ID: `AIW-GATE13R1-20260714`

Codex responsibility:

- The Gate 13 build accepted `%KEYG` as a source-proven unlocked-state signal.
- Direct phone proof disproved that assumption on the Moto Razr 2024 / Android 16 runtime.
- Codex is responsible for the unsupported static assumption and for limiting this repair to keyguard detection only.

Controller responsibility:

- Reconcile the actual XML and ZIP rather than relying on this summary.
- Identify what was independently verified before authorizing any import or phone step.

User/operator responsibility: NONE.

Claims supported statically:

- exact base SHA matched;
- Task ID 230 was unused;
- runtime changes are limited to Tasks 130, 224, 228, new Task 230, and Project tids;
- protected lifecycle nodes are raw-byte identical;
- the probe fails closed in the modeled error/blank/unresolved cases;
- package integrity passes;
- private artifacts remain untracked.

Unsupported claims:

- actual Tasker Java Function execution on Android 16;
- actual unlocked/locked result on the Moto;
- scheduled timer behavior after the repair;
- Gate 13 phone PASS;
- unattended/live readiness.

Tracker decision: no change; `12/14 locked = 86%`.

Final controller decision: pending ChatGPT full artifact audit and the repeated controlled busy-timer phone test.
