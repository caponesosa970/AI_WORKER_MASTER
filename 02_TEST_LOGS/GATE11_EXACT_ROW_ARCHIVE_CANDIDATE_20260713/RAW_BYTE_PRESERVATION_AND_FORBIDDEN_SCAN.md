# Raw-Byte Preservation And Forbidden Scan

## Preservation

- Protected Tasks 71, 75, 199, 223, and 225: raw-byte identical to Gate 10 base.
- Task 71 node SHA256 in base/output: `8E54D94CACA5E2B954E61D3F570B346E0926536A74E5A26D02F27BEAD6BECA91`.
- Task 75 node SHA256 in base/output: `01C8D8AA1D57ACEFFB0844BD2B290FBD3460DFE7A50ACC85AEE090637F8A726F`.
- Task 199 node SHA256 in base/output: `42F3996DA85567FC0EC8B09AE38CF6978393415522196078EB0AC055BF1613A7`.
- Task 223 node SHA256 in base/output: `94B2B2CEB2A83BE56C43B41BF7AD8437DF5FCA1E50A8486CE7E5FA05E6C44733`.
- Task 225 node SHA256 in base/output: `D8897EE0D3220AD2B6FFC83D1BF04A9B726FBCF0C2B867ACCE63BBACE1C17A30`.
- New Task 226 node SHA256: `F272D043C6CE0284890FDDC6D1728D05AC89B7489FFAFA47F481AD4A11EAA7FD`.
- Every other pre-existing task except Task 224: raw-byte identical.
- Profiles: unchanged.
- Scene: unchanged.
- Project task registry: only Task 226 added.
- Current credential value and occurrence count: unchanged without printing the value.

## Forbidden Path Scan

- Calls to `FINAL Archive Done Rows`: 0 in Tasks 224/226
- QueueView broad selection: 0 in Tasks 224/226
- GROUPED eligibility: 0
- TextNow / AutoInput / keyboard: 0
- Send actions or Send-task calls: 0
- Confirmation actions or calls: 0
- READY_TO_SEND / SENDING writes: 0
- DeadArchive / Compactor / HTTP / OpenAI: 0
- Profile enablement / live / timer: 0
- Changes to Tasks 75 or 199: 0
- New broad Archive integration: 0
- New incoming calls to Task 226 beyond Task 224: 0
- Private credential or private runtime XML in public output: 0

## Encoding And Structure

- Mojibake marker count: 0
- XML parse: PASS
- `json:true`: 0
- `<se>true</se>`: 0
- AutoSheets `<se>false</se>`: 20/20 in Task 226
