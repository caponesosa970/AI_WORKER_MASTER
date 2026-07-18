# AI Worker Failure and Regression Ledger

Status: CURRENT ACTIVE FAILURES AND PERMANENT REGRESSIONS

Every active failure remains open until it has a bounded repair, regression proof, and ChatGPT-reviewed closing proof.

Static audit cannot close a phone/runtime issue by itself.

## Active Failures

### ISSUE_CONTROL_SOURCE_TRUTH_DUPLICATION_LOOP

Status: `OPEN / HOLD UNTIL CLEANUP PR MERGED`

Root cause:

Too many active root controller files repeated the same tracker, blocker, proof, merge, phone, Codex, and safety rules. A correction in one file required copying the same correction into multiple files. Small wording differences then created contradictions and additional documentation runs.

Required repair:

Consolidate active root source truth into exactly four files:

- `AGENTS.md`
- `AIW_FULL_GOAL_EXECUTION_CONTRACT_CURRENT.md`
- `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`
- `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`

Required regression:

- only four retained files modified;
- five redundant root control files deleted;
- no new control file, ledger, matrix, preflight file, report directory, or replacement framework;
- no runtime/private/script/phone/Sheet/TextNow/profile/scene/package changes;
- deleted files are not referenced as mandatory active sources;
- only project controller state contains the active tracker and current blocker;
- permanent full goal remains in the execution contract;
- system-wide compatibility and proof rules remain in AGENTS;
- active failures and permanent regression rules remain in this ledger.

Closing proof:

Cleanup PR is independently audited, merged into main, and verified on main.

Prevention rule:

Do not create new active controller documents when the four retained files can carry the required source truth.

### ISSUE_GATE14_DATASOURCE_AUTHORITY_MISMATCH

Status: `OPEN / RUNTIME HOLD`

Root cause:

The Gate 14 Phase A fixture writer and validator used different workbook authorities.

Direct static evidence:

- Task 329 wrote the fixture under staging-workbook authority.
- Task 328 invoked Task 325.
- Task 325 read under production-workbook authority.
- The validator could not read the exact fixture Task 329 wrote.

Phone-proof classification:

No phone execution proved this datasource defect.

Required repair:

Run 2 must return directly to a bounded Datasource R1 or successor runtime artifact path that resolves datasource authority without changing unrelated runtime behavior.

Required regression:

- exact full-project baseline and SHA;
- exact changed-node map;
- upstream/downstream contract map;
- actual workbook authority separation in tests;
- full reachable call graph for affected path;
- state-transition impact;
- protected-node proof;
- application-wide regression plan;
- forbidden-path proof;
- zero Send/TextNow/OpenAI/DONE/Archive/Profile enablement from validation-only path;
- independent ChatGPT artifact approval before phone import.

Closing proof:

Approved runtime artifact passes static and simulated validation, then receives required phone proof under ChatGPT control.

Prevention rule:

Never collapse separate workbook IDs or datasource authorities into one abstract store during simulation or validation.

## Permanent Regression Requirements

| Issue / class | Status | Permanent prevention rule | Must check in |
| --- | --- | --- | --- |
| Static/package proof is not phone proof | PERMANENT | Do not approve phone-visible behavior from Codex summaries, XML parse, generated CSV, simulator, or static report alone. | Every phone-test request and release claim |
| Phone proof supersedes static audit | PERMANENT | When phone proof contradicts static claims, update source truth before further repair. | Every runtime failure triage |
| Generated reports can be incomplete | PERMANENT | A generated report cannot prove its own correctness; use independent verification. | Every artifact audit |
| Encoding/mojibake drift | PERMANENT | Preserve Tasker XML encoding and unchanged regions; reject special-character drift. | Every runtime XML build |
| Wrong-recipient Send | PERMANENT | Prove exact recipient/thread before compose or Send. | Every Send-capable artifact |
| Stale reply Send | PERMANENT | Prove row, ID, sender, message, reply, and status binding before Send. | Every processing and Send artifact |
| Duplicate Send | PERMANENT | Check prior send-attempt and sent state before any reset; no retry after uncertainty. | Every Send/recovery artifact |
| DONE before confirmation | PERMANENT | DONE requires independent confirmation, never Send-click evidence alone. | Every confirmation/DONE artifact |
| Archive before exact proof | PERMANENT | Archive requires confirmed completion, exact copy/readback, uniqueness, and safe source clear. | Every Archive artifact |
| Lock release defect | PERMANENT | Every owned terminal path releases exactly once; no unowned release. | Every lock/recovery artifact |
| AutoInput target drift | PERMANENT | No guessed AutoInput target; preserve and prove phone-visible fields. | Every TextNow/AutoInput artifact |
| Credential drift | PERMANENT | Verify current credential source privately without printing or committing values. | Every private package |
| AutoSheets timeout after lock | PERMANENT | Bound retries and release/close locks on final failure before TextNow. | Every Sheet-read-before-Send path |
| Lifecycle ordering | PERMANENT | One lifecycle transition per cycle; unresolved Send states block new Send selection. | Every queue-cycle artifact |
| STOP/profile safety | PERMANENT | STOP prevents new work and leaves runtime profiles disabled; no silent profile enablement. | Every STOP/recovery/runtime artifact |
| Gate 9 controlled Send | LOCKED | Do not rerun or reopen without newer contradictory phone proof. | Gate 14 regression audit |
| Gate 10 independent confirmation and DONE | LOCKED | Preserve confirmation separate from Send and DONE only after confirmation. | Gate 14 regression audit |
| Gate 11 exact-row Archive | LOCKED | Preserve exact-row Archive and source-clear boundaries. | Gate 14 regression audit |
| Gate 12 queue lifecycle | LOCKED | Preserve one lifecycle transition per cycle. | Gate 14 regression audit |
| Gate 13 timer, STOP, background guard, recovery | LOCKED | Preserve STOP, busy overlap, screen-off, timer, and recovery behavior. | Gate 14 regression audit |
