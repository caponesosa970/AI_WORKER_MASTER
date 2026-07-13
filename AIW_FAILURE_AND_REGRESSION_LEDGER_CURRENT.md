# AI Worker Failure And Regression Ledger Current

Status: ACTIVE ISSUE LEDGER
Updated: 2026-07-12T18:53:46-07:00

Every failure remains active until it has a required repair, a required regression test, and closing proof reviewed by ChatGPT. Static audit cannot close a phone/runtime issue by itself.

## Required Issue Fields

Each issue must include:

- issue ID
- first detected date
- affected build
- affected task/action
- observed symptom
- direct evidence
- root cause
- contributing cause
- Codex responsibility
- ChatGPT/controller responsibility
- user/operator responsibility, if any
- prior warning that was missed
- required repair
- required regression test
- status: OPEN / HOLD / VERIFIED CLOSED
- closing proof
- prevention rule
- builds that must check this issue in preflight

## Prior Failures That Should Have Prevented ISSUE_27B

| Prior warning | Evidence source | Prevention that should have applied |
|---|---|---|
| 26A/26B false-pass class: errored AutoInput actions can still lead to success flags if not checked correctly | `02_TEST_LOGS/27B_20260710/AIW_CODEX_ACCOUNTABILITY_REPORT.md` | Do not accept UI success or PRESERVED claims without direct action-level proof and failure routing review |
| Static/package proof is not phone proof | `AGENTS.md`, `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`, V15A audit reports | Do not approve phone test from Codex summary alone when phone-visible plugin fields are not independently checked |
| Generated reports can be incomplete evidence | 27B generated `V15A_AUTOINPUT_DIFF_TABLE.csv` | A generated CSV cannot prove its own correctness; use independent parser/check and direct source/output field evidence |
| Phone proof supersedes static audit | project authority rules and user/controller instruction | When phone proof contradicts static claims, reopen the issue and update ledgers before further repair |
| Wrong-recipient and send-adjacent paths are critical | `docs/FAILURE_AND_REGRESSION_LEDGER.md` F009-F011 | Every TextNow/AutoInput action must be treated as high risk until field-level and phone-visible proof exists |

## Active Issues

### ISSUE_27B_AUTOINPUT_TARGET_NOT_V15A_PRESERVED

First detected date:

2026-07-12 from Sosa/ChatGPT phone proof report.

Affected build:

27B V15A-preserved controlled send candidate.

Affected task/action:

`AIW27B_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE`, SEARCH_ICON AutoInput action.

Observed symptom:

Phone proof showed SEARCH_ICON used an AutoInput setup that Sosa did not create, including a `menu_search` ID target and Structure Output enabled. The controlled run failed at SEARCH_ICON and safely stopped without sending.

Direct evidence:

- User/controller instruction in this task.
- 27B report claim: `02_TEST_LOGS/27B_20260710/V15A_AUTOINPUT_PRESERVATION_REPORT.md`
- 27B generated static table: `02_TEST_LOGS/27B_20260710/V15A_AUTOINPUT_DIFF_TABLE.csv`
- V15A audit source action: `02_TEST_LOGS/V15A_WORKING_SYSTEM_RECOVERY_AUDIT_20260709/V15A_WORKING_TEXTNOW_ACTION_CONTRACT_AUDIT_20260709.md`
- Phone proof statement: SEARCH_ICON failed and no message was sent.

Root cause:

Codex treated a static generated comparison as enough to claim AutoInput preservation. The comparison did not prove phone-visible AutoInput configuration or Sosa-created action fields.

Contributing cause:

ChatGPT/controller accepted the phone test from Codex summary/static report without independently validating the actual phone-visible AutoInput fields before approval.

Codex responsibility:

Unsupported `PRESERVED` claim. Missing direct field-by-field source/output evidence and missing independent parser/check.

ChatGPT/controller responsibility:

Phone import/test approval was allowed from insufficient evidence. Controller must identify what it personally verified before approving future phone tests.

User/operator responsibility:

No fault recorded. Sosa supplied the phone proof that exposed the issue and reset row 75 to a safe state.

Prior warning that was missed:

26A/26B false-pass issue showed AutoInput/static reports could pass while phone behavior failed. The V15A preservation rule said to preserve the full contract, not just target text.

Required repair:

No repair is authorized in this PR. A future repair must either:

- use a phone-exported Sosa-created AutoInput action as the source, or
- show exact source and output field values for every AutoInput field and pass a second independent comparison, then receive ChatGPT approval before phone import.

Required regression test:

- SEARCH_ICON AutoInput source/output field-by-field comparison.
- Independent parser/check of AutoInput plugin bundle values.
- Phone-visible field screenshot/export or Sosa-created Tasker export proof.
- Runlog proof that failure cannot set success flags.
- Proof that no send, DONE, Archive, live, capacity, or release path is touched.

