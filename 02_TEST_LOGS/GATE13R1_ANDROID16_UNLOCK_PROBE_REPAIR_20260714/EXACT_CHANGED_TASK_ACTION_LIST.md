# Exact Changed Task and Action List

Existing Task 130 - `APP Start AI Worker`:

- Insert one `Perform Task: FINAL Device Unlock Probe` immediately before the former `%KEYG` guard.
- Change guard left side from `%KEYG` to `%AIWUnlockProbeResult`.
- Change guard right side from `off` to `UNLOCKED`.
- Preserve operator `!=` and existing `START_KEYGUARD_HOLD` block.

Existing Task 224 - `AIW GATE13 CONTROLLED TIMER TEST`:

- Insert one helper call immediately before the former `%KEYG` guard.
- Change the guard to `%AIWUnlockProbeResult != UNLOCKED`.
- Preserve `GATE13_KEYGUARD_HOLD`, authorization consumption, environment/screen checks, timer behavior, STOP behavior, and cleanup.

Existing Task 228 - `FINAL Live Tick Guard`:

- Insert one helper call immediately before the former `%KEYG` guard.
- Change the guard to `%AIWUnlockProbeResult != UNLOCKED`.
- Preserve `TICK_SKIPPED_KEYGUARD`, overlap guards, Queue Cycle call count, STOP behavior, and one-shot cleanup.

New Task 230 - `FINAL Device Unlock Probe`:

- 66 actions.
- Three Java Function actions plus fail-closed validation and result routing.

Project registry:

- Add Task ID 230 only.

No other runtime node changed.
