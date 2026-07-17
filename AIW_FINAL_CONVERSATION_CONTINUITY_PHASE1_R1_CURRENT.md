# AI Worker Durable Conversation Continuity - Option A Phase 1 R1

Date: 2026-07-17

Classification: `STATIC DEVELOPMENT PASS / CANDIDATE / HOLD FOR CHATGPT ARTIFACT AUDIT, MIGRATION, AND CONTROLLED PHONE PROOF`

## Source identity

- Repository head before work: `5252f8f09473311e6acd99fa27847149fe849646`.
- Repair base: `AIW_FINAL_INTEGRATED_FULL_PROJECT_TASKER_IMPORT_PRIVATE__CONVERSATION_CONTINUITY_P1.xml`.
- Repair-base bytes: `5,607,668`.
- Repair-base SHA256: `D69480C9A212430D5D46753E3A05CBF4DB52045A6A8F967605BD3A3631CAB66E`.
- R1 private XML: `AIW_FINAL_INTEGRATED_FULL_PROJECT_TASKER_IMPORT_PRIVATE__CONVERSATION_CONTINUITY_P1_R1.xml`.
- R1 private XML bytes: `5,738,927`.
- R1 private XML SHA256: `9EB0A9FD6B3E342E4022AEE20022683F1BF08A54E65892A099565A3542D0A758`.

The source candidate is rejected for phone import. R1 is a new static candidate; it is not phone-approved.

## Issues and responsibility

### ISSUE_CONVERSATION_JOURNAL_STATUS_CONTRACT_WRONG

- First detected: 2026-07-17 controller artifact audit.
- Evidence: Tasks 309, 320, and 325 required `JOURNALED` after Tasks 254/255 had already persisted `RESOLVED_MAIN` or `RESOLVED_OVERFLOW`.
- Root cause: the conversation validator modeled notification receipt but not the admitted production source contract.
- Repair: exact-one journal identity now requires `TEXTNOW`, exact ID/sender/message/normalized sender, numeric `LoggedAt`, and exactly `RESOLVED_MAIN` or `RESOLVED_OVERFLOW` for selected members.
- Codex responsibility: the original Phase 1 static model did not reproduce the admission transition strictly enough.

### ISSUE_CONVERSATION_LIFECYCLE_STARVATION_BY_NEW_ROW

- First detected: 2026-07-17 controller artifact audit.
- Evidence: Task 263 calls Task 282 before Task 262; Task 317 returned a `BUSY_HOLD` only after a new row was selected, causing Task 263's `HOLD|ERROR` guard to exit before lifecycle work.
- Root cause: active-group routing happened after queue candidate selection and used a HOLD result.
- Repair: Task 282 gates active groups before QueueView selection. Lifecycle states return `CONVERSATION_GROUP_LIFECYCLE_ONLY`; review returns `CONVERSATION_GROUP_REVIEW_ONLY`. Neither matches the early-exit regex, so Task 262 runs exactly once.
- Codex responsibility: the original Phase 1 proof did not simulate Task 263's concrete call order with competing NEW rows.

### ISSUE_CONVERSATION_QUIET_RECHECK_NOT_SCHEDULED

- First detected: 2026-07-17 controller artifact audit.
- Evidence: `CONVERSATION_QUIET_WAIT_HOLD` depended on the next normal two-minute tick.
- Root cause: the quiet state had no bounded coalesced continuation.
- Repair: new Task 327 waits outside all queue/conversation/processing/Send/confirmation/Archive ownership, uses Abort-Existing collision behavior, rechecks STOP, and invokes normal Task 263 once after the cutoff.
- Codex responsibility: the original Phase 1 build proved quiet safety but not timely re-entry.

### ISSUE_CONVERSATION_MIGRATION_MANIFEST_NOT_SELF_CONTAINED

- First detected: 2026-07-17 controller workbook/manifest audit.
- Evidence: the addendum referred to an older manifest and omitted exact formulas and full physical contracts for candidate-required tabs.
- Root cause: Phase 1 documented only its additive tab instead of publishing one final migration authority.
- Repair: the current migration manifest now contains all 23 required tabs/views, exact schemas, target grid sizes, every formula, backup, migration, read-only verification, rollback, privacy, and dynamic-fixture rules.
- Codex responsibility: the original Phase 1 deliverable did not independently reconcile all inherited migration dependencies.

Controller responsibility: approve or reject the exact artifacts, then separately approve migration and controlled phone proof.

User/operator responsibility: `NONE`.

## Exact runtime scope

Existing task changes are exactly:

| Task | Name | Base actions | R1 actions | R1 purpose |
|---:|---|---:|---:|---|
| 263 | AIW Integrated Queue Cycle | 49 | 64 | release owner, schedule quiet recheck, preserve lifecycle continuation/result |
| 273 | AIW Validation Phase 4 | 30 | 38 | verify JOURNALED -> admitted -> grouped progression |
| 282 | AIW Integrated Process One | 76 | 81 | active-group gate before QueueView selection |
| 309 | AIW Conversation Quiet Select | 221 | 279 | exact admitted journal contract and deferred cutoff output |
| 317 | AIW Conversation Prepare Group | 147 | 234 | pre-selection lifecycle-only/review routing |
| 320 | AIW Conversation Pre Send Guard | 221 | 364 | unresolved JOURNALED plus active admitted-row freshness |
| 324 | AIW Conversation Schema Check | 244 | 264 | exact group slot/schema/bounds contract |
| 325 | AIW Conversation Validation Audit | 130 | 307 | PRE_JOURNALED, ADMITTED, and POST modes |

Added helper:

| Task | Name | Actions | Collision | Role |
|---:|---|---:|---|---|
| 327 | AIW Conversation Deferred Recheck | 43 | `rty=1` Abort Existing | STOP-aware, coalesced, bounded quiet re-entry |

