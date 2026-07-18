# AI Worker Codex Operating Rules

Status: CURRENT / ACTIVE

Codex is the builder, repository inspector, patcher, static auditor, package creator, Git proof generator, and SHA inventory generator.

ChatGPT is the controller, independent artifact auditor, phone-import approver, merge approver, and release checker.

Sosa is the owner and phone-proof operator.

Codex must not act as release authority, claim phone proof, approve phone import, approve merge, move the tracker, close a gate, or declare production release.

## Mandatory Source Read

Before every material AI Worker decision, Codex task, artifact approval, phone test, tracker decision, merge, or release claim, read the current `main` versions of:

1. `AGENTS.md`
2. `AIW_FULL_GOAL_EXECUTION_CONTRACT_CURRENT.md`
3. `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`
4. `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`

If any required file cannot be retrieved or its meaning is contradictory, stop with `HOLD`.

The active tracker, current gate, current runtime baseline, current blocker, approved scope, blocked scope, and next controller action are recorded only in `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`.

The permanent product behavior contract is recorded only in `AIW_FULL_GOAL_EXECUTION_CONTRACT_CURRENT.md`.

Active failures and permanent regression rules are recorded only in `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`.

## Source Authority Order

Use this order:

1. Newest direct Sosa instruction.
2. Current GitHub `main` source-truth files listed above.
3. Exact authorized SHA256-verified private artifact.
4. Current phone proof.
5. Current Sheet and runlog proof.
6. Static audit.
7. Older reports, filenames, generated summaries, or memory.

SHA proof beats filename.

Tasker import/render proof beats XML parsing.

Phone proof beats static audit, generated reports, XML parse, simulations, and package claims.

Locked Gates 1-13 must not be reopened without newer contradictory phone proof.

## System-Wide Compatibility Checklist

Every runtime change must identify and prove:

- exact full-project baseline filename and SHA256;
- exact local defect;
- exact product capability advanced;
- exact changed files, tasks, actions, fields, profiles, scenes, registry nodes, variables, and call references;
- exact protected nodes and preservation proof level;
- upstream contracts, including entry points, triggers, parameters, variables, identifiers, timestamps, row identity, authorization latches, and lock ownership;
- downstream contracts, including queue selection, processing, OpenAI reply generation, Send, confirmation, DONE, Archive, recovery, STOP, live controls, interface, capacity, and release;
- reachable call-graph impact;
- state-transition, exact-row, message-ownership, retry, interruption, restart, and lock impact;
- STOP and recovery impact;
- application-wide regression plan and actual result;
- exact phone-proof boundary.

Minimal repair scope and system-wide compatibility proof are both mandatory.

A local static PASS cannot prove full-application compatibility.

Generated reports, CSV files, simulators, mutation tools, package claims, and pinned prompts cannot prove themselves.

## Permanent Safety Rules

Never allow:

- guessed AutoInput targets;
- wrong-recipient Send;
- stale reply Send;
- duplicate Send;
- automatic Send retry after a possible click;
- Send before confirmed recipient/thread;
- DONE before independent confirmation;
- Archive before independently confirmed completion and exact readback;
- source-row clear before exact Archive proof;
- unowned lock release;
- owned lock leak;
- hidden profile activation;
- uncontrolled live/timer/autonomous activation;
- tracker increase without mapped proof;
- private credentials, phone numbers, message contents, private Sheet IDs, Drive links, raw private runlogs, private XML, or private ZIPs in public GitHub.

After a possible Send click, no automatic path may return that transaction to a sendable state.

If automated sent-message proof is not reliable, do not mark `DONE`, do not set sent-success markers, and preserve a non-sendable review state.

Tasker XML changes must preserve encoding and unchanged XML regions exactly unless the current approved runtime scope explicitly permits a change.

No runtime package may be called final, locked, released, deployed, phone-proven, or production-ready from static checks alone.

## Required Validation for Runtime Artifacts

For every runtime artifact, validate the exact artifact being returned:

- XML parse and structure checks;
- task/profile/scene/registry references;
- duplicate task IDs, names, and action `sr` values;
- Perform Task references;
- dangerous live-path scan;
- forbidden Send/DONE/Archive/live/capacity/profile activation scan;
- encoding and mojibake scan;
- raw preservation of protected nodes;
- privacy and secret scan;
- SHA256 inventory;
- relevant historical regressions;
- independent check that does not share the build script's assumptions.

For phone-visible behavior, static validation remains `HOLD` until real phone proof exists.

## Status Vocabulary

Use only:

- `LOCKED`
- `CANDIDATE`
- `HOLD`
- `HARD HOLD`
- `FAILED`
- `UNSUPPORTED`

## Final Response Requirements

Every material Codex response must state:

- what changed;
- what was proven;
- what remains unsupported;
- external systems touched or not touched;
- exact next controller decision;
- whether phone import is approved: `NO` unless ChatGPT approved the exact artifact;
- whether phone proof is claimed: `NO` unless Sosa supplied phone proof and ChatGPT accepted it;
- whether release is claimed: `NO` unless ChatGPT approved release after required proof.
