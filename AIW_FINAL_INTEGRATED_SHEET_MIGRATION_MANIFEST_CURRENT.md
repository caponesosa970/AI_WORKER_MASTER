# AIW Final Integrated Sheet Migration Manifest - Fixture-Safe Revision

Status: `PLAN ONLY / NOT APPLIED / HOLD FOR CONTROLLER ROW SELECTION`

Issue: `ISSUE_FINAL_VALIDATION_UNVERIFIED_FIXTURE_CLEANUP`

This public-safe manifest replaces the unsafe fixed-fixture section of the prior integrated migration manifest. It does not authorize or perform a Google Sheet change. All non-fixture schema, view, formula, backup, and verification requirements from the prior manifest remain active unless a later controller record changes them.

## Removed unsafe locations

These locations are prohibited and are not migration fixtures:

- `Sheet1` rows `144`, `145`, `146`, and `147`.
- `Archive` row `999`.
- `DeadArchive` row `999`.

No replacement row number is selected or guessed in this manifest.

## Current physical safety caps

The fixture contract rejects a configured maximum above these current public-safe caps:

| Layer | Current cap | Fixture protected range |
|---|---:|---|
| `Sheet1` | 980 | `A:Z` |
| `Archive` | 933 | `A:C` |
| `DeadArchive` | 972 | `A:A` |
| `OverflowInbox` | 986 | `A:N` |
| `IngressJournal` | 1001 | `A:N` |

The `IngressJournal` value is the migration/runtime bound. Its physical grid must be independently verified after the tab exists and before validation is armed.

## Dynamic fixture roles

The controller must select each row later using a fresh, read-only live Sheet inspection. Every selected row must physically exist and be blank across its full protected range.

| Role | Required layer | Row | Approved maximum | Protected range | Initial state |
|---|---|---|---|---|---|
| `HIST_ARCHIVE` | `Archive` | `CONTROLLER_SUPPLIED` | `CONTROLLER_VERIFIED` | `A:C` | `HISTORY` |
| `HIST_DEAD` | `DeadArchive` | `CONTROLLER_SUPPLIED` | `CONTROLLER_VERIFIED` | `A:A` | `HISTORY` |
| `G14C_REAL` | `Sheet1` | `CONTROLLER_SUPPLIED` | `CONTROLLER_VERIFIED` | `A:Z` | `NEW` |
| `G14C_RATE` | `Sheet1` | `CONTROLLER_SUPPLIED` | `CONTROLLER_VERIFIED` | `A:Z` | `NEW` |
| `G14C_TIMEOUT` | `Sheet1` | `CONTROLLER_SUPPLIED` | `CONTROLLER_VERIFIED` | `A:Z` | `NEW` |
| `G14C_QUOTA` | `Sheet1` | `CONTROLLER_SUPPLIED` | `CONTROLLER_VERIFIED` | `A:Z` | `NEW` |
| `G14C_LEGACY` | `Sheet1` | `CONTROLLER_SUPPLIED` | `CONTROLLER_VERIFIED` | `A:Z` | `ERROR_OPENAI_RETRY` |

## One-shot controller configuration

Before the final orchestrator can enter Phase 0, the controller must supply:

- `%AIWValidationRunID`
- `%AIWFXConfigVersion=FIXTURE_CONTRACT_V1`
- `%AIWFXAuthState=ARMED`
- `%AIWFXAuthRunID` equal to the current validation run ID
- a unique `%AIWFXAuthToken` matching the approved one-shot token format
- `%AIWFXAuthConsumedRun` blank for a new run
- `%AIWFXProtectedSheet1Rows`, including at least `144,145,146,147`
- `%AIWFXMainMax`, `%AIWFXOverflowMax`, and `%AIWFXJournalMax`
- `%AIWFXMainColumns=A:Z`
- `%AIWFXOverflowColumns=A:N`
- `%AIWFXJournalColumns=A:N`

Each role prefix below requires `Role`, `Layer`, `Row`, `Max`, `Columns`, `ID`, `Sender`, `Message`, and `Status` fields:

- `%AIWFXHistArchive...`
- `%AIWFXHistDead...`
- `%AIWFXG14CReal...`
- `%AIWFXG14CRate...`
- `%AIWFXG14CTimeout...`
- `%AIWFXG14CQuota...`
- `%AIWFXG14CLegacy...`

Every expected fixture ID, sender, and message must be unique and tied to `%AIWValidationRunID`. No runtime default or fallback exists.

## Required fresh row evidence

For every selected role, the controller audit must record:

1. Sheet name.
2. Physical row number.
3. Physical maximum row evidence.
4. Exact protected range read.
5. Every returned value.
6. Blank/nonblank classification.
7. Intended role.
8. Expected run-owned fixture identity.
9. Confirmation that the row is not a prior Gate record or production row.
10. Confirmation that no selected role conflicts with another role.

An unresolved output, plugin error, partial value, unexpected value, stale array, `#ERROR`, occupied cell, protected row, duplicate row, duplicate identity, or out-of-bounds row keeps migration on HOLD.

## Runtime setup and cleanup contract

- Task 268 verifies the complete contract before Phase 0.
- Contract verification reads every configured protected range and performs no Sheet write.
- Setup reads before writing and writes only a fully blank approved range.
- Setup performs one write attempt and exact readback; it never retries a possibly successful write.
- Cleanup reads before writing.
- Cleanup clears only a row that matches the current run, expected identity, role, layer, row, and permitted disposable state.
- Already-blank cleanup returns `FIXTURE_ALREADY_CLEAN` with no write.
- Wrong identity, wrong run, occupied data, partial data, plugin error, unresolved output, or ambiguous ownership returns HOLD with no destructive write.
- Cleanup performs exact blank readback.
- Phase 7 consumes the one-shot authorization only after fixture cleanup and proof-ledger success.

## Migration decision

No fixture rows are currently selected. Sheet migration, Tasker import, the final orchestrator, PR merge, Gate 14 closure, and production release remain HOLD.
