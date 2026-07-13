# README FIRST FOR CHATGPT - 31A DASHGOOD SEARCH LANE CONTROLLED SEND CANDIDATE

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT

## 31B Superseding Transaction-Safety Repair Update

The earlier 31B AutoSheets-only repair is superseded by the current transaction-safety 31B package.

31B records the phone failure where task `224` stopped at the AutoSheets row-read preflight with a socket timeout after the Send lock was active and before TextNow launched.

31B changes only task `224`. The task is named:

`AIW31B_AUTOSHEETS_RETRY_CONTROLLED_SEND_CANDIDATE`

Current 31B includes all known controlled one-send transaction-safety requirements:

- clears the five AutoSheets output arrays plus `%err` and `%errmsg` before both preflight reads
- retries the preflight row read once after 3 seconds
- validates all five first elements and all five output array counts
- consumes `%AIW27BAllowSend` into `%AIW31BRunAllowSendLatch`
- sets global `%AIW27BAllowSend=0` before TextNow interaction
- uses the local latch for later send checks
- writes `SENDING` before TextNow, retries once if needed, and reads back `SENDING`
- blocks TextNow if `SENDING` is not confirmed
- keeps Search, contact select, compose, reply insertion, and Send-button AutoInput unchanged
- after Send click, writes `SEND_CLICKED_AWAITING_CONFIRM`, retrying once if needed
- does not write `DONE`
- does not set `%SSSentOne=1`
- does not set `%SSResult=SENT`
- always closes authorization and releases the Send lock on exit

Validation summary for 31B:

- Source 31A1 XML SHA256: `1C1FAF33EA30B69E8F35478AA8E93E58A2AA4ABB967CAA8F5EA927506BBF1B6E`
- Superseded narrow 31B XML SHA256: `0B984F8CADCBCCA4915676F76C269F927ADED0473C34043F15609F1720C60007`
- Superseded narrow 31B ZIP SHA256: `4C529BF48A8DD71B64B0B6B2B62801A0C5C536BD1CA8B6B5DB478723B8150EA3`
- Final superseding 31B XML SHA256: `156D44624EF534DB8F0D4E81F0E873A44FE8A9560B26D1C260348AFA4ED8B820`
- Final superseding 31B ZIP SHA256: `B6C8126034AE775157105A0343F627464AF1F1626B44584CA9140DA3B0D3B67D`
- XML parse: PASS
- Task count/profile count/scene count: `76 / 4 / 1`
- Duplicate task IDs/names: `0 / 0`
- Missing Perform Task refs: `0`
- Only task 224 changed: YES
- AutoSheets attempts maximum: `2`
- Retry wait: `3` seconds
- Final AutoSheets failure releases lock: YES
- Final AutoSheets failure closes AllowSend: YES
- SENDING write/readback before TextNow: YES
- Send authorization consumed before TextNow: YES
- Post-Send status is awaiting confirmation, not DONE: YES
- AutoInput nodes unchanged semantically: YES
- Current key unchanged without printing it: YES
- Phone proof claimed for 31B: NO
- Phone import approved by Codex: NO

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
