# AIW Codex Build99 Patch83 Lean Runtime Load Failure Audit — 2026-07-03

## File audited
- File: `AIW_FINAL_BUILD99_PATCH83_LEAN_RUNTIME.xml`
- SHA256: `b98f748554d47173454f58a8c7d28fdc0dbf5e4d6676678d6b5606faea4e3d2e`
- Size: 1,479,884 bytes

## Static parse result
- XML parse: PASS
- TaskerData tv: `6.7.5-beta`
- Profiles: 4
- Tasks defined: 150
- Scenes: 2
- Projects: 1
- Duplicate task IDs: 0
- Duplicate task names: 0
- Missing Perform Task name refs: 0

## Hard import/load risks found

### 1. Project task registry references tasks that do not exist
- Project `<tids>` lists 194 task IDs.
- Only 150 `<Task>` definitions exist.
- Missing task definitions referenced by project: 60.
- This is a direct Tasker import/load risk because the project manifest points to task IDs not present in the XML.

### 2. Existing task definitions are not listed in the project registry
- 16 task definitions exist but are not included in project `<tids>`.
- These include dashboard/control task IDs:
  - 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 414, 415, 417, 418
- This can cause imported tasks/buttons to be missing or orphaned.

### 3. Scene button references a missing task
- Scene: `AIW COMMAND CENTER P82`
- Missing clickTask: `413`
- Occurrences: 2
- Button label: `TEST SEND 1`
- There is no task ID 413 in the file.
- This matches the earlier Patch80-style dashboard/import failure pattern: scene button exists but action target is missing.

### 4. This file is not a clean Patch83 runtime
- Expected Patch83 runtime from prior audit: 204 tasks, clean static audit, Patch83 send-wait stabilizer only.
- This file has 150 tasks.
- Project name says: `AI WORKER BUILD95 PROCESS DIRECT SHEET1 QUEUE SOURCE`.
- Dashboard text says: `BUILD95 LOCKED | AUTONOMOUS LIVE | DASHBOARD P82`.
- The file contains 0 plain-text `PATCH83` markers.
- Therefore this is a mixed Build95/autonomous/dashboard file, not a faithful Patch83 lean runtime.

### 5. Autonomous/timer path was changed from the known safe Patch83 test path
- Timer profile `FINAL-Z-WOKER Every 2m Tick` points to task ID 424.
- Task 424 is `AIW AUTO LIVE TICK V1`.
- Prior known Patch83 proof target was one controlled send proof, not an autonomous live/timer build.
- This means Codex changed the next gate from controlled Patch83 proof into an autonomous live path.

### 6. Text encoding is corrupted / mojibake is present
- `Ãƒ` occurrences: 775
- Corrupted separator examples appear where `§` should be.
- Dashboard text also contains corrupted bullet characters in `AUTONOMOUS LIVE ... RUNS UNTIL STOPPED`.
- This can break AutoSheets separators, labels, and plugin parameter readability.

### 7. File contains a private OpenAI key assignment
- Task `APP Set OpenAI Key LOCAL ONLY` contains a key assignment.
- The key is not repeated in this audit report.
- This file should be treated as WITH_KEY/private only.

## Verdict
This file should not be imported as the next AI Worker runtime.

## Why it likely did not load properly
The strongest direct causes are:
1. Project `<tids>` references 60 task IDs that do not exist in the file.
2. Scene `TEST SEND 1` points to missing task ID 413.
3. Dashboard/control task definitions exist outside the project task registry.
4. The XML is a mixed/leaned Build95 autonomous dashboard file, not the known Patch83 runtime.
5. The file has widespread mojibake encoding corruption in separators and labels.

## Fact-based recommendation
Do not use this Codex Build99 runtime.

Return Codex to source-side validation only:
- do not edit XML
- do not generate lean runtime
- do not promote autonomous live mode
- build validators only
- preserve the verified Patch83 runtime as test candidate

Next runtime candidate remains:
- `83_AIW_SEND_WAIT_MICRO_STABILIZER_RUNTIME.xml`
- Prior verified SHA: `f5ae33fee530ab0f32770c3b27a1b54b715046ed6258a0673865bec88103db91`
- Prior static audit: PASS
- Next needed proof: one controlled send proof on Moto Razr 2024
