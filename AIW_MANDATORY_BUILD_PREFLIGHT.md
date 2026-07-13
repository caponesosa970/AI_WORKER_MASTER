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
