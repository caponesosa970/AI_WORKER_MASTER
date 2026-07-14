# Confirmation State Machine

## Entry

1. Validate dynamic row and expected ID before lock/UI.
2. Reject an active confirmation lock without clearing it.
3. Acquire `%AIWConfirming` and local ownership.

## Bound Row

1. Read exact `Sheet1!A<row>:E<row>` with at most two attempts.
2. Clear output arrays before each attempt.
3. Require exact ID, exact `SEND_CLICKED_AWAITING_CONFIRM`, valid sender, and valid exact reply.
4. Never mutate the Sheet on read/binding failure.

## Phone Read

1. Launch TextNow using the preserved Plan A launch action.
2. Run the exact exported Get Screen Info action.
3. Require exact TextNow package.
4. Iterate native ordered JSON `text` elements.
5. Require normalized sender identity, one exact reply, and immediate next non-empty `Sent`.

## DONE

1. Reachable only when `%confirmation_positive=1`.
2. Update exact `D<row>` to DONE with at most two attempts.
3. Re-read exact `A<row>:D<row>` with at most two attempts.
4. Report `CONFIRM_DONE_VERIFIED` only when ID and DONE both match.
5. Update/readback uncertainty returns HOLD, never a false DONE claim.

## Exit

Every owned-lock path reaches one common release block exactly once. Invalid parameters and lock-busy paths stop before ownership. No path can click Send.
