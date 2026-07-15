# Navigation And Lock Control-Flow Audit

## Navigation

- Input must be exactly ten digits before any UI action.
- TextNow launch, Navigate up, Chats, Search recovery, search-field recovery, sender search write, exact contact selection, and post-contact wait are source-derived.
- Numeric action errors set `THREAD_NAV_HOLD` and prevent later navigation stages.
- Search text may report an intermediate error; the proven reset/retry lane is retained.
- `THREAD_NAV_READY` is set only when the source-derived lane reaches the post-contact wait without a final action error.
- `THREAD_NAV_READY` is not confirmation.

## Confirmation

- Task 225 calls Task 231 once.
- Navigation HOLD sets `CONFIRM_NAVIGATION_HOLD` and `%continue=0`.
- The ready-only wrapper prevents Get Screen Info and DONE logic after navigation failure.
- Existing exact sender, exact unique reply, immediate `Sent`, package, DONE update, and DONE readback checks remain unchanged.

## Lock And Send Safety

- Task 231 owns and clears no transaction lock.
- Task 225 retains one guarded confirmation-lock release.
- Navigation failure reaches Task 225 common cleanup.
- Send nodes in Tasks 225/231: 0.
- Send-task calls in Tasks 225/231: 0.
- Automatic Send retries introduced: 0.
- Source row mutation from Task 231: 0.

Validator 1: PASS, 35 direct XML/raw checks.
Validator 2: PASS, 104 semantic/control-flow checks.
