# Static Audit of Included Reference XML

This is an audit of the raw included reference file, not a final Build100 runtime.

```json
{
  "main_xml_found": true,
  "sha256": "a75f90a37c0f698eabd8ec3aabe9158beffa3a63eaffda65ed0dc44aad3a2413",
  "size_bytes": 2733880,
  "xml_parse": {
    "status": "PASS",
    "root": "TaskerData"
  },
  "task_tag_count": 211,
  "profile_tag_count": 4,
  "scene_tag_count": 2,
  "duplicate_task_id_count": 0,
  "duplicate_name_count_estimate": 0,
  "BUILD95_marker_count": 2,
  "BUILD99_marker_count": 1,
  "BUILD100_marker_count": 0,
  "PATCH83_marker_count": 0,
  "json_true_count": 0,
  "se_true_count": 0,
  "mojibake_A_count": 0,
  "section_sign_count": 443,
  "openai_key_marker_present": true,
  "tasker_root_present": true,
  "textnow_trigger_present": true,
  "auto_live_tick_present": true,
  "send_wait_1000_present": true,
  "aiw_watchdog_present": false,
  "failure_ledger_present": false,
  "regression_ledger_present": false
}
```

Interpretation:
- The raw reference is preserved.
- It still shows old Build95/Build99/Build100/Patch83 marker state as listed above.
- Codex must fix labels in the new Build100 candidate.
- Key marker presence is reported only as present/absent. Secret values are not printed.
