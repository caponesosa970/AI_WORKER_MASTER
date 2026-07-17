# Second Controller Audit Reconciliation

1. Unowned release: all changed callers are disconnected from `TT5 Simple Log Lock Release HARD`; it has zero incoming callers. Release requires exact owner-token equality.
2. Eight-second race: the age-only logger clear is removed. Admission and overflow locks store owner plus start timestamp and are never stolen by age.
3. ID race/collision: canonical numeric `OriginalID` is built under owned ingress. Numeric `OverflowID` is separately generated under the overflow owner. Same ID/same payload suppresses; same ID/different payload returns `ID_COLLISION_REVIEW`; multiple Sheet1 matches return `DUPLICATE_MAIN_REVIEW`.
4. AutoSheets hygiene: every Get Data node uses native Tasker `Array Clear` for each output array, clears `%err` and `%errmsg`, continues after error, detects numeric nonzero errors, and is bounded to two attempts.
5. Views as hints: `OpenSlotView` and `OverflowSlotView` provide candidate rows only. Exact Sheet1 A:I or OverflowInbox A:N blank readback is write authority. Invalid candidates are never coerced to row 2.
6. Shared ownership: main ingress and overflow drain use `%AIWAdmissionOwner` / `%AIWAdmissionStartedAt`; overflow operations also use `%AIWOverflowOwner` / `%AIWOverflowStartedAt`.
7. Append: exact cross-store check, owned target selection, direct A:N blank check, PENDING write, full readback, then owned release. Pending count is not optimistically incremented.
8. States: PENDING, DRAINING, MAIN_COMMITTED, DRAINED, OVERFLOW_REVIEW. All except DRAINED form the unresolved barrier.
9. Drain: FIFO source is bound, PENDING becomes DRAINING, exact Sheet1 identity is scanned, payload is written as OVERFLOW_ADMITTING, payload is read back, NEW is written last, then MAIN_COMMITTED and DRAINED are each written and read back.
10. Failure evidence: drain review paths increment Attempts and persist LastError before OVERFLOW_REVIEW.
11. STOP: owner acquisition is blocked when STOP is requested. Once a durable state starts, the transaction reaches a verified boundary or leaves DRAINING/MAIN_COMMITTED/OVERFLOW_REVIEW for recovery before exact-owner release.
12. Drain cap: production cap remains three. Control uses exact constants `OVERFLOW_DRAIN_MOVED`, `OVERFLOW_DRAIN_EMPTY`, `OVERFLOW_DRAIN_HOLD`, and `OVERFLOW_DRAIN_RECONCILED`.
13. Capacity: configured source rows are 2-1000, capacity 999. No overwrite or target coercion occurs. Capacity returns `OVERFLOW_CAPACITY_HOLD` and preserves the ingress hold fields.
14. Test IDs: controlled OriginalIDs must match numeric production format `^[0-9]{10,18}$`.
15. Modes: all five controller modes are present with one-shot authorization and isolated production-valid data.
16. Outputs: result, error, mode, run ID, both identities, rows, counts, readbacks, lock acquire/release counts, wrong-row count, duplicate-main count, and final verification are exposed.
17. Scope: only Tasks 33, 35, 68, 215, 217, 218, 219, and 220 change. Tasks 242-245 are added. All 85 other existing tasks are raw-byte identical.
18. Formula findings: view formulas remain candidate hints; live formula/grid alignment is not changed by Codex; DRAINED accumulation and capacity warning remain Gate 14G release work.
19. Static proof: structural validator 360/360 PASS, semantic validator 64/64 PASS, standard Tasker XML audit PASS. No forbidden module is reachable from the controlled launcher.
