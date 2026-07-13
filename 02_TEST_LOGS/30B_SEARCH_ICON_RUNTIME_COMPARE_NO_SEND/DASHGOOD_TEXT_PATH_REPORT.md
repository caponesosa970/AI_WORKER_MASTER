# DASHGOOD TEXT PATH REPORT - 30B1

## Purpose

If the V15A ID path does not complete, test the active Dashgood Task 71 text-search and search-field path without typing or selecting a result.

## Active Task Verified

- Active task ID: `71`
- Active task name: `FINAL Send Sheet`
- Legacy task excluded: ID `270`

## Copied Source Nodes

- Reset wait: active Task 71 source index 100
- Navigate up reset: active Task 71 source index 102
- Wait after reset Navigate up: active Task 71 source index 103
- Chats reset: active Task 71 source index 104
- Wait after Chats reset: active Task 71 source index 105
- Text `Search` action: active Task 71 source index 109
- Wait after Text `Search`: active Task 71 source index 110
- Search field click pair: active Task 71 source indices 122 and 123

## Repaired Failure Semantics

Dashgood AutoInput nodes retain Continue Task After Error OFF. Therefore no post-error Dashgood failure variable is claimed.

For each Dashgood exact-off AutoInput action:

1. 30B1 sets `%AIW30BStep=<STEP>`.
2. 30B1 sets `%AIW30BResult=<STEP>_NOT_COMPLETED` before the action.
3. The exact Dashgood AutoInput node runs.
4. If the action succeeds, 30B1 immediately sets `%AIW30BResult=<STEP>_PASS`.
5. If the action fails and Tasker stops, the last NOT_COMPLETED marker plus runlog is the failure proof.

Removed from 30B1:

- Dashgood retry block
- `%AIW30BResult=DASHGOOD_TEXT_SEARCH_FAILED` unsupported claim

If both Dashgood search-field nodes finish, the task sets `%AIW30BResult=DASHGOOD_TEXT_SEARCH_AND_FIELD_PASS` and stops.
