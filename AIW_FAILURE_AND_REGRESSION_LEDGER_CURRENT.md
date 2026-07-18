# AI Worker Failure and Regression Ledger

Status: CURRENT ACTIVE RELEASE-CAPABILITY HOLDS AND PERMANENT REGRESSIONS

Static audit cannot close a phone/runtime issue by itself.

## Active Release-Capability Holds

### ISSUE_DEADARCHIVE_PROOF_AND_AUTHORIZATION_PENDING

Status: `OPEN / RELEASE HOLD / READ-ONLY AUDIT REQUIRED`

First recorded: `2026-07-18`

Classification:

This is a proof-and-authorization gap, not an implementation-defect finding.

Affected capability:

- DeadArchive eligibility;
- routing;
- destination proof;
- exact-row ownership;
- idempotency;
- source clearing;
- lock ownership and release;
- interruption and restart recovery;
- STOP compatibility;
- activation control.

Current boundary:

DeadArchive is present or referenced in the current phone-proven full project, but it remains blocked, unproven, and unauthorized. Gate 14 did not prove or enable it. No DeadArchive task may be built, repaired, enabled, executed, or phone-tested before the read-only application-wide audit and an exact controller decision.

Required next proof:

1. Read-only inventory of every DeadArchive task, caller, trigger, variable, datasource, status rule, lock, and recovery path.
2. Compare current behavior to the permanent Archive contract, including exact-row ownership, destination readback, idempotency, safe source clear, interruption recovery, STOP, and activation boundaries.
3. Classify the existing implementation as exactly one of:
   - already sufficient but unproven;
   - repair required;
   - superseded or unnecessary.
4. Only after that classification define exact build, artifact-audit, and phone-proof counts.
5. No DeadArchive enablement or execution before ChatGPT approves an exact artifact.


Closing proof required:

- exact read-only application-wide inventory;
- complete caller/callee and reachable-path map;
- exact-row, destination, idempotency, source-clear, lock, interruption, restart, STOP, and activation analysis;
- classification of the existing implementation without assuming a defect;
- controller-approved proof ladder based on the audit;
- exact artifact audit and bounded phone proof if the audit determines they are required;
- preservation of locked Gates 1-14;
- independent ChatGPT release decision.

Prevention rule:

Do not infer a DeadArchive defect, approve DeadArchive execution, or invent build and phone-run counts before the read-only audit proves the current implementation and its complete application-wide impact.

### ISSUE_BRAIN_AND_ARCHIVE_CONTEXT_INTEGRATION_PENDING

Status: `OPEN / RELEASE HOLD / CONFIRMED INTEGRATION GAP / READ-ONLY AUDIT REQUIRED`

First recorded: `2026-07-18`

Affected capability:

- enabled Brain-rule retrieval;
- exact-sender normal-Archive history retrieval;
- chronological conversation-context construction;
- current same-sender group integration;
- OpenAI prompt assembly;
- context-size bounds;
- no cross-sender leakage;
- incomplete/uncertain-row exclusion;
- safe no-history fallback.

Confirmed evidence from the exact A170 artifact:

- same-sender current-message grouping is present and supports a maximum group size of four;
- no active AutoSheets action reads the Brain sheet;
- no active prompt-building action reads normal Archive conversation history;
- `%BrainRules` is cleared during reset but is not populated in the active processing path;
- `%ConversationHistory` is cleared during reset but is not populated in the active processing path;
- `PROCESS Build Prompt` uses a hard-coded system prompt and the newest/current grouped message only;
- Brain rules and prior archived conversation turns therefore do not reach the active OpenAI prompt.

Required audit before build:

1. Inventory all current grouping, prompt, OpenAI, Archive, Brain, SenderState, reset, and recovery tasks.
2. Trace the exact active processing call graph.
3. Define which normal Archive statuses are valid conversation history.
4. Define exact-sender identity normalization and matching.
5. Define chronological ordering.
6. Define bounded turn count and prompt-size limits.
7. Define incoming-message and confirmed-outgoing-reply formatting.
8. Define exclusion rules for DeadArchive, uncertain Send, incomplete rows, unrelated senders, duplicates, and malformed history.
9. Define safe no-history and failed-history-read behavior.
10. Only after the audit define exact build, artifact-audit, and phone-run counts.

