# Gate 14A Read-Only Capacity Inventory Candidate

- Main source commit: `1b73c48c77b05b2518c47d30387778f86b647576`
- Base: `GATE13R2_FULL_PROJECT_TASKER_IMPORT__CONFIRM_THREAD_NAVIGATION_PRIVATE.xml`
- Base SHA256: `1C4D13872C3D6B4579AA698F9E7D2F50F3E81467A4CBD4EAD63CD567087832A7`
- Candidate XML SHA256: `832BEB0F9764EB2838B08A582648097C49197C2A366931196E5F0311860529EF`
- Tracker: `13/14 locked = 93%` (unchanged)
- Runtime phone proof: NOT CLAIMED
- Phone import approval: NO
- Capacity proof: NOT CLAIMED

## Inputs

- Authorization: `%AIWG14AllowInventory = 1`, consumed immediately.
- Run ID: uppercase letters/numbers/underscore/hyphen, length 4-32.
- Expected count: exactly `1`, `5`, `10`, `25`, or `50`.

## Scan

The task reads `Sheet1!A2:I201`, scans IDs in array/source-row order, selects the exact `G14CAP-<RUN_ID>-` prefix, maps index 1 to source row 2, and records ordered rows, IDs, and senders.

## Independent Integrity Counters

Count, unique IDs, unique senders, duplicate IDs, duplicate senders, blank required fields, wrong statuses, nonblank replies, unresolved variables, `#ERROR` cells, and order failures are measured independently. Matching-prefix invalid rows are retained in the observed count and force HOLD.

## Result Priority

Read, count, duplicate-ID, duplicate-sender, status, reply, order, then field-integrity HOLD. `INVENTORY_PASS` requires every contract check to pass. No result writes to the Sheet.
