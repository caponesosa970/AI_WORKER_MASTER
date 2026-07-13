# Regression And Forbidden Path Scan - 31A

## Regression Checks

- Original 27B unchanged: TRUE
- New 31A task present: YES
- Duplicate task IDs: `0`
- Duplicate task names: `0`
- Missing Perform Task refs: `0`
- Search-lane-only semantic diff: PASS
- Downstream actions unchanged: TRUE
- Original 31A current-key claim: REJECTED / DISCONTINUED
- 31A1 sanitized XML comparison after credential redaction: IDENTICAL
- 31A1 Task 224 unchanged byte-for-byte: TRUE
- 31A1 runtime actions changed: NO
- 31A1 discontinued credential remaining count: `0`
- 31A1 current credential occurrence count: `1`
- 31B AutoSheets row-read retry added only to task 224: TRUE
- 31B clears all five AutoSheets outputs plus `%err`/`%errmsg` before both attempts: TRUE
- 31B validates all five first elements and all five array counts equal `1`: TRUE
- 31B AutoSheets attempts maximum: `2`
- 31B retry wait: `3` seconds
- 31B final AutoSheets failure sets `%AIW27BAllowSend=0`: TRUE
- 31B final AutoSheets failure performs `SS Lock Release HARD`: TRUE
- 31B final AutoSheets failure stops before TextNow launch: TRUE
- 31B Search lane unchanged semantically: TRUE
- 31B downstream runtime unchanged semantically excluding Tasker action sr/location renumbering: TRUE
- ZIP integrity: PASS
- Tracker unchanged: `8/14 locked = 57%`
- Sheet changed: NO

## Forbidden Path Scan

These markers are expected elsewhere in the full project because this is a full-project import. For the new 31A task, the scan result is:

- Archive/DeadArchive/Compactor/TT5 marker in 31A task: True
- live/timer marker in 31A task: False
- UI Query marker in 31A task: False

31A preserves the existing controlled-send downstream path from 27B but does not approve it. Phone import and controlled Send remain ChatGPT-gated.

## Historical Regression Coverage

- 23A/23B/23C malformed-class issue: XML parse and TaskerData root checked.
- 26A/26B false-pass class: 30B1 phone result used successful `search_field` reach as positive end-state validation, not the intermediate Text Search marker alone.
- 27B source-preservation issue: original 27B remains unchanged and 31A changes only the cloned task.
- SEARCH_ICON runtime/UI failure: 31A replaces only the failing search lane with Dashgood active Task 71 recovery logic.
- 31A credential provenance failure: 31A1 corrects only the private credential value and keeps runtime actions unchanged.
- 31A AutoSheets timeout after Send lock: 31B adds one retry and lock-release failure handling before TextNow launch.
