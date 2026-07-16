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

## 30B1 Phone Result

Status:

DEVELOPMENT PASS.

Direct phone findings:

- Full-project Tasker import/render passed.
- `AIW30B_SEARCH_ICON_RUNTIME_COMPARE_NO_SEND` ran.
- V15A Id `menu_search` timed out.
- Active Dashgood Task 71 combined Search lane reached the TextNow Search screen.
- Both exact Dashgood `search_field` actions completed OK.
- Final visible state was the Search field focused with keyboard open.
- No number was typed.
- No contact was selected.
- No compose, Send, DONE, Archive, live, or Sheet action ran.

Interpretation:

- Do not treat the Dashgood Text Search AutoInput error alone as fatal.
- Do not trust intermediate wrapper PASS markers as final proof.
- Use successful `search_field` reach as the positive end-state validation.
- Preserve the active Dashgood Search recovery logic exactly.

Tracker effect:

No percentage change. Current tracker remains `8/14 locked = 57%`.


## 31A Repair Candidate Status

31A uses the 30B1 phone result to create a production candidate that preserves the active Dashgood Search recovery lane exactly inside a cloned task.

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT.

Open issue coverage:

- `ISSUE_27B_SEARCH_ICON_RUNTIME_UI_FAILURE_WITH_V15A_PRESERVED` remains OPEN until 31A passes ChatGPT audit and future phone proof.
- Controlled Send remains HOLD.
- Phone proof is not claimed for 31A.


## ISSUE_31A_DISCONTINUED_CREDENTIAL_IN_PRIVATE_PACKAGE

Status: REPAIRED CANDIDATE / HOLD FOR CHATGPT AUDIT

First detected date: 2026-07-13

Affected build:

31A Dashgood search-lane controlled-send candidate.

Observed symptom:

ChatGPT private-package audit found that 31A carried a discontinued credential from an older 27B base even though the report claimed the current key was unchanged.

Direct evidence:

- Original 31A XML SHA256: `D0F5F43DCE0BCD42ED75964ADDFFF078FCBEBC01637553153A280F478583CCD3`
- Credential source XML SHA256: `03CDD603FE4D3991BC3E88472BEA6C684F4CE10D0597A429EF5E247859D66925`
- 31A1 final XML SHA256: `1C1FAF33EA30B69E8F35478AA8E93E58A2AA4ABB967CAA8F5EA927506BBF1B6E`
- Sanitized XML comparison after credential redaction: IDENTICAL

Root cause:

31A used an older private 27B base for credential material.

Contributing cause:

The report claim "Current key unchanged" was accepted from package construction instead of comparing the actual credential against the current credential source.

Codex responsibility:

Codex made an unsupported current-key claim in the original 31A package.

ChatGPT/controller responsibility:

ChatGPT caught the private-key mismatch before phone import and held the package.

User/operator responsibility:

NONE.

Required repair:

Replace only the discontinued private credential literal with the current credential from the verified source. Do not change runtime actions.

Required regression test:

- Sanitized XML byte comparison after redacting all `sk-...` credentials must be IDENTICAL.
- Task 224 must remain byte-identical.
- Discontinued credential remaining count must be `0`.
- Current credential occurrence count must be `1`.
- ZIP integrity must pass.

Closing proof:

Pending ChatGPT audit of 31A1.

Prevention rule:

Credential-current claims require direct source/output credential equality checks without printing the credential. A key-count check alone is not enough.

Builds that must check this issue in preflight:

- 31A1
- any future private runtime package carrying the OpenAI key

## ISSUE_31A_AUTOSHEETS_ROW_READ_TIMEOUT_LOCK_RELEASE_RISK

Status: REPAIRED CANDIDATE / HOLD FOR CHATGPT AUDIT

First detected date: 2026-07-13

Affected build:

31A1 current-key controlled-send candidate, task `224`.

Affected task/action:

Task `224`, AutoSheets row-read preflight for the staged row range.

Observed symptom:

Phone proof reported `java.net.SocketTimeoutException: timeout` at the AutoSheets Get Data action after `%AIWSending` was set to `1` and before TextNow launched.

Direct evidence:

- Sosa/ChatGPT phone-result instruction for 31B.
- Source 31A1 XML SHA256: `1C1FAF33EA30B69E8F35478AA8E93E58A2AA4ABB967CAA8F5EA927506BBF1B6E`
- 31B final XML SHA256: `0B984F8CADCBCCA4915676F76C269F927ADED0473C34043F15609F1720C60007`

Root cause:

The preflight AutoSheets read could fail before TextNow launch while the Send lock was already active, without a one-time retry and explicit final failure path to close AllowSend and release the lock.

Contributing cause:

The earlier candidate focused on Search-lane repair and credential correction. It did not yet harden the AutoSheets preflight read timeout behavior.

Codex responsibility:

31B must prove that AutoSheets timeout handling was added without changing Search, AutoInput, compose, Send, DONE, Archive, profiles, scenes, or credential material.

ChatGPT/controller responsibility:

ChatGPT must audit the private 31B XML before any phone import and must verify the failure path directly, not from summary alone.

