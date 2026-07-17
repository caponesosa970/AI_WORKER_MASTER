# AI Worker Mandatory Build Preflight

Status: ACTIVE PREFLIGHT GATE
Updated: 2026-07-12T17:43:24-07:00

This preflight must run before every AI Worker Codex task. If any required item is unknown, Codex must stop and report HOLD.

## Required Preflight

1. Confirm current working directory and active branch.
2. Read `AGENTS.md`.
3. Read `.codex/config.toml`.
4. Read `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`.
5. Read `AIW_BUILD_ACCOUNTABILITY_LEDGER_CURRENT.md`.
6. Read `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`.
7. Read `AIW_CLAIM_TO_PROOF_MATRIX_CURRENT.md`.
8. Identify current tracker, gate, active blockers, and proof percentage.
9. Identify the exact source truth and source SHA256.
10. Confirm exact base file/package.
11. Confirm exact task scope.
12. Confirm prohibited paths.
13. Confirm patch size limit.
14. Declare required proof.
15. Declare expected return format.
16. Search relevant prior failures and list them.
17. Load prevention rules tied to those failures.
18. Declare phone-proof limitations.
19. Declare tracker effect.
20. Stop if source proof, gate approval, or phone-proof boundary is unclear.

## Required Failure Search Terms

Search current files and relevant git history for:

- false pass
- malformed
- wrong source
- invented AutoInput
- SEARCH_ICON
- menu_search
- Structure Output
- phone proof supersedes
- static audit passed but phone failed
- duplicate
- wrong row
- lock release
- Send failure

## Required Preflight Output

Every task must include a preflight report with:

- current tracker read
- current gate read
- active blockers read
- relevant prior failures searched
- source truth identified
- source SHA verified
- exact base confirmed
- exact task scope confirmed
- prohibited paths confirmed
- patch size confirmed
- required proof declared
- expected return format declared
- previous related failures listed
- prevention rules loaded
- phone-proof limitations declared
- Codex responsibility statement
- ChatGPT verification checklist

## Whole-Application Compatibility Preflight

Before any runtime build, repair, artifact approval, phone-test request, tracker decision, or release claim, Codex must identify:

- current full-project baseline SHA256
- active capability boundary
- local defect
- upstream contracts
- downstream contracts
- changed nodes
- protected nodes
- complete reachable call graph
- state-transition impact
- lock impact
- STOP and recovery impact
- cross-application regression plan
- exact phone-proof boundary
- current synchronized ledger sections covering the active build

The compatibility map must cover the entire AI Worker application and release path: TextNow ingress, exact Sheet logging, row binding, message identifiers, timestamps, ordering, processing, OpenAI reply generation, queue selection, correct-thread navigation, compose safety, Send zero-or-one, independent confirmation, DONE, exact-row Archive, recovery, STOP, timer/live controls, interface, capacity, and release.

Minimal runtime scope does not reduce the required full-application compatibility proof. A local static PASS cannot prove full-application compatibility. A generated report, CSV, simulator, mutation tool, pinned prompt, or package cannot prove its own correctness.

### Current Gate 14 System-Wide Accountability Hard Stop

When `ISSUE_APP_WIDE_ACCOUNTABILITY_DRIFT_GATE14` is open, Codex must treat Gate 14 runtime work and phone execution as `HARD HOLD`.

The active tracker remains `13/14 locked = 93%`. Gates 1-13 remain locked. Gate 14 remains blocked. Phone proof is not claimed, phone import is not approved, tracker effect is NONE, and runtime work may resume only after the synchronized accountability records cover the active build.

Blocked while this issue is open: runtime XML repair, private package modification, Datasource R1 continuation, Tasker import, Tasker execution, TextNow action, live or staging Sheet read/mutation, Send, confirmation, DONE, Archive, DeadArchive, Compactor, TT5, live operation, capacity execution, interface execution, profile activation, Gate 14 release, merge, and production release.

Required full-app compatibility output fields:

- issue ID
- tracker before and after
- active gate
- full-project baseline filename and SHA256
- final product capability advanced
- exact local behavior repaired
- upstream producer and contract map
- downstream consumer and contract map
- exact changed files, tasks, actions, fields, profiles, scenes, task registry nodes, variables, and call references
- exact protected nodes and preservation proof level
- complete reachable call graph from every relevant entry point through every possible terminal outcome
- state-transition impact map
- exact-row and message ownership impact
- lock acquisition, release, stale recovery, retry, interruption, restart, and unresolved transaction impact
- STOP and recovery impact
- cross-application regression plan and actual result
- forbidden-path proof
- expected phone-proof boundary
- synchronized ledger references
- unsupported claims
- ChatGPT verification checklist

## Hard Stop Conditions

Codex must stop if:

- source truth is missing
- source SHA cannot be verified
- branch/source state is unclear
- task scope would touch runtime without approval
- AutoInput target is guessed
- a helper contract is unknown
- prior related failures are not checked
- the claim-to-proof matrix cannot support a requested claim
- phone proof would be needed but is not available
- ChatGPT has not approved the current gate
- accountability records are stale
- claim matrices are gate-only and do not cover the complete application
- upstream or downstream impact is missing
- protected-node map is incomplete
- reachable call graph is incomplete
- state-transition analysis is incomplete
- a local-to-full-application compatibility claim is unsupported
- a runtime task lacks an accountability entry for the active build
- expected results or tests were weakened
- a local PASS could conceal an application-level regression

## AutoInput Preservation Preflight

Before any TextNow/AutoInput work, Codex must prove:

- source XML action exists
- output XML action exists
- every required AutoInput field has source value and output value
- Structure Output state is explicitly shown
- Continue Task After Error state is explicitly shown
- target type and target value are explicitly shown
- waits and `%err/%errmsg` checks are explicitly shown
- failure routing is explicitly shown
- second independent parser/check was run
- phone-visible proof required is listed

If any field is missing, the preservation claim is HOLD.
