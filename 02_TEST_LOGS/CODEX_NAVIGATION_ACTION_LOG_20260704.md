# Codex Navigation Action Log - 2026-07-04

STATUS: ACTIVE OPERATING LOG

Purpose: record Windows, ChatGPT Desktop, file-picker, and phone-screen navigation actions that worked or failed so the next automation pass is faster and less error-prone.

Navigation logs are operational speed tools, not passive reports. Read them before screen work, reuse known-good routes/coordinates, avoid repeating failed paths, and keep the needed work surface visible.

## Current Targets

- ChatGPT desktop target: `AI WORKER - FINAL WORK`
- AI Worker workspace: `C:\Users\Shadow\Documents\ai work\AI_WORKER_MASTER`
- Stage 2 ZIP used for audit handoff: `AIW_BUILD100_PHONE_PROOF_STAGE2_DASHBOARD_STATUS_HOLD_REV3_20260704.zip`
- Phone screen access: TeamViewer / remote screen share will be reattached by user when phone proof is needed.
- Phone-specific navigation log: `CODEX_PHONE_NAVIGATION_ACTION_LOG_20260704.md`

## Rules Before Any UI Action

1. Confirm the target app and visible window before input.
2. Do not type or click if the visible screenshot is Codex when the intended target is ChatGPT.
3. For ChatGPT work, verify both:
   - window title includes `AI WORKER - FINAL WORK`
   - screenshot or accessibility tree is visibly ChatGPT, not Codex
4. Use the ChatGPT desktop app for `AI WORKER / FINAL WORK`, not a browser, unless the user changes that route.
5. Do not automate the Codex desktop UI with Windows input.
6. Before phone actions, announce that Moto screen control is about to start and avoid live/send/start paths unless explicitly approved by the current proof step.
7. After phone actions, return the Moto to the prior progress/chat screen when possible, then bring Codex desktop back to the PC foreground so the user can see progress.
8. Actively track the current target app/window, visible phone screen, pending audit/build/proof task, and next safe action. If the visible screen drifts from the work target, restore the needed screen before continuing.

## Worked

- ChatGPT Desktop opened correctly to project `AI WORKER` and chat `FINAL WORK`.
- The file attachment succeeded after using keyboard focus inside the Windows Open dialog:
  - press file-name access key
  - type the full ZIP path
  - press Enter
- The attached REV3 ZIP appeared in the ChatGPT composer as a ZIP archive chip.
- Typing the Stage 2 audit handoff into the visible composer worked after the ZIP chip was present.
- Sending worked by clicking the visible send button after both attachment and prompt were present.
- Local SHA verification worked and confirmed master ZIP and Downloads copy match:
  - `D56B61FA26E0130C38C2373A50F6FEABD16698277FCBE77A3AFE11279F20E13D`

## Failed Or Slow

- Native Windows Open dialog did not appear as its own targetable window through the automation window list.
- File dialog controls were visible in accessibility but direct element clicking failed because the controls extended outside the captured ChatGPT window bounds.
- Direct `set_value` on the file-name edit was rejected because the element was not settable through that route.
- Repeated mouse-coordinate attempts against the file picker were unreliable and should not be repeated as the first choice.
- Polling screenshots became ambiguous once the visible screenshot showed Codex content while the intended target was ChatGPT. Treat this as a target-verification failure until reselected.
- Long accessibility trees from ChatGPT history are noisy. Filter narrowly and prefer visible composer coordinates after confirming the correct app/window.
- PowerShell window-inspection scripts must not use `$PID` as a variable name because it is reserved and will corrupt process attribution. Use `$procId`.

## Updated Fast Path

1. Find ChatGPT using the app/window list, not by guessing coordinates.
2. Activate `AI WORKER - FINAL WORK`.
3. Take a screenshot and accessibility snapshot.
4. If screenshot does not visibly show ChatGPT, stop UI input and reselect the target.
5. For attachments:
   - open attach picker
   - use keyboard file-name route with the full path
   - verify ZIP chip appears
6. For prompts:
   - click the visible composer area
   - enter or paste the prepared prompt
   - verify the first line and attachment are visible
   - send once
7. For ChatGPT waiting:
   - poll every 30 seconds
   - if the screenshot drifts to Codex, stop polling through that handle and reacquire ChatGPT
   - verify OS process/title if visual state and target handle disagree
8. For phone proof:
   - use TeamViewer only after user reattaches it
   - read `CODEX_PHONE_NAVIGATION_ACTION_LOG_20260704.md` before phone input
   - do not press Tasker START/SEND/live buttons unless the current audited proof step explicitly calls for it

## Current State

- REV3 Stage 2 ZIP was attached and sent to ChatGPT desktop `AI WORKER - FINAL WORK`.
- ChatGPT audit was still processing when this log entry was created.
- No additional phone or Tasker runtime action has been taken after sending the audit bundle.
- Later correction locked in memory and logs: after any phone work, restore the Moto to the prior progress/chat screen and bring Codex desktop to the PC foreground.
- Later correction locked in memory and logs: navigation logs are used to increase screen-navigation speed, click accuracy, visible-work continuity, and active tracking of current work.
