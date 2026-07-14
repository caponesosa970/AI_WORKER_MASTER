# AI Worker Locked Facts — Current

Status: CURRENT / CANONICAL
Updated: 2026-07-14
Authority: Phone proof, current GitHub tracker, SHA-verified sources, live Sheet verification, and newest direct Sosa instruction.

## 1. Current Tracker

Current proof level:

`12/14 locked = 86%`

Locked main gates:

1. Group B2 dry-run UI proof.
2. Group C2 controlled one-send proof.
3. Group D controller/timer-safe proof.
4. Group E maintenance/recovery proof.
5. Group F 22D trigger-only proof.
6. Group F 22J trigger-to-queue proof.
7. Group G process-only exact-row proof.
8. Controlled queue-cycle proof.
9. Gate 9 controlled Send proof by direct Sosa phone proof.
10. Gate 10 independent confirmation and DONE proof by direct Sosa phone proof.
11. Gate 11 exact-row Archive proof by direct Sosa phone proof.
12. Gate 12 permanent queue lifecycle integration proof by direct Sosa phone proof.

Current active main gate:

- Gate 13 timer, STOP, background guard, and recovery — CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT.

No percentage increase is authorized without new phone proof.

## 2. Locked Send-Path Subproofs

Locked:

- Gate 9A non-UI send readiness.
- Gate 9B0 manual TextNow identity.
- Gate 9B1A TextNow search navigation.
- Gate 9B1B manual thread identity.
- Gate 9B1C no-send compose safety inspection.
- Gate 9B1D manual compose focus.
- Gate 9B1E manual draft insert and clear.
- Gate 9B1F exact reply compose dry-run.
- 27B no-send guard.

## 3. Current Phone-Proven Search Result

30B1 phone result:

- Full-project import/render passed.
- V15A ID `menu_search` timed out.
- Active Dashgood Search recovery reached the TextNow Search screen.
- Both `search_field` actions completed.
- Final visible state was the Search field focused with keyboard open.
- No number was typed.
- No contact was selected.
- No compose, Send, DONE, Archive, live, or Sheet action ran.

Interpretation:

- The Dashgood Search lane is the accepted development source for the current Search behavior.
- Do not treat the Text `Search` action error alone as fatal when the Search field is subsequently reached.
- Intermediate wrapper PASS markers are not final proof.
- Successful Search-field reach is the positive end-state check.

## 4. Current Verified Source Files

Authoritative V15A source:

- File: `basefile_v15a_phone_send_cleanup_pass.xml`
- SHA256: `C4CDEAA0BFD78120386FF1B03FA0A2D6B13BCEEDBD15687F84D03A3AD5FEF1C8`
- Role: Sosa-created authoritative send-path AutoInput source.

Dashgood active source:

- File: `dashgood-backup.xml`
- SHA256: `62804D52AE6BAB0E0E5895757D56123539F18F99A4E3E9E9060A8BC9C96A8DB7`
- Active source task: Task ID 71.
- Legacy Task ID 270 is excluded.

Current correct-key full-project Plan A base:

- File: `31A1_FULL_PROJECT_TASKER_IMPORT__DASHGOOD_SEARCH_LANE_CURRENT_KEY_PRIVATE.xml`
- SHA256: `1C1FAF33EA30B69E8F35478AA8E93E58A2AA4ABB967CAA8F5EA927506BBF1B6E`

Current credential source verification SHA:

- `03CDD603FE4D3991BC3E88472BEA6C684F4CE10D0597A429EF5E247859D66925`

The credential value must never be printed or committed.

Rejected 31B reference only:

- File: `31B_FULL_PROJECT_TASKER_IMPORT__AUTOSHEETS_RETRY_CONTROLLED_SEND_PRIVATE.xml`
- SHA256: `156D44624EF534DB8F0D4E81F0E873A44FE8A9560B26D1C260348AFA4ED8B820`
- Status: rejected as Plan A build base.

## 5. Verified Current Topology for Plan A

The 31A1 full-project base contains:

- 76 tasks.
- 4 profiles.
- 1 scene.

Verified topology:

- Task ID 71 is `FINAL Send Sheet`.
- Task ID 199 is `FINAL Queue Cycle`.
- Task 199 calls Task 71 three times in the current base.
- Task IDs 223 and 224 are old unreferenced candidates.
- Tasks 223 and 224 have no incoming Perform Task reference.
- No profile or scene directly invokes Tasks 223 or 224.
- Tasks 223 and 224 currently share duplicate XML `sr="task223"` and must be corrected in Plan A.

## 6. Locked Plan A Decision

Plan A is the approved architecture.

Historical Plan A active roles before Gates 10-12:

- Task 71 — permanent selector only.
- Task 199 — permanent queue connection, one selector call per cycle.
- Task 223 — permanent dynamic `FINAL Send One Bound Row`.
- Task 224 — temporary removable Gate 9 launcher at that historical stage.

That historical four-task build boundary is superseded by the current Gate 12 boundary above. Gate 12 may change existing Tasks 199 and 224, add Task 227, and register Task 227 only. All other pre-existing runtime nodes remain protected.

