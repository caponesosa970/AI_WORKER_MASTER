# AI Worker Failure and Regression Ledger

Status: CURRENT ACTIVE RELEASE-CAPABILITY HOLDS AND PERMANENT REGRESSIONS

Static audit cannot close a phone/runtime issue by itself.

## ISSUE_DEADARCHIVE_REPAIR_REQUIRED

Status: `OPEN / RELEASE HOLD / R3 LOCK SUB-PROOF PHONE-PROVEN / TASK 229 RECOVERY AND RELEASE_BOOLEAN_FINALIZE AUTHORIZED`

Classification: `REPAIR_REQUIRED`

Confirmed:
- application-wide DeadArchive audit completed;
- existing implementation requires repair;
- Boolean compatibility lock must remain `%AIWDeadArchiving = 0/1`;
- owner token must remain separate in `%AIWDeadArchiveOwner`;
- permanent foreign-reset guards exist in Tasks 34, 73, 74, and 147;
- R3 phone proof passed the lock contract;
- Task 334 is locked proof evidence and must remain byte-identical;
- no additional lock-only package is authorized.

R2 rejected:
- artifact SHA256 `31A871EB97C923360A54812A04A5A78BC67477DEAD54729F237E75A002340CD6`;
- phone run `DAL-1784436735760`;
- terminal `HOLD_PROFILE_SOURCE_PRE`;
- `%PENABLED` and `%PACTIVE` rendered unresolved;
- safe zero-mutation outcome;
- R2 must not be rerun.

R3 phone-proven:
- artifact SHA256 `0DBA8B521C33FDECD62C3877A44A860EF9DA8125E0F604FE86782880E7FDD10C`;
- accepted run `DAL-1784441447757`;
- result `PASS`;
- terminal `DEADARCHIVE_LOCK_CONTRACT_PASS`;
- arm consumed `1` to `0`;
- Boolean lock compatibility and separate owner confirmed;
- all four permanent resetters blocked foreign or invalid resets;
- owner release count exactly `1`;
- protected consumers unchanged and globals restored;
- zero workbook, profile-enable, live-enable, and manual-cleanup activity;
- final complete `1` and normal Tasker exit.

Integrated-build blocker:
- restart reconciliation is mandatory at every persistent boundary;
- current startup recovery holds on an active DeadArchive Boolean lock before Queue Cycle can reach Task 199;
- the prior Tasks 18, 19, and 199 scope had no reachable post-restart entry capable of resuming the exact owned transaction;
- accepting a blank/manual caller would not prove the existing owner token and would violate foreign-owner protection;
- the minimum Task 229 recovery entry is authorized only when the Boolean lock is active, the existing owner is verified, and persistent transaction state identifies the same owned transaction;
- Task 229 may pass that exact owner to Task 19 in a dedicated recovery mode, but may not start new work, clear a foreign owner, or alter unrelated recovery behavior;
- the additional `RELEASE_BOOLEAN_FINALIZE` entry is authorized only for Boolean lock `1`, idle owner, phase `RELEASE_BOOLEAN_INTENT`, complete matching transaction identity, proven exact/unique or idempotent destination, proven source reread and exact A:I clear/readback, matching commit state, no owner-controlled work, and immediate commit revalidation;
- that finalizer may set only the Boolean lock to `0`; it may not clear an owner, select a row, start or resume transaction work, mutate a Sheet, accept another phase, or mutate on missing or inconsistent proof;
- authorized runtime changes remain Tasks 18, 19, 199, and only the minimum Task 229 recovery and `RELEASE_BOOLEAN_FINALIZE` entries; no unrelated runtime changes are authorized.

Closing sequence:
1. R3 exact artifact audit and bounded phone run: complete;
2. minimum Task 229 recovery and `RELEASE_BOOLEAN_FINALIZE` authorization: granted;
3. one complete integrated DeadArchive transaction build;
4. application-wide integrity verification;
5. bounded integrated phone proof;
6. independent controller decision.

Prevention:
- no more lock-only package after R3;
- no local PASS may be described as an application PASS;
- every temporary proof must name and immediately advance to its permanent integration point.

## ISSUE_APPLICATION_WIDE_VERIFICATION_GAP

Status: `OPEN / WORKFLOW REPAIR ACTIVE`

Historical failure:
Repairs were sometimes locally scoped correctly for diagnosis but were not consistently surrounded by a mandatory whole-application verifier and immediate integration requirement. This allowed repeated proof packages without closing the permanent subsystem.

Permanent correction:
Every runtime candidate must run the AI Worker Application Integrity Verifier against the exact phone-proven baseline and report:
- source lock;
- complete mutation map;
- protected-byte comparison;
- complete caller/callee graph;
- runtime contract checks;
- STOP/restart/recovery impact;
- forbidden-path reachability;
- scenario matrix;
- exact phone-proof boundary;
- permanent integration point;
- application-wide regression result.

Closing proof:
- current GitHub source truth contains the rule;
- obsolete contradictory controller files are removed or clearly archived as non-authoritative;
- the next runtime artifact includes an integrity return;
- no second package is produced for a passed sub-proof.

## ISSUE_BRAIN_AND_ARCHIVE_CONTEXT_INTEGRATION_PENDING

Status: `OPEN / RELEASE HOLD / CONFIRMED INTEGRATION GAP`

Confirmed:
- current same-sender grouping supports up to four messages;
- no active AutoSheets path reads Brain;
- no active prompt path reads normal Archive history;
- `%BrainRules` and `%ConversationHistory` do not reach the active prompt;
- current prompt uses a hard-coded system prompt and current grouped message only.

Order:
DeadArchive first, Brain/context second, final application-wide release audit third.

## Permanent Regression Rules

- Phone proof supersedes static audit.
- Generated reports cannot prove themselves.
- Preserve Tasker encoding and unchanged bytes.
- Isolate external plugin output contracts with phone proof.
- Clear stale plugin output before every use.
- Prove exact recipient/thread before Send.
- Prove row/ID/sender/message/reply/status binding before Send.
- Never automatically retry after a possible Send click.
- DONE requires independent confirmation.
- Archive requires exact copy/readback/uniqueness/safe source clear.
- Every lock releases only its owner exactly once.
- STOP prevents new work and leaves profiles disabled.
- One lifecycle transition per cycle.
- Gates 1-14 remain locked.
- Every runtime package requires application-wide integrity verification.
- After a sub-proof PASS, move directly to permanent integrated implementation.

## Source-Truth Cleanup Rule

Only these root files may be current authority:
1. `AGENTS.md`
2. `AIW_FULL_GOAL_EXECUTION_CONTRACT_CURRENT.md`
3. `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`
4. `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`

Any other controller, tracker, matrix, bootstrap, handoff, current-state, or release-status file must be:
- deleted when obsolete and redundant; or
- moved under `archive/non_authoritative/` with a header stating `NON-AUTHORITATIVE HISTORICAL EVIDENCE`.

No archived file may contain `CURRENT`, `ACTIVE`, `SOURCE TRUTH`, or instructions that can override the four root files.
