# AI Worker Failed Packages Ledger

Updated: 2026-07-06

Failed packages must not be used as phone-test candidates. They may be inspected only as evidence.

Before every future build, Codex must read this ledger and state which failed packages are relevant to the current scope.

| failed_id | file/package | classification | evidence | reason | allowed use |
|---|---|---|---|---|---|
| FAIL-STAGE4B-001 | `AIW_STAGE4B_SEND_DRYRUN_RUNLOG_AUDIT_20260705_084108.md` / `runlog_stage4b_retry_contact_pick_20260705_154009Z.txt` | FAILED | SHA256 `ACC2787FA48315FD1CE0061D930391C44561E4EEEE12813311FCA51F3F51EC6F` for audit | Stage4B contact-selection dry-run failed: no dry-run pass marker, `SEND=NO` absent, unhandled error count 1. | Use as failure evidence only. |
| FAIL-STAGE4B-DATA-001 | `runlog.txt` formatted-number dry-run | FAILED / DATA FORMAT CONTACT_PICK FAILURE | SHA256 `EB4937BC8EF57CF21EF0E96D9B8676B2A33D171A980EC3F9D799526608E8197E`; summarized in `AIW_STAGE4B_DRYRUN_PROGRESS_SPEED_LOG_20260705.md` | TextNow search used formatted phone text; search field accepted it but TextNow did not resolve the thread. `SS Fail UI Dirty Stop` ran, `SSSentOne=0`, lock released. | Use as proof that formatted phone search key needs normalization. Do not classify as XML/import failure. |
| FAIL-SEARCHICON-001 | `AIW_BUILD100_GROUP_B_SEARCH_ICON_PATCH_FOR_CHATGPT_20260705.zip` and packaged XML | FAILED | `AIW_BUILD100_GROUP_B_SEARCH_ICON_PATCH_PACKAGE_AUDIT_20260705.md` | ChatGPT audit reported broken Tasker block nesting, 30 block issues. | Use only to understand patch intent. Do not import. |
| FAIL-REBASED-IMPORT-001 | `AIW_BUILD100_GROUP_B_SEARCH_ICON_REBASED_FULL_TASKER_20260705.xml` | FAILED / SUPERSEDED | User reported Tasker parse/import failure; superseded by import-safe XML | Normal XML rewrite changed Tasker file shape too much. | Do not import. Use import-safe/10C XML only. |
| FAIL-PRIVATE200-001 | `take_api_WITH_KEY_PRIVATE_20260705.xml` and 200-task private/reference XML family | FAILED AS PHONE-TEST CANDIDATE | `AIW_TAKE_API_WITH_KEY_STATIC_AUDIT_20260705.md` | Older/smaller private reference; not the controlled Build100 replacement; block issues existed in audit context. | Private reference only. Do not ship as Build100 phone XML. |
| FAIL-STAGE4A-001 | Stage4A no-work run where `FINAL Send Sheet` ran | FAILED | `AIW_STAGE4A_PROCESS_ONLY_RUNLOG_AUDIT_20260705_020447.md` | Stage4A failed because no-work/process-only proof entered `FINAL Send Sheet`, even though no real send was proven. | Use as failure evidence only. |
| FAIL-TASKER-IMPORT-001 | Prior statically parseable/auditable XML packages rejected by Tasker | FAILED / TASKER IMPORT REJECTED | User-reported Tasker import rejection and later 10C Tasker-safe package | Static XML parse was treated as enough; Tasker importability was not enforced as a first-class gate. | Do not continue from rejected XML. Rebuild from last Tasker-accepted XML only. |
| FAIL-REDACTED-IMPORT-001 | Redacted ChatGPT audit XML lane | FAILED AS PHONE IMPORT SOURCE | ChatGPT audit feedback requiring full with-key import XML separate from redacted XML | Redacted XML was treated as if it might be importable. | Audit reference only. Never import redacted XML. |
| HARDHOLD-GROUPC-001 | `13_CHATGPT_AUDIT_ZIP__AIW_BUILD100_GROUP_C_RUNTIME_PATCH_20260706.zip` | HARD HOLD / NO PATCH CREATED | SHA256 `D7D21E9F25A55BA6685D58495EFE39D86B71324FC9C6D17CB227B8CCC0C7A83A`; `GROUP_C_HARD_HOLD_SAFETY_INSPECTION_20260706.md` | `SS Controlled One-Row Send Proof` lacks approved-recipient guard and thread/header confirmation before send-button action; pass/DONE markers follow without independent sent-message proof. | Use as safety evidence for ChatGPT. Do not phone test. |

## Reuse Rule

Do not build from a failed package unless the task explicitly says to use it as reference only.

The current safe baseline is:

`PRIVATE_WITH_KEY/runtime_xml/10C_TASKER_IMPORT_XML__AIW_BUILD100_GROUP_B2_SEND_UI_DRYRUN_WITH_KEY_TASKER_SAFE_20260706.xml`

SHA256:

`5E6ACEC6AAADE464A3F19E9750A80E3B33CD3CDB97E5085B965429461ECF527F`

## Prevention Rule Link

For repeatable failure prevention, read:

- `ISSUE_HISTORY_REGISTER.md`
- `BUILD_MISTAKE_PREVENTION_RULES.md`

Known recurring failures now blocked:

- Tasker import rejection,
- redacted XML treated as phone-import XML,
- formatted number search failure,
- dirty UI after dry-run paste,
- Group C controlled-send without wrong-recipient/thread proof.

Older packages may be read as evidence/source history only. They do not override runtime XML, audits, runlogs, screenshots, SHA256 records, ledgers, or ChatGPT audit results.
