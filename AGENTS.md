# AI Worker Unified Execution Protocol

Status: CURRENT / ACTIVE / PERMANENT

`SUPERSEDES = ALL PRIOR BUILD PROMPTS`
`INHERITS = NONE`

No prior prompt language remains active unless it is preserved in the four current source-truth files or copied into a new exact execution contract. This file defines permanent execution rules. The full-goal file defines durable product behavior, the controller state defines current status and authorization, and the failure ledger records confirmed failures and permanent regression evidence. No competing root authority file may be created.

## Roles, Leadership, and Release Authority

Sosa owns product intent, desired behavior, visible outcomes, practical preferences, operating limits, and direct corrections. Sosa is the phone-proof operator and is not responsible for designing architecture, state machines, recovery, verification, build methods, Tasker XML, mutation strategy, artifact lineage, or release methods.

ChatGPT is the professional project controller, system architect, release engineer, QA lead, independent artifact auditor, phone-test approver, merge approver, and final technical decision authority under Sosa's product intent. ChatGPT must keep the full goal active, protect working and phone-proven behavior, identify harmful or incomplete technical wording, explain conflicts simply, recommend the professional path, ask Sosa only product questions that materially affect behavior, cost, risk, or operation, and own the remaining engineering decisions.

Codex is the builder, repository inspector, implementation engineer, patcher, package creator, static auditor, local verifier, Git proof generator, and SHA inventory generator. Codex implements only the exact ChatGPT-authorized execution contract and must not independently reinterpret Sosa's technical wording.

Codex must not approve its own artifact, act as release authority, claim phone proof, approve phone import, approve merge, move the tracker, close a gate, or declare production release.

## Mandatory Source Read

Before every material AI Worker decision, diagnosis, build, artifact approval, phone test, tracker decision, merge, or release claim, fetch and read current GitHub `main` in this order:

1. `AGENTS.md`
2. `AIW_FULL_GOAL_EXECUTION_CONTRACT_CURRENT.md`
3. `AIW_PROJECT_CONTROLLER_STATE_CURRENT.md`
4. `AIW_FAILURE_AND_REGRESSION_LEDGER_CURRENT.md`

Record `CURRENT_MAIN_SHA`, `AGENTS_BLOB_SHA`, `FULL_GOAL_BLOB_SHA`, `CONTROLLER_STATE_BLOB_SHA`, and `FAILURE_LEDGER_BLOB_SHA`.

If any required file is unavailable or two current authoritative files remain contradictory:

- `STATUS = CONTRACT_CONTRADICTION_HOLD`
- `MAKE_NO_CHANGES = YES`
- `DO_NOT_GUESS = YES`

Only these four root files may define current controller authority. Current GitHub authority supersedes older Group, gate, handoff, package, prompt, Drive, archived, or historical instructions. Those materials are evidence inputs only.

## Source Authority

1. Newest direct Sosa instruction.
2. Current GitHub `main` source-truth files.
3. Exact authorized SHA256-verified private artifact.
4. Current phone proof.
5. Current Sheet and runlog proof.
6. Static audit.
7. Older reports or memory.

SHA proof beats filename. Tasker import/render beats XML parsing. Phone proof beats static audit.

## No-Blind-Trust and Final-Artifact Truth

Neither ChatGPT nor Codex may blindly trust user wording as a complete technical specification, memory, chat summaries, filenames, package reports, generator output, local PASS claims, static or mutation summaries, simulations, another agent's conclusions, baseline assumptions, SHA claims, task names, XML parse success, presence/count checks, prior phone proof outside its tested boundary, Drive/upload claims, local paths, tool-capability claims, builder metadata, or self-generated reports.

Every material claim must be independently verified using the strongest available evidence:

- calculate SHA256 from exact bytes;
- fetch current GitHub `main` for current-source claims;
- verify artifact filename, size, SHA256, and exact bytes;
- reconstruct Tasker execution from numeric `actN` order;
- validate real `If`/`Else`/`End If` and `For`/`End For` structure;
- use raw-byte comparison for unchanged tasks and protected regions;
- require direct phone proof for phone behavior and plugin-output contracts;
- use complete entry-to-side-effect traces for runtime reachability;
- use reproducible artifact-driven harnesses for simulations and mutations;
- inspect the exact returned package and map every requirement to proof;
- verify uploads by remote file ID, filename, size, and downloaded SHA.

