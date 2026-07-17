# Static Scenario Matrix

| Scenario | Static result |
|---|---|
| Authorization absent | HOLD before Task 238 |
| Invalid mode/run ID/count | HOLD before read/lock/API |
| Profile, worker, STOP, or transaction lock active | HOLD |
| Wrong row, ID, sender, message, or status | zero write-capable calls; HOLD |
| Nonblank or unresolved Reply before processing | zero write-capable calls; HOLD |
| Duplicate accepted ID | HOLD |
| Exact row NEW and blank Reply | one row transaction allowed |
| API success | exact REVIEW_READY and concrete Reply required |
| Final API failure | exact ERROR_OPENAI_REVIEW and blank Reply required |
| Parse/process review failure | exact safe review terminal required |
| Row remains PROCESSING | HOLD and no next row |
| Terminal readback mismatch | HOLD and no next row |
| STOP during a completed row | release current owned lock; no next row |
| Lock release fails | HOLD and no next row |
| 5-row model | exact 5 starts/completions; lock counts equal |
| 10-row model | exact 10 starts/completions; lock counts equal |
| 25-row model | exact 25 starts/completions; lock counts equal |
| 50-row model | exact 50 starts/completions; lock counts equal |
| Task 235 attempt bound | maximum two attempts; no third attempt |

These are static results only. No target-phone capacity claim is made.
