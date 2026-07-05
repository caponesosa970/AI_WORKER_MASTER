# AI Worker Proof Ledger Rebuild Seed — 2026-07-05

STATUS:
CANDIDATE / HOLD FOR CODEX REPO DISCOVERY

PURPOSE:
This file is a controlled seed for Codex. It is not the final proof ledger.
Codex must use the GitHub repo, current XML, old handoff files, old proof reports, runlogs, screenshots, SHA files, and current audits to build the real ledger.

HARD RULE:
Do not invent proof. If a proof file is missing, mark that item HARD HOLD and name the exact missing file.

WHY THIS EXISTS:
The project has older proven layers from before Codex. Those proofs are not cleanly tied into the current Build100/Codex package, which is causing repeated retesting and confusion.

CURRENT KNOWN CONTEXT:
- Current lane is Build100 Group B SEARCH_ICON / SS Safe Send Dry-Run.
- Current imported XML was accepted by Tasker according to user report.
- Latest runlog did not exercise SEARCH_ICON because it stopped at NO_READY.
- Earlier Group B dry-run reached READY_TO_SEND and failed at SEARCH_ICON, then fail-closed.
- Build100 static audit reported 215 tasks, 4 profiles, 2 scenes, zero missing refs, zero block issues, but HOLD because no runlog artifact was found for that package.
- Build100 deep audit reported one-send rule as partial static evidence and said live TextNow UI behavior still requires phone proof.
- Proof logger exists but first-write AutoSheets errors require runlog/phone proof interpretation.

LOCKED FROM CURRENT FILES ONLY:
- Current SS Safe Send Dry-Run NO_READY path stopped safely when no READY_TO_SEND row existed.
- Earlier SS Safe Send Dry-Run reached a READY_TO_SEND row and failed closed at SEARCH_ICON.
- Build100 XML static structure, as reported in deep audit, had XML parse PASS, task count 215, profile count 4, scene count 2, missing refs 0, duplicate task names 0, duplicate task IDs 0, and block issues 0.

HISTORICAL / NEEDS REPO PROOF:
These were proven before Codex according to project context, but Codex must find the exact proof files or mark HARD HOLD:
- Simple logging worked.
- Process Sheet worked.
- Send Sheet manual/TextNow movement worked.
- TextNow search/open/type/send actions worked before.
- Search icon sometimes required double tap / extra handling.
- AI Worker Tick worked.
- Time Profile ran every 2 minutes.
- Archive Done Rows manual growing-list copy + clear worked.
- Archive was not connected to live loop.
- Dashboard/Legacy dashboard buttons opened/worked/closed.
- Bottom Send self-loop stayed OFF.
- Call notification filtering and duplicate protection had prior checkpoints.
- JSON guard / Structure Output OFF had recurring risk and must be checked per package.

CURRENT CANDIDATE:
- Build100 Group B SS Safe Send Dry-Run
- SEARCH_ICON / SEARCH_FIELD / CONTACT_PICK dry-run path
- Import-safe XML package
- Current proof logger/history controls

CURRENT HOLD:
- SEARCH_ICON success on phone after latest import-safe XML
- SEARCH_FIELD success
- CONTACT_PICK success
- SEND=NO
- %SSSentOne=0
- no TextNow message box touched
- no send button touched
- FINAL Send Sheet not run
- live/autonomous
- timer/live send
- archive/deadarchive/compactor/TT5
- multi-send
- capacity testing

FAILED / DO NOT REUSE:
- The 200-task private/reference XML as a phone-test XML.
- Failed SEARCH_ICON package with broken Tasker block nesting.
- Tasker import rejected XML package.
- Latest NO_READY runlog as SEARCH_ICON proof.
- Any package that fails static gates or lacks phone proof for changed runtime behavior.

FILES CODEX MUST LOOK FOR:
1. AI_Worker_Handoff_Current_2026-05-19.txt
2. OLD_AI_WORKER_CHAT_REFERENCE.txt
3. runlog (5).txt
4. runlog (16).txt
5. AIW_ERROR_PROTECTION_PRE_RESPONSE_LOCK_V1.txt
6. old full build plan before Codex
7. old proof tracker / master project tracker
8. old Simple logging runlogs/screenshots
9. old Process Sheet runlogs/screenshots
10. old Send Sheet / manual TextNow send runlogs/screenshots
11. old double-tap/search-icon proof notes/screenshots
12. old AI Worker Tick proof runlogs
13. old Time Profile proof runlogs/screenshots
14. old Archive manual copy+clear proof files
15. dashboard/P81/P82 proof screenshots/reports
16. locked source ZIP/XML files tied to those proofs
17. SHA256 files or audit reports tied to those packages

REQUIRED OUTPUT FILES TO CREATE OR UPDATE:
1. MASTER_INDEX.md
2. PROOF_LEDGER.md
3. CURRENT_BUILD_STATUS.md
4. FROZEN_LOGIC_REGISTER.md
5. FAILED_PACKAGES_LEDGER.md
6. PATCH_SCOPE_REGISTER.md
7. MISSING_PROOF_REGISTER.md
8. NEXT_GROUPED_PATCH_PLAN.md

REQUIRED LEDGER FIELDS FOR EVERY PROOF:
- proof_id
- layer
- task/profile/scene name
- source package/file
- source SHA256 if known
- proof file name
- proof type: phone runlog, screenshot, XML static audit, manual phone proof, handoff reference, memory reference
- pass condition
- actual observed result
- current XML applicability: YES / NO / UNKNOWN
- carry-forward decision: LOCKED / CANDIDATE / HOLD / FAILED
- reason
- exact missing proof if any

CARRY-FORWARD RULE:
A proof can be carried forward only if:
1. proof file exists,
2. task/profile/scene identity matches,
3. source package or SHA chain is known,
4. relevant logic is unchanged in current XML,
5. no later failed patch replaced that logic.

If any of those are missing, do not lock it. Mark HOLD or HARD HOLD.

GROUPED PATCH RULE:
After ledger rebuild, Codex may propose grouped patch sets only for independent bugs that:
- are in the same layer,
- have separate pass/fail checks,
- do not touch frozen working logic,
- can be tested by one controlled phone proof sequence.

Unsafe to group:
- real send + timer + archive + live
- UI patch + process logic patch
- source cleanup + runtime XML logic changes
- proof logger change + send action change unless explicitly approved

SAFE GROUP CANDIDATE EXAMPLES:
- proof ledger + index + failed package register
- static hygiene + SHA inventory + missing proof register
- SEARCH_ICON selector fallback + bounded wait + fail-closed marker inside SS Safe Send Dry-Run only
- proof logging questions/reporting only, no runtime behavior changes

DO NOT:
- do not change runtime XML while building the ledger
- do not claim phone proof
- do not mark old memory as locked proof unless file-backed
- do not reuse failed packages
- do not enable START/timer/live/archive/deadarchive/compactor/TT5/multi-send
- do not print API keys/secrets
