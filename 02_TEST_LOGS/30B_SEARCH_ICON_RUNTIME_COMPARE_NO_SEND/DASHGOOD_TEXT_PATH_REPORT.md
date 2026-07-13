# DASHGOOD TEXT PATH REPORT - 30B

## Purpose

If the V15A ID path fails, test the active Dashgood Task 71 text-search and search-field path without typing or selecting a result.

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
- Retry wait: active Task 71 source index 129
- Retry Text `Search`: active Task 71 source index 130
- Retry wait after Text `Search`: active Task 71 source index 131
- Retry search field click pair: active Task 71 source indices 136 and 137
- Retry field wait: active Task 71 source index 138

## Runtime Result Variables

- Reset step: `%AIW30BStep=DASHGOOD_RESET_NAVIGATION`
- Search step: `%AIW30BStep=DASHGOOD_TEXT_SEARCH_ATTEMPT`
- Retry step: `%AIW30BStep=DASHGOOD_SEARCH_FIELD_RETRY`
- Error capture: `%AIW30BDashErr` and `%AIW30BDashErrMsg`
- Success result: `%AIW30BResult=DASHGOOD_TEXT_SEARCH_AND_FIELD_PASS`
- Failure result: `%AIW30BResult=DASHGOOD_TEXT_SEARCH_FAILED`

## Safety

The Dashgood path is limited to reset/navigation, Text `Search`, and `search_field` clicks. It does not type a number, select a result, focus compose, paste, send, write DONE, write Sheets, or call Archive.
