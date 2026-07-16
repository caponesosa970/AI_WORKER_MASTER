# Independent Validator Results

Validator one - direct XML, raw-node, ZIP, profile, scene, and registry comparison:

- result: PASS
- checks: 29/29

Validator two - independent PowerShell semantic parser and retry-state model:

- result: PASS
- checks: 24/24

Standard Tasker static audit:

- XML parse: PASS
- root: `TaskerData`
- topology: `89 / 4 / 1`
- duplicate task IDs: 0
- duplicate task names: 0
- missing profile/task/scene references: 0
- `json:true`: 0
- `<se>true</se>`: 0
- mojibake indicators: 0

No generated report was used as the sole proof of its own correctness.
