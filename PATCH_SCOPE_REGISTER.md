# AI Worker Patch Scope Register

Updated: 2026-07-05

## Active Scope

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

No runtime XML patch is allowed in this ledger sync task.

## Current Safe Patch Lane After ChatGPT Audit

Group B2 proposal only, after ChatGPT audit:

- Task: `SS Safe Send Dry-Run`
- Area: search-key normalization before `SEARCH_ICON` / TextNow search.
- Goal: if B has formatted phone text and I has cleaned digits, use the cleaned digits-only search key.
- Required proof after patch/import: one phone runlog from `SS Safe Send Dry-Run` with formatted B and cleaned I.

## Forbidden In Group B

- `FINAL Send Sheet`
- `SS Controlled One-Row Send Proof`
- `AIW SEND 1`
- send button
- message box
- reply paste
- DONE marking
- `START`
- timer/live/autonomous
- archive/deadarchive/compactor/TT5
- multi-send

## Current Locked Dry-Run Result

Stage4B digits-only dry-run passed with search key `9104477850`.

Do not patch the passed `SEARCH_ICON`, `SEARCH_FIELD`, `CONTACT_PICK_ATTEMPT`, lock release, or no-send guard unless the normalization patch directly requires a local adjustment and ChatGPT approves it.

## Later Patch Groups

| group | status | scope | unlock condition |
|---|---|---|---|
| Group C | HOLD | controlled one-send preparation | Stage4B contact-selection dry-run passes and ChatGPT approves. |
| Group D | HOLD | timer/live gates | Controlled one-send passes. |
| Group E | HOLD | archive/deadarchive/compactor/TT5 | Timer/live gates are proven safe or explicitly held off. |
| Group F | HOLD | 50-contact/capacity readiness | Prior send and timer gates are proven. |

## Grouping Rule

Only group changes that:

- are in the same layer,
- have separate pass/fail checks,
- do not touch frozen working logic,
- can be tested by one controlled phone proof sequence.

Do not group real send with timer, archive, or live activation.
