# Static Test Matrix

| Case | Expected static result | Result |
| --- | --- | --- |
| `valid_exact_sender` | ui=True; result=THREAD_NAV_READY | PASS |
| `invalid_sender` | ui=False; result=THREAD_NAV_HOLD | PASS |
| `launch_error` | ui=True; result=THREAD_NAV_HOLD | PASS |
| `navigate_up_error` | ui=True; result=THREAD_NAV_HOLD | PASS |
| `chats_error` | ui=True; result=THREAD_NAV_HOLD | PASS |
| `search_first_error_retry_success` | ui=True; result=THREAD_NAV_READY | PASS |
| `search_field_final_error` | ui=True; result=THREAD_NAV_HOLD | PASS |
| `search_text_entry_error` | ui=True; result=THREAD_NAV_HOLD | PASS |
| `contact_selection_error` | ui=True; result=THREAD_NAV_HOLD | PASS |
| `navigation_hold` | done_reachable=False; row_mutation=False; lock_releases=1 | PASS |
| `confirmation_ui_hold` | done_reachable=False; row_status=SEND_CLICKED_AWAITING_CONFIRM; lock_releases=1 | PASS |
| `positive_confirmation` | done_reachable=True; requires_existing_exact_confirmation=True; lock_releases=1 | PASS |
| `duplicate_send` | reachable_send_nodes=0 | PASS |
| `task_231_incoming_caller` | Task 225 only | PASS |
| `task_231_task_calls` | zero | PASS |
| `task_231_sheets` | zero | PASS |
| `task_231_compose_or_send` | zero | PASS |
| `task_225_confirmation_algorithm` | raw semantic sequence unchanged | PASS |
| `task_225_owned_lock_release` | exactly one guarded release | PASS |
| `all_other_existing_tasks` | 81/81 raw-byte identical | PASS |
| `profiles_and_scene` | raw-byte identical; disabled states preserved | PASS |
| `credential` | one occurrence; value unchanged; not printed | PASS |
| `zip` | one XML; bytes equal standalone XML | PASS |