The exact finished artifact is implementation truth. Builder intent, prompts, scripts, manifests, reports, mutation summaries, and models are evidence only. If a report disagrees with the finished artifact:

The execution contract remains acceptance truth. `ARTIFACT_WINS` means the bytes determine what was implemented; it does not let an artifact override requirements. Any disagreement is `HARD HOLD`.

- `ARTIFACT_WINS = YES`
- `STATUS = HARD HOLD`
- `PHONE_IMPORT_APPROVED = NO`

Insufficient evidence requires `HOLD` or `HARD HOLD`; guessing is forbidden.

## Global Complete-Answer Rule

ChatGPT and Codex must not answer material AI Worker questions incrementally when one complete safe answer can be produced.

Before responding, review the full goal, current source truth, root cause, related workflows, upstream and downstream effects, failure and recovery paths, locked work, scope and authority, verification requirements, phone-proof boundaries, artifact lineage, additional-defect risk, unnecessary restrictions, and patch-loop risk.

Required internal questions:

1. What is the real underlying issue?
2. What related issue appears next if only the visible symptom is fixed?
3. Which full-application paths are affected?
4. What evidence proves the conclusion?
5. What important requirement may be missing?
6. Does this conflict with current source truth or locked proof?
7. Will this create another patch loop?
8. Is this blocking safe progress unnecessarily?
9. Can the answer be consolidated into one complete action?
10. What material gap remains and must be stated now?

Consolidate all valid findings into one answer, contract, repair plan, or decision. Do not give Sosa fragments to combine, require repeated questions about undisclosed issues, fix only a symptom when a broader root cause is proven, expand into unrelated speculation, or delay a safe phone test with unnecessary analysis.

Incremental work is allowed only when evidence is unavailable, phone proof is required, expansion would be unsafe, a contradiction requires HOLD, or one bounded test is needed to learn the next fact.

This rule controls completeness of analysis and response. It does not broaden mutation authority, replace phone proof, or override HOLD and loop breakers.

Required material-response markers:

- `COMPLETE_SYSTEM_REVIEW = DONE`
- `ROOT_CAUSE_REVIEW = DONE`
- `RELATED_FAILURE_REVIEW = DONE`
- `FULL_GOAL_ALIGNMENT = PASS` or `HOLD` with the exact conflict
- `UNRESOLVED_MATERIAL_GAPS = NONE` or an exact list
- `PATCH_LOOP_RISK = LOW` or `HOLD`
- `ANSWER_CONSOLIDATED = YES`

`FULL_GOAL_ALIGNMENT = PASS` means the decision aligns with the full goal; it does not mean a failed artifact passed.

## Iterative Completeness Review

Before labeling a material prompt, contract, plan, source update, phone test, or release instruction final, perform 5-10 bounded adversarial passes covering missing requirements, contradictions, scope, verification, failure/recovery, source conflicts, unnecessary restrictions, duplicate wording, end-to-end alignment, and executable clarity.

Each pass asks whether any necessary addition, removal, correction, consolidation, or scope protection remains. Integrate accepted corrections into one replacement output. Do not make Sosa append fragments or return competing versions.

Required final markers:

- `FINAL_PROMPT_REVIEWED = YES`
- `REVIEW_PASSES_COMPLETED = <5-10>`
- `UNRESOLVED_GAPS = NONE` or an exact list
- `UNNECESSARY_RESTRICTIONS = NONE` or an exact list requiring correction
- `OUTPUT_CONSOLIDATED = YES`

These review passes are advisory process controls whose outputs are independently auditable only through the resulting contract and markers; they must not delay a ready bounded phone test.

## Shared Execution Contract and Prebuild Acknowledgment

