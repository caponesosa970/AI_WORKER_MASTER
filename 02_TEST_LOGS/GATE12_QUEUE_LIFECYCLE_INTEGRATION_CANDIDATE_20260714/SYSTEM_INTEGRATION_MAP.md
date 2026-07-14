# System Integration Map

## Permanent Production Route

`FINAL Queue Cycle (199)`

1. Validates production or controlled mode.
2. Acquires `AIWorkerBusy` ownership.
3. Calls `FINAL Queue Lifecycle Router (227)` exactly once.
4. Stops further lifecycle work when the router handles, blocks, or fails.
5. Reaches the one shared `FINAL Send Sheet (71)` node only when the lifecycle router returns clear and Send is allowed.
6. Releases `AIWorkerBusy` through one common epilogue.

## Lifecycle Router

`FINAL Queue Lifecycle Router (227)`

- Blocks on active transaction locks.
- Reads QueueView with two bounded attempts.
- Blocks multiple awaiting-confirm rows and dangerous unresolved Send states.
- Routes exactly one awaiting-confirm row to `FINAL Confirm One Bound Row (225)`.
- Otherwise routes the numerically lowest DONE source row to `FINAL Archive One Bound Row (226)`.
- Otherwise returns lifecycle clear without mutation.

## Send Route

`FINAL Queue Cycle (199) -> FINAL Send Sheet (71) -> FINAL Send One Bound Row (223)`

Task 71 remains the only caller of Task 223.

## Controlled Launcher

`AIW GATE12 CONTROLLED QUEUE CYCLE TEST (224) -> FINAL Queue Cycle (199)`

The launcher consumes one manual authorization, sets one latch, calls Task 199 once, clears the latch defensively, and stops. It contains no Sheet, UI, Send, confirmation, or Archive action.

## Disconnected Legacy Route

Task 199 no longer calls `QUEUE Archive Drain Silent` or Task 75. Existing broad Archive tasks remain present and unchanged but are not in the permanent queue path.
