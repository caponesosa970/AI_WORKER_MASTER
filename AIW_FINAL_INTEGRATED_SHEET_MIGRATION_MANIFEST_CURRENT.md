# AIW Final Integrated Sheet Migration Manifest - Conversation Continuity P1 R2

Status: `PLAN ONLY / NOT APPLIED / HOLD FOR CONTROLLER APPROVAL`

This is the complete non-destructive migration authority for the Option A Phase 1 R2 candidate. It has no dependency on an older manifest. It incorporates the controller-supplied live dimensions below. Codex did not open or mutate the live workbook, reconcile historical rows, or select a fixture row.

## Safety boundary

- Make a named full-workbook backup and record its revision before any change.
- Keep the worker stopped, all Tasker profiles disabled, and all validation fixture authorization closed during migration.
- Do not rename, clear, reorder, or overwrite existing `Sheet1`, `Archive`, `DeadArchive`, or `OverflowInbox` data.
- Preserve `Sheet1` rows `144:147` exactly. They are occupied/protected and are never fixtures.
- `Archive` row 999 and `DeadArchive` row 999 are not fixtures. The row expansions below exist only because preserved bounded production reads use row 1000.
- Do not select or guess validation fixture rows. They remain dynamic controller inputs after fresh read-only bounds and blankness proof.
- Views are hints. Exact direct-row reads, identity checks, and readbacks remain write authority.
- `DeadArchive`, Compactor, broad Archive drain, and legacy maintenance remain unreachable.
- Every grid size below is a minimum runtime requirement. Never shrink a row count, column count, existing grid range, extension column, or populated cell.
- Preserve `SystemConfig!A1:J2`, `Sheet1!J:CY`, `QueueView!K:Z`, `OverflowInbox!O:CN`, `Archive!K:Z`, and `DeadArchive!N:CI` exactly.
- Preserve every other existing cell outside an explicitly approved formula anchor or the controller-approved `SystemConfig!A3:D16` block.

## Controller-supplied live grid and minimum-requirement matrix

The controller must freshly re-read this matrix before applying the plan. A larger live grid is preserved. Row expansion never authorizes a data write.

| Tab | Existing grid | Minimum required grid | Actual authorized operation | Runtime maximum / privacy |
|---|---:|---:|---|---|
| `SystemConfig` | 1000 x 26 | 100 x 4 | preserve grid and A1:J2; after fresh blank proof write A3:D16 only | lookup A:B / internal configuration |
| `Sheet1` | 980 x 103 | 980 x 26 | preserve; no resize or header rewrite | payload rows 2:201; protected A:Z / private production data |
| `QueueView` | 979 x 26 | 201 x 10 | preserve grid and K:Z; preserve A1 formula when exact match | rows 2:201 / private derived data |
| `Sheet1SlotView` | missing | 2 x 1 | create tab and exact formula anchor | row 2 / internal derived data |
| `OverflowInbox` | 986 x 92 | 986 x 14 | preserve; no resize or header rewrite | rows 2:986 / private production data |
| `OverflowSlotView` | 1000 x 26 | 2 x 1 | preserve grid; replace only A2 formula anchor | row 2 / internal derived data |
| `OverflowView` | 1000 x 26 | 986 x 15 | preserve grid; replace only A1 formula anchor | rows 2:986 / private derived data |
| `Archive` | 933 x 26 | 1000 x 10 | add 67 rows only; preserve all 26 columns | rows 2:1000 / private production history |
| `DeadArchive` | 972 x 87 | 1000 x 13 | add 28 rows only; preserve all 87 columns | reads A2:A1000 / private production history |
| `IngressJournal` | missing | 1001 x 14 | create tab | rows 2:1001 / private production data |
| `IngressSlotView` | missing | 2 x 1 | create tab and formula | row 2 / internal derived data |
| `IngressView` | missing | 1001 x 15 | create tab and formula | rows 2:1001 / private derived data |
| `IdentityProbe` | missing | 2 x 5 | create tab | row 2 / private transient data |
| `IdentityProbeResult` | missing | 2 x 3 | create tab and formulas | row 2 / private derived data |
| `ProofLedger` | missing | 5001 x 12 | create tab | rows 2:5001 / private proof data |
| `ProofLedgerSlotView` | missing | 2 x 1 | create tab and formula | row 2 / internal derived data |
| `RuntimeState` | missing | 2 x 4 | create tab and seed exact state row | row 2 / private runtime state |
| `ValidationControl` | missing | 3 x 2 | create tab and seed closed controls | rows 2:3 / private validation state |
| `RecoveryProbe` | missing | 2 x 6 | create tab and formulas | row 2 / private derived data |
| `SchemaCheck` | missing | 2 x 6 | create tab and formulas | row 2 / internal derived data |
| `ConversationGroups` | missing | 1000 x 42 | create tab | rows 2:1000 / highly private conversation data |
| `ConversationGroupSlotView` | missing | 2 x 1 | create tab and formula | row 2 / internal derived data |
| `ConversationSchemaCheck` | missing | 2 x 7 | create tab and formulas | row 2 / internal derived data |

