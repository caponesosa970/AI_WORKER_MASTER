# Phone Proof Required

ChatGPT must audit the exact R1 XML, ZIP, and sidecar before any import approval.

Required controlled phone regressions after approval:

1. Import/render the exact R1 package.
2. Rerun `TIMEOUT_EXHAUSTED`; require last HTTP code `0`, two attempts, one retry, zero real HTTP calls, exact `ERROR_OPENAI_REVIEW`, blank Reply, and one owned-lock release.
3. Rerun `REAL_SUCCESS`; require last HTTP code `200`, one real request, exact verified Reply/final status, and one owned-lock release.
4. Run the pending `LEGACY_RETRY_MIGRATION`; require zero HTTP calls and exact migration to `ERROR_OPENAI_REVIEW` with Reply preserved.

The prior normal-rate-limit and quota phone proofs remain controller evidence only if ChatGPT confirms those paths are unchanged apart from the overwritten neutral initialization.

Codex approves phone import: NO. Codex claims phone proof: NO.
