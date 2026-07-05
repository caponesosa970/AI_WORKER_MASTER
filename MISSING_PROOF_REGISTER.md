# AI Worker Missing Proof Register

Updated: 2026-07-05

If an item has no exact file, it remains `HARD HOLD`. Do not replace missing proof with memory.

## Exact Named Files Missing From Repo

| missing_id | classification | exact missing file | why it matters |
|---|---|---|---|
| MISS-001 | HARD HOLD | `AI_Worker_Handoff_Current_2026-05-19.txt` | Old project handoff reference requested by ledger seed. |
| MISS-002 | HARD HOLD | `OLD_AI_WORKER_CHAT_REFERENCE.txt` | Old chat reference requested by ledger seed. |
| MISS-003 | HARD HOLD | `runlog (5).txt` | Old runlog requested by ledger seed. |
| MISS-004 | HARD HOLD | `runlog (16).txt` | Old runlog requested by ledger seed. |
| MISS-005 | HARD HOLD | `AIW_ERROR_PROTECTION_PRE_RESPONSE_LOCK_V1.txt` | Old error protection reference requested by ledger seed. |

## Historical Proof Classes Missing

| missing_id | classification | exact missing proof needed | current decision |
|---|---|---|---|
| MISS-HIST-001 | HARD HOLD | old full build plan before Codex | Historical context cannot be locked. |
| MISS-HIST-002 | HARD HOLD | old proof tracker / master project tracker | Historical LOCKED/CANDIDATE/HOLD/FAILED state cannot be carried forward. |
| MISS-HIST-003 | HARD HOLD | old Simple logging runlog/screenshot | Simple logging remains historical only. |
| MISS-HIST-004 | HARD HOLD | old Process Sheet runlog/screenshot | Process Sheet remains historical only. |
| MISS-HIST-005 | HARD HOLD | old Send Sheet / manual TextNow send runlog/screenshot | Manual send movement remains historical only. |
| MISS-HIST-006 | HARD HOLD | old TextNow search/open/type/send proof screenshot/runlog | TextNow UI behavior must be reproven or restored. |
| MISS-HIST-007 | HARD HOLD | old double-tap/search-icon proof notes/screenshots | Search-icon/double-tap behavior remains untrusted without file proof. |
| MISS-HIST-008 | HARD HOLD | old AI Worker Tick proof runlog | Tick proof remains historical only. |
| MISS-HIST-009 | HARD HOLD | old Time Profile proof runlog/screenshot | Timer profile remains HOLD. |
| MISS-HIST-010 | HARD HOLD | old Archive manual copy+clear proof files | Archive remains HOLD. |
| MISS-HIST-011 | HARD HOLD | old dashboard/P81/P82 proof screenshots/reports | Current Stage2 dashboard proof exists, but older P81/P82 proof chain is not restored. |
| MISS-HIST-012 | HARD HOLD | old bottom Send self-loop OFF proof | Self-loop proof cannot be locked from current files. |
| MISS-HIST-013 | HARD HOLD | old call notification filter proof | Filter proof cannot be locked from current files. |
| MISS-HIST-014 | HARD HOLD | old duplicate protection proof | Duplicate protection remains partial/static or historical only. |
| MISS-HIST-015 | HARD HOLD | old JSON guard / Structure Output OFF proof for each old package | Current package has `json:true` 0 and `<se>true</se>` 0, but older packages are not proven. |

## Current Missing Proof

- Active blocker: ChatGPT audit of the subsystem completion package and approval for Group B2.
- Tasker import is user-reported clean because `SS Safe Send Dry-Run` ran afterward. If screenshot-level import proof is required, classify that screenshot as HOLD, not HARD HOLD.
- Raw local copies of `runlog.txt` and `runlog (1).txt`; current ledger has the supplied SHA values and speed/proof summary, but exact raw files were not found locally by exact name during this sync.
- Formatted-number normalization proof using B=`+1(910) 447-7850` and I=`9104477850`.
- Group B2 message-box detection proof.
- Group B2 dry-run paste marker proof if ChatGPT approves paste in dry-run.
- Proof that `button_send` remains untouched during Group B2.
- Proof that `FINAL Send Sheet`, `SS Controlled One-Row Send Proof`, `AIW SEND 1`, timer/live/archive/deadarchive/compactor/TT5 remain at 0 during Group B2.
