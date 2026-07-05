# AIW Stage4B Send Dry-Run Phone Checklist

## Classification

CANDIDATE / HOLD FOR PHONE DRY-RUN PROOF

## Do Not Run

Do not run these during Stage4B:

- FINAL Send Sheet
- SS Controlled One-Row Send Proof
- AIW SEND 1
- FINAL Send Sheet LEGACY
- AIW AUTO LIVE START V1
- AIW AUTO LIVE TICK V1
- APP Start AI Worker
- timer profile activation
- trigger activation
- archive
- deadarchive
- compactor
- TT5

## Test 1: No-Ready Hold Path

Current Sheet state supports this test now:

- QueueView READY_TO_SEND count: 0

Run exactly:

- SS Safe Send Dry-Run

Expected:

- Task exits OK.
- It stops with NO_READY.
- It does not open a real send path.
- It does not press TextNow send.
- It does not change timer, live trigger, archive, deadarchive, compactor, or TT5.

Runlog must prove:

- SS Safe Send Dry-Run = ExitOK
- FINAL Send Sheet = 0
- SS Controlled One-Row Send Proof = 0
- AIW SEND 1 = 0
- button_send = 0
- timer/live/archive/deadarchive/compactor/TT5 = 0

## Test 2: Contact-Selection Dry-Run

Run this only after Test 1 passes and exactly one controlled READY_TO_SEND row exists.

Required setup:

- One approved test contact only.
- One READY_TO_SEND row only.
- Send live hold remains closed.
- Safe Mode/phone live hold remains controlled.

Run exactly:

- SS Safe Send Dry-Run

Expected:

- Task exits OK.
- It opens TextNow.
- It searches/picks the intended test contact.
- It stops before the message box/send button.
- It does not press TextNow send.

Runlog must prove:

- SS Safe Send Dry-Run = ExitOK
- DRYRUN_CONTACT_PICK_PASS or SEND_DRYRUN_PASS marker present
- %SSSentOne = 0
- FINAL Send Sheet = 0
- SS Controlled One-Row Send Proof = 0
- AIW SEND 1 = 0
- button_send = 0
- timer/live/archive/deadarchive/compactor/TT5 = 0

## After Test

- Export fresh Tasker runlog.
- Upload runlog to Drive.
- Keep status CANDIDATE / HOLD until audit reads the runlog.
