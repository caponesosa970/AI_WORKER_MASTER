# ChatGPT Artifact Audit Checklist

- [ ] Base SHA matches `72D5F636AE72F441ACD2BF1C0C9B5B93FFF8503775FA3CA05C59A9111389CDE4`.
- [ ] XML/ZIP/sidecar hashes and sizes match the report.
- [ ] ZIP contains exactly the standalone XML bytes.
- [ ] Topology is 93 tasks / 4 disabled profiles / 1 scene.
- [ ] Exactly the two named tasks were added.
- [ ] All 91 existing tasks are raw-byte identical.
- [ ] `FINAL Simple` still calls TT5 once.
- [ ] TT5 exact-ID equality remains active and unchanged.
- [ ] Historical fingerprint/age actions remain disabled and unchanged.
- [ ] Ordering mode is hard-bounded to rows 199-201.
- [ ] Rows 199 and 201 use the same message and distinct IDs.
- [ ] Duplicate mode reaches only TT5 twice and has zero API/lock/write calls.
- [ ] Authorization, modes, globals, locks, profiles, and control stacks validate.
- [ ] Both independent validators and Tasker static audit pass.
- [ ] No private runtime, credential, Sheet value, Drive ID, phone value, or raw runlog is committed.
- [ ] Status remains candidate/HOLD; PR #9 remains unmerged.
