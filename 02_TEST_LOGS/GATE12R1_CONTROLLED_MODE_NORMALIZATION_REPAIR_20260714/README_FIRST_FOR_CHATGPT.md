# Gate 12R1 Controlled-Mode Normalization Repair

Status: CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT

The original Gate 12 candidate is REJECTED FOR PHONE IMPORT. Tasker text substitution caused `%par1` and `%par2` embedded in two regex RHS fields to become the current argument values, which incorrectly normalized controlled mode to production.

Gate 12R1 uses the rejected Gate 12 XML only as the explicitly authorized direct repair base. It changes exactly two Task 199 condition RHS text fields and no other runtime field.

Operational tracker: 11/14 locked = 79%.

Gate 9, Gate 10, and Gate 11 remain LOCKED / PASS by direct Sosa phone proof. Codex records those controller decisions and does not independently claim phone proof.

Private artifacts:

- `GATE12R1_FULL_PROJECT_TASKER_IMPORT__QUEUE_LIFECYCLE_CONTROLLED_MODE_REPAIR_PRIVATE.xml` - 1690083 bytes - SHA256 `3DC49BF47837403B36D1B213564F34BD6983598B6734429324FF0ACEDA7A23C8`
- `GATE12R1_FULL_PROJECT_PHONE_IMPORT__QUEUE_LIFECYCLE_CONTROLLED_MODE_REPAIR_PRIVATE.zip` - 90096 bytes - SHA256 `0F3D2CAAA6DC74D34EA079618C343C6DB473AA8650A50534E887037600371817`
- `GATE12R1_SHA256__QUEUE_LIFECYCLE_CONTROLLED_MODE_REPAIR_PRIVATE.txt`

Validation:

- Raw-byte/XML/package validator: PASS.
- Tasker-substitution semantic validator: PASS.
- Prior Gate 12 matrix: 57/57 PASS.
- New substitution matrix: 8/8 PASS.
- Combined matrix: 65/65 PASS.
- Protected task nodes: 78/78 raw-byte identical.

Not proven: Tasker import/render or Gate 12 phone behavior.

Phone import approved by Codex: NO.

Phone proof claimed by Codex: NO.
