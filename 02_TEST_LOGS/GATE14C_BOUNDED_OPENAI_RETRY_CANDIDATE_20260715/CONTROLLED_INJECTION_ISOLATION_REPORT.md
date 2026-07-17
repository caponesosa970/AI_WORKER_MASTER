# Controlled Injection Isolation

Task 237 is uncalled and one-shot authorized by `%AIWG14CAllowTest = 1`.

Injected outcomes require all of:

- controlled wrapper context;
- `%PSApiTestAuthorized = 1`;
- exact supported mode;
- exact reserved row;
- exact reserved ID.

The authorization is consumed before use and cleared on exit. Production Task 171 does not create the controlled authorization/context.

Expected real HTTP calls:

- `REAL_SUCCESS`: 1
- `RATE_LIMIT_THEN_SUCCESS`: 1
- `TIMEOUT_EXHAUSTED`: 0
- `QUOTA_429_NO_RETRY`: 0
- `LEGACY_RETRY_MIGRATION`: 0

Unsupported mode, authorization, row, or ID combinations fail before lock, HTTP, or Sheet write.