Task 327 is Project-registered, has no profile/scene caller, is called only by Task 263, and calls only the normal Task 263 cycle. It has no AutoSheets, OpenAI, AutoInput, Send, confirmation, or Archive action.

## Source-contract repair

Selected Sheet1 group members now require exactly one IngressJournal row with:

- exact OriginalID;
- exact source `TEXTNOW`;
- exact sender and message;
- matching normalized sender;
- numeric `LoggedAt`;
- exact status `RESOLVED_MAIN` or `RESOLVED_OVERFLOW`.

Zero matches, duplicate matches, `JOURNALED` only, arbitrary status, collision, mismatched payload, invalid time, unresolved output, plugin error, or `#ERROR` HOLD before ownership, writes, OpenAI, or Send.

Pre-Send freshness treats an unresolved same-sender `JOURNALED` event as stale. It also inspects active QueueView NEW rows and active OverflowInbox rows and requires their exact admitted journal record. A resolved historical record without an active unresolved location is ignored.

Tasks 254 and 255 are raw-byte identical. Their `RESOLVED_MAIN` and `RESOLVED_OVERFLOW` progression is preserved.

## Lifecycle-only routing

Concrete Task 263 order remains:

`journal drain -> overflow drain -> Task 282 -> HOLD|ERROR guard -> Task 262`

Task 282 now calls Task 317 in `LIFECYCLE_GATE` mode before queue health, QueueView load, or candidate selection. These active states return `CONVERSATION_GROUP_LIFECYCLE_ONLY`:

- `GROUP_REPLY_READY`
- `GROUP_SEND_AWAITING_CONFIRM`
- `GROUP_SEND_OUTCOME_REVIEW`
- `GROUP_ANCHOR_ARCHIVED`
- `GROUP_FINALIZING`

`GROUP_REVIEW` returns `CONVERSATION_GROUP_REVIEW_ONLY`; it remains non-sendable. Other contradictory nonterminal states return an explicit recovery HOLD. No second group binds while a nonterminal group exists.

The source-order model covers awaiting-confirm plus 1, 10, and 50 NEW rows, and reply-ready, Send-review, anchor-archived, and partial-finalization plus NEW rows. Each case calls Task 262 once, processes zero NEW rows, makes zero new OpenAI calls, and never exceeds one Send click.

## Deferred quiet recheck

- Timestamp authority remains persisted `IngressJournal.LoggedAt` plus 10,000 ms.
- Task 309 exports exact cutoff and normalized sender only when it returns `CONVERSATION_QUIET_WAIT_HOLD`.
- Task 263 clears worker-busy state and releases its exact queue owner before Task 327 starts.
- Task 327 holds no runtime lock while waiting and performs no Sheet/API/Send action.
- `rty=1` aborts an existing waiter when a newer cutoff is scheduled, leaving one waiter.
- The loop is bounded to 15 one-second checks; a newer event supplies a new cutoff and replaces the old waiter.
- `%AIWStopRequested=1` or worker-off state cancels without dispatch.
- At/after cutoff, Task 327 invokes normal Task 263 once. Normal queue ownership and Task 263 collision behavior remain authoritative.

## Migration authority

`AIW_FINAL_INTEGRATED_SHEET_MIGRATION_MANIFEST_CURRENT.md` is self-contained. It defines 23 tabs/views, exact target row/column counts, all schemas and formulas, `ConversationGroupSlotView!A2`, `ConversationSchemaCheck!A2:G2`, migration/verification/rollback order, and privacy boundaries.

It preserves these rules:

- Sheet1 rows 144:147 are occupied/protected.
- Archive/DeadArchive row 999 is never a fixture.
- Archive and DeadArchive row expansion is a migration plan only, required by preserved bounded row-1000 reads; no row is seeded.
- fixture rows remain dynamic controller inputs with no guessed row;
- no migration was applied by Codex.

## Preservation and proof

- Existing tasks preserved raw-byte: 162/162 outside the eight-task authorization.
- Phone-proven Tasks 71, 199, 223, 225, 226, 227, 230, and 231: raw-byte identical.
- Tasks 254, 255, and 262: raw-byte identical.
- Profiles: 4/4 identical and disabled-state bytes unchanged.
- Scenes: 2/2 identical.
- Missing task/profile/scene/Project references: zero.
- Control-stack issues: zero.
- Independent R1 static checks: 70/70 PASS.
- Migration checks: 22/22 PASS.
- R1 unsafe mutations: 11/11 detected.
- Preserved Phase 1 guard mutations: 18/18 detected.
- R1 source-order schedules: 100,000; operations: 3,200,000; failures: zero.
- Preserved group-state schedules: 100,000; operations: 2,400,000; failures: zero.
- Preserved state-boundary faults: 10/10 PASS.
- Standard Tasker XML audit: PASS.
- Independent integrated analyzer: 171 tasks / 4 profiles / 2 scenes / 24,075 actions; zero control or reference issues.

Generated reports remain evidence inputs, not self-authenticating phone proof.

## Unsupported claims and HOLDs

- Live workbook migration and formulas: not applied or verified.
- Live fixture rows: not selected.
- Tasker import/render: not performed.
- Deferred collision behavior on the target phone: not phone-proven.
- AutoSheets runtime behavior: not phone-proven.
- Phase 4 real lifecycle and real Send: not run.
- Stable transport replay identity: Option A Phase 2 HOLD.
- General heartbeat and production event ledger: Option A Phase 2 HOLD.
- Final orchestrator, Gate 14 closure, merge, and production release: HOLD.

Current decision: `OPTION A PHASE 1 R1 SOURCE-CONTRACT AND LIFECYCLE REPAIR CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT`.
