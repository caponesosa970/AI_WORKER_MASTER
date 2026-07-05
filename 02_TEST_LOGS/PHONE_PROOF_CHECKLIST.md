# Phone Proof Checklist

## Import proof

- Import XML into Tasker.
- Project appears.
- Tasks appear.
- Profiles appear.
- Scenes appear.
- Dashboard opens.
- No import error.

## Safe state proof

- Worker OFF.
- Safe Mode ON.
- Trigger/timer visible.
- Locks clear.
- Status button works.

## Start/stop proof

- START CAPPED turns trigger ON.
- START CAPPED turns timer ON.
- STOP turns trigger OFF.
- STOP turns timer OFF.
- Lockdown returns Safe Mode ON.

## Capture proof

- Prepare an external second-line TextNow sender before Stage 3A.
- Confirm sender is already signed in and can send without Google/TextNow verification.
- Use only the external sender for the controlled inbound test message.
- Enable only `FINAL TextNow Trigger` for Stage 3A trigger-only capture proof.
- Real TextNow message logs once.
- Dialing/ongoing/call notification does not log.
- Exact duplicate does not log.
- Different same-sender message does log.
- Disable `FINAL TextNow Trigger` immediately after the controlled capture.
- Capture Run Log after inbound capture.
- Capture Sheet row proof if available.

## Processor proof

- Add 3 NEW rows.
- One cycle processes according to cap.
- Rows move safely.
- Bad row goes review/error.

## Send proof

- One READY_TO_SEND row.
- One send action.
- TextNow visibly sends correct reply.
- Same row becomes DONE.
- No duplicate.
- No wrong recipient.
- Lock releases.

## Watchdog proof

- Simulate stale lock or stuck row.
- Watchdog detects it.
- Safe Mode ON.
- Recovery mode.
- No send during recovery.
- Stuck row moved to review/error.
- Log written.

## 50-contact cap proof

- Simulate over 50 active contacts.
- Overflow/HOLD fires.
- No live send from overflow.
- Log shows overflow.

## Maintenance proof

- Maintenance runs only when no urgent READY send exists.
- It does not block send.
- It does not run held Archive/Compactor/TT5.

## Release proof

- Export runlog.
- Export screenshots.
- Record SHA.
- Confirm final OFF / SAFE MODE ON / READY when stopped.