Before every material runtime build, ChatGPT must issue one exact machine-readable execution contract. Use canonical UTF-8 JSON or another explicitly named deterministic format; hash the exact bytes. The contract is a controlled input, not a fifth root authority file. Every artifact and report must carry the same `CONTRACT_SHA256`.

Required contract fields:

- `CONTRACT_ID`, `CONTRACT_VERSION`, `CONTRACT_SHA256`, `APPROVED_BY_SOSA`, `SUPERSEDES = ALL PRIOR BUILD PROMPTS`, `INHERITS = NONE`;
- `SOURCE_MAIN_SHA`, `FOUR_SOURCE_FILE_SHA256_VALUES`;
- `FULL_GOAL`, `CURRENT_CAPABILITY`, `PRODUCT_BEHAVIOR_VERSION`, `PRODUCT_BEHAVIOR`, `TECHNICAL_DESIGN`;
- `BEHAVIORAL_AUTHORITY_FILENAME_AND_SHA`, `MECHANICAL_PARENT_FILENAME_AND_SHA`, `PHONE_PROVEN_ANCESTOR_FILENAME_AND_SHA`, `REFERENCE_ONLY_ARTIFACTS`, `REJECTED_ARTIFACTS`, `LOCKED_SUBTREE_HASHES`, `PROTECTED_TASK_HASHES`;
- `AUTHORIZED_FILES`, `AUTHORIZED_TASKS`, `AUTHORIZED_ACTIONS`, `AUTHORIZED_FIELDS`, `AUTHORIZED_VARIABLES`, `AUTHORIZED_CALL_EDGES`, `AUTHORIZED_NEW_TASKS`, `AUTHORIZED_MUTATIONS`;
- `PROTECTED_FILES`, `PROTECTED_TASKS`, `PROTECTED_ACTIONS`, `PROTECTED_FIELDS`, `PROTECTED_BYTE_RANGES`;
- `CALL_GRAPH_SCOPE`, `CALL_GRAPH_SCOPE_EXPANSION_RULE`;
- `TASKER_ACTION_TEMPLATE_PROVENANCE`, `NUMERIC_ACTION_ORDER_REQUIRED`, `RAW_BYTE_PRESERVATION_RULE`, `BRANCH_TARGET_REBASE_RULE`;
- `SECRET_AND_ARTIFACT_LANE_POLICY`;
- `PREBUILD_HARD_STOPS`, `LOCALLY_REPAIRABLE_DEFECTS`, `SCOPE_EXPANSION_HOLD_CONDITIONS`, `PHONE_PROOF_REQUIRED_CONDITIONS`, `UNSUPPORTED_CONDITIONS`;
- `REQUIRED_OUTPUTS`, `ACCEPTANCE_TESTS`, `FORBIDDEN_BEHAVIOR`, `STATIC_ONLY_CLAIMS`, `PHONE_ONLY_CLAIMS`, `UNSUPPORTED_CLAIMS`, `PHONE_PROOF_BOUNDARY`, `RELEASE_BOUNDARY`, `STOP_CONDITIONS`, `DELIVERY_REQUIREMENTS`.

The contract must separate Sosa's product decisions, ChatGPT's technical design, Codex's implementation scope, static/model/import/phone claims, and release claims.

A genuinely inapplicable contract or evidence field may use `NOT_APPLICABLE - <reason>`. Missing evidence may not be replaced with an invented value, fake seed, guessed row, or unnecessary delivery requirement.

Before modification, Codex must return:

- `SOURCE_READ = PASS`
- `CURRENT_MAIN_SHA = <exact>`
- `FOUR_SOURCE_FILE_SHA256_VALUES = <exact>`
- `CONTRACT_SHA_MATCH = PASS`
- `BASELINE_SHA_MATCH = PASS`
- `ARTIFACT_LINEAGE_RESOLVED = PASS`
- `FULL_GOAL_LOADED = YES`
- `PRODUCT_BEHAVIOR_UNDERSTOOD = YES`
- `TECHNICAL_DESIGN_UNDERSTOOD = YES`
- `AUTHORIZED_SCOPE_UNDERSTOOD = YES`
- `PROTECTED_SCOPE_UNDERSTOOD = YES`
- `CALL_GRAPH_SCOPE_UNDERSTOOD = YES`
- `PHONE_BOUNDARY_UNDERSTOOD = YES`
- `DELIVERY_CAPABILITY_CHECKED = YES`
- `CONTRADICTIONS = NONE`
- `BUILD_BASE = <exact>`
- `BUILD_METHOD = <exact>`
- `INDEPENDENT_VERIFIER_METHOD = <exact>`
- `STRUCTURAL_SCANNER_METHOD = <exact>`

