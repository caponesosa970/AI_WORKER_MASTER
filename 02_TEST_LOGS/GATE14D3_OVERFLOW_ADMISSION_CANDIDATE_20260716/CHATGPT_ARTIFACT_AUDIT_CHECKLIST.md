# ChatGPT Artifact Audit Checklist

- [ ] Verify base SHA256.
- [ ] Verify standalone XML SHA256 and byte size.
- [ ] Verify ZIP SHA256 and byte size.
- [ ] Verify sidecar SHA256 and recorded values.
- [ ] Verify ZIP has one XML byte-identical to standalone XML.
- [ ] Parse `TaskerData`; verify 95 tasks / 4 disabled profiles / 1 scene.
- [ ] Verify two added tasks only and 93/93 existing task blocks identical.
- [ ] Verify admission calls unchanged count-50 batch and cannot process row 199.
- [ ] Verify row-199 before/after readback in admission mode.
- [ ] Verify deferred mode binds only row 199.
- [ ] Verify authorization is consumed before processing.
- [ ] Verify no TextNow, Send, confirmation, DONE, Archive, profile, timer, or live path.
- [ ] Verify owned-lock cleanup and no unowned-lock release.
- [ ] Verify public branch contains no private package, secret, raw runlog, phone number, or Drive link.
- [ ] Keep status HOLD until direct Sosa phone proof.