Current planned counts:

- Brain/context build count: `UNDETERMINED PENDING AUDIT`
- Brain/context artifact-audit count: `UNDETERMINED PENDING AUDIT`
- Brain/context phone-run count: `UNDETERMINED PENDING AUDIT`

Closing proof will eventually require:

- enabled Brain rules proven in the final prompt;
- bounded exact-sender normal-Archive history proven in the final prompt;
- the current same-sender group appended last;
- no cross-sender leakage;
- no DeadArchive contamination;
- context-aware controlled phone reply proof;
- preservation of locked Gates 1-14.

Current boundary:

Do not build, enable, execute, or phone-test this capability in the source-correction run. DeadArchive remains the immediate next capability; Brain/context follows it. Full-product release remains `HOLD`.

Prevention rule:

A current-message grouping proof does not prove durable conversation context. Brain rules and exact-sender normal-Archive history must be traced into the exact final prompt, bounded, isolated, and independently proven before release.

## Verified Closed and Historical Failures

### ISSUE_GATE14_FINAL_VALIDATOR_CANDIDATE_UNAUDITED

Status: `CLOSED / PHONE-PROVEN GATE 14`

Closed: `2026-07-18`

Accepted artifact:

- File: `AIW_GATE14_FINAL_PRIVATE_COPY_VALIDATOR_CANDIDATE.xml`
- SHA256: `A170870077C50B2350EB94F823145E5FD80A22FBEA34D1096738DDBA0EEA2B98`
- Task: `AIW G14 FINAL PRIVATE COPY VALIDATOR`
- Task ID: `333`
- Accepted phone run: `G14V-1784387491`
- Result: `PASS`
- Terminal step: `FINAL_PRIVATE_COPY_VALIDATION_PASS`

Closing proof:

- exact full-project import and task rendering through action `1432`;
- OpenSlot before `75` and authorized range preblank;
- four exact single-row A:I writes and four exact row-level readbacks;
- full readback match count `36`;
- QueueView current-run count `4` during the fixture;
- exact source rows `75-78`, exact `SKIP_MANUAL` statuses, and uniqueness proof;
- OpenSlot during `79`;
- precleanup ownership match count `36` and cleanup authorization only after ownership proof;
- four exact single-row A:I clears;
- postcleanup range blank;
- QueueView current-run count `0` after cleanup and queue total restored;
- OpenSlot after `75`;
- manual cleanup required `0`;
- final complete `1` and normal Tasker `ExitOK`;
- faithful private copy restored;
- production untouched;
- zero TextNow, AutoInput, OpenAI, Send, DONE, Archive, DeadArchive, profile, live, shell, or network execution.

Gate effect:

- Gate 14 is `LOCKED` and phone-proven.
- Tracker is `14/14 LOCKED = 100%`.
- Gate 14 requires no rerun.
- Full-product release remains `HOLD`.

Permanent prevention rule:

No candidate may pass from zero-initialized or stale plugin outputs. Every success latch must include the phone-proven plugin success guard plus phase-specific identity, count, settlement, ownership, cleanup, and restoration proof.

### ISSUE_GATE14_R1_AUTOSHEETS_BLANK_RANGE_CONTRACT_UNPROVEN

Status: `CLOSED / PHONE-PROVEN DIAGNOSTIC`

Affected rejected artifact: `AIW_GATE14_REAL_PRODUCT_CONTRACT_R1_PRIVATE.xml`, SHA256 `B291963FEFD5C9DD938F69F8CE0C1C4CB3318E21DF17EA6646FB14C4594730CC`.

Closing proof:

- Diagnostic: `AIW_G14_AUTOSHEETS_CONTRACT_DIAGNOSTIC_NO_WRITE.tsk.xml`
- SHA256: `C5818297BEE535DF5B9B6DB7C862B63F15949483BA73A2D7C59B12DCE97AE411`
- Phone run: `G14D-1784348825`
- Blank success rendered literal `%err` and `%errmsg` with A:I counts all `0`.
- Populated success rendered literal `%err` and `%errmsg` with A:I counts all `1`.
- Controlled failure returned a numeric `%err`, missing-tab `%errmsg`, A:I counts all `0`, and continued after error.

Confirmed root cause:

