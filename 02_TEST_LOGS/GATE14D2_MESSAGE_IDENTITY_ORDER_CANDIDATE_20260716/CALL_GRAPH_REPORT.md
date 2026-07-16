# Gate 14D2 Call Graph

`AIW GATE14D MESSAGE IDENTITY ORDER TEST`
-> `GATE14D Message Identity And Ordering Probe`

Ordering mode only:

`PROCESS Lock Start`
-> `PROCESS Mark Main Processing`
-> `PROCESS Build Prompt`
-> `PROCESS Call OpenAI HTTP`
-> `PROCESS Parse Reply`
-> `PROCESS Commit Success` or existing failure route
-> exact readback
-> `PROCESS Lock Release`

Duplicate mode only:

`TT5 Simple Sheet Duplicate Guard` twice.

The duplicate mode has zero processor, API, lock, or write calls. Neither new task is called by a profile, scene, timer, queue, trigger, startup task, or existing runtime task.
