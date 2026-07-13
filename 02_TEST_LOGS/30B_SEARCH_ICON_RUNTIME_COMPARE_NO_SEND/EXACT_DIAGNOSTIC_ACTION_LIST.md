# EXACT DIAGNOSTIC ACTION LIST - 30B1

Task: `AIW30B_SEARCH_ICON_RUNTIME_COMPARE_NO_SEND`

This is the repaired diagnostic wrapper. It removes the unreachable Dashgood retry/failure branch and balances Tasker If/End If flow.

| Index | Code | AutoInput | Summary |
|---:|---:|---|---|
| 0 | 547 | False | 547 %AIW30BResult START 0 0 0 3 1 |
| 1 | 547 | False | 547 %AIW30BStep START 0 0 0 3 1 |
| 2 | 547 | False | 547 %AIW30BV15AErr 0 0 0 3 1 |
| 3 | 547 | False | 547 %AIW30BV15AErrMsg 0 0 0 3 1 |
| 4 | 547 | False | 547 %AIW30BDashErr 0 0 0 3 1 |
| 5 | 547 | False | 547 %AIW30BDashErrMsg 0 0 0 3 1 |
| 6 | 20 | False | 20 authorization.ui.AuthorizationActivity com.enflick.android.TextNow TextNow |
| 7 | 30 | False | 30 |
| 8 | 547 | False | 547 %AIW30BStep V15A_NAVIGATE_UP 0 0 0 3 1 |
| 9 | 547 | False | 547 %AIW30BResult V15A_NAVIGATE_UP_NOT_COMPLETED 0 0 0 3 1 |
| 10 | 1732635924 | True | 1732635924 false Navigate up java.lang.String 16 java.lang.String <null> java.lang.String 0 java.lang.String false java.lang.Bo... |
| 11 | 547 | False | 547 %AIW30BResult V15A_NAVIGATE_UP_PASS 0 0 0 3 1 |
| 12 | 30 | False | 30 |
| 13 | 547 | False | 547 %AIW30BStep V15A_CHATS 0 0 0 3 1 |
| 14 | 547 | False | 547 %AIW30BResult V15A_CHATS_NOT_COMPLETED 0 0 0 3 1 |
| 15 | 1732635924 | True | 1732635924 false Chats java.lang.String 16 java.lang.String <null> java.lang.String 0 java.lang.String false java.lang.Boolean ... |
| 16 | 547 | False | 547 %AIW30BResult V15A_CHATS_PASS 0 0 0 3 1 |
| 17 | 30 | False | 30 |
| 18 | 547 | False | 547 %AIW30BStep V15A_ID_SEARCH 0 0 0 3 1 |
| 19 | 547 | False | 547 %AIW30BResult V15A_ID_SEARCH_NOT_COMPLETED 0 0 0 3 1 |
| 20 | 547 | False | 547 %err 0 0 0 3 1 |
| 21 | 547 | False | 547 %errmsg 0 0 0 3 1 |
| 22 | 1732635924 | True | 1732635924 false com.enflick.android.TextNow:id/menu_search java.lang.String 16 java.lang.String <null> java.lang.String 1 java... |
| 23 | 547 | False | 547 %AIW30BResult V15A_ID_SEARCH_PASS 0 0 0 3 1 |
| 24 | 547 | False | 547 %AIW30BV15AErr %err 0 0 0 3 1 |
| 25 | 547 | False | 547 %AIW30BV15AErrMsg %errmsg 0 0 0 3 1 |
| 26 | 37 | False | 37 %err 4 ^$ |
| 27 | 30 | False | 30 |
| 28 | 547 | False | 547 %AIW30BStep V15A_SEARCH_FIELD 0 0 0 3 1 |
| 29 | 547 | False | 547 %AIW30BResult V15A_SEARCH_FIELD_NOT_COMPLETED 0 0 0 3 1 |
| 30 | 547 | False | 547 %err 0 0 0 3 1 |
| 31 | 547 | False | 547 %errmsg 0 0 0 3 1 |
| 32 | 1732635924 | True | 1732635924 false com.enflick.android.TextNow:id/search_field java.lang.String 16 java.lang.String <null> java.lang.String 1 jav... |
| 33 | 547 | False | 547 %AIW30BResult V15A_SEARCH_FIELD_PASS 0 0 0 3 1 |
| 34 | 547 | False | 547 %AIW30BV15AErr %err 0 0 0 3 1 |
| 35 | 547 | False | 547 %AIW30BV15AErrMsg %errmsg 0 0 0 3 1 |
| 36 | 37 | False | 37 %err 4 ^$ |
| 37 | 547 | False | 547 %AIW30BStep V15A_COMPLETE 0 0 0 3 1 |
| 38 | 547 | False | 547 %AIW30BResult V15A_ID_SEARCH_AND_FIELD_PASS 0 0 0 3 1 |
| 39 | 137 | False | 137 0 0 |
| 40 | 38 | False | 38 |
| 41 | 38 | False | 38 |
| 42 | 547 | False | 547 %AIW30BStep DASHGOOD_RESET_NAVIGATION 0 0 0 3 1 |
| 43 | 30 | False | 30 |
| 44 | 547 | False | 547 %AIW30BStep DASHGOOD_NAVIGATE_UP 0 0 0 3 1 |
| 45 | 547 | False | 547 %AIW30BResult DASHGOOD_NAVIGATE_UP_NOT_COMPLETED 0 0 0 3 1 |
| 46 | 1732635924 | True | 1732635924 false Navigate up java.lang.String 16 java.lang.String <null> java.lang.String 0 java.lang.String false java.lang.Bo... |
| 47 | 547 | False | 547 %AIW30BResult DASHGOOD_NAVIGATE_UP_PASS 0 0 0 3 1 |
| 48 | 30 | False | 30 |
| 49 | 547 | False | 547 %AIW30BStep DASHGOOD_CHATS 0 0 0 3 1 |
| 50 | 547 | False | 547 %AIW30BResult DASHGOOD_CHATS_NOT_COMPLETED 0 0 0 3 1 |
| 51 | 1732635924 | True | 1732635924 false Chats java.lang.String 16 java.lang.String <null> java.lang.String 0 java.lang.String false java.lang.Boolean ... |
| 52 | 547 | False | 547 %AIW30BResult DASHGOOD_CHATS_PASS 0 0 0 3 1 |
| 53 | 30 | False | 30 |
| 54 | 547 | False | 547 %AIW30BStep DASHGOOD_TEXT_SEARCH 0 0 0 3 1 |
| 55 | 547 | False | 547 %AIW30BResult DASHGOOD_TEXT_SEARCH_NOT_COMPLETED 0 0 0 3 1 |
| 56 | 1732635924 | True | 1732635924 false Search java.lang.String 16 java.lang.String <null> java.lang.String 0 java.lang.String false java.lang.Boolean... |
| 57 | 547 | False | 547 %AIW30BResult DASHGOOD_TEXT_SEARCH_PASS 0 0 0 3 1 |
| 58 | 30 | False | 30 |
| 59 | 547 | False | 547 %AIW30BStep DASHGOOD_SEARCH_FIELD_1 0 0 0 3 1 |
| 60 | 547 | False | 547 %AIW30BResult DASHGOOD_SEARCH_FIELD_1_NOT_COMPLETED 0 0 0 3 1 |
| 61 | 1732635924 | True | 1732635924 false com.enflick.android.TextNow:id/search_field java.lang.String 16 java.lang.String <null> java.lang.String 1 jav... |
| 62 | 547 | False | 547 %AIW30BResult DASHGOOD_SEARCH_FIELD_1_PASS 0 0 0 3 1 |
| 63 | 547 | False | 547 %AIW30BStep DASHGOOD_SEARCH_FIELD_2 0 0 0 3 1 |
| 64 | 547 | False | 547 %AIW30BResult DASHGOOD_SEARCH_FIELD_2_NOT_COMPLETED 0 0 0 3 1 |
| 65 | 1732635924 | True | 1732635924 false com.enflick.android.TextNow:id/search_field java.lang.String 16 java.lang.String <null> java.lang.String 1 jav... |
| 66 | 547 | False | 547 %AIW30BResult DASHGOOD_SEARCH_FIELD_2_PASS 0 0 0 3 1 |
| 67 | 547 | False | 547 %AIW30BStep DASHGOOD_COMPLETE 0 0 0 3 1 |
| 68 | 547 | False | 547 %AIW30BResult DASHGOOD_TEXT_SEARCH_AND_FIELD_PASS 0 0 0 3 1 |
| 69 | 137 | False | 137 0 0 |

Key safety points:

- No phone number is typed.
- No contact/result is selected.
- No compose field is focused.
- No reply is inserted.
- No Send/DONE/Archive path is present.
- Dashgood exact-off actions use pre-action `NOT_COMPLETED` markers and immediate `_PASS` markers only.
