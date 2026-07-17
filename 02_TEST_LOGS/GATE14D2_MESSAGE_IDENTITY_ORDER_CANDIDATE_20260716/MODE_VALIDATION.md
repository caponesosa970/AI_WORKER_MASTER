# Mode Validation

## ORDER_AND_LATER_REPEAT

- Reserved rows are statically fixed to `199,200,201` in ascending order.
- Event IDs are distinct and bound to each exact row.
- All three rows use one identical synthetic sender.
- Rows 199 and 201 use the same message; row 201 has a different event ID.
- Each row requires exact A/B/C, `NEW`, and blank Reply before lock acquisition.
- Each row uses a separate owned processor lock.
- Exact `REVIEW_READY` and current `%PSReply` readback are required before release and the next row.
- Final success requires 3 starts, completions, successes, API calls, and lock acquire/releases, with zero skips, wrong rows, or stale replies.

## EXACT_DUPLICATE_ID

- Existing row-199 event ID must return TT5 duplicate result 1 and the TT5 duplicate marker.
- Unseen control ID must return result 0 and the TT5 pass marker.
- The eligible control ID is not processed.
- API, processor locks, and writes remain zero.

Independent mode models: PASS.
