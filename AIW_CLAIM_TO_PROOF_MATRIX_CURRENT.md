# AI Worker Claim To Proof Matrix Current

Status: ACTIVE CLAIM GATE
Updated: 2026-07-12T18:23:45-07:00

Every Codex claim must map to direct evidence. If proof is missing, the claim is HOLD or UNSUPPORTED.

## Claim Rules

- PASS is forbidden without evidence.
- PRESERVED is forbidden unless every required field is shown.
- UNCHANGED is forbidden unless source/output comparison proves it.
- PHONE-PROVEN is forbidden unless Sosa supplied phone evidence.
- Static XML parse cannot prove Tasker rendering or phone behavior.
- A generated CSV cannot prove its own correctness.

## AutoInput Preservation Evidence Requirement

For every AutoInput preservation claim, proof must show source value and output value for:

- Type
- Value
- Action
- Field Selection Type
- resource ID
- text target
- point
- nearby text
- timeout
- Continue Task After Error
- Structure Output
- accessibility setting
- plugin bundle values
- relevant variable outputs
- wait actions
- error checks
- failure routing

The proof must identify the exact XML action in both files and must be validated by a second independent parser/check.

## Current Claims

| Claim ID | Build | Claim | Evidence type required | Actual evidence provided | Exact file/path | Exact task/action/field | Static proof | Phone proof | Controller independently checked | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| CLAIM-27B-001 | 27B | Source is v15a | Source file SHA and source role | SHA recorded in reports | `02_TEST_LOGS/27B_20260710/AIW_CODEX_ACCOUNTABILITY_REPORT.md` | v15a source SHA | YES | NO | PARTIAL | PARTIAL |
| CLAIM-27B-002 | 27B | V15A AutoInput settings preserved | Field-by-field source/output proof plus independent parser/check plus phone-visible proof for plugin fields | Generated CSV said preserved except action sr | `02_TEST_LOGS/27B_20260710/V15A_AUTOINPUT_DIFF_TABLE.csv` | SEARCH_ICON and other AutoInput actions | PARTIAL | DISPROVEN FOR SEARCH_ICON | NO | DISPROVEN |
| CLAIM-27B-003 | 27B | No phone proof claimed by package | Package reports | Reports state no phone proof | `02_TEST_LOGS/27B_20260710/PHONE_PROOF_REQUIRED.md` | package status | YES | N/A | PARTIAL | PROVEN |
| CLAIM-27B-004 | 27B | Send not approved | Gate report and tracker | Reports and tracker keep Send blocked | `02_TEST_LOGS/27B_20260710/SEND_GATE_GUARD_REPORT.md`; `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md` | `%AIW27BAllowSend`, blocked paths | YES | Phone run stopped before send per user/controller report | PARTIAL | PROVEN FOR NO-SEND OUTCOME |
| CLAIM-ACC-001 | Accountability install | Accountability ledgers created | Direct file existence and commit diff | This PR should add files | root accountability files | project control docs | PENDING | N/A | PENDING | PARTIAL UNTIL PR AUDIT |
| CLAIM-ACC-002 | Accountability install | Tracker percentage unchanged | Direct tracker inspection | Tracker must retain `8/14 locked = 57%` | `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md` | proof percent | PENDING | N/A | PENDING | PARTIAL UNTIL PR AUDIT |
| CLAIM-ACC-003 | Accountability install | Runtime untouched | Git diff has no runtime XML behavior change | To be verified after commit | git changed-file list | changed paths | PENDING | N/A | PENDING | PARTIAL UNTIL PR AUDIT |
| CLAIM-29A-001 | 29A | Authoritative SEARCH_ICON source found | Phone-exported/Sosa-created source plus successful behavior plus no contradiction plus full field inspection | Source search found no candidate satisfying all four requirements | `02_TEST_LOGS/29A_27B_SEARCH_ICON_SOURCE_TRUTH_REPAIR/AUTHORITATIVE_SOURCE_DECISION.md` | SEARCH_ICON source decision | YES | Existing phone proof contradicts V15A menu_search source for current repair | PENDING | DISPROVEN |
| CLAIM-29A-002 | 29A | Runtime repair performed | Git diff and private package hashes | No repair package created because source proof was missing | `02_TEST_LOGS/29A_27B_SEARCH_ICON_SOURCE_TRUTH_REPAIR/ONE_ACTION_CHANGE_REPORT.md` | runtime repair status | YES | N/A | PENDING | NOT PERFORMED |
| CLAIM-29A-003 | 29A | Older text-based Search action is usable repair source | Exact source plus complete successful raw runlog plus phone-visible/source field proof | Partial historical evidence only; complete successful raw runlog tied to exact source not found | `02_TEST_LOGS/29A_27B_SEARCH_ICON_SOURCE_TRUTH_REPAIR/SOURCE_CANDIDATE_LEDGER.md` | old text-search SEARCH_ICON candidate | PARTIAL | PARTIAL ONLY | PENDING | UNSUPPORTED |

## Unsupported Claim Disclosure

The previous 27B `PRESERVED` claim is no longer accepted as proven. It is DISPROVEN for SEARCH_ICON until a future repair supplies direct AutoInput field evidence and phone-visible proof.

29A did not find a source that satisfies the repair rule. The older text-based `Search` action remains a candidate only. It is not approved as runtime build logic.

## Controller Checklist

Before approving any phone import/test, ChatGPT must record:

- exact source file inspected
- exact XML action inspected
- exact field values personally checked
- exact unsupported claims rejected or held
- exact phone proof needed
- exact blocked paths that remain blocked
