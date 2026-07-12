# V15A AutoInput Preservation Rule

Updated: 2026-07-10

Status: ACTIVE RULE / HOLD FOR CHATGPT AUDIT

## Source

Source XML:

- `basefile_v15a_phone_send_cleanup_pass.xml`
- Private source reference: Private Drive source - link and ID retained outside the public repository.
- SHA256: `C4CDEAA0BFD78120386FF1B03FA0A2D6B13BCEEDBD15687F84D03A3AD5FEF1C8`

## Rule

V15A TextNow AutoInput actions are high-trust phone-proven action-shape references.

Codex must not invent AutoInput targets.

Codex must not replace v15a:

- resource IDs
- list item selector
- `edit_text_out`
- `button_send`
- `menu_search`
- `search_field`
- action type
- field selection type
- timeout
- Continue After Error setting
- Structure Output setting
- waits around UI actions
- `%SSUIStep` markers
- `%err` / `%errmsg` handling
- failure-routing pattern

## Safe Use

Copy v15a AutoInput action shapes only when the current ChatGPT scope explicitly allows that lane.

Preserve the contract, not just the target text.

## Blocked Until Explicit Approval

- result select
- thread open
- compose focus
- paste/write reply
- `button_send`
- DONE write
- Archive
- live/timer
- capacity
- release

## 27B Application

27B may preserve the v15a controlled-send path only behind:

- `%AIW27BAllowSend=1`
- row 75 status `READY_TO_SEND`
- ChatGPT audit
- explicit Sosa phone-proof operation

Default state remains no-send.
