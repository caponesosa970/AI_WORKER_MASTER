# AI Worker Release Dependency Graph

Updated: 2026-07-05

## Status

`CANDIDATE / HOLD FOR CHATGPT AUDIT`

## Dependency Graph

```mermaid
flowchart TD
  A["Current controlled Build100 candidate"] --> B["Group B2 Send UI Completion Dry-Run"]
  B --> C["Group C Controlled One-Send"]
  C --> D["Group D Live Controller / Timer Gates"]
  D --> E["Group E Maintenance / Recovery"]
  E --> F["Group F Capacity / Production"]
  F --> RC1["Release Candidate 1 Review"]

  L1["Stage3A Closeout LOCKED"] --> B
  L2["Stage4A No-Work Guard LOCKED"] --> B
  L3["Stage4B No-Ready HOLD Path LOCKED"] --> B
  L4["Stage4B Digits-Only Contact Pick LOCKED"] --> B

  X1["Failed packages quarantine"] -. blocks reuse .-> B
  X2["Missing historical proofs"] -. cannot promote .-> RC1
```

## Gate Order

1. Group B2 must pass before any controlled one-send.
2. Group C must pass before timer/live.
3. Group D must pass before archive/deadarchive/compactor/TT5.
4. Group E must pass or stay disabled before capacity proof.
5. Group F is last and cannot override the one-send rule.

## Shortest Safe Path To RC1

- Finish Group B2 dry-run UI completion.
- Run one isolated controlled-send proof.
- Prove live controller gates without expanding send count.
- Keep maintenance paths held unless explicitly tested.
- Run capacity proof last with one-send-per-cycle still enforced.