User/operator responsibility:

NONE. The operator supplied the phone failure and reset the Sheet state outside this repository task.

Required repair:

Add a one-retry AutoSheets preflight wrapper in task `224` only. Clear output arrays before both attempts, validate all first elements and array counts, and on final failure set `%AIW27BAllowSend=0`, record `AUTOSHEETS_ROW_READ_FAILED`, perform `SS Lock Release HARD`, and stop before TextNow launch.

Required regression test:

- maximum AutoSheets row-read attempts equals `2`
- output arrays cleared before both attempts
- all first elements checked
- all array counts checked for exactly `1`
- final failure path releases lock
- final failure path closes AllowSend
- no TextNow action is reachable after both reads fail
- Search lane and downstream actions remain semantically unchanged

Closing proof:

Pending ChatGPT audit of 31B and any later approved phone proof.

Prevention rule:

Any Send-lock path that performs network or Sheet preflight before TextNow launch must have a bounded retry and an explicit lock-release failure path before UI launch.

Builds that must check this issue in preflight:

- 31B
- any future controlled-send candidate
- any Gate 10 one-send package
- any future Send-lock or Sheet preflight repair

## ISSUE_31B_CONTROLLED_SEND_TRANSACTION_SAFETY_REQUIREMENTS

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT

First detected date: 2026-07-13

Affected build:

31B controlled-send candidate.

Affected task/action:

Task `224`, controlled one-send transaction path.

Observed symptom:

The prior 31B AutoSheets-only repair did not include all current transaction-safety requirements needed to clear the controlled one-send gate.

Direct evidence:

- Sosa/ChatGPT superseding 31B gate correction.
- Final superseding 31B XML SHA256: `156D44624EF534DB8F0D4E81F0E873A44FE8A9560B26D1C260348AFA4ED8B820`
- Final superseding 31B ZIP SHA256: `B6C8126034AE775157105A0343F627464AF1F1626B44584CA9140DA3B0D3B67D`

Root cause:

Controlled one-send needs transaction semantics beyond UI and timeout handling: Send authorization must be consumed, the Sheet row must be moved to `SENDING` before UI, and Send click must not immediately mark `DONE`.

Contributing cause:

The earlier repair was scoped only to AutoSheets timeout survival and lock release.

Codex responsibility:

Implement the complete transaction-safety gate in task `224` without altering AutoInput action nodes, credentials, profiles, scenes, or other tasks.

ChatGPT/controller responsibility:

Audit the private XML directly and do not approve phone import from summary alone.

User/operator responsibility:

NONE.

Required repair:

Superseding 31B must include:

- bounded preflight read retry
- output clearing before each read attempt
- first-element and array-count read validation
- local authorization latch
- global authorization closed before TextNow and every Stop
- `SENDING` write/retry/readback before TextNow
- no `DONE` write from Send click
- post-Send `SEND_CLICKED_AWAITING_CONFIRM` write/retry
- lock release on all exits

Required regression test:

- verify exact read attempts maximum is `2`
- verify exact SENDING update attempts maximum is `2`
- verify exact post-Send status update attempts maximum is `2`
- verify TextNow launch is blocked until SENDING readback passes
- verify task 224 contains no `DONE` write
- verify task 224 contains no `%SSSentOne=1`
- verify task 224 contains no `%SSResult=SENT`
- verify AutoInput nodes are unchanged

Closing proof:

Pending ChatGPT audit and any later approved phone proof.

Prevention rule:

Controlled Send cannot be cleared by a Send-button click alone. It must preserve transaction state: READY_TO_SEND to SENDING before UI, SEND_CLICKED_AWAITING_CONFIRM after click, and controller-verified DONE only after phone evidence.

Builds that must check this issue in preflight:

- 31B
- any future Gate 10 one-send package
- any future controlled-send package
- any release package

<!-- PLAN_A_ACCOUNTABILITY_START -->
## ISSUE_PLAN_A_PHONE_PROOF_PENDING

- First detected: 2026-07-13.
- Affected build: Plan A permanent Send module candidate.
- Affected tasks: 71, 199, 223, 224.
- Observed symptom: none on phone; artifact has not been imported or run.
- Direct evidence: static XML/package validation only.
- Root cause: phone behavior is intentionally not inferred from static output.
- Codex responsibility: keep issue OPEN and avoid phone-proof claims.
- ChatGPT/controller responsibility: independently audit actual artifacts before authorizing any phone import.
- User/operator responsibility: NONE.
- Prior warning: static audit previously passed candidates that later failed on phone.
- Required repair: none statically identified; repair only if full artifact audit finds a concrete defect.
- Required regression test: controlled phone import/render and one approved Gate 9 test after controller approval.
- Status: OPEN / HOLD.
- Closing proof: not available.
- Prevention rule: phone proof supersedes every generated report.
- Builds that must check this issue: Plan A and every later confirmation/Archive integration.

## ISSUE_PLAN_A_TASK199_ARCHIVE_ASSERTION_CONFLICT

