# ChatGPT Audit Prompt: AIW Stage4B Send Dry-Run Preflight

Audit the attached ZIP:

AIW_STAGE4B_SEND_DRYRUN_PREFLIGHT_CANDIDATE_HOLD_20260705.zip

Drive link:

https://drive.google.com/file/d/1YaxY5ongeeHUmI2qcAa-ef-fBGJPxdA9/view?usp=drivesdk

Expected ZIP SHA256:

F2AABCFB3BB8044A584456298E8845E2992A1ADF6F4769BA9473826AEF336707

Do not print API keys or secrets.

Private runtime XML may contain key-bearing data. Preserve private file status in classification. In reports say only:

- KEY_PRESENT=true
- KEY_REDACTED_IN_REPORT=true

Audit goals:

1. Confirm Stage4A proof-cleaned runlog evidence:
   - QC R4A APP Tick No-Work Proof ExitOK
   - APP Reset Locks ExitOK
   - QC Selection Hardening Audit ExitOK
   - APP Run Tick Once ExitOK
   - FINAL Queue Cycle ExitOK guarded no-send
   - FINAL Send Sheet = 0
   - AIW SEND 1 = 0
   - timer/live/archive/deadarchive/compactor/TT5 = 0
   - unhandled errors = 0

2. Confirm Stage4B static dry-run preflight:
   - SS Safe Send Dry-Run exists.
   - It does not Perform Task FINAL Send Sheet.
   - It does not Perform Task SS Controlled One-Row Send Proof.
   - It does not Perform Task AIW SEND 1.
   - It does not contain TextNow button_send click.
   - It contains dry-run/pass/no-send proof markers.
   - It sets or preserves %SSSentOne=0 and does not set %SSSentOne=1.

3. Confirm current Sheet state from the included report:
   - QueueView READY_TO_SEND count is 0.
   - Current next phone proof can only prove NO_READY hold path.
   - Contact-selection dry-run requires exactly one controlled READY_TO_SEND test row later.

4. Classify:
   - Stage4A: CANDIDATE / STAGE4A PROCESS-ONLY PASS / HOLD FOR NEXT PROOF
   - Stage4B: CANDIDATE / HOLD FOR PHONE DRY-RUN PROOF
   - Overall Build100: CANDIDATE / HOLD

5. Required next step:
   - Run exactly SS Safe Send Dry-Run on phone with current Sheet state.
   - Export fresh Tasker runlog.
   - Required result for this no-ready proof:
     - SS Safe Send Dry-Run = ExitOK
     - NO_READY path proven
     - FINAL Send Sheet = 0
     - SS Controlled One-Row Send Proof = 0
     - AIW SEND 1 = 0
     - button_send = 0
     - timer/live/archive/deadarchive/compactor/TT5 = 0

Do not claim locked.

Do not claim ready.

Do not claim Stage4B phone proof until a new runlog proves it.
