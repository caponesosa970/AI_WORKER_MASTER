# AIW Final Validation Fixture-Safety Repair Current

Status: `STATIC REPAIR CANDIDATE / HOLD FOR CHATGPT ARTIFACT AUDIT AND PHONE PROOF`

Issue: `ISSUE_FINAL_VALIDATION_UNVERIFIED_FIXTURE_CLEANUP`

## Source truth

- Authorized PR head before work: `b403bbf76540a0c641b8f39930603cfcb4701221`.
- Exact repair base: `AIW_FINAL_INTEGRATED_FULL_PROJECT_TASKER_IMPORT_PRIVATE.xml`.
- Repair-base bytes: `4,411,599`.
- Repair-base SHA256: `9FB3A33852E12475CFA9A5D97F1157F67C69A9C0A007025CCD026BC9E26EB2A5`.
- Existing-task scope: Tasks `237`, `268`, `270`, `272`, `276`, and `293` only.
- Added scope: validation-only helper tasks, each below 500 actions.

## Original defect

- Task 272 passed fixed `Sheet1` rows 144-147 to destructive cleanup.
- Task 276 repeated rows 144-147 and passed `Archive`/`DeadArchive` row 999.
- Task 293 wrote blank values before proving row ownership.
- Task 237 selected fixed Gate 14C rows and fixture identities.
- Task 270 consumed fixed Archive/DeadArchive identities.
- Task 268 had no fixture-contract gate before Phase 0.
- Task 294 searched `Archive!A2:A1000`; it was reachable only from Task 276.

## Repair architecture

Task 268 now requires `FIXTURE_CONTRACT_READY` before any phase call. The contract validates one-shot run authorization, every role, every layer, row, maximum, protected range, expected identity, disposable payload, duplicate/conflicting configuration, physical caps, and current row state.

The fixture subsystem is split into bounded helpers:

| Task | Name | Actions | Role |
|---:|---|---:|---|
| 295 | AIW Validation Fixture Resolve Config | 323 | Resolve and validate controller-supplied role binding |
| 296 | AIW Validation Fixture Resolve Runtime | 224 | Resolve only an exact run-tracked synthetic row |
| 297 | AIW Validation Fixture Inspect Bound | 115 | Layer router and bound/auth guard |
| 298 | AIW Validation Fixture Contract | 270 | Complete pre-Phase-0 contract and one-shot activation |
| 299 | AIW Validation Fixture Setup Exact | 78 | Blank-read, one write, exact ownership readback |
| 300 | AIW Validation Fixture Cleanup Bound | 103 | Ownership-read, one clear, exact blank readback |
| 301 | AIW Validation Fixture Authorization Close | 22 | Verify configured fixtures blank, consume authorization |
| 302 | AIW Validation Fixture Inspect Sheet1 | 7 | Sheet1 inspection router |
| 303 | AIW Validation Fixture Inspect History | 275 | Archive and DeadArchive direct-row inspection |
| 304 | AIW Validation Fixture Inspect Queue Stores | 10 | Overflow/Journal inspection router |
| 305 | AIW Validation Fixture Inspect Overflow | 423 | Exact `A:N` OverflowInbox inspection |
| 306 | AIW Validation Fixture Inspect Journal | 423 | Exact `A:N` IngressJournal inspection |
| 307 | AIW Validation Fixture Read Sheet1 | 428 | Bounded exact `A:Z` Sheet1 read |
| 308 | AIW Validation Fixture Classify Sheet1 | 392 | Blank/owned/occupied classification |

## Existing task changes

- Task 237 obtains all Gate 14C row, identity, sender, message, and initial-status values from the verified binding. It performs safe setup before any controlled processing path.
- Task 268 calls the complete contract after run initialization and before Phase 0.
- Task 270 sets up the two history fixtures and uses run-owned controller values instead of fixed identities.
- Task 272 sends role identities, not literal rows, into cleanup.
- Task 276 removes the only Task 294 call, cleans configured roles dynamically, and closes authorization only after proof-ledger success.
- Task 293 is a small fail-closed router. Layer plus numeric row is insufficient; runtime rows must match one exact run-tracked row/identity pair.

The exact machine-readable action delta records every changed action and field. The semantic action groups are:

- Task 237: add fixture setup at candidate actions 66-71; bind row, ID, sender, message, and status at actions 73-79, 82-88, 91-97, 100-106, and 109-115; enable bounded error routing on two involved reads.
- Task 268: add the contract call and exact HOLD stop at actions 13-16, before the first phase call.
- Task 270: add history fixture setup at actions 14-21; replace the two fixed history ID/sender/message triples at actions 55-57 and 64-66.
- Task 272: pass roles `G14C_REAL`, `G14C_RATE`, `G14C_TIMEOUT`, and `G14C_QUOTA` at actions 38, 44, 50, and 56, with exact role-specific HOLD results at actions 40, 46, 52, and 58.
- Task 276: replace fixed cleanup targets with dynamic role cleanup at actions 87-119; remove the Task 294 call; close one-shot authorization at actions 134-137.
- Task 293: replace the 649-action arbitrary layer/row cleaner with a 24-action contract gate, exact configured/runtime resolver, and bounded cleanup helper call.

## Preserved boundary

- All other existing tasks are raw-byte identical to the repair base.
- Task 269 is raw-byte identical.
- Task 294 is raw-byte identical and unreachable from Task 268.
- Profiles and scenes are raw-byte identical.
- The Project registry changes only by adding Tasks 295-308.
- Production Send, confirmation, DONE, Archive lifecycle, OpenAI, AutoInput, processing, queue, START, STOP, and recovery tasks are unchanged.

## Oversized task disposition

No added helper exceeds 500 actions. The complete candidate still contains seven pre-existing reachable tasks above 500 actions: Tasks 223 (948), 226 (1,477), 233 (1,947), 248 (541), 254 (525), 255 (514), and 258 (1,525). All seven are raw-byte identical to the authorized base. They are not new helper violations and were outside this repair authorization. The package remains HOLD for controller audit and is not classified as phone-ready.

## Static and modeled result

- Standard Tasker audit: PASS, 152 tasks, 4 profiles, 2 scenes, zero duplicate IDs/names, and zero missing references.
- Independent fixture validator: 56/56 PASS.
- Independent integrated validator: 41/41 PASS.
- Fixture model: 23/23 unsafe cases, 21/21 fault cases, and 8/8 critical mutations detected.
- Fixture randomized model: 100,000 schedules, 4,755,111 operations, and zero unsafe writes.
- Connected-system model: 100,000 schedules, 2,576,571 operations, 134/134 boundary fault cases, and 15/15 mutations detected.
- Controller-independent rerun: 100,000 schedules, 1,997,907 operations, and all six mutations detected.

## Independent proof requirements

Acceptance requires direct XML inspection, an independent DOM validator, the standard Tasker static audit, complete graph and property inventory, a fixture state model, fault injection, at least 100,000 randomized schedules, at least 1,000,000 modeled operations, mutation detection for every critical fixture guard, ZIP equality, privacy checks, and Git scope proof.

These are development/static claims only. They do not prove Tasker import, AutoSheets behavior on the phone, TextNow UI behavior, a real Send, or phone runtime safety.

## Responsibility

- Codex: narrow byte-preserving build, independent static checks, private package, hashes, public-safe records, and conservative HOLD reporting.
- ChatGPT/controller: independently audit exact private artifacts, select fresh rows using read-only evidence, approve or reject migration and phone import.
- Sosa/operator: no action in this repair stage.

Phone import, Sheet migration, final orchestrator execution, PR merge, Gate 14 closure, and release remain HOLD.
