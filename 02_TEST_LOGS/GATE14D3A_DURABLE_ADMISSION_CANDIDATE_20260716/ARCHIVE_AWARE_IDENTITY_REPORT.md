# Archive-Aware Identity Report

Task 243 performs fail-closed read-only identity checks across:

- Sheet1 A2:C201
- OverflowInbox B2:D986
- Archive A2:C1000
- DeadArchive A2:A1000

Classifications:

- no match: ELIGIBLE
- one active same-ID/same-payload match: EXACT_DUPLICATE
- same active ID/different payload: ID_COLLISION_REVIEW
- multiple active matches: DUPLICATE_MAIN_REVIEW
- Archive ID match: HISTORICAL_DUPLICATE
- DeadArchive ID match: EVENT_HISTORY_REVIEW

Archive and DeadArchive are read only. D3A contains no Archive, DeadArchive, or drain mutation.