- First detected: 2026-07-13.
- Affected build: Plan A permanent Send module candidate.
- Affected task: 199, unchanged non-Send maintenance branch.
- Direct evidence: approved base contains historical Archive/maintenance calls outside the Send block.
- Root cause: controlling instructions simultaneously require preserving every non-Send Task 199 action and report zero Archive actions across Task 199.
- Codex responsibility: do not silently remove old maintenance logic and disclose the contradiction.
- User/operator responsibility: NONE.
- Required repair: controller decision only if literal zero-Archive scope is required; otherwise accept no-new-Archive interpretation.
- Status: OPEN / HOLD FOR CHATGPT ARTIFACT AUDIT.
- Prevention rule: conflicting acceptance statements are surfaced, not guessed away.
<!-- PLAN_A_ACCOUNTABILITY_END -->

<!-- PLAN_A1_CORRECTION_FAILURES_START -->
## Plan A Final Artifact Correction Issues

### ISSUE_PLAN_A_AUTOSHEETS_CONTINUE_AFTER_ERROR_MISSING

- First detected: 2026-07-13
- Affected artifact: rejected Plan A XML SHA `00C66283AD073BBCB3E8DEBA6EDE3258BB53258D56D007BB48EF4E404307AA59`
- Affected tasks/actions: all 2 Task 71 and all 24 Task 223 AutoSheets actions
- Symptom: exported actions lacked `<se>false</se>`, so plugin timeout could terminate before retry and lock cleanup
- Root cause: validator treated plugin arg4 as continuation proof and did not inspect the exported `se` field
- Codex responsibility: YES
- ChatGPT/controller responsibility: detected during direct artifact audit
- User/operator responsibility: NONE
- Repair: all 26 AutoSheets actions now contain `<se>false</se>` with payloads unchanged
- Regression: pairwise two-attempt simulation plus lock-release reachability
- Status: REPAIRED CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT
- Closing proof required: ChatGPT artifact audit, followed later by approved phone proof

### ISSUE_PLAN_A_SEND_ERROR_NOT_PRESERVED

- First detected: 2026-07-13
- Affected task/action: Task 223 immediately after `button_send`
- Symptom: `%err` and `%errmsg` were cleared before being preserved; unknown outcome could be reported without confirmed persistent state
- Root cause: Send action error and later AutoSheets errors shared the same transient variables
- Codex responsibility: YES
- ChatGPT/controller responsibility: detected during direct artifact audit
- User/operator responsibility: NONE
- Repair: saved lowercase local variables, confirmed-only unknown result, fallback to POST_SEND_STATUS_UPDATE_FAILED
- Regression: branch ancestry, immediate adjacency, error-source, and no-resend checks
- Status: REPAIRED CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT
- Closing proof required: ChatGPT artifact audit, followed later by approved phone proof

### PLAN_A_ARCHIVE_ASSERTION_WORDING_CONFLICT

- Type: controller specification correction, not runtime defect
- Correction: zero Archive actions applies to Tasks 71/223/224; Task 199 may retain only its byte-identical historical gated maintenance calls
- Task 199 changed by correction: NO
- New Archive connection: NO
- User/operator responsibility: NONE
- Status: VERIFIED CLOSED BY BYTE-IDENTITY AND CONTROLLER RULING
<!-- PLAN_A1_CORRECTION_FAILURES_END -->

## ISSUE_GATE10_CONFIRMATION_SOURCE_NOT_PROVEN

- First detected: 2026-07-13.
- Affected build: Gate 10 confirmation-only request.
- Affected task/action: proposed `FINAL Confirm One Bound Row`; no runtime task was created.
- Observed symptom: no phone-exported or phone-proven Tasker action was found that independently recognizes the exact outgoing reply in TextNow.
- Direct evidence: repository/private XML search, Git history search, Drive source search, R1 UI Query control, historical Gate 10 and Group C2 reports.
- Root cause: the project proved Send visually and manually, but never established an automatable outgoing-message detection contract.
- Contributing cause: UI Query timed out previously and remains blocked; screenshots and recordings do not expose a reusable Tasker plugin bundle.
- Codex responsibility: stop before runtime generation and disclose the missing proof.
- ChatGPT/controller responsibility: supply or approve a separately phone-proven confirmation method before any Gate 10 runtime build.
- User/operator responsibility: NONE.
- Prior warning missed: historical reports repeatedly state that automated sent-message proof is not reliable or approved.
- Required repair: none may be guessed.
- Required regression test: after an exact phone-exported confirmation action exists, prove it can match the bound outgoing reply with zero Send/compose/keyboard actions and preserve awaiting-confirm state on uncertainty.
- Status: OPEN / HOLD.
- Closing proof: a fully inspectable Sosa-created or phone-exported confirmation action plus successful phone runlog and visual proof.
- Prevention rule: DONE logic cannot be built from manual sent-bubble evidence alone.
- Builds that must check this issue: Gate 10 confirmation, DONE, Archive, live/timer, capacity, and release.


## ISSUE_GATE10_CONFIRMATION_SOURCE_NOT_PROVEN - CLOSURE UPDATE

