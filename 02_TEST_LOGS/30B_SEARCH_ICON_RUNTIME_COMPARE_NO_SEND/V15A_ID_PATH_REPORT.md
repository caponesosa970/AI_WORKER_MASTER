# V15A ID PATH REPORT - 30B1

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

## Markers

- `%AIW30BResult=V15A_NAVIGATE_UP_NOT_COMPLETED` before Navigate up
- `%AIW30BResult=V15A_NAVIGATE_UP_PASS` immediately after Navigate up succeeds
- `%AIW30BResult=V15A_CHATS_NOT_COMPLETED` before Chats
- `%AIW30BResult=V15A_CHATS_PASS` immediately after Chats succeeds
- `%AIW30BResult=V15A_ID_SEARCH_NOT_COMPLETED` before V15A SEARCH_ICON
- `%AIW30BResult=V15A_ID_SEARCH_PASS` immediately after V15A SEARCH_ICON succeeds
- `%AIW30BResult=V15A_SEARCH_FIELD_NOT_COMPLETED` before V15A SEARCH_FIELD
- `%AIW30BResult=V15A_SEARCH_FIELD_PASS` immediately after V15A SEARCH_FIELD succeeds

If V15A Search and Search Field both pass, the task sets `%AIW30BResult=V15A_ID_SEARCH_AND_FIELD_PASS` and stops.
