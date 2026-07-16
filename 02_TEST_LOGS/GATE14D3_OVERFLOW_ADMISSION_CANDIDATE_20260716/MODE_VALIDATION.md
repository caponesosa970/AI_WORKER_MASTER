# Mode Validation

## ADMIT_50_DEFER_1

- exact row-199 NEW/blank precheck required
- existing bounded batch called with count 50
- exact rows 149-198 are the only processor rows
- 50 started/completed/successful and balanced 50/50 locks required
- row 199 must remain exact NEW with blank Reply
- sole deferred row reported as 199

## DRAIN_DEFERRED_1

- exact row-199 NEW/blank precheck required
- only row 199 is bound
- one API success and one verified commit required
- row 199 must read back REVIEW_READY with a current nonblank Reply
- one owned lock must release exactly once

Wrong mode, run ID, authorization, profile, lock, or row state fails closed before processing.
