# Controlled Capacity State Machine

1. Task 239 requires and immediately consumes `%AIWG14DAllowTest = 1`.
2. It requires mode `PROCESS_CAPACITY`, a concrete uppercase run ID, count 5/10/25/50, worker off, profiles off, STOP clear, and transaction locks clear.
3. Task 238 independently repeats caller, input, profile, STOP, and lock checks.
4. It iterates rows 149-198 in ascending order, stopping at the requested count.
5. Each row gets deterministic synthetic ID, sender, and message values based on run ID and source row.
6. A fresh A:E read must prove exact A/B/C, status NEW, blank Reply, and no duplicate accepted ID before lock acquisition.
7. One processing lock is acquired for one row.
8. Existing Tasks 166/170/171/198/172 or 173 perform the phone-proven processing transaction.
9. A fresh A:E read must prove exact binding plus REVIEW_READY with a concrete Reply, or a safe review error with blank Reply.
10. The owned lock is released once before another row can start.
11. Any HOLD, STOP, stale Reply, binding failure, unverified terminal state, or lock-release failure prevents the next row from starting.
12. Final PASS requires exact started/completed/terminal counts, zero defects, equal lock counts, and no active processing lock.
