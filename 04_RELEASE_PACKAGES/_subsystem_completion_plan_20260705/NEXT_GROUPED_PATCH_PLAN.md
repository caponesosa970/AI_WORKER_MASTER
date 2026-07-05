# AI Worker Next Grouped Patch Plan

Updated: 2026-07-05

## Status

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

No runtime XML patch is approved yet. After ChatGPT accepts this subsystem completion plan, the next candidate patch is Group B2 only.

## Group B2 - Send UI Completion Dry-Run

Start from current import-safe XML:

`01_CANDIDATE_PATCHES/BUILD100_GROUP_B_SEARCH_ICON_IMPORT_SAFE/xml/AIW_BUILD100_GROUP_B_SEARCH_ICON_IMPORT_SAFE_FULL_TASKER_20260705.xml`

Patch only `SS Safe Send Dry-Run`:

- normalize the TextNow search key before search
- preserve the proven digits-only contact-pick route
- detect the message box in dry-run
- paste the test reply in dry-run only if ChatGPT approves that step
- log selected search key and speed timestamps
- set fail-closed proof values on miss
- stop before send button

## Group B2 Phone Proof

Run only:

`SS Safe Send Dry-Run`

Pass requires:

- `SS Safe Send Dry-Run = ExitOK`
- selected search key uses cleaned digits when formatted sender text is present
- `SEARCH_ICON OK`
- `SEARCH_FIELD OK`
- `CONTACT_PICK_ATTEMPT OK`
- message box detected if paste step is included
- dry-run paste marker present if paste step is included
- `SEND=NO`
- `%SSSentOne=0`
- `FINAL Send Sheet = 0`
- `SS Controlled One-Row Send Proof = 0`
- `AIW SEND 1 = 0`
- `button_send = 0`
- timer/live/archive/deadarchive/compactor/TT5 = 0
- no unhandled errors

## After Group B2 Passes

- Group C: controlled one-send preparation and one isolated phone test.
- Group D: timer/live gates after controlled one-send proof.
- Group E: archive/deadarchive/compactor/TT5 after core live path safety.
- Group F: 50-contact/capacity readiness after all prior gates.

## What Must Stay One-Layer Phone Proof Only

- Group B2 dry-run completion.
- Group C controlled one-send.
- Group D timer/live.
- Group E maintenance/recovery.
- Group F capacity/50-contact.

## Exact Next Codex Patch After ChatGPT Audit

Patch Group B2 in `SS Safe Send Dry-Run` only. Do not touch real send, timer/live, archive, maintenance, capacity, or failed package XML.
