# Call Graph Report

Task 239 incoming callers: zero.

Task 239 outgoing calls:

`Task 239 -> Task 238` exactly once.

Task 238 incoming callers:

`Task 239` only.

Task 238 outgoing call nodes:

- PROCESS Lock Start: 1
- PROCESS Mark Main Processing: 1
- PROCESS Build Prompt: 1
- PROCESS Call OpenAI HTTP: 1
- PROCESS Parse Reply: 1
- PROCESS Commit Success: 1
- PROCESS Commit Failure: 3 mutually exclusive failure branches
- PROCESS Lock Release: 1 common owned-lock release node

No Task 238/239 path calls Queue Cycle, TextNow, Send, confirmation, DONE, Archive, DeadArchive, Compactor, a profile, a timer, or a scene.
