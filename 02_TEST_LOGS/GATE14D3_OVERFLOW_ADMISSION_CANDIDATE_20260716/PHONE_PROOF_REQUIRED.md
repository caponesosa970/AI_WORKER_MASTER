# Phone Proof Required

Codex does not approve import or staging.

After ChatGPT audits the exact XML, ZIP, and sidecar, direct Sosa proof must separately establish:

1. `ADMIT_50_DEFER_1` processes exact rows 149-198 once in ascending order with 50 API calls, 50 verified commits, and balanced 50/50 locks.
2. Row 199 remains exact NEW with blank Reply and is the only deferred row.
3. `DRAIN_DEFERRED_1` processes only row 199 once with one API call, one verified commit, and balanced 1/1 lock ownership.
4. Rows 149-198 are not processed again during the drain.
5. No TextNow, Send, confirmation, DONE, Archive, profile, timer, or live path runs.
