# AI Worker Failure and Regression Ledger

Status: CURRENT ACTIVE FAILURES AND PERMANENT REGRESSIONS

Static audit cannot close a phone/runtime issue by itself.

## Active Failures

### ISSUE_GATE14_FINAL_VALIDATOR_CANDIDATE_UNAUDITED

Status: `OPEN / CANDIDATE HOLD`

First detected: `2026-07-18`

Affected capability:

Final Gate 14 faithful-private-copy write, exact readback, QueueView settlement, ownership-safe cleanup, and restoration proof.

Current candidate:

- File: `AIW_GATE14_FINAL_PRIVATE_COPY_VALIDATOR_CANDIDATE.xml`
- SHA256: `A170870077C50B2350EB94F823145E5FD80A22FBEA34D1096738DDBA0EEA2B98`
- New task: `AIW G14 FINAL PRIVATE COPY VALIDATOR`
- Task ID: `333`
- Action count: `1432`
- Architecture: one manually executed plugin-bearing task, no helpers, no `Perform Task`, no profile or scene trigger.

Current evidence:

- Build 1 AutoSheets contract diagnostic is phone-proven under run `G14D-1784348825`.
- Build 2 is built from the exact Gate13R2 baseline and is static-only.
- Existing baseline task, profile, scene, action, credential-bearing, and production-datasource subtrees are preserved.
- Baseline production-authority count remains `206`; the new task contains zero production authority.
- The new task uses exactly four single-row A:I writes and four single-row A:I clears for rows 75-78.
- Independent static review found and repaired a post-cleanup QueueView false-success path, a preflight fifth-entry authorization gap, and incomplete Popup evidence before the final SHA was accepted.
- The final exact SHA has passed static and independent semantic review, but has not been imported or executed on the phone.

Required closing proof:

1. ChatGPT audits the exact PR #13 head.
2. ChatGPT audits the exact XML and SHA256 sidecar.
3. ChatGPT accepts baseline preservation, production-isolation, range, control-flow, evidence, and mutation proof.
4. ChatGPT approves the exact artifact for one phone run.
5. One phone run proves open-row selection, prewrite blank state, four exact fixture writes, exact row readbacks, 36-cell proof, QueueView settlement, OpenSlot 79, current-run ownership, four exact clears, post-cleanup blank state, QueueView restoration, OpenSlot 75, production untouched, and zero forbidden execution.
6. ChatGPT reconciles the phone evidence and makes the one remaining release decision.

Prevention rule:

No candidate may pass from zero-initialized or stale plugin outputs. Every success latch must include the phone-proven plugin success guard plus the phase-specific identity, count, settlement, and ownership proof.

Tracker effect: `NONE`; tracker remains `13/14 LOCKED = 93%`.

## Verified Closed and Historical Failures

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

Builds that must check it: every Gate 14 AutoSheets diagnostic and validator.

### ISSUE_GATE14_FINAL_VALIDATOR_ACTION_BOUND_HELPER_SCOPE

Status: `RESOLVED / SINGLE-TASK 1477-ACTION CONTROLLER DECISION`

Resolution:

The controller withdrew the helper architecture and 220-action cap. Build 2 uses exactly one new task with a source-backed hard maximum equal to the verified baseline maximum of 1477 actions. The current task uses 1432 actions. No helper or `Perform Task` action exists.

Permanent prevention rule:

Reconcile required proof behavior with verified Tasker task limits before construction. Do not invent helper authority or weaken proof to meet an arbitrary cap.

Builds that must check it: final Gate 14 validator artifacts.

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

Never collapse distinct workbook authorities into one abstract store during simulation. The new validation path may resolve only to the faithful private-copy authority and must contain zero production authority.

Builds that must check it: every Gate 14 validation artifact.

## Permanent Regression Requirements

