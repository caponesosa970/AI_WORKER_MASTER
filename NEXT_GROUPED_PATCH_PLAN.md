# AI Worker Next Grouped Patch Plan

Updated: 2026-07-05

## Status

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

No runtime XML patch is approved yet. After ChatGPT accepts this Stage4B ledger sync, the next candidate patch is limited to `SS Safe Send Dry-Run` search-key normalization.

## Safe Next Action

Group B2 normalization proposal only:

1. Start from current import-safe XML:
   `01_CANDIDATE_PATCHES/BUILD100_GROUP_B_SEARCH_ICON_IMPORT_SAFE/xml/AIW_BUILD100_GROUP_B_SEARCH_ICON_IMPORT_SAFE_FULL_TASKER_20260705.xml`
2. Patch only `SS Safe Send Dry-Run` search-key normalization.
3. If sender is phone-like or ticker has cleaned digits, use digits-only search key.
4. Add proof markers for selected search key and speed timestamps.
5. Do not touch `FINAL Send Sheet`, `SS Controlled One-Row Send Proof`, `AIW SEND 1`, message box, send button, timer/live, archive/deadarchive/compactor/TT5, or multi-send.
6. After ChatGPT audit and import, test with:
   - B = `+1(910) 447-7850`
   - I = `9104477850`
   - expected selected search key = `9104477850`
7. Run only:
   `SS Safe Send Dry-Run`
8. Export runlog.
9. Audit runlog before any next layer.

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
- selected search key shown as `9104477850`

## If It Fails

Patch only the failing sub-area inside `SS Safe Send Dry-Run`:

- search-key selection / normalization
- selected search key proof marker
- bounded waits only if the normalization proof shows they are still needed
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
