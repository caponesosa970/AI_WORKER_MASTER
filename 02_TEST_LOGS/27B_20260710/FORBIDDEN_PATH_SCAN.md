# Forbidden Path Scan

## Scan Result
This is a controlled-send candidate, so send-path actions are intentionally present only behind the hard gate. Codex does not approve Send.

| Path / Marker | Present in new task | Gate / Disposition |
|---|---:|---|
| `button_send` | YES | Behind `%AIW27BAllowSend=1` and `READY_TO_SEND`; candidate only |
| `DONE` write | YES | Behind `%AIW27BAllowSend=1` and `READY_TO_SEND`; candidate only |
| `%SSSentOne=1` | YES | Behind `%AIW27BAllowSend=1` and `READY_TO_SEND`; candidate only |
| Archive / DeadArchive / Compactor / TT5 | NO calls added | BLOCKED |
| live / timer / capacity | NO calls added | BLOCKED |
| UI Query / OCR / screenshot logic | NO | BLOCKED |

## Important HOLD
Phone import approved: NO.
Phone proof claimed: NO.
Send approved by Codex: NO.
