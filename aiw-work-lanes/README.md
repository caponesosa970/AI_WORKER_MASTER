# AI Worker Cross-Chat Work Lanes

Status: `CANDIDATE / REPO-READY / NOT YET INSTALLED`

This directory is a non-authoritative coordination system. It cannot override the four current root authority files:

1. `AGENTS.md`
2. `AIW_FULL_GOAL_EXECUTION_CONTRACT_CURRENT.md`
3. `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`
4. `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`

## Purpose

Allow Sosa, ChatGPT, and Codex to continue AI Worker work across separate chats without losing evidence, mixing test work into the real build, or allowing a test artifact to promote itself.

## Authority model

- `MAIN_LOCKED`: accepted system truth after required independent audit and phone proof.
- `LANE_LOCKED`: finalized evidence within one test lane. It is not production authority.
- `CANDIDATE`: incomplete or unaudited work.
- `HOLD`: work blocked by one exact unresolved condition.
- `REJECTED`: failure evidence only; forbidden as a runtime parent unless a later exact authorization names an isolated safe region.

## Promotion flow

`NEW INFORMATION -> TEST LANE -> VERIFIED -> LANE_LOCKED -> CHATGPT AUDIT -> PHONE PROOF WHEN REQUIRED -> PROMOTION RECORD -> MAIN_LOCKED`

No test lane may edit Main, approve itself, claim phone proof, or declare release.

## Privacy

This repository is public. Never store credentials, API keys, private XML containing credentials, phone numbers, messages, replies, screenshots, runlogs containing private data, workbook rows, or private Drive URLs here. Use safe filenames and SHA256 values only. Private bytes remain out of band.

## Operator phrases

- `Place this for Codex in the Main lane: <information>`
- `Place this for Codex in the DeadArchive test lane: <information>`
- `Receive the latest Codex return from the DeadArchive test lane.`
- `Show the current state of every AI Worker lane.`
- `Promote this lane evidence to Main.`

The final phrase requests an audit; it does not automatically authorize promotion.
