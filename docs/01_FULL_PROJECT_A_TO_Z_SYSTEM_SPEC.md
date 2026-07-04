# AI Worker Full Project A–Z System Spec

## A — Final project purpose

AI Worker is a Tasker-based phone automation system that receives TextNow messages, logs them, processes them with OpenAI, sends safe replies through TextNow, and protects itself from duplicates, wrong recipients, stale replies, overload, stuck locks, bad rows, bad triggers, and runtime drift.

## B — Base device

Primary proof device:
- Moto Razr 2024

Known support environment from screenshots:
- Tasker 6.7.6-beta
- AutoInput 3.0.12

## C — Core apps/plugins

- Tasker
- AutoNotification
- AutoInput
- AutoSheets
- TextNow
- Google Sheets
- OpenAI API

## D — Required runtime format

Final output must be Tasker XML:
- `.xml`
- `<TaskerData ...>`
- full tasks/profiles/scenes/project registry
- plugin bundles preserved
- importable back into Tasker

## E — System layers

Build100 must include all layers:

1. Capture / inbound logger.
2. Queue writer.
3. Queue pressure reader.
4. Mode decision engine.
5. Processor.
6. Sender.
7. Logger/proof system.
8. Watchdog.
9. Recovery.
10. Maintenance cleaner.
11. Dashboard.
12. Failure ledger.
13. Regression ledger.
14. Dependency registry.
15. System registry.
16. Validation engine.
17. Promotion engine.
18. Release controller.
19. HOLD controller.
20. Phone proof checklist.

## F — Operating target

Target:
- 50 active contacts capped design.

Speed model:
- Process multiple rows per cycle.
- Send one TextNow message max per cycle.
- Speed up only when backlog exists.
- Slow/hold/recover when risk exists.

## G — Live start behavior

START CAPPED must:
1. Verify config.
2. Clear stale safe locks if allowed.
3. Turn Worker ON.
4. Keep or set Safe Mode according to selected mode.
5. Turn on TextNow trigger.
6. Turn on timer profile.
7. Set tick route to `AIW AUTO LIVE TICK V1`.
8. Log START event.

## H — Stop/lockdown behavior

STOP / LOCKDOWN must:
1. Turn Worker OFF.
2. Turn Safe Mode ON.
3. Turn off TextNow trigger.
4. Turn off timer profile.
5. Release non-active stale locks.
6. Leave rows safe.
7. Log STOP/LOCKDOWN event.

## I — Capture layer

Inbound TextNow notifications must:
1. Accept real TextNow message notifications.
2. Reject call/dialing/ongoing call/voicemail/bad notifications.
3. Normalize sender.
4. Preserve ticker backup.
5. Create one clean Sheet1 row.
6. Deduplicate exact same sender/message/ticker within short window.
7. Never skip different messages from same sender.

## J — Queue layer

Queue must track:
- NEW
- PROCESSING
- REVIEW_READY
- READY_TO_SEND
- SENDING
- DONE
- ERROR_PROCESS_REVIEW
- ERROR_SEND_REVIEW
- SKIP_BAD_DATA
- HOLD_OVERFLOW
- GROUPED

## K — 50-contact cap

Active contacts = unique senders among unfinished rows.

If active contacts > 50:
- do not process/send overflow live
- mark overflow HOLD_OVERFLOW or REVIEW_READY
- log overflow
- mode HOLD or BACKPRESSURE

## L — Mode decision engine

Modes:
- NORMAL
- BACKLOG
- HOLD
- RECOVERY
- MAINTENANCE

NORMAL:
- queue small
- errors low
- locks clear

BACKLOG:
- active queue growing
- within cap
- errors under cap

HOLD:
- cap exceeded
- errors too high
- unsafe config
- trigger/timer mismatch
- repeated failure pattern

RECOVERY:
- stale lock
- stuck row
- previous cycle failed to exit

MAINTENANCE:
- no urgent sends
- safe cleanup window

## M — Processor

Processor must:
- claim only NEW rows
- process each row safely one at a time
- batch up to 2 in NORMAL
- batch up to 5 in BACKLOG
- never touch DONE/SENDING/ERROR rows except through recovery rules
- write REVIEW_READY if Safe Mode ON
- write READY_TO_SEND only when controlled live mode allows

## N — Sender

Sender must:
- send only one READY_TO_SEND row per cycle
- set SENDING before UI work
- search/select correct TextNow recipient
- paste reply
- wait 1000 ms after paste
- tap send
- mark DONE only after send path completes
- on failure mark ERROR_SEND_REVIEW
- always release send lock

## O — Logger

Logger must record:
- cycle start/end
- cycle ID
- active contact count
- NEW count
- READY count
- errors
- overflow
- mode
- row before/after statuses
- send attempt result
- watchdog events
- recovery events
- maintenance events

## P — Watchdog

Watchdog must be its own system:
- cycle watchdog
- lock watchdog
- row watchdog
- trigger/timer watchdog
- send watchdog

It must not send during recovery.

## Q — Recovery

Recovery must:
- turn Safe Mode ON
- block sending during recovery
- release stale locks only when stale
- move stuck PROCESSING rows to ERROR_PROCESS_REVIEW
- move stuck SENDING rows to ERROR_SEND_REVIEW
- log every action

## R — Maintenance

Maintenance must:
- run only when no urgent READY sends exist
- be lightweight
- clean stale temp variables
- check health counters
- optionally compact logs only when proven
- never block urgent send path

## S — Dashboard

Dashboard must show:
- Worker ON/OFF
- Safe Mode
- Trigger state
- Timer state
- Tick mode
- Active contacts
- NEW count
- READY count
- Error count
- Overflow count
- Locks
- Last cycle result
- Last watchdog result

Top controls:
- STATUS
- START CAPPED
- STOP / LOCKDOWN
- RUN ONE CYCLE
- SAFE MODE ON
- RESET LOCKS

Bottom controls:
- TEST SEND 1
- PROCESS BATCH TEST
- WATCHDOG TEST
- QUEUE PRESSURE CHECK
- HEALTH LOG
- ARCHIVE HOLD
- COMPACTOR HOLD
- TT5 HOLD

## T — Failure ledger

Every known failure must have:
- failure ID
- description
- prevention rule
- audit check
- runtime check if applicable
- promotion blocker status

## U — Regression ledger

If a previous failure pattern returns:
- block release
- mark regression
- require patch
- require proof after patch

## V — Validation engine

Validation must run:
- before START
- before PROCESS
- before SEND
- before RELEASE/PROMOTION

## W — Promotion engine

No candidate promotes unless:
- XML static audit pass
- Tasker import proof
- dashboard proof
- controlled processor proof
- controlled send proof
- watchdog proof
- recovery proof
- runlog proof
- final clean state proof

## X — Release controller

Release must package:
- final XML
- source ZIP
- SHA inventory
- proof summary
- HOLD list
- phone proof
- runlog
- source comparison

## Y — Private data

The primary XML must be WITH_KEY/private.
Preserve private key/task/local info inside XML.
Do not print secrets in markdown.

## Z — Final boundary

Build100 is a candidate until phone proof passes.
No static file can be called final release.
