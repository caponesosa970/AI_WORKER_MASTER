# AI Worker Failure and Regression Ledger

Status: CURRENT ACTIVE RELEASE-CAPABILITY HOLDS AND PERMANENT REGRESSIONS

Static, model, simulation, or local audit cannot close a phone/runtime issue. Generated reports cannot approve themselves.

## ISSUE_DEADARCHIVE_REPAIR_REQUIRED

Status: `OPEN / HARD HOLD / R3 LOCK SUB-PROOF PHONE-PROVEN / PRODUCTION REPAIR BLOCKED / ONE NO-WRITE QUEUEVIEW DIAGNOSTIC AUTHORIZED`

Classification: `REPAIR_REQUIRED`

Locked facts:

- application-wide DeadArchive audit classified the implementation as repair required;
- Boolean compatibility lock remains `%AIWDeadArchiving = 0/1`;
- owner token remains separate in `%AIWDeadArchiveOwner`;
- permanent foreign-reset guards exist in Tasks 34, 73, 74, and 147;
- Task 334 is locked proof evidence and must remain byte-identical;
- no additional lock-only package is authorized;
- Gates 1-14 remain locked.

### Historical Lock-Compatibility R2

Artifact: `AIW_DEADARCHIVE_LOCK_COMPATIBILITY_PROOF_CANDIDATE_R2.xml`

SHA256: `31A871EB97C923360A54812A04A5A78BC67477DEAD54729F237E75A002340CD6`

Phone run `DAL-1784436735760` ended `HOLD_PROFILE_SOURCE_PRE`; `%PENABLED` and `%PACTIVE` remained unresolved; the task exited safely with idle lock/owner, zero workbook/production mutation, and no cleanup requirement. It must not be rerun.

### R3 Phone-Proven Lock Contract

Artifact: `AIW_DEADARCHIVE_LOCK_COMPATIBILITY_PROOF_CANDIDATE_R3.xml`

SHA256: `0DBA8B521C33FDECD62C3877A44A860EF9DA8125E0F604FE86782880E7FDD10C`

Accepted run: `DAL-1784441447757`

Result/terminal: `PASS / DEADARCHIVE_LOCK_CONTRACT_PASS`

The exact phone boundary proved profile-arm consumption, Boolean lock compatibility, separate owner, foreign/invalid reset blocking, matching-owner release once, protected-consumer preservation, global restoration, zero workbook/profile/live/manual-cleanup activity, final complete `1`, and normal Tasker exit. It did not prove the integrated transaction.

### QueueView Diagnostic-First Phone Evidence

Confirmed phone facts:

1. `FINAL Queue Cycle` direct manual entry stopped safely before DeadArchive.
2. `APP Run Tick Once` first stopped because `%AIWorkerTimerOn` was not armed.
3. After arming the timer, Live Tick reached the DeadArchive guard and stopped because `%AIWDeadArchiving = 1`.
4. `APP Safe Recovery` reached both QueueView AutoSheets reads, then stopped with `%AIWRecoveryResult = RECOVERY_QUEUE_READ_HOLD`.
5. A subsequent assumed-predicate repair repeated the same phone failure.
6. No destructive Sheet operation, profile activation, processing, sending, or normal Archive was proven in those failed recovery runs.
7. Root process failure: production predicates were built before measuring the exact phone AutoSheets output contract.

A diagnostic execution contract is required before a no-write QueueView measurement build. A production repair execution contract is forbidden until the real phone AutoSheets output contract is measured and frozen.

### Malformed Clean Integrated R2

Artifact: `AIW_DEADARCHIVE_CLEAN_INTEGRATED_CANDIDATE_R2.xml`

SHA256: `E74BA8E319E3D0F55E4F252CAAD3C5F84F09CDACDDEAB456F121E2E5DBCCAB0D`

Newest direct Sosa classification:

- `STATUS = HARD HOLD`
- `PHONE_IMPORT = FORBIDDEN`
- `REFERENCE_ONLY = YES`
- `INVALID_PARENT = TRUE`
- `PATCH_PARENT = FORBIDDEN`
- `REBUILD_FROM_LAST_PROVEN_BASELINE = REQUIRED`

This is a different artifact from the lock-compatibility R2. The lock R2 SHA must never be assigned to it. This exact SHA256-verified clean integrated R2 is required as a known-bad verifier regression fixture and remains forbidden as a patch parent.

### Preserved Integrated Requirements - Authorization Suspended

The prior restart analysis remains evidence:

- startup recovery holds on an active DeadArchive Boolean lock before Queue Cycle reaches Task 199;
- exact owned recovery may require a bounded Task 229 re-entry into Task 19;
- `RELEASE_BOOLEAN_FINALIZE` may set only Boolean lock `0` after exact phase, identity, destination, source-clear/readback, commit, and immediate revalidation proof with idle owner;
- recovery must never select new work, clear a foreign owner, or mutate on missing/inconsistent proof.

These are not an active production mutation allowlist. The unified protocol is present on current main. Only one contract-bound, isolated, no-write QueueView diagnostic is authorized before phone measurement; production repair construction remains forbidden until the measured plugin output contract is frozen in a later exact execution contract.

Closing sequence:

1. one canonical source-locked diagnostic execution contract against refreshed current main;
2. one isolated no-write QueueView output diagnostic using the exact Task 229 configuration;
3. independent exact-artifact audit and one bounded phone diagnostic run;
4. freeze the measured AutoSheets output contract;
5. only then issue the production repair contract and build from the resolved clean ancestor/parent;
6. independently audit the production repair and obtain a separate bounded phone decision.

