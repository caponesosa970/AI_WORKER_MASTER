# Gate 12 Phone-Proof Inputs Reviewed

Direct Sosa phone proof is the authority. Codex records it and does not independently claim it.

- Gate 12R1 full-project base SHA: `3DC49BF47837403B36D1B213564F34BD6983598B6734429324FF0ACEDA7A23C8`
- Gate 12 cycle 1: Send: `D087C31E4B4B77796E71622EA03030BFB1625E3EEA6CD116338684E49F9F8A5F`
- Gate 12 cycle 2: confirmation: `0CB4243A994143B15343196EA7FF7617B20DD080242A620547BA49EDB4FCEEB3`
- Gate 12 cycle 3: Archive: `E7375BADA436182981F3D15ABD47D69A31A7605CCD4FCB4EB377562FC1911CB3`

The three runlogs show separate routing through Send, confirmation, and Archive. They were used as proof inputs for the Gate 13 source boundary; they are not committed because they contain private runtime detail.

The locked QueueView A1 formula is:

```text
={"SourceRow","ID","Sender","Message","Status","Reply","Touch","Button","Time","Ticker";IFNA(FILTER({ROW(Sheet1!A2:A),Sheet1!A2:I},REGEXMATCH(Sheet1!D2:D,"^(NEW|PROCESSING|READY_TO_SEND|SENDING|SEND_CLICKED_AWAITING_CONFIRM|SEND_OUTCOME_UNKNOWN_REVIEW|POST_SEND_STATUS_UPDATE_FAILED|HOLD_PRE_SEND_FAILED|DONE|REVIEW_READY|REVIEW_HOLD|REVIEW_REJECTED|EDIT_REPLY|SKIP_MANUAL)$")),{"","","","","","","","","",""})}
```

Codex read the formula without writing to the Sheet.
