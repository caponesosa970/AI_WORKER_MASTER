# AI Worker Build Mistake Prevention Rules

Updated: 2026-07-06

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT

Purpose:

Make known Build100 mistakes visible before Codex builds, packages, or recommends phone testing.

## Core Rule

Every repeated failure must become a written prevention rule in the repo.

Codex must read these files before every future build or package:

1. `ISSUE_HISTORY_REGISTER.md`
2. `BUILD_MISTAKE_PREVENTION_RULES.md`
3. `FAILED_PACKAGES_LEDGER.md`

Codex must then state:

- active prevention rules that apply to the current patch,
- prior failed packages that must not be reused,
- current approved baseline/source file,
- whether the requested patch repeats a known failed pattern.

If the source baseline is unclear, Codex must refuse to build.

## Permanent Rule: Tasker Importability Is A First-Class Gate

Static XML parse PASS is not enough.

A runtime patch package must include a full Tasker-importable phone XML lane:

`PHONE_IMPORT_XML/full_importable_xml/`

A redacted XML can be included only as ChatGPT audit evidence:

`CHATGPT_AUDIT_XML/redacted_for_audit/`

Redacted XML must be labeled:

`NOT_FOR_TASKER_IMPORT`

If Tasker rejects the phone-import XML:

- classify `FAILED / TASKER IMPORT REJECTED`,
- do not continue from rejected XML,
- do not request more phone testing from rejected XML,
- rebuild from the last Tasker-accepted XML only.

## Runtime Package Minimum Preflight

Every runtime XML package must prove:

- full import XML parse PASS,
- redacted audit XML parse PASS if included,
- root `TaskerData`,
- task count/profile count/scene count reported,
- duplicate task IDs `0`,
- duplicate task names `0`,
- missing project refs `0`,
- missing profile refs `0`,
- missing Perform Task refs `0`,
- missing scene clickTask refs `0`,
- Tasker block nesting issues `0`,
- duplicate action `sr` `0`,
- abnormal action index gaps checked/reported,
- `json:true` count `0`,
- `<se>true</se>` count `0`,
- `LIVE_OPEN` count `0`,
- changed task list compared to approved baseline,
- forbidden path scan PASS,
- SHA256 inventory,
- README naming which XML is for phone import,
- phone import checklist.

## Known Prevention Rules

### PREVENT-TASKER-IMPORT-001

Tasker import rejection blocks the build.

Do not treat parser-valid XML as import-proven XML.

Required check:

- package contains a full non-redacted phone-import XML,
- README names the phone-import XML,
- Tasker-safe formatting checks pass,
- ChatGPT audits before Moto import.

### PREVENT-REDACTED-IMPORT-001

Redacted XML is never for phone import.

Required check:

- redacted XML path includes `CHATGPT_AUDIT_XML`,
- redacted XML name or README says `NOT_FOR_TASKER_IMPORT`,
- phone-import lane is present for runtime packages.

### PREVENT-SEARCH-FORMAT-001

Phone-like TextNow search keys must normalize to digits-only in the proven send UI lane unless a contact-name path is specifically being tested.

Required check:

- raw search key logged,
- normalized search key logged,
- TextNow search uses normalized value.

### PREVENT-DIRTY-UI-001

Dry-run paste can leave dirty UI.

Required check:

- dry-run paste logs `DIRTY_UI_REQUIRES_MANUAL_CLEAR` if text remains,
- no send-capable task runs while dirty UI marker is active,
- controlled send tests verify the message box is clear before composing.

### PREVENT-GROUPC-UNSAFE-001

`SS Controlled One-Row Send Proof` cannot be narrowly patched for Group C until ChatGPT approves a safer route.

Required check:

- approved-recipient guard exists,
- row sender/ticker comparison exists,
- TextNow thread/header confirmation exists before send,
- exact reply paste proof exists,
- Send is pressed once,
- independent send proof exists before DONE,
- uncertain state becomes `ERROR_SEND_REVIEW`,
- no automatic retry after uncertainty.

## After Every Failed Package

Codex must:

1. Add the package to `FAILED_PACKAGES_LEDGER.md`.
2. Add or update an issue in `ISSUE_HISTORY_REGISTER.md`.
3. Add a prevention rule if the failure can repeat.
4. Mark the exact missing proof or failed gate.
5. Classify the failure type:
   - static XML failure,
   - Tasker import failure,
   - phone runtime failure,
   - test setup failure,
   - source-truth/history failure,
   - packaging/reporting failure.
