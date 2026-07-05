# AI Worker Phone Proof Sequence

Updated: 2026-07-05

## Status

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

## Proof Rules

- Use Moto Razr 2024 Tasker/TextNow proof for runtime claims.
- Run one layer at a time.
- Export runlog after each proof.
- Do not skip from dry-run to timer/live.
- Do not enable archive/deadarchive/compactor/TT5 during send proof.

## Sequence

1. Group B2 Send UI Completion Dry-Run.
   - Run only `SS Safe Send Dry-Run`.
   - Prove search-key normalization, contact pick, message box detection, dry-run paste if included, `SEND=NO`, send button untouched.

2. Group C Controlled One-Send.
   - Use one approved row and one approved recipient.
   - Paste exact reply.
   - Press send once.
   - Verify one send only.
   - Mark DONE only after proof.

3. Group D Live Controller / Timer Gates.
   - Test `APP Start AI Worker`, `APP Run Tick Once`, `AIW AUTO LIVE START V1`, `AIW AUTO LIVE TICK V1`, and timer profile gates.
   - Prove holds and Safe Mode boundaries.

4. Group E Maintenance / Recovery.
   - Test archive, deadarchive, compactor, TT5, cleanup, proof logging, and fail-closed behavior only after core live path safety.

5. Group F Capacity / Production.
   - Test 50-contact readiness, queue pressure, one-send-per-cycle, quota/backoff, and long-run behavior last.

## Required Evidence Each Time

- Fresh runlog.
- SHA256 for runlog.
- Audit report.
- Classification.
- Exact next step.
- No secrets printed.
