# Drain Lock Order Report

Validator result: PASS.

The drain path acquires overflow ownership before any source mutation. It then selects FIFO, direct-reads A:N, binds the exact source, writes DRAINING, and verifies that state before acquiring shared admission ownership.

The admission lock is therefore held only for the exact Sheet1 claim/reconciliation phase. No drain path acquires admission at task entry. Exact-owner equality is required before either lock can be released.

AIWStopRequested = 1 blocks new acquisition. After a durable source transition starts, the task reaches a verified state or leaves a persistent recoverable state before owned release.
