# AI Worker Patch Scope Register

Updated: 2026-07-05

## Active Scope

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

This pass is documentation-only. No runtime XML patch is allowed in this subsystem completion task.

## Next Safe Patch Lane After ChatGPT Audit

Group B2 only:

- Task: `SS Safe Send Dry-Run`
- Areas: search-key normalization, message-box detection, dry-run paste proof, proof markers, speed timestamps, fail-closed route, stop-before-send-button guard.
- Goal: finish dry-run send UI completion without touching real send.
- Required proof after patch/import: one phone runlog from `SS Safe Send Dry-Run`.

## Forbidden In Group B2

- `FINAL Send Sheet`
- `SS Controlled One-Row Send Proof`
- `AIW SEND 1`
- send button
- DONE marking
- `START`
- timer/live/autonomous
- archive/deadarchive/compactor/TT5
- multi-send

## Patch Group Boundaries

| group | status | scope | patch grouping | phone proof rule |
|---|---|---|---|---|
| Group B2 | CANDIDATE | Send UI Completion Dry-Run | May patch as one subsystem. | One dry-run phone proof only. |
| Group C | HOLD | Controlled One-Send | Patch after Group B2 passes. | Must be phone-tested alone. |
| Group D | HOLD | Live Controller / Timer Gates | Patch after controlled one-send passes. | Must be phone-tested after Group C only. |
| Group E | HOLD | Maintenance / Recovery | Patch after live gates are safe or explicitly held. | Must not run with core send proof. |
| Group F | HOLD | Capacity / Production | Patch last. | Must be tested after Groups B2-C-D are proven. |

## Grouping Rule

Only group changes that are in the same layer, have separate pass/fail checks, do not touch frozen working logic, and can be tested by one controlled phone proof sequence.

Do not group real send with timer, archive, or live activation.
