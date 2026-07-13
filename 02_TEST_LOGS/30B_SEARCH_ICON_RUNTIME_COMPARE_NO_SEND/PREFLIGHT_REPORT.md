# PREFLIGHT REPORT - 30B SEARCH ICON RUNTIME COMPARE NO SEND

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT
Date: 2026-07-12

## Read Before Build

- `AGENTS.md`: READ
- `.codex/config.toml`: READ
- `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`: READ
- `AIW_BUILD_ACCOUNTABILITY_LEDGER_CURRENT.md`: READ
- `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`: READ
- `AIW_CLAIM_TO_PROOF_MATRIX_CURRENT.md`: READ
- `AIW_MANDATORY_BUILD_PREFLIGHT.md`: READ

## Tracker

- Current tracker remains: `8/14 locked = 57%`.
- Controlled Send remains HOLD.
- 30B is diagnostic only and does not unlock Send, DONE, Archive, live, capacity, or release.

## Current Issue Context

- `ISSUE_27B_AUTOINPUT_TARGET_NOT_V15A_PRESERVED` was corrected by 30A as source-preservation statically proven for SEARCH_ICON.
- `ISSUE_27B_SEARCH_ICON_RUNTIME_UI_FAILURE_WITH_V15A_PRESERVED` remains OPEN.
- 30B is designed to isolate the phone/runtime/UI behavior of the V15A ID search shape against the Dashgood active text-search shape.

## Bug History Search

Searched repository history and reports for:

- false pass
- malformed
- wrong source
- invented AutoInput
- SEARCH_ICON
- menu_search
- Structure Output
- phone proof supersedes
- static audit passed but phone failed
- duplicate
- wrong row
- lock release
- Send failure

Relevant prior failures applied:

- 23A/23B/23C malformed Tasker class: XML parse is not phone-render proof.
- 26A/26B false-pass class: AutoInput errors must not become success proof.
- 27B SEARCH_ICON phone/runtime failure: static preservation does not prove current TextNow UI behavior.
- 30A source-truth correction: V15A AutoInput action set is authoritative and Sosa-created.

## Approved Scope

Build one isolated diagnostic task:

`AIW30B_SEARCH_ICON_RUNTIME_COMPARE_NO_SEND`

The task compares:

1. V15A ID-based `menu_search` search icon path.
2. Dashgood active Task 71 text-based `Search` path with reset/retry field sequence.

## Prohibited Scope

No Sheets, HTTP, keyboard input, phone number, contact selection, compose focus, reply insertion, send button, DONE write, Archive, timer/live, capacity, or API key.

## Phone-Proof Limits

Codex does not claim phone proof and does not approve phone import. ChatGPT must audit the package before Sosa runs any phone test.
