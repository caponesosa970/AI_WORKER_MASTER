# Phone Proof Required

Phone proof is not claimed by this package.

No import is approved by Codex.

Before any phone test, ChatGPT must audit the ZIP and identify the exact importable XML path if approved.

Future phone proof would need to show:
- Task imports cleanly.
- Row 75 gate behavior stops safely when `%AIW27BAllowSend` is 0.
- No TextNow send occurs unless ChatGPT separately approves the one-send branch.
- If a controlled send is ever approved, `%AIW27BAllowSend=1` must be explicitly set for that one test and row 75 must be `READY_TO_SEND`.
