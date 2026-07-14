# ChatGPT Full Artifact Audit Checklist

- Download the actual standalone XML, ZIP, and SHA sidecar.
- Recalculate both hashes.
- Confirm ZIP has exactly one byte-identical XML.
- Parse TaskerData and verify 81 tasks, 4 profiles, 1 scene.
- Independently compare protected Tasks 71/199/223/225/226/227 against Gate 12R1.
- Inspect every changed task and both new tasks.
- Verify all four profiles are disabled in the artifact.
- Verify boot profiles call Safe Recovery, not Reset Locks.
- Verify Start calls recovery first and enables only trigger plus timer after safe result.
- Verify Stop disables profiles before state changes and never clears transaction locks.
- Verify Task 228 calls Queue Cycle once maximum and no lifecycle module directly.
- Verify Task 229 requires stale timestamps plus queue evidence before any release.
- Verify SENDING never returns to READY_TO_SEND.
- Verify confirmation/Archive recovery calls at most one module.
- Verify watchdogs no longer release locks or mutate rows.
- Verify credential occurrence is unchanged without printing it.
- Verify no private artifact or private value is in the public diff.
- Treat all Android scheduling and runtime behavior as HOLD pending phone proof.
