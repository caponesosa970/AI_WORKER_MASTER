# Admission Transaction

1. Validate exact numeric event ID and concrete sanitized fields.
2. Acquire the shared owned admission lock.
3. Scan Sheet1 IDs and OverflowInbox original IDs.
4. HOLD on multiple IDs or conflicting exact-ID fields.
5. Suppress one valid existing exact ID with zero write.
6. For a new ID, select and independently prove one blank OverflowInbox target.
7. Write exactly one A:N PENDING row with offline update disabled.
8. Read exact A:N back and compare all fields.
9. Re-scan both stores and require exactly one matching ID in OverflowInbox and zero in Sheet1.
10. Release the owned lock.

No API, processing, TextNow, Send, confirmation, DONE, or Archive action is reachable.
