# Static Scenario Matrix

| Scenario | Result |
|---|---|
| Injected timeout attempt one starts at code 0 and retries once | PASS |
| Injected timeout attempt two ends at code 0 and `OPENAI_TRANSIENT_EXHAUSTED` | PASS |
| No numeric error and no returned code is classified as bounded missing code 0 | PASS |
| Real HTTP 200 overwrites 0 and succeeds | PASS |
| Normal injected 429 overwrites 0 and retries once | PASS |
| Quota injected 429 overwrites 0 and does not retry | PASS |
| Maximum attempts remains two | PASS |
| Maximum retries remains one | PASS |
| No third request is reachable | PASS |
| Modeled `%PSHttpCode` and launcher last-code outputs are numeric | PASS |
| Task 233 remains unchanged | PASS |
| Task 237 remains unchanged | PASS |
| Existing rate-limit and quota route structure is unchanged after explicit 429 assignment | PASS |

These are static results only and do not replace the required phone regressions.
