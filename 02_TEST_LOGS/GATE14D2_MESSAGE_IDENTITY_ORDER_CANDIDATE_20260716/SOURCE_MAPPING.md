# Production Source Mapping

## Active exact-ID behavior

`FINAL Simple` has one Perform Task call to `TT5 Simple Sheet Duplicate Guard`.

TT5:

1. Reads the Sheet ID column.
2. Iterates the returned IDs.
3. Sets duplicate result only when `%SNCheckDummy` exactly equals `%SNid`.
4. Returns a duplicate marker for an existing exact ID.
5. Returns a pass marker for a unique ID.

Gate 14D2 requires those explicit TT5 result markers so TT5's read-error pass-open cannot count as a valid unique-ID classification.

## Historical disabled behavior

The `%SNFingerprint` assignment, `%SNDupeAge` calculation, 180-second If condition, duplicate log, Stop, and End If in `FINAL Simple` are disabled. Gate 14D2 does not call, copy, enable, repair, or claim this path.
