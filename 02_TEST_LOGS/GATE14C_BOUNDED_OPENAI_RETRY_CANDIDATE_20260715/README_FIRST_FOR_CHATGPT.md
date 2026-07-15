# Gate 14C Bounded OpenAI Retry Candidate

Status: `GATE 14C BOUNDED OPENAI RETRY RUNTIME CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT`

Tracker: `13/14 locked = 93%`.

This candidate adds a maximum-two-attempt OpenAI controller, converts final API failures to exact-row `ERROR_OPENAI_REVIEW`, and migrates legacy `ERROR_OPENAI_RETRY` rows without another API call.

Runtime scope:

- changed existing Tasks 70, 171, 173, 192, and 233;
- Task 233 has one authorized regex extension only;
- added Tasks 235, 236, and 237;
- Task 69, Task 234, 81 other non-authorized existing tasks, four profiles, and one scene are preserved.

Private artifact SHA256:

- XML: `71A766AE8D550C139AABCEC53DE3B1025CAF26C68561583CBF20AC6D5A5138B3`
- ZIP: `4DCC4B1F3EEE5B4184F17BF0565EF501EF6013188097F811F62062130A74ACD9`
- sidecar: `5529570CC7C071CD53B7EE439CEADEA48D9384A1C0CAF3254B6E7D664BFFA8E6`

Codex did not run Tasker, read or change the live Sheet, call OpenAI, enable a profile, or claim phone proof. Phone import is not approved by Codex.
