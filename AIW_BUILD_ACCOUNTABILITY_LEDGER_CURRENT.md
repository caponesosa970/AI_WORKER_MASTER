# AI Worker Build Accountability Ledger Current

Status: ACTIVE BUILD GATE
Updated: 2026-07-12T17:43:24-07:00

This ledger is mandatory for all AI Worker work. A build, audit, repository sync, phone-test request, or release review is incomplete until its claims are recorded here and mapped to proof in `AIW_CLAIM_TO_PROOF_MATRIX_CURRENT.md`.

## Enforcement Rule

No Codex output may be accepted when it lacks:

- preflight result
- relevant bug-history search
- exact source SHA
- exact changed-file list
- exact changed-task/action list
- claim-to-proof mapping
- historical regression results
- unsupported-claim disclosure
- phone-proof limitations
- tracker decision
- Codex responsibility statement
- ChatGPT verification checklist

## Current Build Entry

### Accountability ID

AIW-ACC-20260712-27B-AUTOINPUT-PRESERVATION

### Date/Time

2026-07-12T17:43:24-07:00

### Gate

Gate 9 send-adjacent / 27B controlled one-send candidate remains HOLD.

### Issue

ISSUE_27B_AUTOINPUT_TARGET_NOT_V15A_PRESERVED

### Exact Task Assigned

Install a permanent AI Worker Build Accountability System. No Tasker runtime repair, AutoInput repair, phone test, Sheet edit, tracker percentage change, or gate advancement is authorized.

### Exact Source Files

| Source file | Source role | SHA256 |
|---|---|---|
| `AGENTS.md` | existing project instruction source | `68E303EBD536BFF8D222843C14EEE56DE63C5C0CB4548680EDD19AEA91D93A37` |
| `.codex/config.toml` | existing Codex project config | `3AA069D13219CE5B19F7CB3DF0D22BFB48432C3EF48E290D017D837484383E72` |
| `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md` | existing controller tracker | `E03842CBC1F763FB56FD5B649D5F0E87E9AA3175DBCF0D7E769A5BBB01E3CFB9` |
| `02_TEST_LOGS/27B_20260710/AIW_CODEX_ACCOUNTABILITY_REPORT.md` | 27B accountability claim source | `EBAFE4AC421473B40A18C86E0522DD2187073F8D307E20AD454723D1834A50A9` |
| `02_TEST_LOGS/27B_20260710/V15A_AUTOINPUT_PRESERVATION_REPORT.md` | 27B preservation claim source | `23AFAF6A469428DE39259576BFF4905EFDFEC7D8CF73DB6102C54EDEF0F1E94E` |
| `02_TEST_LOGS/27B_20260710/V15A_AUTOINPUT_DIFF_TABLE.csv` | 27B generated comparison source | `8DD462194C50B397F9FA67901C0A7C82E22C1547CD339D422D3BEFB2AA0143B0` |

V15A source SHA remains:

`C4CDEAA0BFD78120386FF1B03FA0A2D6B13BCEEDBD15687F84D03A3AD5FEF1C8`

27B package ZIP SHA remains:

`28A859D8B5D2ADF07CC2D608D382136CADC94D9E03D97808D72B87A0E6133FD5`

### Current Branch

`controls/full-build-accountability`

### Starting Commit

`0e9d8f8a7f08c46265f3fcb16f162fd73ccfef50`

### Codex Mode

Repository control/documentation only.

### Approved Actions

- Create accountability ledgers.
- Update AGENTS.md with the mandatory accountability gate.
- Add accountability fallback documents to `.codex/config.toml`.
- Update controller tracker with the active issue and accountability-installation state.
- Commit documentation/control changes.
- Open PR into `main`.

### Prohibited Actions

- No runtime XML change.
- No Tasker action change.
- No AutoInput repair.
- No Sheet edit.
- No phone test.
- No tracker percentage change.
- No Send, DONE, Archive, live, capacity, or release unlock.

### Files Touched

Expected touched files for this accountability install:

- `AIW_BUILD_ACCOUNTABILITY_LEDGER_CURRENT.md`
- `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`
- `AIW_CLAIM_TO_PROOF_MATRIX_CURRENT.md`
- `AIW_MANDATORY_BUILD_PREFLIGHT.md`
- `AGENTS.md`
- `.codex/config.toml`
- `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`

### Runtime Tasks Touched

None.

### Exact Actions Touched

None. No Tasker runtime action is authorized or changed by this accountability install.

### Claims Made

| Claim | Required proof | Current status |
|---|---|---|
| Accountability gate installed | Files exist and are committed in PR | PENDING PR AUDIT |
| Current 27B issue recorded | Issue appears in tracker and failure ledger | PENDING PR AUDIT |
| Tracker percentage unchanged | Tracker still says `8/14 locked = 57%` | PENDING PR AUDIT |
| Runtime untouched | Git changed-file list contains no runtime XML behavior edits | PENDING PR AUDIT |

### Proof Supporting Each Claim

Proof must come from:

- git diff and changed-file list
- direct file inspection
- SHA values where relevant
- ChatGPT PR audit

### Proof Not Available

- Phone-visible AutoInput fields for 27B SEARCH_ICON are not proven by this repository change.
- Raw full 27B runlog is not present in this public-safe repo state.
- No new phone proof is claimed.

### Known Assumptions

- Row 75 has been reset by Sosa/ChatGPT to `TEST_STAGED_NO_SEND`; this ledger records the controller statement only and does not edit or verify the live Sheet.
- The current issue is based on user-supplied phone proof and controller instruction.

### Contradictions Found

27B reports claimed v15a AutoInput preservation from a static generated diff table. Phone proof later contradicted that by showing SEARCH_ICON was not the expected Sosa-created AutoInput setup and failed safely before send.

### Regression Checks Required

Every future build must check:

- false-pass after errored AutoInput action
- unsupported PRESERVED claim
- static report accepted without phone-visible field evidence
- generated CSV used as its own proof
- Tasker phone proof superseding static XML/report evidence
- wrong-recipient, stale-reply, duplicate-send, DONE-before-send, and lock-release regressions

### Regression Results

Current accountability install adds the regression checks. It does not close the 27B issue.

### Phone Proof Required

No phone proof is authorized for this PR.

Future AutoInput preservation repair must include phone-visible field proof or Sosa-created exported action proof before the claim may be marked PROVEN.

### Phone Proof Received

For this accountability PR: none.

For current issue: phone proof reported SEARCH_ICON failure and safe no-send stop.

### Final Controller Decision

Pending ChatGPT audit of accountability PR.

### Tracker Effect

No percentage change. Current tracker remains `8/14 locked = 57%`.

### Responsible Party For Each Failure

| Failure | Codex responsibility | ChatGPT/controller responsibility | User/operator responsibility |
|---|---|---|---|
| 27B PRESERVED claim unsupported | Claimed v15a preservation from generated static table without sufficient independent field-level proof | Accepted phone test from summary/static comparison without independently validating phone-visible AutoInput fields | Provided phone proof that exposed the defect; no operator fault recorded |

### Prevention Rule Added

A PRESERVED claim is forbidden unless source and output values are shown field-by-field and validated by a second independent parser/check. Static XML parse and generated CSV output cannot prove Tasker rendering or phone behavior.