Old candidate names must be absent from active runtime:

- `AIW27B_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE`
- `AIW31A_DASHGOOD_SEARCH_LANE_CONTROLLED_SEND_CANDIDATE`
- `AIW31B_AUTOSHEETS_RETRY_CONTROLLED_SEND_CANDIDATE`

Removed source must be retained privately in `PRIVATE_WITH_KEY\PLAN_A_GULAG\`.

## 7. Current Sheet Safety State

Newest direct Sosa phone proof records:

- Gate 9 sent the exact bound reply once.
- Gate 10 independently confirmed the exact sent reply and wrote `DONE`.
- Gate 11 copied the exact row once, verified the Archive copy, cleared only that source row, released the Archive lock, and returned `ARCHIVE_DONE_VERIFIED`.
- Archive contains exactly one matching copy.
- Private row, recipient, and message values remain excluded from public files.
- Codex did not read or change the live Sheet.

A fresh live Sheet read is mandatory before any future test or mutation.

## 8. Blocked Paths

Blocked until separately proven:

- Gate 12 controlled launcher rerun;
- Gate 13 phone import until ChatGPT audits the actual XML and ZIP;
- Gate 13 phone proof and tracker advancement beyond 12/14;
- broad Archive integration outside Task 227 to Task 226;
- DeadArchive;
- Compactor;
- TT5;
- timer/live and recovery;
- capacity;
- release/production.

## 10. Gate 12R1 Candidate Boundary - Historical Build Record

- The original Gate 12 candidate is rejected because Tasker substituted `%par1` and `%par2` inside the mode-normalization regex text.
- Gate 12R1 changes only Task 199 act4/rhs and act7/rhs from the rejected Gate 12 base.
- Both repaired RHS fields use the literal regex `(?is)^\s*$|^%.*$` and contain no dynamic `%par1` or `%par2` reference.
- Task 199 routes lifecycle work before processing or new Send selection.
- Task 227 may call Task 225 or Task 226 once, but never both in one cycle.
- Task 71 remains the only caller of Task 223.
- Task 199 no longer calls `QUEUE Archive Drain Silent`.
- Controlled Gate 12 mode performs no processing, maintenance, recursion, profile change, or live activation.
- The current phone-proven SourceRow range remains 2 through 201; expansion is a later capacity/release requirement.
- Static validation was not Gate 12 phone proof. Direct Sosa phone proof later locked Gate 12.

## 9. Locked Safety Rules

- Phone proof beats static audit.
- Tasker import/render proof beats XML parse.
- SHA proof beats filename.
- Do not invent AutoInput targets.
- Do not reopen locked work without newer direct proof.
- No wrong-recipient Send.
- No stale reply Send.
- No duplicate Send.
- No DONE before independent Send confirmation.
- No Archive before confirmed completion.
- No automatic Send retry after a possible click.
- No owned-lock exit without release.
- No unowned-lock release.
- No tracker increase without proof.
- No API key or private token in public GitHub files.
- Codex does not approve phone import and does not claim phone proof.

<!-- GATE13_LOCKED_FACTS_START -->
## Gate 13 Candidate Facts

- Gate 12 is locked by direct Sosa phone proof; Codex records and does not claim that proof.
- Gate 13 build base SHA is `3DC49BF47837403B36D1B213564F34BD6983598B6734429324FF0ACEDA7A23C8`.
- STOP disables timer and trigger profiles before changing worker state and never clears an active transaction lock.
- Startup recovery requires a stale timestamp and queue-state evidence before releasing any supported lock.
- `SENDING` remains non-sendable and is never restored to `READY_TO_SEND`.
- One tick calls Queue Cycle once maximum.
- Returned XML profiles remain disabled.
- Timer/live and Gate 13 proof remain blocked pending direct phone evidence.
<!-- GATE13_LOCKED_FACTS_END -->

<!-- GATE13R1_LOCKED_FACTS_START -->
## Gate 13R1 Android 16 Unlock-Probe Facts

- Direct Sosa phone proof showed the Gate 13 `%KEYG` guard falsely held while Tasker was foreground and the phone was visibly unlocked.
- The stop was safe: no profile, tick, Queue Cycle, lifecycle module, or Sheet path ran.
- Gate 13 remains HOLD at `12/14 locked = 86%`.
- Gate 13R1 replaces only the `%KEYG` guard in Tasks 130, 224, and 228 with one call to Task 230 and an explicit `UNLOCKED` result check.
- Task 230 uses `KeyguardManager.isDeviceLocked()` and `isKeyguardLocked()` and fails closed on errors or ambiguous values.
- Protected lifecycle Tasks 71, 199, 223, 225, 226, 227, and recovery Task 229 remain raw-byte identical.
- No profile is enabled in the artifact. No Sheet cell was changed. Tasker was not run.
- Gate 13R1 is a static candidate only; Android execution and the repeated busy-timer test remain blocked pending ChatGPT artifact audit and direct phone proof.
<!-- GATE13R1_LOCKED_FACTS_END -->
