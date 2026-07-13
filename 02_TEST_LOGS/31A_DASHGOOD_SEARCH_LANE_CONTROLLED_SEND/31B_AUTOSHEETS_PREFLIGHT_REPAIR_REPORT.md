# 31B Superseding Transaction-Safety Repair Report

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT

## Superseding Correction

The earlier narrow 31B AutoSheets-only candidate is superseded. The current 31B package includes all known controlled one-send transaction-safety requirements:

1. bounded AutoSheets preflight read retry
2. Send authorization consumption into a local run latch
3. persistent pre-send `SENDING` state with retry and readback verification
4. no `DONE` write from the Send click
5. post-Send `SEND_CLICKED_AWAITING_CONFIRM` status with retry
6. global authorization closed before TextNow and on every exit

Superseded 31B private hashes:

- Superseded 31B XML SHA256: `0B984F8CADCBCCA4915676F76C269F927ADED0473C34043F15609F1720C60007`
- Superseded 31B ZIP SHA256: `4C529BF48A8DD71B64B0B6B2B62801A0C5C536BD1CA8B6B5DB478723B8150EA3`

## Source

- Source package: 31A1 current-key full-project private XML
- Source XML SHA256: `1C1FAF33EA30B69E8F35478AA8E93E58A2AA4ABB967CAA8F5EA927506BBF1B6E`
- Source task ID: `224`
- Source task name: `AIW31A_DASHGOOD_SEARCH_LANE_CONTROLLED_SEND_CANDIDATE`

## Observed Phone Failure Recorded

The controlled run stopped at the AutoSheets row-read preflight with a socket timeout after the Send lock was active and before TextNow launched.

31B repairs only the AutoSheets preflight error handling in task `224`.

The superseding 31B package expands that task-224-only repair to include controlled one-send transaction safety. It still does not alter Search, contact selection, compose, Send-button AutoInput, credential, profiles, scenes, or any other task.

## Exact Runtime Scope

Task `224` was renamed to:

`AIW31B_AUTOSHEETS_RETRY_CONTROLLED_SEND_CANDIDATE`

Only task `224` changed. No other task changed.

31B does not change:

- current private credential
- Dashgood Search lane
- AutoInput actions
- contact selection
- compose action
- exact reply insertion
- Send-button AutoInput
- row contract after successful read
- profiles
- scenes

## Authorization Consumption

After row guards pass, 31B copies the approved global authorization into:

`%AIW31BRunAllowSendLatch`

Then it immediately sets:

`%AIW27BAllowSend = 0`

All later send checks use the local latch. The only remaining global `%AIW27BAllowSend` condition is the initial pre-consume check. Every Stop exit has immediate `%AIW27BAllowSend=0` and `%AIW31BRunAllowSendLatch=0` before stopping.

## Persistent Pre-Send State

Before TextNow launch, 31B writes exact row status:

`SENDING`

The SENDING write:

- uses the existing row-status update shape
- has Continue Task After Error enabled
- retries once after 3 seconds if needed
- reads back the status cell
- requires readback value `SENDING`
- requires readback array count `1`
- stops before TextNow if SENDING is not confirmed

## Post-Send State

After the exact Send-button AutoInput action, 31B no longer writes `DONE`.

31B now writes:

`SEND_CLICKED_AWAITING_CONFIRM`

The post-Send status write:

- retries once after 3 seconds if needed
- records `POST_SEND_STATUS_UPDATE_FAILED` if both attempts fail
- leaves the row in `SENDING` if the post-Send status update fails
- releases the Send lock on both success and failure
- never retries the Send click

31B does not set final sent proof:

- `%SSSentOne=1`: removed from task 224
- `%SSResult=SENT`: removed from task 224
- `DONE` row update: removed from task 224

Final DONE remains a controller action after ChatGPT verifies the phone recording, correct thread, exact reply, exactly one outgoing message, and no duplicate.
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
- Output task actions after superseding wrapper insertion: `470`
- Output clearing before both reads: PASS
- First-element checks present for all five outputs: PASS
- Array-count checks present for all five outputs: PASS
- AutoSheets read attempts for the staged row range: `2`
- AutoSheets Continue Task After Error enabled: PASS
- AutoSheets configuration preserved except required Continue Task After Error change: PASS
- Pre-send `SENDING` updates: `2`
- Pre-send SENDING readback checks: `1`
- Post-Send `SEND_CLICKED_AWAITING_CONFIRM` updates: `2`
- `DONE` updates in task 224: `0`
- `%SSSentOne=1` in task 224: `0`
- `%SSResult=SENT` in task 224: `0`
- If/End If count in task 224: `57 / 57`
- Final If stack depth: `0`
- Search lane unchanged semantically: PASS
- AutoInput nodes unchanged semantically excluding Tasker action sr/location renumbering: PASS
- Current key unchanged without printing it: PASS
- ZIP integrity: PASS
- Private files tracked by Git: NO

## Private Package Hashes

- 31B superseding full private XML SHA256: `156D44624EF534DB8F0D4E81F0E873A44FE8A9560B26D1C260348AFA4ED8B820`
- 31B superseding private ZIP SHA256: `B6C8126034AE775157105A0343F627464AF1F1626B44584CA9140DA3B0D3B67D`

## Proof Boundary

31B is a private runtime candidate for ChatGPT audit.

- Phone proof claimed: NO
- Phone import approved by Codex: NO
- Sheet changed: NO
- Tracker percentage changed: NO
- Controlled Send remains HOLD
