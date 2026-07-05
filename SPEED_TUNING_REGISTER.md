# AI Worker Speed Tuning Register

Updated: 2026-07-05

## Status

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

Speed tuning is evidence collection first. Do not shorten waits or change UI timing until the behavior is stable and ChatGPT approves a tuning patch.

## Current Metrics To Preserve

| layer | metric | observed use |
|---|---|---|
| Stage4B formatted-number failure | task time, UI-start-to-stop time, contact-pick timeout | Shows formatted key reached search but did not resolve. |
| Stage4B digits-only pass | task time, UI-start-to-pass time, task-start-to-lock-release time | Shows contact-pick route can pass faster with cleaned digits. |

## Metrics To Add In Group B2

- selected search-key proof marker.
- search icon tap timestamp.
- search field ready timestamp.
- contact result picked timestamp.
- message box detected timestamp.
- paste attempted timestamp if paste is included.
- dry-run stop-before-send timestamp.
- fail-closed stop timestamp on miss.

## Tune Later, Not Now

- wait lengths
- repeated tap timing
- keyboard dismissal timing
- TextNow search result wait
- TeamViewer/navigation speed

## Rule

Speed can improve only after safety proof is clean. Safety beats speed.
