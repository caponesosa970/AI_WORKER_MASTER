# V15A AutoInput Preservation Report

## Rule
Do not invent or replace v15a AutoInput targets. Preserve the v15a TextNow action settings exactly for copied AutoInput actions.

## Preserved From v15a
- Navigate up / Back
- Chats
- Search icon: `com.enflick.android.TextNow:id/menu_search`
- Search field: `com.enflick.android.TextNow:id/search_field`
- List item selector: `1`
- Compose target: `com.enflick.android.TextNow:id/edit_text_out`
- Send button target: `com.enflick.android.TextNow:id/button_send`
- Waits, `%SSUIStep` markers, `%err/%errmsg` checks, and failure routing pattern.

## Scope Control
The copied result-select, compose, reply-write, and `button_send` actions are retained only behind the hard gate:

- `%AIW27BAllowSend=1`
- Row 75 status `READY_TO_SEND`

When `%AIW27BAllowSend` is not `1`, the task stops before TextNow and before any send-capable action.
When row 75 status is `TEST_STAGED_NO_SEND`, the task stops before TextNow and before any send-capable action.

## Diff Result
See `V15A_AUTOINPUT_DIFF_TABLE.csv`.
