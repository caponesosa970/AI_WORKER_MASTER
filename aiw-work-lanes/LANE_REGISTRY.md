# AI Worker Lane Registry

Registry status: `COORDINATION SCAFFOLD / NON-AUTHORITATIVE`

Source main last verified during preparation: `06cbf2df88ce59cb63310fa97d04906646f57d0c`

| Lane ID | Purpose | Current classification | Blocks final product? | Promotion destination |
|---|---|---|---|---|
| `MAIN_LOCKED_CORE` | Real application, accepted architecture, Gates 1-14, and promoted facts | `MAIN_LOCKED` | N/A | N/A |
| `TEST_BRAIN_ARCHIVE_ALIGNMENT` | Prove exact aligned AutoSheets Archive retrieval | `LANE_LOCKED / SECTION 12 VERIFIED` | Yes | `MAIN_LOCKED_CORE` |
| `TEST_BRAIN_CONTEXT_INTEGRATION` | Integrate Brain rules and bounded sender history into the production prompt | `BLOCKED BY EXPLICIT PRODUCTION BUILD AUTHORIZATION` | Yes | `MAIN_LOCKED_CORE` |
| `TEST_HISTORY_ORDER_QUALITY` | Prove latest-six ordering, timestamp rules, sender isolation, and history eligibility | `BLOCKED BY PRODUCTION BUILD AUTHORIZATION / ORDER PROOF PENDING` | Yes | `MAIN_LOCKED_CORE` |
| `TEST_DEADARCHIVE` | Accumulate isolated DeadArchive transaction, recovery, cleanup, and plugin evidence | `ISOLATED / DEFERRED` | No | Optional later promotion |
| `TEST_SECURITY_PRIVATE_ARTIFACTS` | Produce release derivatives without embedded credentials or private evidence | `REQUIRED BEFORE PUBLIC RELEASE` | Yes | `MAIN_LOCKED_CORE` |
| `TEST_FULL_SYSTEM_REGRESSION` | Recheck STOP, locks, recipient safety, duplicate prevention, confirmation, Archive, and recovery | `DEPENDENT` | Yes | `MAIN_LOCKED_CORE` |
| `TEST_CAPACITY` | Prove queue limits, throughput, quotas, bounded retries, and intended 50-contact reliability | `DEPENDENT` | Yes | `MAIN_LOCKED_CORE` |
| `TEST_CONTROL_INTERFACE` | Prove safe operator controls, status visibility, STOP, and recovery controls | `DEPENDENT` | Yes | `MAIN_LOCKED_CORE` |
| `TEST_LIVE_PRODUCTION` | Controlled live activation and final production proof | `FINAL DEPENDENT LANE` | Yes | `MAIN_LOCKED_CORE` |

## Isolation rule

DeadArchive is explicitly isolated and does not block completion of the final product path. Automatic DeadArchive runtime remains deferred and cleanup remains manual unless later promoted evidence changes that decision.

## Single-lane ownership

Every handoff packet belongs to exactly one lane. Cross-lane evidence must be referenced by packet ID; it must not be silently copied or inherited.

## Authority boundary

This registry is a coordination scaffold only. It is non-authoritative and cannot change Main authority, promote evidence, authorize production Brain/context work, or override the four root authority files.
