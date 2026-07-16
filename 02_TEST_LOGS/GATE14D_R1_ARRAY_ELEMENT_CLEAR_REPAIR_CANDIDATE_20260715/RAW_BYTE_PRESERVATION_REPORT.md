# Raw Preservation

- Existing task count: 91.
- Changed task blocks: Task 238 only.
- Unchanged task blocks: 90/90 raw-byte identical.
- Task 239 raw-byte identical: PASS.
- Profiles: 4/4 raw-byte identical and disabled.
- Scene: raw-byte identical.
- Project registry: raw-byte identical.
- Credential: equality checked without printing; unchanged because all bytes outside Task 238 are preserved.
- Task 238 action count: 389 -> 399.
- Removing the ten inserted clears and neutralizing required action `sr` renumbering reproduces all 389 original action nodes semantically: PASS.
- Section-sign count unchanged; mojibake indicator count zero.
