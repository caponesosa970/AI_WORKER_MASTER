# V15A Working TextNow Action Contract Audit - 20260709

FINAL STATUS: AUDIT ONLY / RETURN TO CHATGPT

## Source Truth
- Drive title: `basefile_v15a_phone_send_cleanup_pass.xml`
- Drive file ID: `1ApmhN8tYy248mAnbDgeTnZhyXh7-fPAz`
- Drive link: https://drive.google.com/file/d/1ApmhN8tYy248mAnbDgeTnZhyXh7-fPAz/view?usp=drivesdk
- Local source used for parsing: `C:\Users\Shadow\Documents\ai work\AI_WORKER_MASTER\02_TEST_LOGS\PROJECT_WIDE_VALUE_PRESERVATION_AUDIT_20260709\sources\basefile_v15a_phone_send_cleanup_pass.xml`
- Local SHA256: `C4CDEAA0BFD78120386FF1B03FA0A2D6B13BCEEDBD15687F84D03A3AD5FEF1C8`
- Role: source truth / high-trust phone-proven v15a reference for TextNow send-cleanup behavior.
- Phone proof claimed by this audit: NO. This audit only extracts and classifies the XML contract.

## Scope
- Focus task: `FINAL Send Sheet`
- Helpers inspected: `SS Reset Result Flags`, `SS Fail UI Dirty Stop`, `SS Lock Release HARD`
- Runtime patch/build/import package created: NO

## Direct Helper Calls From FINAL Send Sheet
| Action | Helper | Perform Task Priority | Classification |
|---:|---|---:|---|
| 0 | `SS Reset Result Flags` | 100 | safe helper |
| 31 | `SS Lock Release HARD` | 100 | safe helper |
| 55 | `SS Lock Release HARD` | 100 | safe helper |
| 64 | `SS Lock Release HARD` | 100 | safe helper |
| 81 | `SS Fail UI Dirty Stop` | 100 | failure-routing helper |
| 90 | `SS Fail UI Dirty Stop` | 100 | failure-routing helper |
| 101 | `SS Fail UI Dirty Stop` | 100 | failure-routing helper |
| 110 | `SS Fail UI Dirty Stop` | 100 | failure-routing helper |
| 125 | `SS Fail UI Dirty Stop` | 100 | failure-routing helper |
| 134 | `SS Lock Release HARD` | 100 | safe helper |
| 138 | `SS Lock Release HARD` | 100 | safe helper |

