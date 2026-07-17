# Exact Changed Task And Action List

Changed existing tasks:

- `FINAL Simple Get Open Slot Row`: 25 to 6 actions. It delegates slot claim to the shared exact transaction engine.
- `TT5 Simple Log Lock Release HARD`: 2 to 9 actions. It releases the shared main-slot lock only when its owner token matches.
- `TT5 Log Current Message To OverflowInbox`: 48 to 10 actions. It retains ID creation and sanitization, then delegates exact admission.
- `TT5 Overflow Drain One`: 79 to 8 actions. It delegates exact drain and maps only verified results.

Added:

- `TT5 Safe Overflow Admission Drain`: 2,320 actions.
- `AIW GATE14D3 SAFE OVERFLOW TEST`: 128 actions.

No other existing task changed. Final topology: 95 tasks / 4 disabled profiles / 1 scene.
