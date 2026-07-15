# AutoSheets Transaction Audit

- Source: phone-proven Get Data and Update Cells nodes from protected Tasks 225 and 223.
- Get range: dynamic exact `A%PSMainRow:E%PSMainRow` only.
- Update cells: dynamic exact `D%PSMainRow` or `E%PSMainRow` only.
- `Continue Task After Error`: enabled on every cloned node (`<se>false</se>`).
- `updateLaterIfOffline`: false on every update.
- `createSheetIfNeeded`: false on every update.
- Arrays, `%err`, and `%errmsg`: cleared before each read attempt.
- Error detection: numeric `%err` only.
- Attempts: every plugin node is enclosed by a fixed `1,2` loop; no third attempt or infinite retry.
- Blank Reply: exact `%txn_replyN` placeholder uses a scoped flag; Variable Clear is never used as a usable blank.
- Readback after every write: required.
