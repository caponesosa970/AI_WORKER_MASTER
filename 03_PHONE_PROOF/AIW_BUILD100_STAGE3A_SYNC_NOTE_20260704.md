# AIW Build100 Stage 3A Sync Note - 2026-07-04

## Status

CANDIDATE / HOLD FOR PHONE PROOF

## Branch

Current project branch:

`build100-phone-proof`

Remote:

`origin`

## Pushed Commits

- `ee65a25` - Add Stage 3A same-device retry hold proof
- `b93fd95` - Add Stage 3A same-device retry audit prompt
- `8fc84fb` - Add Stage 3A cleanup proof checklist
- `b140247` - Add Stage 3A sync note
- `bcb1c15` - Add controlled-test Build100 source routing
- `2425307` - Preserve Tasker XML bytes in Git

## Controlled-Test XML In GitHub Branch

Current controlled-test XML:

`01_CANDIDATE_PATCHES/AIW_BUILD100_CONTROLLED_TEST_HOLD_FULL_TASKER.xml`

SHA256:

`99B2A1C8C9AE1FF3FF191F49ACA9245DAEA45A5FA08810EAE89D3DAB5BF18D7F`

Byte-preservation check:

- Git HEAD blob SHA256 matches working file SHA256.
- Git HEAD blob byte length matches working file byte length.
- `.gitattributes` now contains `*.xml -text` so Tasker XML is not line-ending-normalized by Git.

## Controlled-Test Release ZIP Verification

Release ZIP:

`04_RELEASE_PACKAGES/AIW_BUILD100_CONTROLLED_TEST_HOLD_CANDIDATE_20260704.zip`

ZIP SHA256:

`4393777CB373420862979A094263564B5BD06BE5E3940D36D697C34F453AAF39`

ZIP byte size:

`180890`

ZIP file count:

`8`

XML inside ZIP:

`AIW_BUILD100_CONTROLLED_TEST_HOLD_FULL_TASKER.xml`

XML SHA256 inside ZIP:

`99B2A1C8C9AE1FF3FF191F49ACA9245DAEA45A5FA08810EAE89D3DAB5BF18D7F`

## Local ZIP For ChatGPT Audit

ZIP file:

Original retry ZIP:

`03_PHONE_PROOF/AIW_BUILD100_STAGE3A_2NDLINE_SAME_DEVICE_RETRY_HOLD_20260704.zip`

Package SHA256:

`871DA73FCAA796295382E09A9030E6D04C4B6F7AAAD3D4DB85E357BD6B9AAD9F`

Updated Run Log captured ZIP:

`03_PHONE_PROOF/AIW_BUILD100_STAGE3A_2NDLINE_SAME_DEVICE_RETRY_RUNLOG_CAPTURED_HOLD_20260704.zip`

Updated package SHA256 and byte size:

Recorded outside the ZIP in:

`03_PHONE_PROOF/SHA256_STAGE3A_2NDLINE_SAME_DEVICE_RETRY_RUNLOG_CAPTURED_PACKAGE_20260704.csv`

Reason:

The ZIP cannot contain a note with its own final SHA256 without changing that SHA256.

Updated package file count:

`13`

This ZIP is superseded by the final runlog-included ZIP below.

Final runlog-included ZIP:

`03_PHONE_PROOF/AIW_BUILD100_STAGE3A_2NDLINE_SAME_DEVICE_RETRY_WITH_RUNLOG_HOLD_20260705.zip`

Final package SHA256 and byte size:

Recorded outside the ZIP in:

`03_PHONE_PROOF/SHA256_STAGE3A_2NDLINE_SAME_DEVICE_RETRY_WITH_RUNLOG_PACKAGE_20260705.csv`

This ZIP includes:

- post-test Run Log screenshot,
- Moto `runlog.txt` external-view screenshot,
- redacted full runlog text,
- Stage 3A runlog audit report.

Raw private runlog:

`03_PHONE_PROOF/PRIVATE_RUNTIME_DO_NOT_SHARE/runlog_STAGE3A_same_device_retry_RAW_PRIVATE_20260705.txt`

Raw private runlog SHA256:

`BBA0DC77592849C9C5E8017AC229D0BC1D68C4A833352D4801F6624BB2AEDC48`

Redacted runlog SHA256:

`832F5874D52BD24A42216720D553AAD5DBE09312C22DC7E837A50EBF6EA47CBB`

Privacy:

- KEY_PRESENT_IN_RAW=true
- KEY_REDACTED_IN_AUDIT_COPY=true
- PHONE_VALUES_REDACTED_IN_AUDIT_COPY=true

ZIP files are ignored by Git by rule `*.zip`, so local ZIPs remain local unless uploaded separately.

## Drive Backup / Transfer Copy

Uploaded to Google Drive folder:

`AI Work / CHATGPT_HANDOFF`

Drive file:

`AIW_BUILD100_STAGE3A_2NDLINE_SAME_DEVICE_RETRY_HOLD_20260704.zip`

Drive size:

`127521` bytes

Drive link:

`https://drive.google.com/file/d/1-SxmQTL-RQOjqplMy7EtavA2tL2cKm46/view?usp=drivesdk`

Audit prompt file also uploaded:

`CHATGPT_STAGE3A_2NDLINE_SAME_DEVICE_RETRY_AUDIT_PROMPT_20260704.md`

Audit prompt Drive link:

`https://drive.google.com/file/d/1RTvJVv_YSbx7hAHHrWZSZxLvlR6l3R3g/view?usp=drivesdk`

## ChatGPT Upload Staging

Local staging folder:

`LOCAL_CODEX_NAVIGATION_LOGS/chatgpt_upload_stage`

Current staged file:

`AIW_BUILD100_STAGE3A_2NDLINE_SAME_DEVICE_RETRY_HOLD_20260704.zip`

## GitHub Visibility Check

GitHub CLI was not installed.

Anonymous GitHub API check returned 404 for the repo.

Meaning:

- The repo is not publicly readable from anonymous GitHub API in this check.
- This supports "likely private."
- It does not replace authenticated GitHub settings-screen proof.

## Current Hold

The full downloaded Moto `runlog.txt` has been pulled from Drive and audited through a redacted copy.

Stage 3A remains HOLD because the runlog proves trigger capture but also shows safety/setup task clean exit was not proven.

Next phone step is a clean Stage 3A rerun, not process/send testing.

Screen rule:

Codex must stay visible on PC while ChatGPT is used.
