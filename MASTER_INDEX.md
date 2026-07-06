# AI Worker Master Index

Updated: 2026-07-06

This folder is the clean working root for AI Worker Build100 work.

## Folder Map

- `00_LOCKED_SOURCE/`: locked source references and raw source packages. Do not replace these without phone proof and release approval.
- `01_CANDIDATE_PATCHES/`: active Build100 candidate XMLs and narrow patch work.
- `02_TEST_LOGS/`: static audits, validation reports, SHA256 inventories, HOLD lists, proof-ledger inputs, and generated ledgers.
- `03_PHONE_PROOF/`: Moto Razr 2024 runlogs, screenshots, ChatGPT audit results, and phone-proof packages.
- `04_RELEASE_PACKAGES/`: candidate and audit ZIP packages for ChatGPT handoff.
- `docs/`: source and candidate documentation.
- `scripts/`: Build100 generation, patch, audit, and verification scripts.
- `PRIVATE_WITH_KEY/`: private key-bearing runtime references. Do not print secrets from here.

## Required Ledgers

- `MASTER_PLAN_CURRENT.md`: current active workflow plan and supersession rule.
- `PROOF_LEDGER.md`: file-backed proof map by layer.
- `CURRENT_BUILD_STATUS.md`: current Build100 status and next gate.
- `FROZEN_LOGIC_REGISTER.md`: logic that must not be patched unless directly touched by a new approved scope.
- `FAILED_PACKAGES_LEDGER.md`: failed, rejected, or hard-held packages that must not be reused.
- `PATCH_SCOPE_REGISTER.md`: allowed and forbidden patch areas.
- `MISSING_PROOF_REGISTER.md`: exact missing proof files or proof classes.
- `NEXT_GROUPED_PATCH_PLAN.md`: next safe grouped patch/test sequence.
- `RELEASE_DEPENDENCY_GRAPH.md`: dependency order from current state to Release Candidate 1.
- `RELEASE_BLOCKER_REGISTER.md`: active blockers by subsystem.
- `PHONE_PROOF_SEQUENCE.md`: one-layer phone proof order.
- `SPEED_TUNING_REGISTER.md`: timing markers to collect before tuning.
- `TONIGHT_COMPLETION_PLAN.md`: current short-run completion plan.
- `ISSUE_HISTORY_REGISTER.md`: issue history with proof, root cause, prevention rule, preflight, status, and next validation.
- `BUILD_MISTAKE_PREVENTION_RULES.md`: mandatory pre-build mistake-prevention rules.

## Mandatory Pre-Build Read Order

Before every future build or package, Codex must read:

1. `ISSUE_HISTORY_REGISTER.md`
2. `BUILD_MISTAKE_PREVENTION_RULES.md`
3. `FAILED_PACKAGES_LEDGER.md`

Codex must state:

- active prevention rules that apply,
- prior failed packages that must not be reused,
- current approved baseline/source file,
- whether the requested patch repeats a known failed pattern.

## Current Status

Overall Build100 remains:

`CANDIDATE / HOLD`

Layer status:

- Stage1 Stop / Safe / Reset / Status: file-backed phone evidence exists, but remains `CANDIDATE` because the report itself kept full stage status on HOLD.
- Stage2 dashboard STATUS: screenshot-backed runtime proof exists, but remains `CANDIDATE` pending independent audit/runlog if required.
- Stage3A trigger marker: `CANDIDATE`; trigger-marker capture passed, but final stage advancement depended on closeout.
- Stage3A final safe-state closeout: `LOCKED` for closeout layer only, per ChatGPT audit.
- Stage4A process-only no-work guard: `LOCKED` for process-only no-work guard layer only, per runlog audit.
- Stage4B no-ready dry-run hold: `LOCKED` for no-ready hold behavior only, per runlog audit.
- Stage4B formatted-number contact/search dry-run before normalization: `FAILED / DATA FORMAT CONTACT_PICK FAILURE`; use as evidence only.
- Stage4B digits-only contact/search dry-run: `LOCKED` for contact-pick/no-send layer only.
- Group B2 Send UI Dry Run: `LOCKED` for formatted search normalization, thread open, message box detection, dry-run paste, `SEND=NO`, `%SSSentOne=0`, dirty UI marker, and lock release.
- Group C Controlled One-Send: `HARD HOLD` for narrow patching of `SS Controlled One-Row Send Proof` until ChatGPT approves a safer implementation route.
- Timer/live, archive/deadarchive/compactor/TT5, and 50-contact capacity: `HOLD`.

## Current Runtime Candidate

- Current private runtime source: `PRIVATE_WITH_KEY/runtime_xml/10C_TASKER_IMPORT_XML__AIW_BUILD100_GROUP_B2_SEND_UI_DRYRUN_WITH_KEY_TASKER_SAFE_20260706.xml`
- XML SHA256: `5E6ACEC6AAADE464A3F19E9750A80E3B33CD3CDB97E5085B965429461ECF527F`
- Static status: XML parse PASS, 215 tasks, 4 profiles, 2 scenes, missing refs 0, duplicate IDs/names 0, block nesting issues 0, duplicate action `sr` 0, `json:true` 0, `<se>true</se>` 0.
- Current ChatGPT handoff ZIP: `C:\Users\Shadow\Downloads\ai work\Codex to ChatGPT\13_CHATGPT_AUDIT_ZIP__AIW_BUILD100_GROUP_C_RUNTIME_PATCH_20260706.zip`
- Current ChatGPT handoff SHA256: `D7D21E9F25A55BA6685D58495EFE39D86B71324FC9C6D17CB227B8CCC0C7A83A`

## Supersession Rule

Older import, contact-pick, SEARCH_ICON, Stage4A, and ledger handoff packages are historical evidence/source history only.

Do not use them as the active workflow plan unless a newer ChatGPT audit explicitly restores them.

Technical truth remains in runtime XML, static audits, phone runlogs, screenshots, SHA256 inventories, `PROOF_LEDGER.md`, `FROZEN_LOGIC_REGISTER.md`, `FAILED_PACKAGES_LEDGER.md`, issue-history registers, and ChatGPT audit results.

## Git Note

Do not commit unless separately requested.
