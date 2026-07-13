# 30A Regression Report

Status: SOURCE-TRUTH CORRECTED / NO RUNTIME CHANGE

## Regression Checks

| Regression class | Result |
|---|---|
| Sosa-created source incorrectly downgraded | CORRECTED |
| SEARCH_ICON preservation claim unsupported | CORRECTED: field-level comparison now proves preservation |
| Fake repair when no drift exists | PREVENTED |
| Runtime XML changed without need | PREVENTED |
| API key exposed or changed | NOT TOUCHED |
| Send/DONE/Archive/live/capacity unlocked | NOT TOUCHED |
| Tracker percentage changed | NOT CHANGED |
| Phone proof claimed from static comparison | NOT CLAIMED |

## Responsibility Correction

User/operator responsibility:

NONE.

Codex responsibility:

Prior 29A conclusion was unsupported after Sosa source-truth clarification. Codex must record that V15A is authoritative and Sosa-created.

ChatGPT/controller responsibility:

Controller failed to apply repeated user source-truth instructions before accepting the 29A source-not-found conclusion.

## Current Failure Classification

The 27B phone failure remains real.

Corrected classification:

Phone/runtime/UI failure with V15A SEARCH_ICON preserved.

Not currently supported:

Source-preservation drift.
