# Exact Changed Task And Action List

| Task | Base actions | Output actions | Exact change |
| --- | ---: | ---: | --- |
| 70 - FINAL Retry Error Rows | 17 | 42 | Route only `ERROR_OPENAI_RETRY` to Task 236; retain non-OpenAI branches; add fail-closed read cleanup |
| 171 - PROCESS Call OpenAI HTTP | 28 | 24 | Replace direct HTTP with one Task 235 wrapper call and safe output/log routing |
| 173 - PROCESS Commit Failure | 15 | 15 | Request `ERROR_OPENAI_REVIEW` for final OpenAI/API failures |
| 192 - PROCESS Queue Health | 18 | 18 | Include `ERROR_OPENAI_REVIEW` in pressure accounting |
| 233 - PROCESS Exact Row Transaction | 1947 | 1947 | Extend one `COMMIT_FAILURE` accepted-status regex only |
| 235 - PROCESS OpenAI Bounded Retry | new | 243 | Maximum two HTTP attempts, one jittered retry, safe final classes |
| 236 - PROCESS Legacy OpenAI Retry Review | new | 266 | Exact-row/readback migration to `ERROR_OPENAI_REVIEW`, no API call |
| 237 - AIW GATE14C CONTROLLED OPENAI RETRY TEST | new | 308 | Isolated one-shot controlled launcher |

Task 233 exact field:

From:

`^(ERROR_PROCESS|ERROR_OPENAI_RETRY|ERROR_PROCESS_REVIEW)$`

To:

`^(ERROR_PROCESS|ERROR_OPENAI_RETRY|ERROR_PROCESS_REVIEW|ERROR_OPENAI_REVIEW)$`

No Task 233 action was added, removed, reordered, enabled, or disabled.
