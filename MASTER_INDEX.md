# AI Worker Master Index

Updated: 2026-07-05

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

- `PROOF_LEDGER.md`: file-backed proof map by layer.
- `CURRENT_BUILD_STATUS.md`: current Build100 status and next gate.
- `FROZEN_LOGIC_REGISTER.md`: logic that must not be patched unless directly touched by a new approved scope.
- `FAILED_PACKAGES_LEDGER.md`: failed or rejected packages that must not be reused.
- `PATCH_SCOPE_REGISTER.md`: allowed and forbidden patch areas.
- `MISSING_PROOF_REGISTER.md`: exact missing proof files or proof classes.
- `NEXT_GROUPED_PATCH_PLAN.md`: next safe grouped patch/test sequence.

## Current Status

Overall Build100 remains:

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

Layer status:

- Stage1 Stop / Safe / Reset / Status: file-backed phone evidence exists, but remains `CANDIDATE` because the report itself kept full stage status on HOLD.
- Stage2 dashboard STATUS: screenshot-backed runtime proof exists, but remains `CANDIDATE` pending independent audit/runlog if required.
- Stage3A trigger marker: `CANDIDATE`; trigger-marker capture passed, but final stage advancement depended on closeout.
- Stage3A final safe-state closeout: `LOCKED` for closeout layer only, per ChatGPT audit.
- Stage4A process-only no-work guard: `LOCKED` for process-only no-work guard layer only, per runlog audit.
- Stage4B no-ready dry-run hold: `LOCKED` for no-ready hold behavior only, per runlog audit.
- Stage4B contact/search dry-run: `FAILED / HOLD`; latest contact-pick/search path did not pass.
- Controlled one-send, timer/live, archive/deadarchive/compactor/TT5, and 50-contact capacity: `HOLD`.

## Current Runtime Candidate

- Current lane: Build100 Group B `SS Safe Send Dry-Run` around `SEARCH_ICON`, `SEARCH_FIELD`, and `CONTACT_PICK`.
- Current import-safe XML: `01_CANDIDATE_PATCHES/BUILD100_GROUP_B_SEARCH_ICON_IMPORT_SAFE/xml/AIW_BUILD100_GROUP_B_SEARCH_ICON_IMPORT_SAFE_FULL_TASKER_20260705.xml`
- XML SHA256: `55A4936C329A16DDD0DFA94003D52AB53887BBBEBE192045EEA6F9D38B6DE4CA`
- Static status: XML parse PASS, 215 tasks, 4 profiles, 2 scenes, missing refs 0, duplicate IDs/names 0, `json:true` 0, `<se>true</se>` 0.

## Git Note

This ledger update should be committed on branch `build100-phone-proof` after review of staged files. Use only ledger files and the proof-ledger input package unless intentionally adding other artifacts.