## Exact Ordered Action List - FINAL Send Sheet
| Action | Code | Kind | Summary |
|---:|---:|---|---|
| 0 | `130` | Perform Task | Perform Task SS Reset Result Flags priority 100 |
| 1 | `37` | If | If %AIWSending op2 1 |
| 2 | `547` | Variable Set | Set %SSBlocked = 1 |
| 3 | `547` | Variable Set | Set %SSFailed = 1 |
| 4 | `547` | Variable Set | Set %SSResult = SEND_BLOCKED_LOCK |
| 5 | `547` | Variable Set | Set %SSLastError = SEND blocked already sending |
| 6 | `547` | Variable Set | Set %AIWorkerLastError = SEND blocked already sending |
| 7 | `137` | Stop | Stop task |
| 8 | `38` | End If | End If |
| 9 | `547` | Variable Set | Set %AIWSending = 1 |
| 10 | `547` | Variable Set | Set %AIWSendingStartedAt = %TIMES |
| 11 | `547` | Variable Set | Set %AIWorkerLastError = SEND LOCK STARTED |
| 12 | `1810865467` | AutoSheets GetData | Spreadsheet ID: [REDACTED_LONG_ID] | Sheet Name: QueueView | Mode: Columns | Output Array Names: qv_source,id,sender,message,status,reply,touch,button,time,ticker | Range: A2:J201 | Joiner: § | Output Format: Formatted |
| 13 | `547` | Variable Set | Set %SSResult = NO_READY |
| 14 | `547` | Variable Set | Set %SSLastError = SEND read QueueView, no READY found yet |
| 15 | `547` | Variable Set | Set %count = 0 |
| 16 | `39` | Action | 39 %dummy %status() |
| 17 | `888` | Action | 888 %count |
| 18 | `547` | Variable Set | Set %realrow = %qv_source(%count) |
| 19 | `547` | Variable Set | Set %curstatus = %status(%count) |
| 20 | `37` | If | If %curstatus op2 READY_TO_SEND |
| 21 | `547` | Variable Set | Set %SSFoundReady = 1 |
| 22 | `547` | Variable Set | Set %SSRealRow = %realrow |
| 23 | `547` | Variable Set | Set %SSResult = FOUND_READY |
| 24 | `547` | Variable Set | Set %SSLastError = SEND found READY row:%SSRealRow |
| 25 | `37` | If | If %AIWorkerSafeMode op2 1 |
| 26 | `547` | Variable Set | Set %SSResult = SAFE_MODE_REVIEW |
| 27 | `547` | Variable Set | Set %SSLastError = SEND safe mode held row:%SSRealRow |
| 28 | `547` | Variable Set | Set %SSSentOne = 0 |
| 29 | `1461810131` | AutoSheets UpdateCells | Spreadsheet ID: [REDACTED_LONG_ID] | Sheet Name: Sheet1 | Cell Reference: D%realrow | Rows Or Columns: Rows | Data: REVIEW_READY | Separator: § | Row Separator:  |  | Mode: Parsed |
| 30 | `547` | Variable Set | Set %AIWorkerLastError = Safe Mode held row %realrow for review |
| 31 | `130` | Perform Task | Perform Task SS Lock Release HARD priority 100 |
| 32 | `137` | Stop | Stop task |
| 33 | `38` | End If | End If |
| 34 | `547` | Variable Set | Set %sendname = %sender(%count) |
| 35 | `547` | Variable Set | Set %sendreply = %reply(%count) |
| 36 | `598` | Action | 598 %sendname ^'+ |
| 37 | `598` | Action | 598 %sendreply ^'+ |
| 38 | `37` | If | If %sendname op4 (?i).*#error.* |
| 39 | `547` | Variable Set | Set %sendname = %ticker(%count) |
| 40 | `598` | Action | 598 %sendname ^TITLE: |
| 41 | `598` | Action | 598 %sendname \sTICKER:.*$ |
| 42 | `598` | Action | 598 %sendname :.*$ |
| 43 | `38` | End If | End If |
| 44 | `37` | If | If %sendname op4 ^\+ |
| 45 | `598` | Action | 598 %sendname [^0-9] |
| 46 | `598` | Action | 598 %sendname ^1 |
| 47 | `38` | End If | End If |
| 48 | `547` | Variable Set | Set %sendsearch = %sendname |
| 49 | `37` | If | If %sendname op4 (?i)^$|.*#error.*|^%.*$ |
| 50 | `547` | Variable Set | Set %SSSkippedBadData = 1 |
| 51 | `547` | Variable Set | Set %SSFailed = 1 |
| 52 | `547` | Variable Set | Set %SSResult = BAD_DATA_CONTINUE |
| 53 | `547` | Variable Set | Set %SSLastError = SEND bad sender review row:%SSRealRow sendname:%sendname |
| 54 | `1461810131` | AutoSheets UpdateCells | Spreadsheet ID: [REDACTED_LONG_ID] | Sheet Name: Sheet1 | Cell Reference: D%realrow | Rows Or Columns: Rows | Data: ERROR_SEND_REVIEW | Separator: § | Row Separator:  |  | Mode: Parsed |
| 55 | `130` | Perform Task | Perform Task SS Lock Release HARD priority 100 |
| 56 | `137` | Stop | Stop task |
| 57 | `38` | End If | End If |
| 58 | `37` | If | If %sendreply op4 (?i)^$|.*#error.*|^%.*$ |
| 59 | `547` | Variable Set | Set %SSSkippedBadData = 1 |
| 60 | `547` | Variable Set | Set %SSFailed = 1 |
| 61 | `547` | Variable Set | Set %SSResult = BAD_DATA_CONTINUE |
| 62 | `547` | Variable Set | Set %SSLastError = SEND bad reply review row:%SSRealRow reply:%sendreply |
| 63 | `1461810131` | AutoSheets UpdateCells | Spreadsheet ID: [REDACTED_LONG_ID] | Sheet Name: Sheet1 | Cell Reference: D%realrow | Rows Or Columns: Rows | Data: ERROR_SEND_REVIEW | Separator: § | Row Separator:  |  | Mode: Parsed |
| 64 | `130` | Perform Task | Perform Task SS Lock Release HARD priority 100 |
| 65 | `137` | Stop | Stop task |
| 66 | `38` | End If | End If |
| 67 | `1461810131` | AutoSheets UpdateCells | Spreadsheet ID: [REDACTED_LONG_ID] | Sheet Name: Sheet1 | Cell Reference: D%realrow | Rows Or Columns: Rows | Data: SENDING | Separator: § | Row Separator:  |  | Mode: Parsed |
| 68 | `547` | Variable Set | Set %SSResult = UI_STARTED |
| 69 | `547` | Variable Set | Set %SSLastError = SEND UI started row:%SSRealRow search:%sendsearch |
| 70 | `20` | Launch App | Launch TextNow |
| 71 | `30` | Wait | Wait 662 ms secFlag=0 |
| 72 | `1732635924` | AutoInput Action | AutoInput Click Text Navigate up timeout=4 continueAfterError=0 |
| 73 | `30` | Wait | Wait 627 ms secFlag=0 |
| 74 | `1732635924` | AutoInput Action | AutoInput Click Text Chats timeout=4 continueAfterError=0 |
| 75 | `30` | Wait | Wait 433 ms secFlag=1 |
| 76 | `549` | Variable Clear | Clear %err |
| 77 | `549` | Variable Clear | Clear %errmsg |
| 78 | `547` | Variable Set | Set %SSUIStep = SEARCH_ICON |
| 79 | `1732635924` | AutoInput Action | AutoInput Click Id com.enflick.android.TextNow:id/menu_search timeout=12 continueAfterError=1 |
| 80 | `37` | If | If %err op4 ^[0-9]+$ |
| 81 | `130` | Perform Task | Perform Task SS Fail UI Dirty Stop priority 100 |
| 82 | `137` | Stop | Stop task |
| 83 | `38` | End If | End If |
| 84 | `30` | Wait | Wait 347 ms secFlag=1 |
| 85 | `549` | Variable Clear | Clear %err |
| 86 | `549` | Variable Clear | Clear %errmsg |
| 87 | `547` | Variable Set | Set %SSUIStep = SEARCH_FIELD |
| 88 | `1732635924` | AutoInput Action | AutoInput Click Id com.enflick.android.TextNow:id/search_field timeout=12 continueAfterError=1 |
| 89 | `37` | If | If %err op4 ^[0-9]+$ |
| 90 | `130` | Perform Task | Perform Task SS Fail UI Dirty Stop priority 100 |
| 91 | `137` | Stop | Stop task |
| 92 | `38` | End If | End If |
| 93 | `30` | Wait | Wait 500 ms secFlag=0 |
| 94 | `328` | Keyboard | Keyboard deleteAll(),wait(300),write(%sendsearch) |
| 95 | `30` | Wait | Wait 344 ms secFlag=1 |
| 96 | `549` | Variable Clear | Clear %err |
| 97 | `549` | Variable Clear | Clear %errmsg |
| 98 | `547` | Variable Set | Set %SSUIStep = CONTACT_PICK |
| 99 | `1732635924` | AutoInput Action | AutoInput Click List 1 timeout=15 continueAfterError=0 |
| 100 | `37` | If | If %err op4 ^[0-9]+$ |
| 101 | `130` | Perform Task | Perform Task SS Fail UI Dirty Stop priority 100 |
| 102 | `137` | Stop | Stop task |
| 103 | `38` | End If | End If |
| 104 | `30` | Wait | Wait 307 ms secFlag=1 |
| 105 | `549` | Variable Clear | Clear %err |
| 106 | `549` | Variable Clear | Clear %errmsg |
| 107 | `547` | Variable Set | Set %SSUIStep = MESSAGE_BOX |
| 108 | `1732635924` | AutoInput Action | AutoInput Click Id com.enflick.android.TextNow:id/edit_text_out timeout=15 continueAfterError=0 |
| 109 | `37` | If | If %err op4 ^[0-9]+$ |
| 110 | `130` | Perform Task | Perform Task SS Fail UI Dirty Stop priority 100 |
| 111 | `137` | Stop | Stop task |
| 112 | `38` | End If | End If |
| 113 | `30` | Wait | Wait 500 ms secFlag=0 |
| 114 | `547` | Variable Set | Set %LastBotReply = %sendreply |
| 115 | `547` | Variable Set | Set %LastBotTime = %TIMES |
| 116 | `328` | Keyboard | Keyboard deleteAll(),wait(250),deleteAll(),wait(250),write(%sendreply) |
| 117 | `30` | Wait | Wait 700 ms secFlag=0 |
| 118 | `547` | Variable Set | Set %SSResult = [REDACTED_LONG_ID] |
| 119 | `30` | Wait | Wait 526 ms secFlag=0 |
| 120 | `549` | Variable Clear | Clear %err |
| 121 | `549` | Variable Clear | Clear %errmsg |
| 122 | `547` | Variable Set | Set %SSUIStep = SEND_BUTTON |
| 123 | `1732635924` | AutoInput Action | AutoInput Click Id com.enflick.android.TextNow:id/button_send timeout=15 continueAfterError=0 |
| 124 | `37` | If | If %err op4 ^[0-9]+$ |
| 125 | `130` | Perform Task | Perform Task SS Fail UI Dirty Stop priority 100 |
| 126 | `137` | Stop | Stop task |
| 127 | `38` | End If | End If |
| 128 | `30` | Wait | Wait 538 ms secFlag=0 |
| 129 | `1461810131` | AutoSheets UpdateCells | Spreadsheet ID: [REDACTED_LONG_ID] | Sheet Name: Sheet1 | Cell Reference: D%realrow | Rows Or Columns: Rows | Data: DONE | Separator: § | Row Separator:  |  | Mode: Parsed |
| 130 | `547` | Variable Set | Set %SSSentOne = 1 |
| 131 | `547` | Variable Set | Set %SSFailed = 0 |
| 132 | `547` | Variable Set | Set %SSResult = SENT |
| 133 | `547` | Variable Set | Set %SSLastError = SEND sent row:%SSRealRow name:%sendname |
| 134 | `130` | Perform Task | Perform Task SS Lock Release HARD priority 100 |
| 135 | `137` | Stop | Stop task |
| 136 | `38` | End If | End If |
| 137 | `40` | Action | 40 |
| 138 | `130` | Perform Task | Perform Task SS Lock Release HARD priority 100 |
| 139 | `547` | Variable Set | Set %SSResult = NO_READY |
| 140 | `547` | Variable Set | Set %SSLastError = SEND no READY_TO_SEND rows |
| 141 | `547` | Variable Set | Set %SSSentOne = 0 |
| 142 | `547` | Variable Set | Set %AIWorkerLastError = SEND complete no more READY_TO_SEND rows |

