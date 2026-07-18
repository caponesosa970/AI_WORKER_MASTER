# AI Worker Failure and Regression Ledger

Status: CURRENT ACTIVE FAILURES AND PERMANENT REGRESSIONS

Every active failure remains open until it has a bounded repair, regression proof, and ChatGPT-reviewed closing proof.

Static audit cannot close a phone/runtime issue by itself.

## Active Failures

### ISSUE_GATE14_R1_AUTOSHEETS_BLANK_RANGE_CONTRACT_UNPROVEN

Status: `OPEN / RUNTIME HOLD`

First detected: `2026-07-18`

Affected artifact:

`AIW_GATE14_REAL_PRODUCT_CONTRACT_R1_PRIVATE.xml`

SHA256:

`B291963FEFD5C9DD938F69F8CE0C1C4CB3318E21DF17EA6646FB14C4594730CC`

Affected task:

`AIW REAL PRODUCT CONTRACT R1 LAUNCHER`

Task ID:

`329`

Affected action:

Human Action 52 / XML action `act51`

Observed phone result:

- AutoSheets OpenSlotView read completed.
- Rows 75-78 were selected.
- AutoSheets blank-range read of faithful-copy `Sheet1 A75:I78` completed.
- `%pav_read_ok` was set to `1`.
- Human Action 52 evaluated true.
- `%pav_read_ok` was reset to `0`.
- Task stopped at `PHASE_A_NO_WRITE`.
- No Sheet write occurred.
- No TextNow, OpenAI, Send, DONE, Archive, DeadArchive, or profile action occurred.

Root-cause class:

`UNPROVEN AUTOSHEETS BLANK-RANGE OUTPUT CONTRACT`

Current known defect:

Codex simulated AutoSheets blank-range behavior using assumptions that were not isolated on the phone. Static and simulated PASS claims overstated proof. The phone result proves the R1 candidate cannot continue past the blank-range read guard, but it does not yet prove the exact `%err`, `%errmsg`, or A:I array state.

Required diagnostic proof:

One corrected bounded no-write diagnostic must phone-prove exactly:

- blank-range success behavior against faithful-copy `Sheet1 A75:I78`;
- populated-range structural behavior against faithful-copy `Sheet1 A1:I1`, logging counts and shape only, not header values;
- `%err` and `%errmsg` state/rendering;
- unset-variable rendering;
- A:I array existence/count/shape;
- one controlled private-copy AutoSheets failure with Continue Task After Error ON using nonexistent tab `AIW_DIAG_MISSING_TAB_20260718` and range `A1:I1`;
- durable retrievable evidence output through one phone-proven Tasker Run Log action and a preserved global summary variable.

Required integration proof:

One final integrated private-copy validator must phone-prove:

- open-row selection;
- approved fixture write;
- exact readback;
- QueueView/formula settlement;
- queue non-contamination;
- cleanup identity and execution;
- cleanup readback;
- OpenSlotView restoration;
- production workbook untouched;
- no TextNow, OpenAI, Send, DONE, Archive, DeadArchive, or profile reachability;
- locked baseline preservation.

Current planned counts:

- Runtime builds remaining: `2`
- ChatGPT artifact audits remaining: `2`
- Phone runs remaining: `2`
- Private-copy write runs remaining: `1`
- Production write runs remaining: `0`
- Release decisions remaining: `1`

Prevention rule:

No future Gate 14 build may integrate external plugin output assumptions unless the exact external contract is first isolated with phone-visible, durable, retrievable evidence.

Regression rule:

Mocks and mutations must include separate cases for:

- unset `%err` rendered literally;
- set-empty `%err`;
- numeric `%err`;
- `#ERROR`;
- missing arrays;
- zero-length arrays;
- one-empty-item arrays;
- populated arrays;
- controlled AutoSheets failure;
- stale output arrays.

Static or simulated evidence cannot close this issue.

Closing proof required:

- ChatGPT-approved corrected diagnostic artifact.
- One diagnostic phone run with complete durable structural evidence.
- ChatGPT-approved final integrated private-copy validator.
- One integrated phone run proving write/readback/formula settlement/cleanup/protection.
- Production workbook unchanged.
- Tracker remains 13/14 until ChatGPT release decision.

