# AI Worker Locked Facts — Current

Status: CURRENT / CANONICAL
Updated: 2026-07-15
Authority: Phone proof, current GitHub tracker, SHA-verified sources, live Sheet verification, and newest direct Sosa instruction.

## 1. Current Tracker

Current proof level:

`13/14 locked = 93%`

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
13. Gate 13 timer, STOP, background guard, and recovery proof by direct Sosa phone proof.

Current active main gate:

- Gate 14 capacity, reliability ladder, final control interface, and release proof - BLOCKED.

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

## 4. Current Phone-Proven Runtime Baseline

- File: `GATE13R2_FULL_PROJECT_TASKER_IMPORT__CONFIRM_THREAD_NAVIGATION_PRIVATE.xml`
- SHA256: `1C4D13872C3D6B4579AA698F9E7D2F50F3E81467A4CBD4EAD63CD567087832A7`
- Topology: 83 tasks, 4 profiles, 1 scene.
- Current runtime additions include Task 230, `FINAL Device Unlock Probe`, and Task 231, `FINAL Open Bound TextNow Thread No Send`.
- Status: phone-proven Gate 13 runtime baseline.

The credential value remains private and must never be printed or committed.

### Historical Source Records

Historical authoritative V15A AutoInput source:

- File: `basefile_v15a_phone_send_cleanup_pass.xml`
- SHA256: `C4CDEAA0BFD78120386FF1B03FA0A2D6B13BCEEDBD15687F84D03A3AD5FEF1C8`
- Role: Sosa-created authoritative send-path AutoInput source.

Historical Dashgood Search source:

- File: `dashgood-backup.xml`
- SHA256: `62804D52AE6BAB0E0E5895757D56123539F18F99A4E3E9E9060A8BC9C96A8DB7`
- Active source task: Task ID 71.
- Legacy Task ID 270 is excluded.

Historical correct-key full-project Plan A base:

- File: `31A1_FULL_PROJECT_TASKER_IMPORT__DASHGOOD_SEARCH_LANE_CURRENT_KEY_PRIVATE.xml`
- SHA256: `1C1FAF33EA30B69E8F35478AA8E93E58A2AA4ABB967CAA8F5EA927506BBF1B6E`

Current credential source verification SHA:

- `03CDD603FE4D3991BC3E88472BEA6C684F4CE10D0597A429EF5E247859D66925`

The credential value must never be printed or committed.

Rejected 31B reference only:

- File: `31B_FULL_PROJECT_TASKER_IMPORT__AUTOSHEETS_RETRY_CONTROLLED_SEND_PRIVATE.xml`
- SHA256: `156D44624EF534DB8F0D4E81F0E873A44FE8A9560B26D1C260348AFA4ED8B820`
- Status: rejected as Plan A build base.

## 5. Historical Plan A Topology Record

The historical 31A1 full-project base contained:

- 76 tasks.
- 4 profiles.
- 1 scene.

Historical topology at that Plan A stage:

- Task ID 71 is `FINAL Send Sheet`.
- Task ID 199 is `FINAL Queue Cycle`.
- Task 199 called Task 71 three times in that historical base.
- Task IDs 223 and 224 were old unreferenced candidates at that stage.
- Tasks 223 and 224 had no incoming Perform Task reference at that stage.
- No profile or scene directly invoked Tasks 223 or 224 at that stage.
- Tasks 223 and 224 shared duplicate XML `sr="task223"` before Plan A corrected that historical topology.

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
- Gate 13 launcher and proof reruns;
- broad Archive integration outside Task 227 to Task 226;
- DeadArchive;
- Compactor;
- TT5;
- unattended production live operation;
- Gate 14 capacity testing;
- final control-interface release;
- production release.

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

<!-- GATE13R2_LOCKED_FACTS_START -->
## Gate 13R2 Confirmation-Recovery Navigation Facts

