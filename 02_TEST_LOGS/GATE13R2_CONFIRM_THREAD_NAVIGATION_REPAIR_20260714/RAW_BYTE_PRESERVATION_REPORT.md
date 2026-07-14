# Raw-Byte Preservation Report

- Base SHA256: `CF955572B9EB7F9700E8563AFC6522427ECFE53576DEBF4E5F089BFD1F6A4BC6`
- Pre-existing tasks: 82.
- Existing task changed: Task 225 only.
- Other existing tasks raw-byte identical: 81/81 - PASS.
- Protected Tasks 71, 130, 131, 199, 223, 224, 226, 227, 228, 229, and 230: PASS.
- Profiles: raw-byte identical - PASS.
- Scene: raw-byte identical - PASS.
- Credential occurrence/value: unchanged without disclosure - PASS.
- Section-sign count: preserved at 399.
- Mojibake marker count: 0.

Within Task 225:

- Actions before the old launch prelude are unchanged semantically.
- Old Launch App and Wait are replaced by the Task 231 call and explicit ready guard.
- Existing Get Screen Info and exact sender/reply/`Sent` algorithm are unchanged semantically.
- Existing DONE update/readback and confirmation-lock cleanup are unchanged semantically.