R1's broad `%err` regex falsely classified the phone-proven unresolved success rendering as an error.

Permanent prevention rule:

Clear error variables and output arrays before every Get Data action, snapshot error variables immediately after it, and apply the accepted literal success contract plus exact phase evidence. Never restore the rejected broad regex.

Builds that must check it: every AutoSheets diagnostic and validator.

### ISSUE_GATE14_FINAL_VALIDATOR_ACTION_BOUND_HELPER_SCOPE

Status: `RESOLVED / SINGLE-TASK 1477-ACTION CONTROLLER DECISION`

Resolution:

The controller withdrew the helper architecture and 220-action cap. Gate 14 used exactly one new task with a source-backed hard maximum equal to the verified predecessor-baseline maximum of 1477 actions. The phone-proven task uses 1432 actions. No helper or `Perform Task` action exists.

Permanent prevention rule:

Reconcile required proof behavior with verified Tasker task limits before construction. Do not invent helper authority or weaken proof to meet an arbitrary cap.

Builds that must check it: future large Tasker validation artifacts.

### ISSUE_CONTROL_SOURCE_TRUTH_DUPLICATION_LOOP

Status: `HISTORICAL / CONSOLIDATION MERGED TO MAIN`

Permanent prevention rule:

Use the four retained root source-truth files. Do not recreate deleted controller files, report frameworks, matrices, or duplicate current-state sections.

Builds that must check it: every controller/source synchronization.

### ISSUE_GATE14_DATASOURCE_AUTHORITY_MISMATCH

Status: `SUPERSEDED / HISTORICAL CONTEXT`

Historical root cause:

An earlier staging fixture writer and validation reader used different workbook authorities. No phone execution proved that defect. The faithful private-copy architecture superseded it.

Permanent prevention rule:

Never collapse distinct workbook authorities into one abstract store during simulation. A validation path may resolve only to its explicitly authorized authority and must preserve production isolation.

Builds that must check it: every validation artifact.

## Permanent Workflow Controls

| Control | Permanent rule | Must check in |
| --- | --- | --- |
| Source lock | Freeze current main SHA, PR head, and artifact SHA before every material decision; regenerate the decision if any source moves. | Every material decision and merge |
| Prompt compiler | Classify requirements as product, safety, source-proven, phone-proven, controller choice, or unresolved assumption; unresolved assumptions cannot become mandatory facts. | Every controller dispatch |
| Pre-dispatch checks | Contradiction, missing-information, evidence-retrieval, privacy, cleanup, and locked-work checks must pass before dispatch. | Every build, audit, phone handoff, and release decision |
| Exact artifact verifier | Codex reports cannot approve their own artifact; ChatGPT independently audits exact bytes, SHA256, call graph, mutations, cleanup, evidence, and protected nodes. | Every artifact approval |
| Binary phone handoff | Phone handoff is exactly `APPROVED FOR ONE PHONE RUN` or `REJECTED — ONE EXACT DEFECT / ONE MINIMAL REPAIR`. | Every phone-test decision |

## Permanent Regression Requirements

