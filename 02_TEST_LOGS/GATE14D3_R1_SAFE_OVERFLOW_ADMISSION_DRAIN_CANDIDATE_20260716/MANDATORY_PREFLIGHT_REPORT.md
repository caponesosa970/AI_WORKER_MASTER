# Mandatory Preflight

- Exact base SHA256: `3851E073BE042F80068E52CF7E3D410ED3D0EBA8A63C5F4C10108532912FE0EA`.
- Base topology: 93 tasks / 4 disabled profiles / 1 scene.
- Current branch start: `262df72253af71d7533061ea701655a545834e97`.
- Unused new task identities: verified.
- Required controller/accountability files: read.
- Exact production source audited: logger, slot selector/recycler, pending check, overflow logger, drain cap, drain one, Queue Cycle, lock cleanup, and duplicate guard.
- Allowed runtime scope: four overflow/admission-specific existing tasks plus one permanent engine and one isolated launcher.
- Forbidden processing, API, TextNow, lifecycle, timer, and profile changes: honored.
