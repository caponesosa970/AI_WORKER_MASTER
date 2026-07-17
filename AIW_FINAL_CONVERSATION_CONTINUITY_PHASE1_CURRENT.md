# AI Worker Durable Conversation Continuity — Option A Phase 1

Date: 2026-07-17

Classification: `SUPERSEDED SOURCE CANDIDATE / REJECTED FOR PHONE IMPORT / REPAIRED BY PHASE 1 R1`

Controller audit found four blocking defects in this source candidate: admitted IngressJournal rows were incorrectly required to remain `JOURNALED`; an active nonterminal group could be starved by a newly selected `NEW` row; quiet waits had no bounded deferred recheck; and the migration addendum was not self-contained. The exact source remains preserved as the authorized R1 repair base. See `AIW_FINAL_CONVERSATION_CONTINUITY_PHASE1_R1_CURRENT.md` for the current static candidate.

Candidate artifact identity:

- Private XML filename: `AIW_FINAL_INTEGRATED_FULL_PROJECT_TASKER_IMPORT_PRIVATE__CONVERSATION_CONTINUITY_P1.xml`
- Bytes: `5,607,668`
- SHA256: `D69480C9A212430D5D46753E3A05CBF4DB52045A6A8F967605BD3A3631CAB66E`

## Source and issue

- Authorized base: `AIW_FINAL_INTEGRATED_FULL_PROJECT_TASKER_IMPORT_PRIVATE__FIXTURE_SAFETY_R1.xml`.
- Base bytes: `4,876,933`.
- Base SHA256: `58A5229EB7F6892C03AD799BB7A4C3144C59ACD4DEC0E5B2235F0AAF68EEF76B`.
- Issue: `ISSUE_FINAL_CONVERSATION_GROUPING_AND_ARCHIVE_CONTEXT_INCOMPLETE`.
- User/operator responsibility: `NONE`.

The source route grouped only an in-memory QueueView snapshot, had no durable group identity or recovery, left companion rows `NEW`, and built an OpenAI prompt without bounded confirmed Archive history. That could permit one member to be answered again after the anchor reply.

## Authorized runtime scope

Existing semantic changes are limited to:

- Task 262 — `AIW Protected Send Confirm Archive One`
- Task 273 — `AIW Validation Phase 4`
- Task 276 — `AIW Validation Phase 7`
- Task 278 — `AIW Owner Safe Startup Recovery`
- Task 282 — `AIW Integrated Process One`
- Task 284 — `AIW Sheet Schema Check`

Added conversation-only helpers are Tasks 309 through 326. Every helper has `rty=0`, `stayawake=true`, fewer than 500 actions, a single bounded role, Project registration, and no profile or scene caller.

Phone-proven Tasks 71, 199, 223, 225, 226, 227, 230, and 231 are raw-byte identical to the authorized base. Tasks 27, 28, 69, and 222 are also raw-byte identical and unreachable from the final production and validation roots.

## Runtime architecture

The active production route remains:

`199 → 263 → 282 → 262`

Task 282 now uses:

`ledger locate → quiet select → durable bind → Task 233 MARK_PROCESSING → conversation prompt → unchanged bounded OpenAI → Task 233 COMMIT_SUCCESS → durable GROUP_REPLY_READY`

Task 262 now uses:

`pre-Send exact group guard → unchanged Task 71 → durable possible-click state → unchanged Task 227 → anchor Archive proof → exact companion finalization through unchanged Task 226`

Task 278 invokes one bounded recovery helper. Recovery never calls `FINAL Send Sheet`.

## Durable schema

The additive `ConversationGroups` tab uses schema version `AIW_CONVERSATION_V1`. It stores 42 columns, A:AP:

| Columns | Contents |
|---|---|
| A:F | schema version, GroupID, normalized SenderKey, anchor row, anchor OriginalID, member count |
| G:N | four ordered member row/OriginalID pairs |
| O:Q | durable state, quiet cutoff, bound timestamp |
| R:X | confirmed reply, recovery/error/update, confirmation, Archive state, finalized count |
| Y:AJ | owner pair, ledger row, freeze timestamp, history/prompt references, transition sequence, bind/Archive masks, capacity, validation run context |
| AK:AN | four ordered member messages |
| AO:AP | sender display and production/validation role |

V1 capacity is four messages per group. Excess rows remain `NEW` and are not marked consumed. Only one nonterminal group may exist in the serialized final-production path; a second candidate returns `CONVERSATION_ACTIVE_GROUP_BUSY_HOLD` so Task 262 can advance the existing lifecycle first.

## Durable state machine

The allowed states are:

- `GROUP_BINDING`
- `GROUP_BOUND`
- `GROUP_PROCESSING`
- `GROUP_REPLY_READY`
- `GROUP_SEND_AWAITING_CONFIRM`
- `GROUP_SEND_OUTCOME_REVIEW`
- `GROUP_ANCHOR_ARCHIVED`
- `GROUP_FINALIZING`
- `GROUP_COMPLETE`
- `GROUP_REVIEW`

Task 316 validates both the exact current state and an explicit legal source-to-target edge before every state write, then performs exact readback. Illegal edges HOLD.

## Quiet gate and bind transaction

