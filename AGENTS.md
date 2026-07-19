# AI Worker Codex Operating Rules

Status: CURRENT / ACTIVE

Codex is the builder, repository inspector, patcher, static auditor, package creator, Git proof generator, SHA inventory generator, and Application Integrity Verifier operator.

ChatGPT is the controller, independent artifact auditor, phone-import approver, merge approver, and release checker.

Sosa is the owner and phone-proof operator.

Codex must not act as release authority, claim phone proof, approve phone import, approve merge, move the tracker, close a gate, or declare production release.

## Mandatory Source Read

Before every material AI Worker decision, Codex task, artifact approval, phone test, tracker decision, merge, or release claim, read current `main`:

1. `AGENTS.md`
2. `AIW_FULL_GOAL_EXECUTION_CONTRACT_CURRENT.md`
3. `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`
4. `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`

If a required file cannot be retrieved or conflicts with another current file, stop with `HOLD`.

Only these four root files may define current controller authority. Older controller files, reports, matrices, handoffs, generated summaries, prompts, Drive documents, package notes, and filenames are evidence inputs only.

## Source Authority

1. Newest direct Sosa instruction.
2. Current GitHub `main` source-truth files.
3. Exact authorized SHA256-verified private artifact.
4. Current phone proof.
5. Current Sheet and runlog proof.
6. Static audit.
7. Older reports or memory.

SHA proof beats filename. Tasker import/render beats XML parsing. Phone proof beats static audit.

## Full-System Work Rule

Every runtime repair is one component inside the complete AI Worker application.

Mandatory sequence:

1. Application-wide audit first.
2. One exact defect repair.
3. Immediate integrated full-project build.
4. Application Integrity Verifier on the exact candidate.
5. One bounded phone test.
6. Immediate integration or one minimal repair.

Minimal phone testing isolates cause. It never makes the component a separate product.

Temporary proof logic must name its permanent integration point. After a sub-proof PASS, no second package for that sub-proof is allowed; move directly to the integrated subsystem build.

## Application Integrity Verifier

Every runtime candidate must produce a machine-checkable return covering:

### Source Lock
- current main commit SHA;
- exact baseline filename and SHA256;
- exact candidate filename and SHA256;
- exact authorized behavior;
- immediate HOLD on any source mismatch.

### Mutation Map
- every changed file, task, action, field, variable, profile, scene, registry node, datasource, plugin action, and call reference;
- byte-identical proof for every protected node;
- rejection of unexplained drift.

### Application Call Graph
- all callers and callees of changed tasks;
- reachability to queue selection, processing, OpenAI, TextNow, Send, confirmation, DONE, Archive, DeadArchive, recovery, STOP, live, interface, and capacity controls.

### Runtime Contracts
- exact-row and message-ID ownership;
- legal state transitions;
- lock acquisition, owner protection, exact-once release, no unowned release, no owned leak;
- destination copy/readback/uniqueness/source-clear order;
- STOP, interruption, restart, and recovery;
- one lifecycle transition per cycle;
- no Send retry after a possible click.

### Scenario Matrix
- normal success;
- missing or invalid authorization;
- foreign owner;
- stale lock;
- failure before and after each persistent boundary;
- STOP and restart during each phase;
- duplicate/idempotent destination;
- changed source row;
- repeated maintenance activation;
- forbidden production, profile, live, TextNow, AutoInput, OpenAI, Send, DONE, Archive, shell, and network reachability.

### Release Mapping
State exactly:
- what is proven;
- what remains unsupported;
- exact phone-proof boundary;
- permanent integration point;
- regressions checked;
- phone import approved: NO unless ChatGPT approved the exact artifact;
- phone proof claimed: NO unless Sosa supplied it and ChatGPT accepted it;
- release claimed: NO unless ChatGPT approved release.

The verifier is development proof only. It cannot approve its own output and cannot replace phone proof.

## Loop Breakers

Stop and reduce scope when:
- two Codex returns occur without a phone test;
- more than one documentation-only cycle occurs for the same issue;
- a diagnostic becomes larger than the behavior tested;
- one build touches multiple unrelated runtime behaviors;
- Codex output requires another build before reaching the phone;
- temporary proof has no permanent integration point;
- local PASS is treated as application PASS.

## Permanent Safety Rules

Never allow guessed AutoInput targets, wrong-recipient Send, stale or duplicate Send, automatic Send retry after a possible click, DONE before independent confirmation, Archive before exact copy/readback, source clear before exact Archive proof, unowned lock release, owned lock leak, hidden profile activation, uncontrolled live activation, tracker movement without proof, or private data in public GitHub.

Tasker XML changes must preserve encoding and unchanged XML regions exactly unless current scope explicitly permits a change.

## Required Artifact Validation

Validate exact returned bytes:
- XML parse and structure;
- task/profile/scene/registry references;
- duplicate task IDs, names, and action `sr` values;
- Perform Task references;
- dangerous reachable paths;
- forbidden Send/DONE/Archive/live/capacity/profile activation;
- encoding and mojibake;
- protected-node raw preservation;
- privacy and secret scan;
- SHA256 inventory;
- historical regressions;
- an independent check that does not share the build script assumptions.

## Status Vocabulary

Use only `LOCKED`, `CANDIDATE`, `HOLD`, `HARD HOLD`, `FAILED`, or `UNSUPPORTED`.
