# SOURCE NODE LEDGER - 30B1 CONTROL-FLOW REPAIR

Status: CANDIDATE / HOLD FOR CHATGPT RE-AUDIT

## Original Rejected Candidate

| Artifact | SHA256 |
|---|---|
| original XML | `91EC3870FE7F463E478BB10CF1E812EE7DB8F3636D3B971BBCFE7DBFA537E275` |
| original ZIP | `7241D7FB0405C4B7E4805D05ADA53EF58E8537363C508836BFEED9CF5A217362` |

Original audit result: REJECTED.

Reasons:

1. If/End If control flow was unbalanced.
2. Dashgood exact-off AutoInput actions made the claimed post-error failure result unreachable.

## Repaired Candidate

| Artifact | SHA256 |
|---|---|
| repaired XML | `08D88FA8B5DFF7BA0F5D90F7C389B6FFAE20EA68FB4DC82E5EC70A4E6D08DD98` |
| repaired ZIP | `0F5BA14F00A0402A7364A1D747F7FBC956B2342EC4B99BB9839520B329A383BD` |

## Source A - Authoritative V15A

- File title: `basefile_v15a_phone_send_cleanup_pass.xml`
- SHA256: `C4CDEAA0BFD78120386FF1B03FA0A2D6B13BCEEDBD15687F84D03A3AD5FEF1C8`
- Source role: Authoritative Sosa-created V15A send-path AutoInput source
- Task: `FINAL Send Sheet`

## Source B - Dashgood Active Send Task

- File title: `dashgood-backup.xml`
- SHA256: `62804D52AE6BAB0E0E5895757D56123539F18F99A4E3E9E9060A8BC9C96A8DB7`
- Source role: Private historical active Tasker backup
- Active task: ID `71`, name `FINAL Send Sheet`
- Legacy excluded: ID `270`, name `FINAL Send Sheet LEGACY UI FROZEN V19M`

## Exact Source-to-Output Copy Map

| Node | Source | Source sr | Source list index | Output action index | AutoInput | Continue After Error | XML equal except sr | Semantic equal |
|---|---|---:|---:|---:|---|---|---|---|
| V15A_LAUNCH | v15a | act70 | 111 | 6 | NO | false | YES | YES |
| V15A_WAIT_BEFORE_NAV | v15a | act71 | 112 | 7 | NO | false | YES | YES |
| V15A_NAVIGATE_UP | v15a | act72 | 113 | 10 | YES | false | YES | YES |
| V15A_WAIT_AFTER_NAV | v15a | act73 | 114 | 12 | NO | false | YES | YES |
| V15A_CHATS | v15a | act74 | 115 | 15 | YES | false | YES | YES |
| V15A_WAIT_AFTER_CHATS | v15a | act75 | 116 | 17 | NO | false | YES | YES |
| V15A_ID_SEARCH | v15a | act79 | 120 | 22 | YES | false | YES | YES |
| V15A_WAIT_AFTER_ID_SEARCH | v15a | act84 | 126 | 27 | NO | false | YES | YES |
| V15A_SEARCH_FIELD | v15a | act88 | 130 | 32 | YES | false | YES | YES |
| DASHGOOD_WAIT_BEFORE_NAV | dashgood | act189 | 100 | 43 | NO | false | YES | YES |
| DASHGOOD_NAVIGATE_UP | dashgood | act190 | 102 | 46 | YES | false | YES | YES |
| DASHGOOD_WAIT_AFTER_NAV | dashgood | act191 | 103 | 48 | NO | false | YES | YES |
| DASHGOOD_CHATS | dashgood | act192 | 104 | 51 | YES | false | YES | YES |
| DASHGOOD_WAIT_AFTER_CHATS | dashgood | act193 | 105 | 53 | NO | false | YES | YES |
| DASHGOOD_TEXT_SEARCH | dashgood | act197 | 109 | 56 | YES | false | YES | YES |
| DASHGOOD_WAIT_AFTER_TEXT_SEARCH | dashgood | act198 | 110 | 58 | NO | false | YES | YES |
| DASHGOOD_SEARCH_FIELD_1 | dashgood | act208 | 122 | 61 | YES | false | YES | YES |
| DASHGOOD_SEARCH_FIELD_2 | dashgood | act209 | 123 | 65 | YES | false | YES | YES |

Result: all selected source nodes are copied exactly except required output `sr` renumbering.
