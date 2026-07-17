# AIW Final Integrated Sheet Migration Manifest - Conversation Continuity P1 R1

Status: `PLAN ONLY / NOT APPLIED / HOLD FOR CONTROLLER APPROVAL`

This is the complete migration authority for the Option A Phase 1 R1 candidate. It has no dependency on an older manifest. Codex did not open or mutate the live workbook and selected no fixture row.

## Safety boundary

- Make a named full-workbook backup and record its revision before any change.
- Keep the worker stopped, all Tasker profiles disabled, and all validation fixture authorization closed during migration.
- Do not rename, clear, reorder, or overwrite existing `Sheet1`, `Archive`, `DeadArchive`, or `OverflowInbox` data.
- Preserve `Sheet1` rows `144:147` exactly. They are occupied/protected and are never fixtures.
- `Archive` row 999 and `DeadArchive` row 999 are not fixtures. The row expansions below exist only because preserved bounded production reads use row 1000.
- Do not select or guess validation fixture rows. They remain dynamic controller inputs after fresh read-only bounds and blankness proof.
- Views are hints. Exact direct-row reads, identity checks, and readbacks remain write authority.
- `DeadArchive`, Compactor, broad Archive drain, and legacy maintenance remain unreachable.

## Exact target inventory

The controller must reconcile every existing tab against this table before applying any formula. Row expansion never authorizes data writes.

| Tab | Purpose | Target physical rows x columns | Runtime maximum | Privacy |
|---|---|---:|---:|---|
| `SystemConfig` | Version and bounded maxima | 100 x 4 | rows 2:100 | internal configuration |
| `Sheet1` | Existing production queue | 980 x 26 | payload rows 2:201; protected range A:Z | private production data |
| `QueueView` | Existing phone-proven lifecycle hint | 201 x 10 | rows 2:201 | private derived data |
| `Sheet1SlotView` | Blank-main-row hint | 2 x 1 | row 2 | internal derived data |
| `OverflowInbox` | Durable overflow admission | 986 x 14 | rows 2:986 | private production data |
| `OverflowSlotView` | Blank-overflow-row hint | 2 x 1 | row 2 | internal derived data |
| `OverflowView` | Ordered active overflow hint | 986 x 15 | rows 2:986 | private derived data |
| `Archive` | Confirmed production history | 1000 x 10 | rows 2:1000 | private production history |
| `DeadArchive` | Preserved legacy identity history | 1000 x 13 | candidate reads A2:A1000 only | private production history |
| `IngressJournal` | Durable notification admission journal | 1001 x 14 | rows 2:1001 | private production data |
| `IngressSlotView` | Blank-journal-row hint | 2 x 1 | row 2 | internal derived data |
| `IngressView` | Ordered unresolved ingress hint | 1001 x 15 | rows 2:1001 | private derived data |
| `IdentityProbe` | Serialized exact-identity input | 2 x 5 | row 2 | private transient data |
| `IdentityProbeResult` | Exact identity classification | 2 x 3 | row 2 | private derived data |
| `ProofLedger` | Append-only validation proof | 5001 x 12 | rows 2:5001 | private proof data |
| `ProofLedgerSlotView` | Blank-proof-row hint | 2 x 1 | row 2 | internal derived data |
| `RuntimeState` | Durable START/STOP desired state | 2 x 4 | row 2 | private runtime state |
| `ValidationControl` | Dynamic validation gate | 3 x 2 | rows 2:3 | private validation state |
| `RecoveryProbe` | Durable ambiguity summary | 2 x 6 | row 2 | private derived data |
| `SchemaCheck` | Integrated base schema gate | 2 x 6 | row 2 | internal derived data |
| `ConversationGroups` | Durable conversation group ledger | 1000 x 42 | rows 2:1000 | highly private conversation data |
| `ConversationGroupSlotView` | Blank-group-row hint | 2 x 1 | row 2 | internal derived data |
| `ConversationSchemaCheck` | Conversation schema and bounds gate | 2 x 7 | row 2 | internal derived data |

## Exact schemas and seed values

### SystemConfig

Headers `A1:D1`:

`Key | Value | Description | UpdatedAt`

Exact rows:

