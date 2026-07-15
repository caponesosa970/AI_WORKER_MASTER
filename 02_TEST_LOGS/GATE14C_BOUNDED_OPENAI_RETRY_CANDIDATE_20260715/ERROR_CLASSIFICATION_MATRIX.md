# Error Classification Matrix

| Outcome | Retry | Final class |
| --- | ---: | --- |
| HTTP 200 plus usable data | no | `OPENAI_SUCCESS` |
| Network, timeout, missing code | once | `OPENAI_TRANSIENT_EXHAUSTED` after second failure |
| 408, 409, normal 429, 500, 502, 503, 504 | once | `OPENAI_TRANSIENT_EXHAUSTED` after second failure |
| 200 with blank, unresolved, or `#ERROR` data | once | `OPENAI_BAD_RESPONSE_EXHAUSTED` |
| 429 insufficient quota/billing/credit | no | `OPENAI_QUOTA_HOLD` |
| 401 or 403 | no | `OPENAI_AUTH_HOLD` |
| 400 or 422 | no | `OPENAI_BAD_REQUEST_HOLD` |
| 404 or invalid endpoint/model/input | no | `OPENAI_CONFIG_HOLD` |
| other non-transient response | no | `OPENAI_UNCLASSIFIED_HOLD` |

All final API failures request exact-row `ERROR_OPENAI_REVIEW`. No Gate 14C production path creates `ERROR_OPENAI_RETRY`.
