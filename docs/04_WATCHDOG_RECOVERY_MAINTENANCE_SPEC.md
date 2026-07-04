# Watchdog, Recovery, and Maintenance Spec

## AIW WATCHDOG V1

Purpose:
Protect the system when nobody is watching.

## Watchdog triggers

1. At every cycle start.
2. At every cycle end.
3. On timer if `%AIWorkerBusy = 1` longer than timeout.
4. Before START completes.
5. Before RELEASE/PROMOTION.

## Watchdog timeout variables

- `%AIWCycleTimeoutSec = 180`
- `%AIWProcessTimeoutSec = 120`
- `%AIWSendTimeoutSec = 90`
- `%AIWStuckProcessingMin = 5`
- `%AIWStuckSendingMin = 3`

## Watchdog checks

- `%AIWorkerBusy`
- `%AIWProcessing`
- `%AIWSending`
- `%AIWCycleStartedAt`
- rows stuck PROCESSING
- rows stuck SENDING
- timer state
- trigger state
- worker state
- Safe Mode state
- last cycle result
- repeated error count

## Watchdog actions

If stale busy lock:
- set RECOVERY
- Safe Mode ON
- release busy if timeout exceeded
- log

If stale processing lock:
- set RECOVERY
- move stuck PROCESSING rows to ERROR_PROCESS_REVIEW
- release process lock
- log

If stale send lock:
- set RECOVERY
- move stuck SENDING rows to ERROR_SEND_REVIEW
- release send lock
- log

If timer/trigger mismatch:
- if Worker ON and trigger OFF: HOLD, do not expect inbound queue
- if Worker OFF and timer ON: turn timer OFF
- log

## Recovery rule

Recovery never sends.
Recovery protects first, sends later after next clean cycle.

## Maintenance rule

Maintenance is lightweight:
- clears temp state
- updates health counters
- checks log sizes
- checks stale cycle IDs
- checks dashboard status data

Maintenance must not:
- run Archive live
- run Compactor live
- run TT5 live
- block READY_TO_SEND priority
- create heavy load during backlog
