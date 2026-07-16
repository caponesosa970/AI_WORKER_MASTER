# ChatGPT Artifact Audit Checklist

- [ ] Base SHA is exactly `A7C577E6929E930938F0D48937332D19F441D2C1FFD9821E7047E397ECE74C07`.
- [ ] XML SHA, ZIP SHA, sidecar SHA, and sizes match the public hash report.
- [ ] ZIP contains exactly the standalone XML bytes.
- [ ] Topology is 91 tasks / 4 disabled profiles / 1 scene.
- [ ] Only Task 238 changed.
- [ ] Task 238 actions are 389 -> 399.
- [ ] Five indexed-array clears immediately precede each Get Data action.
- [ ] Task 239 and all other 90 tasks are raw-byte identical.
- [ ] Profiles, scene, project registry, and credential are unchanged.
- [ ] Two-row stale-bleed simulation passes and real nonblank Reply remains nonblank.
- [ ] Both independent validators pass.
- [ ] No Sheet/Tasker/TextNow/OpenAI action was run by Codex.
- [ ] No private artifact, phone data, raw runlog, credential, or Drive address is committed.
- [ ] Status remains candidate/HOLD; tracker remains 13/14.
