from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict, deque
from pathlib import Path


EXPECTED_BASE_SHA = "58A5229EB7F6892C03AD799BB7A4C3144C59ACD4DEC0E5B2235F0AAF68EEF76B"
AUTHORIZED = {262, 273, 276, 278, 282, 284}
ADDED = set(range(309, 327))
PROTECTED = {68, 71, 170, 199, 223, 225, 226, 227, 230, 231, 233, 235, 248, 249, 250, 252, 254, 255, 256, 258, 259, 260, 263, 268, 269, 270, 272, 293, *range(295, 309)}
LEGACY = {27, 28, 69, 222}
PHONE_PROVEN = {71, 199, 223, 225, 226, 227, 230, 231}
STATES = {
    "GROUP_BINDING", "GROUP_BOUND", "GROUP_PROCESSING", "GROUP_REPLY_READY",
    "GROUP_SEND_AWAITING_CONFIRM", "GROUP_SEND_OUTCOME_REVIEW", "GROUP_ANCHOR_ARCHIVED",
    "GROUP_FINALIZING", "GROUP_COMPLETE", "GROUP_REVIEW",
}
HEADERS = [
    "SchemaVersion", "GroupID", "SenderKey", "AnchorSheet1Row", "AnchorOriginalID",
    "MemberCount", "Member1Row", "Member1OriginalID", "Member2Row", "Member2OriginalID",
    "Member3Row", "Member3OriginalID", "Member4Row", "Member4OriginalID", "GroupState",
    "QuietCutoffMs", "BoundAtMs", "ConfirmedReply", "RecoveryCount", "LastError",
    "LastUpdateMs", "ConfirmationState", "ArchiveState", "FinalizedMemberCount", "OwnerToken",
    "OwnerStartedAtMs", "LedgerRow", "FreezeLoggedAtMs", "HistoryReference", "HistoryTurnCount",
    "PromptReference", "TransitionSequence", "BoundMask", "ArchivedMask", "MemberCapacity",
    "ValidationRunContext", "Member1Message", "Member2Message", "Member3Message", "Member4Message",
    "SenderDisplay", "FixtureRole",
]


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


def task_names(tasks: dict[int, ET.Element]) -> dict[str, int]:
    return {task.findtext("nme", ""): task_id for task_id, task in tasks.items()}


def calls(tasks: dict[int, ET.Element]) -> dict[int, set[int]]:
    names = task_names(tasks)
    graph: dict[int, set[int]] = defaultdict(set)
    for task_id, task in tasks.items():
        for action in task.findall("Action"):
            if action.findtext("code") == "130":
                target = action.findtext("Str[@sr='arg0']", "")
                if target in names:
                    graph[task_id].add(names[target])
    return graph


def reachable(graph: dict[int, set[int]], roots: set[int]) -> set[int]:
    seen: set[int] = set()
    queue = deque(roots)
    while queue:
        node = queue.popleft()
        if node in seen:
            continue
        seen.add(node)
        queue.extend(graph.get(node, set()) - seen)
    return seen


def actions(task: ET.Element) -> list[ET.Element]:
    return sorted(task.findall("Action"), key=lambda node: int((node.get("sr") or "act-1")[3:]))


def perform_names(task: ET.Element) -> list[str]:
    return [a.findtext("Str[@sr='arg0']", "") for a in actions(task) if a.findtext("code") == "130"]


def plugin_parameters(action: ET.Element) -> dict[str, object] | None:
    node = action.find("Bundle/Vals/parameters")
    if node is None or not node.text:
        return None
    try:
        return json.loads(node.text)
    except json.JSONDecodeError:
        return None


def balanced(task: ET.Element) -> bool:
    stack: list[int] = []
    pairs = {38: 37, 40: 39}
    for action in actions(task):
        code = int(action.findtext("code", "-1"))
        if code in (37, 39):
            stack.append(code)
        elif code == 43:
            if not stack or stack[-1] != 37:
                return False
        elif code in pairs:
            if not stack or stack.pop() != pairs[code]:
                return False
    return not stack