- Closing evidence: Sosa supplied a phone-exported one-task source whose native Get Screen Info action completed on the phone and returned TextNow package and ordered visible text.
- Source role: DEVELOPMENT PASS for the non-mutating screen-read action only.
- Codex verification: source SHA, exact action, Continue Task After Error, outputs, and forbidden-action absence.
- Status: VERIFIED CLOSED FOR SOURCE AVAILABILITY.
- User/operator responsibility: NONE.
- Prevention retained: production confirmation still requires artifact audit and separate phone proof.

## ISSUE_GATE10_PRODUCTION_CONFIRMATION_PHONE_PROOF_PENDING

- First detected: 2026-07-14.
- Affected build: Gate 10 production confirmation-only candidate.
- Affected tasks: Task 224 launcher and new Task 225 confirmation worker.
- Observed symptom: static candidate exists but has not been imported or run on the phone.
- Direct evidence: private XML/ZIP and public Gate 10 audit reports.
- Root cause: phone proof is a separate gate after source and static proof.
- Codex responsibility: keep candidate on HOLD and never claim phone proof.
- ChatGPT/controller responsibility: independently audit actual artifacts before any import instruction.
- User/operator responsibility: NONE.
- Required regression test: one confirmation-only run proving exact thread identity, exact unique reply + immediate Sent, exact row DONE readback, lock release, and zero Send behavior.
- Status: OPEN / HOLD FOR CHATGPT ARTIFACT AUDIT.
- Closing proof: direct Sosa phone recording/runlog plus controller verification.
- Builds that must check this issue: Gate 10, DONE, Archive, live/timer, capacity, and release.


<!-- GATE11_FAILURE_LEDGER_START -->
## ISSUE_GATE10_PRODUCTION_CONFIRMATION_PHONE_PROOF_PENDING - CLOSURE UPDATE

- Closing authority: direct Sosa phone proof accepted by the controller.
- Closing result: exact independent confirmation and DONE passed; no second Send was run.
- Status: VERIFIED CLOSED.
- Codex responsibility: record the controller decision without independently claiming phone proof.
- User/operator responsibility: NONE.

## ISSUE_GATE11_PRODUCTION_ARCHIVE_PHONE_PROOF_PENDING

- First detected date: 2026-07-13.
- Affected build: Gate 11 exact-row Archive candidate.
- Affected task/action: Task 224 launcher and Task 226 permanent exact-row Archive worker.
- Observed symptom: static candidate exists but has not been imported or run on the phone.
- Direct evidence: private candidate hashes, raw-node comparison, independent validators, and public audit reports.
- Root cause: phone import/render and live AutoSheets copy/clear behavior are separate proof gates.
- Contributing cause: existing Task 75 is broad and cannot prove exact-row idempotent Archive behavior.
- Codex responsibility: keep Gate 11 on HOLD; disclose source and runtime limitations; never claim phone proof.
- ChatGPT/controller responsibility: independently inspect the actual artifact before any import instruction and reconcile the future phone result.
- User/operator responsibility: NONE.
- Prior warning that was applied: confirmed completion must precede Archive; source clear must follow verified Archive copy.
- Required repair: none established; candidate requires artifact audit first.
- Required regression test: one exact bound DONE row archived once, exact Archive readback, exact source A:I clear/readback, lock release, no other row or blocked path touched.
- Status: OPEN / HOLD FOR CHATGPT ARTIFACT AUDIT.
- Closing proof: direct Sosa phone recording/runlog and controller review.
- Prevention rule: broad Archive routes cannot substitute for exact bound-row copy/readback/idempotency proof.
- Builds that must check this issue: Gate 11, broad Archive integration, DeadArchive, Compactor, live/timer, capacity, and release.
<!-- GATE11_FAILURE_LEDGER_END -->

<!-- GATE12_FAILURE_LEDGER_START -->
## ISSUE_GATE12_QUEUE_LIFECYCLE_PHONE_PROOF_PENDING

- First detected date: 2026-07-14.
- Affected build: Gate 12 queue lifecycle integration candidate.
- Affected task/action: Tasks 199, 224, and new Task 227.
- Observed symptom: no Gate 12 phone execution has occurred; static proof cannot establish Tasker import/render or the three-cycle lifecycle behavior.
- Direct evidence: candidate package, validators, reports, and absence of a Gate 12 runlog or phone recording.
- Root cause: normal proof boundary for a new runtime integration.
- Contributing cause: the three permanent modules were phone-proven separately, not through the integrated permanent queue.
- Codex responsibility: keep Gate 12 on HOLD, disclose unsupported phone claims, and preserve all proven module nodes.
- ChatGPT/controller responsibility: independently inspect the actual XML and ZIP before any import instruction, then control the three-cycle proof.
- User/operator responsibility: NONE.
- Prior warning that was applied: one queue invocation must not Send, confirm, and Archive consecutively.
- Required repair: none established by static audit; candidate requires artifact audit and controlled phone proof.
- Required regression test: READY_TO_SEND to awaiting-confirm; awaiting-confirm to DONE; DONE to verified Archive and source clear, with one transition per cycle.
- Status: OPEN / HOLD FOR CHATGPT FULL ARTIFACT AUDIT.
- Closing proof: direct Sosa phone recording/runlogs and controller reconciliation for all three cycles.
- Prevention rule: no tracker increase or lifecycle lock from static proof alone.
- Builds that must check this issue: Gate 12, Gate 13 recovery/timer, Gate 14 capacity/control/release.

