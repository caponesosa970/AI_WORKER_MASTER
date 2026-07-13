# Control Flow and Exact-Once Audit

## Machine Assertions

- `xml_parse`: PASS
- `taskerdata_root`: PASS
- `tasks`: PASS
- `profiles`: PASS
- `scenes`: PASS
- `duplicate_task_ids`: PASS
- `duplicate_task_names`: PASS
- `duplicate_task_srs`: PASS
- `missing_perform_refs`: PASS
- `missing_profile_refs`: PASS
- `missing_scene_refs`: PASS
- `only_four_tasks_changed`: PASS
- `old_candidate_names_active`: PASS
- `diagnostic_tasks_active`: PASS
- `task199_selector_calls_exactly_one`: PASS
- `task199_direct_worker_calls_zero`: PASS
- `task71_worker_calls_exactly_one`: PASS
- `task224_worker_calls_exactly_one`: PASS
- `task223_button_send_nodes_exactly_one`: PASS
- `task223_lock_release_calls_exactly_one`: PASS
- `done_writes_zero`: PASS
- `archive_actions_zero_in_71_223_224`: PASS
- `task199_existing_archive_routes_unchanged`: PASS
- `lastbotreply_assignments_zero`: PASS
- `lastbottime_assignments_zero`: PASS
- `task223_gate9_refs_zero`: PASS
- `task223_hardcoded_row_75_zero`: PASS
- `task223_fixed_phone_zero`: PASS
- `task223_fixed_message_zero`: PASS
- `task223_fixed_reply_zero`: PASS
- `task223_uppercase_temporaries_zero`: PASS
- `task223_numeric_error_checks_only`: PASS
- `task223_auto_send_retry_zero`: PASS
- `reachable_send_clicks_at_most_one`: PASS
- `control_flow_balanced`: PASS
- `autoinput_method1_all_equal`: PASS
- `autoinput_method2_all_equal`: PASS
- `credential_unchanged`: PASS
- `zip_one_xml`: PASS
- `zip_xml_matches`: PASS
- `zip_integrity`: PASS
- `static_matrix_all_pass`: PASS

## Independent Validator

- `root_taskerdata`: PASS
- `task_count_76`: PASS
- `profile_count_4`: PASS
- `scene_count_1`: PASS
- `unique_task_ids`: PASS
- `unique_task_names`: PASS
- `unique_task_srs`: PASS
- `changed_tasks_exact`: PASS
- `task_roles_exact`: PASS
- `missing_perform_refs_zero`: PASS
- `control_flow_balanced`: PASS
- `autoinput_canonical_all_equal`: PASS
- `autoinput_semantic_all_equal`: PASS
- `keyboard_count_two`: PASS
- `keyboards_exact`: PASS
- `button_send_one`: PASS
- `send_marker_one`: PASS
- `send_click_latch_one`: PASS
- `no_done_write`: PASS
- `no_lastbotreply`: PASS
- `no_lastbottime`: PASS
- `no_gate9_in_worker`: PASS
- `no_fixed_row_in_worker`: PASS
- `no_fixed_phone_in_worker`: PASS
- `uppercase_temporaries_zero`: PASS
- `autosheets_continue_after_error`: PASS
- `autosheets_no_broad_err_regex`: PASS
- `three_second_retry_waits_present`: PASS
- `selector_once_from_queue`: PASS
- `worker_not_direct_from_queue`: PASS
- `worker_once_from_selector`: PASS
- `lock_release_once_in_worker`: PASS
- `launcher_worker_once`: PASS
- `launcher_no_plugin_actions`: PASS
- `old_candidate_names_zero`: PASS
- `diagnostic_names_zero`: PASS
- `credential_unchanged`: PASS
- `zip_exactly_one_xml`: PASS
- `zip_bytes_match`: PASS
- `zip_integrity`: PASS
- `sidecar_records_xml`: PASS
- `sidecar_records_zip`: PASS
- `matrix_cases_18`: PASS

## 18-Case Static Matrix

| Case | Scenario | Expected safe result | Max Send clicks | Owned lock release | Result |
| ---: | --- | --- | ---: | --- | --- |
| 1 | Launcher not armed | `GATE9_NOT_ARMED` | 0 | N/A | PASS |
| 2 | Missing or invalid parameters | `SEND_INVALID_PARAMETERS` | 0 | N/A | PASS |
| 3 | Lock already active | `SEND_BLOCKED_LOCK` | 0 | N/A | PASS |
| 4 | Initial row read fails twice | `SEND_ROW_READ_FAILED` | 0 | YES | PASS |
| 5 | Row ID mismatch | `SEND_ROW_BINDING_MISMATCH` | 0 | YES | PASS |
| 6 | Row status not ready | `SEND_ROW_NOT_READY` | 0 | YES | PASS |
| 7 | Bad sender/message/reply | `SEND_BAD_DATA_HELD\|PRE_SEND_FAILURE_STATUS_UNKNOWN` | 0 | YES | PASS |
| 8 | SENDING write fails | `SENDING_WRITE_FAILED` | 0 | YES | PASS |
| 9 | SENDING readback fails | `SENDING_READBACK_FAILED` | 0 | YES | PASS |
| 10 | Search ultimately fails | `PRE_SEND_UI_FAILED\|PRE_SEND_FAILURE_STATUS_UNKNOWN` | 0 | YES | PASS |
| 11 | Contact selection fails | `PRE_SEND_UI_FAILED\|PRE_SEND_FAILURE_STATUS_UNKNOWN` | 0 | YES | PASS |
| 12 | Compose path fails | `PRE_SEND_UI_FAILED\|PRE_SEND_FAILURE_STATUS_UNKNOWN` | 0 | YES | PASS |
| 13 | Send button reports error | `SEND_OUTCOME_UNKNOWN_REVIEW` | 1 | YES | PASS |
| 14 | Send click and status confirm | `SEND_CLICKED_AWAITING_CONFIRM` | 1 | YES | PASS |
| 15 | Send click post-status failure | `POST_SEND_STATUS_UPDATE_FAILED` | 1 | YES | PASS |
| 16 | Selector pending state | `SEND_BLOCKED_PENDING_CONFIRM` | 0 | N/A | PASS |
| 17 | Selector one ready row | `FINAL Send One Bound Row once` | 0 | N/A | PASS |
| 18 | Queue Cycle integration | `FINAL Send Sheet once` | 0 | N/A | PASS |

## Exact Changed-Task/Action Ledger

The following index is generated from the final XML construction ledger. Every changed action has one classified purpose.

### Task 71

