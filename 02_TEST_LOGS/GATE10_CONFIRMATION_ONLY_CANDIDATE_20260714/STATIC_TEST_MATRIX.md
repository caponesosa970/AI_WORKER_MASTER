# Static Test Matrix

| # | Scenario | Expected machine result | Result |
| ---: | --- | --- | --- |
| 1 | Positive exact reply + immediate Sent | DONE update/readback path | PASS |
| 2 | Wrong package | HOLD; no DONE | PASS |
| 3 | Wrong expected ID | HOLD; no UI mutation/DONE | PASS |
| 4 | Wrong row status | HOLD; no UI mutation/DONE | PASS |
| 5 | Blank sender | HOLD | PASS |
| 6 | Blank reply | HOLD | PASS |
| 7 | Missing sender identity | HOLD | PASS |
| 8 | Missing reply | HOLD | PASS |
| 9 | Reply appears twice | HOLD | PASS |
| 10 | Next text is not Sent | HOLD | PASS |
| 11 | Sent without exact reply | HOLD | PASS |
| 12 | Malformed ai_texts JSON | HOLD | PASS |
| 13 | Empty ai_texts | HOLD | PASS |
| 14 | Screen-read action error | HOLD | PASS |
| 15 | Initial Sheet read timeout twice | HOLD; lock released | PASS |
| 16 | DONE update failure | HOLD; DONE not claimed | PASS |
| 17 | DONE readback mismatch | HOLD; DONE not claimed | PASS |
| 18 | Confirmation lock busy | Blocked; foreign lock untouched | PASS |
| 19 | Every owned-lock exit | One release | PASS |
| 20 | No reachable Send path | Zero Send actions | PASS |

The parser model separately proved exact element equality, duplicate rejection, adjacency rejection, blank-element skipping, wrong-package rejection, missing-identity rejection, and substring-only rejection.

Phone behavior is not part of this static PASS.