## Exact schemas and seed values

### SystemConfig

Preserve `A1:J2` exactly. Do not write or replace row 1. Immediately before migration, re-read `A3:D16` and require every cell blank. Any nonblank, unresolved, errored, or changed value returns migration HOLD.

After that fresh blank proof and separate controller approval, write only these exact rows. Column D remains blank unless the controller supplies the migration timestamp in the same approved operation.

| Row | Key | Value | Description |
|---:|---|---|---|
| 3 | `SchemaVersion` | `AIW_FINAL_V1` | integrated base schema |
| 4 | `MainMaxRow` | `201` | production Sheet1 payload maximum |
| 5 | `OverflowMaxRow` | `986` | OverflowInbox physical/runtime maximum |
| 6 | `JournalMaxRow` | `1001` | IngressJournal physical/runtime maximum |
| 7 | `ReleaseMode` | `FINAL_INTEGRATED` | final integrated candidate mode |
| 8 | `DeadArchiveEnabled` | `0` | unreachable in V1 |
| 9 | `CompactorEnabled` | `0` | unreachable in V1 |
| 10 | `ConversationSchemaVersion` | `AIW_CONVERSATION_V1` | group schema version |
| 11 | `ConversationGroupMaxRow` | `1000` | bounded ConversationGroups maximum |
| 12 | `ConversationMemberCapacity` | `4` | maximum members per group |
| 13 | `ConversationQuietSeconds` | `10` | persisted quiet window |
| 14 | `Sheet1PhysicalMaxRow` | `980` | verified minimum physical row count |
| 15 | `ArchivePhysicalMaxRow` | `1000` | required after audited row addition |
| 16 | `DeadArchivePhysicalMaxRow` | `1000` | required after audited row addition |

### Sheet1

Preserve the existing tab. Required payload headers `A1:I1`:

`ID | Sender | Message | Status | Reply | Touch | Button | Time | Ticker`

Columns `J:CY` are protected extension columns. Preserve their existing headers and values exactly; the R2 candidate does not redefine them. No runtime payload row above 201 is authorized.

### OverflowInbox

Headers `A1:N1`:

`OverflowID | OriginalID | Sender | Message | Status | Reply | TouchAction | ButtonAction | EventTime | Ticker | LoggedAt | Source | Attempts | LastError`

Preserve existing columns `O:CN` and every existing header/value. Existing header aliases in A:N may remain when runtime authority is positional and no schema check requires a rename.

### Archive

Headers `A1:J1`:

`ID | Sender | Message | Status | Reply | Touch | Button | Time | Ticker | ArchivedAt`

Add exactly 67 rows to reach the 1000-row minimum. Preserve columns `K:Z`, all existing 26 columns, and every existing cell. Do not shrink columns and do not seed a row.

### DeadArchive

The candidate contract reads only `A2:A1000` by position. Preserve the existing `A:CI` grid, including `N:CI`, headers, aliases, and all values. Add exactly 28 rows to reach the 1000-row minimum. Do not shrink columns, rewrite a header, or create a row-999 fixture.

### IngressJournal

Headers `A1:N1`:

`JournalID | OriginalID | Sender | Message | Status | Reply | TouchAction | ButtonAction | EventTime | Ticker | LoggedAt | Source | Attempts | LastErrorOrResolvedLocation`

Production progression is exact: `JOURNALED` -> `RESOLVED_MAIN` or `RESOLVED_OVERFLOW`. `JOURNAL_REVIEW` is unresolved review. `RESOLVED_DUPLICATE` is terminal duplicate evidence and is never valid membership proof.

### IdentityProbe

Headers `A1:E1`:

`OriginalID | Sender | Message | ExcludeIngressRow | ExcludeOverflowRow`

Leave `A2:E2` blank.

### ProofLedger

Headers `A1:L1`:

