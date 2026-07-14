# Preflight And Archive Source Search

## Search Result

- `FINAL Archive Done One V1`, Build90/Group E Archive proof, exact-row Archive, copy-before-clear, duplicate recovery, and broad Archive call paths were searched in the repository, private source storage, package history, and Drive metadata.
- Local files titled `basefile_v18c_archive_one_row_move_pass.xml` and `basefile_v18d_archive_multi_row_move_pass.xml` were not XML; their contents were Google sign-in HTML. They were rejected as runtime sources.
- The raw older V18C/V18D XML exports were not silently reconstructed.

## Exact Sources Selected

1. Gate 10 base Task 75 `FINAL Archive Done Rows`:
   - Action 28: current QueueView Get Data shape, not copied into Task 226.
   - Action 94: current Archive ID scan shape.
   - Action 104: current Archive Update Data shape.
   - Action 111: current Sheet1 clear Update Data shape.
   - Role: current spreadsheet ID, sheet names, current column mapping, and exported AutoSheets node shape only.

2. Group E 20B Task 422 `AIW ARCHIVE DONE ONE V1`, SHA256 `630D3DD233FD75CD5E30C8193DDAF99F11544DC3E0B159FD1F7300757373CE27`:
   - Action 108: Sheet1 A:I read shape.
   - Action 327: Archive ID scan shape.
   - Action 356: Archive row write shape.
   - Action 378: Sheet1 row clear shape.
   - Role: locked historical copy-before-clear order and Archive failure-before-clear behavior.

## Excluded Source Behavior

- Task 75 broad QueueView selector
- DONE/GROUPED multi-row eligibility
- broad Archive callers
- append/clear behavior lacking the Gate 11 exact copy/readback/idempotency contract
- any action that depended on unverified older HTML downloads

## Source Decision

The selected exported AutoSheets action shapes were preserved for plugin configuration. The bounded exact-row transaction wrapper, duplicate checks, exact readbacks, first-empty-row selection, source revalidation, and recovery states are new Gate 11 control logic. They are statically validated but not phone-proven.
