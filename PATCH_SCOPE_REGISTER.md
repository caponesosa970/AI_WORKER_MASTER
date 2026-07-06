# AI Worker Patch Scope Register

Updated: 2026-07-06

## Active Scope

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

This issue-history pass is documentation-only. No runtime XML patch is allowed in this task.

## Required Pre-Build Reads

Before every future build or package, Codex must read:

- `ISSUE_HISTORY_REGISTER.md`
- `BUILD_MISTAKE_PREVENTION_RULES.md`
- `FAILED_PACKAGES_LEDGER.md`

Codex must state which prevention rules apply before editing or packaging.

## Current Safe Baseline

- Current private runtime source: `PRIVATE_WITH_KEY/runtime_xml/10C_TASKER_IMPORT_XML__AIW_BUILD100_GROUP_B2_SEND_UI_DRYRUN_WITH_KEY_TASKER_SAFE_20260706.xml`
- Source SHA256: `5E6ACEC6AAADE464A3F19E9750A80E3B33CD3CDB97E5085B965429461ECF527F`
- Group B2 phone proof is the latest locked send-UI layer.

## Current Blocker

Group C controlled one-send is on HARD HOLD for the current narrow patch target:

`SS Controlled One-Row Send Proof`

Reason:

- missing approved-recipient guard,
- missing TextNow thread/header confirmation before send,
- DONE/pass markers occur after send-button action without independent sent-message proof.

## Next Safe Patch Lane After ChatGPT Audit

ChatGPT must choose one route:

1. broader rebuild of `SS Controlled One-Row Send Proof`, or
2. new isolated Group C controlled one-send proof task, or
3. continued HARD HOLD.

No Group C phone test is approved until this decision is made and a runtime patch package passes audit.

## Patch Group Boundaries

| group | status | scope | patch grouping | phone proof rule |
|---|---|---|---|---|
| Group B2 | LOCKED layer | Send UI Completion Dry-Run | Do not patch unless source changes or ChatGPT approves direct carry-forward fix. | Phone proof passed for dry-run paste/no-send only. |
| Group C | HARD HOLD | Controlled One-Send | Patch only after ChatGPT chooses safe route. | Must be phone-tested alone. |
| Group D | HOLD | Live Controller / Timer Gates | Patch after controlled one-send passes. | Must be phone-tested after Group C only. |
| Group E | HOLD | Maintenance / Recovery | Patch after live gates are safe or explicitly held. | Must not run with core send proof. |
| Group F | HOLD | Capacity / Production | Patch last. | Must be tested after Groups B2-C-D are proven. |

## Forbidden Until Approved

- FINAL Queue Cycle,
- FINAL Send Sheet,
- AIW SEND 1,
- START,
- timer/live/autonomous,
- archive/deadarchive/compactor/TT5,
- multi-send,
- redacted XML phone import,
- building from failed runtime XML,
- controlled send without approved-recipient and thread/header confirmation.

## Grouping Rule

Only group changes that are in the same layer, have separate pass/fail checks, do not touch frozen working logic, and can be tested by one controlled phone proof sequence.

Do not group real send with timer, archive, or live activation.
