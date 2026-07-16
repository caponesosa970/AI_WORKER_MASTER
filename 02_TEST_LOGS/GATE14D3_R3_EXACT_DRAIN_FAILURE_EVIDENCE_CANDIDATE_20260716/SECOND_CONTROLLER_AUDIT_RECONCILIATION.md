# Second Controller Audit Reconciliation

1. Unowned release: all changed callers are disconnected from the legacy hard release. Release requires exact local/stored owner equality.
2. Eight-second race: age-only lock stealing is absent. Admission and overflow locks store owner plus start timestamp and are never cleared by age alone.
3. ID race/collision: numeric OriginalID is canonicalized under owned ingress; numeric OverflowID is generated separately under overflow ownership. Duplicate, collision, and duplicate-main classifications are distinct.
4. AutoSheets hygiene: every new Get Data clears arrays, err, and errmsg, continues after error, detects numeric nonzero errors, rejects unresolved outputs, and is bounded to two attempts.
5. Candidate versus authority: OpenSlotView and OverflowSlotView are hints only. Exact Sheet1 A:I and OverflowInbox A:N direct reads are write authority. No invalid row becomes row 2.
6. Shared ownership: main ingress and overflow drain use AIWAdmissionOwner/StartedAt; overflow operations use AIWOverflowOwner/StartedAt. Release is owner-matched.
7. Append transaction: cross-store check, owned candidate selection, exact blank A:N proof, PENDING write, complete readback, then owner release. No optimistic pending count is used.
8. State machine: PENDING, DRAINING, MAIN_COMMITTED, DRAINED, and OVERFLOW_REVIEW are exact persisted states. Every state except DRAINED forms the unresolved direct-admission barrier.
9. Drain transaction: overflow ownership, FIFO selection, exact source read/bind, and verified DRAINING all occur before shared admission acquisition. Payload is written as OVERFLOW_ADMITTING and verified before NEW; MAIN_COMMITTED and DRAINED are then verified.
10. Failure records: every exact-source-bound failed drain reaches a common bounded Attempts/LastError M:N write/readback unless its review branch already verified the evidence. Existing LastError is preserved and extended.
11. STOP: STOP blocks new lock acquisition. A started durable transaction reaches a verified or persistent recoverable state before exact-owner release.
12. Drain cap: cap remains three. Control uses exact constants OVERFLOW_DRAIN_MOVED, OVERFLOW_DRAIN_EMPTY, OVERFLOW_DRAIN_HOLD, and OVERFLOW_DRAIN_RECONCILED.
13. Capacity: configured data source rows are 2-1000, capacity 999. Full capacity cannot overwrite or coerce a target and returns OVERFLOW_CAPACITY_HOLD.
14. Test IDs: controlled OriginalIDs must match the numeric production format of 10-18 digits.
15. Modes: ADMIT_TWO_WITH_PENDING_BARRIER, SUPPRESS_DUPLICATE_AND_HOLD_COLLISION, DRAIN_TWO_FIFO, RECONCILE_PARTIAL_COMMIT, and OVERFLOW_CAPACITY_HOLD are isolated behind one-shot authorization.
16. Outputs: result, error, mode, run ID, identities, rows, transaction counts, readbacks, lock counts, wrong rows, duplicate-main count, and final verification are exposed.
17. Scope: existing Tasks 33, 35, 68, 215, 217, 218, 219, and 220 change. Tasks 242-245 are added. The other 85 existing tasks are raw-byte identical.
18. Formula findings: view formulas remain candidate hints; live formula/grid alignment is unchanged by Codex; DRAINED accumulation and interface capacity warnings remain later release work.
19. Static proof: structure validator 367/367 PASS; semantic validator 69/69 PASS; standard XML audit and one-entry ZIP equality PASS. No forbidden module is reachable.
