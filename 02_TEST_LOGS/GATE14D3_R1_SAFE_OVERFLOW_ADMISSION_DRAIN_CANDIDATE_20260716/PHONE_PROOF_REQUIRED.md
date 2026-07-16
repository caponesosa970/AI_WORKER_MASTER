# Phone Proof Required

Codex does not approve import, Sheet staging, or phone execution.

After ChatGPT audits the exact package, direct Sosa proof must separately establish:

1. `ADMIT_ONE_TO_OVERFLOW`: one exact PENDING row, exact readback, no Sheet1 write, no API call.
2. `SUPPRESS_EXACT_OVERFLOW_DUPLICATE`: no second overflow row, no Sheet1 write, duplicate count one.
3. `DRAIN_ONE_OVERFLOW`: one exact Sheet1 row, exact readback before exact DRAINED readback, all fields preserved.
4. `DRAIN_RERUN_IDEMPOTENT`: zero second main write, zero duplicate, source remains DRAINED.
5. Every mode: zero OpenAI, TextNow, Send, confirmation, DONE, Archive, profile, timer, and live actions.
6. Every owned lock releases exactly once; no unowned lock is cleared.

Controlled rows are isolated to OverflowInbox row 999 and Sheet1 row 199. ChatGPT must verify both exact states before staging or authorization.
