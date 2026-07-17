# AI Worker Final Integrated Validation Plan - Current

Status: CURRENT PUBLIC-SAFE PLAN / NO PHONE IMPORT APPROVAL
Updated: 2026-07-16

## Objective

Produce one integrated private Tasker candidate that connects durable ingress, exact admission, overflow, processing, bounded API behavior, one-click Send, independent confirmation, exact Archive, STOP, restart recovery, environment controls, and a final operator interface.

The candidate remains held until independent artifact audit and direct phone validation.

## Source Boundary

- Current private runtime base: Gate 14D3A admission-only candidate.
- D3A SHA256: `880CC569185A9FFF45703EC77E71D6260A88474B0F63ECDE6B31E0A11CFF090A`.
- D3A direct source base SHA256: `3851E073BE042F80068E52CF7E3D410ED3D0EBA8A63C5F4C10108532912FE0EA`.
- Rejected D3, R1, R2, and R3 packages are reference history only.
- Gates 1 through 13 and phone-proven Gate 14 subproofs are preserved unless newer phone evidence contradicts the exact behavior.

## Frozen System Properties

The integrated candidate must maintain these properties:

- no legitimate event loss;
- no duplicate active OriginalID;
- no wrong-row write;
- no stale reply;
- no processable incomplete row;
- at most one real Send;
- no DONE before independent confirmation;
- no Archive before confirmed DONE;
- no unowned lock release;
- no new task aborting an active transaction;
- no unresolved overflow or ingress state bypass;
- no unbounded retry or queue recursion;
- every durable failure is recoverable or explicitly review-held.

## Connected Architecture

### Ingress And Identity

- Capture each notification payload into task-local values before shared serialization.
- Require sender and message; normalize missing optional metadata to explicit constants.
- Preserve only source-proven sender fallback behavior.
- Persist a bounded multi-event ingress journal before lock-busy or capacity HOLD can lose an event.
- Classify identity across Sheet1, unresolved OverflowInbox, Archive, DeadArchive, and unresolved ingress journal entries.

### Admission

- Views provide candidate hints only.
- Shared admission ownership protects every Sheet1 slot claim.
- Direct A:Z read proves blankness.
- Write payload A:I with a non-processable staging state.
- Verify the exact payload.
- Publish NEW last and verify it.
- Resolve the ingress journal only after authoritative readback.

### Overflow

- Physical OverflowInbox writes remain inside rows 2 through 986 unless an audited Sheet migration expands the grid first.
- Unresolved states block newer direct admission.
- FIFO authority is LoggedAt ascending, then physical source row ascending.
- Drain lock order is overflow owner, then admission owner.
- Safe drain order is verified DRAINING, verified main payload staging, verified source MAIN_COMMITTED, verified main NEW, then verified source DRAINED.
- Existing identical main rows reconcile without a second write.
- Collision or duplicate-main ambiguity routes to review.
- Bound failures preserve verified Attempts and LastError evidence.

### Queue And Processing

- Queue Cycle continues only after an exact allowed overflow result.
- HOLD, unresolved, or plugin-error results stop the current cycle before processing or Send.
- One top-level tick may consume at most one immediate pending kick.
- Preserve the phone-proven exact-row processing transaction and bounded OpenAI classifications.

### Send, Confirmation, And Archive

- Preserve phone-proven AutoInput targets and navigation semantics.
- Pre-click UI failure makes zero Send clicks and reaches owned cleanup.
- Post-click ambiguity never retries Send.
- Send click alone cannot produce DONE.
- Independent confirmation remains the DONE authority.
- Exact DONE plus confirmation remains the Archive authority.

### START, STOP, And Recovery

- Persistent DesiredRun controls boot resume.
- START runs recovery, environment, schema, and release-mode preflight before enabling approved entries.
- STOP disables new entries first and never blanket-clears an active owner.
- Startup recovery reconciles partial owner/timestamp state, admission staging, overflow staging, and ingress journal entries from durable evidence.
- Release V1 fails closed outside the approved powered, screen-on, unlocked environment.

## Final Validation Orchestrator

One top-level task, `AIW FINAL RELEASE VALIDATION ORCHESTRATOR`, must be one-shot authorized, phase-checkpointed, resumable, and stop at the first exact failure.

Required phases:

0. Preflight: package identity, profile state, permissions, environment, Sheet schema/bounds, test IDs, locks, recovery, and proof ledger.
1. Admission: direct main, overflow append, optional metadata, sender fallback, duplicate/collision/history, same-time identity, special characters, contention, and cleanup.
2. Overflow/recovery: two-event FIFO, transition order, partial-main reconciliation, failure evidence, queue drain gate, durable capacity/lock-busy hold, lock recovery, and no duplicate main row.
3. Process/API: one real API success plus injected rate-limit, timeout, quota, malformed-response, and ambiguous-plugin outcomes.
4. One real lifecycle: one approved inbound message, one API reply, one exact thread, no more than one Send click, confirmation, DONE, Archive, and zero second Send.
5. STOP/restart/environment: STOP boundaries, tick/kick coalescing, lock-screen failure, and DesiredRun resume.
6. Compressed soak: synthetic non-UI cycles with lock, duplicate, stale-row, queue-depth, and duration counters.
7. Cleanup: exact test-ID cleanup, authorization cleanup, disabled unsafe maintenance, final STOP state, and proof summary.

## Offline Test-Engineer Suite

Before packaging, Codex must run and independently reproduce:

