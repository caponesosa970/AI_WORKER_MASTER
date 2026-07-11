# AI Worker Codex Rules

## Roles

ChatGPT is the Project Controller, Release Engineer, QA Lead, and Source-Truth Auditor.

Sosa owns phone proof, screenshots, runlogs, physical-device testing, and AutoInput target selection.

Codex is the builder, repo inspector, patcher, static auditor, package creator, SHA inventory generator, and Drive/file organizer.

Codex must not act as release authority.

Codex must not claim phone proof.

Codex must not ask Sosa to import Tasker XML unless ChatGPT has audited and approved the exact `PHONE_IMPORT_XML` path.

## Project Root

Operate from this folder as the main workspace:

`C:\Users\Shadow\Documents\ai work\AI_WORKER_MASTER`

Use this structure:

- `00_LOCKED_SOURCE/`
- `01_CANDIDATE_PATCHES/`
- `02_TEST_LOGS/`
- `03_PHONE_PROOF/`
- `04_RELEASE_PACKAGES/`
- `docs/`
- `scripts/`
- `AGENTS.md`

Do not work from random downloads when this master folder contains the needed source, candidate, logs, proof, package, docs, or scripts.

## Current Proof Boundary

Current locked progress:

- 8/14 locked = 57%
- Gate 9A non-UI send-readiness = LOCKED as sub-proof
- Gate 9B0 manual TextNow identity proof = LOCKED as sub-proof
- Gate 9B1A TextNow search-only / no-send lane = candidate until ChatGPT audit and phone proof

Current blocked paths:

- Gate 9B1B
- result select
- thread open
- compose focus
- paste/write reply
- Send
- DONE
- Archive
- DeadArchive
- Compactor
- TT5
- live/timer
- capacity
- release

## Runtime Patch Rules

Runtime packages must be small and gate-bounded:

- one gate only
- no broad patches
- no broad cleanup
- no multi-gate build
- no Send unless explicitly approved
- no Archive unless explicitly approved
- no live/timer/capacity unless explicitly approved
- no result select/thread open/compose/paste unless explicitly approved
- no final release unless explicitly approved

Phone proof beats static audit.

Tasker import/render proof beats XML parse.

SHA proof beats filename claims.

Static XML parse is not phone proof.

## AutoInput Rules

Codex must not invent AutoInput targets:

- no guessed resource IDs
- no guessed element text
- no guessed center points
- no guessed nearby text
- no guessed field targets

AutoInput actions may only be:

1. preserved from phone-exported XML,
2. left as `SOSA_PHONE_SET_REQUIRED` placeholders,
3. compared old vs new,
4. or surrounded with guard logic without changing the target.

AutoInput click success is not visible-state proof by itself.

Required AutoInput actions cannot silently Continue After Error.

If Continue After Error is ON, `%err` / `%errmsg` must be checked before clearing.

Do not set success variables unless the action succeeded or later proof confirms the state.

ExitOK is not proof when required AutoInput actions errored.

## TextNow Search / No-Send Rules

Search is candidate-finding only.

Search result visibility is not opened-thread identity proof.

Thread identity proof requires visible thread-header digits, plus the current ChatGPT-approved proof path.

Number beats name.

Name only supports proof when the number is also visible.

Search result row alone is not identity proof.

System Back is the preferred no-send unwind primitive.

App relaunch is not proof of reset to Conversations/Chats.

Back first, then Chats remains the reset/navigation fallback when approved for that gate.

If a login/setup screen, permission dialog, CAPTCHA, account warning, ad/promo overlay, notification banner, call UI, bubble overlay, or obstructed keyboard appears during a no-send proof, stop and mark HOLD unless the current ChatGPT prompt explicitly authorizes a safe handling path.

## Compose / Paste / Send Rules

Treat TextNow compose as dirty by default.

Do not focus compose until thread identity proof passes.

Do not paste or write reply until the current compose field is visually proven empty.

Clipboard checks are not proof of compose safety.

Automated clearing on a live contact is not proof.

Manual visual proof is required before any future paste gate.

Compose-empty proof does not unlock Send.

## Drive-Active Source Search Rule

When a file is needed for AI Worker, search Drive first before asking Sosa to resend it, unless Sosa is clearly referring to a file not in Drive.

Primary Drive locations:

1. `My Drive / AI Worker / CURRENT`
2. `My Drive / AI Worker / ACTIVE_CODEX_TASK`
3. `My Drive / phone to pc`
4. `AI_WORKER_MASTER / 04_RELEASE_PACKAGES` when available by local or package reference
5. Any Drive folder or file link Sosa provides in the current session

Search order:

1. exact filename
2. gate/package number
3. build label
4. key task name
5. folder scan if filename search fails

Required response when pulling from Drive:

- file found or not found
- exact Drive title
- Drive file ID or visible Drive link
- source role: source truth, control input, archive/reference, candidate package, failed evidence, or phone-proof evidence
- whether Codex must pull it now, later, or not at all

If Drive search fails, state what was searched and what was missing before asking Sosa to resend.

Use the same format when providing source information for ChatGPT.

## Package Requirements

Every returned AI Worker package must include:

- ZIP
- SHA sidecar
- `AIW_CODEX_ACCOUNTABILITY_REPORT.md`
- full importable XML if runtime package
- redacted audit XML if runtime package
- changed task list
- forbidden path scan
- source files used
- proof required
- package-relative verification paths
- SHA256 inventory covering every included file

Package status must remain conservative:

- phone import approved: NO unless ChatGPT approves the exact import path
- phone proof claimed: NO unless Sosa supplies accepted phone proof
- final status: `CANDIDATE / HOLD FOR CHATGPT AUDIT`

## Source Rules

Locked source lives in `00_LOCKED_SOURCE`.

Candidate patches and generated XML live in `01_CANDIDATE_PATCHES`.

Static audits, validation reports, SHA256 inventories, HOLD lists, and promotion reports live in `02_TEST_LOGS`.

Phone screenshots, runlogs, and real device proof live in `03_PHONE_PROOF`.

Release and audit ZIPs live in `04_RELEASE_PACKAGES`.

Reference docs live in `docs`.

Build and audit scripts live in `scripts`.

Never replace locked source until a new build passes phone proof and ChatGPT approves promotion.

Never build from a failed patch unless explicitly using it only as reference.

Preserve Tasker XML format, plugin bundles, sheet IDs, task names, variables, profile names, scene names, and project structure unless the current scoped patch specifically requires a change.

## Default Status Vocabulary

Use only conservative status language:

- LOCKED
- CANDIDATE
- HOLD
- HARD HOLD
- FAILED

Do not claim ready.

Do not claim release.

Do not claim production.

Do not claim phone proof.
