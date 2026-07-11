# Send Gate Guard Report

## Gate Variable
`%AIW27BAllowSend`

Default set by the task:
`0`

## Gate Behavior
If `%AIW27BAllowSend != 1`:
- stops before TextNow
- stops before `button_send`
- does not write `DONE`
- does not set `%SSSentOne=1`
- does not Archive
- does not change row status to `DONE`

If `%AIW27BAllowSend = 1`:
- send-capable behavior is still blocked unless row 75 status is `READY_TO_SEND`.
- this condition is candidate-only and requires ChatGPT audit plus future explicit Sosa phone-proof operation.

## Rechecks
The task rechecks `%AIW27BAllowSend=1` before result select and before `button_send`.
