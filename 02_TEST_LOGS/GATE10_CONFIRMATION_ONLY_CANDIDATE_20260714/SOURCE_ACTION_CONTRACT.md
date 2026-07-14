# Source Action Contract

## Base

- Corrected Plan A full-project SHA256: `82148AF8B72A24E3DBA77936A15E547E2114FEC01B705A084D12AA319534442B`
- Tasks 71, 199, and 223 are raw-byte identical to that base.
- The current private credential remains one unchanged occurrence in an untouched task.

## Phone-Exported Source

- Source SHA256: `C4850C3B24FA7A2E43FC424DF198EACB2DF2DFAE59B89AC42749349ECCD85C64`
- Source task: `AIW G10 OUTGOING READ SOURCE TEST`
- Task count: 1
- Action count: 10
- Selected action: action 6, native Tasker code 421, Get Screen Info (Assistant)
- Continue Task After Error: enabled (`se=false`)
- Relevant outputs used: `%ai_app_package`, `%ai_texts`
- Source/output semantic comparison excluding only action `sr`: PASS by two implementations

## Structured Parser

Tasker's native screen action returns `%ai_texts` as a JSON array. The candidate reads its `text` fields in order. It does not split a comma-joined string and does not use substring matching.

Positive confirmation requires all of these simultaneously:

1. package exactly `com.enflick.android.TextNow`;
2. normalized bound sender identity present;
3. exact bound reply is one complete ordered element;
4. exact reply occurrence count equals one;
5. next non-empty ordered element equals `Sent`;
6. no screen-read error and a resolved structured text count.

No AutoInput UI Query action was added.
