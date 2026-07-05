# AI Worker Patch Scope Register

Updated: 2026-07-05

## Active Scope

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

No runtime XML patch is allowed in this ledger task.

## Current Safe Patch Lane After ChatGPT Audit

Group B only:

- Task: `SS Safe Send Dry-Run`
- Area: `SEARCH_ICON`, `SEARCH_FIELD`, `CONTACT_PICK`
- Goal: contact-selection dry-run success without touching send button, message box, reply paste, or DONE marking.
- Required proof after patch/import: one phone runlog from `SS Safe Send Dry-Run`.

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
