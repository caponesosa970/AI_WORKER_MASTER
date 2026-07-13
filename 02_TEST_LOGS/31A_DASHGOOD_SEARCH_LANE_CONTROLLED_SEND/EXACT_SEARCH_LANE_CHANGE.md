# Exact Search Lane Change - 31A

## Decision

Build 31A by cloning the existing 27B task and replacing only the Search lane with the active Dashgood Task 71 search recovery lane proven by the 30B1 phone result.

## Task Scope

- Original task kept unchanged: `AIW27B_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE`
- New task added: `AIW31A_DASHGOOD_SEARCH_LANE_CONTROLLED_SEND_CANDIDATE`
- New task ID: `224`

## Replaced 27B Range

- Start boundary: immediately after existing V15A Chats action
- End boundary: immediately before existing keyboard action that writes `%sendsearch`
- Original replaced action count: `19`
- Inserted Dashgood action count: `49`

## Dashgood Source Range

Copied active Task 71 source actions by source action number:

`act180` through `act228`

This range includes:

- Search error reset/navigation/retry logic
- exact `Text = Search` action
- exact Navigate up and Chats reset actions
- disabled immediate Search-error fatal guard
- exact `search_field` actions
- exact search-field retry logic
- final search-field failure route through `SS Fail UI Dirty Stop`

Excluded:

- Dashgood Task 270 legacy task
- contact pick
- message box
- reply insertion
- Send button
- DONE write
- Archive/live/capacity behavior
- unrelated row-binding actions interleaved in Dashgood Task 71

## Semantic Result

- Original 27B task unchanged: TRUE
- Actions before the search lane unchanged in 31A: TRUE
- Downstream actions from keyboard write through the end unchanged in 31A: TRUE
- Existing keyboard write action preserved: TRUE
