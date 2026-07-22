# Test Lane - DeadArchive

Lane ID: `TEST_DEADARCHIVE`

Classification: `ISOLATED / DEFERRED / NON-RELEASE-BLOCKING`

Production authorization: `NO`

## Product decision

DeadArchive does not block completion of the final product path. Its work remains isolated so useful evidence can accumulate without changing or delaying Main.

## Current boundaries

- Automatic DeadArchive runtime: `DEFERRED`.
- DeadArchive recovery: `BLOCKED`.
- Cleanup: `MANUAL ONLY`.
- Gates 1-14: protected.
- Main runtime parent: may not be changed from this lane.
- Rejected artifacts: evidence only and forbidden as parents.
- Production, profiles, live mode, TextNow, OpenAI, Send, normal Archive, and unrelated Sheet writes: forbidden.

## Evidence allowed

- Safe artifact filename and SHA256.
- Exact task/action identity without private payloads.
- Static audit result.
- Sanitized phone-result summary.
- Sanitized runlog findings.
- Verified failure and regression facts.
- Promotion recommendation.

## Promotion rule

DeadArchive evidence may become `LANE_LOCKED` after exact verification. It enters Main only after an explicit later product decision, independent artifact audit, required phone proof, and `PROMOTED_TO_MAIN` record.