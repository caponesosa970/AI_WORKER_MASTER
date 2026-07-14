# Environment Safety and Limitations

Source-proven runtime checks used:

- `%SCREEN` must equal `on`.
- `%KEYG` must equal `off`.

No exact exported source was available for reliable automatic detection of fold state, AutoInput accessibility state, TextNow availability, or Android battery/background restrictions. The candidate therefore requires the explicit global readiness latch `%AIWGate13EnvironmentReady=1` before Start or the controlled timer launcher can arm.

This latch is not set automatically by the launcher. It must be armed only after the future ChatGPT-controlled phone test visibly verifies the environment.

Unsupported claims:

- Screen-off operation: not proven and blocked.
- Locked-screen operation: blocked.
- Folded-state automation: not automatically detected or proven.
- Background/battery-restricted reliability: not automatically detected or proven.
- AutoInput accessibility continuity: requires phone verification.
- One-shot launcher result is asynchronous and appears in `%AIWGate13TestResult` after the scheduled tick.