## GATE11_PHONE_PROOF_RECONCILIATION

- Gate 11 exact-row Archive is recorded as VERIFIED CLOSED by direct Sosa phone proof.
- Codex does not independently claim that proof.
- Controller-provided result: exact copy verified, exact source row cleared, Archive lock released, `ARCHIVE_DONE_VERIFIED` returned.
<!-- GATE12_FAILURE_LEDGER_END -->

<!-- GATE12R1_FAILURE_LEDGER_START -->
## ISSUE_GATE12_CONTROLLED_MODE_NORMALIZATION_SUBSTITUTION

- First detected date: 2026-07-14.
- Affected build: original Gate 12 queue lifecycle integration candidate.
- Affected task/action: Task 199 action 5/XML act4 RHS and action 8/XML act7 RHS.
- Observed symptom: controlled arguments would be substituted into their own regex conditions, causing controlled mode to normalize to production and clearing the one-cycle token.
- Direct evidence: independent artifact audit of the actual XML and Tasker variable-replacement semantics.
- Root cause: dynamic `%par1` and `%par2` references were embedded in regex RHS text intended to detect unresolved literals.
- Contributing cause: the 57-case validator modeled branch state but not Tasker substitution inside action text.
- Codex responsibility: original static controlled-mode claim was unsupported by a substitution-aware test.
- ChatGPT/controller responsibility: independently inspected the artifact and caught the defect before phone import.
- User/operator responsibility: NONE.
- Prior warning missed: static XML structure cannot prove Tasker runtime text behavior.
- Required repair: replace only both RHS fields with literal `(?is)^\s*$|^%.*$`.
- Required regression test: model controlled, blank, unresolved, production, and invalid arguments after Tasker substitution; rerun all prior cases.
- Status: REPAIRED CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT.
- Closing proof: independent artifact audit followed by controlled phone proof.
- Prevention rule: scan every Tasker action-text variable reference for runtime substitution effects.
- Builds that must check this issue: Gate 12R1, Gate 13, Gate 14, and release.

## Original Gate 12 Candidate Disposition

- XML SHA256 `11D2C17F1107F024155C775E9320D68E447086DA5C6E38C900618A162FD65902` is REJECTED FOR PHONE IMPORT.
- Its reports remain preserved as failure evidence and are not overwritten.
<!-- GATE12R1_FAILURE_LEDGER_END -->

<!-- GATE13_FAILURE_LEDGER_START -->
## ISSUE_GATE13_BLANKET_LOCK_RESET_PATHS

- First detected: 2026-07-14
- Affected tasks/profiles: Start, Stop, Safe Recovery, boot profiles, watchdogs
- Symptom: existing control paths could clear transaction ownership without stale proof
- Direct evidence: Gate 12R1 call-graph audit
- Root cause: legacy reset helpers predated Send/confirmation/Archive ownership contracts
- Required repair: disconnect blanket resets; require STOP-first and stale timestamp plus queue evidence
- Required regression: no active-lock force clear, SENDING preserved, one recovery module maximum
- Status: REPAIRED CANDIDATE / HOLD FOR PHONE PROOF
- Closing proof: pending ChatGPT artifact audit and direct phone proof
- User/operator responsibility: NONE

## ISSUE_GATE13_ENVIRONMENT_STATE_NOT_FULLY_DETECTABLE

- First detected: 2026-07-14
- Symptom: no source-proven exact node detects fold state, AutoInput accessibility, TextNow availability, and Android battery/background restrictions
- Required control: screen and keyguard checks plus explicit environment-readiness latch
- Status: OPEN / HOLD FOR PHONE PROOF
- Prevention rule: do not claim unsupported background states; block before queue/UI work
<!-- GATE13_FAILURE_LEDGER_END -->

<!-- GATE13R1_FAILURE_LEDGER_START -->
## ISSUE_G13_KEYG_FALSE_HOLD_ANDROID16

