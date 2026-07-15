# ChatGPT Artifact Audit Checklist

- [ ] Download the standalone XML, ZIP, and SHA sidecar from their separate Drive links.
- [ ] Recalculate both hashes.
- [ ] Confirm the ZIP contains exactly one byte-identical XML.
- [ ] Confirm topology is 82 tasks, 4 profiles, 1 scene.
- [ ] Confirm all profiles are disabled.
- [ ] Confirm Task 230 was added and is called only by Tasks 130, 224, and 228.
- [ ] Inspect all three Java Function action fields directly.
- [ ] Confirm all three Java actions have `<se>false</se>`.
- [ ] Confirm `UNLOCKED` requires both exact false values.
- [ ] Confirm errors, null, blanks, unresolved literals, and ambiguity route to HOLD.
- [ ] Confirm each caller preserves its existing HOLD result.
- [ ] Confirm `%KEYG` is absent from Tasks 130, 224, and 228.
- [ ] Confirm protected Tasks 71, 199, 223, 225, 226, 227, and 229 are byte-identical.
- [ ] Confirm no credential changed without printing it.
- [ ] Confirm no private artifact is present in the public diff.
- [ ] Confirm Gate 13 remains HOLD and no phone import instruction is issued from Codex's report alone.
