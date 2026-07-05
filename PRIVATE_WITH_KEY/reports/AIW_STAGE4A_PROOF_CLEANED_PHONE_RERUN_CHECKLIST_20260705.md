# AIW Stage4A Proof-Cleaned Phone Rerun Checklist - 2026-07-05

## Import

Import/apply:

AIW_BUILD100_STAGE4A_NO_WORK_GUARD_PROOF_CLEANED_WITH_KEY_PRIVATE_20260705.xml

## Run Exactly

QC R4A APP Tick No-Work Proof

## Required Pass

- QC R4A APP Tick No-Work Proof = ExitOK
- APP Reset Locks = ExitOK
- APP Config Setup proof error, if run, must be NONE
- APP Reset Locks proof error must be NONE
- QC Selection Hardening Audit = ExitOK twice
- APP Run Tick Once = ExitOK
- FINAL Queue Cycle = ExitOK guarded no-send
- FINAL Send Sheet = 0
- AIW SEND 1 = 0
- Timer/live/archive/deadarchive/compactor/TT5 = 0
- Unhandled errors = 0

## Do Not Run Yet

- one-send live proof
- timer/live loop
- archive/deadarchive/compactor
