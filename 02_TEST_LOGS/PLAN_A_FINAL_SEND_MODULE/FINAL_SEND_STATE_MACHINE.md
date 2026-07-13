# Final Send State Machine

## Successful Controlled Path

```text
exact row binding
  -> READY_TO_SEND verified
  -> SENDING written (maximum two attempts)
  -> exact row ID + SENDING read back (maximum two attempts)
  -> TextNow UI sequence
  -> compose populated by preserved source action
  -> button_send executes zero or one time
  -> SEND_CLICKED_AWAITING_CONFIRM written and read back
  -> owned lock released exactly once
```

## Terminal States

| State | Send click possible | Retry Send | DONE | Archive | Lock result |
| --- | ---: | ---: | ---: | ---: | --- |
| SEND_INVALID_PARAMETERS | 0 | NO | NO | NO | Not acquired |
| SEND_BLOCKED_LOCK | 0 | NO | NO | NO | Foreign lock untouched |
| SEND_ROW_READ_FAILED | 0 | NO | NO | NO | Owned lock released |
| SEND_ROW_BINDING_MISMATCH | 0 | NO | NO | NO | Owned lock released |
| SEND_ROW_NOT_READY | 0 | NO | NO | NO | Owned lock released |
| SEND_BAD_DATA_HELD | 0 | NO | NO | NO | Owned lock released |
| PRE_SEND_FAILURE_STATUS_UNKNOWN | 0 | NO | NO | NO | Owned lock released |
| SENDING_WRITE_FAILED | 0 | NO | NO | NO | Owned lock released |
| SENDING_READBACK_FAILED | 0 | NO | NO | NO | Owned lock released |
| PRE_SEND_UI_FAILED | 0 | NO | NO | NO | Owned lock released |
| SEND_OUTCOME_UNKNOWN_REVIEW | 1 max | NO | NO | NO | Owned lock released |
| SEND_CLICKED_AWAITING_CONFIRM | 1 max | NO | NO | NO | Owned lock released |
| POST_SEND_STATUS_UPDATE_FAILED | 1 max | NO | NO | NO | Owned lock released |

## Permanent Safety Rules

- No automatic Send retry.
- No return to READY_TO_SEND after a possible Send click.
- No DONE write from the Send action.
- No Archive from Tasks 71, 223, or 224.
- No `%LastBotReply` or `%LastBotTime` assignment in Task 223.
- `%SSSentOne` remains 0 because a click is not confirmation.
- A possible click always leaves the row non-sendable or in its last persistent `SENDING` state.
- Every owned-lock terminal path saves the final error, invokes `SS Lock Release HARD`, and restores the saved error.

## Selector Pending-State Block

Task 71 blocks before selecting a new READY row when QueueView contains any of:

- SENDING
- SEND_CLICKED_AWAITING_CONFIRM
- SEND_OUTCOME_UNKNOWN_REVIEW
- POST_SEND_STATUS_UPDATE_FAILED
- HOLD_PRE_SEND_FAILED

Blocked result: `SEND_BLOCKED_PENDING_CONFIRM`; worker calls: 0.
