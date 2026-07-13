# 29A Source Candidate Ledger

Status: PUBLIC-SAFE SUMMARY

No private XML content, private Drive IDs, local user paths, API keys, or phone numbers are included here.

## Source-Truth Rule

A repair is authorized only if Codex finds an exact SEARCH_ICON source that is:

1. phone-exported or directly created by Sosa
2. supported by successful historical phone behavior
3. not contradicted by newer phone proof
4. fully inspectable field-by-field

If any item is missing, patching must stop.

## Drive Search Performed

Searches performed:

- `basefile_v15a_phone_send_cleanup_pass`
- `basefile_v15a`
- `SEARCH_ICON`
- `DRYRUN_CONTACT_PICK_PASS`

Drive findings:

| Drive result title | Role | Result |
|---|---|---|
| `V15A_WORKING_TEXTNOW_ACTION_CONTRACT_AUDIT_20260709.md` | V15A audit report | Found |
| `runlog (3).txt` | SEARCH_ICON failed runlog | Found |
| `runlog (4).txt` | SEARCH_ICON passed, later contact-pick failed runlog | Found |
| `Sheet1` | live Sheet, read-only reference only | Found |
| `00_CODEX_EXECUTE_THIS_BUILD100_GROUPED_COMPLETION_PLAN_PRO.md` | plan/reference document | Found |
| `AIW_BUILD100_DEEP_AUDIT_REPORT.md` | old audit/reference document | Found |

Drive did not return a raw complete successful runlog proving the exact SEARCH_ICON source and full successful no-send navigation chain.

## Candidate Sources

| Candidate ID | Source role | SHA256 | Phone-exported/source status | Historical run proof | Contradiction | Decision |
|---|---|---|---|---|---|---|
| SRC-V15A-FINAL-SEND | V15A `FINAL Send Sheet` source | `C4CDEAA0BFD78120386FF1B03FA0A2D6B13BCEEDBD15687F84D03A3AD5FEF1C8` | phone-exported stable reference | V15A report claims working send path | New 27B phone proof contradicts this SEARCH_ICON shape for current repair | NOT AUTHORITATIVE |
| SRC-27B-PRIVATE | Current private 27B runtime source | `1D354D6E3A672C96F07CA5A991D03764631AD335127313EC1CB1DC552339C31D` | current candidate/private source | Failed current phone proof | Disputed SEARCH_ICON action failed | NOT AUTHORITATIVE |
| SRC-OLD-TEXT-SEARCH | Older text-based Search action source | `8A99DD4995B310AFABEC414A321240CD98EE4D5225B9F2144B115811ED0B7CF1` | private historical source/reference | One local/Drive run shows SEARCH_ICON OK; flow failed later at contact pick | Complete successful run tied to this exact source not found | INSUFFICIENT |
| SRC-STAGE4B-REPORTS | Stage4B proof ledgers and summaries | multiple docs | documentation/reference | Summary claims a later pass | Local metrics state raw pass runlogs were not found during sync | INSUFFICIENT |

## Direct Source Finding

The V15A `FINAL Send Sheet` SEARCH_ICON source extracted from XML is:

- Type: Id
- Value: TextNow `menu_search` resource
- Action: Click
- Field Selection Type: Id/resource mode
- Timeout: 12
- Continue After Error: enabled

The newer 27B phone proof says this exact family of action was not Sosa's expected AutoInput setup and failed at SEARCH_ICON. Therefore this candidate cannot be used as the authoritative repair source.

## Older Text-Based Candidate

An older `SS Safe Send Dry-Run` source contains:

- Type: Text
- Value: Search
- Action: Click
- Field Selection Type: text mode
- Timeout: 12
- Continue After Error: disabled

This is closer to the action Sosa appears to expect, but it does not satisfy all four source-truth requirements. The available runlog evidence proves only partial behavior: SEARCH_ICON can succeed in one run, but the flow failed later. A complete successful phone behavior chain tied to the exact source was not found.
