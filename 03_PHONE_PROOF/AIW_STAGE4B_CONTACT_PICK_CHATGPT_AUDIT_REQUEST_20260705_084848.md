# AIW Build100 Stage4B ChatGPT Audit Request

## Requested Classification

Classify this package and give Codex a patch order.

Use only these labels:

- LOCKED
- CANDIDATE
- HOLD
- HARD HOLD
- FAILED

Expected conservative status unless proven otherwise:

CANDIDATE / HOLD FOR CONTACT_PICK PATCH AND PHONE RERUN

## Current Build

- Project: AI Worker Build100
- Runtime target: Moto Razr 2024 / Tasker / TextNow / AutoInput / Google Sheets
- Current controlled XML: AIW_BUILD100_CONTROLLED_TEST_HOLD_FULL_TASKER.xml
- Current proof stage: Stage4B send dry-run contact-selection proof
- Required phone task: SS Safe Send Dry-Run

## Important Safety Rules

Do not redesign.
Do not enable live send.
Do not enable timer/live/autonomous routes.
Do not enable archive/deadarchive/compactor/TT5.
Do not enable multi-send.
Do not strip private/local runtime data from the XML.
Do not print secrets, keys, phone numbers, message contents, or contact data in reports.

One-send rule remains locked.
Any send path must keep %AIWSendBatchCap=1.

## Why This Package Exists

Stage4B is going in circles. Repeating the same phone test is no longer useful.

The latest failed run advanced farther than the prior one:

- Prior failure: SEARCH_ICON / early TextNow UI path
- Latest failure: CONTACT_PICK

The latest run did not prove a real send and did not press send.

Known latest audit facts:

- SS Safe Send Dry-Run ran and exited OK.
- FINAL Send Sheet did not run.
- AIW SEND 1 did not run.
- button_send marker was not present.
- %SSSentOne stayed 0.
- Safety dirty stop ran.
- Failure point: CONTACT_PICK.
- Sheet row was reset after failure for a future retry.

## What ChatGPT Should Audit

1. Open the full controlled Tasker XML.
2. Inspect the task SS Safe Send Dry-Run.
3. Inspect the CONTACT_PICK section and surrounding AutoInput/TextNow actions.
4. Compare against the failed Stage4B runlogs and audit reports.
5. Determine whether the issue is:
   - wrong selector,
   - wrong screen state assumption,
   - bad timing/wait,
   - keyboard/search overlay state,
   - contact result not selected,
   - missing guard,
   - or proof/test setup problem.
6. Give Codex the smallest safe patch order.

## Patch Order Needed From ChatGPT

Return a direct patch instruction for Codex:

- exact task name,
- exact failed area,
- smallest allowed change,
- forbidden changes,
- required static checks,
- required phone rerun,
- final conservative status.

## Required Phone Rerun After Patch

After Codex patches and static audit passes:

Run exactly:

SS Safe Send Dry-Run

Required pass:

- SS Safe Send Dry-Run = ExitOK
- CONTACT_PICK succeeds
- no SS Fail UI Dirty Stop
- FINAL Send Sheet = 0
- AIW SEND 1 = 0
- button_send = 0
- %SSSentOne=0
- no timer/live/archive/deadarchive/compactor/TT5 path

## Required Codex Output After Patch

- patched full Tasker XML
- static audit
- SHA256 inventory
- change report
- remaining HOLD list
- phone rerun checklist

Final Codex status must stay:

CANDIDATE / HOLD FOR PHONE RERUN

Do not claim locked.
Do not claim ready.
Do not claim phone-proven.
