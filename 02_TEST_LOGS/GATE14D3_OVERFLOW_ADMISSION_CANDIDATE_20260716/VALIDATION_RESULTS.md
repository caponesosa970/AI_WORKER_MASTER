# Validation Results

- Direct XML/parser/raw preservation validator: PASS, 148 checks.
- Independent PowerShell semantic/control-flow validator: PASS, 28 checks.
- Standard Tasker static audit: PASS.
- XML parse/root: PASS / `TaskerData`.
- Topology: 95 tasks / 4 profiles / 1 scene.
- Duplicate task IDs/names: 0/0.
- Missing Perform Task/profile/scene references: 0/0/0.
- Existing tasks raw-byte identical: 93/93.
- Profiles disabled: 4/4.
- ZIP entry count: 1.
- ZIP XML byte equality: PASS.
- `git diff --check`: required before commit.

No phone/runtime claim is made by these static results.
