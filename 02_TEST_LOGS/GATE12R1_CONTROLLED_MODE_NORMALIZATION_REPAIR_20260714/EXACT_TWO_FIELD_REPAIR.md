# Exact Two-Field Repair

Repair base: `GATE12_FULL_PROJECT_TASKER_IMPORT__QUEUE_LIFECYCLE_INTEGRATION_PRIVATE.xml`

Base SHA256: `11D2C17F1107F024155C775E9320D68E447086DA5C6E38C900618A162FD65902` - verified.

Changed runtime task: Task 199 `FINAL Queue Cycle` only.

Task 199 action count before and after: 180.

## Tasker Action 5 / XML act4

Field: `ConditionList/Condition/rhs`

Before: `(?is)^\s*$|^%par1$`

After: `(?is)^\s*$|^%.*$`

## Tasker Action 8 / XML act7

Field: `ConditionList/Condition/rhs`

Before: `(?is)^%par2$`

After: `(?is)^\s*$|^%.*$`

No other Task 199 field changed. Reverse replacement of these two fields reconstructs the rejected Gate 12 Task 199 raw node exactly.

Task 224 raw-byte identical: PASS.

Task 227 raw-byte identical: PASS.

Every other task, Project registry, all profiles, and the scene unchanged: PASS.
