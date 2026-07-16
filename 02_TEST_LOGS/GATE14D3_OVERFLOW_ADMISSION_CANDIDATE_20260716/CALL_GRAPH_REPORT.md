# Call Graph

Launcher incoming callers: none.

Launcher calls:

- `GATE14D3 Overflow Admission Probe` exactly once.

Probe admission mode calls:

- `PROCESS Controlled Capacity Batch` exactly once.

Probe deferred-drain mode calls only the existing bounded processor lane:

- `PROCESS Lock Start`
- `PROCESS Mark Main Processing`
- `PROCESS Build Prompt`
- `PROCESS Call OpenAI HTTP`
- `PROCESS Parse Reply`
- `PROCESS Commit Success` or `PROCESS Commit Failure`
- `PROCESS Lock Release`

No new TextNow, Send, confirmation, DONE, Archive, profile, timer, live, Queue Cycle, or recursive call exists.
