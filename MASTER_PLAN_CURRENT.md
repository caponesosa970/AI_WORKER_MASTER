# AI Worker Build100 Active Workflow

Updated: 2026-07-05

This document is the ACTIVE WORKFLOW PLAN only.

It is NOT the source of truth for runtime behavior.
It must NEVER replace:

- locked source XML
- proven runtime behavior
- proof ledger
- runlogs
- screenshots
- SHA256 evidence
- Git history

## Source Of Truth Priority

1. Locked source packages
2. Proven phone proof
3. Current runtime XML
4. Proof Ledger
5. Git history
6. Active workflow plan

## Workflow Roles

ChatGPT:

- System architect
- Planner
- Auditor
- Release controller
- Decides promotion from CANDIDATE to LOCKED

Codex:

- Static auditor
- Repository maintainer
- Builder
- Documentation maintainer
- Git historian

## General Rules

- Never replace locked source without proof.
- Never remove proven logic unless evidence proves it is broken.
- Never invent proof.
- If proof is missing, mark HARD HOLD and identify the exact missing file.
- Preserve every proven layer when the source chain is unchanged.
- Build by subsystem, not by isolated bugs.
- Group independent safe fixes together.
- Leave dangerous runtime changes isolated for phone proof.

## Current Subsystem Order

Group A:

- Frozen proven systems.
- Do not touch unless source changes.

Group B:

- Send UI Dry Run.
- Current active subsystem.

Group C:

- Controlled One Send.

Group D:

- Live Controller / Timer.

Group E:

- Maintenance / Recovery.

Group F:

- Capacity / Production.

## Phone Testing

Phone proof is required only when runtime behavior cannot be proven statically.

Static work should be grouped whenever safe.

## Every Codex Output Must Include

- static audit
- SHA256 inventory
- git status
- git log -1 --stat
- git diff --name-only
- files changed
- remaining HOLD list
- next phone-proof checklist

## Current Package

Current workflow package:

`04_RELEASE_PACKAGES/_subsystem_completion_plan_20260705/`

Current ChatGPT audit ZIP:

`C:\Users\Shadow\Downloads\ai work\Codex to ChatGPT\06_CHATGPT_AUDIT_ZIP__AIW_BUILD100_SUBSYSTEM_COMPLETION_PLAN_20260705.zip`

## Final Project Status

`CANDIDATE / HOLD`

This remains true until ChatGPT audits the results.