| Action | Classified purpose |
| ---: | --- |
| 0 | caller token guard |
| 1 | manual caller rejected: failed |
| 2 | manual caller rejected: result |
| 3 | manual caller rejected: detail |
| 4 | manual caller rejected: controller error |
| 5 | manual caller rejected: stop |
| 6 | end caller token guard |
| 7 | reset selector result flags |
| 8 | QueueView attempt 1: clear qv_source array |
| 9 | QueueView attempt 1: clear qv_id array |
| 10 | QueueView attempt 1: clear qv_sender array |
| 11 | QueueView attempt 1: clear qv_message array |
| 12 | QueueView attempt 1: clear qv_status array |
| 13 | QueueView attempt 1: clear qv_reply array |
| 14 | QueueView attempt 1: clear qv_touch array |
| 15 | QueueView attempt 1: clear qv_button array |
| 16 | QueueView attempt 1: clear qv_time array |
| 17 | QueueView attempt 1: clear qv_ticker array |
| 18 | QueueView attempt 1: clear err |
| 19 | QueueView attempt 1: clear errmsg |
| 20 | QueueView Get Data attempt 1 |
| 21 | QueueView attempt 1: assume structurally valid |
| 22 | QueueView attempt 1: numeric error |
| 23 | QueueView attempt 1: plugin error |
| 24 | QueueView attempt 1: end error check |
| 25 | QueueView attempt 1: require one or more rows |
| 26 | QueueView attempt 1: empty result |
| 27 | QueueView attempt 1: end row-count check |
| 28 | QueueView attempt 1: qv_source dimensional check |
| 29 | QueueView attempt 1: qv_source dimension mismatch |
| 30 | QueueView attempt 1: end qv_source dimension check |
| 31 | QueueView attempt 1: qv_id dimensional check |
| 32 | QueueView attempt 1: qv_id dimension mismatch |
| 33 | QueueView attempt 1: end qv_id dimension check |
| 34 | QueueView attempt 1: qv_sender dimensional check |
| 35 | QueueView attempt 1: qv_sender dimension mismatch |
| 36 | QueueView attempt 1: end qv_sender dimension check |
| 37 | QueueView attempt 1: qv_message dimensional check |
| 38 | QueueView attempt 1: qv_message dimension mismatch |
| 39 | QueueView attempt 1: end qv_message dimension check |
| 40 | QueueView attempt 1: qv_status dimensional check |
| 41 | QueueView attempt 1: qv_status dimension mismatch |
| 42 | QueueView attempt 1: end qv_status dimension check |
| 43 | QueueView attempt 1: qv_reply dimensional check |
| 44 | QueueView attempt 1: qv_reply dimension mismatch |
| 45 | QueueView attempt 1: end qv_reply dimension check |
| 46 | QueueView attempt 1: qv_touch dimensional check |
| 47 | QueueView attempt 1: qv_touch dimension mismatch |
| 48 | QueueView attempt 1: end qv_touch dimension check |
| 49 | QueueView attempt 1: qv_button dimensional check |
| 50 | QueueView attempt 1: qv_button dimension mismatch |
| 51 | QueueView attempt 1: end qv_button dimension check |
| 52 | QueueView attempt 1: qv_time dimensional check |
| 53 | QueueView attempt 1: qv_time dimension mismatch |
| 54 | QueueView attempt 1: end qv_time dimension check |
| 55 | QueueView attempt 1: qv_ticker dimensional check |
| 56 | QueueView attempt 1: qv_ticker dimension mismatch |
| 57 | QueueView attempt 1: end qv_ticker dimension check |
| 58 | QueueView retry after first failure |
| 59 | QueueView exact 3 second retry wait |
| 60 | QueueView attempt 2: clear qv_source array |
| 61 | QueueView attempt 2: clear qv_id array |
| 62 | QueueView attempt 2: clear qv_sender array |
| 63 | QueueView attempt 2: clear qv_message array |
| 64 | QueueView attempt 2: clear qv_status array |
| 65 | QueueView attempt 2: clear qv_reply array |
| 66 | QueueView attempt 2: clear qv_touch array |
| 67 | QueueView attempt 2: clear qv_button array |
| 68 | QueueView attempt 2: clear qv_time array |
| 69 | QueueView attempt 2: clear qv_ticker array |
| 70 | QueueView attempt 2: clear err |
| 71 | QueueView attempt 2: clear errmsg |
| 72 | QueueView Get Data attempt 2 |
| 73 | QueueView attempt 2: assume structurally valid |
| 74 | QueueView attempt 2: numeric error |
| 75 | QueueView attempt 2: plugin error |
| 76 | QueueView attempt 2: end error check |
| 77 | QueueView attempt 2: require one or more rows |
| 78 | QueueView attempt 2: empty result |
| 79 | QueueView attempt 2: end row-count check |
| 80 | QueueView attempt 2: qv_source dimensional check |
| 81 | QueueView attempt 2: qv_source dimension mismatch |
| 82 | QueueView attempt 2: end qv_source dimension check |
| 83 | QueueView attempt 2: qv_id dimensional check |
| 84 | QueueView attempt 2: qv_id dimension mismatch |
| 85 | QueueView attempt 2: end qv_id dimension check |
| 86 | QueueView attempt 2: qv_sender dimensional check |
| 87 | QueueView attempt 2: qv_sender dimension mismatch |
| 88 | QueueView attempt 2: end qv_sender dimension check |
| 89 | QueueView attempt 2: qv_message dimensional check |
| 90 | QueueView attempt 2: qv_message dimension mismatch |
| 91 | QueueView attempt 2: end qv_message dimension check |
| 92 | QueueView attempt 2: qv_status dimensional check |
| 93 | QueueView attempt 2: qv_status dimension mismatch |
| 94 | QueueView attempt 2: end qv_status dimension check |
| 95 | QueueView attempt 2: qv_reply dimensional check |
| 96 | QueueView attempt 2: qv_reply dimension mismatch |
| 97 | QueueView attempt 2: end qv_reply dimension check |
| 98 | QueueView attempt 2: qv_touch dimensional check |
| 99 | QueueView attempt 2: qv_touch dimension mismatch |
| 100 | QueueView attempt 2: end qv_touch dimension check |
| 101 | QueueView attempt 2: qv_button dimensional check |
| 102 | QueueView attempt 2: qv_button dimension mismatch |
| 103 | QueueView attempt 2: end qv_button dimension check |
| 104 | QueueView attempt 2: qv_time dimensional check |
| 105 | QueueView attempt 2: qv_time dimension mismatch |
| 106 | QueueView attempt 2: end qv_time dimension check |
| 107 | QueueView attempt 2: qv_ticker dimensional check |
| 108 | QueueView attempt 2: qv_ticker dimension mismatch |
| 109 | QueueView attempt 2: end qv_ticker dimension check |
| 110 | QueueView end retry |
| 111 | QueueView final failure |
| 112 | QueueView final failure: failed |
| 113 | QueueView final failure: result |
| 114 | QueueView final failure: detail |
| 115 | QueueView final failure: controller error |
| 116 | QueueView final failure: stop |
| 117 | QueueView final failure end |
| 118 | pending-state scan index reset |
| 119 | scan all QueueView statuses for pending send |
| 120 | pending-state scan index increment |
| 121 | pending send state match |
| 122 | pending send state: blocked |
| 123 | pending send state: no send |
| 124 | pending send state: result |
| 125 | pending send state: detail |
| 126 | pending send state: controller error |
| 127 | pending send state: stop selector |
| 128 | end pending state match |
| 129 | end pending-state scan |
| 130 | ready-state scan index reset |
| 131 | scan QueueView for first READY_TO_SEND |
| 132 | ready-state scan index increment |
| 133 | READY_TO_SEND candidate |
| 134 | bind selected source row |
| 135 | bind selected ID |
| 136 | normalize selected source row |
| 137 | normalize selected ID |
| 138 | validate selected SourceRow and ID |
| 139 | selector found READY row |
| 140 | selector publishes exact source row |
| 141 | selector result before worker call |
| 142 | call permanent worker exactly once |
| 143 | stop after one bound-row transaction |
| 144 | invalid selected SourceRow or ID |
| 145 | invalid selector candidate: failed |
| 146 | invalid selector candidate: result |
| 147 | invalid selector candidate: detail |
| 148 | invalid selector candidate: controller error |
| 149 | invalid selector candidate: stop |
| 150 | end selector candidate validation |
| 151 | end READY candidate |
| 152 | end ready-state scan |
| 153 | no READY row: no send |
| 154 | no READY row: result |
| 155 | no READY row: detail |
| 156 | no READY row: controller error |
| 157 | no READY row: stop |

### Task 223

