# AIW Build100 Current Source Routing - 2026-07-04

## Current Usable Candidate Source

Use this XML for the controlled-test Build100 path:

`01_CANDIDATE_PATCHES/AIW_BUILD100_CONTROLLED_TEST_HOLD_FULL_TASKER.xml`

SHA256:

`99B2A1C8C9AE1FF3FF191F49ACA9245DAEA45A5FA08810EAE89D3DAB5BF18D7F`

Static status:

- XML parse: PASS
- Task count: 215
- Profile count: 4
- Scene count: 2
- Duplicate task IDs: 0
- Duplicate task names: 0
- Missing profile task refs: 0
- Missing Perform Task refs: 0
- Missing scene clickTask refs: 0
- Tasker block issues: 0 in the controlled-test deep audit
- Final classification: HOLD because phone/runlog proof is still missing

## Do Not Use As Current Runtime Candidate

Do not use this older project candidate as the current controlled-test source:

`01_CANDIDATE_PATCHES/IMPORT_THIS_IN_TASKER_BUILD100_CANDIDATE.xml`

Reason:

The Stage 3A baseline recheck found:

- Final classification: FAILED
- Broken Tasker block nesting
- Config proof error carrying dirty state
- Missing Build100 cap variables

This older XML remains useful only as reference/history unless explicitly patched again.

## Current Phone Proof State

Stage 3A remains:

HOLD / NEED FINAL RUN LOG AND TRIGGER STATE VERIFICATION

Do not move to process-only, send dry-run, one-send, timer, or live-loop testing until cleanup proof is captured.