- Direct Sosa phone proof showed startup recovery routed exactly once to Task 225 and failed closed on the Chats list as `CONFIRM_UI_HOLD`.
- No Send, DONE, Archive, profile, or unsafe Sheet action occurred; the awaiting-confirm row remained unchanged.
- Gate 13 remains HOLD at `12/14 locked = 86%`.
- Gate 13R2 uses base SHA `CF955572B9EB7F9700E8563AFC6522427ECFE53576DEBF4E5F089BFD1F6A4BC6`.
- New Task 231 copies the Task 223 navigation lane through exact contact selection and the following wait, stopping before `MESSAGE_BOX`, compose focus, reply typing, or Send.
- Task 225 alone is changed among existing tasks; 81/81 other existing task blocks, all profiles, and the scene remain raw-byte identical.
- Task 225's existing exact sender, unique exact reply, immediate `Sent`, DONE readback, and confirmation-lock cleanup remain the confirmation authority.
- Gate 13R2 is a static candidate only. Phone import and phone proof remain blocked pending ChatGPT full artifact audit.
<!-- GATE13R2_LOCKED_FACTS_END -->

<!-- GATE13_PHONE_PROOF_CLOSURE_START -->
## Gate 13 Phone-Proof Closure

- Authority: newest direct Sosa phone proof supplied on 2026-07-14. Codex records this proof and does not claim it independently.
- Gate 13R2 full-project import and render passed on the phone.
- The Android unlock probe passed both visibly unlocked and active locked-screen cases.
- Controlled scheduled timer proof showed one tick; busy overlap returned `TICK_SKIPPED_BUSY` with zero Queue Cycle calls; screen-off returned `TICK_SKIPPED_SCREEN_OFF`.
- STOP-before-tick prevented scheduled work. STOP during a pending transaction preserved the unowned lock. Clean STOP returned `STOPPED_CLEAN`.
- Startup held on an active non-stale busy lock without releasing it and safely released a stale busy lock.
- An unresolved `SENDING` row stayed non-sendable with zero Send retry.
- Awaiting-confirm recovery autonomously opened the exact thread, independently proved the exact reply and immediate `Sent`, changed only the bound row to `DONE`, and made zero Send and Archive calls during confirmation.
- DONE recovery archived exact rows one at a time with copy, readback, uniqueness, and source-clear proof.
- Clean startup returned `RECOVERY_SAFE` and `STARTED_SAFE`, enabling only TextNow Trigger and Every 2m Tick.
- Final STOP disabled all four profiles before the next scheduled tick; no Tick, Live Guard, Queue Cycle, Router, Send, Confirm, or Archive task ran after STOP.
- Gate 13 is `LOCKED / PASS`. Operational tracker is `13/14 locked = 93%`.
- This closure supersedes the earlier Gate 13, Gate 13R1, and Gate 13R2 candidate/HOLD sections above without deleting their historical evidence.
- Fold-state and battery/background-restriction behavior are not claimed by this closure and remain Gate 14 release limitations.
- Gate 14 capacity, final control-interface validation, and release proof remain blocked.
<!-- GATE13_PHONE_PROOF_CLOSURE_END -->

<!-- GATE14B_LOCKED_FACTS_START -->
## Gate 14A Closure And Gate 14B Candidate Facts

- Gate 14A R2 read-only inventory passed the direct Sosa 1/5/10/25/50 phone ladder; Codex records but does not claim that phone proof.
- Every passing inventory run used one read, all defect counters were zero, and staged rows remained unchanged.
- Gate 14A proves read-only count/order/uniqueness visibility, not production 50-contact processing.
- Gate 14B uses exact base SHA256 `73E8048D8941C0529A26E397FA9E6EBAF84FAB9C0F03D3C56CBA163932C34662`.
- Only existing Tasks 166, 172, and 173 change; Tasks 233 and 234 are added; 81/81 protected tasks remain raw-byte equal.
- Gate 14B static validators PASS/PASS; phone proof does not exist.
- Tracker remains `13/14 locked = 93%`; Gate 14 and release remain blocked.
<!-- GATE14B_LOCKED_FACTS_END -->

<!-- GATE14C_LOCKED_FACTS_START -->
## Gate 14B Phone Closure And Gate 14C Verified Closure Facts

