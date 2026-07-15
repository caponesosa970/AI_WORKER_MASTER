# Updated Static Test Matrix

Result: PASS

Prior Gate 12 cases: 57/57 PASS.

Tasker-substitution cases: 8/8 PASS.

Combined cases: 65/65 PASS.

| Case | Result |
| --- | --- |
| prior_01_invalid_task199_mode | PASS |
| prior_02_controlled_without_latch | PASS |
| prior_03_launcher_not_armed | PASS |
| prior_04_launcher_consumes_authorization | PASS |
| prior_05_launcher_calls_task199_once | PASS |
| prior_06_production_worker_off | PASS |
| prior_07_controlled_worker_off | PASS |
| prior_08_controlled_safe_mode_on | PASS |
| prior_09_production_busy | PASS |
| prior_10_controlled_busy | PASS |
| prior_11_router_bad_token | PASS |
| prior_12_send_lock | PASS |
| prior_13_confirmation_lock | PASS |
| prior_14_archive_lock | PASS |
| prior_15_processing_lock | PASS |
| prior_16_deadarchive_lock | PASS |
| prior_17_compactor_lock | PASS |
| prior_18_first_read_retry_succeeds | PASS |
| prior_19_both_reads_fail | PASS |
| prior_20_parallel_array_mismatch | PASS |
| prior_21_invalid_pending_row | PASS |
| prior_22_invalid_pending_id | PASS |
| prior_23_one_awaiting | PASS |
| prior_24_multiple_awaiting | PASS |
| prior_25_awaiting_plus_danger | PASS |
| prior_26_sending | PASS |
| prior_27_send_outcome_unknown_review | PASS |
| prior_28_post_send_status_update_failed | PASS |
| prior_29_hold_pre_send_failed | PASS |
| prior_30_one_done | PASS |
| prior_31_multiple_done_lowest | PASS |
| prior_32_awaiting_plus_done | PASS |
| prior_33_clear_plus_ready | PASS |
| prior_34_clear_no_ready | PASS |
| prior_35_confirm_success_no_archive | PASS |
| prior_36_confirm_failure_no_fallback | PASS |
| prior_37_archive_success_no_process_send | PASS |
| prior_38_archive_failure_no_send | PASS |
| prior_39_send_no_same_cycle_confirm | PASS |
| prior_40_controlled_no_process | PASS |
| prior_41_controlled_no_maintenance | PASS |
| prior_42_controlled_no_recursion | PASS |
| prior_43_production_handled_skips_process_send | PASS |
| prior_44_production_blocked_skips_process_send | PASS |
| prior_45_production_clear_retains_process | PASS |
| prior_46_one_task71_node | PASS |
| prior_47_one_task227_node | PASS |
| prior_48_one_task225_node | PASS |
| prior_49_one_task226_node | PASS |
| prior_50_no_broad_archive_call | PASS |
| prior_51_no_task75_call | PASS |
| prior_52_one_module_maximum | PASS |
| prior_53_owned_busy_release_once | PASS |
| prior_54_no_unowned_busy_release | PASS |
| prior_55_profiles_disabled | PASS |
| prior_56_protected_task_preservation | PASS |
| prior_57_no_private_tracked | PASS |
| sub_01_controlled_tokens_survive | PASS |
| sub_02_blank_normalizes_production | PASS |
| sub_03_unresolved_normalizes_production | PASS |
| sub_04_explicit_production_valid | PASS |
| sub_05_controlled_bad_token_rejected | PASS |
| sub_06_bad_mode_rejected | PASS |
| sub_07_dynamic_par_rhs_absent | PASS |
| sub_08_corrected_regex_exact | PASS |

Additional proof: the rejected behavior was reproduced by the same substitution model.

This is static evidence. It does not prove Tasker import/render or phone behavior.
