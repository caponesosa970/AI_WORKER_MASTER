# AI Worker Release Blocker Register

Updated: 2026-07-05

## Status

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

## Active Blockers

| blocker_id | classification | blocker | required proof or action |
|---|---|---|---|
| BLOCK-B2-001 | HOLD | ChatGPT has not audited this subsystem completion package. | ChatGPT classification and Group B2 patch approval. |
| BLOCK-B2-002 | HOLD | Formatted search-key normalization is unproven. | Group B2 phone runlog showing cleaned selected search key and contact pick pass. |
| BLOCK-B2-003 | HOLD | Message box detection and dry-run paste proof are unproven. | Group B2 dry-run runlog proving paste marker, `SEND=NO`, and send button untouched. |
| BLOCK-C-001 | HOLD | Controlled one-send is not proven. | One approved row, one approved recipient, one send, DONE only after proof. |
| BLOCK-D-001 | HOLD | Timer/live controller is not proven. | Timer/live proof after Group C pass; no uncontrolled sends. |
| BLOCK-E-001 | HOLD | Archive/deadarchive/compactor/TT5 are not proven. | Maintenance proof after core send/live gates. |
| BLOCK-F-001 | HOLD | 50-contact/capacity readiness is not proven. | Capacity proof with one-send-per-cycle and overflow hold/review behavior. |
| BLOCK-HIST-001 | HARD HOLD | Historical proof files are missing by exact name. | Restore exact files or keep historical claims unpromoted. |

## Failed Package Quarantine

Never use these as phone-test candidates:

- Failed SEARCH_ICON package with broken Tasker block nesting.
- Tasker import rejected/rebased XML package.
- 200-task private/reference XML as Build100 replacement.
- Stage4A no-work run where `FINAL Send Sheet` entered.
- Stage4B formatted-number run as a passing proof.

## Release Cannot Advance Until

- Group B2 passes and ChatGPT accepts it.
- Group C controlled one-send passes alone.
- Group D timer/live gates pass after Group C.
- Maintenance/capacity gates remain held or get their own proof.
