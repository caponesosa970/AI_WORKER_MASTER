# Final Send State Machine

## Successful Click Path

`READY_TO_SEND` -> verified `SENDING` -> TextNow UI -> one `button_send` -> verified `SEND_CLICKED_AWAITING_CONFIRM` -> lock release.

No `DONE`, Archive, `%SSSentOne=1`, `LastBotReply`, or `LastBotTime` occurs in this module.

## Numeric Send-Error Path

1. Save `%err` and `%errmsg` immediately.
2. Never click Send again.
3. Attempt and read back `SEND_OUTCOME_UNKNOWN_REVIEW`.
4. Report that result only when exact ID/status readback confirms it.
5. Otherwise attempt `POST_SEND_STATUS_UPDATE_FAILED` at most twice.
6. Preserve the original Send error through lock release.

## AutoSheets Failure Contract

Every Task 71/223 AutoSheets action contains `se=false`. Each operation has at most two identical attempts, one three-second retry wait, numeric `%err` checks after both attempts, and deterministic failure handling. Task 223 contains no stop between lock acquisition and its common lock-release helper.
