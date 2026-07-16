# Drain Transaction And Recovery

1. Acquire the shared owned admission lock.
2. Scan production OverflowInbox order and bind the earliest PENDING event.
3. Read and bind the exact A:N source row.
4. Scan Sheet1 for the exact original ID.
5. More than one main ID or conflicting fields HOLD.
6. One exact existing main row activates partial-commit recovery and skips the main write.
7. No existing ID requires an exact blank target, one A:I write, and exact A:I readback.
8. Only after main authority, write source status DRAINED.
9. Read exact source A:N back and require DRAINED with all other bound fields preserved.
10. Release the owned lock.

A completed controlled rerun verifies one DRAINED source and one exact existing main row, then performs zero writes.
