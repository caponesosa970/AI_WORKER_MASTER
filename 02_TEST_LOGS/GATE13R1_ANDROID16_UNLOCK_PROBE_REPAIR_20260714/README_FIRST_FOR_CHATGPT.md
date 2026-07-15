# Gate 13R1 Android 16 Unlock-Probe Repair

Status: `CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT`

This candidate repairs only the false keyguard HOLD observed on the phone. The Gate 13 base used `%KEYG`, but direct phone proof showed `%KEYG` was not a reliable current-unlocked signal on the Moto Razr 2024 / Android 16 runtime.

Runtime scope:

- Task 130: insert one call to `FINAL Device Unlock Probe`; replace only its `%KEYG != off` guard with `%AIWUnlockProbeResult != UNLOCKED`.
- Task 224: same scoped call and guard replacement.
- Task 228: same scoped call and guard replacement.
- Task 230: new `FINAL Device Unlock Probe` using Android `KeyguardManager` Java Function calls.
- Project task registry: add Task 230.

No phone import is approved. Tasker was not run. No profile was enabled. No live Sheet cell was changed. Gate 13 remains HOLD at `12/14 locked = 86%`.

Independent static results:

- direct XML/package validator: PASS (`34/34`);
- unlock-probe state model: PASS (`16/16` required cases and `10/10` added control-flow checks);
- repository Tasker static audit: PASS;
- topology: `82 tasks / 4 profiles / 1 scene`;
- profiles enabled in export: `0`.

The same controlled busy-timer phone test is still required after ChatGPT audits the actual XML and ZIP.