Status:

OPEN.

Closing proof:

None.

Prevention rule:

No `PRESERVED`, `UNCHANGED`, `PHONE-PROVEN`, or `PASS` claim may be recorded without direct evidence mapped in `AIW_CLAIM_TO_PROOF_MATRIX_CURRENT.md`.

Builds that must check this issue in preflight:

- 27B repair
- 29A or later SEARCH_ICON source-truth repair
- any Gate 9B1 TextNow UI work
- any result select or thread identity work
- any compose, paste, Send, DONE, Archive, live, capacity, or release work
- any AutoInput preservation or migration work

29A forensic status:

HOLD. No authoritative SEARCH_ICON source was found. No runtime repair was performed.

29A missing proof:

- phone-exported or Sosa-created SEARCH_ICON action source
- successful historical phone behavior tied to that exact source
- no contradiction from newer phone proof
- fully inspectable field-by-field AutoInput bundle values

29A prevention rule:

Do not patch from partial historical evidence. Older text-based `Search` action evidence is a candidate only until direct source and successful behavior proof are supplied.

30A correction:

Sosa directly confirmed that all V15A send-path AutoInput actions were manually created by him. The authoritative source exists and is `basefile_v15a_phone_send_cleanup_pass.xml`.

30A comparison result:

- V15A SEARCH_ICON and current private 27B SEARCH_ICON are semantically identical.
- The only byte-level difference is action `sr`, required because the action lives at a different position in the 27B task.
- No SEARCH_ICON field drift was found.
- No runtime repair was created.

Corrected issue classification:

The original "not V15A preserved" claim is not supported after 30A comparison. The remaining failure is now classified as phone/runtime/UI behavior with V15A SEARCH_ICON preserved.

Codex responsibility:

- Prior 29A conclusion that no authoritative source existed is superseded and must not be used as active truth.
- No proven copy drift exists in SEARCH_ICON.

ChatGPT/controller responsibility:

- Failed to apply repeated user source-truth instructions before accepting the 29A source-not-found conclusion.

User/operator responsibility:

NONE.

Required next diagnostic:

30B phone/runtime/UI diagnostic. Do not patch XML. Verify the phone-visible SEARCH_ICON action state, TextNow UI state, and runlog behavior around SEARCH_ICON.

## Existing Regression Categories Still Active

| Issue | Status | Required preflight check |
|---|---|---|
| F003 Encoding corruption | OPEN | Verify no mojibake or XML format drift for any runtime XML work |
| F009 Wrong-recipient send | OPEN | Verify recipient/thread proof and no guessed AutoInput target |
| F010 Stale reply send | OPEN | Verify row ID, sender, reply, and status contract |
| F011 DONE before send | OPEN | Verify no DONE write without independent sent proof |
| F012 Lock not released | OPEN | Verify lock release on success, hold, and error exits |
| 23A/23B/23C malformed phone task class | OPEN/HISTORICAL | Do not treat XML parse as Tasker phone-render proof |
| 26A/26B AutoInput false-pass class | OPEN/HISTORICAL | Required AutoInput errors must not set success variables or ExitOK proof states |

## 30B Diagnostic Follow-Up

Issue:

`ISSUE_27B_SEARCH_ICON_RUNTIME_UI_FAILURE_WITH_V15A_PRESERVED`

Status:

OPEN / DIAGNOSTIC PACKAGE CANDIDATE.

30B action:

Created one no-send diagnostic task candidate to compare V15A ID `menu_search` plus `search_field` against Dashgood active Task 71 Text `Search` plus `search_field` reset/retry path.

Repair status:

No repair to 27B or FINAL Send Sheet was performed.

Required regression proof:

- phone import/render of diagnostic task after ChatGPT audit
- runlog showing which path succeeds/fails
- no phone number typed
- no result/contact selection
- no compose focus
- no Send/DONE/Archive/live/capacity path touched

Closing proof:

None. Issue remains OPEN until phone/runtime diagnostic proof is supplied and ChatGPT decides the next repair path.

## 30B Rejection / 30B1 Repair Status

30B private-package audit result: REJECTED.

Blocking defects:

1. Original 30B If/End If count was unbalanced: 6 If actions and 5 End If actions, final stack depth 1.
2. Original 30B claimed a Dashgood failure result even though Dashgood exact AutoInput nodes use Continue Task After Error OFF.

30B1 repair status:

- If/End If balanced: 2 If actions and 2 End If actions.
- Final control stack depth: 0.
- Dashgood retry block removed.
- Unsupported `DASHGOOD_TEXT_SEARCH_FAILED` claim removed.
- Exact-off AutoInput steps now use pre-action NOT_COMPLETED markers and immediate PASS markers.

Issue remains OPEN until ChatGPT re-audits and phone/runtime proof is supplied.