- First detected date: 2026-07-14.
- Affected build: Gate 13 timer, STOP, background-guard, and recovery candidate.
- Affected tasks/actions: Task 130 act33, Task 224 act14, and Task 228 act48 in the Gate 13 base.
- Observed symptom: the controlled busy-timer test stopped at `GATE13_KEYGUARD_HOLD` while Tasker was visibly foreground and the phone was visibly unlocked.
- Direct evidence: controller-provided phone Run Log and visible phone state.
- Root cause: built-in `%KEYG` did not provide a reliable current-unlocked result on this Moto Razr 2024 / Android 16 runtime.
- Contributing cause: the Gate 13 static validator treated a documented built-in as source-proven runtime behavior without direct device proof.
- Codex responsibility: unsupported static assumption and missing device-specific proof before the keyguard claim.
- ChatGPT/controller responsibility: reconciled phone evidence, rejected a rerun, and constrained the replacement to one fail-closed probe.
- User/operator responsibility: NONE.
- Prior warning missed: phone proof supersedes static audit, including documented platform-state assumptions.
- Required repair: replace only the three `%KEYG` guard blocks with a shared `KeyguardManager` probe that requires both lock results to be explicitly false.
- Required regression: unlocked, locked, screen-off, Java error, blank, unresolved, busy-timer skip, caller HOLD preservation, no profile enablement, and no duplicate Send.
- Status: REPAIRED CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT.
- Closing proof: independent artifact audit followed by the repeated controlled busy-timer phone test.
- Prevention rule: platform-state signals require phone proof on the target Android runtime; errors and ambiguous values must HOLD.
- Builds that must check this issue: Gate 13R1, Gate 13 phone ladder, Gate 14, and release.

## Gate 13 Phone-Failure Safety Reconciliation

- Authorization was consumed before the false keyguard HOLD.
- No profile, tick, Queue Cycle, Send, confirmation, Archive, or Sheet action ran.
- No unsafe behavior occurred.
- Gate 13 remains HOLD and the tracker remains 12/14 locked = 86%.
<!-- GATE13R1_FAILURE_LEDGER_END -->

<!-- GATE13R2_FAILURE_LEDGER_START -->
## ISSUE_G13_CONFIRM_RECOVERY_CHAT_LIST_HOLD

- First detected date: 2026-07-14.
- Affected build: Gate 13R1 startup recovery path.
- Affected task/action: Task 225 standalone TextNow launch/wait prelude before Get Screen Info.
- Observed symptom: recovery routed correctly to Task 225, but Get Screen Info inspected the Chats list and could not prove exact sender, unique exact reply, and immediate `Sent`.
- Direct evidence: controller-provided Run Log, visible phone state, unchanged awaiting-confirm row, and disabled profiles.
- Root cause: Task 225 launched TextNow without source-proven navigation into the exact bound conversation.
- Contributing cause: the original confirmation candidate was proven from an already-open conversation; recovery from an arbitrary TextNow screen required a separate navigation lane.
- Codex responsibility: keep failure closed, add only source-proven navigation, and preserve confirmation and lock contracts.
- ChatGPT/controller responsibility: reconciled phone evidence and prohibited manual pre-navigation as substitute proof.
- User/operator responsibility: NONE.
- Prior warning applied: no invented AutoInput target; phone proof supersedes static assumptions; uncertainty must preserve awaiting-confirm state.
- Required repair: add Task 231 from exact Task 223 navigation nodes and call it once from Task 225 before screen proof.
- Required regression: start on Chats list; autonomously open exact bound conversation; exact confirmation; DONE readback; zero Send/Archive; confirmation lock released; profiles off.
- Status: REPAIRED CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT.
- Closing proof: independent artifact audit and direct Sosa phone recovery run.
- Prevention rule: confirmation must prove both navigation into the bound thread and independent visible sent-message evidence; neither substitutes for the other.
- Builds that must check this issue: Gate 13R2, remaining Gate 13 tests, Gate 14, and release.

## Phone-Failure Safety Reconciliation

- Exactly one confirmation task ran.
- No Send or Archive task ran.
- Task 225 released its owned confirmation lock.
- Result was `CONFIRM_UI_HOLD`; startup returned HOLD.
- The row remained `SEND_CLICKED_AWAITING_CONFIRM`.
- No unsafe behavior occurred.
<!-- GATE13R2_FAILURE_LEDGER_END -->

<!-- GATE13_PHONE_PROOF_CLOSURE_FAILURES_START -->
## Gate 13 Phone-Proof Failure Closures

Authority: newest direct Sosa phone proof supplied on 2026-07-14. Raw runlogs and private phone values remain outside the public repository. Codex records the proof and does not claim it independently.

### ISSUE_GATE13_BLANKET_LOCK_RESET_PATHS

- Status: VERIFIED CLOSED.
- Closing proof: active non-stale busy lock caused startup HOLD without release; stale busy lock released safely; STOP during a pending transaction preserved the unowned lock; clean STOP disabled triggers first and returned `STOPPED_CLEAN`.
- Required regression result: PASS by direct Sosa phone proof.
- Prevention rule retained: no blanket lock reset and no lock release without ownership or stale-age plus queue-state proof.
- User/operator responsibility: NONE.

### ISSUE_G13_KEYG_FALSE_HOLD_ANDROID16

- Status: VERIFIED CLOSED.
- Closing proof: the Android unlock probe passed both visibly unlocked and active locked-screen cases; screen-off separately failed closed as `TICK_SKIPPED_SCREEN_OFF`.
- Required regression result: PASS by direct Sosa phone proof.
- Prevention rule retained: platform-state signals require target-device proof and ambiguous results must HOLD.
- User/operator responsibility: NONE.

### ISSUE_G13_CONFIRM_RECOVERY_CHAT_LIST_HOLD