def condition_index(task: ET.Element, text: str) -> int:
    for index, action in enumerate(actions(task)):
        if text in ET.tostring(action, encoding="unicode"):
            return index
    return -1


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
    base_raw = raw_blocks(base_text, "Task", r"<id>(\d+)</id>")
    candidate_raw = raw_blocks(candidate_text, "Task", r"<id>(\d+)</id>")
    base_profiles = raw_blocks(base_text, "Profile", r"<id>(\d+)</id>")
    candidate_profiles = raw_blocks(candidate_text, "Profile", r"<id>(\d+)</id>")
    base_scenes = {m.group(1): m.group(0) for m in re.finditer(r'<Scene sr="([^"]+)".*?</Scene>', base_text, re.DOTALL)}
    candidate_scenes = {m.group(1): m.group(0) for m in re.finditer(r'<Scene sr="([^"]+)".*?</Scene>', candidate_text, re.DOTALL)}
    graph = calls(candidate_tasks)
    production_reachable = reachable(graph, {199})
    validation_reachable = reachable(graph, {268})

    checks: list[dict[str, object]] = []

    def check(name: str, passed: bool, evidence: object) -> None:
        checks.append({"name": name, "pass": bool(passed), "evidence": evidence})

    changed = sorted(task_id for task_id in base_tasks if base_raw[task_id] != candidate_raw.get(task_id))
    added = sorted(set(candidate_tasks) - set(base_tasks))
    check("base_sha_exact", digest(base_bytes) == EXPECTED_BASE_SHA, digest(base_bytes))
    check("utf8_no_bom", not candidate_bytes.startswith(b"\xef\xbb\xbf"), None)
    check("xml_root_taskerdata", candidate_root.tag == "TaskerData", candidate_root.tag)
    check("existing_scope_exact", changed == sorted(AUTHORIZED), changed)
    check("helper_set_exact", added == sorted(ADDED), added)
    check("protected_raw_identical", all(base_raw[i] == candidate_raw[i] for i in PROTECTED | LEGACY), sorted(PROTECTED | LEGACY))
    check("phone_proven_raw_identical", all(base_raw[i] == candidate_raw[i] for i in PHONE_PROVEN), sorted(PHONE_PROVEN))
    check("profiles_raw_identical", base_profiles == candidate_profiles, len(candidate_profiles))
    check("scenes_raw_identical", base_scenes == candidate_scenes, len(candidate_scenes))

    ids = [int(task.findtext("id", "-1")) for task in candidate_root.findall("Task")]
    names = [task.findtext("nme", "") for task in candidate_root.findall("Task")]
    check("duplicate_task_ids_zero", len(ids) == len(set(ids)), len(ids) - len(set(ids)))
    check("duplicate_task_names_zero", len(names) == len(set(names)), len(names) - len(set(names)))
    check("all_control_stacks_balanced", all(balanced(task) for task in candidate_tasks.values()), [i for i, task in candidate_tasks.items() if not balanced(task)])

    helper_props = {
        i: {
            "name": candidate_tasks[i].findtext("nme"),
            "actions": len(actions(candidate_tasks[i])),
            "rty": candidate_tasks[i].findtext("rty"),
            "stayawake": candidate_tasks[i].findtext("stayawake"),
        }
        for i in sorted(ADDED)
    }
    check("helpers_below_500", all(v["actions"] < 500 for v in helper_props.values()), helper_props)
    check("helpers_explicit_collision", all(v["rty"] == "0" for v in helper_props.values()), helper_props)
    check("helpers_stay_awake", all(v["stayawake"] == "true" for v in helper_props.values()), helper_props)

    project = candidate_root.find("Project")
    project_ids = {int(v) for v in (project.findtext("tids", "") if project is not None else "").split(",") if v}
    check("helpers_registered", ADDED <= project_ids, sorted(ADDED - project_ids))
    profile_mids = {int(node.text) for profile in candidate_root.findall("Profile") for node in profile if re.fullmatch(r"mid\d+", node.tag) and node.text}
    scene_clicks = {int(node.text) for scene in candidate_root.findall("Scene") for node in scene.iter("clickTask") if node.text and not node.text.startswith("-")}
    check("helpers_no_profile_or_scene_callers", not (ADDED & (profile_mids | scene_clicks)), sorted(ADDED & (profile_mids | scene_clicks)))

    check("legacy_unreachable_from_production", not (LEGACY & production_reachable), sorted(LEGACY & production_reachable))
    check("legacy_unreachable_from_validation", not (LEGACY & validation_reachable), sorted(LEGACY & validation_reachable))
    check("task282_removed_legacy_group", "PROCESS Build Same Sender Group" not in perform_names(candidate_tasks[282]), perform_names(candidate_tasks[282]))
    check("task282_removed_old_prompt", "PROCESS Build Prompt" not in perform_names(candidate_tasks[282]), perform_names(candidate_tasks[282]))
    check("task282_uses_conversation_prepare_prompt", {"AIW Conversation Prepare Group", "AIW Conversation Prompt Build"} <= set(perform_names(candidate_tasks[282])), perform_names(candidate_tasks[282]))

    send_callers = sorted(i for i, task in candidate_tasks.items() if "FINAL Send Sheet" in perform_names(task))
    reachable_send_callers = sorted(set(send_callers) & production_reachable)
    check("one_reachable_send_caller", reachable_send_callers == [262], {"all": send_callers, "reachable": reachable_send_callers})
    check("protected_lifecycle_only_from_wrapper", {71, 227, 322} <= graph[262], sorted(graph[262]))

    task317_xml = candidate_raw[317]
    quiet_call = task317_xml.find("AIW Conversation Quiet Select")
    owner_call = task317_xml.find("AIW Conversation Owner")
    ledger_create = task317_xml.find("AIW Conversation Ledger Create")
    check("quiet_before_owner_and_ledger", 0 <= quiet_call < owner_call < ledger_create, {"quiet": quiet_call, "owner": owner_call, "ledger": ledger_create})
    quiet_plugins = [int(a.findtext("code", "-1")) for a in actions(candidate_tasks[309]) if int(a.findtext("code", "-1")) in (1810865467, 1461810131)]
    check("quiet_task_read_only", quiet_plugins and set(quiet_plugins) == {1810865467}, quiet_plugins)
    check("quiet_10_second_cutoff", "%AIWConversationNewestLoggedAt+10000" in task317_xml or "%AIWConversationNewestLoggedAt+10000" in candidate_raw[309], None)
    check("quiet_hold_exact", "CONVERSATION_QUIET_WAIT_HOLD" in candidate_raw[309], None)

    candidate_states = {state for state in STATES if state in candidate_text}
    check("all_group_states_present", candidate_states == STATES, sorted(STATES - candidate_states))
    check("group_capacity_four", "%AICGL_AI" in candidate_raw[313] and ">4</Str>" in candidate_raw[313] and "%AIWConversationMemberCount" in candidate_raw[309], None)
    check("member_messages_durable", all(header in candidate_raw[324] for header in HEADERS[36:40]), HEADERS[36:40])
    check("exact_schema_version", "AIW_CONVERSATION_V1" in candidate_text, None)
    check("all_schema_headers_present", all(header in candidate_raw[324] for header in HEADERS), [h for h in HEADERS if h not in candidate_raw[324]])
    check("schema_before_start_in_task284", "AIW Conversation Schema Check" in perform_names(candidate_tasks[284]), perform_names(candidate_tasks[284]))

    pre_send = candidate_raw[320]
    check("pre_send_exact_member_reads", "AIW Conversation Member Verify" in pre_send and "CONVERSATION_PRE_SEND_STALE_HOLD" in pre_send, None)
    check("possible_click_lifecycle_only", "CONVERSATION_GROUP_LIFECYCLE_ONLY" in candidate_raw[262] and "GROUP_SEND_AWAITING_CONFIRM" in candidate_raw[321], None)
    task262_performs = [(index, action.findtext("Str[@sr='arg0']", "")) for index, action in enumerate(actions(candidate_tasks[262])) if action.findtext("code") == "130"]
    send_sheet_index = next(index for index, name in task262_performs if name == "FINAL Send Sheet")
    send_state_indices = [index for index, name in task262_performs if name == "AIW Conversation Send State"]
    post_send_router_indices = [index for index, name in task262_performs if name == "FINAL Queue Lifecycle Router" and index > send_sheet_index]
    check("send_state_persisted_before_router", len(send_state_indices) == 2 and len(post_send_router_indices) == 2 and all(any(send_sheet_index < state < router for state in send_state_indices) for router in post_send_router_indices), {"send": send_sheet_index, "state": send_state_indices, "router": post_send_router_indices})
    check("confirmation_before_finalization", "ARCHIVE_DONE_VERIFIED" in candidate_raw[262] and "AIW Conversation Finalize Companions" in candidate_raw[262], None)
    check("finalizer_calls_protected_archive", "FINAL Archive One Bound Row" in perform_names(candidate_tasks[322]), perform_names(candidate_tasks[322]))
    check("complete_only_after_companion_archive", candidate_raw[322].find("FINAL Archive One Bound Row") < candidate_raw[322].rfind("GROUP_COMPLETE"), None)
    check("recovery_no_send_call", "FINAL Send Sheet" not in perform_names(candidate_tasks[323]), perform_names(candidate_tasks[323]))
    check("recovery_handles_partial_states", all(v in candidate_raw[323] for v in ("GROUP_BINDING", "GROUP_PROCESSING", "GROUP_FINALIZING", "GROUP_REVIEW")), None)

    check("history_sender_isolation", "PROCESS Normalize Sender" in perform_names(candidate_tasks[318]) and "%AIWConversationSenderKey" in candidate_raw[318], None)
    check("history_done_and_reply_filter", "DONE" in candidate_raw[318] and "%cgh_e" in candidate_raw[318], None)
    check("history_latest_five", all(f"%cgh_turn{i}" in candidate_raw[318] for i in range(1, 6)), None)
    check("history_character_cap", ".{0,3000}" in candidate_raw[318], None)
    check("grouped_history_collapse", "%cgh_seen_groups" in candidate_raw[318] and "GROUP_COMPLETE" in candidate_raw[318], None)
    check("archive_failure_holds_before_openai", "CONVERSATION_HISTORY_ARCHIVE_READ_HOLD" in candidate_raw[318] and condition_index(candidate_tasks[282], "PSBuildPromptOk") < condition_index(candidate_tasks[282], "PROCESS OpenAI Bounded Retry"), None)

    new_plugin_issues: list[dict[str, object]] = []
    for task_id in sorted(ADDED):
        task_actions = actions(candidate_tasks[task_id])
        for index, action in enumerate(task_actions):
            code = int(action.findtext("code", "-1"))
            if code not in (1810865467, 1461810131):
                continue
            params = plugin_parameters(action)
            if params is None:
                new_plugin_issues.append({"task": task_id, "action": index, "issue": "parameters"})
                continue
            raw = json.dumps(params, sort_keys=True)
            if '"createSheetIfNeeded": true' in raw or '"updateLaterIfOffline": true' in raw:
                new_plugin_issues.append({"task": task_id, "action": index, "issue": "unsafe_write_setting"})
            preceding = ET.tostring(candidate_tasks[task_id], encoding="unicode")
            if "%err" not in preceding or "%errmsg" not in preceding:
                new_plugin_issues.append({"task": task_id, "action": index, "issue": "error_route_missing"})
            if code == 1810865467 and action.findtext("se") == "true":
                new_plugin_issues.append({"task": task_id, "action": index, "issue": "continue_after_error_disabled"})
    check("new_plugin_settings_safe", not new_plugin_issues, new_plugin_issues)
    check("bounded_attempt_literal", all("1,2" in candidate_raw[i] for i in (309, 311, 312, 313, 314, 318, 320, 322, 324, 325, 326)), None)
    check("numeric_error_detection", all("^[1-9][0-9]*$" in candidate_raw[i] for i in (309, 311, 312, 313, 314, 318, 320, 322, 324, 325, 326)), None)

    forbidden_literals: list[dict[str, object]] = []
    for task_id in AUTHORIZED | ADDED:
        for action in actions(candidate_tasks[task_id]):
            for node in action.findall("Str"):
                value = node.text or ""
                if value in {"144", "145", "146", "147", "999", "999999999999990001", "999999999999990002"}:
                    forbidden_literals.append({"task": task_id, "action": action.get("sr"), "value": value})
            params = plugin_parameters(action)
            if params and re.search(r"(?<![0-9])(144|145|146|147|999)(?![0-9])", json.dumps(params)):
                forbidden_literals.append({"task": task_id, "action": action.get("sr"), "value": "plugin_range"})
    check("no_forbidden_fixture_literals", not forbidden_literals, forbidden_literals)
    check("no_default_group_row", "ConversationGroupSlotView" in candidate_raw[313] and "A%AIWConversationLedgerRow" in candidate_raw[313], None)
    bounded_direct = {
        311: "AIWConversationGroupMax" in candidate_raw[311],
        312: "AIWConversationGroupMax" in candidate_raw[312],
        313: "AIWConversationGroupMax" in candidate_raw[313],
        316: "AIW Conversation Ledger Read Exact" in candidate_raw[316],
        324: "ConversationSchemaCheck" in candidate_raw[324] and "A1:AP1" in candidate_raw[324],
        326: "AIW Conversation Ledger Read Exact" in candidate_raw[326] and "AIWConversationArchiveMax" in candidate_raw[326],
    }
    check("bounds_before_direct_reads", all(bounded_direct.values()), bounded_direct)

    text_markers = {marker: candidate_text.count(marker) for marker in ("Â§", "Ã", "�")}
    check("mojibake_zero", all(count == 0 for count in text_markers.values()), text_markers)
    check("section_sign_preserved_and_source_proven_extensions_only", candidate_text.count("§") >= base_text.count("§"), {"base": base_text.count("§"), "candidate": candidate_text.count("§")})
    check("openai_key_marker_preserved", candidate_text.count("%OpenAIKey") == base_text.count("%OpenAIKey"), {"base": base_text.count("%OpenAIKey"), "candidate": candidate_text.count("%OpenAIKey")})
    base_secret_like = {hashlib.sha256(v.encode()).hexdigest() for v in re.findall(r"sk-[A-Za-z0-9_-]{20,}", base_text)}
    candidate_secret_like = {hashlib.sha256(v.encode()).hexdigest() for v in re.findall(r"sk-[A-Za-z0-9_-]{20,}", candidate_text)}
    check("no_literal_openai_secret_pattern_added", candidate_secret_like == base_secret_like, {"base_count": len(base_secret_like), "candidate_count": len(candidate_secret_like)})
    check("notification_ingress_raw_identical", base_raw[68] == candidate_raw[68], None)

    notification_strings = [node.text or "" for action in actions(candidate_tasks[68]) for node in action.findall("Str")]
    profile_text = "\n".join(ET.tostring(profile, encoding="unicode") for profile in candidate_root.findall("Profile"))
    source_identifier_candidates = {
        "%anid", "%ankey", "%antag", "%anwhen", "%anwhentime", "%anconversation", "%anextras",
        "%anpackage", "%anuserid", "%antouchaction", "%anbutton1action", "%antitle", "%antext", "%anticker",
    }
    exposed = sorted(value for value in source_identifier_candidates if value in profile_text)
    consumed = sorted({v for v in notification_strings if v in {"%antitle", "%antext", "%anticker", "%antouchaction", "%anbutton1action", "%TIMEMS"}})
    transport = {
        "available_or_candidate_source_identifiers": exposed,
        "currently_consumed_source_fields": consumed,
        "source_to_original_id_mapping": "%SNid = %TIMEMS + %evt_r1 + %evt_r2; both random values are six digits",
        "stable_replay_identity_proven": False,
        "later_repeat_distinct_identity": "generated random identity normally differs but is not a source-proven delivery identity",
        "phase2_hold": True,
    }
    check("transport_identity_audit_complete", {"%anid", "%ankey", "%antag", "%anwhen", "%anwhentime"} <= set(exposed) and {"%antitle", "%antext", "%anticker", "%antouchaction", "%anbutton1action", "%TIMEMS"} <= set(consumed), transport)

    oversized = [
        {"task_id": task_id, "name": task.findtext("nme"), "actions": len(actions(task)), "new": task_id in ADDED}
        for task_id, task in sorted(candidate_tasks.items()) if len(actions(task)) > 500
    ]
    check("no_new_oversized_helper", not any(item["new"] for item in oversized), oversized)

    failures = [item for item in checks if not item["pass"]]
    report = {
        "status": "PASS" if not failures else "FAIL",
        "base": {"file": args.base.name, "bytes": len(base_bytes), "sha256": digest(base_bytes)},
        "candidate": {"file": args.candidate.name, "bytes": len(candidate_bytes), "sha256": digest(candidate_bytes)},
        "topology": {"tasks": len(candidate_tasks), "profiles": len(candidate_root.findall("Profile")), "scenes": len(candidate_root.findall("Scene")), "actions": sum(len(actions(task)) for task in candidate_tasks.values())},
        "changed_existing": changed,
        "added_helpers": helper_props,
        "production_reachable": sorted(production_reachable),
        "validation_reachable": sorted(validation_reachable),
        "transport_identity_audit": transport,
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
