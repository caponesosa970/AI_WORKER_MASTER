# SOURCE NODE LEDGER - 30B

## Source A - Authoritative V15A

- File title: `basefile_v15a_phone_send_cleanup_pass.xml`
- SHA256: `C4CDEAA0BFD78120386FF1B03FA0A2D6B13BCEEDBD15687F84D03A3AD5FEF1C8`
- Source role: Authoritative Sosa-created V15A send-path AutoInput source
- Task: `FINAL Send Sheet`
- Use: exact source nodes for launch, navigation fallback, ID `menu_search`, ID `search_field`, and surrounding waits

## Source B - Dashgood Active Send Task

- File title: `dashgood-backup.xml`
- SHA256: `62804D52AE6BAB0E0E5895757D56123539F18F99A4E3E9E9060A8BC9C96A8DB7`
- Source role: Private historical Tasker backup, active send-path reference
- Active task: ID `71`, name `FINAL Send Sheet`
- Legacy excluded: ID `270`, name `FINAL Send Sheet LEGACY UI FROZEN V19M`
- Use: exact source nodes for active reset/navigation sequence, text `Search`, ID `search_field`, retry field sequence, and waits

## Exact Source-to-Output Copy Map

| Source | Source sr | Source list index | Output action index | Purpose | XML equal except sr | Semantic equal |
|---|---:|---:|---:|---|---|---|
| v15 | act70 | 111 | 6 | Launch TextNow | YES | YES |
| v15 | act71 | 112 | 7 | wait before nav | YES | YES |
| v15 | act72 | 113 | 8 | Navigate up | YES | YES |
| v15 | act73 | 114 | 9 | wait after nav | YES | YES |
| v15 | act74 | 115 | 10 | Chats | YES | YES |
| v15 | act75 | 116 | 11 | wait after chats | YES | YES |
| v15 | act79 | 120 | 15 | V15A menu_search | YES | YES |
| v15 | act84 | 126 | 19 | wait after menu_search | YES | YES |
| v15 | act88 | 130 | 20 | V15A search_field | YES | YES |
| dash | act189 | 100 | 29 | dash reset wait | YES | YES |
| dash | act190 | 102 | 30 | dash reset navigate | YES | YES |
| dash | act191 | 103 | 31 | dash reset nav wait | YES | YES |
| dash | act192 | 104 | 32 | dash reset chats | YES | YES |
| dash | act193 | 105 | 33 | dash reset chats wait | YES | YES |
| dash | act197 | 109 | 37 | dash Text Search | YES | YES |
| dash | act198 | 110 | 41 | dash search wait | YES | YES |
| dash | act208 | 122 | 42 | dash field1 | YES | YES |
| dash | act209 | 123 | 43 | dash field2 | YES | YES |
| dash | act214 | 129 | 51 | dash retry wait | YES | YES |
| dash | act215 | 130 | 54 | dash retry Text Search | YES | YES |
| dash | act216 | 131 | 58 | dash retry search wait | YES | YES |
| dash | act220 | 136 | 61 | dash retry field1 | YES | YES |
| dash | act221 | 137 | 62 | dash retry field2 | YES | YES |
| dash | act222 | 138 | 63 | dash retry field wait | YES | YES |

Result: all selected source nodes are copied exactly except required output `sr` renumbering, and all selected nodes are semantically equal by an independent comparison.