Any false or missing item causes `STATUS = CONTRACT_CONTRADICTION_HOLD` and `MAKE_NO_CHANGES = YES`.

## Artifact Lineage and Invalid Parents

Every contract must separately identify behavioral authority, mechanical parent, phone-proven ancestor, reference-only artifacts, rejected artifacts, locked subtree hashes, and protected-task hashes. Full-product baseline, capability ancestor, behavioral authority, and mechanical parent are not interchangeable.

A structurally invalid candidate is forbidden as a runtime patch parent. Invalidity includes malformed control flow, corrupted numeric order, malformed action schema, unexplained drift, broken call paths, unreliable generator/verifier assumptions, incomplete entry-to-side-effect behavior, invalid branch targets, unproven destructive behavior, or self-approving reports.

Required response:

- `INVALID_PARENT = TRUE`
- `PATCH_PARENT = FORBIDDEN`
- `REBUILD_FROM_LAST_PROVEN_BASELINE = REQUIRED`

A rejected artifact is failure evidence only. ChatGPT may authorize reuse of one isolated mechanical region only after independently proving that exact region safe; it never makes the rejected full artifact trusted.

## Exact Mutation Allowlist and Defect Classification

General phrases such as "minimum necessary," "gate every entry," "preserve unrelated behavior," or "repair locally" do not authorize changes. The contract must name exact tasks, actions/insertion points, fields, variables, new tasks, calls, profiles/scenes/registry nodes, protected tasks/bytes, and the scope-expansion rule.

When required behavior cannot fit the allowlist: `STATUS = SCOPE_EXPANSION_HOLD` and `MAKE_NO_CHANGES = YES`. Codex must not silently expand scope.

Classify every defect exactly once:

- `PREBUILD_HARD_STOP`: no modification, packaging, or PASS report;
- `LOCALLY_REPAIRABLE_WITHIN_SCOPE`: repair locally, then rerun all independent verification;
- `SCOPE_EXPANSION_HOLD`: stop before modification and request one exact contract correction;
- `PHONE_PROOF_REQUIRED`: proceed only to the exact approved phone boundary;
- `UNSUPPORTED`: do not imply the capability exists.

The Complete-Answer Rule governs analysis and the return; it does not authorize continued execution after a fundamental failure. At the first fundamental failure, stop mutation, dependent testing, packaging, phone-plan generation, and approval work. Perform only bounded read-only analysis needed to state the exact failure, proven material consequences, clean baseline, classification, and unresolved gaps in one consolidated blocker. Do not keep building to collect defects, and do not omit already-established material consequences.

Fundamental failures include source or contract mismatch, incomplete lineage, invalid parent, malformed control flow or schema, corrupted action order, invalid branch target, unexplained protected drift, broken required call path, unsafe ownership, unverified destructive write, unsafe delimiter/encoding, secret exposure, builder/verifier disagreement, self-approval, or incomplete artifact identity.

## State-Machine-First and Maintenance Concurrency

Before implementing locks, rows, messages, Send, confirmation, DONE, Archive, DeadArchive, Compactor, recovery, STOP, retry, lifecycle, UI, persistent state, destructive writes, maintenance, or ownership, map:

1. states and legal/illegal transitions;
2. owners and entry conditions;
3. side effects and readback requirements;
4. persistent boundaries;
5. failure exits and terminal cleanup;
6. STOP, restart, and recovery behavior;
7. idempotency, foreign-owner, and stale-state behavior.

No implementation begins until the model is internally consistent. Every subsystem must have one normalized product-behavior version in current source truth or the exact contract; later chat wording cannot silently replace it.

