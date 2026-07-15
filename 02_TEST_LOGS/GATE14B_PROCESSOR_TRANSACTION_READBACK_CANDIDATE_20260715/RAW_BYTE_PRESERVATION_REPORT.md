# Raw-Byte Preservation Report

- Source existing tasks: 84.
- Authorized changed existing tasks: 166, 172, 173.
- Protected existing tasks: 81.
- Protected raw-node equality: 81/81 PASS.
- Task 69 raw-node equality: PASS.
- Task 232 raw-node equality: PASS.
- Profiles raw equality: 4/4 PASS; all remain disabled.
- Scene raw equality: PASS.
- Project change: register IDs 233 and 234 exactly once.

Reproducible raw SHA256 values from the exact full-project source/output:

- Task 69: `0FBC6730D2891E86689AA1C82EDC2C1C391F44EE9F3935A8A30D3E196A029525`
- Task 232: `3A0CAFA8640E716B6EBBA1F0988925CB1D97A46E251D31A608B34DAF2F39CC75`

The per-task hashes supplied in the build instruction do not equal raw task-node bytes or the tested XML canonicalizations. The full-project source SHA matches exactly, and direct extracted raw-node equality is the preservation authority used here. ChatGPT should independently inspect this normalization discrepancy during artifact audit.
