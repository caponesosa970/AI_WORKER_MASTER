# Static Scenario Matrix

All required scenarios passed in the independent model and XML control audit:

1. Exact NEW/blank Reply marks PROCESSING.
2. Update error plus correct readback succeeds.
3. Two unverified mark attempts HOLD.
4-8. Wrong ID/sender/message/status/unresolved data produce zero writes.
9. Reply readback precedes final status.
10. Equal Reply continues idempotently.
11. Conflicting Reply blocks final-status write.
12. Final-status update error plus exact readback succeeds.
13. Failed final status routes to verified ERROR_PROCESS_REVIEW.
14. Failed review recovery leaves non-NEW partial HOLD and blocks grouping.
15-16. Failure commit verifies from NEW and PROCESSING.
17. Failure commit against terminal status writes zero.
18-19. One read failure recovers; two read failures HOLD.
20. Unsupported mode writes zero.
21-22. Unarmed or wrong reserved launcher input writes zero.
23-26. SUCCESS, WRONG_ID_HOLD, PARTIAL_AFTER_REPLY_HOLD, and FAILURE_COMMIT contracts are present and isolated.
27. Safe-mode REVIEW_READY and normal READY_TO_SEND remain preserved.
28-29. Tasks 69 and 232 remain byte-identical.
30. Launcher reaches no Send, confirm, Archive, UI, API, live, or production queue path.
