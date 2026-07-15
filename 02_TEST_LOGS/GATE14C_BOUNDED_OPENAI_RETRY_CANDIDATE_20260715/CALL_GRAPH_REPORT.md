# Call Graph

Permanent changes:

- Task 171 -> Task 235 exactly once.
- Task 173 -> Task 233 exactly once, unchanged call contract.
- Task 70 -> Task 236 exactly once from the legacy OpenAI status branch.
- Task 235 -> no task.
- Task 236 -> no task.

Controlled launcher:

- Task 237 has zero incoming callers.
- Task 237 may call only Tasks 161, 166, 170, 171, 198, 172, 173, 162, and 236.
- Task 237 has no Queue Cycle, TextNow, Send, confirmation, Archive, timer, profile, or scene path.

Incoming callers:

- Task 235: Task 171 only.
- Task 236: Tasks 70 and 237 only.
- Task 237: none.
