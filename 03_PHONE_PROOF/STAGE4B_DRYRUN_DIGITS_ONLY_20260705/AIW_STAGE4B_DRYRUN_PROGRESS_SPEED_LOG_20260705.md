# AI Worker Build100 Stage4B Dry-Run Proof Progress + Speed Log

Date: 2026-07-05

## Final classification

CANDIDATE / HOLD FOR LEDGER SYNC AND NEXT CONTROLLED GATE

## Key result

Run 1 failed because the search key was formatted as `+1(910) 447-7850`.
Run 2 passed when the search key was changed to digits-only: `9104477850`.

The second run did not paste a message. That was planned for this gate.
This gate is a safe dry-run contact-pick proof, not a message-paste or send proof.

## Source files

| File | SHA256 | Result |
|---|---:|---|
| runlog.txt | EB4937BC8EF57CF21EF0E96D9B8676B2A33D171A980EC3F9D799526608E8197E | FAILED at CONTACT_PICK using formatted number |
| runlog (1).txt | 59811D4A3F731A4693C540CB512CFC7C39E46366A15D88058EA6A195017D053C | PASS using digits-only number |

## Speed log

| Metric | Run 1 formatted number failure | Run 2 digits-only pass |
|---|---:|---:|
| Task start | 18:46:31 | 18:50:51 |
| Task end | 18:47:10 | 18:51:16 |
| Total task time | 39 sec | 25 sec |
| READY row found | 1 sec after task start | 1 sec after task start |
| UI start | 18:46:33 | 18:50:54 |
| UI start to final result | 37 sec to fail/stop | 15 sec to dry-run pass |
| Search icon step | 18:46:41, action error but continued | 18:50:58, OK |
| Search field step | 18:46:45, OK | 18:51:00, OK |
| Keyboard/search submit | 18:46:51, OK | 18:51:07, OK |
| Contact pick attempt | 18:46:54, failed after timeout | 18:51:09, OK |
| Lock release | 18:47:10 | 18:51:11 |
| Result | SEND_UI_DIRTY_STOP | SAFE_SEND_DRYRUN_PASS |

## Locked from Run 2

- `SS Safe Send Dry-Run` found exactly one `READY_TO_SEND` row.
- Search key `9104477850` was used.
- `SEARCH_ICON` action passed.
- `SEARCH_FIELD` action passed.
- `CONTACT_PICK_ATTEMPT` action passed.
- `SSResult` became `DRYRUN_CONTACT_PICK_PASS`.
- `SSSentOne=0`.
- `SSFailed=0`.
- `AIWProofResult=PASS`.
- `AIWProofError=NONE`.
- `SS Lock Release HARD` ran and exited OK.
- `SS Safe Send Dry-Run` exited OK.

## Not proven by this run

- Message box paste.
- Send button.
- Real send.
- Controlled one-send.
- Timer/live send.
- Archive/deadarchive/compactor/TT5.
- Multi-send/capacity.

## Important synchronization rule

Any build layer that was already tested and proven stays promoted into the working final build **only when the proof is tied to the source chain and the relevant logic is unchanged**.

That means:
- Do not retest proven frozen logic unless source changed or proof is missing.
- Do not replace locked source with a candidate patch until the candidate passes required proof.
- Old proven send/paste work must remain in the ledger as carried/historical proof until the exact old evidence file is connected.

## Current progress visual

```
SOURCE / LEDGER SYNC          [███████░░░] 70%  Candidate ledger exists; needs sync with these logs
XML STATIC / IMPORT           [██████████] 100% Static/import-safe package accepted
NO_READY SAFE STOP            [██████████] 100% Locked
READY ROW PREFLIGHT           [██████████] 100% Locked for row 68
SEARCH_ICON                   [██████████] 100% Locked in digits-only run
SEARCH_FIELD                  [██████████] 100% Locked in digits-only run
CONTACT_PICK DRY-RUN          [██████████] 100% Locked in digits-only run
NO-SEND DRY-RUN GUARD         [██████████] 100% Locked, SSSentOne=0
MESSAGE BOX / PASTE           [░░░░░░░░░░] 0%   Not part of this dry-run
CONTROLLED ONE-SEND           [░░░░░░░░░░] 0%   HOLD
TIMER / LIVE LOOP             [░░░░░░░░░░] 0%   HOLD
ARCHIVE / DEADARCHIVE / TT5   [░░░░░░░░░░] 0%   HOLD
CAPACITY / MULTI-SEND         [░░░░░░░░░░] 0%   HOLD
```

## Candidate bug from Run 1

The system searched `+1(910) 447-7850` even though the ticker backup was `9104477850`.
TextNow did not resolve the formatted number.
The digits-only number resolved and passed.

Candidate fix:
Normalize phone-like search keys to digits-only for `SS Safe Send Dry-Run`, then later carry the same proven normalization into the real send path only after dry-run proof.

## Recommended next action

1. Sync ledgers with both logs and speed metrics.
2. Do not patch real send yet.
3. Safe grouped patch candidate:
   - search-key normalization inside `SS Safe Send Dry-Run`;
   - speed/proof marker logging;
   - ledger update.
4. Re-test formatted-number row after normalization:
   - B = `+1(910) 447-7850`
   - I = `9104477850`
   - expected search key used = `9104477850`
   - expected result = dry-run pass.
