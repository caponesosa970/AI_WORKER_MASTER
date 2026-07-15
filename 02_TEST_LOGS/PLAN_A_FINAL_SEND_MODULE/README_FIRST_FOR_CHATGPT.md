# Plan A Final Artifact Correction

Status: CANDIDATE / HOLD FOR CHATGPT FULL ARTIFACT AUDIT

## Replacement

- Rejected XML SHA256: `00C66283AD073BBCB3E8DEBA6EDE3258BB53258D56D007BB48EF4E404307AA59`
- Rejected ZIP SHA256: `086811C752CCEAF1705EE00427290F756B3EFC489363F52C93BDDC7A5A2575E4`
- Replacement XML: `PLAN_A1_FULL_PROJECT_TASKER_IMPORT__FINAL_SEND_MODULE_CORRECTED_PRIVATE.xml`
- Replacement XML SHA256: `82148AF8B72A24E3DBA77936A15E547E2114FEC01B705A084D12AA319534442B`
- Replacement ZIP: `PLAN_A1_FULL_PROJECT_PHONE_IMPORT__FINAL_SEND_MODULE_CORRECTED_PRIVATE.zip`
- Replacement ZIP SHA256: `3FC66D70AA55B517E99F7AECB067DBD9D211AAF91667D94161ED424C73E73F89`
- Replacement sidecar: `PLAN_A1_SHA256__FINAL_SEND_MODULE_CORRECTED_PRIVATE.txt`

Do not import the rejected Plan A artifact.

## Exact Correction

1. Task 71 AutoSheets actions with `se=false`: 2/2.
2. Task 223 AutoSheets actions with `se=false`: 24/24.
3. The Send-button `%err` and `%errmsg` are copied immediately into `%send_action_err` and `%send_action_errmsg` before any clear.
4. Numeric Send-error detection uses `%send_action_err`.
5. `SEND_OUTCOME_UNKNOWN_REVIEW` is reported only after exact ID/status readback confirms that state.
6. An unconfirmed unknown outcome routes to `POST_SEND_STATUS_UPDATE_FAILED` without another Send click.
7. The original saved Send error is retained through `SS Lock Release HARD`.

Only Tasks 71 and 223 changed from the rejected Plan A artifact. Tasks 199 and 224 are byte-identical.

## Archive Ruling

The previous Archive HOLD statement is superseded. Existing Task 199 Archive/DeadArchive maintenance calls were present in the verified base, remain byte-identical, remain behind their existing flags, and are not reachable from Task 224. No new Archive action or Send-to-Archive route was added.

## Validation

- Prior independent suite: 43/43 PASS.
- New independent suite: 67/67 PASS.
- Static scenarios: 18/18 PASS.
- Tasker XML parse/root/reference audit: PASS.
- Tasks/profiles/scenes: 76/4/1.
- Duplicate task IDs/names/sr and missing references: 0.
- `button_send` nodes: 1.
- Automatic Send retry paths: 0.
- Owned-lock AutoSheets failures bypassing cleanup: 0.
- ZIP contains exactly one XML and its bytes match the standalone XML.

## Boundaries

- Tracker: 8/14 locked = 57%.
- Sheet changed: NO.
- Tasker run: NO.
- Phone proof claimed: NO.
- Phone import approved: NO.
- Controlled Send, DONE, Archive progression, live/timer, capacity, and release remain blocked.