- two independent XML/static validators;
- complete call-graph extraction;
- variable read/write and lock-owner mapping;
- plugin settings, timeout, collision, and Keep Device Awake inventory;
- balanced Tasker block and reference checks;
- executable connected state model;
- failure injection before and after each lock, Sheet, HTTP, AutoInput, Send, transition, STOP, and recovery boundary;
- at least 100,000 randomized schedules and at least 1,000,000 modeled operations;
- mutation tests for duplicate, owner, readback, NEW-last, MAIN_COMMITTED, drain-gate, Send, confirmation, Archive, STOP, journal-capacity, and collision guards;
- exact protected-action comparison for phone-proven modules;
- encoding, privacy, credential-equality, ZIP-equality, Git-diff, and private-file tracking checks.

Generated reports cannot prove themselves. A second implementation or direct independent inspection must confirm critical results.

## Sheet Migration Manifest

Codex must not change the live Sheet. The candidate return must provide a public-safe migration manifest or `NONE`.

Any proposed migration must align:

- QueueView recovery visibility without making staging states processable;
- OverflowView unresolved states and FIFO ordering;
- OpenSlotView hint behavior with A:Z authority;
- physical grid bounds and runtime bounds;
- ingress journal schema when a Sheet-backed journal is selected;
- proof-ledger schema used by the orchestrator.

## Acceptance Boundary

Artifact acceptance requires structural, semantic, concurrency, fault, mutation, privacy, and package checks. Release still requires Tasker import/render, the complete orchestrator, one exact real lifecycle, clean final locks/state, proof export, controller audit, and direct Sosa approval.

Current status remains:

- main-gate count: `13/14 locked = 93%`;
- detailed tracker: 40 total, 25 phone/runtime, 15 non-phone;
- phone import: HOLD;
- PR merge: BLOCKED;
- release: BLOCKED.

## Fixture-Safety Contract Amendment

This section supersedes every fixed-row validation-fixture example in earlier planning text.

- Task 268 must obtain one complete controller-supplied, one-shot fixture contract and return `FIXTURE_CONTRACT_READY` before Task 269 or any phase is reachable.
- The contract must bind the current validation run ID, layer, physically valid row, approved maximum row, protected columns, expected fixture identity, disposable payload, and role.
- There are no default or example fixture rows, IDs, senders, messages, or layers in runtime.
- Setup performs exact read-before-write, requires the protected range to be blank, then performs exact identity readback.
- Cleanup performs exact read-before-clear, requires the current run, role, row, identity, and permitted disposable contents, then performs exact blank readback.
- Already-blank cleanup writes nothing. Any ambiguity, unexpected content, plugin error, stale authorization, or bounds conflict returns HOLD with zero writes.
- The controller must select live rows later from fresh read-only evidence. Sheet migration and phone import remain HOLD until that evidence and the complete artifact audit pass.

## Option A Phase 1 Conversation-Continuity Amendment

This section supersedes the earlier one-inbound Phase 4 description only.

Phase 4 now requires one approved test contact, two to four rapid legitimate inbound messages, exact journal evidence for every OriginalID, the 10-second persisted-`LoggedAt` quiet gate, one durable ordered group, one context-aware OpenAI reply, one READY_TO_SEND anchor, zero sendable companions, one Send click maximum, independent confirmation, exact anchor Archive, exact companion Archive, `GROUP_COMPLETE`, clean ownership, and zero second Send.

The validation run must use a controller-approved confirmed Archive history fixture from the existing one-shot fixture contract. No fixed row or identity is permitted. Phase 7 must clear only the current run-owned journal, Archive, and ConversationGroups records after exact identity reads and exact blank readbacks.

Offline acceptance additionally requires:

- all ten durable group states and legal transition edges;
- exact source-order and normalized-sender membership;
- duplicate member row/ID rejection;
- a four-message V1 capacity with excess left eligible;
- Archive-history sender isolation, latest-five and character caps, and grouped-reply collapse;
- active-group serialization before any second group can bind;
- pre-Send membership freshness and lifecycle-only routing after a possible click;
- recovery at every group-state boundary;
- 32 named conversation scenarios, 100,000 randomized schedules, at least 1,000,000 operations, and mutations for all critical guards.

Transport-level notification replay identity remains a separate Option A Phase 2 HOLD. No text fingerprint is authorized.

## Phase 1 R1 validation correction

Phase 4 must now prove the actual source progression:

`JOURNALED -> RESOLVED_MAIN or RESOLVED_OVERFLOW -> durable group membership`

It must reject zero/duplicate journal matches, arbitrary terminal status, mismatched sender/message/normalized sender, invalid LoggedAt, unresolved output, and `#ERROR`.

The source-order regression must execute Task 263's actual order and prove lifecycle-only routing for awaiting-confirm plus 1/10/50 NEW rows, reply-ready, Send-review, anchor-archived, and partial-finalization states. Every applicable case requires one Task 262 call, zero newly processed rows, zero new OpenAI calls, and zero second Send.

Quiet validation must prove exact-cutoff scheduling, Abort-Existing coalescing, no lock/write/API/Send during wait, STOP cancellation, cutoff extension by a newer event, and one normal-cycle dispatch.

Migration validation must independently enumerate all 23 required tabs/views and compare every formula in `AIW_FINAL_INTEGRATED_SHEET_MIGRATION_MANIFEST_CURRENT.md`. Migration remains plan-only and is not part of Codex offline execution.
