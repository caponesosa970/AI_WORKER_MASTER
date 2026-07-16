# R2 To R3 Exact Repair

R2 was held before phone use. R3 repairs two audit findings without reopening unrelated runtime behavior.

## Drain Lock Order

R3 mutating drain order is:

1. acquire exact overflow owner;
2. select FIFO source by LoggedAt then source row;
3. direct-read and bind exact OverflowInbox A:N source;
4. write and read back DRAINING;
5. acquire exact shared admission owner;
6. scan Sheet1 and perform the idempotent main/source transaction;
7. release only matching owned locks.

Admission ownership is not acquired before the durable source transition.

## Bound Failure Evidence

After exact source binding, every failed drain reaches one common pre-release evidence path unless evidence was already written. It increments Attempts, preserves prior LastError by appending the current safe error, writes M:N, and requires exact A-D/M/N readback. Reads and writes are bounded to two attempts.

If failure evidence itself cannot be verified, the result is OVERFLOW_FAILURE_RECORD_HOLD; no success is reported.
