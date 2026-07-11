# V15A Reuse / Blocked Actions Matrix - 20260709

FINAL STATUS: AUDIT ONLY / RETURN TO CHATGPT

| Source action/pattern | v15a action(s) | Current gate decision | Why |
|---|---:|---|---|
| Reset stale result flags | 0 | preserve exactly | `SS Reset Result Flags` prevents stale send-result state from contaminating run proof. |
| SENDING Sheet write | 67 | block | Current no-send gates must not mutate row status or mark `SENDING`. |
| Launch TextNow | 70 | isolate behind manual start state | Safe only after row/recipient/reply/no-send flags are locked and current gate approves TextNow open. |
| Wait after launch | 71 | preserve exactly | Phone-proven UI path needed settle time before AutoInput navigation. |
| Navigate up / Back fallback | 72 | preserve as optional fallback | Useful screen-state recovery; failure cannot prove success. |
| Wait after Navigate up | 73 | preserve exactly | Part of v15a transition contract. |
| Chats fallback | 74 | preserve as optional fallback | Useful reset to conversations; failure cannot prove success. |
| Wait after Chats | 75 | preserve exactly | Part of v15a transition contract. |
| Clear `%err/%errmsg` before required step | 76-77,85-86,96-97,105-106,120-121 | preserve exactly | Prevents old errors from being misread as current action results. |
| Set `%SSUIStep` before required step | 78,87,98,107,122 | preserve exactly | Failure helper uses this to identify the failed UI step. |
| Search icon click by ID | 79 | preserve exactly for search-only | Phone-exported AutoInput resource ID and timeout pattern; current gate may use it as required proof step. |
| Search field click by ID | 88 | preserve exactly for search-only | Phone-exported AutoInput resource ID and timeout pattern; current gate may use it as required proof step. |
| Keyboard clear/type search value | 94 | preserve pattern only | Safe for search field after field click success; no compose use. |
| List item 1 contact pick | 99 | block | Search-result row/list position is not identity proof. Result select/thread open remains blocked. |
| Compose field focus | 108 | block | Compose is dirty by default; no compose focus until thread identity and compose-empty proof pass. |
| Keyboard write reply | 116 | block | Paste/write reply is blocked until compose-empty proof and approved paste gate. |
| Send button click | 123 | block | `button_send` is real send path; Gate 10 remains blocked. |
| DONE Sheet write | 129 | block | DONE cannot be written before controlled send and independent sent proof. |
| Set `%SSSentOne=1` | 130 | block | Cannot mark sent without accepted phone proof. |
| Back/unwind after send | 136-142 | reference only | Useful for future cleanup only after send gate; not needed for no-send search proof. |
| Archive/live/capacity paths | none inside focused v15a send lane | block | Not part of Gate 9B1A and remains blocked by project rules. |
