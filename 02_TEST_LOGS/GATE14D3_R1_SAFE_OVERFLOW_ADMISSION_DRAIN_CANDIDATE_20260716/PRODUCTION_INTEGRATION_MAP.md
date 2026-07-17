# Production Integration Map

## Admission

`FINAL Simple` unchanged
to `FINAL Simple Get Open Slot Row` repaired
to `TT5 Safe Overflow Admission Drain` main-slot claim.

When no slot is available, unchanged `FINAL Simple` routes to repaired `TT5 Log Current Message To OverflowInbox`, which calls the same engine in admission mode.

## Drain

`FINAL Queue Cycle` unchanged
to `TT5 Overflow Drain Cap` unchanged
to repaired `TT5 Overflow Drain One`
to the same engine in drain mode.

The controlled launcher calls only the repaired logger or drain wrapper. It does not call Queue Cycle, processing, OpenAI, TextNow, Send, confirmation, or Archive.
