# AI Worker Next Grouped Patch Plan

Updated: 2026-07-05

## Status

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

No more repeated phone loops until ChatGPT audits this ledger or explicitly tells Codex the next patch order.

## Safe Next Group

Group B retry only:

1. Use current import-safe XML:
   `01_CANDIDATE_PATCHES/BUILD100_GROUP_B_SEARCH_ICON_IMPORT_SAFE/xml/AIW_BUILD100_GROUP_B_SEARCH_ICON_IMPORT_SAFE_FULL_TASKER_20260705.xml`
2. Import into Tasker only if the phone accepts the XML.
3. Prepare exactly one approved `READY_TO_SEND` row.
4. Run only:
   `SS Safe Send Dry-Run`
5. Export runlog.
6. Audit runlog before any next layer.

## Pass Conditions

- `SS Safe Send Dry-Run = ExitOK`
- `DRYRUN_CONTACT_PICK_PASS` or `SEND_DRYRUN_PASS` present
- `SEND=NO`
- `%SSSentOne=0`
- `FINAL Send Sheet = 0`
- `SS Controlled One-Row Send Proof = 0`
- `AIW SEND 1 = 0`
- `FINAL Send Sheet LEGACY = 0`
- `button_send = 0`
- message box marker = 0
- timer/live/archive/deadarchive/compactor/TT5 = 0
- no unhandled errors

## If It Fails

Patch only the failing sub-area inside `SS Safe Send Dry-Run`:

- `SEARCH_ICON`
- `SEARCH_FIELD`
- `CONTACT_PICK`
- bounded waits
- safe keyboard/back dismissal
- fail-closed proof values

Do not patch send logic.

## After Group B Passes

Next grouped plan remains HOLD until ChatGPT approves:

- Group C: controlled one-send proof preparation.
- Group D: timer/live gates.
- Group E: archive/deadarchive/compactor/TT5.
- Group F: 50-contact/capacity readiness.

## One-Layer Phone Proof Only

Each of these must be tested alone:

- Stage4B contact-selection dry-run.
- Controlled one-send.
- Timer/live loop.
- Archive/deadarchive/compactor/TT5.
- Capacity/50-contact.
