# ChatGPT Full Artifact Audit Checklist

- [ ] Verify the repair base SHA256 `11D2C17F1107F024155C775E9320D68E447086DA5C6E38C900618A162FD65902`.
- [ ] Verify standalone XML SHA256 `3DC49BF47837403B36D1B213564F34BD6983598B6734429324FF0ACEDA7A23C8`.
- [ ] Verify ZIP SHA256 `0F3D2CAAA6DC74D34EA079618C343C6DB473AA8650A50534E887037600371817`.
- [ ] Confirm ZIP contains exactly one XML and its bytes match standalone XML.
- [ ] Compare rejected Gate 12 XML to Gate 12R1 byte-for-byte.
- [ ] Confirm only Task 199 changed.
- [ ] Confirm only act4/rhs and act7/rhs changed inside Task 199.
- [ ] Confirm act4/rhs changed from `(?is)^\s*$|^%par1$` to `(?is)^\s*$|^%.*$`.
- [ ] Confirm act7/rhs changed from `(?is)^%par2$` to `(?is)^\s*$|^%.*$`.
- [ ] Confirm Task 199 retains 180 actions.
- [ ] Confirm Task 224 and Task 227 are raw-byte identical.
- [ ] Confirm every other task, Project registry, profile, and scene is identical.
- [ ] Independently model Tasker substitution for controlled, blank, unresolved, production, and invalid tokens.
- [ ] Confirm no Task 199 RHS retains dynamic `^%par1$` or `^%par2$`.
- [ ] Recheck topology, duplicate identifiers, references, call graph, one-transition limit, busy cleanup, controlled isolation, and AutoSheets fields.
- [ ] Verify credential occurrence without printing it.
- [ ] Keep phone import blocked until this exact artifact passes audit.
