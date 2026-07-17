# Processor Transaction State Machine

## Common gate

1. Accept only MARK_PROCESSING, COMMIT_SUCCESS, or COMMIT_FAILURE.
2. Validate row 2-201 and concrete ID/sender/message.
3. Read exact `Sheet1!A<row>:E<row>` with at most two attempts.
4. Require exact A/B/C equality before every write.
5. Treat exact readback as authority even when an Update Cells action reports an error.

## MARK_PROCESSING

`NEW + blank Reply -> PROCESSING`, verified by exact A:E readback. Any mismatched binding, status, or Reply causes zero authorization for OpenAI.

## COMMIT_SUCCESS

`PROCESSING -> exact Reply verified -> READY_TO_SEND or REVIEW_READY verified`.

An already-equal Reply is idempotent. A conflicting Reply holds before status mutation. If Reply is verified but final status cannot be verified, the engine attempts and reads back `ERROR_PROCESS_REVIEW`; otherwise it leaves the observed non-NEW state and returns `PROCESS_PARTIAL_WRITE_HOLD`.

## COMMIT_FAILURE

Only `NEW` or `PROCESSING` may enter. The classified failure status is accepted only after exact A/B/C and D readback. Terminal/review/send states are never overwritten.

The temporary partial-failure hook requires the exact controlled mode, row 142, reserved synthetic ID, and one-shot authorization. It is consumed at Task 233 entry and is unreachable from ordinary production data.
