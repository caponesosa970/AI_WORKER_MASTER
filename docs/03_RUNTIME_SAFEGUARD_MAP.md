# Runtime Safeguard Map

## Startup safeguards

Fires:
- before START CAPPED completes

Checks:
- XML/system config present
- key task exists
- sheet config exists
- TextNow trigger exists
- timer profile exists
- dashboard task refs exist
- stale locks safe to clear

Actions:
- if pass: Worker ON, trigger ON, timer ON
- if fail: Safe Mode ON, HOLD, log failure

## Capture safeguards

Fires:
- on AutoNotification TextNow Created/Updated

Checks:
- app is TextNow
- notification is real message
- sender exists
- message exists
- not call/dialing/ongoing/voicemail
- not exact duplicate within short window

Actions:
- write clean NEW row
- bad row SKIP_BAD_DATA
- duplicate SKIP_DUPLICATE

## Queue pressure safeguards

Fires:
- every tick before process/send

Checks:
- active unique sender count
- NEW count
- READY count
- error count
- overflow count
- stuck statuses

Actions:
- set NORMAL/BACKLOG/HOLD/RECOVERY/MAINTENANCE

## Processor safeguards

Fires:
- before batch process
- before each row process

Checks:
- Worker ON
- not in HOLD
- processing lock clear
- row status NEW
- sender/message valid
- not duplicate
- active contact cap not exceeded

Actions:
- set PROCESSING
- build reply
- set REVIEW_READY or READY_TO_SEND
- errors to ERROR_PROCESS_REVIEW
- release process lock

## Send safeguards

Fires:
- before send
- before TextNow UI actions
- after send attempt

Checks:
- send lock clear
- one-send cap not exceeded
- status READY_TO_SEND
- reply valid
- sender key valid
- not in Safe Mode unless controlled proof
- not overflow

Actions:
- set SENDING
- paste
- wait 1000 ms
- send
- DONE after completion
- ERROR_SEND_REVIEW on failure
- release send lock

## Watchdog safeguards

Fires:
- cycle start
- cycle end
- periodic tick when busy too long

Checks:
- stale busy lock
- stale processing lock
- stale send lock
- row stuck PROCESSING
- row stuck SENDING
- timer ON while worker OFF
- trigger OFF while worker ON
- cycle duration too long

Actions:
- Safe Mode ON
- mode RECOVERY
- no send
- stale locks released
- stuck rows moved to review/error
- log WATCHDOG_RECOVERY

## Maintenance safeguards

Fires:
- only if no urgent READY sends
- only if locks clear
- only if mode allows

Checks:
- temp variables
- old cycle markers
- log pressure
- stale counters

Actions:
- clean light temp state
- never block send priority
- never run heavy compactor unless separately proven

## Release safeguards

Fires:
- before promotion/release

Checks:
- static audit
- phone import proof
- dashboard proof
- send proof
- watchdog proof
- recovery proof
- runlog proof
- SHA lock
- HOLD list confirmed

Actions:
- promote only if all gates pass
- otherwise HOLD