- Status: VERIFIED CLOSED.
- Closing proof: recovery navigated autonomously to the exact bound thread, independently proved the exact reply and immediate `Sent`, updated only the bound row to `DONE`, released the confirmation lock, and made zero Send and Archive calls during confirmation.
- Required regression result: PASS by direct Sosa phone proof.
- Prevention rule retained: confirmation must autonomously open the bound thread and separately prove the exact visible sent-message state.
- User/operator responsibility: NONE.

### ISSUE_GATE13_ENVIRONMENT_STATE_NOT_FULLY_DETECTABLE

- Status: PARTIAL / OPEN FOR GATE 14 RELEASE REVIEW.
- Gate 13 evidence closes screen-off and keyguard behavior only.
- Unsupported fold-state and battery/background-restriction behavior is not claimed and does not reopen Gate 13.
- Prevention rule retained: unsupported device states must not be advertised as release-proven.

Gate 13 is `LOCKED / PASS`; operational tracker is `13/14 locked = 93%`. Gate 14 remains blocked.
<!-- GATE13_PHONE_PROOF_CLOSURE_FAILURES_END -->


<!-- GATE14A_FAILURE_LEDGER_START -->
## ISSUE_GATE14_CAPACITY_MEASUREMENT_NOT_PHONE_PROVEN

- Status: OPEN / GATE 14A CANDIDATE.
- Risk: later capacity claims could be invalid if source-row order, exact count, ID uniqueness, or sender uniqueness cannot be measured independently.
- Prevention: Task 232 is read-only, manually authorized, prefix-bound, bounded to two reads, and retains separate integrity counters.
- Static evidence: exact 1/5/10/25/50 scenario models pass; duplicate and malformed cases hold; existing runtime is unchanged.
- Missing proof: target-phone import/render and authorized one-row read with the source row unchanged.
- No capacity, throughput, production, or release claim is made.
- User/operator responsibility: NONE.
<!-- GATE14A_FAILURE_LEDGER_END -->

<!-- GATE14A_R1_FAILURE_LEDGER_START -->
## ISSUE_G14A_BLANK_REPLY_OUTPUT_UNRESOLVED

- Status: `REPAIRED CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT`.
- First detected: direct Sosa phone execution of Gate 14A on 2026-07-15.
- Affected XML SHA256: `832BEB0F9764EB2838B08A582648097C49197C2A366931196E5F0311860529EF`.
- Symptom: a blank AutoSheets Reply element arrived as `%g14_reply89`, producing `INVENTORY_REPLY_HOLD`, nonblank Reply count 1, and unresolved count 1.
- Direct evidence: one successful Task 232 phone read bound the correct synthetic row; fresh direct Sheet proof showed the Reply cell was blank; no production or mutation path ran.
- Root cause: the static model represented a blank array element as an empty string and did not model Tasker's unresolved indexed-array placeholder.
- Codex responsibility: static validation missed the runtime representation.
- ChatGPT/controller responsibility: phone proof correctly identified and bounded the unsupported assumption.
- User/operator responsibility: `NONE`.
- Repair: Task 232 only clears `%row_reply` when it exactly matches `(?s)^[%]g14_reply[0-9]+$`.
- Regression: real replies, unrelated unresolved values, required fields, `#ERROR`, duplicate, order, count, and bounded-retry checks remain active.
- Tracker: `13/14 locked = 93%`; Gate 14 and PR merge remain blocked.
- Closing proof required: ChatGPT artifact audit followed by one separately authorized phone rerun.
<!-- GATE14A_R1_FAILURE_LEDGER_END -->

<!-- GATE14A_R2_FAILURE_LEDGER_START -->
## ISSUE_G14A_R1_CLEAR_LEAVES_ROW_REPLY_UNRESOLVED

- Status: `REPAIRED R2 CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT`.
- First detected: direct Sosa R1 phone run on 2026-07-15.
- Affected R1 XML SHA256: `34197CB7044B740F73B5ED173D26E7B73DE6B6602637B83F26F94D0ECDECD9FC`.
- Symptom: exact placeholder detection and Variable Clear executed, but later Tasker references exposed unresolved `%row_reply`; nonblank and unresolved counters each became 1.
- Safety result: Task 232 remained isolated, made one read, called no task, wrote no Sheet value, and returned `INVENTORY_REPLY_HOLD`.
- Fresh controller evidence: the exact staged row remained unchanged and its Reply cell was blank.
- Root cause: R1 assumed Variable Clear would remain a usable blank value in later Tasker comparisons.
- User/operator responsibility: `NONE`.
- Codex responsibility: R1 static modeling did not reproduce Tasker's cleared-local-variable representation.
- ChatGPT/controller responsibility: direct phone proof identified the mismatch and bounded the flag-based repair.
- R2 repair: reset `%reply_blank_norm = 0` per row, set it to 1 only for the exact indexed Reply placeholder, and gate only Reply nonblank/unresolved counters.
- Regression: real replies, unrelated unresolved values, required fields, `#ERROR`, duplicates, order, count, and bounded read handling remain active.
- Tracker: `13/14 locked = 93%`; Gate 14, PR merge, phone rerun, and release remain blocked.
- Closing proof required: independent artifact audit and a separately authorized R2 phone rerun.
<!-- GATE14A_R2_FAILURE_LEDGER_END -->