| Action | Classified purpose |
| ---: | --- |
| 0 | reset worker result flags |
| 1 | bind source-row parameter |
| 2 | bind expected-ID parameter |
| 3 | normalize source-row parameter |
| 4 | normalize expected-ID parameter |
| 5 | reject nonnumeric source-row parameter |
| 6 | invalid parameters: failed |
| 7 | invalid parameters: result |
| 8 | invalid parameters: detail |
| 9 | invalid parameters: controller error |
| 10 | invalid parameters: stop before lock |
| 11 | end numeric source-row guard |
| 12 | reject header or row 1 |
| 13 | invalid row number: failed |
| 14 | invalid row number: result |
| 15 | invalid row number: detail |
| 16 | invalid row number: controller error |
| 17 | invalid row number: stop before lock |
| 18 | end row greater-than-one guard |
| 19 | reject blank/unresolved/error expected ID |
| 20 | invalid expected ID: failed |
| 21 | invalid expected ID: result |
| 22 | invalid expected ID: detail |
| 23 | invalid expected ID: controller error |
| 24 | invalid expected ID: stop before lock |
| 25 | end expected-ID guard |
| 26 | publish bound source row |
| 27 | worker never claims confirmed send |
| 28 | existing Send lock guard |
| 29 | existing Send lock: blocked |
| 30 | existing Send lock: failed |
| 31 | existing Send lock: result |
| 32 | existing Send lock: detail |
| 33 | existing Send lock: controller error |
| 34 | existing Send lock: stop without releasing foreign lock |
| 35 | end existing Send lock guard |
| 36 | acquire Send lock |
| 37 | record Send lock start time |
| 38 | mark local lock ownership |
| 39 | initialize transaction continuation flag |
| 40 | initialize exact-once Send-click latch |
| 41 | initialize persistent SENDING confirmation latch |
| 42 | initial exact-row read attempt 1: clear row_id array |
| 43 | initial exact-row read attempt 1: clear row_sender array |
| 44 | initial exact-row read attempt 1: clear row_message array |
| 45 | initial exact-row read attempt 1: clear row_status array |
| 46 | initial exact-row read attempt 1: clear row_reply array |
| 47 | initial exact-row read attempt 1: clear row_touch array |
| 48 | initial exact-row read attempt 1: clear row_button array |
| 49 | initial exact-row read attempt 1: clear row_time array |
| 50 | initial exact-row read attempt 1: clear row_ticker array |
| 51 | initial exact-row read attempt 1: clear err |
| 52 | initial exact-row read attempt 1: clear errmsg |
| 53 | initial exact-row read: Get Data attempt 1 |
| 54 | initial exact-row read attempt 1: assume read valid |
| 55 | initial exact-row read attempt 1: numeric plugin error check |
| 56 | initial exact-row read attempt 1: plugin error invalidates read |
| 57 | initial exact-row read attempt 1: end plugin error check |
| 58 | initial exact-row read attempt 1: row_id count check |
| 59 | initial exact-row read attempt 1: row_id count invalid |
| 60 | initial exact-row read attempt 1: end row_id count check |
| 61 | initial exact-row read attempt 1: row_id value check |
| 62 | initial exact-row read attempt 1: row_id value invalid |
| 63 | initial exact-row read attempt 1: end row_id value check |
| 64 | initial exact-row read attempt 1: row_sender count check |
| 65 | initial exact-row read attempt 1: row_sender count invalid |
| 66 | initial exact-row read attempt 1: end row_sender count check |
| 67 | initial exact-row read attempt 1: row_sender value check |
| 68 | initial exact-row read attempt 1: row_sender value invalid |
| 69 | initial exact-row read attempt 1: end row_sender value check |
| 70 | initial exact-row read attempt 1: row_message count check |
| 71 | initial exact-row read attempt 1: row_message count invalid |
| 72 | initial exact-row read attempt 1: end row_message count check |
| 73 | initial exact-row read attempt 1: row_message value check |
| 74 | initial exact-row read attempt 1: row_message value invalid |
| 75 | initial exact-row read attempt 1: end row_message value check |
| 76 | initial exact-row read attempt 1: row_status count check |
| 77 | initial exact-row read attempt 1: row_status count invalid |
| 78 | initial exact-row read attempt 1: end row_status count check |
| 79 | initial exact-row read attempt 1: row_status value check |
| 80 | initial exact-row read attempt 1: row_status value invalid |
| 81 | initial exact-row read attempt 1: end row_status value check |
| 82 | initial exact-row read attempt 1: row_reply count check |
| 83 | initial exact-row read attempt 1: row_reply count invalid |
| 84 | initial exact-row read attempt 1: end row_reply count check |
| 85 | initial exact-row read attempt 1: row_reply value check |
| 86 | initial exact-row read attempt 1: row_reply value invalid |
| 87 | initial exact-row read attempt 1: end row_reply value check |
| 88 | initial exact-row read attempt 1: row_touch count check |
| 89 | initial exact-row read attempt 1: row_touch count invalid |
| 90 | initial exact-row read attempt 1: end row_touch count check |
| 91 | initial exact-row read attempt 1: row_touch value check |
| 92 | initial exact-row read attempt 1: row_touch value invalid |
| 93 | initial exact-row read attempt 1: end row_touch value check |
| 94 | initial exact-row read attempt 1: row_button count check |
| 95 | initial exact-row read attempt 1: row_button count invalid |
| 96 | initial exact-row read attempt 1: end row_button count check |
| 97 | initial exact-row read attempt 1: row_button value check |
| 98 | initial exact-row read attempt 1: row_button value invalid |
| 99 | initial exact-row read attempt 1: end row_button value check |
| 100 | initial exact-row read attempt 1: row_time count check |
| 101 | initial exact-row read attempt 1: row_time count invalid |
| 102 | initial exact-row read attempt 1: end row_time count check |
| 103 | initial exact-row read attempt 1: row_time value check |
| 104 | initial exact-row read attempt 1: row_time value invalid |
| 105 | initial exact-row read attempt 1: end row_time value check |
| 106 | initial exact-row read attempt 1: row_ticker count check |
| 107 | initial exact-row read attempt 1: row_ticker count invalid |
| 108 | initial exact-row read attempt 1: end row_ticker count check |
| 109 | initial exact-row read attempt 1: row_ticker value check |
| 110 | initial exact-row read attempt 1: row_ticker value invalid |
| 111 | initial exact-row read attempt 1: end row_ticker value check |
| 112 | initial exact-row read: retry only after first failure |
| 113 | initial exact-row read: exact 3 second retry wait |
| 114 | initial exact-row read attempt 2: clear row_id array |
| 115 | initial exact-row read attempt 2: clear row_sender array |
| 116 | initial exact-row read attempt 2: clear row_message array |
| 117 | initial exact-row read attempt 2: clear row_status array |
| 118 | initial exact-row read attempt 2: clear row_reply array |
| 119 | initial exact-row read attempt 2: clear row_touch array |
| 120 | initial exact-row read attempt 2: clear row_button array |
| 121 | initial exact-row read attempt 2: clear row_time array |
| 122 | initial exact-row read attempt 2: clear row_ticker array |
| 123 | initial exact-row read attempt 2: clear err |
| 124 | initial exact-row read attempt 2: clear errmsg |
| 125 | initial exact-row read: Get Data attempt 2 |
| 126 | initial exact-row read attempt 2: assume read valid |
| 127 | initial exact-row read attempt 2: numeric plugin error check |
| 128 | initial exact-row read attempt 2: plugin error invalidates read |
| 129 | initial exact-row read attempt 2: end plugin error check |
| 130 | initial exact-row read attempt 2: row_id count check |
| 131 | initial exact-row read attempt 2: row_id count invalid |
| 132 | initial exact-row read attempt 2: end row_id count check |
| 133 | initial exact-row read attempt 2: row_id value check |
| 134 | initial exact-row read attempt 2: row_id value invalid |
| 135 | initial exact-row read attempt 2: end row_id value check |
| 136 | initial exact-row read attempt 2: row_sender count check |
| 137 | initial exact-row read attempt 2: row_sender count invalid |
| 138 | initial exact-row read attempt 2: end row_sender count check |
| 139 | initial exact-row read attempt 2: row_sender value check |
| 140 | initial exact-row read attempt 2: row_sender value invalid |
| 141 | initial exact-row read attempt 2: end row_sender value check |
| 142 | initial exact-row read attempt 2: row_message count check |
| 143 | initial exact-row read attempt 2: row_message count invalid |
| 144 | initial exact-row read attempt 2: end row_message count check |
| 145 | initial exact-row read attempt 2: row_message value check |
| 146 | initial exact-row read attempt 2: row_message value invalid |
| 147 | initial exact-row read attempt 2: end row_message value check |
| 148 | initial exact-row read attempt 2: row_status count check |
| 149 | initial exact-row read attempt 2: row_status count invalid |
| 150 | initial exact-row read attempt 2: end row_status count check |
| 151 | initial exact-row read attempt 2: row_status value check |
| 152 | initial exact-row read attempt 2: row_status value invalid |
| 153 | initial exact-row read attempt 2: end row_status value check |
| 154 | initial exact-row read attempt 2: row_reply count check |
| 155 | initial exact-row read attempt 2: row_reply count invalid |
| 156 | initial exact-row read attempt 2: end row_reply count check |
| 157 | initial exact-row read attempt 2: row_reply value check |
| 158 | initial exact-row read attempt 2: row_reply value invalid |
| 159 | initial exact-row read attempt 2: end row_reply value check |
| 160 | initial exact-row read attempt 2: row_touch count check |
| 161 | initial exact-row read attempt 2: row_touch count invalid |
| 162 | initial exact-row read attempt 2: end row_touch count check |
| 163 | initial exact-row read attempt 2: row_touch value check |
| 164 | initial exact-row read attempt 2: row_touch value invalid |
| 165 | initial exact-row read attempt 2: end row_touch value check |
| 166 | initial exact-row read attempt 2: row_button count check |
| 167 | initial exact-row read attempt 2: row_button count invalid |
| 168 | initial exact-row read attempt 2: end row_button count check |
| 169 | initial exact-row read attempt 2: row_button value check |
| 170 | initial exact-row read attempt 2: row_button value invalid |
| 171 | initial exact-row read attempt 2: end row_button value check |
| 172 | initial exact-row read attempt 2: row_time count check |
| 173 | initial exact-row read attempt 2: row_time count invalid |
| 174 | initial exact-row read attempt 2: end row_time count check |
| 175 | initial exact-row read attempt 2: row_time value check |
| 176 | initial exact-row read attempt 2: row_time value invalid |
| 177 | initial exact-row read attempt 2: end row_time value check |
| 178 | initial exact-row read attempt 2: row_ticker count check |
| 179 | initial exact-row read attempt 2: row_ticker count invalid |
| 180 | initial exact-row read attempt 2: end row_ticker count check |
| 181 | initial exact-row read attempt 2: row_ticker value check |
| 182 | initial exact-row read attempt 2: row_ticker value invalid |
| 183 | initial exact-row read attempt 2: end row_ticker value check |
| 184 | initial exact-row read: end retry |
| 185 | initial exact-row read final failure |
| 186 | row read failure: failed |
| 187 | row read failure: result |
| 188 | row read failure: detail |
| 189 | row read failure: controller error |
| 190 | row read failure: stop transaction |
| 191 | end row read failure |
| 192 | continue after exact-row read |
| 193 | bind scalar %bound_id |
| 194 | normalize scalar %bound_id |
| 195 | bind scalar %bound_sender |
| 196 | normalize scalar %bound_sender |
| 197 | bind scalar %bound_message |
| 198 | normalize scalar %bound_message |
| 199 | bind scalar %bound_status |
| 200 | normalize scalar %bound_status |
| 201 | bind scalar %bound_reply |
| 202 | normalize scalar %bound_reply |
| 203 | bind scalar %bound_ticker |
| 204 | normalize scalar %bound_ticker |
| 205 | exact row-binding ID mismatch |
| 206 | binding mismatch: failed |
| 207 | binding mismatch: result |
| 208 | binding mismatch: detail |
| 209 | binding mismatch: controller error |
| 210 | binding mismatch: stop transaction |
| 211 | end binding mismatch |
| 212 | exact READY_TO_SEND guard |
| 213 | not-ready row: failed |
| 214 | not-ready row: result |
| 215 | not-ready row: detail |
| 216 | not-ready row: controller error |
| 217 | not-ready row: stop transaction |
| 218 | end READY_TO_SEND guard |
| 219 | normalize and validate bound Send data |
| 220 | bind sender |
| 221 | bind message |
| 222 | bind reply |
| 223 | normalize %sendname |
| 224 | normalize %sendmessage |
| 225 | normalize %sendreply |
| 226 | sender invalid: try ticker fallback |
| 227 | use ticker fallback for invalid sender |
| 228 | normalize ticker fallback |
| 229 | end ticker fallback |
| 230 | normalize numeric sender |
| 231 | remove sender formatting |
| 232 | remove leading US country code |
| 233 | end numeric sender normalization |
| 234 | bind TextNow search key |
| 235 | initialize bad-data flag |
| 236 | validate %sendsearch |
| 237 | mark %sendsearch invalid |
| 238 | end %sendsearch validation |
| 239 | validate %sendmessage |
| 240 | mark %sendmessage invalid |
| 241 | end %sendmessage validation |
| 242 | validate %sendreply |
| 243 | mark %sendreply invalid |
| 244 | end %sendreply validation |
| 245 | require reply length greater than one |
| 246 | mark reply too short |
| 247 | end reply length check |
| 248 | numeric recipient must be exactly ten digits |
| 249 | mark numeric recipient invalid |
| 250 | end numeric recipient length check |
| 251 | end normalize and validate data |
| 252 | bad bound data failure route |
| 253 | bad-data HOLD_PRE_SEND_FAILED write attempt 1: clear err |
| 254 | bad-data HOLD_PRE_SEND_FAILED write attempt 1: clear errmsg |
| 255 | bad-data HOLD_PRE_SEND_FAILED write: Update Cells attempt 1 |
| 256 | bad-data HOLD_PRE_SEND_FAILED write: assume attempt 1 success |
| 257 | bad-data HOLD_PRE_SEND_FAILED write: attempt 1 numeric error check |
| 258 | bad-data HOLD_PRE_SEND_FAILED write: attempt 1 failed |
| 259 | bad-data HOLD_PRE_SEND_FAILED write: end attempt 1 error check |
| 260 | bad-data HOLD_PRE_SEND_FAILED write: retry only after first failure |
| 261 | bad-data HOLD_PRE_SEND_FAILED write: exact 3 second retry wait |
| 262 | bad-data HOLD_PRE_SEND_FAILED write attempt 2: clear err |
| 263 | bad-data HOLD_PRE_SEND_FAILED write attempt 2: clear errmsg |
| 264 | bad-data HOLD_PRE_SEND_FAILED write: Update Cells attempt 2 |
| 265 | bad-data HOLD_PRE_SEND_FAILED write: assume attempt 2 success |
| 266 | bad-data HOLD_PRE_SEND_FAILED write: attempt 2 numeric error check |
| 267 | bad-data HOLD_PRE_SEND_FAILED write: attempt 2 failed |
| 268 | bad-data HOLD_PRE_SEND_FAILED write: end attempt 2 error check |
| 269 | bad-data HOLD_PRE_SEND_FAILED write: end retry |
| 270 | bad-data status write succeeded |
| 271 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: clear verify_id array |
| 272 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: clear verify_sender array |
| 273 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: clear verify_message array |
| 274 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: clear verify_status array |
| 275 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: clear err |
| 276 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: clear errmsg |
| 277 | bad-data HOLD_PRE_SEND_FAILED readback: Get Data attempt 1 |
| 278 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: assume read valid |
| 279 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: numeric plugin error check |
| 280 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: plugin error invalidates read |
| 281 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: end plugin error check |
| 282 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_id count check |
| 283 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_id count invalid |
| 284 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: end verify_id count check |
| 285 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_id value check |
| 286 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_id value invalid |
| 287 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: end verify_id value check |
| 288 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_sender count check |
| 289 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_sender count invalid |
| 290 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: end verify_sender count check |
| 291 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_sender value check |
| 292 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_sender value invalid |
| 293 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: end verify_sender value check |
| 294 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_message count check |
| 295 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_message count invalid |
| 296 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: end verify_message count check |
| 297 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_message value check |
| 298 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_message value invalid |
| 299 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: end verify_message value check |
| 300 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_status count check |
| 301 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_status count invalid |
| 302 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: end verify_status count check |
| 303 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_status value check |
| 304 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: verify_status value invalid |
| 305 | bad-data HOLD_PRE_SEND_FAILED readback attempt 1: end verify_status value check |
| 306 | bad-data HOLD_PRE_SEND_FAILED readback: retry only after first failure |
| 307 | bad-data HOLD_PRE_SEND_FAILED readback: exact 3 second retry wait |
| 308 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: clear verify_id array |
| 309 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: clear verify_sender array |
| 310 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: clear verify_message array |
| 311 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: clear verify_status array |
| 312 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: clear err |
| 313 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: clear errmsg |
| 314 | bad-data HOLD_PRE_SEND_FAILED readback: Get Data attempt 2 |
| 315 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: assume read valid |
| 316 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: numeric plugin error check |
| 317 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: plugin error invalidates read |
| 318 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: end plugin error check |
| 319 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_id count check |
| 320 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_id count invalid |
| 321 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: end verify_id count check |
| 322 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_id value check |
| 323 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_id value invalid |
| 324 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: end verify_id value check |
| 325 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_sender count check |
| 326 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_sender count invalid |
| 327 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: end verify_sender count check |
| 328 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_sender value check |
| 329 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_sender value invalid |
| 330 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: end verify_sender value check |
| 331 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_message count check |
| 332 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_message count invalid |
| 333 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: end verify_message count check |
| 334 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_message value check |
| 335 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_message value invalid |
| 336 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: end verify_message value check |
| 337 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_status count check |
| 338 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_status count invalid |
| 339 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: end verify_status count check |
| 340 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_status value check |
| 341 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: verify_status value invalid |
| 342 | bad-data HOLD_PRE_SEND_FAILED readback attempt 2: end verify_status value check |
| 343 | bad-data HOLD_PRE_SEND_FAILED readback: end retry |
| 344 | bad-data HOLD_PRE_SEND_FAILED: default confirmation false |
| 345 | bad-data HOLD_PRE_SEND_FAILED: exact ID and status confirmation |
| 346 | bad-data HOLD_PRE_SEND_FAILED: confirmation passed |
| 347 | bad-data HOLD_PRE_SEND_FAILED: end exact confirmation |
| 348 | bad-data status write failed |
| 349 | bad-data status unconfirmed |
| 350 | end bad-data status write result |
| 351 | bad-data hold confirmed |
| 352 | bad-data hold result |
| 353 | bad-data hold detail |
| 354 | bad-data hold controller error |
| 355 | bad-data hold unconfirmed |
| 356 | bad-data unknown status result |
| 357 | bad-data unknown status detail |
| 358 | bad-data unknown controller error |
| 359 | end bad-data confirmation result |
| 360 | bad-data terminal failure |
| 361 | bad-data stop transaction |
| 362 | end bad-data failure route |
| 363 | persistent SENDING write gate |
| 364 | SENDING write attempt 1: clear err |
| 365 | SENDING write attempt 1: clear errmsg |
| 366 | SENDING write: Update Cells attempt 1 |
| 367 | SENDING write: assume attempt 1 success |
| 368 | SENDING write: attempt 1 numeric error check |
| 369 | SENDING write: attempt 1 failed |
| 370 | SENDING write: end attempt 1 error check |
| 371 | SENDING write: retry only after first failure |
| 372 | SENDING write: exact 3 second retry wait |
| 373 | SENDING write attempt 2: clear err |
| 374 | SENDING write attempt 2: clear errmsg |
| 375 | SENDING write: Update Cells attempt 2 |
| 376 | SENDING write: assume attempt 2 success |
| 377 | SENDING write: attempt 2 numeric error check |
| 378 | SENDING write: attempt 2 failed |
| 379 | SENDING write: end attempt 2 error check |
| 380 | SENDING write: end retry |
| 381 | SENDING write final failure |
| 382 | SENDING write failure: failed |
| 383 | SENDING write failure: result |
| 384 | SENDING write failure: detail |
| 385 | SENDING write failure: controller error |
| 386 | SENDING write failure: stop transaction |
| 387 | end SENDING write failure |
| 388 | SENDING readback gate |
| 389 | SENDING readback attempt 1: clear verify_id array |
| 390 | SENDING readback attempt 1: clear verify_sender array |
| 391 | SENDING readback attempt 1: clear verify_message array |
| 392 | SENDING readback attempt 1: clear verify_status array |
| 393 | SENDING readback attempt 1: clear err |
| 394 | SENDING readback attempt 1: clear errmsg |
| 395 | SENDING readback: Get Data attempt 1 |
| 396 | SENDING readback attempt 1: assume read valid |
| 397 | SENDING readback attempt 1: numeric plugin error check |
| 398 | SENDING readback attempt 1: plugin error invalidates read |
| 399 | SENDING readback attempt 1: end plugin error check |
| 400 | SENDING readback attempt 1: verify_id count check |
| 401 | SENDING readback attempt 1: verify_id count invalid |
| 402 | SENDING readback attempt 1: end verify_id count check |
| 403 | SENDING readback attempt 1: verify_id value check |
| 404 | SENDING readback attempt 1: verify_id value invalid |
| 405 | SENDING readback attempt 1: end verify_id value check |
| 406 | SENDING readback attempt 1: verify_sender count check |
| 407 | SENDING readback attempt 1: verify_sender count invalid |
| 408 | SENDING readback attempt 1: end verify_sender count check |
| 409 | SENDING readback attempt 1: verify_sender value check |
| 410 | SENDING readback attempt 1: verify_sender value invalid |
| 411 | SENDING readback attempt 1: end verify_sender value check |
| 412 | SENDING readback attempt 1: verify_message count check |
| 413 | SENDING readback attempt 1: verify_message count invalid |
| 414 | SENDING readback attempt 1: end verify_message count check |
| 415 | SENDING readback attempt 1: verify_message value check |
| 416 | SENDING readback attempt 1: verify_message value invalid |
| 417 | SENDING readback attempt 1: end verify_message value check |
| 418 | SENDING readback attempt 1: verify_status count check |
| 419 | SENDING readback attempt 1: verify_status count invalid |
| 420 | SENDING readback attempt 1: end verify_status count check |
| 421 | SENDING readback attempt 1: verify_status value check |
| 422 | SENDING readback attempt 1: verify_status value invalid |
| 423 | SENDING readback attempt 1: end verify_status value check |
| 424 | SENDING readback: retry only after first failure |
| 425 | SENDING readback: exact 3 second retry wait |
| 426 | SENDING readback attempt 2: clear verify_id array |
| 427 | SENDING readback attempt 2: clear verify_sender array |
| 428 | SENDING readback attempt 2: clear verify_message array |
| 429 | SENDING readback attempt 2: clear verify_status array |
| 430 | SENDING readback attempt 2: clear err |
| 431 | SENDING readback attempt 2: clear errmsg |
| 432 | SENDING readback: Get Data attempt 2 |
| 433 | SENDING readback attempt 2: assume read valid |
| 434 | SENDING readback attempt 2: numeric plugin error check |
| 435 | SENDING readback attempt 2: plugin error invalidates read |
| 436 | SENDING readback attempt 2: end plugin error check |
| 437 | SENDING readback attempt 2: verify_id count check |
| 438 | SENDING readback attempt 2: verify_id count invalid |
| 439 | SENDING readback attempt 2: end verify_id count check |
| 440 | SENDING readback attempt 2: verify_id value check |
| 441 | SENDING readback attempt 2: verify_id value invalid |
| 442 | SENDING readback attempt 2: end verify_id value check |
| 443 | SENDING readback attempt 2: verify_sender count check |
| 444 | SENDING readback attempt 2: verify_sender count invalid |
| 445 | SENDING readback attempt 2: end verify_sender count check |
| 446 | SENDING readback attempt 2: verify_sender value check |
| 447 | SENDING readback attempt 2: verify_sender value invalid |
| 448 | SENDING readback attempt 2: end verify_sender value check |
| 449 | SENDING readback attempt 2: verify_message count check |
| 450 | SENDING readback attempt 2: verify_message count invalid |
| 451 | SENDING readback attempt 2: end verify_message count check |
| 452 | SENDING readback attempt 2: verify_message value check |
| 453 | SENDING readback attempt 2: verify_message value invalid |
| 454 | SENDING readback attempt 2: end verify_message value check |
| 455 | SENDING readback attempt 2: verify_status count check |
| 456 | SENDING readback attempt 2: verify_status count invalid |
| 457 | SENDING readback attempt 2: end verify_status count check |
| 458 | SENDING readback attempt 2: verify_status value check |
| 459 | SENDING readback attempt 2: verify_status value invalid |
| 460 | SENDING readback attempt 2: end verify_status value check |
| 461 | SENDING readback: end retry |
| 462 | SENDING: default confirmation false |
| 463 | SENDING: exact ID and status confirmation |
| 464 | SENDING: confirmation passed |
| 465 | SENDING: end exact confirmation |
| 466 | SENDING readback final failure |
| 467 | SENDING readback failure: failed |
| 468 | SENDING readback failure: result |
| 469 | SENDING readback failure: detail |
| 470 | SENDING readback failure: controller error |
| 471 | SENDING readback failure: stop transaction |
| 472 | end SENDING readback failure |
| 473 | end SENDING readback gate |
| 474 | end persistent SENDING write gate |
| 475 | TextNow reachability hard gate |
| 476 | TextNow UI start result |
| 477 | TextNow UI start detail |
| 478 | Launch TextNow exact V15A node |
| 479 | V15A launch settle wait |
| 480 | V15A Navigate up |
| 481 | V15A Navigate up settle wait |
| 482 | V15A Chats |
| 483 | V15A Chats settle wait |
| 484 | Search lane: clear err |
| 485 | Search lane: clear errmsg |
| 486 | Search lane: SEARCH_ICON marker |
| 487 | Dashgood Text Search |
| 488 | Dashgood Text Search reported numeric error |
| 489 | Search lane: error detail |
| 490 | Search retry: clear err |
| 491 | Search retry: clear errmsg |
| 492 | Dashgood Search reset wait 1 |
| 493 | Dashgood reset Navigate up |
| 494 | Dashgood Search reset wait 2 |
| 495 | Dashgood reset Chats |
| 496 | Dashgood Search reset wait 3 |
| 497 | Search retry: clear err before retry action |
| 498 | Search retry: clear errmsg before retry action |
| 499 | Search lane: SEARCH_ICON_RETRY marker |
| 500 | Dashgood retry Text Search |
| 501 | Dashgood retry Search settle wait |
| 502 | end Search error reset/retry |
| 503 | Dashgood pre-search-field wait |
| 504 | Search field: clear err |
| 505 | Search field: clear errmsg |
| 506 | Search field marker |
| 507 | Dashgood search_field action 1 |
| 508 | Dashgood search_field action 2 |
| 509 | Search field numeric error |
| 510 | Search field retry detail |
| 511 | Search field retry: clear err |
| 512 | Search field retry: clear errmsg |
| 513 | Dashgood search-field retry wait 1 |
| 514 | Dashgood retry Text Search for field recovery |
| 515 | Dashgood search-field retry wait 2 |
| 516 | Search field retry: clear err before field actions |
| 517 | Search field retry: clear errmsg before field actions |
| 518 | Search field retry marker |
| 519 | Dashgood retry search_field action 1 |
| 520 | Dashgood retry search_field action 2 |
| 521 | Dashgood retry search-field settle wait |
| 522 | end Search field retry |
| 523 | initialize pre-send UI failure flag |
| 524 | final Search field failure check |
| 525 | mark final Search field failure |
| 526 | save Search field failure |
| 527 | end final Search field failure check |
| 528 | search-key keyboard gate |
| 529 | search-key keyboard: clear err |
| 530 | search-key keyboard: clear errmsg |
| 531 | Dashgood pre-search-key wait |
| 532 | V15A exact keyboard search write |
| 533 | V15A search result settle wait |
| 534 | search-key keyboard error check |
| 535 | mark search-key keyboard failure |
| 536 | save search-key keyboard failure |
| 537 | end search-key keyboard error check |
| 538 | end search-key keyboard gate |
| 539 | contact selection gate |
| 540 | contact selection: clear err |
| 541 | contact selection: clear errmsg |
| 542 | contact selection marker |
| 543 | V15A exact contact List 1 |
| 544 | contact selection error check |
| 545 | mark contact selection failure |
| 546 | save contact selection failure |
| 547 | end contact selection error check |
| 548 | end contact selection gate |
| 549 | message-box gate |
| 550 | V15A post-contact settle wait |
| 551 | message box: clear err |
| 552 | message box: clear errmsg |
| 553 | message-box marker |
| 554 | V15A exact message-box focus |
| 555 | message-box focus error check |
| 556 | mark message-box focus failure |
| 557 | save message-box focus failure |
| 558 | end message-box focus error check |
| 559 | end message-box gate |
| 560 | reply keyboard gate |
| 561 | V15A pre-reply settle wait |
| 562 | reply keyboard: clear err |
| 563 | reply keyboard: clear errmsg |
| 564 | V15A exact clear-and-write reply keyboard action |
| 565 | V15A reply settle wait |
| 566 | reply keyboard error check |
| 567 | mark reply keyboard failure |
| 568 | save reply keyboard failure |
| 569 | end reply keyboard error check |
| 570 | end reply keyboard gate |
| 571 | pre-send UI failure route |
| 572 | pre-send UI failure: dirty UI |
| 573 | pre-send HOLD_PRE_SEND_FAILED write attempt 1: clear err |
| 574 | pre-send HOLD_PRE_SEND_FAILED write attempt 1: clear errmsg |
| 575 | pre-send HOLD_PRE_SEND_FAILED write: Update Cells attempt 1 |
| 576 | pre-send HOLD_PRE_SEND_FAILED write: assume attempt 1 success |
| 577 | pre-send HOLD_PRE_SEND_FAILED write: attempt 1 numeric error check |
| 578 | pre-send HOLD_PRE_SEND_FAILED write: attempt 1 failed |
| 579 | pre-send HOLD_PRE_SEND_FAILED write: end attempt 1 error check |
| 580 | pre-send HOLD_PRE_SEND_FAILED write: retry only after first failure |
| 581 | pre-send HOLD_PRE_SEND_FAILED write: exact 3 second retry wait |
| 582 | pre-send HOLD_PRE_SEND_FAILED write attempt 2: clear err |
| 583 | pre-send HOLD_PRE_SEND_FAILED write attempt 2: clear errmsg |
| 584 | pre-send HOLD_PRE_SEND_FAILED write: Update Cells attempt 2 |
| 585 | pre-send HOLD_PRE_SEND_FAILED write: assume attempt 2 success |
| 586 | pre-send HOLD_PRE_SEND_FAILED write: attempt 2 numeric error check |
| 587 | pre-send HOLD_PRE_SEND_FAILED write: attempt 2 failed |
| 588 | pre-send HOLD_PRE_SEND_FAILED write: end attempt 2 error check |
| 589 | pre-send HOLD_PRE_SEND_FAILED write: end retry |
| 590 | pre-send hold write succeeded |
| 591 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: clear verify_id array |
| 592 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: clear verify_sender array |
| 593 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: clear verify_message array |
| 594 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: clear verify_status array |
| 595 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: clear err |
| 596 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: clear errmsg |
| 597 | pre-send HOLD_PRE_SEND_FAILED readback: Get Data attempt 1 |
| 598 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: assume read valid |
| 599 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: numeric plugin error check |
| 600 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: plugin error invalidates read |
| 601 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: end plugin error check |
| 602 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_id count check |
| 603 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_id count invalid |
| 604 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: end verify_id count check |
| 605 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_id value check |
| 606 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_id value invalid |
| 607 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: end verify_id value check |
| 608 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_sender count check |
| 609 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_sender count invalid |
| 610 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: end verify_sender count check |
| 611 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_sender value check |
| 612 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_sender value invalid |
| 613 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: end verify_sender value check |
| 614 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_message count check |
| 615 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_message count invalid |
| 616 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: end verify_message count check |
| 617 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_message value check |
| 618 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_message value invalid |
| 619 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: end verify_message value check |
| 620 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_status count check |
| 621 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_status count invalid |
| 622 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: end verify_status count check |
| 623 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_status value check |
| 624 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: verify_status value invalid |
| 625 | pre-send HOLD_PRE_SEND_FAILED readback attempt 1: end verify_status value check |
| 626 | pre-send HOLD_PRE_SEND_FAILED readback: retry only after first failure |
| 627 | pre-send HOLD_PRE_SEND_FAILED readback: exact 3 second retry wait |
| 628 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: clear verify_id array |
| 629 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: clear verify_sender array |
| 630 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: clear verify_message array |
| 631 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: clear verify_status array |
| 632 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: clear err |
| 633 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: clear errmsg |
| 634 | pre-send HOLD_PRE_SEND_FAILED readback: Get Data attempt 2 |
| 635 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: assume read valid |
| 636 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: numeric plugin error check |
| 637 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: plugin error invalidates read |
| 638 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: end plugin error check |
| 639 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_id count check |
| 640 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_id count invalid |
| 641 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: end verify_id count check |
| 642 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_id value check |
| 643 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_id value invalid |
| 644 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: end verify_id value check |
| 645 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_sender count check |
| 646 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_sender count invalid |
| 647 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: end verify_sender count check |
| 648 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_sender value check |
| 649 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_sender value invalid |
| 650 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: end verify_sender value check |
| 651 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_message count check |
| 652 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_message count invalid |
| 653 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: end verify_message count check |
| 654 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_message value check |
| 655 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_message value invalid |
| 656 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: end verify_message value check |
| 657 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_status count check |
| 658 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_status count invalid |
| 659 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: end verify_status count check |
| 660 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_status value check |
| 661 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: verify_status value invalid |
| 662 | pre-send HOLD_PRE_SEND_FAILED readback attempt 2: end verify_status value check |
| 663 | pre-send HOLD_PRE_SEND_FAILED readback: end retry |
| 664 | pre-send HOLD_PRE_SEND_FAILED: default confirmation false |
| 665 | pre-send HOLD_PRE_SEND_FAILED: exact ID and status confirmation |
| 666 | pre-send HOLD_PRE_SEND_FAILED: confirmation passed |
| 667 | pre-send HOLD_PRE_SEND_FAILED: end exact confirmation |
| 668 | pre-send hold write failed |
| 669 | pre-send hold status unconfirmed |
| 670 | end pre-send hold write result |
| 671 | pre-send hold confirmed |
| 672 | pre-send UI failure result |
| 673 | pre-send UI failure detail |
| 674 | pre-send UI failure controller error |
| 675 | pre-send hold unconfirmed |
| 676 | pre-send unknown status result |
| 677 | pre-send unknown status detail |
| 678 | pre-send unknown controller error |
| 679 | end pre-send UI failure status result |
| 680 | pre-send UI failure: failed |
| 681 | pre-send UI failure: stop transaction |
| 682 | end pre-send UI failure route |
| 683 | final exact-once pre-Send gate |
| 684 | V15A pre-Send settle wait |
| 685 | Send button: clear err |
| 686 | Send button: clear errmsg |
| 687 | Send-button marker |
| 688 | V15A exact button_send node |
| 689 | latch possible Send click exactly once |
| 690 | ambiguous Send-button outcome |
| 691 | SEND_OUTCOME_UNKNOWN_REVIEW write attempt 1: clear err |
| 692 | SEND_OUTCOME_UNKNOWN_REVIEW write attempt 1: clear errmsg |
| 693 | SEND_OUTCOME_UNKNOWN_REVIEW write: Update Cells attempt 1 |
| 694 | SEND_OUTCOME_UNKNOWN_REVIEW write: assume attempt 1 success |
| 695 | SEND_OUTCOME_UNKNOWN_REVIEW write: attempt 1 numeric error check |
| 696 | SEND_OUTCOME_UNKNOWN_REVIEW write: attempt 1 failed |
| 697 | SEND_OUTCOME_UNKNOWN_REVIEW write: end attempt 1 error check |
| 698 | SEND_OUTCOME_UNKNOWN_REVIEW write: retry only after first failure |
| 699 | SEND_OUTCOME_UNKNOWN_REVIEW write: exact 3 second retry wait |
| 700 | SEND_OUTCOME_UNKNOWN_REVIEW write attempt 2: clear err |
| 701 | SEND_OUTCOME_UNKNOWN_REVIEW write attempt 2: clear errmsg |
| 702 | SEND_OUTCOME_UNKNOWN_REVIEW write: Update Cells attempt 2 |
| 703 | SEND_OUTCOME_UNKNOWN_REVIEW write: assume attempt 2 success |
| 704 | SEND_OUTCOME_UNKNOWN_REVIEW write: attempt 2 numeric error check |
| 705 | SEND_OUTCOME_UNKNOWN_REVIEW write: attempt 2 failed |
| 706 | SEND_OUTCOME_UNKNOWN_REVIEW write: end attempt 2 error check |
| 707 | SEND_OUTCOME_UNKNOWN_REVIEW write: end retry |
| 708 | ambiguous outcome write succeeded |
| 709 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: clear verify_id array |
| 710 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: clear verify_sender array |
| 711 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: clear verify_message array |
| 712 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: clear verify_status array |
| 713 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: clear err |
| 714 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: clear errmsg |
| 715 | SEND_OUTCOME_UNKNOWN_REVIEW readback: Get Data attempt 1 |
| 716 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: assume read valid |
| 717 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: numeric plugin error check |
| 718 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: plugin error invalidates read |
| 719 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: end plugin error check |
| 720 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_id count check |
| 721 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_id count invalid |
| 722 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: end verify_id count check |
| 723 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_id value check |
| 724 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_id value invalid |
| 725 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: end verify_id value check |
| 726 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_sender count check |
| 727 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_sender count invalid |
| 728 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: end verify_sender count check |
| 729 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_sender value check |
| 730 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_sender value invalid |
| 731 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: end verify_sender value check |
| 732 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_message count check |
| 733 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_message count invalid |
| 734 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: end verify_message count check |
| 735 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_message value check |
| 736 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_message value invalid |
| 737 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: end verify_message value check |
| 738 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_status count check |
| 739 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_status count invalid |
| 740 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: end verify_status count check |
| 741 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_status value check |
| 742 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: verify_status value invalid |
| 743 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 1: end verify_status value check |
| 744 | SEND_OUTCOME_UNKNOWN_REVIEW readback: retry only after first failure |
| 745 | SEND_OUTCOME_UNKNOWN_REVIEW readback: exact 3 second retry wait |
| 746 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: clear verify_id array |
| 747 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: clear verify_sender array |
| 748 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: clear verify_message array |
| 749 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: clear verify_status array |
| 750 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: clear err |
| 751 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: clear errmsg |
| 752 | SEND_OUTCOME_UNKNOWN_REVIEW readback: Get Data attempt 2 |
| 753 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: assume read valid |
| 754 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: numeric plugin error check |
| 755 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: plugin error invalidates read |
| 756 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: end plugin error check |
| 757 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_id count check |
| 758 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_id count invalid |
| 759 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: end verify_id count check |
| 760 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_id value check |
| 761 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_id value invalid |
| 762 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: end verify_id value check |
| 763 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_sender count check |
| 764 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_sender count invalid |
| 765 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: end verify_sender count check |
| 766 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_sender value check |
| 767 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_sender value invalid |
| 768 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: end verify_sender value check |
| 769 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_message count check |
| 770 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_message count invalid |
| 771 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: end verify_message count check |
| 772 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_message value check |
| 773 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_message value invalid |
| 774 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: end verify_message value check |
| 775 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_status count check |
| 776 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_status count invalid |
| 777 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: end verify_status count check |
| 778 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_status value check |
| 779 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: verify_status value invalid |
| 780 | SEND_OUTCOME_UNKNOWN_REVIEW readback attempt 2: end verify_status value check |
| 781 | SEND_OUTCOME_UNKNOWN_REVIEW readback: end retry |
| 782 | SEND_OUTCOME_UNKNOWN_REVIEW: default confirmation false |
| 783 | SEND_OUTCOME_UNKNOWN_REVIEW: exact ID and status confirmation |
| 784 | SEND_OUTCOME_UNKNOWN_REVIEW: confirmation passed |
| 785 | SEND_OUTCOME_UNKNOWN_REVIEW: end exact confirmation |
| 786 | ambiguous outcome write failed |
| 787 | ambiguous outcome status unconfirmed |
| 788 | end ambiguous outcome write result |
| 789 | ambiguous Send result |
| 790 | ambiguous Send never claims confirmed send |
| 791 | ambiguous Send requires review |
| 792 | ambiguous Send detail |
| 793 | ambiguous Send controller error |
| 794 | ambiguous Send terminal |
| 795 | Send-button action returned without numeric error |
| 796 | V15A post-Send settle wait |
| 797 | SEND_CLICKED_AWAITING_CONFIRM write attempt 1: clear err |
| 798 | SEND_CLICKED_AWAITING_CONFIRM write attempt 1: clear errmsg |
| 799 | SEND_CLICKED_AWAITING_CONFIRM write: Update Cells attempt 1 |
| 800 | SEND_CLICKED_AWAITING_CONFIRM write: assume attempt 1 success |
| 801 | SEND_CLICKED_AWAITING_CONFIRM write: attempt 1 numeric error check |
| 802 | SEND_CLICKED_AWAITING_CONFIRM write: attempt 1 failed |
| 803 | SEND_CLICKED_AWAITING_CONFIRM write: end attempt 1 error check |
| 804 | SEND_CLICKED_AWAITING_CONFIRM write: retry only after first failure |
| 805 | SEND_CLICKED_AWAITING_CONFIRM write: exact 3 second retry wait |
| 806 | SEND_CLICKED_AWAITING_CONFIRM write attempt 2: clear err |
| 807 | SEND_CLICKED_AWAITING_CONFIRM write attempt 2: clear errmsg |
| 808 | SEND_CLICKED_AWAITING_CONFIRM write: Update Cells attempt 2 |
| 809 | SEND_CLICKED_AWAITING_CONFIRM write: assume attempt 2 success |
| 810 | SEND_CLICKED_AWAITING_CONFIRM write: attempt 2 numeric error check |
| 811 | SEND_CLICKED_AWAITING_CONFIRM write: attempt 2 failed |
| 812 | SEND_CLICKED_AWAITING_CONFIRM write: end attempt 2 error check |
| 813 | SEND_CLICKED_AWAITING_CONFIRM write: end retry |
| 814 | awaiting-confirm write succeeded |
| 815 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: clear verify_id array |
| 816 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: clear verify_sender array |
| 817 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: clear verify_message array |
| 818 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: clear verify_status array |
| 819 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: clear err |
| 820 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: clear errmsg |
| 821 | SEND_CLICKED_AWAITING_CONFIRM readback: Get Data attempt 1 |
| 822 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: assume read valid |
| 823 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: numeric plugin error check |
| 824 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: plugin error invalidates read |
| 825 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: end plugin error check |
| 826 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_id count check |
| 827 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_id count invalid |
| 828 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: end verify_id count check |
| 829 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_id value check |
| 830 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_id value invalid |
| 831 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: end verify_id value check |
| 832 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_sender count check |
| 833 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_sender count invalid |
| 834 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: end verify_sender count check |
| 835 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_sender value check |
| 836 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_sender value invalid |
| 837 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: end verify_sender value check |
| 838 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_message count check |
| 839 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_message count invalid |
| 840 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: end verify_message count check |
| 841 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_message value check |
| 842 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_message value invalid |
| 843 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: end verify_message value check |
| 844 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_status count check |
| 845 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_status count invalid |
| 846 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: end verify_status count check |
| 847 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_status value check |
| 848 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: verify_status value invalid |
| 849 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 1: end verify_status value check |
| 850 | SEND_CLICKED_AWAITING_CONFIRM readback: retry only after first failure |
| 851 | SEND_CLICKED_AWAITING_CONFIRM readback: exact 3 second retry wait |
| 852 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: clear verify_id array |
| 853 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: clear verify_sender array |
| 854 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: clear verify_message array |
| 855 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: clear verify_status array |
| 856 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: clear err |
| 857 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: clear errmsg |
| 858 | SEND_CLICKED_AWAITING_CONFIRM readback: Get Data attempt 2 |
| 859 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: assume read valid |
| 860 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: numeric plugin error check |
| 861 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: plugin error invalidates read |
| 862 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: end plugin error check |
| 863 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_id count check |
| 864 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_id count invalid |
| 865 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: end verify_id count check |
| 866 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_id value check |
| 867 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_id value invalid |
| 868 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: end verify_id value check |
| 869 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_sender count check |
| 870 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_sender count invalid |
| 871 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: end verify_sender count check |
| 872 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_sender value check |
| 873 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_sender value invalid |
| 874 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: end verify_sender value check |
| 875 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_message count check |
| 876 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_message count invalid |
| 877 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: end verify_message count check |
| 878 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_message value check |
| 879 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_message value invalid |
| 880 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: end verify_message value check |
| 881 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_status count check |
| 882 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_status count invalid |
| 883 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: end verify_status count check |
| 884 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_status value check |
| 885 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: verify_status value invalid |
| 886 | SEND_CLICKED_AWAITING_CONFIRM readback attempt 2: end verify_status value check |
| 887 | SEND_CLICKED_AWAITING_CONFIRM readback: end retry |
| 888 | SEND_CLICKED_AWAITING_CONFIRM: default confirmation false |
| 889 | SEND_CLICKED_AWAITING_CONFIRM: exact ID and status confirmation |
| 890 | SEND_CLICKED_AWAITING_CONFIRM: confirmation passed |
| 891 | SEND_CLICKED_AWAITING_CONFIRM: end exact confirmation |
| 892 | awaiting-confirm write failed |
| 893 | awaiting-confirm status unconfirmed |
| 894 | end awaiting-confirm write result |
| 895 | awaiting-confirm exact readback passed |
| 896 | successful click awaiting confirmation result |
| 897 | successful click is not confirmed send proof |
| 898 | awaiting-confirm state persisted |
| 899 | awaiting-confirm detail |
| 900 | awaiting-confirm controller state |
| 901 | awaiting-confirm update/readback failed |
| 902 | POST_SEND_STATUS_UPDATE_FAILED fallback write attempt 1: clear err |
| 903 | POST_SEND_STATUS_UPDATE_FAILED fallback write attempt 1: clear errmsg |
| 904 | POST_SEND_STATUS_UPDATE_FAILED fallback write: Update Cells attempt 1 |
| 905 | POST_SEND_STATUS_UPDATE_FAILED fallback write: assume attempt 1 success |
| 906 | POST_SEND_STATUS_UPDATE_FAILED fallback write: attempt 1 numeric error check |
| 907 | POST_SEND_STATUS_UPDATE_FAILED fallback write: attempt 1 failed |
| 908 | POST_SEND_STATUS_UPDATE_FAILED fallback write: end attempt 1 error check |
| 909 | POST_SEND_STATUS_UPDATE_FAILED fallback write: retry only after first failure |
| 910 | POST_SEND_STATUS_UPDATE_FAILED fallback write: exact 3 second retry wait |
| 911 | POST_SEND_STATUS_UPDATE_FAILED fallback write attempt 2: clear err |
| 912 | POST_SEND_STATUS_UPDATE_FAILED fallback write attempt 2: clear errmsg |
| 913 | POST_SEND_STATUS_UPDATE_FAILED fallback write: Update Cells attempt 2 |
| 914 | POST_SEND_STATUS_UPDATE_FAILED fallback write: assume attempt 2 success |
| 915 | POST_SEND_STATUS_UPDATE_FAILED fallback write: attempt 2 numeric error check |
| 916 | POST_SEND_STATUS_UPDATE_FAILED fallback write: attempt 2 failed |
| 917 | POST_SEND_STATUS_UPDATE_FAILED fallback write: end attempt 2 error check |
| 918 | POST_SEND_STATUS_UPDATE_FAILED fallback write: end retry |
| 919 | post-Send status failure result |
| 920 | post-Send status failure never claims confirmed send |
| 921 | post-Send status failure: failed |
| 922 | post-Send status failure detail |
| 923 | post-Send status failure controller error |
| 924 | end post-Send status outcome |
| 925 | successful/ambiguous Send branch terminal |
| 926 | end Send-button result branch |
| 927 | end final exact-once pre-Send gate |
| 928 | end TextNow reachability hard gate |
| 929 | end continue-after-exact-row-read transaction body |
| 930 | common owned-lock release |
| 931 | save final error before helper |
| 932 | release owned Send lock exactly once |
| 933 | restore final error after helper overwrite |
| 934 | clear local lock ownership |
| 935 | end common owned-lock release |
| 936 | permanent worker terminal stop |