## Historical Context

### ISSUE_CONTROL_SOURCE_TRUTH_DUPLICATION_LOOP

Status: `HISTORICAL / CONSOLIDATION MERGED TO MAIN`

The active root source truth was consolidated into four files. Do not recreate deleted controller files, ledgers, matrices, preflight files, report directories, or replacement frameworks when the four retained files can carry the required source truth.

### ISSUE_GATE14_DATASOURCE_AUTHORITY_MISMATCH

Status: `SUPERSEDED / HISTORICAL CONTEXT`

Root cause:

The earlier Gate 14 Phase A fixture writer and validator used different workbook authorities.

Direct static evidence:

- Task 329 wrote the fixture under staging-workbook authority.
- Task 328 invoked Task 325.
- Task 325 read under production-workbook authority.
- The validator could not read the exact fixture Task 329 wrote.

Phone-proof classification:

No phone execution proved this datasource defect.

Current disposition:

R1 superseded the staging datasource path by moving the validation launcher to the faithful private copy, but R1 is rejected because phone evidence exposed the newer AutoSheets blank-range output contract blocker before any Sheet write occurred.

Prevention rule:

Never collapse separate workbook IDs or datasource authorities into one abstract store during simulation or validation.

## Permanent Regression Requirements

| Issue / class | Status | Permanent prevention rule | Must check in |
| --- | --- | --- | --- |
| Static/package proof is not phone proof | PERMANENT | Do not approve phone-visible behavior from Codex summaries, XML parse, generated CSV, simulator, or static report alone. | Every phone-test request and release claim |
| Phone proof supersedes static audit | PERMANENT | When phone proof contradicts static claims, update source truth before further repair. | Every runtime failure triage |
| Generated reports can be incomplete | PERMANENT | A generated report cannot prove its own correctness; use independent verification. | Every artifact audit |
| Encoding/mojibake drift | PERMANENT | Preserve Tasker XML encoding and unchanged regions; reject special-character drift. | Every runtime XML build |
| Wrong-recipient Send | PERMANENT | Prove exact recipient/thread before compose or Send. | Every Send-capable artifact |
| Stale reply Send | PERMANENT | Prove row, ID, sender, message, reply, and status binding before Send. | Every processing and Send artifact |
| Duplicate Send | PERMANENT | Check prior send-attempt and sent state before any reset; no retry after uncertainty. | Every Send/recovery artifact |
| DONE before confirmation | PERMANENT | DONE requires independent confirmation, never Send-click evidence alone. | Every confirmation/DONE artifact |
| Archive before exact proof | PERMANENT | Archive requires confirmed completion, exact copy/readback, uniqueness, and safe source clear. | Every Archive artifact |
| Lock release defect | PERMANENT | Every owned terminal path releases exactly once; no unowned release. | Every lock/recovery artifact |
| AutoInput target drift | PERMANENT | No guessed AutoInput target; preserve and prove phone-visible fields. | Every TextNow/AutoInput artifact |
| Credential drift | PERMANENT | Verify current credential source privately without printing or committing values. | Every private package |
| AutoSheets timeout after lock | PERMANENT | Bound retries and release/close locks on final failure before TextNow. | Every Sheet-read-before-Send path |
| External plugin output assumptions | PERMANENT | Do not integrate unproven AutoSheets or plugin output shape; isolate the exact phone-visible contract first with durable evidence. | Every Gate 14 diagnostic and runtime validator |
| Lifecycle ordering | PERMANENT | One lifecycle transition per cycle; unresolved Send states block new Send selection. | Every queue-cycle artifact |
| STOP/profile safety | PERMANENT | STOP prevents new work and leaves runtime profiles disabled; no silent profile enablement. | Every STOP/recovery/runtime artifact |
| Gate 9 controlled Send | LOCKED | Do not rerun or reopen without newer contradictory phone proof. | Gate 14 regression audit |
| Gate 10 independent confirmation and DONE | LOCKED | Preserve confirmation separate from Send and DONE only after confirmation. | Gate 14 regression audit |
| Gate 11 exact-row Archive | LOCKED | Preserve exact-row Archive and source-clear boundaries. | Gate 14 regression audit |
| Gate 12 queue lifecycle | LOCKED | Preserve one lifecycle transition per cycle. | Gate 14 regression audit |
| Gate 13 timer, STOP, background guard, recovery | LOCKED | Preserve STOP, busy overlap, screen-off, timer, and recovery behavior. | Gate 14 regression audit |

