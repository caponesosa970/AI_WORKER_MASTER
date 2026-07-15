# Source Search And Selected Contracts

Runtime base:

- Gate 11 full-project XML - SHA256 `FF08EEFFC6E3D6350CEA10924164FAC962797BE984C3643B4A5A68E1D1095195` - authoritative build base.

Reference-only historical queue sources:

- v19 queue-safe grouping source - SHA256 `7D8E3B083BA517F6C4FFB37911D96CFFD300439B2EDE843A2E0D07A1EBCD01E1`.
- v12 queue-cycle-safe source - SHA256 `92212E46C43C10DFA8BEE7BEB067F008A8A8AA261987A1C7DD99203051AAC28E`.

The historical sources retained three same-cycle Send-selector calls and broad Archive behavior. They were inspected for queue history only and were not used as runtime bases.

Selected contracts:

- Task 199 production entry, watchdog, processing, maintenance-frequency, Safe Mode guard, KickPending behavior, and shared Send-selector source regions came from the Gate 11 base.
- Task 227 copied the two exact QueueView `A2:J201` AutoSheets Get Data plugin nodes from Gate 11 Task 71. Both retain Continue Task After Error ON and the exact ten-array output contract. The private spreadsheet identifier remains only in private XML.
- Task 227 consumes the existing result contracts of Task 225 and Task 226 by calling those preserved modules. It contains no confirmation or Archive mutation itself.
- Task 224 uses the existing Tasker export structure and calls only Task 199 with the controlled one-cycle tokens.

No AutoInput, Get Screen Info, Send, confirmation, or Archive transaction node was copied or rebuilt. Phone-proven Tasks 71, 223, 225, and 226 remain raw-byte identical.

Known capacity limit: the preserved queue and exact-row Archive range is SourceRow 2-201. Expansion remains a later capacity/release requirement.