| Issue / class | Status | Permanent prevention rule | Must check in |
| --- | --- | --- | --- |
| Static/package proof is not phone proof | PERMANENT | Do not approve phone-visible behavior from Codex summaries, XML parse, generated CSV, simulator, or static report alone. | Every phone-test request and release claim |
| Phone proof supersedes static audit | PERMANENT | When phone proof contradicts static claims, update source truth before further repair. | Every runtime failure triage |
| Generated reports can be incomplete | PERMANENT | A generated report cannot prove its own correctness; use independent verification. | Every artifact audit |
| Encoding and unchanged-byte drift | PERMANENT | Preserve Tasker XML encoding and unchanged regions; reject unexplained special-character or protected-node drift. | Every runtime XML build |
| External plugin output assumptions | PERMANENT | Isolate exact external output contracts with durable phone-visible evidence before integration. | Every Gate 14 plugin path |
| Stale plugin outputs | PERMANENT | Clear errors and output arrays, snapshot immediately, and require exact phase evidence; zero-initialized counters never authorize PASS. | Every AutoSheets phase |
| Wrong-recipient Send | PERMANENT | Prove exact recipient/thread before compose or Send. | Every Send-capable artifact |
| Stale reply Send | PERMANENT | Prove row, ID, sender, message, reply, and status binding before Send. | Every processing and Send artifact |
| Duplicate Send | PERMANENT | Check prior send-attempt and sent state before any reset; no retry after uncertainty. | Every Send/recovery artifact |
| DONE before confirmation | PERMANENT | DONE requires independent confirmation, never Send-click evidence alone. | Every confirmation/DONE artifact |
| Archive before exact proof | PERMANENT | Archive requires confirmed completion, exact copy/readback, uniqueness, and safe source clear. | Every Archive artifact |
| Lock release defect | PERMANENT | Every owned terminal path releases exactly once; no unowned release. | Every lock/recovery artifact |
| AutoInput target drift | PERMANENT | No guessed AutoInput target; preserve and prove phone-visible fields. | Every TextNow/AutoInput artifact |
| Credential drift | PERMANENT | Verify current credential source privately without printing or committing values. | Every private package |
| AutoSheets timeout after lock | PERMANENT | Bound retries and release/close locks on final failure before TextNow. | Every Sheet-read-before-Send path |
| Cleanup ownership | PERMANENT | Clear only an exact current-run row after immediate full ownership proof; leave blank or unknown rows untouched and HOLD. | Every validation and Archive cleanup |
| Formula settlement | PERMANENT | Poll within a fixed bound; a failed read or unsettled formula blocks PASS and never triggers automatic rerun. | Every view/formula validation |
| Lifecycle ordering | PERMANENT | One lifecycle transition per cycle; unresolved Send states block new Send selection. | Every queue-cycle artifact |
| STOP/profile safety | PERMANENT | STOP prevents new work and leaves runtime profiles disabled; no silent profile enablement. | Every STOP/recovery/runtime artifact |
| Gate 9 controlled Send | LOCKED | Do not rerun or reopen without newer contradictory phone proof. | Gate 14 regression audit |
| Gate 10 confirmation and DONE | LOCKED | Preserve confirmation separate from Send and DONE only after confirmation. | Gate 14 regression audit |
| Gate 11 exact-row Archive | LOCKED | Preserve exact-row Archive and source-clear boundaries. | Gate 14 regression audit |
| Gate 12 queue lifecycle | LOCKED | Preserve one lifecycle transition per cycle. | Gate 14 regression audit |
| Gate 13 timer, STOP, background guard, recovery | LOCKED | Preserve STOP, busy overlap, screen-off, timer, and recovery behavior. | Gate 14 regression audit |

## Current Counts and Boundary

- Runtime builds remaining: `0`
- ChatGPT artifact audits remaining: `1`
- Phone runs remaining: `1`
- Faithful-copy controlled mutation runs remaining: `1`
- Production write runs remaining: `0`
- Release decisions remaining: `1`

The candidate remains `HOLD`. Phone import, Tasker execution, workbook mutation, tracker movement, Gate 14 closure, and production release remain blocked until ChatGPT approves the exact artifact and the remaining phone proof is accepted.