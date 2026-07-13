# README FIRST FOR CHATGPT - 31A DASHGOOD SEARCH LANE CONTROLLED SEND CANDIDATE

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT

## 31A1 Current-Key Repair Update

ChatGPT rejected the original 31A private package because the search-lane runtime logic passed static audit, but the private XML carried the discontinued credential from an older 27B base.

31A1 repairs only that private credential literal. No Tasker action, task ID, task name, search lane action, AutoInput action, row guard, Send guard, Sheet logic, DONE logic, Archive logic, profile, or scene was changed.

Validation summary for 31A1:

- Original 31A XML SHA256: `D0F5F43DCE0BCD42ED75964ADDFFF078FCBEBC01637553153A280F478583CCD3`
- Credential source XML SHA256: `03CDD603FE4D3991BC3E88472BEA6C684F4CE10D0597A429EF5E247859D66925`
- Final 31A1 XML SHA256: `1C1FAF33EA30B69E8F35478AA8E93E58A2AA4ABB967CAA8F5EA927506BBF1B6E`
- Final 31A1 ZIP SHA256: `C05103D3EE95185E6FB47523C2793A27D9DAECFDA55931C569952B7DB5023921`
- Sanitized XML comparison after replacing all `sk-...` credentials with `[REDACTED_API_KEY]`: IDENTICAL
- Task 224 unchanged byte-for-byte: TRUE
- Runtime actions changed: NO
- Discontinued credential remaining count: `0`
- Current credential intended occurrence count: `1`
- Phone proof claimed for 31A1: NO
- Phone import approved by Codex: NO

## Preflight

- AGENTS.md read: YES
- .codex/config.toml read: YES
- Tracker read: YES
- Accountability ledgers read: YES
- Bug history searched: YES
- Current tracker: `8/14 locked = 57%`
- Controlled Send: HOLD
- Sheet changed: NO
- Phone proof claimed for 31A: NO
- Phone import approved by Codex: NO

## Scope

31A clones the existing private 27B full-project controlled-send candidate into a new task:

`AIW31A_DASHGOOD_SEARCH_LANE_CONTROLLED_SEND_CANDIDATE`

New task ID: `224`

Original 27B task remains unchanged.

Only the search lane in the cloned 31A task was changed. The replaced lane starts after the existing V15A Chats action and ends immediately before the existing keyboard action that writes `%sendsearch`.

## Source Truth

- Private 27B full-project XML SHA256: `1D354D6E3A672C96F07CA5A991D03764631AD335127313EC1CB1DC552339C31D`
- Dashgood active Task 71 source SHA256: `62804D52AE6BAB0E0E5895757D56123539F18F99A4E3E9E9060A8BC9C96A8DB7`
- Dashgood legacy Task 270: excluded
- 30B1 phone result: development pass for Dashgood combined Search plus both `search_field` actions

## Validation Summary

- XML parse: PASS
- Root: `TaskerData`
- Task count: `76`
- Profile count: `4`
- Scene count: `1`
- Original 27B task unchanged: TRUE
- 31A task present: YES
- Search lane copied exactly: TRUE
- Downstream actions unchanged: TRUE
- 31A original current-key claim: REJECTED / DISCONTINUED
- 31A1 current-key repair: credential-only repair, runtime actions unchanged
- ZIP integrity: PASS

## Blocked Paths

31A1 remains a controlled-send candidate for ChatGPT audit. Codex does not approve import, phone proof, Send, DONE, Archive, live, capacity, or release.
