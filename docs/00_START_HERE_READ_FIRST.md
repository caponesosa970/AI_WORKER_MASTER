# START HERE — AI Worker Full Project Control Package for Codex

STATUS:
CANDIDATE CONTROL PACKAGE / NOT A RUNTIME RELEASE

MISSION:
Use this package to build the next Tasker-importable AI Worker candidate:

`AIW_BUILD100_FULL_CONTROL_50_CONTACT_CAPPED_QUEUE_WITH_WATCHDOG_CANDIDATE.xml`

This is not queue-only. It is a full start-to-finish control system plan.

PRIMARY RULE:
The final runtime must be a clean Tasker XML export/import file. Do not convert the runtime into another format. Do not output snippets as the runtime.

SOURCE RULE:
Use the raw XML reference in:

`REFERENCE_RAW_DO_NOT_REFORMAT/AIW_BUILD99_PATCH83_IMPORT_SAFE_MINIMAL.xml`

Preserve it as Tasker XML. Preserve Tasker plugin bundles, variables, profiles, tasks, scenes, local settings, spreadsheet IDs, and WITH_KEY/private data inside the XML.

REPORT RULE:
Do not print secrets in markdown reports. Preserve them inside the WITH_KEY XML.

OUTPUT RULE:
Codex must return ONE ZIP containing:
1. Full Tasker XML candidate.
2. Static XML audit.
3. Task/action change report.
4. SHA256 inventory.
5. Runtime safeguard map.
6. Phone proof checklist.
7. HOLD list.
8. Failure/regression ledger.
9. Promotion/release gate report.

FINAL STATUS MUST BE:
CANDIDATE / HOLD FOR PHONE PROOF