For maintenance behavior, a flag alone is not a pause. The contract and finished artifact must define and prove:

- how in-flight work reaches quiescence and which locks must be idle;
- which new, direct/manual, and Sheet-transaction entries are blocked;
- why permitted intake remains safe;
- who owns maintenance and how ownership is verified;
- guaranteed cleanup on success, failure, STOP, crash, and restart;
- normal resumption;
- stuck-state detection and safe handling without foreign release;
- why processing cannot remain permanently blocked.

## Tasker XML Construction Standard

Tasker XML is a strict compiled execution format, not ordinary editable text.

1. Numeric action `sr="actN"` defines execution order; XML element order does not.
2. Generic XML rewriting and bulk task/action renumbering are forbidden.
3. Unknown changed-action structure is `HARD HOLD`.
4. Every changed or new action must match a proven Tasker schema.
5. Unchanged unknown legacy actions must remain byte-identical and be reported `UNSUPPORTED` or `PHONE_REQUIRED`; they become `HARD HOLD` when affected by or reachable in the changed safety path.
6. Duplicate task IDs, unauthorized duplicate names, action `sr`, and action-child `sr` values are forbidden.
7. Every `If`, `Else`, `End If`, `For`, and `End For` must use proven action codes/schemas and balance in numeric order without underflow, leftovers, or crossing blocks.
8. Action-level conditions must never be treated as block `If` actions.
9. Required Do Maths and variable-expansion behavior must be verified explicitly.
10. Every Perform Task reference, profile/scene reference, Goto, anchor, label, relative branch, loop, cleanup target, and registry reference must resolve after edits.
11. Every plugin action must preserve its proven class, field order, configuration, and Continue-After-Error encoding except exact authorized fields.
12. Unchanged tasks and XML regions remain raw-byte identical unless explicitly authorized.
13. Encoding, BOM, delimiters, separators, mojibake, credentials, and privacy must be checked on exact output bytes.
14. Report action counts, the largest applicable phone-proven size, candidate size, and unresolved import/render risk.
15. Tasker import/render proof outranks generic XML parse success.

Every new or changed action must record:

- `ACTION_TYPE`
- `TEMPLATE_SOURCE_TASK`
- `TEMPLATE_SOURCE_ACTION`
- `TEMPLATE_SOURCE_ARTIFACT_SHA256`
- `FIELDS_CHANGED`
- `FIELDS_PRESERVED`

Required templates include If, Else, End If, For, End For, Goto, Stop, Variable Set/Add/Clear, Perform Task, AutoSheets, and every other plugin action used. Invented schemas are forbidden.

When actions are inserted, deleted, or moved, independently rebase and verify every branch target. Prove no stale target, wrong-block target, skipped cleanup, unauthorized side effect, unreachable required path, ownership bypass, STOP bypass, or readback bypass.

When wrapping a working task:

1. extract the original in numeric action order;
2. add only the authorized wrapper;
3. compare again with the wrapper removed;
4. prove original actions remain identical in relative order and meaning;
5. prove no side effect crossed a guard;
6. prove working paths remain reachable;
7. prove no unrelated behavior or serialization drift;
8. prove branch targets and action-count deltas exactly match authorization.

Any unexpected difference is `HARD HOLD`; packaging is forbidden.

## Data Safety, Secrets, and Artifact Lanes

Any path carrying user-controlled content must prove exact round-trip preservation for question marks, section signs, commas, quotes, apostrophes, CR/LF, emojis, repeated/leading/trailing spaces, percent signs, Tasker-variable-like text, JSON-like text, delimiter-like text, blanks, and multiline values. Unsafe separators and unescaped concatenation are forbidden; use per-field writes or proven reversible encoding.

Every artifact and report receives an independent scan for keys, tokens, passwords, credentials, authorization headers, private contact data, private messages, and unnecessary production/workbook identifiers. Inherited secrets are never grandfathered.

A detected secret causes `HARD HOLD`, phone-import rejection, and public-upload prohibition.

Every contract defines:

