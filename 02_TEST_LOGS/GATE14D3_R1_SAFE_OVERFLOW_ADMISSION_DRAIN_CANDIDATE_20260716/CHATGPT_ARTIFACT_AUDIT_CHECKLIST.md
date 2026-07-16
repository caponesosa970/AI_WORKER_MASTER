# ChatGPT Artifact Audit Checklist

- [ ] Verify exact Gate 14D2 base SHA.
- [ ] Verify original Gate 14D3 package is classified rejected/diagnostic only.
- [ ] Verify XML, ZIP, and sidecar hashes and byte sizes.
- [ ] Verify ZIP contains one byte-identical XML.
- [ ] Parse 95 tasks / 4 disabled profiles / 1 scene.
- [ ] Verify only four existing overflow/admission tasks changed and two tasks were added.
- [ ] Verify `FINAL Simple`, `FINAL Queue Cycle`, processing/API, TextNow, Send, confirmation, Archive, timer, profiles, and scene are unchanged.
- [ ] Verify existing production logger and drain-cap call graph reaches the new engine through repaired wrappers.
- [ ] Verify cross-store exact-ID scan before admission and exact uniqueness after admission.
- [ ] Verify main-row readback precedes source DRAINED write.
- [ ] Verify exact DRAINED readback precedes success.
- [ ] Verify partial recovery skips the main write.
- [ ] Verify completed rerun performs zero writes.
- [ ] Verify shared lock ownership and guarded release.
- [ ] Verify no API/TextNow/lifecycle path in engine or launcher.
- [ ] Keep import and phone test on HOLD until the exact artifact is approved.
