# Static Scenario Matrix

| Scenario | Result |
|---|---|
| Owner mismatch release | PASS: rejected |
| Live owner older than eight seconds | PASS: no age clear exists |
| Same OriginalID and same payload | PASS: exact duplicate suppressed |
| Same OriginalID and different payload | PASS: ID_COLLISION_REVIEW |
| Multiple Sheet1 copies | PASS: DUPLICATE_MAIN_REVIEW |
| Stale AutoSheets output | PASS: Array Clear before each read |
| Invalid view candidate | PASS: direct-row verification blocks write |
| PENDING append | PASS: exact A:N readback |
| FIFO tie | PASS: lower source row first |
| Full payload before NEW | PASS |
| Partial main commit rerun | PASS: zero second main-row write |
| Failed drain evidence | PASS: Attempts and LastError persisted |
| Capacity 999 reached | PASS: no overwrite, capacity hold |
| STOP before acquisition | PASS: no new transaction |
| Drain Cap empty/moved/reconciled/hold | PASS: exact constants |
| Controlled five-mode isolation | PASS |
| API/TextNow/lifecycle reachability | PASS: zero |

Independent executable model cases all passed.
