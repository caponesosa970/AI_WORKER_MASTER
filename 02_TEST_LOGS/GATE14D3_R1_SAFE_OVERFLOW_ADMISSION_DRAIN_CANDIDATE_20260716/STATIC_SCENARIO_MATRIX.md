# Static Scenario Matrix

| Scenario | Main writes | Overflow admission writes | Source-state writes | Result |
|---|---:|---:|---:|---|
| New exact event admission | 0 | 1 | 0 | PENDING verified |
| Exact duplicate in OverflowInbox | 0 | 0 | 0 | suppressed |
| Exact duplicate in Sheet1 | 0 | 0 | 0 | suppressed |
| Conflicting or multiple duplicate | 0 | 0 | 0 | HOLD |
| Fresh PENDING drain | 1 | 0 | 1 | DRAINED verified |
| Main write already committed, source PENDING | 0 | 0 | 1 | recovery verified |
| Completed drain rerun | 0 | 0 | 0 | already complete |
| Wrong controlled ID or source row | 0 | 0 | 0 | HOLD |
| Target not blank | 0 | 0 | 0 | HOLD |
| Lock busy or owner mismatch | 0 | 0 | 0 | HOLD |
| Read/write failure after two attempts | bounded | bounded | bounded | HOLD |

All modeled writes are bounded to at most two attempts with exact readback authority.
