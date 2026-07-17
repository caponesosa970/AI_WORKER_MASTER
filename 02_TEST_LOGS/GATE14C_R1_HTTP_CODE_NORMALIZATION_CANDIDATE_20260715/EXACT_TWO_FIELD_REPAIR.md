# Exact Two-Field Repair

Source XML SHA256: `71A766AE8D550C139AABCEC53DE3B1025CAF26C68561583CBF20AC6D5A5138B3`.

Changed task: `235 - PROCESS OpenAI Bounded Retry` only.

1. Existing `act119` remains in place and changes from `Variable Clear %http_response_code` to `Variable Set %http_response_code = 0` using the source-proven Tasker Variable Set structure.
2. Existing `act162` preserves `%api_observed_error != 1` and changes only the `%PSHttpCode` regex from `(?s)^\s*$|^%.*$` to `(?s)^\s*$|^%.*$|^0$`.

Task 235 action count: `243 -> 243`.

Task 235 raw SHA256:

- before: `A5920C1665BBBD900363CD63615631E2871D0A7FDC4EBAC17168B8698DBFE84A`
- after: `5DF99C24464FC1A601DC2ACC2390403596DFA8779D0D0CF1BB87C97F4CEC5267`

No action was added, removed, reordered, enabled, or disabled.
