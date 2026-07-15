# Plan A System Integration Map

| Task | Permanent role | Current correction |
| ---: | --- | --- |
| 71 | READY_TO_SEND selector | AutoSheets `se=false` only |
| 199 | Queue controller | Byte-identical; one Task 71 call; historical maintenance branches unchanged |
| 223 | Bound-row Send transaction | AutoSheets continuation and Send-error preservation repaired |
| 224 | Removable Gate 9 launcher | Byte-identical |

Permanent call graph:

`FINAL Queue Cycle` -> `FINAL Send Sheet` -> `FINAL Send One Bound Row`

Controlled Gate 9 call graph:

`AIW GATE9 CONTROLLED SEND TEST` -> `FINAL Send One Bound Row`

Task 224 does not call Task 199. Existing Task 199 maintenance calls therefore are not part of the Gate 9 controlled-test path.

No new Archive/DeadArchive call, flag, or connection was added. Tasks 71, 223, and 224 contain zero Archive actions.
