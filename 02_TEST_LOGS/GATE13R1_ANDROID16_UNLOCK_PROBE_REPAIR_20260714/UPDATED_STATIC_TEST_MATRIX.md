# Updated Static Test Matrix

Required matrix result: `16/16 PASS`

| Case | Result |
| --- | --- |
| Visible unlocked: both platform values false | PASS - UNLOCKED |
| Active lock: either platform value true | PASS - LOCKED |
| Screen off | PASS - blocked before queue |
| Java Function error | PASS - HOLD |
| Blank result | PASS - HOLD |
| Unresolved literal result | PASS - HOLD |
| Task 224 authorization consumed immediately | PASS |
| Unlocked/environment-ready with AIWorkerBusy=1 | PASS - timer can arm; tick skips busy; Queue Cycle 0 |
| Task 228 locked state | PASS - TICK_SKIPPED_KEYGUARD; Queue Cycle 0 |
| Task 130 locked state | PASS - START_KEYGUARD_HOLD; profile enable 0 |
| `%KEYG` remaining in Tasks 130/224/228 | PASS - 0 |
| Protected lifecycle task bytes | PASS |
| Profiles enabled in artifact | PASS - 0 |
| Reachable duplicate Send | PASS - none introduced |
| Live Sheet mutation by Codex | PASS - none |
| Credential disclosure | PASS - none |

Additional control-flow checks: `10/10 PASS`.

Independent validator results:

- direct XML/raw/reference/package validator: PASS (`34/34`);
- independent state-machine validator: PASS (`16/16` plus `10/10`);
- repository Tasker static auditor: PASS.
