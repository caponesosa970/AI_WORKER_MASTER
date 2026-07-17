# Exact Changed Task And Action List

Existing tasks:

- Task 33 `FINAL Simple Slot Recycler`: 23 to 6 actions; delegates only to the owner-checked exact slot claimant.
- Task 35 `FINAL Simple Get Open Slot Row`: 25 to 6 actions; same owner-checked claimant.
- Task 68 `FINAL Simple`: 175 to 40 actions; actions 0-29 filtering preserved, admission/overflow lane replaced by the permanent state machine.
- Task 215 `TT5 Build Message ID If Missing`: 10 to 9 actions; canonical numeric OriginalID without an unowned sequence race.
- Task 217 `TT5 Log Current Message To OverflowInbox`: 48 to 8 actions; permanent append wrapper.
- Task 218 `TT5 Overflow Pending Quick Check`: 17 to 9 actions; all unresolved states and fail-closed read.
- Task 219 `TT5 Overflow Drain One`: 79 to 14 actions; permanent idempotent drain wrapper with exact constants.
- Task 220 `TT5 Overflow Drain Cap`: 18 to 12 actions; exact-result three-drain cap.

Added tasks:

- Task 242 `TT5 Owner Token Lock`: 79 actions.
- Task 243 `TT5 Cross Store Event Check`: 179 actions.
- Task 244 `TT5 Safe Overflow State Machine`: 4155 actions.
- Task 245 `AIW GATE14D3 SAFE OVERFLOW TEST`: 408 actions.

No other existing task changed.
