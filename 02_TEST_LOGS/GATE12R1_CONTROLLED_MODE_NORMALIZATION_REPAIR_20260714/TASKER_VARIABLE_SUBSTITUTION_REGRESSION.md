# Tasker Variable-Substitution Regression

Result: PASS

The validator models Tasker replacement of variable references embedded in action text before regex execution.

Original defect reproduced: PASS. With the rejected RHS fields, controlled arguments normalize to `PRODUCTION` and the one-cycle token is cleared.

## Required Scenarios

1. Controlled arguments:
   - mode: `GATE12_CONTROLLED`
   - mode2: `ONE_CYCLE`
   - controlled flag: `1`
   - mode valid: `1`
   - latch consumed: `True`
   - production entry skipped: `True`
   - busy acquired: `True`
   - router reached: `True`
   - result: PASS

2. Blank arguments normalize to `PRODUCTION` with blank mode2: PASS.

3. Literal unresolved arguments normalize to `PRODUCTION` with blank mode2: PASS.

4. Explicit production remains valid: `1` - PASS.

5. Controlled plus bad secondary token: `QUEUE_CYCLE_MODE_REJECTED`, no busy/router - PASS.

6. Bad primary mode: `QUEUE_CYCLE_MODE_REJECTED`, no busy/router - PASS.

7. Task 199 condition RHS contains neither dynamic `^%par1$` nor `^%par2$`: PASS.

8. Both corrected RHS fields literally equal `(?is)^\s*$|^%.*$`: PASS.

The percent sign in `%.*` is not followed by a Tasker variable-name character, so it remains regex text and matches only unresolved literal values beginning with `%`.