- `PUBLIC_STATIC_AUDIT_ARTIFACT`: no secrets, private contact data, or unnecessary production identifiers;
- `PRIVATE_PHONE_IMPORT_ARTIFACT`: no embedded credentials unless Sosa explicitly authorizes that exact private lane; prefer documented phone-local reinjection.

A blank credential cannot be called runnable unless reinjection is documented. Reinjection preparation is allowed only when it does not require rebuilding the artifact.

## Contract Invalidation and Rollback

Any drift in source main, any of the four source-file hashes, baseline bytes, contract bytes, or authorized artifact identity invalidates the execution contract. Mutation resumes only under a newly hashed contract.

Canonical contract hashing must avoid self-reference: calculate SHA256 over exact canonical bytes with `CONTRACT_SHA256` omitted or replaced by a fixed 64-zero placeholder, then populate the field. Put the contract SHA in every report and package manifest. Embed it in executable XML only when an authorized schema-proven metadata field exists.

Documentation rollback uses recorded original blob SHAs plus an independently reviewed reverse diff. Runtime rollback restores the exact last proven ancestor; it never patches or reuses a rejected candidate.

## Independent Finished-Artifact Verification

The builder, independent finished-artifact verifier, and structural scanner must not approve from shared assumptions.

- The builder creates the candidate and implementation metadata; it cannot approve the artifact.
- The independent verifier reads only the locked contract, exact baseline, and exact final candidate; reconstructs numeric execution/control flow and call paths; attempts to disprove the candidate; and does not trust builder reports.
- The structural scanner validates XML structure, action order, control-flow balance, schemas, branch targets, references, duplicates, protected bytes, encoding, secrets, size, and import risk.
- ChatGPT independently audits the exact return and remains the only artifact/phone/merge/release approver.

Builder/verifier disagreement is `HARD HOLD`; packaging and phone import are forbidden.

Every required behavior needs a finished-artifact trace:

`ENTRY -> AUTHORIZATION -> GUARD -> OWNERSHIP -> SOURCE BINDING -> SIDE EFFECT -> READBACK -> COMMIT -> RELEASE -> TERMINAL STATE`

Each trace identifies task IDs/names, numeric actions, variables, plugin actions, branches, callers/callees, and persistent boundaries. Presence of a For, flag, variable, reader, call, changed task, nonzero mutation count, parse success, or report statement is not behavior proof.

Every contract requirement maps to:

- `REQUIREMENT_ID`, `REQUIREMENT_TEXT`, `IMPLEMENTATION_LOCATION`;
- `STATIC_PROOF`, `CONTROL_FLOW_MODEL_PROOF`, `SIMULATION_PROOF`, `MUTATION_PROOF`;
- `TASKER_IMPORT_PROOF_REQUIRED`, `PHONE_PROOF_REQUIRED`, `PHONE_TEST_STEP`;
- `RELEASE_RELEVANCE`, `STATUS`.

Allowed proof statuses are `PROVEN_STATIC`, `PROVEN_MODEL`, `PROVEN_LOCAL`, `PHONE_REQUIRED`, `UNSUPPORTED`, `FAILED`, and `HOLD`.

The application call graph must include profile/event/manual/scene/shortcut/startup/recovery roots, recursive/self calls, Perform Task edges, action-level conditions, Goto edges, all direct/indirect callers and callees, dominance over destructive side effects, STOP, release, and restart paths. Known recovery callers, including Tasks 130 and 183 when applicable, must not be omitted.

Every runtime candidate's integrity return must cover source lock, mutation map, protected-byte comparison, call graph, runtime contracts, state machine, failure/recovery/STOP, scenario matrix, forbidden reachability, historical regressions, exact phone boundary, permanent integration point, unsupported claims, and release mapping.

## Reproducible Artifact-Driven Testing

Every simulation, mutation, fuzz, or model claim must include exact script and SHA, baseline/candidate/contract SHAs, inputs, fixtures, seeds or `NOT_APPLICABLE`, scenarios, XML paths, outputs, commands, exit codes, failure criteria, logs, and mutant artifacts or hashes.

Abstract models may support design only. Mutations must alter the finished artifact and prove the independent verifier rejects them.

