NON-AUTHORITATIVE HISTORICAL EVIDENCE
This file cannot authorize builds, phone tests, tracker changes, merges, live activation, or release.

# AI Worker Master Index

Updated: 2026-07-10

Status: HISTORICAL REPO SYNC SNAPSHOT / HOLD FOR CHATGPT AUDIT

This folder is the clean working root for AI Worker Build100 work.

## Historical Controller Source Snapshot

Read first:

- `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`
- `AGENTS.md`
- `.codex/config.toml`

## Historical Proof State Snapshot

8/14 locked = 57%.

Locked main gates:

1. Group B2 dry-run UI proof - LOCKED
2. Group C2 controlled one-send proof - LOCKED
3. Group D controller/timer-safe proof - LOCKED
4. Group E maintenance/recovery proof - LOCKED
5. Group F 22D trigger-only proof - LOCKED
6. Group F 22J trigger-to-queue proof - LOCKED
7. Group G process-only exact row proof - LOCKED
8. Controlled queue-cycle proof - LOCKED

Locked sub-proofs:

- Gate 9A non-UI send-readiness
- Gate 9B0 manual TextNow identity
- Gate 9B1A TextNow search-navigation
- Gate 9B1B manual thread identity
- Gate 9B1C no-send compose safety inspection
- Gate 9B1D manual compose-focus proof
- Gate 9B1E manual draft insert-and-clear proof
- Gate 9B1F exact reply compose dry-run
- 27B no-send guard proof

Historical paused gate:

- 27B controlled one-send rerun - HOLD

Blocked:

- Send
- DONE
- Archive
- DeadArchive
- Compactor
- TT5
- live/timer
- capacity
- release/production

## Historical Source Packages And Records

V15A source:

- `basefile_v15a_phone_send_cleanup_pass.xml`
- Private source reference: Private Drive source - link and ID retained outside the public repository.
- SHA256: `C4CDEAA0BFD78120386FF1B03FA0A2D6B13BCEEDBD15687F84D03A3AD5FEF1C8`

27B candidate:

- ZIP: `27B_CHATGPT_AUDIT_ZIP__AIW_BUILD100_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE_20260710.zip`
- ZIP private source reference: Private Drive source - link and ID retained outside the public repository.
- SHA sidecar: `27B_SHA256__AIW_BUILD100_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE_20260710.txt`
- SHA sidecar private source reference: Private Drive source - link and ID retained outside the public repository.
- ZIP SHA256: `28A859D8B5D2ADF07CC2D608D382136CADC94D9E03D97808D72B87A0E6133FD5`

## Folder Map

- `00_LOCKED_SOURCE/`: locked source references and raw source packages.
- `01_CANDIDATE_PATCHES/`: historical Build100 candidate XMLs and narrow patch work.
- `02_TEST_LOGS/`: static audits, validation reports, SHA inventories, HOLD lists, sync reports, and generated ledgers.
- `03_PHONE_PROOF/`: Moto Razr runlogs, screenshots, phone-proof summaries, and phone-proof packages.
- `04_RELEASE_PACKAGES/`: candidate and audit package outputs for ChatGPT handoff.
- `docs/`: source and candidate documentation.
- `scripts/`: Build100 generation, patch, audit, and verification scripts.
- private key-bearing runtime reference folder: private key-bearing runtime references. Do not print secrets from here.

## Required Ledgers

- `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`: historical controller tracker.
- `archived historical Drive source map`: historical Drive source map.
- `docs/V15A_AUTOINPUT_PRESERVATION_RULE_20260710.md`: v15a preservation rule.
- `02_TEST_LOGS/GITHUB_SYNC_STATUS_20260710.md`: latest GitHub sync state.
- `FAILED_PACKAGES_LEDGER.md`: failed, rejected, or hard-held packages.
- `ISSUE_HISTORY_REGISTER.md`: issue history and prevention rules.
- `BUILD_MISTAKE_PREVENTION_RULES.md`: mandatory pre-build prevention rules.

## Historical Note

Older Stage 2, Stage 3A, Stage 4A, Stage 4B, Group B, and Group C handoff text remains historical evidence through Git history and older reports. It is not controller authority.

At the time, the controller state was `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`.
