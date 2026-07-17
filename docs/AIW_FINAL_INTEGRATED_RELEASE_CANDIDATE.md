# AI Worker Final Integrated Release Candidate

Status: `FINAL INTEGRATED RELEASE CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT`

This public-safe change records the offline validation tooling used for the private final integrated Tasker candidate. It contains no private XML, credentials, phone numbers, raw run logs, or Drive links.

## Integrated runtime boundary

The candidate uses one production path:

1. TextNow notification fields stay local until exact ingress ownership.
2. The event is written and read back in a durable ingress journal.
3. One queue owner drains journal rows into bounded Sheet1 or Overflow storage.
4. Unresolved Overflow state blocks newer direct admission and downstream processing.
5. Processing uses the protected exact-row transaction and bounded API retry tasks unchanged.
6. Send uses the protected dynamic Send task unchanged and permits at most one click.
7. Independent confirmation is required before DONE.
8. Exact Archive verification is required before source cleanup.
9. STOP persists desired-run state and never clears an active owner.
10. Boot recovery is owner-, age-, durable-state-, and proof-ledger-gated.

DeadArchive, Compactor, old ON/OFF controls, reset-lock controls, the legacy retry worker, and the obsolete D3A launcher are blocked or unreachable from final controls.

## Public validation tools

- `scripts/aiw_final_integrated_analyze.py` builds a system inventory, call graph, variable/lock ownership map, and plugin audit without printing secret values.
- `scripts/aiw_final_integrated_validate.py` independently parses with `minidom`, checks task/profile/scene/project references, control stacks, exact task scope, protected task byte equality, collision policy, Keep Device Awake markers, plugin settings, lock order, reachability, encoding, and privacy markers.
- `scripts/aiw_final_integrated_model.py` runs the independent state model, fault matrix, randomized concurrency schedules, and mutation suite.
- `scripts/aiw_final_integrated_controller_rerun.py` independently reruns the controller-supplied model.
- `scripts/aiw_tasker_task_dump.py` creates privacy-safe task/action dumps for audit.

## Offline evidence boundary

The final offline run reports:

- 100,000 randomized schedules;
- more than 2.5 million modeled operations;
- zero randomized invariant failures;
- failure injection before and after 67 durable/runtime boundaries;
- 15 of 15 unsafe mutations detected;
- two independent XML/static validator passes;
- protected processing, Send, confirmation, Archive, and navigation tasks byte-identical to the authorized private base;
- no missing active task, profile, scene, or project references;
- no duplicate task IDs or names;
- no control-stack imbalance;
- no mojibake indicator.

These are offline/static results only. They do not prove Tasker import/render, Google Sheets migration, TextNow UI behavior, Moto Razr behavior, one real Send, reboot recovery, or phone soak.

## Release boundary

- Phone import approved: NO.
- Phone proof claimed: NO.
- Release claimed: NO.
- PR merge authorized: NO.

The private XML, one-entry phone-import ZIP, SHA sidecar, migration manifest, and complete proof packet are handed to ChatGPT through private storage for full artifact audit. Sosa is not asked to import until ChatGPT approves those exact private artifacts.