## Helper Summary
### SS Reset Result Flags
- Task ID: `211`
- Action count: 9
| Action | Code | Kind | Summary |
|---:|---:|---|---|
| 0 | `547` | Variable Set | Set %SSFoundReady = 0 |
| 1 | `547` | Variable Set | Set %SSSentOne = 0 |
| 2 | `547` | Variable Set | Set %SSFailed = 0 |
| 3 | `547` | Variable Set | Set %SSBlocked = 0 |
| 4 | `547` | Variable Set | Set %SSDirtyUI = 0 |
| 5 | `547` | Variable Set | Set %SSSkippedBadData = 0 |
| 6 | `547` | Variable Set | Set %SSResult = START |
| 7 | `547` | Variable Set | Set %SSRealRow = 0 |
| 8 | `547` | Variable Set | Set %SSLastError = SEND result flags reset |

### SS Fail UI Dirty Stop
- Task ID: `212`
- Action count: 10
| Action | Code | Kind | Summary |
|---:|---:|---|---|
| 0 | `547` | Variable Set | Set %SSDirtyUI = 1 |
| 1 | `547` | Variable Set | Set %SSFailed = 1 |
| 2 | `547` | Variable Set | Set %SSSentOne = 0 |
| 3 | `547` | Variable Set | Set %SSResult = SEND_FAILED_STOP |
| 4 | `547` | Variable Set | Set %SSLastError = SEND UI dirty stop row:%SSRealRow step:%SSUIStep err:%err msg:%errmsg |
| 5 | `37` | If | If %SSRealRow op4 ^[0-9]+$ |
| 6 | `1461810131` | AutoSheets UpdateCells | Spreadsheet ID: [REDACTED_LONG_ID] | Sheet Name: Sheet1 | Cell Reference: D%SSRealRow | Rows Or Columns: Rows | Data: ERROR_SEND_REVIEW | Separator: § | Row Separator:  |  | Mode: Parsed |
| 7 | `38` | End If | End If |
| 8 | `547` | Variable Set | Set %AIWorkerLastError = %SSLastError |
| 9 | `130` | Perform Task | Perform Task SS Lock Release HARD priority 100 |