| Row | Key | Value | Description |
|---:|---|---|---|
| 2 | `SchemaVersion` | `AIW_FINAL_V1` | integrated base schema |
| 3 | `MainMaxRow` | `201` | production Sheet1 payload maximum |
| 4 | `OverflowMaxRow` | `986` | OverflowInbox physical/runtime maximum |
| 5 | `JournalMaxRow` | `1001` | IngressJournal physical/runtime maximum |
| 6 | `ReleaseMode` | `FINAL_INTEGRATED` | final integrated candidate mode |
| 7 | `DeadArchiveEnabled` | `0` | unreachable in V1 |
| 8 | `CompactorEnabled` | `0` | unreachable in V1 |
| 9 | `ConversationSchemaVersion` | `AIW_CONVERSATION_V1` | group schema version |
| 10 | `ConversationGroupMaxRow` | `1000` | bounded ConversationGroups maximum |
| 11 | `ConversationMemberCapacity` | `4` | maximum members per group |
| 12 | `ConversationQuietSeconds` | `10` | persisted quiet window |
| 13 | `Sheet1PhysicalMaxRow` | `980` | verified physical row count |
| 14 | `ArchivePhysicalMaxRow` | `1000` | required target after audited row expansion |
| 15 | `DeadArchivePhysicalMaxRow` | `1000` | required target after audited row expansion |

### Sheet1

Preserve the existing tab. Required payload headers `A1:I1`:

`ID | Sender | Message | Status | Reply | Touch | Button | Time | Ticker`

Columns `J:Z` are protected extension columns. Preserve their existing headers and values byte-for-byte; the R1 candidate does not redefine them. No runtime payload row above 201 is authorized.

### OverflowInbox

Headers `A1:N1`:

`OverflowID | OriginalID | Sender | Message | Status | Reply | TouchAction | ButtonAction | EventTime | Ticker | LoggedAt | Source | Attempts | LastError`

### Archive

Headers `A1:J1`:

`ID | Sender | Message | Status | Reply | Touch | Button | Time | Ticker | ArchivedAt`

Expand the existing grid from its controller-observed 933 rows to exactly 1000 rows without changing any existing cell. No row is seeded.

### DeadArchive

The candidate contract uses `A1` = `ID` and reads only `A2:A1000`. Preserve the existing `B:M` headers and all values exactly. Expand rows from the controller-observed 972 to exactly 1000 without changing any existing cell. Do not create a row-999 fixture.

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

Every formula is entered exactly once in the listed anchor. The target tab must otherwise be blank before the array formula is installed.

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

## Migration order

1. STOP; verify profiles disabled and no lock/owner active.
2. Create a named backup and record revision, all tab sizes, headers, formulas, and protected-row hashes.
3. Verify `Sheet1!144:147` read-only and record its unchanged proof.
4. Expand `Archive` to 1000 rows and `DeadArchive` to 1000 rows; add no values.
5. Create/normalize `SystemConfig`, `IngressJournal`, `ProofLedger`, `RuntimeState`, `ValidationControl`, and `IdentityProbe` in the order listed above.
6. Create the base view tabs and install their exact formulas.
7. Create `ConversationGroups` with exact A:AP headers and a blank A2:AP1000 range.
8. Create `ConversationGroupSlotView` and `ConversationSchemaCheck`; install exact formulas.
9. Run the read-only verification order below. Do not select fixtures.

## Read-only verification order

1. Re-read workbook revision, tab inventory, physical row/column counts, and all headers.
2. Re-read every exact formula anchor.
3. Require `SchemaCheck!B2=PASS` and `ConversationSchemaCheck!B2=PASS`.
4. Require all slot views to return a numeric in-bounds row or `FULL`.
5. Require empty `IngressView` and `OverflowView` to expose blank output, never an error literal.
6. Require `RuntimeState!B2=0`, `ValidationControl!B2=NORMAL`, and `ValidationControl!B3=NONE`.
7. Re-read `Sheet1!144:147` and all preexisting production ranges; compare against backup evidence.
8. Verify no fixture authorization is armed and no fixture row was selected.

## Rollback order

1. Keep STOP asserted and profiles disabled.
2. Preserve/export any nonterminal `ConversationGroups` row as private evidence; never reset a bound or possible-click member to `NEW`.
3. Restore formulas and created tabs from the named backup in reverse migration order.
4. Remove only the added blank rows from `Archive` and `DeadArchive` after proving they stayed blank and after controller approval.
5. Re-read all protected rows and production hashes; any mismatch is an incident HOLD.

Final migration status: `PLAN ONLY / NOT APPLIED / NO LIVE FIXTURE SELECTED / HOLD FOR CHATGPT AUDIT`