`RunID | Phase | Result | ExactRows | ExactIDs | LockCounts | ReadCount | WriteCount | ErrorCode | StartedAt | FinishedAt | Verification`

Rows are append-only.

### RuntimeState

Headers `A1:D1`:

`Key | Value | UpdatedAt | RunID`

Seed `A2:D2` exactly:

`DesiredRun | 0 | MIGRATION | NONE`

### ValidationControl

Headers `A1:B1`: `Key | Value`

- `A2:B2`: `MainCapacityInjection | NORMAL`
- `A3:B3`: `AuthorizedRunID | NONE`

### ConversationGroups

Schema version: `AIW_CONVERSATION_V1`. Headers `A1:AP1`, exactly in this order:

`SchemaVersion | GroupID | SenderKey | AnchorSheet1Row | AnchorOriginalID | MemberCount | Member1Row | Member1OriginalID | Member2Row | Member2OriginalID | Member3Row | Member3OriginalID | Member4Row | Member4OriginalID | GroupState | QuietCutoffMs | BoundAtMs | ConfirmedReply | RecoveryCount | LastError | LastUpdateMs | ConfirmationState | ArchiveState | FinalizedMemberCount | OwnerToken | OwnerStartedAtMs | LedgerRow | FreezeLoggedAtMs | HistoryReference | HistoryTurnCount | PromptReference | TransitionSequence | BoundMask | ArchivedMask | MemberCapacity | ValidationRunContext | Member1Message | Member2Message | Member3Message | Member4Message | SenderDisplay | FixtureRole`

Leave `A2:AP1000` blank. No group row is preselected.

## Exact view formulas

For a newly created view, enter its formula exactly once in the listed anchor and require the remaining spill range blank. For an existing view, preserve the grid and every cell except the explicitly approved anchor. Preserve `QueueView!A1` when it already matches the formula below; otherwise stop for controller approval. For this migration, the only authorized existing-view replacements are `OverflowView!A1` and `OverflowSlotView!A2`.

### QueueView

`A1`:

```text
={"SourceRow","ID","Sender","Message","Status","Reply","Touch","Button","Time","Ticker";IFNA(FILTER({ROW(Sheet1!A2:A),Sheet1!A2:I},REGEXMATCH(Sheet1!D2:D,"^(NEW|PROCESSING|READY_TO_SEND|SENDING|SEND_CLICKED_AWAITING_CONFIRM|SEND_OUTCOME_UNKNOWN_REVIEW|POST_SEND_STATUS_UPDATE_FAILED|HOLD_PRE_SEND_FAILED|DONE|REVIEW_READY|REVIEW_HOLD|REVIEW_REJECTED|EDIT_REPLY|SKIP_MANUAL)$")),{"","","","","","","","","",""})}
```

### Sheet1SlotView

- `A1`: `TargetRow`
- `A2`: `=IF(AND(ValidationControl!B2="FORCE_MAIN_FULL",ValidationControl!B3<>"NONE"),"FULL",IFERROR(MATCH(TRUE,INDEX(Sheet1!A2:A201="",0),0)+1,"FULL"))`

### OverflowSlotView

- `A1`: `TargetRow`
- `A2`: `=IFERROR(MATCH(TRUE,INDEX(OverflowInbox!A2:A986="",0),0)+1,"FULL")`

### OverflowView

`A1`:

```text
={"OverflowID","OriginalID","Sender","Message","Status","Reply","TouchAction","ButtonAction","EventTime","Ticker","LoggedAt","Source","Attempts","LastError","SourceRow";IFERROR(SORT(FILTER({OverflowInbox!A2:N986,ROW(OverflowInbox!A2:A986)},REGEXMATCH(OverflowInbox!E2:E986,"^(PENDING|DRAINING|MAIN_COMMITTED|OVERFLOW_REVIEW)$")),11,TRUE,15,TRUE),{"","","","","","","","","","","","","","",""})}
```

### IngressSlotView

- `A1`: `TargetRow`
- `A2`: `=IFERROR(MATCH(TRUE,INDEX(IngressJournal!A2:A1001="",0),0)+1,"FULL")`

### IngressView

`A1`:

```text
={"JournalID","OriginalID","Sender","Message","Status","Reply","TouchAction","ButtonAction","EventTime","Ticker","LoggedAt","Source","Attempts","LastErrorOrResolvedLocation","SourceRow";IFERROR(SORT(FILTER({IngressJournal!A2:N1001,ROW(IngressJournal!A2:A1001)},REGEXMATCH(IngressJournal!E2:E1001,"^(JOURNALED|JOURNAL_REVIEW)$")),11,TRUE,15,TRUE),{"","","","","","","","","","","","","","",""})}
```

