# README FIRST FOR CHATGPT - 31A DASHGOOD SEARCH LANE CONTROLLED SEND CANDIDATE

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT

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
- Current key count unchanged: TRUE
- ZIP integrity: PASS

## Blocked Paths

31A remains a controlled-send candidate for ChatGPT audit. Codex does not approve import, phone proof, Send, DONE, Archive, live, capacity, or release.
