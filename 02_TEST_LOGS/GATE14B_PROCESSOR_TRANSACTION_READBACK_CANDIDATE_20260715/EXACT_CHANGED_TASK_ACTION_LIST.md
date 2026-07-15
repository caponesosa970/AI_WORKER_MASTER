# Exact Changed Task And Action List

| Task | Role | Source actions | Output actions | Change |
| --- | --- | ---: | ---: | --- |
| 166 | PROCESS Mark Main Processing | 8 | 16 | Replace direct unverified write with one `MARK_PROCESSING` engine call and verified-result mapping |
| 172 | PROCESS Commit Success | 16 | 24 | Preserve READY/REVIEW selection; call `COMMIT_SUCCESS`; block grouping on HOLD |
| 173 | PROCESS Commit Failure | 13 | 15 | Preserve existing failure classification; call `COMMIT_FAILURE`; report persistence only after readback |
| 233 | PROCESS Exact Row Transaction | new | 1947 | Exact A:E binding, bounded writes/reads, idempotency, partial-write routing |
| 234 | AIW GATE14B CONTROLLED PROCESS TRANSACTION TEST | new | 260 | Four isolated one-shot controlled scenarios and owned-lock cleanup |

Task 233 action-code inventory: 14 Get Data, 5 Update Cells, 19 bounded For loops, 19 waits, 19 write/read attempt counters, 486 If/End If pairs, 18 Else, and deterministic variable/result actions.

Task 234 action-code inventory: 2 Get Data, 0 Update Cells, 6 allowlisted Perform Task nodes, 2 bounded read loops, 45 If/End If pairs, and deterministic setup/result/cleanup actions.

No other existing task action changed.