### IdentityProbeResult

- `A1:C1`: `Classification | MatchCount | Detail`
- `A2`:

```text
=LET(id,IdentityProbe!A2,s,IdentityProbe!B2,m,IdentityProbe!C2,xj,IdentityProbe!D2,xo,IdentityProbe!E2,mainId,COUNTIF(Sheet1!A2:A201,id),mainExact,SUMPRODUCT(N(Sheet1!A2:A201=id),N(Sheet1!B2:B201=s),N(Sheet1!C2:C201=m)),ovId,SUMPRODUCT(N(OverflowInbox!B2:B986=id),N(ROW(OverflowInbox!B2:B986)<>xo),N(REGEXMATCH(OverflowInbox!E2:E986,"^(PENDING|DRAINING|MAIN_COMMITTED|OVERFLOW_REVIEW)$"))),ovExact,SUMPRODUCT(N(OverflowInbox!B2:B986=id),N(OverflowInbox!C2:C986=s),N(OverflowInbox!D2:D986=m),N(ROW(OverflowInbox!B2:B986)<>xo),N(REGEXMATCH(OverflowInbox!E2:E986,"^(PENDING|DRAINING|MAIN_COMMITTED|OVERFLOW_REVIEW)$"))),archiveId,COUNTIF(Archive!A2:A1000,id),deadId,COUNTIF(DeadArchive!A2:A1000,id),jId,SUMPRODUCT(N(IngressJournal!B2:B1001=id),N(ROW(IngressJournal!B2:B1001)<>xj),N(REGEXMATCH(IngressJournal!E2:E1001,"^(JOURNALED|JOURNAL_REVIEW)$"))),jExact,SUMPRODUCT(N(IngressJournal!B2:B1001=id),N(IngressJournal!C2:C1001=s),N(IngressJournal!D2:D1001=m),N(ROW(IngressJournal!B2:B1001)<>xj),N(REGEXMATCH(IngressJournal!E2:E1001,"^(JOURNALED|JOURNAL_REVIEW)$"))),activeId,mainId+ovId+jId,activeExact,mainExact+ovExact+jExact,IF(id="","IDENTITY_PROBE_HOLD",IF(mainId+ovId>1,"DUPLICATE_MAIN_REVIEW",IF(activeId>activeExact,"ID_COLLISION_REVIEW",IF(deadId>0,"EVENT_HISTORY_REVIEW",IF(archiveId>0,"HISTORICAL_DUPLICATE",IF(activeExact>0,"EXACT_DUPLICATE","ELIGIBLE")))))))
```

- `B2`: `=IFERROR(COUNTIF(Sheet1!A2:A201,IdentityProbe!A2)+COUNTIF(OverflowInbox!B2:B986,IdentityProbe!A2)+COUNTIF(Archive!A2:A1000,IdentityProbe!A2)+COUNTIF(DeadArchive!A2:A1000,IdentityProbe!A2)+COUNTIF(IngressJournal!B2:B1001,IdentityProbe!A2)-N(INDEX(IngressJournal!B:B,IdentityProbe!D2)=IdentityProbe!A2)-N(INDEX(OverflowInbox!B:B,IdentityProbe!E2)=IdentityProbe!A2),0)`
- `C2`: `=A2&":"&B2`

### ProofLedgerSlotView

- `A1`: `TargetRow`
- `A2`: `=IFERROR(MATCH(TRUE,INDEX(ProofLedger!A2:A5001="",0),0)+1,"FULL")`

### SchemaCheck

- `A1:F1`: `SchemaVersion | Result | MainMaxRow | OverflowMaxRow | JournalMaxRow | ReleaseMode`
- `A2`: `=IFERROR(VLOOKUP("SchemaVersion",SystemConfig!A:B,2,FALSE),"MISSING")`
- `B2`: `=IF(AND(A2="AIW_FINAL_V1",C2=201,D2=986,E2=1001,F2="FINAL_INTEGRATED"),"PASS","HOLD")`
- `C2`: `=IFERROR(VALUE(VLOOKUP("MainMaxRow",SystemConfig!A:B,2,FALSE)),0)`
- `D2`: `=IFERROR(VALUE(VLOOKUP("OverflowMaxRow",SystemConfig!A:B,2,FALSE)),0)`
- `E2`: `=IFERROR(VALUE(VLOOKUP("JournalMaxRow",SystemConfig!A:B,2,FALSE)),0)`
- `F2`: `=IFERROR(VLOOKUP("ReleaseMode",SystemConfig!A:B,2,FALSE),"MISSING")`

