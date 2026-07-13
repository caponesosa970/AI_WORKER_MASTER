AI WORKER / ALL PROJECTS FULL-CAPABILITY OPERATING INSTRUCTION

Operate from this folder as the main workspace:

AI_WORKER_MASTER/
  00_LOCKED_SOURCE/
  01_CANDIDATE_PATCHES/
  02_TEST_LOGS/
  03_PHONE_PROOF/
  04_RELEASE_PACKAGES/
  docs/
  scripts/
  AGENTS.md

Do not work from random downloads when this master folder contains the needed source, candidate, logs, proof, package, docs, or scripts.

Source rules:
- LOCKED source lives in 00_LOCKED_SOURCE.
- CANDIDATE patches and generated XML live in 01_CANDIDATE_PATCHES.
- Static audits, validation reports, SHA256 inventories, HOLD lists, and promotion reports live in 02_TEST_LOGS.
- Phone screenshots, runlogs, and real device proof live in 03_PHONE_PROOF.
- Release ZIPs live in 04_RELEASE_PACKAGES.
- Reference docs live in docs.
- Build and audit scripts live in scripts.

Status rules:
- Never replace locked source until a new build passes phone proof.
- Never promote an output without independent audit.
- Never build from a failed patch unless explicitly using it only as reference.
- Preserve Tasker XML format, plugin bundles, sheet IDs, task names, variables, profile names, scene names, and project structure unless the patch specifically requires a change.
- Keep Build100 as CANDIDATE / HOLD FOR PHONE PROOF until Moto Razr 2024 phone proof passes.

Required proof before release:
- XML parse pass.
- SHA256 recorded.
- Task/action references checked.
- Scene links checked.
- Profile links checked.
- Perform Task references checked.
- Dashboard clickTask references checked.
- Dangerous live paths checked.
- Runlog or phone proof checked when runtime behavior is claimed.

Safety priorities:
1. No wrong-recipient sends.
2. No stale replies.
3. No duplicate sends.
4. No ghost rows.
5. No uncontrolled live/autonomous activation.
6. No Archive/Compactor/DeadArchive live use until proven.
7. No multi-send unless explicitly proven safe.
8. One-send rule remains locked unless a tested replacement is approved.
9. Safe Mode, holds, locks, watchdogs, and stop paths must be verified, not assumed.

Default final status vocabulary:
- LOCKED
- CANDIDATE
- HOLD
- HARD HOLD
- FAILED

## Mandatory Build Accountability Gate

This gate is required before, during, and after every AI Worker task. It applies to audits, repository syncs, runtime packages, phone-test requests, and release review.

### A. Pre-Build Accountability

- Read `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`.
- Read `AIW_BUILD_ACCOUNTABILITY_LEDGER_CURRENT.md`.
- Read `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`.
- Read `AIW_CLAIM_TO_PROOF_MATRIX_CURRENT.md`.
- Read `AIW_MANDATORY_BUILD_PREFLIGHT.md`.
- Read all relevant bug history, logs, phone-proof summaries, and prior package reports for the current gate.
- List the exact prior failures relevant to the task.
- Explain how the new work prevents each regression.
- Identify exact source truth and source SHA256.
- Stop if source proof is missing, ambiguous, or contradicted by phone proof.

### B. During-Build Accountability

- Keep an exact changed-file list.
- Keep an exact changed-task/action list.
- Record every command that materially changes output.
- Record source and output SHA values.
- Record every deviation from the approved task.
- Do not silently repair unrelated issues.
- Do not invent AutoInput targets.
- Do not convert an unsupported claim into build logic.

### C. Post-Build Accountability

- Independently re-read the output.
- Do not rely only on the script that generated the output.
- Compare required fields semantically, not only by byte/string equality.
- Produce a claim-to-proof mapping.
- Run all relevant historical regression checks.
- Mark unsupported claims as HOLD.
- A generated CSV or report cannot prove its own correctness.

### D. Phone-Proof Accountability

- Codex must never claim phone proof.
- Every phone result must be reconciled against the build claims.
- Phone failure immediately reopens or creates an issue in `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`.
- Phone proof supersedes static reports, XML parse, generated CSV files, and package claims.

### E. Controller Accountability

- ChatGPT must inspect direct source evidence before phone import approval.
- ChatGPT must not approve from Codex summaries alone.
- ChatGPT must identify what it personally verified.
- ChatGPT must record its own missed control when a preventable failure reaches the phone.

### F. Release Accountability

- No merge, release, tracker increase, or gate lock without complete claim-to-proof evidence.
- Every release must include open-issue scan and regression ledger review.
- Send, DONE, Archive, live, capacity, and release remain blocked unless explicitly approved by ChatGPT and backed by phone proof.

### AutoInput Preservation Claim Rule

A build cannot say `PRESERVED` merely because fields were copied by a script.

For AutoInput preservation, evidence must show source and output values for:

- Type
- Value
- Action
- Field Selection Type
- resource ID
- text target
- point
- nearby text
- timeout
- Continue Task After Error
- Structure Output
- accessibility setting
- plugin bundle values
- relevant variable outputs
- wait actions
- error checks
- failure routing

The proof must identify the exact XML action in both files and must be validated by a second independent parser/check.

