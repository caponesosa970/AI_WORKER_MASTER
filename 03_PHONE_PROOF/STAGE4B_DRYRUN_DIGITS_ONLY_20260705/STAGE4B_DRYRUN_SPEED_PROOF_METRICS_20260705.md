# Stage4B Dry-Run Speed And Proof Metrics

Date: 2026-07-05

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT

## Evidence Files

| file | SHA256 | note |
|---|---|---|
| `AIW_STAGE4B_DRYRUN_PROGRESS_SPEED_LOG_20260705.md` | `DB86C604924FD629379F3734D89A8D835FC505F08F607627DD325FD9645DA82E` | Supplied speed/proof summary. |
| `AIW_CODEX_STAGE4B_DRYRUN_SYNC_AND_NEXT_PATCH_ORDER_20260705.txt` | `B316B9C21A906EA36C6F7DB0E7062AA2DC387D7946242D1E310784661849A6C3` | Codex ledger-sync order. |
| `runlog.txt` | `EB4937BC8EF57CF21EF0E96D9B8676B2A33D171A980EC3F9D799526608E8197E` | Raw file not found locally by exact name during this sync; classified from supplied proof summary. |
| `runlog (1).txt` | `59811D4A3F731A4693C540CB512CFC7C39E46366A15D88058EA6A195017D053C` | Raw file not found locally by exact name during this sync; classified from supplied proof summary. |

## Run 1: Formatted Number

- Search key: `+1(910) 447-7850`
- Result: FAILED / DATA FORMAT CONTACT_PICK FAILURE
- Task time: 39 seconds
- UI-start-to-stop: 37 seconds
- Contact-pick timeout: about 15 seconds
- Safety result: `SSSentOne=0`, `SS Fail UI Dirty Stop` ran, lock released.
- Classification: FAILED as data-format evidence, not XML/import failure.

## Run 2: Digits-Only Number

- Search key: `9104477850`
- Result: LOCKED for Stage4B dry-run contact-pick/no-send guard only.
- Task time: 25 seconds
- UI-start-to-pass: 15 seconds
- Task-start-to-lock-release: 20 seconds
- Passed markers: `SEARCH_ICON`, `SEARCH_FIELD`, `CONTACT_PICK_ATTEMPT`, `DRYRUN_CONTACT_PICK_PASS`, `SAFE_SEND_DRYRUN_PASS`.
- Safety result: `SSSentOne=0`, `SSFailed=0`, lock released, task ExitOK.

## Not Proven

- Message paste.
- Send button.
- Real send.
- Controlled one-send.
- Timer/live route.
- Archive/deadarchive/compactor/TT5.
- Multi-send/capacity.

## Candidate Patch Proposal

Patch only `SS Safe Send Dry-Run` search-key normalization after ChatGPT audit.

Expected retest:

- Column B: `+1(910) 447-7850`
- Column I: `9104477850`
- Selected search key: `9104477850`
- Task: `SS Safe Send Dry-Run`
- Expected result: dry-run contact-pick pass with no paste and no send.
