# Validation Results

Validator 1, direct XML/raw-node/call-graph/package implementation: PASS, 36 checks.

Validator 2, independent PowerShell Tasker-state/control-flow implementation: PASS, 22 checks.

Tasker static audit:

- XML parse and TaskerData root: PASS.
- Topology: 91 tasks / 4 profiles / 1 scene.
- Duplicate task IDs/names: 0/0.
- Missing profile/Perform Task/scene references: 0/0/0.
- Duplicate action `sr` in Task 238: 0.
- Control stack final depth: 0.
- AutoSheets Get Data actions: 2, unchanged range and plugin semantics, Continue Task After Error ON.
- Bounded read attempts: 2 maximum per read.
- `json:true`: 0; `<se>true</se>`: 0; mojibake indicators: 0.
- Forbidden Send/confirmation/Archive/live paths added: 0.
- ZIP entry count: 1; XML byte equality: PASS.
