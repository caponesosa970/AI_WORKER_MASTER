# Exact Java Function Fields

New task: Task 230, `FINAL Device Unlock Probe`

Java Function 1:

- Return: `(KeyguardManager) kgm`
- Class or object: `CONTEXT`
- Function: `getSystemService\n{Object} (String)`
- Parameter 1: `keyguard`
- Continue Task After Error: ON (`<se>false</se>`)

Java Function 2:

- Return: `%AIWUnlockDeviceLocked`
- Class or object: `kgm`
- Function: `isDeviceLocked\n{boolean} ()`
- Continue Task After Error: ON (`<se>false</se>`)

Java Function 3:

- Return: `%AIWUnlockKeyguardLocked`
- Class or object: `kgm`
- Function: `isKeyguardLocked\n{boolean} ()`
- Continue Task After Error: ON (`<se>false</se>`)

Decision contract:

- `UNLOCKED` only when both returned values are explicitly `false`.
- `LOCKED` when either validated value is `true`.
- `HOLD` on Java error, null manager, blank value, unresolved literal, unsupported call, or any other ambiguous value.

The helper has no Perform Task call, Sheet plugin, TextNow action, profile action, transaction-lock write, or lifecycle-module call.
