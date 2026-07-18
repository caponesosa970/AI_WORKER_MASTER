# AI Worker Full Goal Execution Contract

Status: CURRENT / PERMANENT PRODUCT CONTRACT

This file defines the durable end-to-end behavior required for AI Worker V1. It does not record the active tracker, current gate, active blocker, or candidate status.

## Full Product Goal

AI Worker must:

1. Detect legitimate TextNow messages.
2. Log each legitimate event to the exact authorized Sheet row.
3. Preserve sender, message, message ID, notification identity, timestamps, order, and row identity.
4. Group rapid same-contact messages safely with a maximum group size of four.
5. Preserve different senders in separate groups.
6. Preserve repeated text with a new event ID as a new legitimate event.
7. Suppress only exact duplicate IDs under an explicit duplicate rule.
8. Build bounded confirmed conversation context.
9. Generate a context-aware OpenAI reply.
10. Bind the reply to the exact source row, sender, message, and ID.
11. Open the exact TextNow conversation.
12. Verify thread identity and compose safety.
13. Insert the exact bound reply.
14. Click Send zero or one time.
15. Never automatically retry Send after a possible click.
16. Confirm completion independently.
17. Write `DONE` only after independent confirmation.
18. Archive only independently confirmed exact rows.
19. Recover safely from interruption, plugin failure, restart, and stale state.
20. Run until STOP.
21. Support START, STOP, SAFE, LIVE, STATUS, validation, final interface, and release controls.
22. Meet the intended 50-contact reliability target through bounded, proof-backed capacity testing.

## Exact-Row Contract

Every runtime operation must remain bound to one exact source row and one exact message ID.

Forbidden:

- row switch after binding;
- blank sender;
- blank message;
- blank ID;
- blank or stale reply reaching Send;
- unresolved variable authorizing a write, API call, UI action, Send, DONE, or Archive;
- stale plugin output authorizing a state transition;
- source clear before exact Archive copy/readback proof.

Every Sheet write that affects runtime authority must have exact readback proof before downstream action depends on it.

## Message and Grouping Contract

One legitimate event receives one stable event identity.

Same-contact rapid messages may group only in arrival order and only up to four events.

Five messages partition as `4+1`.

Eight messages partition as `4+4`.

Nine messages partition as `4+4+1`.

Different senders must never share a group.

No legitimate event may be lost, silently overwritten, or hidden by view ordering.

## OpenAI Contract

OpenAI requests must:

- use the exact bound sender/message/context;
- avoid stale prompt or stale reply reuse;
- bound retries;
- handle timeout, rate limit, quota, malformed response, empty response, and unusable body safely;
- never return a row to a sendable state after an unresolved API failure;
- never print, commit, or expose credentials.

## Send Transaction Contract

A Send-capable path must:

- validate row, ID, sender, message, reply, status, authorization, and lock state before UI action;
- persist and verify the send-intent state before opening TextNow;
- open only the exact bound TextNow thread;
- fail closed on ambiguous search results, unknown UI, popup, overlay, login prompt, update prompt, network banner, dirty compose, or unrelated draft text;
- insert only the exact bound reply;
- consume one-shot Send authorization before Send-capable work;
- click Send zero or one time;
- permanently end automatic Send eligibility after any possible click;
- route uncertain click outcome to review without retry;
- never mark `DONE` from Send-click evidence alone;
- never Archive from the Send module;
- release owned locks exactly once and never release another owner.

## Confirmation and DONE Contract

Confirmation must be independent from Send.

`DONE` requires proof that the expected reply reached the correct conversation as the completed outgoing message.

Confirmation must fail closed on wrong thread, wrong reply, missing sent marker, stale UI, unresolved variables, plugin timeout, or uncertain screen state.

## Archive Contract

Archive may occur only after confirmed completion.

Archive must:

- copy the exact confirmed source row;
- read back the copy;
- prove uniqueness or idempotent existing copy;
- clear only the exact source row after copy/readback proof;
- fail closed on mismatch, duplicate conflict, source-row change, or clear uncertainty.

DeadArchive, Compactor, and broad archive drains remain blocked unless specifically proven and authorized in the current controller state.

## Lock, Recovery, and STOP Contract

Every lock must have:

- owner token;
- acquisition proof;
- stale detection;
- active-owner protection;
- success release;
- failure release;
- STOP/restart handling;
- no unowned release;
- no double release;
- no owned leak on terminal paths.

STOP must prevent new work and leave runtime profiles disabled.

Recovery must not retry Send after a possible click, clear another run's lock, skip unresolved events, or hide durable review states.

## UI and Phone Runtime Contract

AutoInput/TextNow behavior requires phone proof for release claims.

Static XML can verify structure and configured selectors, but cannot prove Android, TextNow, keyboard, accessibility, overlay, fold-state, or render behavior.

No guessed AutoInput target is allowed.

Unknown UI state fails closed.

## Capacity and Release Contract

The 50-contact target must map to:

- accepted events;
- completed events;
- skipped or held events;
- duplicate IDs suppressed;
- legitimate repeated messages accepted;
- API attempts and retries;
- permanent failures;
- lock acquisitions/releases;
- group counts and sizes;
- SendCount;
- confirmations;
- Archives;
- queue age;
- cycle duration;
- recovery duration;
- measured and projected throughput.

Capacity proof must not imply a 50-recipient real-Send blast.

Production release requires direct proof for every release claim and independent ChatGPT approval.

No tracker increase, merge, gate closure, phone import, real Send, or release occurs without mapped evidence.