### RecoveryProbe

- `A1:F1`: `Ingress | Admission | Overflow | Queue | AdmissionStaging | AmbiguousDurableState`
- `A2`: `=IF(COUNTIF(IngressJournal!E2:E1001,"JOURNAL_REVIEW")=0,"SAFE_CLEAR","HOLD")`
- `B2`: `=IF(COUNTIF(Sheet1!D2:D201,"ADMISSION_STAGING")=0,"SAFE_CLEAR","HOLD")`
- `C2`: `=IF(SUM(COUNTIF(OverflowInbox!E2:E986,{"DRAINING","MAIN_COMMITTED","OVERFLOW_REVIEW"}))=0,"SAFE_CLEAR","HOLD")`
- `D2`: `=IF(AND(B2="SAFE_CLEAR",C2="SAFE_CLEAR"),"SAFE_CLEAR","HOLD")`
- `E2`: `=IF(COUNTIF(Sheet1!D2:D201,"ADMISSION_STAGING")=0,"CLEAR","RECOVERABLE")`
- `F2`: `=COUNTIF(IngressJournal!E2:E1001,"JOURNAL_REVIEW")+COUNTIF(Sheet1!D2:D201,"ADMISSION_STAGING")+SUM(COUNTIF(OverflowInbox!E2:E986,{"DRAINING","MAIN_COMMITTED","OVERFLOW_REVIEW"}))`

### ConversationGroupSlotView

- `A1`: `TargetRow`
- `A2`: `=IFERROR(MATCH(TRUE,INDEX(ConversationGroups!A2:A1000="",0),0)+1,"FULL")`

This is a hint only. Runtime still performs exact direct-row `A:AP` blank proof before group creation.

### ConversationSchemaCheck

- `A1:G1`: `SchemaVersion | Result | GroupPhysicalMax | GroupConfiguredMax | ArchivePhysicalMax | Sheet1PhysicalMax | JournalPhysicalMax`
- `A2`: `=IFERROR(VLOOKUP("ConversationSchemaVersion",SystemConfig!A:B,2,FALSE),"MISSING")`
- `B2`:

```text
=IF(AND(A2="AIW_CONVERSATION_V1",C2=1000,D2=1000,C2>=D2,E2=1000,F2=980,G2=1001,TEXTJOIN("|",FALSE,ConversationGroups!A1:AP1)="SchemaVersion|GroupID|SenderKey|AnchorSheet1Row|AnchorOriginalID|MemberCount|Member1Row|Member1OriginalID|Member2Row|Member2OriginalID|Member3Row|Member3OriginalID|Member4Row|Member4OriginalID|GroupState|QuietCutoffMs|BoundAtMs|ConfirmedReply|RecoveryCount|LastError|LastUpdateMs|ConfirmationState|ArchiveState|FinalizedMemberCount|OwnerToken|OwnerStartedAtMs|LedgerRow|FreezeLoggedAtMs|HistoryReference|HistoryTurnCount|PromptReference|TransitionSequence|BoundMask|ArchivedMask|MemberCapacity|ValidationRunContext|Member1Message|Member2Message|Member3Message|Member4Message|SenderDisplay|FixtureRole"),"PASS","HOLD")
```

- `C2`: `=ROWS(ConversationGroups!A:A)`
- `D2`: `=IFERROR(VALUE(VLOOKUP("ConversationGroupMaxRow",SystemConfig!A:B,2,FALSE)),0)`
- `E2`: `=ROWS(Archive!A:A)`
- `F2`: `=ROWS(Sheet1!A:A)`
- `G2`: `=ROWS(IngressJournal!A:A)`

## Dynamic fixture contract

No row number appears in runtime as a fixture default. After migration is separately approved and applied, the controller must select each validation row from a fresh read-only inspection and prove:

1. exact tab and physical maximum;
2. exact protected range;
3. every cell blank;
4. no prior Gate or production record;
5. unique validation run ID, role, expected identity, sender, message, status, and one-shot authorization;
6. no conflict with another fixture;
7. `Sheet1!144:147` excluded;
8. no Archive or DeadArchive row 999 fixture.

Missing, stale, duplicate, occupied, out-of-bounds, unresolved, plugin-error, `#ERROR`, or conflicting evidence remains HOLD with zero writes.