### Task 224

| Action | Classified purpose |
| ---: | --- |
| 0 | Gate 9 authorization guard |
| 1 | Gate 9 launcher not armed |
| 2 | Gate 9 launcher not armed: no send |
| 3 | Gate 9 launcher not armed: stop |
| 4 | end Gate 9 authorization guard |
| 5 | consume one-time Gate 9 authorization |
| 6 | call permanent worker once for staged Gate 9 row |
| 7 | Gate 9 launcher stop after one call |

### Task 199

- Removed the old same-cycle repeat block formerly identified by source action identifiers `act73` through `act80`.
- Replaced the first selector call with one call carrying `%par1=QUEUE_CYCLE`.
- Expanded only the Send-result stop guard to recognize all permanent Plan A terminal results.
- Every action outside that Send block is semantically identical to the approved base.

## Exact-Once Proof

- Task 223 `button_send` nodes: 1.
- Loop or retry edge to `button_send`: 0.
- `%send_clicked=1` latch assignments after the node: 1.
- Maximum reachable Send clicks on every modeled path: 0 or 1.
- Common `SS Lock Release HARD` calls in Task 223: 1.
- Non-owned lock paths that call release: 0.
- Static Tasker block issues: 0.
- Maximum Task 223 If depth reported by the independent structure linter: 7.

## AutoSheets Proof

- Continue Task After Error is enabled on every new Get Data and Update Cells action.
- Numeric plugin errors use only `^[0-9]+$`.
- Broad `^.+$` error checks in Tasks 71/223: 0.
- Every exact-row Get Data clears all expected arrays and `%err/%errmsg` before each attempt.
- Exact-row array counts must equal 1; required values reject blank, unresolved-variable, and `#ERROR` content.
- Every retry wait is exactly 3 seconds; no operation has a third attempt.
- QueueView is a multi-row exception: all ten array dimensions must be equal and nonzero.
