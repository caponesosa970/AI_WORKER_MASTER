# Validation, Promotion, and Release Engine

## Validation engine

Runs at four levels:

1. Static XML validation.
2. Runtime pre-start validation.
3. Runtime pre-action validation.
4. Release validation.

## Static XML validation

Must check:
- XML parse
- TaskerData root
- task count
- profiles
- scenes
- duplicate IDs
- duplicate names
- missing refs
- scene click refs
- plugin bundles preserved
- json true
- se true
- mojibake
- Build95 labels removed
- Build100 labels present
- private key marker present in WITH_KEY XML
- watchdog/recovery/ledger systems present

## Runtime pre-start validation

Must check:
- TextNow trigger exists
- timer profile exists
- key task exists
- sheets configured
- dashboard exists
- locks can be safely reset
- Safe Mode default sane

## Runtime pre-process validation

Must check:
- Worker ON
- not HOLD
- process lock clear
- row status NEW
- row sender/message valid
- cap not exceeded

## Runtime pre-send validation

Must check:
- send lock clear
- one-send cap available
- row READY_TO_SEND
- reply valid
- sender key valid
- not stale
- not overflow
- Safe Mode rule satisfied

## Promotion engine

CANDIDATE can become LOCKED only if:
1. Static XML audit passes.
2. Tasker import proof passes.
3. Dashboard proof passes.
4. Controlled processor proof passes.
5. Controlled send proof passes.
6. Watchdog proof passes.
7. Recovery proof passes.
8. Runlog proof passes.
9. Final status proof passes.
10. SHA inventory is recorded.

## Release controller

Release ZIP must include:
- runtime XML
- source files
- SHA report
- phone proof
- runlog
- static audit
- hold list
- known limits
- promotion decision

If any proof missing:
STATUS = HOLD
