# AIW Build100 Stage4A Phone Rerun Checklist

1. Import/apply the patched full Tasker XML.
2. In Tasker, run exactly `QC R4A APP Tick No-Work Proof`.
3. Do not run live start, timer, trigger, send test, archive, deadarchive, compactor, or TT5.
4. Export the Tasker runlog.
5. Required pass evidence:
   - `QC R4A APP Tick No-Work Proof = ExitOK`
   - `APP Reset Locks = ExitOK`
   - `QC Selection Hardening Audit = ExitOK`
   - `FINAL Queue Cycle = ExitOK` or guarded no-send stop
   - `FINAL Send Sheet = 0`
   - `AIW SEND 1 = 0`
   - `timer/live/archive/deadarchive/compactor/TT5 = 0`
6. Upload the fresh runlog for audit.