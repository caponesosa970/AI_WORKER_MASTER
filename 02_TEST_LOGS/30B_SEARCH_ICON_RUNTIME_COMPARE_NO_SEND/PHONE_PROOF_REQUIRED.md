# PHONE PROOF REQUIRED - 30B

Status: REQUIRED LATER / NOT CLAIMED BY CODEX

Codex does not approve phone import and does not claim phone proof.

If ChatGPT approves a phone test, Sosa must provide:

1. Tasker import/render proof for `AIW30B_SEARCH_ICON_RUNTIME_COMPARE_NO_SEND`.
2. Tasker runlog for the single diagnostic run.
3. Final `%AIW30BResult` value.
4. Final `%AIW30BStep` value.
5. `%AIW30BV15AErr` and `%AIW30BV15AErrMsg` if the V15A path fails.
6. `%AIW30BDashErr` and `%AIW30BDashErrMsg` if the Dashgood path runs.
7. Screenshot or screen recording showing TextNow stopped before typing, contact select, compose, or Send.

Expected safe outcomes:

- `V15A_ID_SEARCH_AND_FIELD_PASS`, or
- `DASHGOOD_TEXT_SEARCH_AND_FIELD_PASS`, or
- `DASHGOOD_TEXT_SEARCH_FAILED` with no Send/DONE/Archive path touched.

What stays blocked:

- phone number typing
- result/contact selection
- thread open
- compose focus
- reply insertion
- Send
- DONE write
- Archive
- live/timer
- capacity
- release
