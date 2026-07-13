# SEARCH_ICON Field-By-Field Comparison

Status: PUBLIC-SAFE SUMMARY

No private XML content, local user paths, private Drive IDs, API keys, or phone numbers are included here.

## Compared Actions

| Source | Task | Action marker | Role |
|---|---|---|---|
| SRC-V15A-FINAL-SEND | `FINAL Send Sheet` | SEARCH_ICON | Disputed V15A source shape |
| SRC-27B-PRIVATE | `AIW27B_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE` | SEARCH_ICON | Current failed output shape |
| SRC-OLD-TEXT-SEARCH | `SS Safe Send Dry-Run` | SEARCH_ICON | Historical text-based candidate |

## Field Comparison

| Field | SRC-V15A-FINAL-SEND | SRC-27B-PRIVATE | SRC-OLD-TEXT-SEARCH |
|---|---|---|---|
| Type | Id | Id | Text |
| Value | TextNow menu_search resource | TextNow menu_search resource | Search |
| Action | Click | Click | Click |
| Field Selection Type | Id/resource mode | Id/resource mode | text mode |
| Resource ID | menu_search resource | menu_search resource | not used |
| Text target | not used | not used | Search |
| Point | not used | not used | not used |
| Nearby text | blank | blank | blank |
| Timeout | 12 | 12 | 12 |
| Continue After Error | enabled | enabled | disabled |
| Structure Output | XML field reports disabled; phone observation contradicts expected setup | XML field reports disabled; phone observation showed enabled/disputed setup | XML field reports disabled |
| Plugin bundle values | inspectable in static XML | inspectable in static XML | inspectable in static XML |
| Surrounding waits | present | present | present |
| Error checks | present after action | present after action | present after action |
| Failure routing | fail-stop route exists | fail-stop route exists | fail-stop route exists |

## Result

The current 27B output matches the V15A `menu_search` ID source shape closely enough to show why Codex called it preserved. That does not prove it is the right phone-visible action. The newest phone proof contradicts the action for this repair.

The text-based candidate is a different action shape and cannot be called preserved from V15A. It may be a future repair candidate only after source proof is supplied.
