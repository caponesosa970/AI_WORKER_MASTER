# AI Worker Frozen Logic Register

Updated: 2026-07-05

Frozen means do not patch unless a future approved task directly touches that layer and gives a specific reason.

## Frozen Layer-Level Logic

| layer | status | frozen area | proof source | reason |
|---|---|---|---|---|
| Stage3A closeout | LOCKED layer | `AIW AUTO LIVE STOP V1`, `APP Safe Mode ON`, `APP Reset Locks`, `APP Status Snapshot Simple` closeout route | `CHATGPT_STAGE3A_FINAL_SAFE_STATE_CLOSEOUT_AUDIT_RESULT_20260705.md` | ChatGPT marked Stage3A closeout pass and locked for closeout layer only. |
| Stage4A process-only | LOCKED layer | `QC R4A APP Tick No-Work Proof`, no-work guard, `APP Run Tick Once`, guarded `FINAL Queue Cycle` no-send behavior | `AIW_STAGE4A_PROCESS_ONLY_RUNLOG_AUDIT_20260705_043750.md` | Runlog audit passed with send/timer/live/archive/TT5 paths at 0. |
| Stage4B no-ready hold | LOCKED layer | `SS Safe Send Dry-Run` no-ready hold/stop behavior | `AIW_STAGE4B_SEND_DRYRUN_RUNLOG_AUDIT_20260705_065955.md` | Phone runlog proves no-ready dry-run hold only. |
| Stage4B digits-only dry-run contact pick | LOCKED layer | `SS Safe Send Dry-Run` ready-row preflight, digits-only `SEARCH_ICON`, `SEARCH_FIELD`, `CONTACT_PICK_ATTEMPT`, no-send guard | `AIW_STAGE4B_DRYRUN_PROGRESS_SPEED_LOG_20260705.md` plus raw runlog SHA recorded in `PROOF_LEDGER.md` | Phone runlog summary proves digits-only search key passed contact-pick dry-run with `SSSentOne=0`; does not prove paste/send. |
| Current static XML structure | LOCKED static layer | Task/profile/scene counts, refs, duplicate IDs/names, block-safe current import-safe XML | `AIW_BUILD100_GROUP_B_SEARCH_ICON_IMPORT_SAFE_STATIC_AUDIT_20260705.md` | Static checks passed; does not prove phone import/runtime. |

## Do Not Touch During Group B2

- `FINAL Send Sheet`
- `SS Controlled One-Row Send Proof`
- `AIW SEND 1`
- send button
- DONE marking
- `APP Start AI Worker`
- timer/live/autonomous routes
- archive/deadarchive/compactor/TT5
- multi-send caps

## Allowed Group B2 Patch Area After ChatGPT Audit

- `SS Safe Send Dry-Run`
- search-key normalization before TextNow search
- message box detection in dry-run only
- dry-run reply paste proof marker, with stop before send button
- selected search-key proof marker
- speed timestamps for search/open/contact-pick/message-box/paste stages
- fail-closed proof markers
- no-send dry-run proof markers

## Synchronization Rule

Any build layer already tested and proven stays promoted into the working final build when proof exists, the source chain is known, relevant logic is unchanged, and the new patch did not replace that layer.

Do not retest or replace frozen working logic unless source changed or proof is missing.

## Frozen Until Later Proof

- One-send rule stays at one send.
- Timer/live loop stays disabled/held.
- Archive, DeadArchive, Compactor, Heavy Cleanup, and TT5 stay held.
- 50-contact/capacity readiness stays held until send dry-run and controlled one-send pass first.
