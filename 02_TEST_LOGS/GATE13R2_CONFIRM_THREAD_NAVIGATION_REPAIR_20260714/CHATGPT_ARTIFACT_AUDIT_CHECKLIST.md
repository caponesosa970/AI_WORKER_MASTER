# ChatGPT Full Artifact Audit Checklist

- [ ] Download the standalone XML and verify `1C4D13872C3D6B4579AA698F9E7D2F50F3E81467A4CBD4EAD63CD567087832A7`.
- [ ] Download the ZIP and verify `5AB5E12C64D830C1EF6436CBEA3FB5CC56D82ABFB874670F7417441668D2AD03`.
- [ ] Confirm the ZIP has exactly one XML byte-equal to the standalone XML.
- [ ] Parse 83 tasks, 4 profiles, and 1 scene.
- [ ] Confirm Task ID/name/`sr` and action `sr` uniqueness.
- [ ] Confirm no missing task/profile/scene references.
- [ ] Confirm Task 231 has one incoming caller, Task 225, and no outgoing task call.
- [ ] Confirm Task 231 contains no Sheets, compose focus, reply write, Send, status write, profile action, or lock clear.
- [ ] Compare all 12 Task 231 AutoInput nodes against Task 223 source fields and bundles.
- [ ] Confirm source cutoff before `MESSAGE_BOX` and compose focus.
- [ ] Confirm Task 225 calls Task 231 once and preserves its existing confirmation algorithm.
- [ ] Confirm navigation failure sets `CONFIRM_NAVIGATION_HOLD`, skips DONE, and reaches common confirmation-lock cleanup.
- [ ] Confirm 81/81 other pre-existing tasks, profiles, and scene are raw-byte identical.
- [ ] Confirm credential occurrence/value unchanged without printing it.
- [ ] Confirm no private artifact is tracked or present in public diff.
- [ ] Treat this report as candidate readiness only, not phone-import approval.
