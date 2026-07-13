# V15A vs 27B SEARCH_ICON Exact Diff

Status: NO SEARCH_ICON FIELD DRIFT FOUND

## Compared Actions

| Source | Task | SEARCH_ICON action location |
|---|---|---|
| Authoritative V15A | `FINAL Send Sheet` | source SEARCH_ICON AutoInput action |
| Current private 27B | `AIW27B_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE` | target SEARCH_ICON AutoInput action |

## Byte-Level Result

| Check | Result |
|---|---|
| Raw XML node bytes equal | NO |
| Raw XML node bytes equal after preserving 27B action `sr` | YES |

Reason:

The action `sr` differs because the same AutoInput action lives at a different action index in the 27B task. The 27B action must keep its own `sr` to preserve action ordering. After adjusting only that ordering attribute, the XML node bytes match.

## Field-Level Result

| Field | V15A value | 27B value | Result |
|---|---|---|---|
| Type | Id | Id | MATCH |
| Value | `com.enflick.android.TextNow:id/menu_search` | `com.enflick.android.TextNow:id/menu_search` | MATCH |
| Action | Click | Click | MATCH |
| Field Selection Type | `1` | `1` | MATCH |
| resource ID | `com.enflick.android.TextNow:id/menu_search` | `com.enflick.android.TextNow:id/menu_search` | MATCH |
| text target | not used | not used | MATCH |
| point | blank | blank | MATCH |
| nearby text | `<null>` | `<null>` | MATCH |
| timeout | `12` | `12` | MATCH |
| Continue Task After Error | `1` | `1` | MATCH |
| Structure Output | `false` in XML | `false` in XML | MATCH |
| accessibility setting | `<null>` | `<null>` | MATCH |
| plugin type | AutoInput Perform Action | AutoInput Perform Action | MATCH |
| plugin instance ID | same value | same value | MATCH |
| variable outputs | `%err`, `%errmsg` available on error | `%err`, `%errmsg` available on error | MATCH |
| plugin bundle keys/values | same | same | MATCH |

## Surrounding Context

| Context item | V15A | 27B | Result |
|---|---|---|---|
| TextNow launch before search lane | present | present | MATCH |
| Wait before Navigate up fallback | `662 ms` | `662 ms` | MATCH |
| Navigate up fallback | Text click, timeout 4, Continue After Error off | same | MATCH |
| Wait before Chats fallback | `627 ms` | `627 ms` | MATCH |
| Chats fallback | Text click, timeout 4, Continue After Error off | same | MATCH |
| Wait before SEARCH_ICON | `433 ms` | `433 ms` | MATCH |
| Clear `%err` before SEARCH_ICON | yes | yes | MATCH |
| Clear `%errmsg` before SEARCH_ICON | yes | yes | MATCH |
| Set `%SSUIStep=SEARCH_ICON` | yes | yes | MATCH |
| SEARCH_ICON AutoInput | same after `sr` adjustment | same after `sr` adjustment | MATCH |
| Error check after SEARCH_ICON | present | present | MATCH |
| Failure helper | `SS Fail UI Dirty Stop` | `SS Fail UI Dirty Stop` | MATCH |
| Stop after SEARCH_ICON failure | present | present | MATCH |
| Wait before SEARCH_FIELD | `347 ms` | `347 ms` | MATCH |

Structural note:

V15A contains one surrounding parent-block `End If` near the SEARCH_ICON error path that is not part of the SEARCH_ICON AutoInput node. 27B keeps the required SEARCH_ICON failure route and stop behavior. This is surrounding task-structure context, not SEARCH_ICON field drift.

## Decision

No SEARCH_ICON XML/plugin-bundle drift exists. Do not create a fake repair.
