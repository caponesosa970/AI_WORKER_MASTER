# Lock Ownership

Shared lock variables:

- `%AIWOverflowAdmissionLock`
- `%AIWOverflowAdmissionOwner`
- `%AIWOverflowAdmissionStartedAt`

Admission and drain acquire only when free, record a concrete owner, and verify owner readback.

The main logger slot claim transfers its lock to the existing logger cleanup boundary. Cleanup clears it only when the owner equals the current main logger token.

Overflow admission and drain retain local ownership and release only when the global owner still matches. A mismatched owner is never released.

All engine-owned terminal paths reach the common release block. The controlled launcher requires the shared lock to be free before entry.
