# Exact Runtime Change

Changed existing task: Task 238 - `PROCESS Controlled Capacity Batch`.

Action count: 389 -> 399.

Before each of the two existing AutoSheets Get Data actions, five Variable Clear actions were inserted in this exact order:

1. `%g14d_id1`
2. `%g14d_sender1`
3. `%g14d_message1`
4. `%g14d_status1`
5. `%g14d_reply1`

The existing base-array, `%err`, and `%errmsg` clears remain. The existing Get Data actions and plugin bundles are semantically identical. Required action `sr` values were renumbered. No action was removed or otherwise changed.

Get Data positions: `[162, 276]` -> `[167, 286]` in zero-based static indexing.
