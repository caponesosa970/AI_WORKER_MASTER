# Static Scenario Matrix

All required static scenarios PASS.

| Scenario | Result |
|---|---|
| Exact duplicate across stores | PASS, no new row |
| Same OriginalID with different payload | PASS, collision review |
| Multiple matching main rows | PASS, duplicate-main review |
| Pending barrier includes all unresolved states | PASS |
| FIFO LoggedAt then source row | PASS |
| PENDING to verified DRAINING before admission lock | PASS |
| Exact blank target authority | PASS |
| Payload verified before NEW | PASS |
| MAIN_COMMITTED and DRAINED exact readback | PASS |
| Existing exact main row reconciliation | PASS, zero second main write |
| Every bound failed drain records Attempts/LastError | PASS |
| Capacity 999 full path | PASS, no overwrite |
| STOP before acquisition | PASS, zero new acquisition |
| Drain cap exact constants and cap three | PASS |
| Controlled five-mode isolation | PASS |
| Forbidden processing/API/TextNow/lifecycle paths | PASS |

Phone behavior remains unsupported until ChatGPT audits this exact artifact and Sosa performs the controlled phone ladder.