## ISSUE_GATE14_FINAL_VALIDATOR_ACTION_BOUND_HOLD

Status: `OPEN / HOLD`

First detected: 2026-07-18

Affected work:

- Final Gate 14 private-copy validator Build 2.
- Public source synchronization for diagnostic phone proof.

Direct evidence:

- The accepted no-write diagnostic phone run `G14D-1784348825` resolved the AutoSheets blank/populated/failure output contract.
- The final validator prompt requires a complete private-copy write, row-level readback, 36-cell readback, QueueView settlement, OpenSlot proof, precleanup ownership proof, exact cleanup, postcleanup blank proof, QueueView removal, OpenSlot restoration, fail-closed evidence, and forbidden-path counters.
- A direct single-runner implementation using only proven Tasker/native/plugin action shapes exceeds the current runner action limit.
- The prompt authorizes helper tasks, but the named helper contracts restrict them to audit-only/no-plugin behavior, so they cannot safely absorb the plugin-bearing write/read/cleanup phases without a controller correction.

Current root cause:

The remaining validator behavior is larger than the current runner action bound when implemented with proven action shapes and explicit fail-closed evidence. The helper allowance is not broad enough to split the plugin-bearing phases safely.

Diagnostic phone proof now locked:

- Artifact: `AIW_G14_AUTOSHEETS_CONTRACT_DIAGNOSTIC_NO_WRITE.tsk.xml`
- SHA256: `C5818297BEE535DF5B9B6DB7C862B63F15949483BA73A2D7C59B12DCE97AE411`
- Phone run: `G14D-1784348825`
- Blank success: literal `%err`, literal `%errmsg`, A:I counts all `0`.
- Populated success: literal `%err`, literal `%errmsg`, A:I counts all `1`.
- Controlled failure: numeric `%err`, missing-tab `%errmsg`, A:I counts all `0`, Continue After Error confirmed.

Rejected R1 regression:

R1 must not be reused. Its broad `%err` regex falsely classifies the phone-proven success rendering as failure.

Prevention rule:

Before any new final-validator build, the controller must reconcile behavior size with Tasker action bounds. If helper tasks are authorized to carry plugin phases, their exact scope must be stated. If not, the runner action limit must be increased or the validator proof must be split by controller approval.

Closing proof required:

- Updated controller instruction resolving the action-bound/helper-scope conflict.
- A candidate built from the Gate13R2 baseline only.
- Existing baseline task/profile/scene preservation proof.
- Production authority count preserved.
- New validation path contains zero production authority.
- Exact private-copy write/readback/formula/cleanup proof path configured.
- Static and mutation audit against the exact returned artifact.
- ChatGPT artifact approval before phone import.
- One final phone run proving private-copy cleanup/restoration.

Public-source privacy rule:

- Production authority alias: `AIW_PRODUCTION_WORKBOOK_AUTHORITY_PRIVATE`.
- Faithful private-copy authority alias: `AIW_GATE14_FAITHFUL_COPY_AUTHORITY_PRIVATE`.
- Exact workbook IDs must remain private and must not be added to public GitHub, PR text, reports, or final returns.
- Git history has not been purged; separate history remediation is outside this issue.

Current remaining counts:

- Runtime builds remaining: `1`
- ChatGPT artifact audits remaining: `1`
- Phone runs remaining: `1`
- Private-copy controlled runs remaining: `1`
- Production write runs remaining: `0`
- Release decisions remaining: `1`

Sosa responsibility: `NONE`.

Tracker effect: `NONE`; tracker remains `13/14 LOCKED = 93%`.
