# Common Failure Evidence Report

Validator result: PASS.

Every drain path that has bound an exact OverflowInbox source sets a source-bound marker. A common epilogue runs before lock release when the transaction failed and failure evidence has not already been verified.

The epilogue:

- re-reads exact A:N with cleared outputs and bounded attempts;
- verifies source identity;
- increments Attempts;
- appends the current safe error to existing LastError instead of erasing it;
- writes M:N;
- reads exact A-D/M/N back;
- requires exact Attempts and LastError equality.

Collision and duplicate-main review branches set the already-recorded marker after their own exact evidence readback. No failure path can report drain success from an unverified evidence write.
