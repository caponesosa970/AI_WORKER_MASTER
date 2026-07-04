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