- Timestamp authority: exact persisted `IngressJournal.LoggedAt`, not notification display time.
- Quiet interval: 10,000 ms after the newest eligible same-sender event.
- Quiet HOLD: `CONVERSATION_QUIET_WAIT_HOLD`.
- Quiet task operations: bounded AutoSheets reads only; no lock, group-ledger write, Sheet write, OpenAI call, or Send call.
- Sender normalization reuses the existing Task 194 behavior.
- Membership preserves QueueView physical source order, exact OriginalIDs, exact messages, and normalized sender equality.
- Duplicate member rows or IDs HOLD before ownership or mutation.
- Ledger creation and every companion `GROUP_BOUND` status use exact read-before-write and readback.
- Partial bind is never blindly reset to `NEW`; it becomes durable review/recovery work.

## History and prompt boundary

Archive remains the confirmed-history authority. The history helper:

- reads only configured physical bounds;
- accepts only exact same-sender `DONE` rows with a nonblank confirmed reply;
- rejects unresolved values and `#ERROR`;
- keeps chronological order and the latest five turns;
- enforces a 3,000-character history budget and a 600-character per-turn budget;
- treats no history as valid;
- HOLDs on a real Archive read failure without using cached history;
- uses completed durable group membership to collapse a grouped turn to ordered inbound messages plus one assistant reply.

Validation Phase 4 additionally requires the current controller-approved history fixture ID from the one-shot fixture contract. The private prompt payload is not recorded in Git.

## Send-once and finalization boundary

- A group may reach Task 71 only from exact `GROUP_REPLY_READY` after exact anchor and companion reads.
- A new same-sender event logged on or before the group bound timestamp and absent from membership causes `CONVERSATION_PRE_SEND_STALE_HOLD` with zero Send clicks.
- An event logged after the documented freeze boundary remains the next turn.
- A possible click is durably recorded before Task 227 runs.
- Restart or later cycles in awaiting-confirm/review use `CONVERSATION_GROUP_LIFECYCLE_ONLY`; Task 71 is skipped.
- Independent confirmation remains the only DONE authority.
- Exact Task 226 Archive completion remains the source-clear authority.
- Companions receive the exact confirmed anchor reply only after anchor Archive proof, then each companion uses exact row/ID/sender/message/status verification, one DONE/reply write and readback, unchanged Task 226, and durable per-member progress.
- `GROUP_COMPLETE` requires every member independently verified in Archive and cleared from Sheet1.

## Recovery

Recovery classifies incomplete bind, processing, reply-ready, possible-click, anchor-archived, partial companion Archive, review, and complete states. It never retries Send after a possible click, never releases an unowned conversation lock, never resets uncertain rows to `NEW`, and finalizes already-confirmed companions idempotently.

## Validation and proof

- Standard Tasker XML audit: PASS.
- Independent DOM/runtime-contract validator: 61/61 PASS.
- Complete topology: 170 tasks / 4 profiles / 2 scenes / 23,519 actions.
- Missing task/profile/scene/Project references: zero.
- Control-stack issues: zero.
- XML guard mutants detected: 18/18.
- Independent modeled scenarios: 32/32 PASS.
- Group-state crash boundaries: 10/10 PASS.
- Randomized schedules: 100,000.
- Modeled operations: 2,400,000.
- Randomized invariant failures: zero.
- Mojibake markers: zero.

Generated reports are evidence inputs, not self-authenticating proof. ChatGPT must reproduce critical checks against the exact private XML and ZIP.

## Transport replay boundary

The current AutoNotification profile exposes candidate identifiers including notification ID, key, tag, notification times, conversation/extras metadata, package/user context, and touch/button actions. Task 68 currently derives OriginalID as `%TIMEMS` plus two random six-digit values and does not consume a source-proven stable delivery identity.

Therefore transport-level replay protection is `UNSUPPORTED / HOLD FOR OPTION A PHASE 2`. No sender/message fingerprint was added, and Task 68 is raw-byte identical.

## Next hardening handoff

The separate heartbeat/production-ledger capability must observe:

- `%AIWConversationOwner` and `%AIWConversationOwnerStartedAt`;
- current GroupID, ledger row, SenderKey, anchor row/ID, member count, and transition sequence;
- `GROUP_SEND_AWAITING_CONFIRM`, `GROUP_SEND_OUTCOME_REVIEW`, `GROUP_ANCHOR_ARCHIVED`, `GROUP_FINALIZING`, `GROUP_COMPLETE`, and `GROUP_REVIEW`;
- finalized-member count, bind/Archive masks, last error, confirmation state, and Archive state.

The heartbeat/production ledger is not implemented in this phase.

## Unsupported claims and HOLDs

- Stable transport replay identity: HOLD for Option A Phase 2.
- Live ConversationGroups schema and physical bounds: not migrated or phone-proven.
- Tasker import/render: not performed.
- AutoSheets runtime behavior: not phone-proven.
- Phase 4 real lifecycle: not run.
- Final orchestrator: not run.
- Phone proof, Gate 14 closure, PR merge, and production release: not claimed.

## R2 Current Repair Boundary

R2 corrects only the full-capacity freshness cutoff and the non-destructive live-workbook migration plan. Phase 1 architecture, R1 journal/lifecycle/quiet repairs, phone-proven modules, and Option A Phase 2 exclusions remain unchanged. See `AIW_FINAL_CONVERSATION_CONTINUITY_PHASE1_R2_CURRENT.md`.
