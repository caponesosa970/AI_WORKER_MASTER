# Timer, Control, and Recovery Call Graph

## Existing Hazardous Paths Removed

- Start no longer calls `APP Reset Locks`, `FINAL AI Worker ON`, or `FINAL Queue Cycle`.
- Stop no longer calls `FINAL AI Worker Off`.
- Safe Recovery no longer calls `APP Reset Locks`.
- Boot profiles no longer call `APP Reset Locks`.
- Watchdogs no longer call lock-release, Sheet-repair, DeadArchive, or Compactor tasks.

## Final Permanent Paths

- Profile 137 -> Task 72 `FINAL AI Work Tick` -> Task 228 `FINAL Live Tick Guard` -> Task 199 `FINAL Queue Cycle` once maximum.
- Task 130 `APP Start AI Worker` -> Task 229 `FINAL Safe Startup Recovery` before profile enablement.
- Task 131 `APP Stop AI Worker` disables timer and trigger profiles before setting STOP and worker/timer off.
- Profiles 134 and 135 -> Task 183 `APP Safe Recovery` -> Stop -> Task 229.
- Task 229 -> Task 227 only for one awaiting-confirm or DONE recovery transition; it never calls Send tasks directly.
- Task 210 -> Task 13 only for read-only watchdog HOLD classification.

The permanent Gate 12 lifecycle call graph remains unchanged. A timer tick cannot directly call Tasks 71, 223, 225, 226, or 227.
