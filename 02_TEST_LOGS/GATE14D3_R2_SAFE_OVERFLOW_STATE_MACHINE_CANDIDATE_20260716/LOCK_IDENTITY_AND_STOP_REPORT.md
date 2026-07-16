# Lock, Identity, And STOP Report

- Lock order is overflow owner first, admission owner second.
- Release order is admission owner first, overflow owner second.
- Release is rejected unless the stored owner equals the caller token.
- No age threshold clears an owner.
- STOP blocks every new acquisition.
- Durable drain states are persisted before later steps, so STOP cannot turn a partial main write into an untracked retry.
- `OriginalID` and `OverflowID` are separate numeric fields.
- Cross-store classification is fail-closed for exact duplicate, collision, and duplicate-main states.
- The legacy hard-release task has zero incoming callers.