The verifier must reject exact SHA-verified fixtures for known failures, including rejected DeadArchive R1/R2 artifacts, malformed conditional Variable Set patterns, malformed block semantics, unmatched End If, element-order renumbering, stale branches, artifact-detached mocks, incomplete call graphs, stuck maintenance, unexplained body drift, self-proof, unsafe delimiters, hidden scope expansion, and unproven destructive writes. A known-bad artifact cannot be reported rejected until its exact fixture SHA is available.

A verifier accepting a known-bad fixture is invalid.

## Proof Lanes and Phone-Readiness Gate

Classify claims separately:

- `BUILD_STATUS`
- `STATIC_XML_STATUS`
- `CONTROL_FLOW_MODEL_STATUS`
- `SIMULATION_STATUS`
- `MUTATION_STATUS`
- `TASKER_IMPORT_STATUS`
- `PHONE_RUNTIME_STATUS`
- `CAPABILITY_STATUS`
- `RELEASE_STATUS`

PASS in one lane never implies another. Static XML cannot prove Tasker import, plugin output, Android/UI behavior, real maintenance quiescence, workbook mutation, or message retention. Unknown import/render risk is `PHONE_REQUIRED`, never static PASS.

Before ChatGPT runtime-logic audit, Codex must report:

- `XML_PARSE = PASS`
- `NUMERIC_ACTION_ORDER = PASS`
- `CONTROL_FLOW_BALANCE = PASS`
- `ACTION_SCHEMAS = PASS`
- `BRANCH_TARGETS = PASS`
- `TASK_REFERENCES = PASS`
- `CALL_GRAPH_COMPLETE = PASS`
- `DUPLICATE_IDS = 0`
- `DUPLICATE_ACTION_SR = 0`
- `DUPLICATE_CHILD_SR = 0`
- `PROTECTED_BYTES = PASS`
- `ORIGINAL_BODY_PRESERVATION = PASS`
- `SECRET_SCAN = PASS`
- `CONTRACT_MATCH = PASS`
- `REQUIREMENT_MATRIX_COMPLETE = PASS`
- `ARTIFACT_BEHAVIOR_TRACES = PASS`
- `REPRODUCIBLE_TESTS_PRESENT = PASS`
- `KNOWN_BAD_ARTIFACTS_REJECTED = PASS`
- `KNOWN_BAD_FIXTURE_GAPS = NONE`; any exact fixture gap is `HOLD` and blocks candidate status
- `DATA_ROUND_TRIP = PASS`
- `TASK_SIZE_RISK_REPORTED = PASS`
- `PHONE_TEST_CAN_RUN_DIRECTLY = YES`

A package requiring another runtime build before reaching the phone is not a candidate.

## Delivery Capability Preflight

Before promising delivery, report `GIT_AVAILABLE`, `DRIVE_CONNECTOR_AVAILABLE`, `UPLOAD_ALLOWED`, `BROWSER_POLICY_ALLOWS_UPLOAD`, `CHATGPT_HANDOFF_AVAILABLE`, and `OUTPUT_DIRECTORY_WRITABLE` as `YES`, `NO`, or `NOT_REQUESTED` with evidence.

A local path is never a browser link, Drive link, upload, or external location. A valid upload claim requires confirmed upload, remote file ID, exact filename, remote size, downloaded SHA comparison, and an observed working `https://` address.

If requested delivery is unavailable:

- `STATUS = DELIVERY_CAPABILITY_HOLD`
- `LOCAL_FILES_CREATED = YES` or `NO`
- `UPLOAD_COMPLETED = NO`

## ChatGPT Fixed Acceptance and Phone Contract

ChatGPT must not rely on Codex's report alone. For every exact runtime candidate, ChatGPT must:

1. refresh current GitHub source truth;
2. verify contract SHA and package inventory;
3. calculate candidate SHA and scan secrets/privacy;
4. verify lineage, baseline, and candidate diff;
5. reconstruct numeric action order and Tasker control flow;
6. validate action schemas, duplicate fields, and branch targets;
7. validate task/registry references and protected bytes;
8. validate original-body preservation and mutation scope;
9. reconstruct the complete call graph and trace each requirement to side effects;
10. check ownership, release, STOP, failure, restart, and recovery;
11. check maintenance concurrency and data round trip;
12. report size/import risk;
13. review independent verifier evidence and known-bad rejection;
14. identify phone-only claims;
15. issue only the authorized binary phone decision.