## Separately controlled pre-test historical-row reconciliation

This step is not part of Codex work and is not authorized until after migration verification and a fresh controller read. The protected historical rows are:

| Range | Current supplied status | Protected history |
|---|---|---|
| `Sheet1!A69:Z69` | `D69=NEW` | controlled Send note records `SENT=YES` |
| `Sheet1!A72:Z72` | `D72=NEW` | historical trigger-to-queue proof |
| `Sheet1!A73:Z73` | `D73=NEW` | controlled Send note records `SENT=YES` |
| `Sheet1!A141:Z141` | `D141=NEW` | historical wrong-ID transaction fixture |

Required controller sequence for each row:

1. Keep Tasker stopped and freshly read the exact `A:Z` row.
2. Compare the full row with protected evidence and obtain explicit controller approval.
3. Change only column D from exact `NEW` to exact `REVIEW_HOLD`, using one bounded status write per row or one exact atomic D-only batch.
4. Re-read all four complete `A:Z` ranges and prove A:C and E:Z are unchanged.
5. Prove no unlisted row or column changed.

Never set these rows to `PROCESSING`, `READY_TO_SEND`, `DONE`, or blank. Never Archive or clear them automatically. Any mismatch, non-NEW status, unresolved output, plugin error, or changed protected field returns reconciliation HOLD with zero further writes.

## Migration order

1. STOP; verify profiles disabled and no lock/owner active.
2. Create a named backup and record revision, all tab sizes, headers, formulas, and protected-row hashes.
3. Freshly re-read the controller-supplied grid matrix, `SystemConfig!A1:J20`, `Sheet1!A69:CY73`, `Sheet1!A141:CY147`, and every existing formula anchor. Stop on any contradiction.
4. Require `SystemConfig!A3:D16` blank and preserve `A1:J2`; after separate approval write only A3:D16 as specified.
5. Add 67 blank rows to `Archive` and 28 blank rows to `DeadArchive`; add no columns or values and remove nothing.
6. Create only missing base tabs. Preserve existing header aliases when runtime authority is positional.
7. Preserve matching `QueueView!A1`; replace only `OverflowView!A1` and `OverflowSlotView!A2`; install formulas only in missing view tabs.
8. Create `ConversationGroups` with exact A:AP headers and a blank A2:AP1000 range.
9. Create `ConversationGroupSlotView` and `ConversationSchemaCheck`; install exact formulas.
10. Run the read-only verification order below. Do not select fixtures and do not perform historical-row reconciliation yet.

## Read-only verification order

1. Re-read workbook revision, tab inventory, physical row/column counts, and all headers; require every grid to be at least its minimum and no preexisting dimension to decrease.
2. Re-read every exact formula anchor.
3. Require `SchemaCheck!B2=PASS` and `ConversationSchemaCheck!B2=PASS`.
4. Require all slot views to return a numeric in-bounds row or `FULL`.
5. Require empty `IngressView` and `OverflowView` to expose blank output, never an error literal.
6. Require `RuntimeState!B2=0`, `ValidationControl!B2=NORMAL`, and `ValidationControl!B3=NONE`.
7. Re-read `SystemConfig!A1:J20`, `Sheet1!J:CY`, `QueueView!K:Z`, `OverflowInbox!O:CN`, `Archive!K:Z`, `DeadArchive!N:CI`, `Sheet1!144:147`, and the four historical A:Z rows; compare with backup evidence.
8. Prove only the approved SystemConfig block, added blank rows, created tabs, and approved formula anchors changed.
9. Verify no fixture authorization is armed, no fixture row was selected, and historical-row reconciliation has not run.

## Rollback order

1. Keep STOP asserted and profiles disabled.
2. Preserve/export any nonterminal `ConversationGroups` row as private evidence; never reset a bound or possible-click member to `NEW`.
3. Restore only created tabs, approved formula anchors, and `SystemConfig!A3:D16` from the named backup in reverse migration order; never overwrite preserved cells while rolling back.
4. Remove only the added rows from `Archive` and `DeadArchive` after proving every added row remained blank and after separate controller approval; retain all original columns.
5. Re-read all extension ranges, protected rows, historical rows, and production hashes; any mismatch is an incident HOLD.

Final migration status: `NON-DESTRUCTIVE PLAN ONLY / NOT APPLIED / HISTORICAL ROWS UNCHANGED / NO LIVE FIXTURE SELECTED / HOLD FOR CHATGPT AUDIT`
