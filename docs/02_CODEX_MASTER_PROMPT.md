# CODEX MASTER PROMPT — AI Worker Build100 Full Project Control Runtime

Build the next AI Worker candidate from the raw Tasker XML reference.

SOURCE:
`REFERENCE_RAW_DO_NOT_REFORMAT/AIW_BUILD99_PATCH83_IMPORT_SAFE_MINIMAL.xml`

TARGET:
`AIW_BUILD100_FULL_CONTROL_50_CONTACT_CAPPED_QUEUE_WITH_WATCHDOG_CANDIDATE.xml`

STATUS:
CANDIDATE / HOLD FOR PHONE PROOF

## Non-negotiable runtime rules

1. Output must be full Tasker XML.
2. XML must import into Tasker.
3. Do not convert XML to JSON/YAML/markdown.
4. Do not output snippets as runtime.
5. Do not strip plugin bundles.
6. Do not strip private/local data from the WITH_KEY XML.
7. Do not print secrets in reports.
8. Preserve OpenAI key task/local variables/spreadsheet IDs inside XML.
9. Do not enable Archive/Compactor/TT5/DeadArchive live paths.
10. Do not claim phone proof.

## Required build systems

Create/verify the following systems:

1. Capture / inbound logger.
2. Queue writer.
3. Queue pressure reader.
4. Mode decision engine.
5. Batch processor.
6. One-send sender.
7. AIWProofLog.
8. SendLog.
9. HealthLog.
10. Watchdog.
11. Recovery.
12. Lightweight maintenance.
13. Dashboard.
14. Failure ledger.
15. Regression ledger.
16. Dependency registry.
17. System registry.
18. Validation engine.
19. Promotion engine.
20. Release controller.
21. HOLD controller.

## Required Build100 behavior

- 50 active contact cap.
- NORMAL mode processes up to 2 NEW rows.
- BACKLOG mode processes up to 5 NEW rows.
- Send max remains 1 READY_TO_SEND row per cycle.
- Start turns on TextNow trigger and timer together.
- Stop turns off TextNow trigger and timer.
- Timer route uses `AIW AUTO LIVE TICK V1`.
- All send paths keep 1000 ms wait after paste.
- Watchdog catches stale locks/stuck rows/trigger timer mismatch.
- Recovery never sends.
- Maintenance runs only when not blocking urgent sends.
- Dashboard labels must say Build100 candidate, not Build95.
- Every dashboard button must point to a real task.

## Required validation before output

Run static validation 100 passes or a single deterministic validator loop repeated 100 times.

Each pass checks:
- XML parse
- TaskerData root
- task count
- profile count
- scene count
- duplicate task IDs
- duplicate task names
- project task refs
- profile task refs
- scene clickTask refs
- Perform Task refs
- json:true count
- <se>true</se> count
- mojibake count
- Build95 label count
- Build100 label count
- 1000 ms waits
- private key marker present without printing key
- watchdog task exists
- recovery task exists
- validation engine exists
- failure ledger exists
- regression ledger exists

If any pass fails:
- do not claim ready
- output HOLD with exact failure list

## Required output ZIP

Return one ZIP with:
1. Build100 XML candidate.
2. Static audit report.
3. 100-pass validation report.
4. Task/action change report.
5. SHA256 inventory.
6. Runtime safeguard map.
7. Failure ledger.
8. Regression ledger.
9. Dependency registry.
10. System registry.
11. Phone proof checklist.
12. HOLD list.
