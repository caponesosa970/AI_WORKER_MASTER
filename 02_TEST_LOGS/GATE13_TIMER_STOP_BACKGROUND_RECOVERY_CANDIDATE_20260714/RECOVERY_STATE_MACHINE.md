# Safe Startup Recovery State Machine

Stale threshold: 300 seconds, inherited from the existing watchdog contract.

Recovery first performs the exact two-attempt QueueView read semantics copied from Task 71. It changes no lock if that read fails.

- Non-stale or timestamp-unknown lock: HOLD, no release.
- Stale processing lock: release only with a visible PROCESSING row; preserve the row and HOLD.
- Stale Send lock: release only with visible non-sendable lifecycle evidence; SENDING remains HOLD and is never changed to READY_TO_SEND.
- Stale confirmation lock: release only with exactly one awaiting-confirm row; route confirmation once.
- Stale Archive lock: release only with DONE/Archive recovery evidence; route exact-row Archive once.
- Stale worker-busy lock: release only after its timestamp is stale and no child transaction lock remains.
- Retrying, DeadArchive, or Compactor lock: HOLD with no automatic release.
- Awaiting-confirm without active locks: route confirmation once, then leave Start unarmed for that invocation.
- DONE without active locks: route Archive once, then leave Start unarmed for that invocation.
- Clear queue and clear locks: `RECOVERY_SAFE`.

Recovery never opens TextNow, clicks Send, rewrites SENDING, or calls more than one lifecycle module.