### SS Lock Release HARD
- Task ID: `17`
- Action count: 3
| Action | Code | Kind | Summary |
|---:|---:|---|---|
| 0 | `547` | Variable Set | Set %AIWSending = 0 |
| 1 | `549` | Variable Clear | Clear %AIWSendingStartedAt |
| 2 | `547` | Variable Set | Set %AIWorkerLastError = SEND LOCK RELEASED HARD |

## Main Contract Findings
- v15a uses `SS Reset Result Flags` at the start to clear stale send-result state.
- v15a writes `SENDING` before opening TextNow. That is blocked for current no-send gates.
- v15a uses screen recovery before search: launch TextNow, wait, optional Navigate up, wait, optional Chats, wait.
- v15a marks required UI steps in `%SSUIStep`: `SEARCH_ICON`, `SEARCH_FIELD`, `CONTACT_PICK`, `MESSAGE_BOX`, `SEND_BUTTON`.
- v15a clears `%err` and `%errmsg` before required proof steps, then checks errors immediately after required AutoInput actions.
- v15a routes failed required UI steps to `SS Fail UI Dirty Stop` and stops, preventing false pass after a failed required action.
- v15a uses list item `1` for contact pick. That may be high-trust for old working send behavior, but it is blocked for current gates because search result is not identity proof.
- v15a focuses compose, writes reply, taps `button_send`, and writes DONE. All are blocked for current no-send gates.

## Reuse Recommendation
- Preserve exactly as action-shape reference: launch TextNow, waits, optional Navigate up/Chats fallback, required Search icon click, required Search field click, keyboard `deleteAll(),wait(...),write(...)`, `%SSUIStep` markers, `%err/%errmsg` clear/check/fail routing pattern.
- Isolate behind manual start state: any TextNow UI lane should start only after row/recipient/reply/no-send flags are locked.
- Block: list item 1 result select, compose focus, reply write, `button_send`, `SENDING`, `DONE`, archive/live/capacity.
- Needs Sosa phone-set AutoInput: any new target not already present in v15a or phone-exported XML.
