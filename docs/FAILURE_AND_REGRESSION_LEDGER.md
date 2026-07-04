# Failure and Regression Ledger

## F001 — Broken dashboard actions

Failure:
Dashboard button exists but task action is empty or missing.

Prevention:
Every scene clickTask must resolve to existing task ID. Every wrapper task must contain action.

Promotion blocker:
Yes.

## F002 — Missing task definitions

Failure:
Project/profile/scene references task IDs not defined.

Prevention:
Static audit checks project tids, profile refs, scene clickTask refs, Perform Task refs.

Promotion blocker:
Yes.

## F003 — Encoding corruption

Failure:
Separators corrupted into mojibake.

Prevention:
UTF-8 preservation. Mojibake count must be 0.

Promotion blocker:
Yes.

## F004 — AutoSheets JSON/structured output drift

Failure:
`json:true` or `<se>true</se>` appears unexpectedly.

Prevention:
Static audit. Runtime guard where possible.

Promotion blocker:
Yes.

## F005 — Literal variable writes

Failure:
Unresolved Tasker variables written into Sheet/Archive.

Prevention:
Pre-write literal variable guard.

Promotion blocker:
Yes.

## F006 — Ghost rows

Failure:
Blank sender/message row gets status/reply.

Prevention:
Row validation before write/process.

Promotion blocker:
Yes.

## F007 — Duplicate notification logging

Failure:
Notification swipe/update creates duplicate row.

Prevention:
Exact duplicate short-window guard using sender/message/ticker.

Promotion blocker:
Yes.

## F008 — Call notification logging

Failure:
Dialing/ongoing/missed/voicemail logs as message.

Prevention:
AutoNotification filter and message content validation.

Promotion blocker:
Yes.

## F009 — Wrong-recipient send

Failure:
Reply sent to wrong TextNow contact.

Prevention:
One-send UI lock, sender key validation, search target validation, no stale row reuse.

Promotion blocker:
Critical.

## F010 — Stale reply send

Failure:
Old reply sent to later/different row.

Prevention:
Row ID + sender key + status gate before send.

Promotion blocker:
Critical.

## F011 — DONE before send

Failure:
Row marked DONE before TextNow send completes.

Prevention:
DONE only after visible send path completes.

Promotion blocker:
Critical.

## F012 — Lock not released

Failure:
System stuck busy/processing/sending.

Prevention:
Exit handlers and watchdog.

Promotion blocker:
Yes until watchdog proven.

## F013 — Trigger off after start/reset

Failure:
System ON but inbound trigger OFF.

Prevention:
Start turns trigger+timer ON; watchdog checks mismatch.

Promotion blocker:
Yes.

## F014 — Archive/Compactor/TT5 early live risk

Failure:
Heavy cleanup systems run before proven.

Prevention:
Keep HOLD/OFF.

Promotion blocker:
Yes if live-enabled.

## F015 — Overload without backpressure

Failure:
More contacts/rows than system can safely handle.

Prevention:
50-contact cap, BACKLOG/HOLD mode, overflow handling.

Promotion blocker:
Yes.
