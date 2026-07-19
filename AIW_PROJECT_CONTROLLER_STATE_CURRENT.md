# AI Worker Project Controller State

Status: CURRENT OPERATIONAL SOURCE TRUTH

## STATUS

`STATUS = 14/14 LOCKED = 100%`
`GATES_1_TO_14 = LOCKED`
`FULL_PRODUCT_RELEASE = HOLD`
`LIVE_ACTIVATION = OFF`
`PROFILE_ACTIVATION = OFF`
`PRODUCTION_WRITES = 0`

## Full Goal

Complete the autonomous AI Worker system that detects legitimate TextNow messages, logs exact Sheet rows, builds bounded context-aware OpenAI replies, opens the correct conversation, sends exactly once, confirms completion independently, archives safely, recovers from failures, runs until STOP, supports the final interface, and reaches the intended 50-contact reliability target.

## Current Phone-Proven Baseline

File: `AIW_GATE14_FINAL_PRIVATE_COPY_VALIDATOR_CANDIDATE.xml`

SHA256: `A170870077C50B2350EB94F823145E5FD80A22FBEA34D1096738DDBA0EEA2B98`

Gates 1-14 are locked by phone proof and must not be rebuilt or rerun without newer contradictory phone evidence.

## Current Capability

`CURRENT_CAPABILITY = DEADARCHIVE`

Classification: `REPAIR_REQUIRED`

Lock-contract sub-proof: `PHONE-PROVEN / LOCKED`

Integrated transaction build: `HOLD / MINIMUM TASK 229 RECOVERY CHANGE AUTHORIZED`

Permanent runtime guards are installed in Tasks 34, 73, 74, and 147.

Protected paths include Tasks 13, 18, 19, 24, 130, 131, 156, 199, 210, 226, 227, 228, and 229. Task 229 remains protected except for the exact bounded recovery-entry delta authorized below.

## R2 Phone-Proven Failure

Artifact: `AIW_DEADARCHIVE_LOCK_COMPATIBILITY_PROOF_CANDIDATE_R2.xml`

SHA256: `31A871EB97C923360A54812A04A5A78BC67477DEAD54729F237E75A002340CD6`

Run ID: `DAL-1784436735760`

Result: `HOLD`

Terminal: `HOLD_PROFILE_SOURCE_PRE`

Phone proof:
- `%dalenabledprofiles = %PENABLED`;
- `%dalactiveprofiles = %PACTIVE`;
- built-in profile variables remained unresolved literals;
- final complete `0`;
- release count `0`;
- manual cleanup required `0`;
- `%AIWDeadArchiving = 0`;
- `%AIWDeadArchiveOwner` blank;
- Tasker `ExitOK`;
- no workbook or production activity.

R2 must not be rerun.

## R3 Phone-Proven Lock Contract

Artifact: `AIW_DEADARCHIVE_LOCK_COMPATIBILITY_PROOF_CANDIDATE_R3.xml`

SHA256: `0DBA8B521C33FDECD62C3877A44A860EF9DA8125E0F604FE86782880E7FDD10C`

Accepted run ID: `DAL-1784441447757`

Result: `PASS`

Terminal: `DEADARCHIVE_LOCK_CONTRACT_PASS`

Phone proof confirmed:
- profile proof arm consumed from `1` to `0`;
- Boolean `%AIWDeadArchiving` remained compatible;
- `%AIWDeadArchiveOwner` remained separate;
- Tasks 34, 73, 74, and 147 blocked foreign or invalid reset attempts;
- matching-owner release succeeded exactly once;
- protected consumers remained unchanged;
- globals were restored;
- workbook touches, profile enables, live enables, and manual cleanup were all zero;
- final complete was `1` and Tasker exited normally.

Task 334 is locked proof evidence and must remain byte-identical. No additional lock-only package is authorized.

## Integrated DeadArchive Build HOLD

The complete transaction still requires Tasks 18, 19, and caller 199 to implement exact binding, destination copy/readback/uniqueness, idempotency, immediate source reread, exact A:I clear/readback, owner-first release, STOP handling, and restart reconciliation.

The prior three-task scope could not complete the mandatory restart contract. Current startup recovery holds on `%AIWDeadArchiving = 1` before Queue Cycle can reach Task 199, so Tasks 18 and 19 otherwise have no authorized re-entry after a restart at a persistent transaction boundary.

Authorized next-build exception: Task 229 may change only enough to provide one bounded recovery re-entry into Task 19 when `%AIWDeadArchiving = 1`, `%AIWDeadArchiveOwner` is a verified nonblank nonliteral owner, and persistent DeadArchive transaction state proves the same owned transaction requires reconciliation. The recovery call must pass the exact existing owner and a dedicated recovery mode, must start no new transaction, must never clear a foreign owner, and must preserve every unrelated Task 229 action and path.

Authorized integrated runtime scope is Tasks 18, 19, 199, plus only that minimum Task 229 recovery entry. All other Task 229 actions and every unrelated runtime task, profile, scene, registry, lifecycle, Send, Archive, live, or production-activation behavior must remain unchanged.

Current blocker: the authorized integrated candidate has not yet been built or independently audited. Do not build a partial candidate. Do not weaken restart reconciliation. Do not modify Task 334.

## Permanent Build Direction

R3 proves only the lock contract.

For the next integrated build:
- no additional lock-only package;
- move directly to one complete integrated DeadArchive transaction build;
- cover Tasks 18, 19, caller 199, canonical DeadView statuses, exact source ownership, destination copy/readback, uniqueness/idempotency, immediate source reread, exact A:I clear, clear readback, owner-first release, crash/restart reconciliation, STOP behavior, one-shot Queue Cycle maintenance activation, zero unowned reset, zero double release, and application-wide regression proof.

After DeadArchive:
1. Brain plus bounded normal-Archive conversation-context audit/build.
2. Final application-wide release audit.
3. Capacity, interface, live, and production proof.

## Mandatory Workflow

Every runtime change follows:
1. application-wide audit;
2. one exact repair;
3. immediate integrated full-project build;
4. Application Integrity Verifier;
5. one bounded phone test;
6. integrate or one minimal repair.

Every candidate is audited as part of the complete AI Worker application. Local proof may advance development; only integrated application-wide proof may advance release.

## Current Blocked Actions

Until exact candidate construction, independent audit, and phone approval:
- phone import;
- DeadArchive execution;
- Compactor;
- broad archive drains;
- production writes;
- TextNow;
- AutoInput;
- OpenAI;
- Send;
- DONE;
- Archive;
- Brain/context runtime;
- live or timer activation;
- profile activation;
- capacity execution;
- production activation;
- full-product release.

## Binary Phone Handoff

Use exactly:
- `APPROVED FOR ONE PHONE RUN`
- `REJECTED — ONE EXACT DEFECT / ONE MINIMAL REPAIR`
