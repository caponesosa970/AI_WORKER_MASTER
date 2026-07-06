# AI Worker Issue History Register

Updated: 2026-07-06

Status: CANDIDATE / HOLD FOR CHATGPT AUDIT

Purpose:

- Keep repeated Build100 failures from being repeated.
- Make every known issue traceable to proof, root cause, prevention rule, and preflight check.
- Require Codex to read this register before every future build or package.

## Required Fields

Every issue entry must include:

- issue_id
- date/time
- package/file name
- SHA256 if available
- affected task/profile/scene
- observed failure
- exact proof source
- root cause, if known
- prevention rule
- required preflight check
- current status: OPEN / MITIGATED / LOCKED / FAILED
- next validation needed

## Issue Register

| issue_id | date/time | package/file name | SHA256 if available | affected task/profile/scene | observed failure | exact proof source | root cause | prevention rule | required preflight check | current status | next validation needed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AIW-ISSUE-TASKER-IMPORT-001 | 2026-07-06 | Prior Group B/Group B2 runtime XML packages before 10C Tasker-safe correction | See failed package ledgers and package SHA inventories | Full Tasker import XML | XML/package appeared statically parseable or auditable but did not import/parse properly into Tasker. | User-reported Tasker import rejection plus later 10C Tasker-safe correction package. | Static XML parse was treated as stronger proof than actual Tasker importability; package lane did not clearly enforce a full phone-import XML separate from audit XML. | Tasker importability is a first-class gate. Runtime packages must include a full importable `PHONE_IMPORT_XML` lane. Redacted XML is audit-only and must be labeled `NOT_FOR_TASKER_IMPORT`. If Tasker rejects import XML, classify `FAILED / TASKER IMPORT REJECTED` and rebuild from the last Tasker-accepted XML only. | Confirm full import XML parse PASS, root `TaskerData`, no BOM/mojibake import risk, no redaction, Tasker-safe formatting, and clear README naming which XML is for phone import. | MITIGATED | Next runtime package must prove phone-import XML lane and ChatGPT audit before Moto import. |
| AIW-ISSUE-REDACTED-IMPORT-001 | 2026-07-06 | Group B2 audit ZIP / redacted XML lane | See `10_CHATGPT_AUDIT_ZIP__AIW_BUILD100_GROUP_B2_RUNTIME_PATCH_20260705.zip` and later 10B/10C correction SHA files | Package structure | A redacted ChatGPT audit XML was treated like it might be importable. | ChatGPT audit feedback requiring importable private XML separate from redacted audit XML. | Audit XML and phone-import XML were not clearly separated for the user path. | Never import redacted XML. Never place only redacted XML in a runtime patch package. Runtime package must contain `PHONE_IMPORT_XML/full_importable_xml/` and optional `CHATGPT_AUDIT_XML/redacted_for_audit/NOT_FOR_TASKER_IMPORT`. | ZIP content check must prove both lanes when runtime XML is included; README must state phone-import lane plainly. | MITIGATED | Next runtime package must pass lane naming and redaction/import separation check. |
| AIW-ISSUE-SEARCH-FORMAT-001 | 2026-07-05 | Stage4B formatted-number dry-run attempt | Runlog/audit SHA recorded in Stage4B progress reports | `SS Safe Send Dry-Run` | Formatted sender `+1(910) 447-7850` failed contact pick before normalization; digits-only `9104477850` passed. | Stage4B failed runlog and `AIW_STAGE4B_DRYRUN_PROGRESS_SPEED_LOG_20260705.md`; later 10C Group B2 phone proof. | TextNow search did not resolve the formatted phone string in the same way as digits-only search. | Phone-like TextNow search keys must be normalized to digits-only in the proven send UI lane unless a contact-name path is specifically being tested. | Before UI search, log raw search key, normalized search key, and proof that the normalized key is used for TextNow search. | LOCKED | Preserve normalization in all future send UI tasks unless ChatGPT approves a contact-name test. |
| AIW-ISSUE-DIRTY-UI-001 | 2026-07-06 | Group B2 dry-run paste proof | Group B2 phone proof/runlog SHA recorded in phone proof package | `SS Safe Send Dry-Run`; TextNow message box | Dry-run paste proof can leave text in the TextNow message box. | Group B2 phone proof and user confirmation that pasted dry-run text was manually cleared before Group C planning. | Dry-run intentionally stops before send button after paste proof, so UI can remain dirty. | Any dry-run paste proof must log `DIRTY_UI_REQUIRES_MANUAL_CLEAR` if text remains. No send-capable task may run while dirty UI marker is active. User or task must clear text before controlled send tests. | Before controlled send, verify dirty UI marker is clear and TextNow message box is empty or intentionally prepared by the controlled-send task. | MITIGATED | Group C runtime patch must prove dirty UI is clear before one-send proof. |
| AIW-ISSUE-GROUPC-SEND-PROOF-001 | 2026-07-06 | `13_CHATGPT_AUDIT_ZIP__AIW_BUILD100_GROUP_C_RUNTIME_PATCH_20260706.zip` | Package SHA `D7D21E9F25A55BA6685D58495EFE39D86B71324FC9C6D17CB227B8CCC0C7A83A` | `SS Controlled One-Row Send Proof` | Pre-patch inspection found missing approved-recipient guard and missing TextNow thread/header confirmation before send-button action; task then moves into pass/DONE markers without independent sent-message proof. | `GROUP_C_HARD_HOLD_SAFETY_INSPECTION_20260706.md` in Group C hard-hold package. | Existing controlled-send task is not safe for a narrow Group C runtime patch. | Do not patch this task narrowly for Group C until ChatGPT approves either a broader rebuild or a new isolated proof task. | Before any Group C runtime patch, prove approved-recipient guard, thread/header confirmation, one-send proof, DONE-after-proof, and uncertainty-to-review route in design and static diff. | OPEN | ChatGPT must choose broader rebuild, new isolated Group C proof task, or continued HARD HOLD. |

## Standing Use Rule

Before every future build or package, Codex must:

1. Read this register.
2. State which issue prevention rules apply.
3. State which prior failed packages must not be reused.
4. State the approved baseline/source file.
5. Refuse to build if the baseline is unclear.
6. Refuse to build if the requested patch repeats a known failed pattern.
