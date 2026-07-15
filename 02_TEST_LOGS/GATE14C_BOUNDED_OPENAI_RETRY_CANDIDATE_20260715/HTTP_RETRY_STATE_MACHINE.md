# HTTP Retry State Machine

1. Validate exact processor binding, prompts, endpoint, model, and private-key contract.
2. Clear all HTTP outputs and `%err/%errmsg` before each attempt.
3. Execute at most two attempts.
4. Accept success only for code 200, usable response data, and no numeric action error.
5. Retry only one time for network/timeout, missing code, 408, 409, normal 429, 500/502/503/504, or unusable 200 data.
6. Choose and record a 2, 3, or 4 second randomized backoff.
7. Do not retry quota, auth, bad request, configuration, or other non-transient 4xx outcomes.
8. Return a safe OpenAI-prefixed final class with no response body in public/error logs.
9. Task 173 persists final API failures as `ERROR_OPENAI_REVIEW` through Task 233 exact readback.

Hard limits:

- HTTP node count in Task 235: 1.
- maximum executions of that node per run: 2.
- maximum retry count: 1.
- recursive HTTP task calls: 0.
- automatic cross-cycle API retry status creation: 0.
