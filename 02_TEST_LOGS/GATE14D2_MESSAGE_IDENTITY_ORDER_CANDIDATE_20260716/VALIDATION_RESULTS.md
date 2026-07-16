# Validation Results

Validator one, direct XML/raw preservation/source mapping/call graph/package: PASS, 149 checks.

Validator two, independent PowerShell mode reachability and state models: PASS, 30 checks.

Tasker static audit:

- XML parse and TaskerData root: PASS.
- Topology: 93 tasks / 4 profiles / 1 scene.
- Duplicate task IDs/names: 0/0.
- Missing profile/Perform Task/scene/project references: 0.
- Duplicate action `sr`: 0.
- Control stacks: balanced.
- `json:true`: 0; `<se>true</se>`: 0; mojibake indicators: 0.
- ZIP entry count: 1; standalone XML byte equality: PASS.
