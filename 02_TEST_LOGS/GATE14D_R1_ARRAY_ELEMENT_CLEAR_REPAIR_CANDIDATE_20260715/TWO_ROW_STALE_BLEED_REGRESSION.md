# Two-Row Stale-Bleed Regression

The independent state model reproduces the phone defect:

- Row 149 returns a real Reply into `%g14d_reply1`.
- A base-array clear alone leaves that generated element available.
- A blank row 150 Reply does not overwrite it.
- The old path therefore sees row 149's Reply during row 150 precheck.

R1 result:

- `%g14d_reply1` is explicitly cleared before row 150 Get Data.
- A blank Reply leaves the scoped unresolved placeholder `%g14d_reply1`.
- The existing proven regex `(?s)^[%]g14d_reply[0-9]+$` marks it blank.
- Row 150 cannot inherit row 149's Reply.
- A real row-150 nonblank Reply overwrites the placeholder and is not suppressed.

Static two-row regression: PASS. Target-phone behavior remains HOLD for direct Sosa proof after ChatGPT audits the exact artifact.
