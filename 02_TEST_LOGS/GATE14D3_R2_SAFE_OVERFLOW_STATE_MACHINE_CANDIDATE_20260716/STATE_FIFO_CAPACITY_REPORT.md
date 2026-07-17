# State, FIFO, And Capacity Report

State path:

`PENDING -> DRAINING -> OVERFLOW_ADMITTING payload -> NEW -> MAIN_COMMITTED -> DRAINED`

`OVERFLOW_REVIEW` is a durable hold. PENDING, DRAINING, MAIN_COMMITTED, and OVERFLOW_REVIEW block newer direct admission.

FIFO authority is numeric LoggedAt ascending, then physical OverflowInbox source row ascending.

Configured V1 overflow bounds are source rows 2-1000, for capacity 999. At capacity the task does not overwrite, coerce a target, or report success. It returns `OVERFLOW_CAPACITY_HOLD` and preserves the event in ingress-hold globals.

Live grid/formula alignment is not changed in this build and must be verified before phone execution.
