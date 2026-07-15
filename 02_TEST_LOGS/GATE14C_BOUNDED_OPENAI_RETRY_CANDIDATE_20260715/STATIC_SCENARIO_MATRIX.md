# Static Scenario Matrix

All 40 required scenarios passed both direct XML/control inspection and the independent state model.

| # | Scenario | Result |
| ---: | --- | --- |
| 1 | Valid 200 response | PASS - one attempt |
| 2 | Normal 429 then 200 | PASS - one backoff, two attempts |
| 3 | Timeout then 200 | PASS - bounded retry |
| 4 | 500 then 200 | PASS - bounded retry |
| 5 | 503 twice | PASS - two attempts, exhausted |
| 6 | Connection failure twice | PASS - two attempts, exhausted |
| 7 | 429 insufficient quota | PASS - no retry |
| 8 | 401 | PASS - no retry |
| 9 | 403 | PASS - no retry |
| 10 | 400 | PASS - no retry |
| 11 | 422 | PASS - no retry |
| 12 | Missing key | PASS - zero HTTP |
| 13 | Invalid endpoint | PASS - zero HTTP |
| 14 | Prompt not ready | PASS - zero HTTP |
| 15 | 200 blank response | PASS - one retry maximum |
| 16 | 200 unresolved response | PASS - one retry maximum |
| 17 | 200 `#ERROR` response | PASS - one retry maximum |
| 18 | Attempt cap | PASS - no third attempt |
| 19 | Retry counter | PASS - maximum one |
| 20 | Real-call counter | PASS - actual HTTP only |
| 21 | Production injection isolation | PASS |
| 22 | Wrong reserved row | PASS - zero lock/HTTP/write |
| 23 | Wrong reserved ID | PASS - zero lock/HTTP/write |
| 24 | Authorization absent | PASS - zero lock/HTTP/write |
| 25 | REAL_SUCCESS path | PASS static / PHONE HOLD |
| 26 | RATE_LIMIT_THEN_SUCCESS path | PASS static / PHONE HOLD |
| 27 | TIMEOUT_EXHAUSTED path | PASS static / PHONE HOLD |
| 28 | QUOTA_429_NO_RETRY path | PASS static / PHONE HOLD |
| 29 | Legacy retry migration | PASS static / PHONE HOLD |
| 30 | Legacy wrong ID | PASS - zero writes |
| 31 | Legacy Reply preservation | PASS |
| 32 | Task 70 has no API retry-to-NEW path | PASS |
| 33 | Task 173 BAD_MESSAGE behavior | PASS |
| 34 | Task 69 raw-byte preservation | PASS |
| 35 | Task 233 one-field scope | PASS |
| 36 | Task 234 raw-byte preservation | PASS |
| 37 | Owned launcher lock release | PASS |
| 38 | No unowned lock release | PASS |
| 39 | No response body in public logs | PASS |
| 40 | No TextNow/Send/confirm/Archive/live/profile path | PASS |

Static PASS is not phone proof.