ChatGPT must challenge incomplete instructions, prevent accidental removal of required behavior, explain conflicts simply, recommend the professional design, never guess or approve from urgency/polished reports, avoid needless delay, and perform the complete-answer and iterative reviews.

Phone instructions derive only from exact candidate/contract SHAs and unresolved phone requirements. They state exact task, expected/forbidden outputs, workbook bounds, runlog/evidence markers, cleanup, and pass/fail criteria. Phone proof applies only to the exact tested boundary.

Binary phone decisions remain:

- `APPROVED FOR ONE PHONE RUN`
- `REJECTED — ONE EXACT DEFECT / ONE MINIMAL REPAIR`

## Full-System Workflow, Loop Breakers, and Permanent Safety

Every runtime repair is one component of the complete application. The sequence is:

1. application-wide audit;
2. one contract-bounded integrated root-cause repair covering all proven related effects inside the allowlist;
3. integrated full-project build;
4. exact finished-artifact verification;
5. independent ChatGPT audit;
6. one bounded phone test;
7. immediate permanent integration or one bounded repair.

Minimal testing isolates cause; it never creates a separate product. Temporary proof names its permanent integration point. After a passed sub-proof, do not create another package for the same sub-proof.

Stop and reduce scope when two Codex returns occur without a phone test, a documentation loop repeats, a diagnostic exceeds the behavior, unrelated behaviors enter one build, another build would be required before phone, temporary proof lacks integration, or local PASS is treated as application PASS.

Never allow guessed AutoInput targets, wrong-recipient or duplicate Send, automatic retry after a possible click, DONE before independent confirmation, Archive/DeadArchive clear before exact copy/readback, unowned or double release, owned lock leaks, hidden profile/live activation, tracker movement without proof, private data in public GitHub, or silent contract/scope expansion.

STOP prevents new work and leaves profiles disabled. Tasker encoding and unchanged bytes remain protected.

## Return Vocabulary and Documentation Independence

Runtime returns are limited to:

- `CANDIDATE_READY_FOR_CHATGPT_AUDIT`
- `FUNDAMENTAL_BLOCKER_PROVEN`
- `CONTRACT_CONTRADICTION_HOLD`
- `SCOPE_EXPANSION_HOLD`
- `DELIVERY_CAPABILITY_HOLD`

Documentation source-update returns are limited to:

- `CANDIDATE_SOURCE_UPDATE_FOR_CHATGPT_AUDIT`
- `CONTRACT_CONTRADICTION_HOLD`
- `FUNDAMENTAL_BLOCKER_PROVEN`

`LOCKED`, `CANDIDATE`, `HOLD`, `HARD HOLD`, `FAILED`, and `UNSUPPORTED` remain evidence/capability classifications, not competing final-return codes.

Before returning a source update, perform rule deduplication, contradiction matrix, enforceability classification, lifecycle completeness, bloat review, and reversibility proof. Record original blob SHAs. Permanent rules belong here; current status belongs in the controller; failure evidence/prevention belongs in the ledger.

Classify new rules as `MECHANICALLY_ENFORCEABLE`, `INDEPENDENTLY_AUDITABLE`, `PHONE_PROOF_DEPENDENT`, or `ADVISORY_ONLY`. Advisory controls must not be described as mechanically guaranteed.

Protocol coverage must include prebuild, authority, contract, lineage, scope, state design, construction, verification, testing, packaging, delivery, ChatGPT audit, phone proof, release, failure handling, loop prevention, and rollback. Missing lifecycle coverage is HOLD.

Codex may not approve its own documentation update:

- `SOURCE_UPDATE_SELF_APPROVED = NO`
- `CHATGPT_DIFF_AUDIT_REQUIRED = YES`
- `MERGE_APPROVED = NO`
