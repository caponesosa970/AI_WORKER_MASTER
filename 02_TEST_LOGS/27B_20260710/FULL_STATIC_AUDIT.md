# Full Static Audit

## Full XML
- Path: `[PRIVATE_FULL_IMPORT_XML_PATH_REDACTED]/27B_TASKER_IMPORT_XML__AIW_BUILD100_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE_WITH_KEY_20260710.xml`
- Parse: PASS
- Root: `TaskerData`
- Tasker version: `6.7.5-beta`
- Task count: 75
- Profile count: 4
- Scene count: 1
- Project count: 1
- Duplicate task IDs: 0
- Duplicate task names: 0
- Duplicate profile IDs: 0
- Missing Perform Task refs: 0
- Missing profile refs: 0
- Missing project task refs: 0
- Duplicate action sr issues: 0

## Redacted XML
- Path: `CHATGPT_AUDIT_XML/redacted_for_audit/27B_REDACTED_NOT_FOR_IMPORT__AIW_BUILD100_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE_20260710.xml`
- Parse: PASS
- Root: `TaskerData`
- Task count: 75
- Missing Perform Task refs: 0

## Scope
- New runtime task: `AIW27B_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE`
- Original `FINAL Send Sheet` unchanged by body: True
- Original `FINAL Send Sheet` source body SHA256: `AEBB3DBD01D436FB1F722AC125D547F9E85B612A6CAE429FED21CEB0C651CA18`
- Original `FINAL Send Sheet` output body SHA256: `AEBB3DBD01D436FB1F722AC125D547F9E85B612A6CAE429FED21CEB0C651CA18`
- Project wrapper preserved; project task registry updated with new task ID.

## Redaction Scan
- Redacted XML `sk-` key patterns: 0
- Redacted XML raw Sheet ID matches: 0
- Redacted XML raw target phone matches: 0
- Redacted XML raw target digit matches: 0
- Redacted XML OpenAI text markers: 28 benign text/config markers; private key pattern count is zero.

## Limit
Static audit is not phone proof.
