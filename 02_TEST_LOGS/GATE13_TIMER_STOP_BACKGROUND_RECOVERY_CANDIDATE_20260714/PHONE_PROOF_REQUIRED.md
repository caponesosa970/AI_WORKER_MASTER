# Phone Proof Required

Phone import is not approved by Codex.

Required Gate 13 ladder after ChatGPT audits the exact XML and ZIP:

1. Import/render with every profile still disabled.
2. Not-armed launcher check: no profile enabled and no queue call.
3. One-shot safe timer: manually verify environment, arm once, prove one scheduled tick, one Queue Cycle maximum, timer self-disables.
4. STOP before tick: prove no queue call.
5. STOP during a non-Send owned transaction: prove future triggers stop and owner releases itself.
6. Busy/overlap test: prove second tick skips and does not queue another cycle.
7. Non-stale lock startup: prove HOLD and no lock release.
8. Stale SENDING recovery: prove lock release only with non-sendable row preserved and no Send retry.
9. Awaiting-confirm recovery: prove confirmation only, no Send.
10. DONE/Archive recovery: prove exact-row Archive only.
11. Screen-off and keyguard checks: prove the tick blocks before TextNow UI.

Capacity, release, live unattended operation, screen-off operation, and background-restriction claims remain blocked.
