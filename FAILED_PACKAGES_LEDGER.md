# AI Worker Failed Packages Ledger

Updated: 2026-07-05

Failed packages must not be used as phone-test candidates. They may be inspected only as evidence.

| failed_id | file/package | classification | evidence | reason | allowed use |
|---|---|---|---|---|---|
| FAIL-STAGE4B-001 | `AIW_STAGE4B_SEND_DRYRUN_RUNLOG_AUDIT_20260705_084108.md` / `runlog_stage4b_retry_contact_pick_20260705_154009Z.txt` | FAILED | SHA256 `ACC2787FA48315FD1CE0061D930391C44561E4EEEE12813311FCA51F3F51EC6F` for audit | Stage4B contact-selection dry-run failed: no dry-run pass marker, `SEND=NO` absent, unhandled error count 1. | Use as failure evidence only. |
| FAIL-STAGE4B-DATA-001 | `runlog.txt` formatted-number dry-run | FAILED / DATA FORMAT CONTACT_PICK FAILURE | SHA256 `EB4937BC8EF57CF21EF0E96D9B8676B2A33D171A980EC3F9D799526608E8197E`; summarized in `AIW_STAGE4B_DRYRUN_PROGRESS_SPEED_LOG_20260705.md` | TextNow search used `+1(910) 447-7850`; search field accepted it but TextNow did not resolve the thread. `SS Fail UI Dirty Stop` ran, `SSSentOne=0`, lock released. | Use as proof that formatted phone search key needs normalization. Do not classify as XML/import failure. |
| FAIL-SEARCHICON-001 | `AIW_BUILD100_GROUP_B_SEARCH_ICON_PATCH_FOR_CHATGPT_20260705.zip` and packaged XML | FAILED | `AIW_BUILD100_GROUP_B_SEARCH_ICON_PATCH_PACKAGE_AUDIT_20260705.md` | ChatGPT audit reported broken Tasker block nesting, 30 block issues. | Use only to understand patch intent. Do not import. |
| FAIL-REBASED-IMPORT-001 | `AIW_BUILD100_GROUP_B_SEARCH_ICON_REBASED_FULL_TASKER_20260705.xml` | FAILED / SUPERSEDED | User reported Tasker parse/import failure; superseded by `IMPORT_SAFE` XML | Normal XML rewrite changed Tasker file shape too much. | Do not import. Use `IMPORT_SAFE` XML only. |
| FAIL-PRIVATE200-001 | `take_api_WITH_KEY_PRIVATE_20260705.xml` and 200-task private/reference XML family | FAILED AS PHONE-TEST CANDIDATE | `AIW_TAKE_API_WITH_KEY_STATIC_AUDIT_20260705.md` | Older/smaller private reference; not the controlled Build100 replacement; block issues existed in audit context. | Private reference only. Do not ship as Build100 phone XML. |
| FAIL-STAGE4A-001 | Stage4A no-work run where `FINAL Send Sheet` ran | FAILED | `AIW_STAGE4A_PROCESS_ONLY_RUNLOG_AUDIT_20260705_020447.md` | Stage4A failed because no-work/process-only proof entered `FINAL Send Sheet`, even though no real send was proven. | Use as failure evidence only. |

## Reuse Rule

Do not build from a failed package unless the task explicitly says to use it as reference only. The current usable candidate is:

`01_CANDIDATE_PATCHES/BUILD100_GROUP_B_SEARCH_ICON_IMPORT_SAFE/xml/AIW_BUILD100_GROUP_B_SEARCH_ICON_IMPORT_SAFE_FULL_TASKER_20260705.xml`

The current active plan is:

`MASTER_PLAN_CURRENT.md`

Older packages may be read as evidence only. They do not override the subsystem completion plan.