<!-- GATE14B_FAILURE_LEDGER_START -->
## ISSUE_G14B_PROCESSOR_WRITES_NOT_TRANSACTIONALLY_VERIFIED

- Status: `REPAIRED STATIC CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT`.
- Prior defect: processor wrappers could claim PROCESSING, Reply, final status, or failure status without exact A:E readback.
- Risk: OpenAI could be authorized after an unverified mark; Reply/status could split; wrong-row or changed-ID writes could go undetected.
- Repair: Task 233 requires exact A/B/C before every write, bounded attempts, and exact readback authority; wrappers only report verified outcomes.
- Partial success: verified Reply plus unverified final status routes to verified `ERROR_PROCESS_REVIEW` or a non-NEW partial HOLD; Reply is never cleared and NEW is never restored.
- Gate 14A historical issues are closed by direct Sosa R2 phone proof across 1/5/10/25/50; no production-capacity claim follows.
- User/operator responsibility: NONE.
- Codex responsibility: build/static proof only; no phone proof or import approval.
- Tracker remains `13/14 locked = 93%`; PR merge and Gate 14 completion remain blocked.
<!-- GATE14B_FAILURE_LEDGER_END -->

<!-- GATE14C_FAILURE_LEDGER_START -->
## ISSUE_G14C_UNBOUNDED_OPENAI_FAILURE_AND_LEGACY_RETRY_LOOP

- Status: `REPAIRED STATIC CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT`.
- Prior defect: HTTP failure could escape bounded cleanup; transient and permanent classes were not separated; complete response data could enter error logs; legacy `ERROR_OPENAI_RETRY` maintenance could repeatedly reset a row to NEW.
- Risk: stuck PROCESSING rows, unlimited cross-cycle API calls, cost growth, stale success data, and unsafe retry oscillation.
- Repair: Task 235 caps each run at two attempts with one 2-4 second jittered retry; Task 173 requests exact `ERROR_OPENAI_REVIEW`; Task 236 migrates legacy retry rows without API or NEW; Task 70 disconnects the old API retry-to-NEW branch.
- Static regression: 40/40 required cases PASS; independent validators PASS/PASS.
- Closing proof still required: ChatGPT artifact audit and direct Sosa controlled phone ladder.

## ISSUE_G14C_TASK233_REJECTS_ERROR_OPENAI_REVIEW

- Status: `REPAIRED STATIC CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT`.
- Pre-build finding: phone-proven Task 233 accepted `ERROR_PROCESS`, `ERROR_OPENAI_RETRY`, and `ERROR_PROCESS_REVIEW`, but rejected required `ERROR_OPENAI_REVIEW`.
- Codex responsibility: identified the contradiction before packaging and returned HOLD instead of bypassing the exact-row transaction engine.
- Controller decision: authorize one exact regex extension only.
- Repair proof: Task 233 action count remains 1947; old/new raw task hashes recorded; direct comparison shows one regex-string difference and no other field change.
- User/operator responsibility: NONE.
- Tracker remains `13/14 locked = 93%`; Gate 14C phone proof, PR merge, and release remain blocked.

## ISSUE_G14C_NO_RESPONSE_CODE_UNRESOLVED_LITERAL

- Status: `CLOSED BY DIRECT SOSA R1 PHONE PROOF`.
- Direct Sosa phone evidence: quota/no-retry passed; timeout exhaustion used two attempts, one retry, zero real HTTP calls, exact review persistence, blank Reply, and one lock release.
- Observed defect: when no real HTTP action returned a response code, Task 235 copied unresolved `%http_response_code` into its public result.
- Root cause: `Variable Clear` leaves the Tasker variable unresolved when later referenced.
- R1 repair: set `%http_response_code` to numeric `0` before every attempt and extend only the existing missing-code regex with `|^0$`.
- Regression boundary: Task 235 only; 243 actions remain 243; all other tasks, profiles, scene, and registry are unchanged.
- User/operator responsibility: NONE.
- Codex/static responsibility: the first Gate 14C model did not reproduce Tasker's unresolved no-response-code representation.
- Closing proof: R1 import/render, timeout exhaustion with numeric code 0, real-success code 200, and legacy migration all passed by direct Sosa proof.
- Closure details: all five Gate 14C modes passed; attempts stayed at two maximum, retries at one maximum, no third request occurred, exact review persistence passed, and every owned processing lock released once.
- Legacy closure: zero API attempts, zero retries, zero real HTTP calls, no processing lock, blank Reply preserved, and fresh exact-row readback confirmed `ERROR_OPENAI_REVIEW`.
- Remaining risk moved to Gate 14D-G; no Gate 14C runtime defect remains open.
- Tracker remains `13/14 locked = 93%`; merge and release remain blocked.
<!-- GATE14C_FAILURE_LEDGER_END -->
