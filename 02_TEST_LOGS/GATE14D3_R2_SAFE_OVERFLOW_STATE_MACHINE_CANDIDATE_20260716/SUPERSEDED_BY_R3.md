# R2 Superseded

Status: HOLD / DO NOT IMPORT / DO NOT PHONE TEST.

R2 is preserved as source history but is not the current Gate 14D3 candidate.

The final audit found two exact gaps:

- drain acquired the shared admission lock before exact source binding and the verified DRAINING transition;
- Attempts and LastError were not durably recorded for every bound failed drain path.

Gate 14D3 R3 supersedes R2 and repairs only those two contracts while preserving the complete second-audit state machine.
