# Codex Phone Navigation Action Log - 2026-07-04

STATUS: ACTIVE OPERATING LOG

Purpose: record Moto Razr 2024, TeamViewer, Tasker, TextNow, AutoInput, and phone-proof navigation actions that work or fail so future phone testing is faster and safer.

Navigation logs are operational speed tools, not passive reports. Use this file to move faster on the phone, reuse known-good coordinates/routes, avoid failed click/search paths, and keep the needed phone screen visible for the current proof step.

Do not store or print TeamViewer session IDs, phone numbers, account identifiers, contacts, message contents, API keys, webhook URLs, or Sheet IDs in this log. Record route behavior and proof status only.

## Current Phone Context

- Device: Moto Razr 2024.
- Phone access route: TeamViewer / remote screen share when user reattaches it.
- Tasker XML import status from current project context: Build100 candidate XML was imported into Tasker.
- Current proof layer: Stage 2 dashboard STATUS proof.
- Current classification: `CANDIDATE / HOLD FOR PHONE PROOF`.

## Hard Boundaries

Do not press during Stage 2 dashboard proof:

- `START CAPPED`
- `TEST SEND 1`
- `ARCHIVE DONE 1`
- `COMPACTOR HOLD`
- `APP Start AI Worker`
- `APP Run Tick Once`
- `FINAL Queue Cycle`
- `FINAL Send Sheet`
- Any TextNow send button
- Any live/autonomous start, timer, trigger, queue-cycle, archive, compactor, deadarchive, or send path

Stage 2 is only for proving dashboard scene runtime display and the safe STATUS path.

## Worked

- TeamViewer / phone screen share can provide visible phone state for proof, but only what is actually visible on-screen counts as phone proof.
- Tasker import was completed by the user before this Stage 2 proof pass.
- Tasker `SCENES` area exposed `AIW COMMAND CENTER P82`.
- Opening `AIW COMMAND CENTER P82` in Tasker showed the dashboard scene editor.
- Screenshots of the scene editor were captured for the Stage 2 HOLD bundle.
- Static wiring from the submitted REV3 bundle confirms:
  - scene `STATUS` clickTask points to task ID `402`
  - task ID `402` is `AIW P82 CC STATUS`
  - `AIW P82 CC STATUS` performs `AIW HELPER LOCKDOWN SNAPSHOT`
  - helper runs `APP Stop AI Worker`, then `APP Status Snapshot Simple`
  - `%SnapSafe` ordering correction is valid and not a static proof bug

## Failed Or Incomplete

- Scene editor proof is not runtime dashboard proof. Pressing `STATUS` in scene edit mode would select or edit the element, not prove the runtime click path.
- Prior attempt to locate/run `AIW DASHBOARD P82` in Tasker task list did not reliably expose the row.
- Stage 2 does not pass until the dashboard appears outside Scene Edit mode and the `STATUS` button is pressed in runtime scene mode.
- No Tasker runlog proving Stage 2 STATUS runtime path has been captured yet.

## ChatGPT-Audited Next Phone Route

Proceed with Option 2 first:

1. Start screen recording.
2. In Tasker, go to `TASKS`.
3. Tap search.
4. Search `AIW P82`.
5. If needed, search `AIW DASHBOARD`.
6. Open `AIW DASHBOARD P82`.
7. Press Tasker's play/run button for that task.
8. Confirm dashboard appears outside Scene Edit mode.
9. Screenshot dashboard before pressing anything.
10. Press only `STATUS` in the runtime dashboard scene.
11. Capture the resulting popup/runlog/status proof.

Do not patch or add a helper before trying this route.

## Approved Fallback Only If Existing Task Cannot Be Exposed

If `AIW DASHBOARD P82` cannot be located/run after the audited searches, ChatGPT approved a contained helper task:

```text
Task name: TEST SHOW AIW COMMAND CENTER P82 ONLY
Action 1: Show Scene AIW COMMAND CENTER P82
Action 2: Flash/Popup "Dashboard scene shown for STATUS proof only"
```

Fallback rules:

- No live variables changed.
- No safe-mode changes.
- No phone-live hold changes.
- No send-live hold changes.
- No dry-run changes.
- No profile enable/disable.
- No timer enable/disable.
- No queue cycle.
- No TextNow UI action.
- No archive, compactor, or deadarchive.

## Fast Path Before Phone Control