- Direct Sosa phone proof locks the Gate 14B processor transaction subproof: SUCCESS, WRONG_ID_HOLD, PARTIAL_AFTER_REPLY_HOLD, FAILURE_COMMIT, exact readback, and owned-lock release passed.
- The accidental repeat of the completed partial mode safely held before lock acquisition or Sheet mutation.
- Codex records but does not independently claim the Gate 14B phone proof.
- Gate 14C direct runtime base is Gate 14B SHA256 `46880D2B0C7E444195E0BA4F587957E86475A95D0F1737CA42218452E4C49C9B`.
- Gate 14C changes existing Tasks 70, 171, 173, 192, and one exact Task 233 regex; it adds Tasks 235, 236, and 237.
- Task 233 remains 1947 actions and newly accepts `ERROR_OPENAI_REVIEW` only in its existing `COMMIT_FAILURE` status guard.
- Task 235 permits no more than two HTTP attempts and one randomized 2-4 second retry.
- Final OpenAI failures persist as exact-row `ERROR_OPENAI_REVIEW`; no production Gate 14C path creates another `ERROR_OPENAI_RETRY`.
- Legacy `ERROR_OPENAI_RETRY` rows migrate to `ERROR_OPENAI_REVIEW` without an API call or reset to NEW.
- The original Gate 14C candidate SHA256 `71A766AE8D550C139AABCEC53DE3B1025CAF26C68561583CBF20AC6D5A5138B3` is historical and superseded by R1.
- Direct Sosa phone proof establishes `QUOTA_429_NO_RETRY` passed and `TIMEOUT_EXHAUSTED` failed safely, but the timeout result exposed an unresolved no-response-code literal.
- `ISSUE_G14C_NO_RESPONSE_CODE_UNRESOLVED_LITERAL` is repaired only in the Gate 14C R1 candidate by setting the per-attempt response code to numeric `0` and classifying code `0` as bounded missing response code.
- Gate 14C R1 phone-proven runtime XML SHA256 is `535A163DA2FCEF1A655AB7DBBA4EBE5E9A991C7BF63CD74525244820D4BCA2A1`.
- Direct Sosa proof passed R1 import/render and all five controlled modes: real success, rate-limit then success, timeout exhaustion with code 0, quota/no-retry, and legacy retry migration.
- Attempts remained capped at two, retries at one, and no third HTTP attempt occurred.
- Exact `ERROR_OPENAI_REVIEW` persistence and every owned processing-lock release passed.
- Legacy migration made zero API calls, acquired no processing lock, preserved blank Reply, and fresh exact-row readback confirmed the review status.
- `ISSUE_G14C_NO_RESPONSE_CODE_UNRESOLVED_LITERAL` is closed by direct Sosa R1 phone proof.
- Gate 14C is verified closed; Gate 14D capacity is next.
- Tracker remains `13/14 locked = 93%`; production 50-contact capacity, final controls, merge, and release remain blocked.
<!-- GATE14C_LOCKED_FACTS_END -->

<!-- GATE14D_LOCKED_FACTS_START -->
## Gate 14D Controlled Capacity Candidate Facts

- Gate 14C R1 is closed by direct Sosa phone proof; its phone-proven XML SHA256 is `535A163DA2FCEF1A655AB7DBBA4EBE5E9A991C7BF63CD74525244820D4BCA2A1`.
- Gate 14D adds only Tasks 238 and 239; all 89 existing task blocks are raw-byte identical.
- Task 238 is limited to controlled synthetic rows 149-198, ascending order, and counts 5/10/25/50.
- Each row requires exact A/B/C, NEW, and blank Reply before one per-row processing lock is acquired.
- Existing bounded Tasks 166/170/171/198/172/173 remain the processing authority.
- An exact terminal readback and owned-lock release are required before another row can start.
- Task 239 has no production/profile/scene caller and consumes one-shot authorization before calling Task 238.
- New-task TextNow, Send, confirmation, DONE, Archive, Queue Cycle, profile, timer, and live paths are absent.
- Static validators PASS/PASS; no Gate 14D phone proof or capacity claim exists.
- Tracker remains `13/14 locked = 93%` with 50 checkpoints remaining; import, merge, live mode, and release remain blocked.
<!-- GATE14D_LOCKED_FACTS_END -->

## Gate 14D R1 Candidate Facts

- Direct Sosa proof showed the first Gate 14D candidate completed row 149, then failed closed before row 150 processing because a generated AutoSheets array element retained row 149's Reply.
- The failure caused no duplicate lock, API call, write, Send, confirmation, DONE, or Archive action; rows 150-153 remained unchanged.
- R1 uses exact base SHA256 `A7C577E6929E930938F0D48937332D19F441D2C1FFD9821E7047E397ECE74C07`.
- R1 changes Task 238 only: ten explicit generated-element clears, five before each exact-row Get Data action.
- All other 90 task blocks, all profiles, the scene, project registry, and credential remain unchanged.
- Static validators PASS/PASS; R1 has no phone proof and is not approved for import.
- Tracker remains `13/14 locked = 93%`; 50 checkpoints remain; capacity, interface, merge, live operation, and release remain blocked.

