# AI Worker Full Goal Execution Contract — Current

Status: CURRENT / CANONICAL
Established: 2026-07-13
Authority: Newest direct Sosa instructions and the approved Plan A architecture.

## 1. Product Goal

Deliver a phone-based autonomous AI Worker that:

1. Detects legitimate TextNow messages.
2. Logs each message to the exact Google Sheet row.
3. Preserves sender, message, IDs, timestamps, and row identity.
4. Generates a context-aware reply through the OpenAI API.
5. Opens the correct TextNow conversation.
6. Ensures the compose field is safe.
7. Inserts the exact bound reply.
8. Clicks Send no more than once.
9. Confirms the outcome before declaring completion.
10. Archives only confirmed completed rows.
11. Recovers safely from partial failures.
12. Runs until STOP.
13. Supports the final control interface.
14. Reaches the intended 50-contact reliability target.

## 2. Permanent End-to-End Flow

The final system flow is:

`TextNow event`
→ `exact Sheet row logged`
→ `exact row processed`
→ `reply generated`
→ `READY_TO_SEND`
→ `exact row selected`
→ `SENDING written and verified`
→ `correct TextNow thread opened`
→ `compose verified and populated`
→ `Send clicked zero or one time`
→ `SEND_CLICKED_AWAITING_CONFIRM`
→ `send confirmation`
→ `DONE / confirmed completion`
→ `Archive eligible`
→ `safe archive`
→ `next cycle`

## 3. Exact-Row Contract

Every runtime action must remain bound to one exact source row and one exact message ID.

Required:

- No stale row index.
- No wrong-row status update.
- No blank sender.
- No blank reply.
- No unresolved literal variable.
- No `#ERROR`.
- No switching to a different row after binding.
- No completion update to any row other than the bound row.
- No row clear or archive before confirmed completion.

## 4. Message Contract

The system must respond to every non-identical message event in order.

Rules:

- A newer message does not silently erase an older valid event.
- Exact duplicates may be suppressed only by a short, explicit duplicate guard.
- A later repeated message must be accepted when it is a new event.
- Replies must use the current bound message and current conversation context.
- Stale replies are forbidden.

## 5. Send Transaction Contract

The permanent Send module must:

1. Receive a dynamic row and expected message ID.
2. Validate inputs before acquiring the Send lock.
3. Acquire the lock only when no other Send owns it.
4. Re-read and validate the exact row.
5. Require `READY_TO_SEND`.
6. Persist and verify `SENDING` before opening TextNow.
7. Use only source-proven TextNow UI actions.
8. Verify the correct conversation and safe compose state.
9. Click Send no more than once.
10. Never automatically retry Send after a possible click.
11. Persist an outcome state.
12. Release the owned lock exactly once.
13. Never release another run's lock.
14. Never mark `DONE` from the Send click alone.
15. Never Archive from the Send module.

Permanent Send outcomes:

- `SEND_CLICKED_AWAITING_CONFIRM`
- `SEND_OUTCOME_UNKNOWN_REVIEW`
- `POST_SEND_STATUS_UPDATE_FAILED`
- `HOLD_PRE_SEND_FAILED`

A later confirmation module consumes `SEND_CLICKED_AWAITING_CONFIRM`.

A later Archive module consumes only independently confirmed completion.

## 6. Approved Plan A Architecture

The approved permanent architecture is:

- Task 71 — `FINAL Send Sheet`: permanent selector only.
- Task 199 — `FINAL Queue Cycle`: permanent queue connection.
- Task 223 — `FINAL Send One Bound Row`: permanent production Send transaction.
- Task 224 — `AIW GATE9 CONTROLLED SEND TEST`: temporary removable Gate 9 launcher.

Only Tasks 71, 199, 223, and 224 may change semantically during Plan A.

Task 224 may hard-code the controlled test row and test ID.

Tasks 71, 199, and 223 must remain free of Gate 9 hard-coded test values.

Removing Task 224 after Gate 9 must not change Tasks 71, 199, or 223.

## 7. Queue Contract

The queue controller may start at most one Send transaction per cycle.

Before choosing `READY_TO_SEND`, the selector must block when any unresolved send state exists, including:

- `SENDING`
- `SEND_CLICKED_AWAITING_CONFIRM`
- `SEND_OUTCOME_UNKNOWN_REVIEW`
- `POST_SEND_STATUS_UPDATE_FAILED`
- `HOLD_PRE_SEND_FAILED`

When blocked:

- no new Send transaction starts;
- Task 223 is not called;
- the cycle reports `SEND_BLOCKED_PENDING_CONFIRM`.

## 8. Lock and Recovery Contract

Every owned-lock terminal path must release the lock exactly once.

Every operation that can time out must have deterministic handling.

For AutoSheets operations:

- clear expected outputs before each read;
- clear `%err` and `%errmsg`;
- Continue Task After Error must be enabled where error routing depends on `%err`;
- numeric error detection only;
- maximum two attempts;
- no infinite retry;
- exact readback for states that authorize TextNow or Send.

After a possible Send click:

- never return automatically to `READY_TO_SEND`;
- never click Send again automatically;
- preserve a non-sendable review state.

## 9. STOP and Live Contract

STOP must prevent new work and release owned locks safely.

Live operation remains blocked until:

- controlled Send passes;
- confirmation passes;
- Archive passes;
- timer/background reliability passes;
- recovery passes;
- capacity ladder passes.

No test package may silently enable live profiles, timer loops, Archive, DeadArchive, Compactor, or capacity behavior.

## 10. Capacity Contract

The intended release target is 50 contacts.

Capacity work must prove:

- no skipped rows;
- no duplicate sends;
- no stale replies;
- no race between processing, sending, and archiving;
- bounded retries;
- ordered handling;
- safe crash/restart behavior;
- controlled API timeout and rate-limit behavior;
- measurable throughput and recovery.

Capacity claims require stress proof and may not be inferred from one-row success.

## 11. Proof Contract

Development proof permits a safe test.

Gate proof locks one behavior.

Release proof requires the complete system.

Phone proof beats static audit.

Tasker import/render proof beats XML parse.

Static reports may support a claim but cannot prove phone behavior.

No tracker increase, merge, release, or unlock occurs without mapped evidence.

## 12. Source and Security Contract

Source truth order is defined in `AIW_CONTROLLER_BOOTSTRAP_CURRENT.md`.

No API key, credential, private token, phone number, or private package may be committed to the public repository.

Private artifacts remain outside Git.

SHA256 must identify every private package used for testing.

## 13. Plan A Completion Boundary

Plan A is complete only when:

- one permanent selector exists;
- one permanent queue connection exists;
- one permanent dynamic Send module exists;
- one removable Gate 9 launcher exists;
- old candidates and diagnostics are removed from active runtime;
- all changed paths are classified;
- every reachable Send path clicks zero or one time;
- every owned lock exit releases safely;
- AutoSheets and AutoInput preservation checks pass;
- actual XML and ZIP pass independent ChatGPT artifact audit;
- phone proof confirms the controlled transaction.

Plan A does not itself unlock Archive, live, capacity, or release.