1. Confirm TeamViewer is connected and showing the Moto screen.
2. Announce before taking phone control.
3. Confirm current app and screen, and remember it as the return screen.
4. If Tasker is not visible, navigate to Tasker without opening TextNow.
5. Follow the audited route exactly.
6. Record every screen/state transition here afterward:
   - route attempted
   - exact visible screen
   - action taken
   - result
   - pass/fail/hold classification
7. Stop immediately if any route exposes live send/start controls in a way that would require pressing them.
8. After phone work, return the Moto to the user's prior progress/chat screen when possible.
9. After phone work, bring Codex desktop back to the front on the PC so the user can see progress.
10. Actively track current phone screen, current PC foreground app, current proof layer, current waiting audit, and next safe phone action.

## Current State

- TeamViewer / phone screen access was reattached.
- Tasker was opened from the Moto home screen.
- Tasker `TASKS` tab was opened.
- Tasker search did not accept TeamViewer typed text cleanly. Text entered through the Android input layer but did not visibly filter Tasker results.
- The task list was manually scrolled to the P82 task block.
- `AIW DASHBOARD P82` was located and opened.
- Tasker run/play was pressed for `AIW DASHBOARD P82`.
- Runtime dashboard scene appeared outside Scene Edit mode.
- Pre-press proof screenshot saved:
  - `03_PHONE_PROOF/20260704_RUNTIME_DASHBOARD_BEFORE_STATUS_TEAMVIEWER.jpg`
  - SHA256 `052C591FAE21CEB53C2DEB2302A2767A8C89813EFF03A6B0223B04AC7FA01332`
- Only the runtime `STATUS` button was pressed.
- A bottom status popup appeared on the runtime dashboard. It visibly indicates worker/lock status.
- Post-press proof screenshot saved:
  - `03_PHONE_PROOF/20260704_RUNTIME_STATUS_AFTER_PRESS_TEAMVIEWER.jpg`
  - SHA256 `394293098F236E837049E5D0C6D6A8C2F8984D868AE9B453A667790FD140F3C4`
- No start, send, archive, compactor, queue-cycle, TextNow, timer, trigger, or live/autonomous activation control was pressed in this pass.
- Runtime proof bundle created:
  - `03_PHONE_PROOF/AIW_BUILD100_PHONE_PROOF_STAGE2_RUNTIME_STATUS_PROOF_HOLD_20260704.zip`
  - SHA256 `292765EA61AF2944BFBD087B55B8A7C469212B53C098769E6AD99D6F3E6BBCC4`
- Runtime proof bundle was attached and sent to ChatGPT Desktop project `AI WORKER`, chat `FINAL WORK`, for independent audit.
- ChatGPT audit result for runtime proof bundle:
  - `STAGE 2 PASS WITH VARIANCE`
  - Accepted for narrow dashboard/STATUS proof.
  - Still not release/locked.
  - Remaining hold: Tasker runlog missing and exact final status values not fully readable.
  - Next contained route: rerun `AIW DASHBOARD P82 -> STATUS`, wait 3-5 seconds, screenshot final status output if visible, export Tasker runlog immediately, send both back to ChatGPT.
- User corrected workflow: after phone work, return the Moto to the prior progress/chat screen and bring Codex desktop to the PC foreground.
- Restore completed after user correction:
  - Moto returned to the prior progress/chat screen.
  - Codex desktop app brought to the PC foreground.
- Navigation speed/tracking correction locked in:
  - use this log before phone clicks
  - keep the needed screen visible
  - track active phone/PC targets and pending proof/audit state
  - update what worked and failed after each phone navigation pass

## Navigation Lessons From Stage 2 Runtime Proof

- Moto Home coordinate through current TeamViewer scaling: approximate center Home button at TeamViewer window coordinate `x=494, y=506`.
- Tasker home-screen icon worked at approximate TeamViewer coordinate `x=498, y=437`.
- Tasker `TASKS` tab worked at approximate TeamViewer coordinate `x=494, y=189`.
- Tasker search icon worked at approximate TeamViewer coordinate `x=567, y=173`, but typed search did not reliably filter results through TeamViewer.
- Manual task-list dragging worked better than Tasker search for this session.
- P82 task block was reachable by scrolling downward through the task list, then slightly upward after overshooting.
- `AIW DASHBOARD P82` was located just above the visible `AIW P82 CC STATUS` / `AIW P82 CC START LIVE` / `AIW P82 CC QUEUEVIEW` block.
- Runtime `STATUS` button worked at approximate TeamViewer coordinate `x=478, y=247`.
