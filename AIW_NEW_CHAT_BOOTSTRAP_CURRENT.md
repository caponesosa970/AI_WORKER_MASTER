# AI Worker New Chat Bootstrap - Current

Status: REQUIRED STARTUP ORDER FOR THE NEXT CODEX CHAT
Updated: 2026-07-16

## Instruction-State Gate

Before any source edit, the next chat must confirm:

```text
PROJECT_INSTRUCTIONS_LOADED = YES
GROUP_C2_SCOPE_ACTIVE = NO
FULL_INTEGRATED_SCOPE_AUTHORIZED = YES
```

If any value is false or cannot be proven, return HOLD without editing source.

## Repository Read Order

1. Fetch current `origin/main`.
2. Read from main:
   - `AIW_CONTROLLER_BOOTSTRAP_CURRENT.md`
   - `AIW_FULL_GOAL_EXECUTION_CONTRACT_CURRENT.md`
   - `AIW_LOCKED_FACTS_CURRENT.md`
   - `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`
   - `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`
   - `AIW_CLAIM_TO_PROOF_MATRIX_CURRENT.md`
   - `AGENTS.md`
   - `AIW_MANDATORY_BUILD_PREFLIGHT.md`
3. Fetch PR #9 and record its exact remote head.
4. Verify the PR head contains the commit whose subject is `Synchronize Gate 14 repository handoff` and that its ancestry contains pre-sync head `26b2bea5f464c01cbc6e9a0d49edc2dea32436ea`.
5. Read the complete current PR branch, including every committed Gate 14 report.
6. Read:
   - `AIW_FINAL_TONIGHT_HANDOFF_CURRENT.md`
   - `AIW_FINAL_INTEGRATED_VALIDATION_PLAN_CURRENT.md`
   - `AIW_GATE14_CHECKPOINT_TRACKER_CURRENT.md`
7. Reconcile main, PR branch, private manifest, and newest direct Sosa instruction. Newer direct proof controls when older main text is stale.

The exact handoff synchronization SHA is Git metadata and is returned by the synchronization task. It is verified from the remote PR head rather than embedded inside the commit whose own content determines that SHA.

## Private Source Verification

Pull the current private input manifest first. Verify every required file by byte size and SHA256 before editing.

Required private runtime facts:

- D3A XML SHA256: `880CC569185A9FFF45703EC77E71D6260A88474B0F63ECDE6B31E0A11CFF090A`.
- Direct Gate 14D2 base SHA256: `3851E073BE042F80068E52CF7E3D410ED3D0EBA8A63C5F4C10108532912FE0EA`.
- D3A topology: 99 tasks, 4 disabled profiles, 1 scene.

Use only the D3A XML identified by the current private manifest as the runtime base.

Never use a file marked:

- `SUPERSEDED_DO_NOT_USE`
- `SUPERSEDED_REFERENCE_ONLY`
- `DO_NOT_IMPORT`
- `DO_NOT_PHONE_TEST`

R1, R2, and R3 are design history only.

## Locked Proof Boundary

- Preserve Gates 1 through 13.
- Preserve phone-proven Gate 14 inventory, processing, ordering, later-repeat, and duplicate-ID behavior.
- Do not rerun a 50-call capacity test.
- Do not change phone-proven AutoInput targets without exact controller authorization and source proof.
- Do not claim phone proof, phone-import approval, Gate 14 closure, or release.

## Current Assignment

Build one integrated candidate with modular helpers and one consolidated validation orchestrator. Do not return another narrow D3A, D3B, or D3C phone package.

The return must include:

- final private XML, phone-import ZIP, and SHA sidecar;
- full private proof/validation packet;
- exact Drive output manifest and visible output links;
- exact names, sizes, and hashes;
- ZIP byte-equality proof;
- changed task/action/property inventory;
- call graph and variable/lock map;
- plugin settings audits;
- state model, fault injection, randomized concurrency, and mutation results;
- Sheet migration manifest or `NONE`;
- commit SHA and PR state;
- privacy and private-file tracking proof;
- unsupported claims and exact phone-proof limitations.

## Hard HOLD Conditions

Return HOLD before runtime edits when:

- current main or PR #9 cannot be read;
- the handoff commit is absent;
- required private source is missing or hash-mismatched;
- source instructions contradict each other without a newer controlling decision;
- a superseded package would be used as runtime base;
- a phone-proven module would be changed without exact source preservation proof;
- private data would enter Git;
- the connected validation assignment cannot be completed safely.

## Current Status

- Gates 1-13: LOCKED.
- Main-gate count: `13/14 locked = 93%`.
- Detailed remaining tracker: 40 total, 25 phone/runtime, 15 non-phone.
- D3A: admission-only candidate, no phone proof, not final release.
- Phone import: HOLD.
- Sheet mutation by Codex: PROHIBITED.
- PR merge: BLOCKED.
- Gate 14 closure and release: BLOCKED.
