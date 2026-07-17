from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict, deque
from pathlib import Path


EXPECTED_BASE_SHA = "D69480C9A212430D5D46753E3A05CBF4DB52045A6A8F967605BD3A3631CAB66E"
AUTHORIZED = {263, 273, 282, 309, 317, 320, 324, 325}
ADDED = {327}
PHONE_PROVEN = {71, 199, 223, 225, 226, 227, 230, 231}
JOURNAL_RESOLUTION = {254, 255}
PROTECTED_CONVERSATION = ({262, 276, 278, 284} | set(range(310, 317)) |
                          set(range(318, 327))) - AUTHORIZED
FIXTURE_HELPERS = {268, 293} | set(range(295, 309))
LEGACY = {27, 28, 69, 222}
LIFECYCLE_STATES = {
    "GROUP_REPLY_READY", "GROUP_SEND_AWAITING_CONFIRM",
    "GROUP_SEND_OUTCOME_REVIEW", "GROUP_ANCHOR_ARCHIVED", "GROUP_FINALIZING",
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def raw_blocks(text: str, tag: str, key_pattern: str) -> dict[int, str]:
    result: dict[int, str] = {}
    for match in re.finditer(rf"<{tag}\b.*?</{tag}>", text, re.DOTALL):
        key = re.search(key_pattern, match.group(0), re.DOTALL)
        if key:
            result[int(key.group(1))] = match.group(0)
    return result


def task_map(root: ET.Element) -> dict[int, ET.Element]:
    return {int(task.findtext("id", "-1")): task for task in root.findall("Task")}


def action_number(action: ET.Element) -> int:
    return int((action.get("sr") or "act-1")[3:])


def actions(task: ET.Element) -> list[ET.Element]:
    return sorted(task.findall("Action"), key=action_number)


def task_names(tasks: dict[int, ET.Element]) -> dict[str, int]:
    return {task.findtext("nme", ""): task_id for task_id, task in tasks.items()}


def performs(task: ET.Element) -> list[tuple[int, str]]:
    return [
        (action_number(action), action.findtext("Str[@sr='arg0']", ""))
        for action in actions(task) if action.findtext("code") == "130"
    ]


def graph(tasks: dict[int, ET.Element]) -> dict[int, set[int]]:
    by_name = task_names(tasks)
    result: dict[int, set[int]] = defaultdict(set)
    for task_id, task in tasks.items():
        for _, target in performs(task):
            if target in by_name:
                result[task_id].add(by_name[target])
    return result


def reachable(call_graph: dict[int, set[int]], roots: set[int]) -> set[int]:
    found: set[int] = set()
    pending = deque(roots)
    while pending:
        node = pending.popleft()
        if node in found:
            continue
        found.add(node)
        pending.extend(call_graph.get(node, set()) - found)
    return found


def balanced(task: ET.Element) -> bool:
    stack: list[int] = []
    for action in actions(task):
        code = int(action.findtext("code", "-1"))
        if code in (37, 39):
            stack.append(code)
        elif code == 43:
            if not stack or stack[-1] != 37:
                return False
        elif code == 38:
            if not stack or stack.pop() != 37:
                return False
        elif code == 40:
            if not stack or stack.pop() != 39:
                return False
    return not stack


def plugin_parameters(action: ET.Element) -> dict[str, object] | None:
    text = action.findtext("Bundle/Vals/parameters")
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def decoded_text(node: ET.Element) -> str:
    """Flatten decoded XML node text so regex metacharacters are not entity-escaped."""
    return "\n".join(value for element in node.iter() if (value := element.text))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()

    base_bytes = args.base.read_bytes()
    candidate_bytes = args.candidate.read_bytes()
    base_text = base_bytes.decode("utf-8")
    candidate_text = candidate_bytes.decode("utf-8")
    base_root = ET.fromstring(base_bytes)
    candidate_root = ET.fromstring(candidate_bytes)
    base_tasks = task_map(base_root)
    candidate_tasks = task_map(candidate_root)
    task_text = {task_id: decoded_text(task) for task_id, task in candidate_tasks.items()}
    base_raw = raw_blocks(base_text, "Task", r"<id>(\d+)</id>")
    candidate_raw = raw_blocks(candidate_text, "Task", r"<id>(\d+)</id>")
    base_profiles = raw_blocks(base_text, "Profile", r"<id>(\d+)</id>")
    candidate_profiles = raw_blocks(candidate_text, "Profile", r"<id>(\d+)</id>")
    base_scenes = {m.group(1): m.group(0) for m in re.finditer(r'<Scene sr="([^"]+)".*?</Scene>', base_text, re.DOTALL)}
    candidate_scenes = {m.group(1): m.group(0) for m in re.finditer(r'<Scene sr="([^"]+)".*?</Scene>', candidate_text, re.DOTALL)}
    changed = sorted(task_id for task_id in base_tasks if base_raw[task_id] != candidate_raw.get(task_id))
    added = sorted(set(candidate_tasks) - set(base_tasks))
    protected = PHONE_PROVEN | JOURNAL_RESOLUTION | PROTECTED_CONVERSATION | FIXTURE_HELPERS | LEGACY
    call_graph = graph(candidate_tasks)
    production = reachable(call_graph, {199})
    validation = reachable(call_graph, {268})

    checks: list[dict[str, object]] = []

    def check(name: str, passed: bool, evidence: object = None) -> None:
        checks.append({"name": name, "pass": bool(passed), "evidence": evidence})

    check("base_sha_exact", digest(base_bytes) == EXPECTED_BASE_SHA, digest(base_bytes))
    check("candidate_utf8_no_bom", not candidate_bytes.startswith(b"\xef\xbb\xbf"))
    check("xml_root_taskerdata", candidate_root.tag == "TaskerData", candidate_root.tag)
    check("existing_change_scope_exact", changed == sorted(AUTHORIZED), changed)
    check("added_helper_exact", added == sorted(ADDED), added)
    check("protected_tasks_raw_identical", all(base_raw[i] == candidate_raw[i] for i in protected), sorted(protected))
    check("all_unauthorized_existing_raw_identical", all(base_raw[i] == candidate_raw[i] for i in set(base_tasks) - AUTHORIZED), len(base_tasks) - len(AUTHORIZED))
    check("profiles_raw_identical", base_profiles == candidate_profiles, len(candidate_profiles))
    check("scenes_raw_identical", base_scenes == candidate_scenes, len(candidate_scenes))
    check("duplicate_task_ids_zero", len(candidate_tasks) == len(set(candidate_tasks)), len(candidate_tasks))
    names = [task.findtext("nme", "") for task in candidate_tasks.values()]
    check("duplicate_task_names_zero", len(names) == len(set(names)), len(names) - len(set(names)))
    check("control_stacks_balanced", all(balanced(task) for task in candidate_tasks.values()), [i for i, t in candidate_tasks.items() if not balanced(t)])

    project = candidate_root.find("Project")
    project_ids = {int(v) for v in (project.findtext("tids", "") if project is not None else "").split(",") if v}
    profile_refs = {int(node.text) for profile in candidate_root.findall("Profile") for node in profile if re.fullmatch(r"mid\d+", node.tag) and node.text}
    scene_refs = {int(node.text) for scene in candidate_root.findall("Scene") for node in scene.iter("clickTask") if node.text and not node.text.startswith("-")}
    helper = candidate_tasks[327]
    helper_info = {
        "name": helper.findtext("nme"), "actions": len(actions(helper)),
        "rty": helper.findtext("rty"), "stayawake": helper.findtext("stayawake"),
    }
    check("helper_below_500", helper_info["actions"] < 500, helper_info)
    check("helper_abort_existing_collision", helper_info["rty"] == "1", helper_info)
    check("helper_stay_awake", helper_info["stayawake"] == "true", helper_info)
    check("helper_registered", 327 in project_ids)
    check("helper_no_profile_scene_caller", 327 not in profile_refs | scene_refs)
    check("helper_only_runtime_caller_task263", sorted(i for i, targets in call_graph.items() if 327 in targets) == [263])

    order263 = performs(candidate_tasks[263])
    names263 = [name for _, name in order263]
    required_order = [
        "AIW Ingress Journal Drain One", "AIW Overflow Drain Transaction",
        "AIW Integrated Process One", "AIW Conversation Deferred Recheck",
        "AIW Protected Send Confirm Archive One",
    ]
    indexes263 = [names263.index(name) for name in required_order]
    check("task263_exact_source_order", indexes263 == sorted(indexes263), list(zip(required_order, indexes263)))
    raw263 = candidate_raw[263]
    text263 = task_text[263]
    quiet_pos = text263.find("CONVERSATION_QUIET_WAIT_HOLD")
    defer_pos = text263.find("AIW Conversation Deferred Recheck")
    broad_exit_pos = text263.find("HOLD|ERROR")
    lifecycle_pos = text263.find("^(CONVERSATION_GROUP_LIFECYCLE_ONLY|CONVERSATION_GROUP_REVIEW_ONLY)$")
    lifecycle_call_pos = text263.find("AIW Protected Send Confirm Archive One")
    check("quiet_branch_before_broad_exit", 0 <= quiet_pos < defer_pos < broad_exit_pos, {"quiet": quiet_pos, "defer": defer_pos, "broad_exit": broad_exit_pos})
    check("lifecycle_result_surfaces_after_task262", 0 <= lifecycle_call_pos < lifecycle_pos and names263.count("AIW Protected Send Confirm Archive One") == 1, {"task262": lifecycle_call_pos, "result_surface": lifecycle_pos})
    check("task263_quiet_branch_stops_before_broad_exit", "CONVERSATION_QUIET_WAIT_HOLD" in text263 and "HOLD|ERROR" in text263)

    order282 = performs(candidate_tasks[282])
    check("task282_lifecycle_gate_before_queue_selection", order282[0][1] == "AIW Conversation Prepare Group" and order282[1][1] == "PROCESS Queue Health", order282[:4])
    raw282 = candidate_raw[282]
    check("task282_zero_new_work_on_lifecycle_result", raw282.find("CONVERSATION_GROUP_(LIFECYCLE|REVIEW)_ONLY") < raw282.find("PROCESS Queue Health"), None)
    check("task282_no_legacy_group_tasks", not ({"PROCESS Build Same Sender Group", "PROCESS Mark Grouped Rows"} & {name for _, name in order282}), order282)

    raw317 = candidate_raw[317]
    check("active_group_detection_before_quiet_selection", raw317.find("LIFECYCLE_GATE") < raw317.find("AIW Conversation Quiet Select"), None)
    check("lifecycle_states_complete", all(state in raw317 for state in LIFECYCLE_STATES), sorted(state for state in LIFECYCLE_STATES if state not in raw317))
    check("lifecycle_result_non_hold", "CONVERSATION_GROUP_LIFECYCLE_ONLY" in raw317 and "CONVERSATION_ACTIVE_GROUP_BUSY_HOLD" not in raw317)
    check("review_result_non_sendable_non_hold", "CONVERSATION_GROUP_REVIEW_ONLY" in raw317)
    check("second_group_rejected", "CONVERSATION_ACTIVE_GROUP_RECOVERY_HOLD" in raw317)

    raw309 = candidate_raw[309]
    text309 = task_text[309]
    check("selected_member_requires_admitted_status", "^(RESOLVED_MAIN|RESOLVED_OVERFLOW)$" in text309)
    check("selected_member_rejects_journaled_only", "JOURNALED" not in text309)
    check("journal_source_textnow_exact", "TEXTNOW" in text309)
    check("journal_exact_one_id_match", all(f"%cgq_idmatch{i}" in text309 for i in range(1, 5)))
    check("journal_exact_one_valid_match", all(f"%cgq_valid{i}" in text309 for i in range(1, 5)))
    check("journal_sender_message_normalization", all(v in text309 for v in ("%AIWConversationMemberSender", "%AIWConversationMemberMessage", "PROCESS Normalize Sender")))
    check("journal_loggedat_numeric", "^[0-9]+$" in text309)
    check("quiet_cutoff_persisted_source_timestamp", "%AIWConversationNewestLoggedAt+10000" in text309)
    check("quiet_wait_sets_deferred_contract", all(v in text309 for v in ("%AIWConversationQuietRecheckCutoff", "%AIWConversationQuietRecheckSender", "CONVERSATION_QUIET_WAIT_HOLD")))

    raw320 = candidate_raw[320]
    text320 = task_text[320]
    check("freshness_recognizes_unresolved_journaled", "JOURNALED" in text320 and "CONVERSATION_PRE_SEND_STALE_HOLD" in text320)
    check("freshness_recognizes_resolved_active_rows", "^(RESOLVED_MAIN|RESOLVED_OVERFLOW)$" in text320 and "PROCESS Load Queue Globals" in text320 and "OverflowInbox" in text320)
    check("freshness_exact_one_journal_match", "%cgfq_idmatches" in text320 and "%cgfq_valid" in text320 and "%cgfoa_idmatches" in text320 and "%cgfoa_valid" in text320)
    check("freshness_historical_resolved_not_global_block", "A2:N%AIWConversationJournalMax" in text320 and "CONVERSATION_PRE_SEND_STALE_HOLD" in text320)
    check("freshness_wrong_contract_reviews", "PRE_SEND_JOURNAL_CONTRACT_REVIEW" in text320)

    raw325 = candidate_raw[325]
    check("validation_real_journal_progression", all(mode in raw325 for mode in ("PRE_JOURNALED", "ADMITTED", "POST")))
    check("validation_exact_status_progression", all(status in raw325 for status in ("JOURNALED", "RESOLVED_MAIN", "RESOLVED_OVERFLOW")))
    raw273 = candidate_raw[273]
    check("phase4_calls_progression_modes", all(mode in raw273 for mode in ("PRE_JOURNALED", "ADMITTED", "POST")) and raw273.count("AIW Conversation Validation Audit") >= 3)

    raw327 = candidate_raw[327]
    text327 = task_text[327]
    check("deferred_wait_stop_aware", "%AIWorkerOn" in text327 and "%AIWStopRequested" in text327 and "CONVERSATION_QUIET_RECHECK_CANCELLED_STOP" in text327)
    check("deferred_wait_bounded", "%cgdr_tick" in text327 and "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15" in text327)
    check("deferred_wait_no_plugin_or_write", not any(int(a.findtext("code", "-1")) in (1810865467, 1461810131, 339, 344) for a in actions(helper)))
    check("deferred_wait_no_api_or_send", not ({"PROCESS OpenAI Bounded Retry", "FINAL Send Sheet"} & {name for _, name in performs(helper)}), performs(helper))
    check("deferred_wait_no_lock_acquire", all(v not in text327 for v in ("PROCESS Lock Acquire", "AIW Queue Owner", "AIW Conversation Owner")))
    check("deferred_wait_requires_all_locks_clear", all(v in text327 for v in ("%AIWQueueOwner", "%AIWConversationOwner", "%AIWProcessing", "%AIWSending", "%AIWConfirming", "%AIWArchiving")))
    check("deferred_wait_invokes_normal_cycle_once", [name for _, name in performs(helper)].count("AIW Integrated Queue Cycle") == 1)
    check("deferred_wait_inputs_fail_closed", all(v in text327 for v in ("CONVERSATION_QUIET_RECHECK_INPUT_HOLD", "CONVERSATION_QUIET_RECHECK_LOCK_HOLD", "CONVERSATION_QUIET_RECHECK_DEADLINE_HOLD")))

    raw324 = candidate_raw[324]
    text324 = task_text[324]
    check("schema_checks_group_slot_view", "ConversationGroupSlotView" in text324 and "ConversationSchemaCheck" in text324)
    check("schema_checks_group_bounds", all(v in text324 for v in ("%AIWConversationGroupPhysicalMax", "%AIWConversationGroupMax", "%AIWConversationArchiveMax", "%AIWConversationMainMax", "%AIWConversationJournalMax")))

    plugin_issues: list[dict[str, object]] = []
    for task_id in (309, 320, 324, 325):
        task_actions = actions(candidate_tasks[task_id])
        for position, action in enumerate(task_actions):
            code = int(action.findtext("code", "-1"))
            if code not in (1810865467, 1461810131):
                continue
            params = plugin_parameters(action)
            if params is None:
                plugin_issues.append({"task": task_id, "action": action.get("sr"), "issue": "invalid_parameters"})
                continue
            if params.get("createSheetIfNeeded") is True or params.get("updateLaterIfOffline") is True:
                plugin_issues.append({"task": task_id, "action": action.get("sr"), "issue": "unsafe_setting"})
            prefix = "".join(ET.tostring(a, encoding="unicode") for a in task_actions[max(0, position - 20):position])
            if "%err" not in prefix or "%errmsg" not in prefix:
                plugin_issues.append({"task": task_id, "action": action.get("sr"), "issue": "stale_error_not_cleared"})
            if code == 1810865467 and action.findtext("se") == "true":
                plugin_issues.append({"task": task_id, "action": action.get("sr"), "issue": "continue_after_error_disabled"})
    check("changed_plugin_settings_and_error_routing", not plugin_issues, plugin_issues)
    check("changed_reads_bounded_two_attempts", all("1,2" in candidate_raw[i] and "^[1-9][0-9]*$" in candidate_raw[i] for i in (309, 320, 324, 325)))

    send_callers = sorted(task_id for task_id, task in candidate_tasks.items() if "FINAL Send Sheet" in {name for _, name in performs(task)})
    reachable_send_callers = sorted(set(send_callers) & production)
    check("single_reachable_send_path_preserved", reachable_send_callers == [262], {"all": send_callers, "reachable": reachable_send_callers})
    check("task262_raw_identical", base_raw[262] == candidate_raw[262])
    check("tasks254_255_raw_identical", base_raw[254] == candidate_raw[254] and base_raw[255] == candidate_raw[255])
    check("legacy_unreachable", not (LEGACY & (production | validation)), sorted(LEGACY & (production | validation)))
    check("new_helper_reachable_only_via_task263", 327 in production and sorted(i for i, targets in call_graph.items() if 327 in targets) == [263], {"production": 327 in production, "validation": 327 in validation})

    forbidden_literals: list[dict[str, object]] = []
    for task_id in AUTHORIZED | ADDED:
        for action in actions(candidate_tasks[task_id]):
            for node in action.findall("Str"):
                if (node.text or "") in {"144", "145", "146", "147", "999", "999999999999990001", "999999999999990002"}:
                    forbidden_literals.append({"task": task_id, "action": action.get("sr"), "value": node.text})
    check("no_forbidden_fixture_literals", not forbidden_literals, forbidden_literals)
    mojibake = {marker: candidate_text.count(marker) for marker in ("Ã‚Â§", "Ãƒ", "ï¿½", "�")}
    check("mojibake_zero", not any(mojibake.values()), mojibake)
    check("source_section_sign_count_preserved_or_extended", candidate_text.count("Â§") >= base_text.count("Â§"), {"base": base_text.count("Â§"), "candidate": candidate_text.count("Â§")})
    check("secret_marker_count_unchanged", candidate_text.count("%OpenAIKey") == base_text.count("%OpenAIKey"))
    base_secrets = set(re.findall(r"sk-[A-Za-z0-9_-]{20,}", base_text))
    candidate_secrets = set(re.findall(r"sk-[A-Za-z0-9_-]{20,}", candidate_text))
    check("no_literal_secret_added", candidate_secrets == base_secrets, {"base": len(base_secrets), "candidate": len(candidate_secrets)})

    oversized = [
        {"task": task_id, "name": task.findtext("nme"), "actions": len(actions(task)), "added": task_id in ADDED}
        for task_id, task in sorted(candidate_tasks.items()) if len(actions(task)) > 500
    ]
    check("no_added_helper_over_500", not any(item["added"] for item in oversized), oversized)

    failures = [item for item in checks if not item["pass"]]
    report = {
        "status": "PASS" if not failures else "FAIL",
        "base": {"file": args.base.name, "bytes": len(base_bytes), "sha256": digest(base_bytes)},
        "candidate": {"file": args.candidate.name, "bytes": len(candidate_bytes), "sha256": digest(candidate_bytes)},
        "topology": {"tasks": len(candidate_tasks), "profiles": len(candidate_root.findall("Profile")), "scenes": len(candidate_root.findall("Scene")), "actions": sum(len(actions(task)) for task in candidate_tasks.values())},
        "changed_existing": changed,
        "added_helper": helper_info,
        "production_reachable": sorted(production),
        "validation_reachable": sorted(validation),
        "oversized_tasks": oversized,
        "checks": checks,
        "failures": failures,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "checks": len(checks), "failures": [f["name"] for f in failures], "candidate_sha256": digest(candidate_bytes)}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
