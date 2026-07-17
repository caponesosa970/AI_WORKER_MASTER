# ChatGPT Artifact Audit Checklist

- Verify standalone XML SHA and size.
- Verify ZIP SHA, one member, integrity, and byte equality.
- Parse actual XML and confirm 86 / 4 / 1.
- Compare every existing task node against the exact Gate 14A R2 base.
- Confirm only 166, 172, 173 changed and only 233, 234 were added.
- Independently inspect Task 69 and Task 232 raw equality.
- Reconcile the documented per-task hash-normalization discrepancy.
- Inspect all Task 233 reads, writes, retry loops, error routes, and exact readbacks.
- Confirm no write can occur before exact A/B/C binding.
- Confirm Reply verification precedes final status.
- Confirm partial failure never returns NEW or clears Reply.
- Confirm Task 173 cannot overwrite terminal/review/send states.
- Confirm Task 234 authorization, reserved bindings, lock ownership, one-shot hook, and common cleanup.
- Confirm no forbidden production/UI/API/Send/Archive path.
- Confirm profiles are disabled and credentials/private values are not public.
- Do not issue an import instruction from this Codex report alone.