## ISSUE_GLOBAL_BUILDER_VERIFIER_AND_ARTIFACT_PROOF_FAILURE

Status: `OPEN / WORKFLOW REPAIR ACTIVE / DIRECT SOSA FAILURE CLASSIFICATION`

The following failure classes are recorded from the newest direct Sosa instruction against the exact SHA256-verified clean integrated R2 artifact above. They are not represented as independently reproduced artifact findings in this documentation-only update:

- builder and verifier shared false assumptions;
- malformed integrated R2 control flow;
- invalid rejected-parent reuse;
- shallow presence/count verification substituted for behavior proof;
- abstract mock tests were detached from the finished XML;
- XML element-order renumbering corrupted numeric `actN` execution order;
- builder reports approved their own artifact;
- call graph and entry-to-side-effect coverage were incomplete;
- maintenance quiescence/concurrency was unproven;
- maintenance state could remain stuck after interruption;
- local filesystem paths were misrepresented as downloadable/uploaded links;
- repeated narrow repairs failed to consolidate the underlying root cause.

Material consequence:

- the clean integrated R2 is `HARD HOLD / DO NOT IMPORT`;
- no report or package from that artifact authorizes a phone run;
- no further patch may use it as a parent;
- the unified protocol and clean-baseline rebuild path are required.

Permanent prevention is consolidated in `AGENTS.md`:

- current-source lock and exact machine-readable contract;
- distinct artifact-lineage roles and invalid-parent prohibition;
- exact mutation allowlist and state-machine-first design;
- numeric Tasker control-flow/schema/branch validation;
- raw protected-byte and original-body preservation;
- separate builder, finished-artifact verifier, and structural scanner;
- complete call graph and requirement-to-proof traces;
- reproducible artifact-driven mutations and known-bad rejection;
- maintenance quiescence, ownership, cleanup, STOP/restart proof;
- proof-lane separation and phone boundary;
- verified upload identity and working HTTPS links only;
- first-fundamental-failure stop plus one consolidated return.

Completed workflow prerequisite:

- the unified protocol was independently audited and merged through PR #15 at merge SHA `83d14b31e5222da49de22763ada1dfbd12e0800f`.

Closing proof requires:
- next contract uses refreshed current-main and exact artifact identities;
- next verifier rejects the exact SHA256-verified clean integrated R2 and every other contract-required known-bad fixture;
- next candidate supplies reproducible finished-artifact proof;
- no builder-generated report self-approves;
- phone import remains separately approved.

## ISSUE_BRAIN_AND_ARCHIVE_CONTEXT_INTEGRATION_PENDING

Status: `OPEN / RELEASE HOLD / CONFIRMED INTEGRATION GAP`

Confirmed:

- current same-sender grouping supports up to four messages;
- no active AutoSheets path reads Brain;
- no active prompt path reads normal Archive history;
- `%BrainRules` and `%ConversationHistory` do not reach the active prompt;
- current prompt uses a hard-coded system prompt and current grouped message only.

Order: DeadArchive first, Brain/context second, final application-wide release audit third.

## Permanent Regression Rules

- Phone proof outranks static/model proof but applies only to its exact tested boundary.
- Exact finished bytes outrank builder intent and generated reports for implementation truth.
- Requirements/contracts remain acceptance truth; disagreement with bytes is `HARD HOLD`.
- Preserve Tasker numeric action order, encoding, action schemas, branch targets, and unauthorized bytes.
- Clear stale plugin output and require exact readback before dependent/destructive action.
- No plugin-dependent production patch may rely on inferred plugin output. When the exact behavior is not already phone-proven in the same configuration, first build and run one isolated diagnostic that captures raw outputs, array shapes, unset/blank/literal states, and completion markers.
- Prove exact recipient/thread/row/ID/sender/message/reply/status before Send.
- Never retry automatically after a possible Send click.
- DONE requires independent confirmation.
- Archive/DeadArchive requires exact copy/readback/uniqueness and safe exact source clear.
- Locks release only their verified owner exactly once; no owned leak or foreign release.
- STOP prevents new work and leaves profiles disabled.
- One lifecycle transition per cycle.
- Every runtime package requires independent application-wide exact-artifact verification.
- Passed sub-proofs advance to their permanent integration point; they do not create repeated packages.
- Private data and credentials never enter public GitHub.

## Source-Truth Cleanup Rule

Only these root files may be current authority:

1. `AGENTS.md`
2. `AIW_FULL_GOAL_EXECUTION_CONTRACT_CURRENT.md`
3. `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`
4. `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`

Other controller/tracker/matrix/bootstrap/handoff/status files must be deleted when wholly redundant or archived under `archive/non_authoritative/` with the required non-authoritative warning. Archived evidence cannot override these files.

## Protocol Review Boundary

`SOURCE_UPDATE_SELF_APPROVED = NO`
`CHATGPT_DIFF_AUDIT_REQUIRED = COMPLETE`
`MERGE_APPROVED = YES`
`PROTOCOL_PR = #15`
`PROTOCOL_MERGE_SHA = 83d14b31e5222da49de22763ada1dfbd12e0800f`
`GLOBAL_EXECUTION_PROTOCOL = ACTIVE / MERGED ON CURRENT MAIN`
`RUNTIME_BUILD = AUTHORIZED ONLY FOR ONE CONTRACT-BOUND NO-WRITE QUEUEVIEW DIAGNOSTIC`
`PRODUCTION_REPAIR_BUILD = FORBIDDEN PENDING PHONE-MEASURED AUTOSHEETS OUTPUT CONTRACT`