## Gate 14D Capacity Closure And Gate 14D2 Candidate Facts

- Direct Sosa phone proof passes controlled processing at 5, 10, 25, and 50 rows; the 50-row run completed exact rows 149-198 with all defect counters zero and balanced 50/50 locks.
- Codex records but does not independently claim that phone proof.
- Active duplicate behavior is exact event-ID equality in `TT5 Simple Sheet Duplicate Guard`.
- The fingerprint assignment, age calculation, 180-second condition, duplicate log, Stop, and End If in `FINAL Simple` are historical and disabled; no active TTL claim is allowed.
- Gate 14D2 uses exact base SHA256 `72D5F636AE72F441ACD2BF1C0C9B5B93FFF8503775FA3CA05C59A9111389CDE4`.
- Gate 14D2 adds two isolated tasks and changes none of the 91 existing task blocks.
- Topology is 93 tasks / 4 disabled profiles / 1 scene; static validators PASS/PASS.
- Visible planning tracker is 43 total, 28 phone/runtime, 15 non-phone; main tracker remains `13/14 locked = 93%`.
- Phone import, target-phone modes, overflow, merge, live operation, interface, hardening, and release remain blocked.

## Historical Rejected Gate 14D3 Diagnostic Facts

The candidate described in this section is superseded by Gate 14D3 R1 below. It is retained only as a historical processing-window diagnostic.

- Direct Sosa phone proof passes same-sender ordering, later-repeat acceptance under a unique event ID, and exact duplicate-ID suppression.
- The duplicate test suppressed one existing event ID, kept one unique control ID eligible, and made zero API calls, processing-lock calls, or Sheet writes; the controlled rows remained unchanged.
- Codex records but does not independently claim this phone proof.
- Gate 14D3 uses exact base SHA256 `3851E073BE042F80068E52CF7E3D410ED3D0EBA8A63C5F4C10108532912FE0EA`.
- Gate 14D3 adds two isolated tasks and changes none of the 93 existing task blocks.
- Admission mode reaches only existing bounded rows 149-198 and independently proves row 199 remains exact NEW with blank Reply.
- Deferred-drain mode binds and processes only row 199 through the existing bounded processor lane.
- Topology is 95 tasks / 4 disabled profiles / 1 scene; static validators PASS/PASS.
- Visible planning tracker is 40 total, 25 phone/runtime, 15 non-phone; overflow/admission is the one remaining Gate 14D checkpoint.
- This package is rejected as overflow proof. Phone import and phone testing are prohibited.

## Gate 14D3 Correction And R1 Candidate Facts

- The first Gate 14D3 package is rejected as overflow proof because it called the already-proven controlled rows 149-198 processor and never exercised production OverflowInbox admission or drain.
- Rejected source and commit history are preserved; the package is a diagnostic only and is not approved for import or phone testing.
- Direct Gate 14D3 R1 base SHA256 is `3851E073BE042F80068E52CF7E3D410ED3D0EBA8A63C5F4C10108532912FE0EA`.
- The production logger still reaches `TT5 Log Current Message To OverflowInbox`; the permanent queue still reaches `TT5 Overflow Drain One` through `TT5 Overflow Drain Cap`.
- R1 centralizes both wrappers through one exact transaction engine and places the normal Sheet1 slot selector under the same owned admission lock.
- Admission scans exact IDs across Sheet1 and OverflowInbox, verifies the exact blank destination, writes one PENDING row, reads it back, and requires post-write cross-store count exactly one.
- Drain selects the earliest PENDING source, verifies its exact A:N fields, checks Sheet1 for an existing exact ID, writes at most one exact A:I row, reads it back before DRAINED, and reads DRAINED back before success.
- A PENDING source plus one exact matching Sheet1 row follows the source-only recovery path and cannot write a second main row.
- A completed controlled rerun verifies DRAINED plus the exact existing main row and performs zero writes.
- Four existing overflow/admission-specific tasks change; 89 existing tasks, all profiles, and scene remain raw-byte identical.
- No new OpenAI, TextNow, Send, confirmation, DONE, Archive, timer, live, or profile path exists.
- R1 has no phone proof. Planning tracker remains 40/25/15 and main remains `13/14 locked = 93%`.

