# Control Flow and Exact-Once Audit

## AutoSheets Action Ledger

| Task | Output action | Plugin | Continue after error | Preserved fields |
| ---: | ---: | --- | --- | --- |
| 71 | 20 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 71 | 72 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 53 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 125 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 255 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 264 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 277 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 314 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 366 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 375 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 395 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 432 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 575 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 584 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 597 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 634 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 696 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 705 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 718 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 755 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 806 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 815 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 828 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 865 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 916 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |
| 223 | 925 | AutoSheets | `se=false` | bundle/range/output/timeout unchanged |

Assertions:

- Task 71 AutoSheets: 2 total, 2 `se=false`, 0 missing.
- Task 223 AutoSheets: 24 total, 24 `se=false`, 0 missing.
- Retry operation pairs: 1 in Task 71 and 12 in Task 223.
- First-attempt numeric error checks: PASS for every pair.
- Second-attempt numeric error checks: PASS for every pair.
- Three-second retry wait: exactly one per pair.
- Maximum attempts per operation: 2.
- AutoSheets error after lock acquisition that can terminate before cleanup: 0.

## Send-Branch Change Ledger

| Task | Output action | Classified purpose |
| ---: | ---: | --- |
| 223 | 689 | preserve Send-button numeric error before any plugin reset |
| 223 | 690 | preserve Send-button error message before any plugin reset |
| 223 | 691 | initialize shared post-Send fallback latch |
| 223 | 693 | ambiguous Send-button outcome using preserved error |
| 223 | 792 | unknown outcome exact status confirmed |
| 223 | 793 | confirmed unknown outcome result |
| 223 | 794 | unknown outcome never claims confirmed send |
| 223 | 795 | unknown outcome requires review |
| 223 | 796 | unknown outcome preserves original Send error in SSLastError |
| 223 | 797 | unknown outcome preserves original Send error for lock-release restore |
| 223 | 798 | confirmed unknown outcome terminal |
| 223 | 799 | unknown outcome status was not confirmed |
| 223 | 800 | route unconfirmed unknown outcome to shared fallback |
| 223 | 801 | end unknown outcome confirmation decision |
| 223 | 909 | route unconfirmed awaiting-confirm outcome to shared fallback |
| 223 | 913 | shared post-Send fallback required |
| 223 | 914 | POST_SEND_STATUS_UPDATE_FAILED fallback write attempt 1: clear err |
| 223 | 915 | POST_SEND_STATUS_UPDATE_FAILED fallback write attempt 1: clear errmsg |
| 223 | 916 | POST_SEND_STATUS_UPDATE_FAILED fallback write: Update Cells attempt 1 |
| 223 | 917 | POST_SEND_STATUS_UPDATE_FAILED fallback write: assume attempt 1 success |
| 223 | 918 | POST_SEND_STATUS_UPDATE_FAILED fallback write: attempt 1 numeric error check |
| 223 | 919 | POST_SEND_STATUS_UPDATE_FAILED fallback write: attempt 1 failed |
| 223 | 920 | POST_SEND_STATUS_UPDATE_FAILED fallback write: end attempt 1 error check |
| 223 | 921 | POST_SEND_STATUS_UPDATE_FAILED fallback write: retry only after first failure |
| 223 | 922 | POST_SEND_STATUS_UPDATE_FAILED fallback write: exact 3 second retry wait |
| 223 | 923 | POST_SEND_STATUS_UPDATE_FAILED fallback write attempt 2: clear err |
| 223 | 924 | POST_SEND_STATUS_UPDATE_FAILED fallback write attempt 2: clear errmsg |
| 223 | 925 | POST_SEND_STATUS_UPDATE_FAILED fallback write: Update Cells attempt 2 |
| 223 | 926 | POST_SEND_STATUS_UPDATE_FAILED fallback write: assume attempt 2 success |
| 223 | 927 | POST_SEND_STATUS_UPDATE_FAILED fallback write: attempt 2 numeric error check |
| 223 | 928 | POST_SEND_STATUS_UPDATE_FAILED fallback write: attempt 2 failed |
| 223 | 929 | POST_SEND_STATUS_UPDATE_FAILED fallback write: end attempt 2 error check |
| 223 | 930 | POST_SEND_STATUS_UPDATE_FAILED fallback write: end retry |
| 223 | 932 | post-Send fallback never claims confirmed send |
| 223 | 933 | post-Send fallback remains failed for review |
| 223 | 934 | post-Send fallback preserves original Send error in SSLastError |
| 223 | 935 | post-Send fallback preserves original Send error for lock-release restore |
| 223 | 936 | post-Send fallback terminal |
| 223 | 937 | end shared post-Send fallback |

The single `button_send` remains at Task 223 output action 688. No AutoInput node changed. There is no edge back to the Send action.

## Lock Proof

- Lock-release helper calls in Task 223: 1.
- Stop actions between owned-lock acquisition and release: 0.
- All post-lock AutoSheets actions have `se=false`.
- The intended final controller error is saved before `SS Lock Release HARD` and restored afterward.
- Unowned-lock release paths: 0.

## Independent Validation

- Original independent suite rerun: 43/43 PASS.
- New independent suite: 67/67 PASS.

## 18-Case Matrix

| Case | Scenario | Result |
| ---: | --- | --- |
| 1 | Launcher not armed | PASS |
| 2 | Invalid worker parameters | PASS |
| 3 | Lock already active | PASS |
| 4 | Initial row read fails twice | PASS |
| 5 | Row ID mismatch | PASS |
| 6 | Row not READY_TO_SEND | PASS |
| 7 | Bad sender/message/reply | PASS |
| 8 | SENDING write fails | PASS |
| 9 | SENDING readback fails | PASS |
| 10 | Search ultimately fails | PASS |
| 11 | Contact selection fails | PASS |
| 12 | Compose path fails | PASS |
| 13 | Send action reports error | PASS |
| 14 | Send click status confirms | PASS |
| 15 | Post-Send status fails | PASS |
| 16 | Selector sees pending state | PASS |
| 17 | Selector sees one READY row | PASS |
| 18 | Queue Cycle integration | PASS |

Static validation does not prove phone import, Tasker rendering, TextNow UI state, or a real Send.