| Issue / class | Status | Permanent prevention rule | Must check in |
| --- | --- | --- | --- |
| Static/package proof is not phone proof | PERMANENT | Do not approve phone-visible behavior from Codex summaries, XML parse, generated CSV, simulator, or static report alone. | Every phone-test request and release claim |
| Phone proof supersedes static audit | PERMANENT | When phone proof contradicts static claims, update source truth before further repair. | Every runtime failure triage |
| Generated reports can be incomplete | PERMANENT | A generated report cannot prove its own correctness; use independent verification. | Every artifact audit |
| Encoding and unchanged-byte drift | PERMANENT | Preserve Tasker XML encoding and unchanged regions; reject unexplained special-character or protected-node drift. | Every runtime XML build |
| External plugin output assumptions | PERMANENT | Isolate exact external output contracts with durable phone-visible evidence before integration. | Every plugin path |
| Stale plugin outputs | PERMANENT | Clear errors and output arrays, snapshot immediately, and require exact phase evidence; zero-initialized counters never authorize PASS. | Every AutoSheets phase |
| Wrong-recipient Send | PERMANENT | Prove exact recipient/thread before compose or Send. | Every Send-capable artifact |
| Stale reply Send | PERMANENT | Prove row, ID, sender, message, reply, and status binding before Send. | Every processing and Send artifact |
| Duplicate Send | PERMANENT | Check prior send-attempt and sent state before any reset; no retry after uncertainty. | Every Send/recovery artifact |
| DONE before confirmation | PERMANENT | DONE requires independent confirmation, never Send-click evidence alone. | Every confirmation/DONE artifact |
| Archive before exact proof | PERMANENT | Archive requires confirmed completion, exact copy/readback, uniqueness, and safe source clear. | Every Archive artifact |
| DeadArchive authorization | PERMANENT | Do not enable or execute DeadArchive before a read-only application-wide audit, controller classification, exact artifact approval, and any required phone proof. | Every DeadArchive decision |
| Lock release defect | PERMANENT | Every owned terminal path releases exactly once; no unowned release. | Every lock/recovery artifact |
| AutoInput target drift | PERMANENT | No guessed AutoInput target; preserve and prove phone-visible fields. | Every TextNow/AutoInput artifact |
| Credential drift | PERMANENT | Verify current credential source privately without printing or committing values. | Every private package |
| AutoSheets timeout after lock | PERMANENT | Bound retries and release/close locks on final failure before TextNow. | Every Sheet-read-before-Send path |
| Cleanup ownership | PERMANENT | Clear only an exact current-run row after immediate full ownership proof; leave blank or unknown rows untouched and HOLD. | Every validation and Archive cleanup |
| Formula settlement | PERMANENT | Poll within a fixed bound; a failed read or unsettled formula blocks PASS and never triggers automatic rerun. | Every view/formula validation |
| Lifecycle ordering | PERMANENT | One lifecycle transition per cycle; unresolved Send states block new Send selection. | Every queue-cycle artifact |
| STOP/profile safety | PERMANENT | STOP prevents new work and leaves runtime profiles disabled; no silent profile enablement. | Every STOP/recovery/runtime artifact |
| Gate 9 controlled Send | LOCKED | Do not rerun or reopen without newer contradictory phone proof. | Every later regression audit |
| Gate 10 confirmation and DONE | LOCKED | Preserve confirmation separate from Send and DONE only after confirmation. | Every later regression audit |
| Gate 11 exact-row Archive | LOCKED | Preserve exact-row Archive and source-clear boundaries. | Every later regression audit |
| Gate 12 queue lifecycle | LOCKED | Preserve one lifecycle transition per cycle. | Every later regression audit |
| Gate 13 timer, STOP, background guard, recovery | LOCKED | Preserve STOP, busy overlap, screen-off, timer, and recovery behavior. | Every later regression audit |
| Gate 14 validation and isolation | LOCKED | Preserve the phone-proven AutoSheets contract, exact readback, ownership-safe cleanup, restoration, production isolation, and forbidden-path isolation. | Every later regression and release audit |
| Gates 1-14 | LOCKED | Do not rerun or reopen a locked gate without newer contradictory phone proof. | Every regression and release audit |

## Current Counts and Boundary

- Gate 14 runtime builds remaining: `0`
- Gate 14 artifact audits remaining: `0`
- Gate 14 phone runs remaining: `0`
- Gate 14 private-copy controlled runs remaining: `0`
- Gate 14 gate decisions remaining: `0`
- DeadArchive build count: `UNDETERMINED PENDING AUDIT`
- DeadArchive artifact-audit count: `UNDETERMINED PENDING AUDIT`
- DeadArchive phone-run count: `UNDETERMINED PENDING AUDIT`
- Brain/context build count: `UNDETERMINED PENDING AUDIT`
- Brain/context artifact-audit count: `UNDETERMINED PENDING AUDIT`
- Brain/context phone-run count: `UNDETERMINED PENDING AUDIT`
- Full-product release decision: `PENDING`

Gate 14 is phone-proven and locked. Full-product release remains `HOLD`. DeadArchive remains the immediate next audit capability; Brain plus bounded normal-Archive conversation-context integration follows it. A final application-wide release audit occurs after both known capability holds are resolved, and the known list is not exhaustive until that audit. DeadArchive, Brain/context integration, Compactor, broad archive drains, live activation, production activation, and capacity execution remain blocked unless separately authorized.