## Gate 14D3 R2 Second-Audit Candidate Facts

- Gate 14D3 R1 is superseded and remains `DO NOT IMPORT / DO NOT PHONE TEST`.
- R2 again uses exact Gate 14D2 base SHA256 `3851E073BE042F80068E52CF7E3D410ED3D0EBA8A63C5F4C10108532912FE0EA`.
- R2 candidate XML SHA256 is `149D4877B08B2A730CA7B524941E257AE8550C44C9BB7AA9247092C63CDC9ED5`.
- R2 topology is 97 tasks / 4 disabled profiles / 1 scene.
- Permanent owner-token locks replace unowned hard release and eight-second age stealing.
- `OriginalID` and `OverflowID` are distinct; duplicate, collision, and duplicate-main classifications fail closed.
- Every new AutoSheets read deletes indexed arrays first and is bounded to two attempts.
- Views are candidate hints only; direct target-row reads are transaction authority.
- Drain order is LoggedAt then source row and persists DRAINING, MAIN_COMMITTED, DRAINED, or OVERFLOW_REVIEW through exact readback.
- Configured V1 overflow capacity is 999 data rows, source rows 2-1000; capacity cannot overwrite.
- R2 has no phone proof. Gate 14D remains open; tracker remains 40/25/15 and `13/14 locked = 93%`.

## Gate 14D3 R3 Exact Drain Failure Evidence Candidate Facts

- R2 is superseded and is `HOLD / DO NOT IMPORT / DO NOT PHONE TEST`.
- R2 acquired the shared admission lock before exact source binding and verified `DRAINING`; it also lacked durable Attempts/LastError evidence on every bound failed drain.
- R3 uses the exact Gate 14D2 base SHA256 `3851E073BE042F80068E52CF7E3D410ED3D0EBA8A63C5F4C10108532912FE0EA`.
- R3 candidate XML SHA256 is `04E09D4059D1B314AEDAD89580043B50200EA57C70ACD8C9382802DF1B6F21F7`.
- R3 topology remains 97 tasks / 4 disabled profiles / 1 scene.
- Drain now acquires overflow ownership, binds and verifies the exact source, and persists verified `DRAINING` before acquiring shared admission ownership.
- Every exact-source-bound failed drain reaches one bounded exact Attempts/LastError write/readback path before release unless evidence was already verified.
- Existing changed tasks remain 33, 35, 68, 215, 217, 218, 219, and 220; Tasks 242-245 remain the only additions; 85/85 other tasks are raw-byte identical.
- Structure validator 367/367 PASS and semantic validator 69/69 PASS. R3 has no phone proof and is not approved for import.
- Gate 14D remains open; tracker remains 40/25/15 and `13/14 locked = 93%`.

## Gate 14D3A Durable Owned Admission Candidate Facts

- R3 integrity passed but runtime scope is rejected. R3 is design history only and is `DO NOT IMPORT / DO NOT PHONE TEST`.
- D3A rebuilds from exact Gate 14D2 SHA256 `3851E073BE042F80068E52CF7E3D410ED3D0EBA8A63C5F4C10108532912FE0EA`.
- D3A candidate XML SHA256 is `880CC569185A9FFF45703EC77E71D6260A88474B0F63ECDE6B31E0A11CFF090A`.
- Topology is 99 tasks / 4 disabled profiles / 1 scene.
- Existing changes are exactly Tasks 68, 215, and 217. Tasks 242-247 are added. The other 90 existing tasks are raw-byte identical.
- Every added helper is below 500 actions; maximum is 494.
- Sheet1 blank authority is exact A:Z. OverflowInbox admission is limited to physical rows 2-986.
- Identity checks Sheet1, OverflowInbox, Archive, and DeadArchive before any admission write.
- Tasks 218-220 and Queue Cycle Task 199 remain raw-byte identical. D3B and D3C remain deferred.
- Validators pass 450/450 and 559/559. D3A has no phone proof and is not approved for import.
- Gate 14D remains open; tracker remains 40/25/15 and `13/14 locked = 93%`.
