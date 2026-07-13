# 30A V15A Source-Truth Correction

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT

Issue:

`ISSUE_27B_AUTOINPUT_TARGET_NOT_V15A_PRESERVED`

Sosa source-truth correction:

Sosa directly confirmed that every AutoInput action inside `basefile_v15a_phone_send_cleanup_pass.xml` was manually created by him. The V15A send-path AutoInput action set is therefore authoritative.

Authoritative source:

- File: `basefile_v15a_phone_send_cleanup_pass.xml`
- SHA256: `C4CDEAA0BFD78120386FF1B03FA0A2D6B13BCEEDBD15687F84D03A3AD5FEF1C8`

Decision:

No SEARCH_ICON XML/plugin-bundle drift was found between authoritative V15A and current private 27B. No runtime repair was created.

Important distinction:

The phone failure remains real, but it is not proven to be source-preservation drift. The current evidence points to phone/runtime/UI behavior with the authoritative V15A SEARCH_ICON preserved in 27B.

Runtime changed:

NO.

Private XML created:

NO.

Private ZIP created:

NO.

Phone proof claimed:

NO.

Phone import approved:

NO.

Tracker:

No percentage change. Current tracker remains `8/14 locked = 57%`.

Next diagnostic gate:

30B should be a phone/runtime diagnostic only after ChatGPT approval. It should not patch XML. It should verify the phone-visible SEARCH_ICON action state and TextNow UI state, then capture runlog and screen proof around SEARCH_ICON.
