# AI Worker Locked Facts — Current

Status: CURRENT / CANONICAL
Updated: 2026-07-13
Authority: Phone proof, current GitHub tracker, SHA-verified sources, live Sheet verification, and newest direct Sosa instruction.

## 1. Current Tracker

Current proof level:

`8/14 locked = 57%`

Locked main gates:

1. Group B2 dry-run UI proof.
2. Group C2 controlled one-send proof.
3. Group D controller/timer-safe proof.
4. Group E maintenance/recovery proof.
5. Group F 22D trigger-only proof.
6. Group F 22J trigger-to-queue proof.
7. Group G process-only exact-row proof.
8. Controlled queue-cycle proof.

Current active main gate:

- Gate 9 controlled Send path — HOLD.

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

Final active roles:

- Task 71 — permanent selector only.
- Task 199 — permanent queue connection, one selector call per cycle.
- Task 223 — permanent dynamic `FINAL Send One Bound Row`.
- Task 224 — temporary removable Gate 9 launcher.

Only Tasks 71, 199, 223, and 224 may change semantically.

Old candidate names must be absent from active runtime:

- `AIW27B_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE`
- `AIW31A_DASHGOOD_SEARCH_LANE_CONTROLLED_SEND_CANDIDATE`
- `AIW31B_AUTOSHEETS_RETRY_CONTROLLED_SEND_CANDIDATE`

Removed source must be retained privately in `PRIVATE_WITH_KEY\PLAN_A_GULAG\`.

## 7. Current Sheet Safety State

Last live verified state on 2026-07-13:

- Row 75 ID: `AIW9B1G-STAGED-20260709-01`
- Row 75 status: `TEST_STAGED_NO_SEND`
- Row 75 reply is populated.
- Row 75 is not authorized for Send.

A fresh live Sheet read is mandatory before any future test or mutation.

## 8. Blocked Paths

Blocked until separately proven:

- uncontrolled Send;
- DONE write;
- Archive;
- DeadArchive;
- Compactor;
- TT5;
- timer/live;
- capacity;
- release/production.

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
