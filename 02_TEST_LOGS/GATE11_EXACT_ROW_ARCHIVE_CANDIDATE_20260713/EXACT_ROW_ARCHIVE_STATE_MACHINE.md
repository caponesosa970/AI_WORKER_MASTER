# Exact-Row Archive State Machine

## Entry

1. Validate dynamic source row and expected ID before acquiring a lock.
2. Block if Archive, Send, Confirm, Processing, DeadArchive, or Compactor lock is active.
3. Acquire only the Archive lock and record local ownership.

## Source Binding

1. Read exact `Sheet1!A%archive_row:I%archive_row`, with one retry maximum.
2. Bind A:I and require exact ID, status `DONE`, required data, no unresolved variable, and no `#ERROR`.
3. If the exact source row is blank, scan Archive and return `ARCHIVE_ALREADY_COMPLETE` only when one valid matching Archive row exists.

## Destination Decision

- Duplicate count greater than one: `ARCHIVE_DUPLICATE_ID_HOLD`.
- One exact matching Archive row: verify A:I and populated J, then use source-clear recovery only.
- One conflicting Archive row: `ARCHIVE_ID_CONFLICT_HOLD`.
- No matching Archive row: select the first verified empty Archive ID row; never use array count as the target row.

## New Copy

1. Re-read and revalidate the exact source A:I immediately before writing.
2. Write exactly one Archive A:J row with bounded retry.
3. Read back that exact Archive row and require exact A:I, exact timestamp J, and exactly one occurrence of the expected ID.
4. Copy failure or mismatch never reaches source clear.

## Source Clear

1. Re-read exact source A:I immediately before clear and require it to remain identical and `DONE`.
2. Clear exact Sheet1 A:I only.
3. Read exact Sheet1 A:I and require all nine cells blank.
4. If clear fails after a verified copy, return `ARCHIVE_COPIED_SOURCE_CLEAR_FAILED`; retry detects the existing copy and cannot append a duplicate.

## Terminal Results

- `ARCHIVE_DONE_VERIFIED`
- `ARCHIVE_ALREADY_COMPLETE`
- `ARCHIVE_DUPLICATE_ID_HOLD`
- `ARCHIVE_ID_CONFLICT_HOLD`
- `ARCHIVE_COPY_VERIFY_FAILED`
- `ARCHIVE_SOURCE_CHANGED_AFTER_COPY`
- `ARCHIVE_COPIED_SOURCE_CLEAR_FAILED`
- deterministic source-read, Archive-scan, write, readback, clear, input, data, target-full, and lock-blocked failures

Every owned-lock terminal path reaches one guarded release block. Pre-lock and lock-conflict exits never release another run's lock.
