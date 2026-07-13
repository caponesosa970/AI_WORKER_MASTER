# System Integration Map

## Permanent Architecture

| Task ID | Name | Role | Actions | Incoming path |
| --- | --- | --- | ---: | --- |
| 71 | FINAL Send Sheet | Permanent QueueView selector | 158 | Task 199 once per cycle with `%par1=QUEUE_CYCLE` |
| 199 | FINAL Queue Cycle | Permanent queue controller | 99 | Existing controller/profile paths unchanged |
| 223 | FINAL Send One Bound Row | Permanent exact-row Send transaction | 937 | Task 71 or temporary Task 224 |
| 224 | AIW GATE9 CONTROLLED SEND TEST | Temporary removable Gate 9 launcher | 8 | Manual only; no profile, scene, or Perform Task references |

## Call Graph

```text
FINAL Queue Cycle (199)
  -> FINAL Send Sheet (71), exactly once, par1=QUEUE_CYCLE
       -> FINAL Send One Bound Row (223), at most once with selected SourceRow + ID

AIW GATE9 CONTROLLED SEND TEST (224)
  -> FINAL Send One Bound Row (223), exactly once when its one-time global gate is armed
```

Task 199 directly calls Task 223: NO.
Task 71 launches TextNow: NO.
Task 224 contains Sheet, AutoInput, keyboard, TextNow, or Send actions: NO.
Task 224 can be removed without changing Tasks 71, 199, or 223: YES.

Normalized Task 223 node SHA256: `2B91FBB6B3B3CE4C0E539DA2D2129111D09C95D7E1B7BE9198530250346ACD4B`.

## Task 199 Send-Block Change

- Before: three same-cycle `FINAL Send Sheet` calls with two waits and conditional repeat blocks.
- After: one `FINAL Send Sheet` call with `%par1=QUEUE_CYCLE`.
- Direct worker call: zero.
- Existing non-Send logic: semantically unchanged.
- Existing maintenance/Archive branch: preserved, not expanded, and outside the changed Send block.

## Stable Output Contract for Later Gates

Task 223 permanently emits these unresolved terminal states for later modules:

- `SEND_CLICKED_AWAITING_CONFIRM`
- `SEND_OUTCOME_UNKNOWN_REVIEW`
- `POST_SEND_STATUS_UPDATE_FAILED`
- `HOLD_PRE_SEND_FAILED`

A later confirmation module may consume confirmed `SEND_CLICKED_AWAITING_CONFIRM`. A later Archive module may consume only confirmed completion. Neither is implemented here.

## Changed-Task Classification

Unclassified changed tasks: 0.
Unchanged task-byte differences: 0.
Profile references changed: 0.
Scene references changed: 0.
