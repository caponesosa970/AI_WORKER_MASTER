# V15A ID PATH REPORT - 30B

## Purpose

Test the authoritative V15A ID-based search entry path first.

## Copied Source Nodes

- Launch TextNow: V15A source action list index 111
- Wait before navigation fallback: V15A source action list index 112
- Navigate up: V15A source action list index 113
- Wait after Navigate up: V15A source action list index 114
- Chats: V15A source action list index 115
- Wait after Chats: V15A source action list index 116
- SEARCH_ICON ID `menu_search`: V15A source action list index 120
- Wait after SEARCH_ICON: V15A source action list index 126
- SEARCH_FIELD ID `search_field`: V15A source action list index 130

## Runtime Result Variables

- Start step: `%AIW30BStep=V15A_ID_SEARCH_ATTEMPT`
- Error capture: `%AIW30BV15AErr` and `%AIW30BV15AErrMsg`
- Success result: `%AIW30BResult=V15A_ID_SEARCH_AND_FIELD_PASS`

## Safety

If both V15A SEARCH_ICON and SEARCH_FIELD complete without `%err`, the diagnostic stops immediately. It does not type, select, compose, send, or write to Sheets.

If either action reports an error, the diagnostic preserves the error values and proceeds to the Dashgood text-search comparison path.
