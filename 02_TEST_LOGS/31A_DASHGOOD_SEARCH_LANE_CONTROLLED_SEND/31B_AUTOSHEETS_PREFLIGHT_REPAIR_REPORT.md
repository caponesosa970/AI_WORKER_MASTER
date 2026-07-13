# 31B AutoSheets Preflight Retry Repair Report

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT

## Source

- Source package: 31A1 current-key full-project private XML
- Source XML SHA256: `1C1FAF33EA30B69E8F35478AA8E93E58A2AA4ABB967CAA8F5EA927506BBF1B6E`
- Source task ID: `224`
- Source task name: `AIW31A_DASHGOOD_SEARCH_LANE_CONTROLLED_SEND_CANDIDATE`

## Observed Phone Failure Recorded

The controlled run stopped at the AutoSheets row-read preflight with a socket timeout after the Send lock was active and before TextNow launched.

31B repairs only the AutoSheets preflight error handling in task `224`.

## Exact Runtime Scope

Task `224` was renamed to:

`AIW31B_AUTOSHEETS_RETRY_CONTROLLED_SEND_CANDIDATE`

Only task `224` changed. No other task changed.

31B does not change:

- current private credential
- Dashgood Search lane
- AutoInput actions
- row contract after successful read
- contact selection
- compose
- Send
- DONE
- Archive
- profiles
- scenes

## AutoSheets Repair

The existing AutoSheets Get Data configuration was preserved:

- sheet target: unchanged
- sheet tab: unchanged
- range: unchanged
- output names: unchanged
- formatted output: unchanged
- timeout: unchanged at 60 seconds

The Get Data action now has Continue Task After Error enabled so the task can capture timeout failure and release the Send lock safely.

Maximum AutoSheets row-read attempts: `2`

## Corrected 31B Validation Rules

Before the first read attempt, 31B clears:

- `%aiw27b_id`
- `%aiw27b_sender`
- `%aiw27b_message`
- `%aiw27b_status`
- `%aiw27b_reply`
- `%err`
- `%errmsg`

Before the retry, 31B clears the same outputs again.

A read is treated as successful only when all first elements are set and every output array count equals exactly `1`:

- `%aiw27b_id1`
- `%aiw27b_sender1`
- `%aiw27b_message1`
- `%aiw27b_status1`
- `%aiw27b_reply1`
- `%aiw27b_id(#) = 1`
- `%aiw27b_sender(#) = 1`
- `%aiw27b_message(#) = 1`
- `%aiw27b_status(#) = 1`
- `%aiw27b_reply(#) = 1`

If `%err` is set, if any first element is unset, or if any count is not `1`, the read is treated as failed.

Retry wait: `3` seconds.

## Final Failure Path

After both read attempts fail, 31B:

- sets `%AIW27BAllowSend = 0`
- sets `%AIW27BStatus = HOLD_AUTOSHEETS_ROW_READ_FAILED`
- sets `%SSFailed = 1`
- sets `%SSResult = AUTOSHEETS_ROW_READ_FAILED`
- records `%err` and `%errmsg` into safe failure variables
- performs `SS Lock Release HARD`
- stops before TextNow launch

## Validation Summary

- XML parse: PASS
- Root: `TaskerData`
- Task count: `76`
- Profile count: `4`
- Scene count: `1`
- Duplicate task IDs: `0`
- Duplicate task names: `0`
- Missing Perform Task refs: `0`
- Source task actions before repair: `238`
- Output task actions after wrapper insertion: `336`
- Output clearing before both reads: PASS
- First-element checks present for all five outputs: PASS
- Array-count checks present for all five outputs: PASS
- AutoSheets read attempts for the staged row range: `2`
- AutoSheets Continue Task After Error enabled: PASS
- AutoSheets configuration preserved except required Continue Task After Error change: PASS
- If/End If count in task 224: `45 / 45`
- Final If stack depth: `0`
- Search lane unchanged semantically: PASS
- Downstream actions unchanged semantically excluding Tasker action sr/location renumbering: PASS
- Current key unchanged without printing it: PASS
- ZIP integrity: PASS
- Private files tracked by Git: NO

## Private Package Hashes

- 31B full private XML SHA256: `0B984F8CADCBCCA4915676F76C269F927ADED0473C34043F15609F1720C60007`
- 31B private ZIP SHA256: `4C529BF48A8DD71B64B0B6B2B62801A0C5C536BD1CA8B6B5DB478723B8150EA3`

## Proof Boundary

31B is a private runtime candidate for ChatGPT audit.

- Phone proof claimed: NO
- Phone import approved by Codex: NO
- Sheet changed: NO
- Tracker percentage changed: NO
- Controlled Send remains HOLD
