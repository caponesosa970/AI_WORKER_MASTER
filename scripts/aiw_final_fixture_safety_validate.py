from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict, deque
from pathlib import Path
from xml.dom import minidom


EXPECTED_BASE_SHA = "9FB3A33852E12475CFA9A5D97F1157F67C69A9C0A007025CCD026BC9E26EB2A5"
AUTHORIZED_EXISTING = {237, 268, 270, 272, 276, 293}
EXPECTED_HELPERS = {
    295: "AIW Validation Fixture Resolve Config",
    296: "AIW Validation Fixture Resolve Runtime",
    297: "AIW Validation Fixture Inspect Bound",
    298: "AIW Validation Fixture Contract",
    299: "AIW Validation Fixture Setup Exact",
    300: "AIW Validation Fixture Cleanup Bound",
    301: "AIW Validation Fixture Authorization Close",
    302: "AIW Validation Fixture Inspect Sheet1",
    303: "AIW Validation Fixture Inspect History",
    304: "AIW Validation Fixture Inspect Queue Stores",
    305: "AIW Validation Fixture Inspect Overflow",
    306: "AIW Validation Fixture Inspect Journal",
    307: "AIW Validation Fixture Read Sheet1",
    308: "AIW Validation Fixture Classify Sheet1",
}
DECLARED_REACHABLE_RUN_BOTH = {248, 263, 286}
CONFIG_ROLES = {
    "HIST_ARCHIVE", "HIST_DEAD", "G14C_REAL", "G14C_RATE", "G14C_TIMEOUT", "G14C_QUOTA", "G14C_LEGACY"
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def children(node, tag: str | None = None):
    out = [child for child in node.childNodes if child.nodeType == child.ELEMENT_NODE]
    return [child for child in out if child.tagName == tag] if tag else out


def first(node, tag: str):
    return next((child for child in children(node, tag)), None)


def text_of(node, tag: str, default: str = "") -> str:
    child = first(node, tag)
    if child is None:
        return default
    return "".join(part.data for part in child.childNodes if part.nodeType in (part.TEXT_NODE, part.CDATA_SECTION_NODE))


def string_arg(action, sr: str) -> str:
    for node in children(action, "Str"):
        if node.getAttribute("sr") == sr:
            return "".join(part.data for part in node.childNodes if part.nodeType in (part.TEXT_NODE, part.CDATA_SECTION_NODE))
    return ""


def int_arg(action, sr: str) -> str:
    for node in children(action, "Int"):
        if node.getAttribute("sr") == sr:
            return node.getAttribute("val")
    return ""


def action_index(action) -> int:
    match = re.fullmatch(r"act(\d+)", action.getAttribute("sr"))
    return int(match.group(1)) if match else -1


def raw_nodes(text: str, tag: str, key_pattern: str) -> dict[str, str]:
    pattern = rf'<{tag}\b[^>]*{key_pattern}.*?</{tag}>'
    out = {}
    for match in re.finditer(pattern, text, flags=re.DOTALL):
        key = re.search(key_pattern, match.group(0))
        if key:
            out[key.group(1)] = match.group(0)
    return out


def raw_tasks(text: str) -> dict[int, str]:
    return {int(k): v for k, v in raw_nodes(text, "Task", r'sr="task(\d+)"').items()}


def check(report: dict, name: str, passed: bool, detail=None) -> None:
    report["checks"][name] = {"pass": bool(passed), "detail": detail}


def build_graph(tasks_by_id: dict[int, object], tasks_by_name: dict[str, object]):
    graph: dict[int, set[int]] = defaultdict(set)
    callers: dict[int, set[int]] = defaultdict(set)
    missing = []
    actions_by_id = {}
    control_issues = []
    gaps = []
    duplicate_sr = []
    for task_id, task in tasks_by_id.items():
        actions = sorted(children(task, "Action"), key=action_index)
        actions_by_id[task_id] = actions
        indices = [action_index(action) for action in actions]
        if indices != list(range(len(actions))):
            gaps.append({"task": task_id, "indices": indices})
        if len(indices) != len(set(indices)):
            duplicate_sr.append(task_id)
        stack = []
        for action in actions:
            code = text_of(action, "code")
            if code == "37":
                stack.append("if")
            elif code == "43":
                if not stack or stack[-1] != "if":
                    control_issues.append({"task": task_id, "sr": action_index(action), "issue": "else_without_if"})
            elif code == "38":
                if not stack or stack[-1] != "if":
                    control_issues.append({"task": task_id, "sr": action_index(action), "issue": "endif_without_if"})
                else:
                    stack.pop()
            elif code == "39":
                stack.append("for")
            elif code == "40":
                if not stack or stack[-1] != "for":
                    control_issues.append({"task": task_id, "sr": action_index(action), "issue": "endfor_without_for"})
                else:
                    stack.pop()
            elif code == "130":
                target = string_arg(action, "arg0")
                if target in tasks_by_name:
                    target_id = int(text_of(tasks_by_name[target], "id"))
                    graph[task_id].add(target_id)
                    callers[target_id].add(task_id)
                elif target:
                    missing.append({"task": task_id, "target": target})
        if stack:
            control_issues.append({"task": task_id, "issue": "unclosed", "stack": stack})
    return graph, callers, actions_by_id, missing, gaps, duplicate_sr, control_issues


def reachable_from(graph: dict[int, set[int]], roots: set[int]) -> set[int]:
    seen = set()
    queue = deque(roots)
    while queue:
        value = queue.popleft()
        if value in seen:
            continue
        seen.add(value)
        queue.extend(graph.get(value, set()))
    return seen


def action_calls(actions, target: str) -> list[int]:
    return [index for index, action in enumerate(actions) if text_of(action, "code") == "130" and string_arg(action, "arg0") == target]


def plugin_properties(task_ids: set[int], actions_by_id: dict[int, list]) -> list[dict]:
    issues = []
    for task_id in task_ids:
        for action in actions_by_id[task_id]:
            code = text_of(action, "code")
            if code not in {"1810865467", "1461810131"}:
                continue
            rendered = action.toxml()
            if text_of(action, "se") != "false" or int_arg(action, "arg4") != "1":
                issues.append({"task": task_id, "sr": action_index(action), "issue": "continue_after_error"})
            if '"json":true' in rendered:
                issues.append({"task": task_id, "sr": action_index(action), "issue": "json_true"})
            if code == "1461810131" and ('"createSheetIfNeeded":true' in rendered or '"updateLaterIfOffline":true' in rendered):
                issues.append({"task": task_id, "sr": action_index(action), "issue": "unsafe_write_mode"})
    return issues


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
    base_dom = minidom.parseString(base_bytes)
    dom = minidom.parseString(candidate_bytes)
    root = dom.documentElement
    base_root = base_dom.documentElement

    report = {
        "validator": "fixture-safety-independent-minidom-v1",
        "source": {
            "base_filename": args.base.name,
            "base_bytes": len(base_bytes),
            "base_sha256": sha(base_bytes),
            "candidate_filename": args.candidate.name,
            "candidate_bytes": len(candidate_bytes),
            "candidate_sha256": sha(candidate_bytes),
        },
        "checks": {},
        "inventory": {},
    }
    check(report, "authorized_base_sha", sha(base_bytes) == EXPECTED_BASE_SHA, sha(base_bytes))
    check(report, "candidate_no_bom", not candidate_bytes.startswith(b"\xef\xbb\xbf"))
    check(report, "root_taskerdata", root.tagName == "TaskerData", root.tagName)

    tasks = children(root, "Task")
    base_tasks = children(base_root, "Task")
    task_ids = [int(text_of(task, "id", "-1")) for task in tasks]
    task_names = [text_of(task, "nme") for task in tasks]
    by_id = {int(text_of(task, "id")): task for task in tasks}
    by_name = {text_of(task, "nme"): task for task in tasks}
    base_by_id = {int(text_of(task, "id")): task for task in base_tasks}
    raw_base = raw_tasks(base_text)
    raw_candidate = raw_tasks(candidate_text)
    changed = {task_id for task_id in raw_base if raw_base[task_id] != raw_candidate.get(task_id)}
    added = set(raw_candidate) - set(raw_base)
    check(report, "duplicate_task_ids_zero", len(task_ids) == len(set(task_ids)), [k for k, v in Counter(task_ids).items() if v > 1])
    check(report, "duplicate_task_names_zero", len(task_names) == len(set(task_names)), [k for k, v in Counter(task_names).items() if v > 1])
    check(report, "changed_existing_exact_authorized", changed == AUTHORIZED_EXISTING, sorted(changed))
    check(report, "added_helpers_exact", added == set(EXPECTED_HELPERS), sorted(added))
    check(report, "helper_names_exact", all(text_of(by_id[task_id], "nme") == name for task_id, name in EXPECTED_HELPERS.items()), {str(task_id): text_of(by_id[task_id], "nme") for task_id in EXPECTED_HELPERS})
    helper_counts = {task_id: len(children(by_id[task_id], "Action")) for task_id in EXPECTED_HELPERS}
    check(report, "all_helpers_under_500_actions", all(count < 500 for count in helper_counts.values()), helper_counts)
    unchanged = set(raw_base) - AUTHORIZED_EXISTING
    check(report, "all_unauthorized_existing_tasks_byte_equal", all(raw_base[task_id] == raw_candidate[task_id] for task_id in unchanged), {"count": len(unchanged)})
    check(report, "task269_byte_equal", raw_base[269] == raw_candidate[269], sha(raw_candidate[269].encode("utf-8")))
    check(report, "task294_byte_equal", raw_base[294] == raw_candidate[294], sha(raw_candidate[294].encode("utf-8")))

    base_profiles = raw_nodes(base_text, "Profile", r'sr="prof(\d+)"')
    candidate_profiles = raw_nodes(candidate_text, "Profile", r'sr="prof(\d+)"')
    base_scenes = raw_nodes(base_text, "Scene", r'sr="([^"]+)"')
    candidate_scenes = raw_nodes(candidate_text, "Scene", r'sr="([^"]+)"')
    check(report, "profiles_raw_byte_equal", base_profiles == candidate_profiles, sorted(candidate_profiles))
    check(report, "scenes_raw_byte_equal", base_scenes == candidate_scenes, sorted(candidate_scenes))
    base_project = re.search(r"<Project\b.*?</Project>", base_text, flags=re.DOTALL).group(0)
    candidate_project = re.search(r"<Project\b.*?</Project>", candidate_text, flags=re.DOTALL).group(0)
    suffix = "," + ",".join(str(task_id) for task_id in sorted(EXPECTED_HELPERS))
    check(report, "project_registry_only_helper_tids_added", candidate_project.replace(suffix, "", 1) == base_project, suffix)

    graph, callers, actions_by_id, missing, gaps, duplicate_sr, control_issues = build_graph(by_id, by_name)
    reachable = reachable_from(graph, {268})
    check(report, "perform_task_refs_complete", not missing, missing)
    check(report, "action_indices_contiguous", not gaps, gaps)
    check(report, "duplicate_action_sr_zero", not duplicate_sr, duplicate_sr)
    check(report, "control_stacks_balanced", not control_issues, control_issues)
    check(report, "task294_unreachable_from_orchestrator", 294 not in reachable, sorted(callers.get(294, set())))
    check(report, "task294_has_no_callers", not callers.get(294), sorted(callers.get(294, set())))
    profile_refs = {int(text_of(profile, "mid0", "-1")) for profile in children(root, "Profile")}
    scene_refs = set()
    for scene in children(root, "Scene"):
        for node in children(scene):
            click = text_of(node, "clickTask")
            if click.isdigit():
                scene_refs.add(int(click))
    check(report, "task294_no_profile_or_scene_caller", 294 not in profile_refs | scene_refs, {"profiles": sorted(profile_refs), "scenes": sorted(scene_refs)})
    check(report, "new_helpers_reachable_only_from_validation", all(callers.get(task_id) and all(caller in ({237, 268, 270, 272, 276, 293} | set(EXPECTED_HELPERS)) for caller in callers[task_id]) for task_id in EXPECTED_HELPERS), {str(task_id): sorted(callers.get(task_id, set())) for task_id in EXPECTED_HELPERS})
    check(report, "new_helpers_have_no_profile_or_scene_caller", not (set(EXPECTED_HELPERS) & (profile_refs | scene_refs)), sorted(set(EXPECTED_HELPERS) & (profile_refs | scene_refs)))

    orchestrator_calls = [(index, string_arg(action, "arg0")) for index, action in enumerate(actions_by_id[268]) if text_of(action, "code") == "130"]
    contract_index = next((index for index, target in orchestrator_calls if target == "AIW Validation Fixture Contract"), -1)
    phase_indices = [index for index, target in orchestrator_calls if target.startswith("AIW Validation Phase ")]
    check(report, "fixture_contract_before_every_phase", contract_index >= 0 and phase_indices and contract_index < min(phase_indices), {"contract": contract_index, "phases": phase_indices})
    pre_contract_calls = [target for index, target in orchestrator_calls if index < contract_index]
    check(report, "zero_sheet_or_lifecycle_calls_before_contract", not pre_contract_calls, pre_contract_calls)
    task268_raw = raw_candidate[268]
    check(report, "contract_exact_ready_gate_present", "FIXTURE_CONTRACT_READY" in task268_raw and task268_raw.find("FIXTURE_CONTRACT_READY") < task268_raw.find("AIW Validation Phase 0"))

    visible_fixture_tasks = {237, 268, 270, 272, 276, 293} | set(EXPECTED_HELPERS)
    visible_text = "\n".join(raw_candidate[task_id] for task_id in sorted(visible_fixture_tasks))
    use_findings = []
    for task_id in reachable:
        for action in actions_by_id[task_id]:
            if text_of(action, "code") == "130" and string_arg(action, "arg0") == "AIW Validation Cleanup Exact Row":
                if string_arg(action, "arg2") in {"MAIN", "ARCHIVE", "DEAD"} and string_arg(action, "arg3") in {"144", "145", "146", "147", "999"}:
                    use_findings.append({"task": task_id, "sr": action_index(action), "args": [string_arg(action, "arg2"), string_arg(action, "arg3")]})
    check(report, "prohibited_cleanup_rows_absent", not use_findings, use_findings)
    task237_sets = [(string_arg(action, "arg0"), string_arg(action, "arg1")) for action in actions_by_id[237] if text_of(action, "code") == "547"]
    check(report, "task237_has_no_hardcoded_fixture_rows", not any(name == "%PSMainRow" and value in {"144", "145", "146", "147", "148"} for name, value in task237_sets), [item for item in task237_sets if item[0] == "%PSMainRow"])
    task270_sets = [(string_arg(action, "arg0"), string_arg(action, "arg1")) for action in actions_by_id[270] if text_of(action, "code") == "547"]
    check(report, "task270_hardcoded_history_ids_removed", not any(value in {"999999999999990001", "999999999999990002"} for _, value in task270_sets))
    check(report, "task276_no_task294_call", not action_calls(actions_by_id[276], "AIW Validation Archive Cleanup By ID"))

    setup_actions = actions_by_id[299]
    cleanup_actions = actions_by_id[300]
    setup_read_calls = action_calls(setup_actions, "AIW Validation Fixture Inspect Bound")
    setup_writes = [index for index, action in enumerate(setup_actions) if text_of(action, "code") == "1461810131"]
    cleanup_read_calls = action_calls(cleanup_actions, "AIW Validation Fixture Inspect Bound")
    cleanup_writes = [index for index, action in enumerate(cleanup_actions) if text_of(action, "code") == "1461810131"]
    check(report, "setup_read_before_every_write_and_readback_after", setup_read_calls and setup_writes and min(setup_read_calls) < min(setup_writes) < max(setup_read_calls), {"reads": setup_read_calls, "writes": setup_writes})
    check(report, "cleanup_read_before_every_write_and_readback_after", cleanup_read_calls and cleanup_writes and min(cleanup_read_calls) < min(cleanup_writes) < max(cleanup_read_calls), {"reads": cleanup_read_calls, "writes": cleanup_writes})
    check(report, "setup_write_count_bounded_one_per_layer", len(setup_writes) == 3, setup_writes)
    check(report, "cleanup_write_count_bounded_one_per_layer", len(cleanup_writes) == 5, cleanup_writes)
    check(report, "already_blank_zero_write_branch_present", "FIXTURE_ALREADY_CLEAN" in raw_candidate[300] and raw_candidate[300].find("FIXTURE_ALREADY_CLEAN") < raw_candidate[300].find("1461810131"))
    check(report, "occupied_and_wrong_identity_hold_present", "FIXTURE_ROW_OCCUPIED_HOLD" in visible_text and "VALIDATION_CLEANUP_AUTHORIZATION_HOLD" in visible_text)
    check(report, "bounds_hold_present_in_resolvers_and_inspect", all("FIXTURE_OUT_OF_BOUNDS_HOLD" in raw_candidate[task_id] for task_id in (295, 296, 297, 307)))
    check(report, "protected_rows_guard_only", all(token in raw_candidate[295] and token in raw_candidate[296] for token in ("144", "145", "146", "147")))
    check(report, "run_and_expected_identity_checks_present", all(token in visible_text for token in ("%AIWValidationRunID", "%AIWFixtureBoundID", "%AIWFixtureBoundRunID", "%AIWFixtureBoundAuthToken")))
    check(report, "one_shot_authorization_consumed_and_closed", all(token in visible_text for token in ("%AIWFXAuthConsumedRun", "ACTIVE", "USED", "FIXTURE_AUTHORIZATION_CLOSED")))
    check(report, "no_arbitrary_layer_numeric_cleanup_authority", "AIW Validation Fixture Resolve Runtime" in raw_candidate[293] and "RUNTIME_FIXTURE_OWNERSHIP_HOLD" in raw_candidate[296] and not any(text_of(action, "code") in {"1810865467", "1461810131"} for action in actions_by_id[293]))

    helper_plugin_issues = plugin_properties(set(EXPECTED_HELPERS), actions_by_id)
    check(report, "helper_plugin_continue_error_and_safe_write_settings", not helper_plugin_issues, helper_plugin_issues)
    read_helpers = {303, 305, 306, 307}
    read_contract_issues = []
    for task_id in read_helpers:
        raw = raw_candidate[task_id]
        if "1,2" not in raw or "%err" not in raw or "%errmsg" not in raw or "<code>357</code>" not in raw:
            read_contract_issues.append(task_id)
    check(report, "all_fixture_reads_clear_arrays_errors_and_use_two_attempts", not read_contract_issues, read_contract_issues)
    check(report, "exact_direct_row_ranges_only", all(fragment in visible_text for fragment in ("A%AIWFixtureBoundRow:Z%AIWFixtureBoundRow", "A%AIWFixtureBoundRow:C%AIWFixtureBoundRow", "A%AIWFixtureBoundRow:A%AIWFixtureBoundRow", "A%AIWFixtureBoundRow:N%AIWFixtureBoundRow")))
    check(report, "no_unsafe_default_fixture_rows", not any(re.search(rf'<Str sr="arg1" ve="3">{row}</Str>', raw_candidate[task_id]) for task_id in visible_fixture_tasks for row in ("144", "145", "146", "147", "148", "999")), "guard regex literals are allowed; value defaults are forbidden")

    all_rty = {task_id: text_of(task, "rty", "DEFAULT") for task_id, task in by_id.items()}
    run_both_all = {task_id for task_id, value in all_rty.items() if value == "2"}
    run_both_reachable = run_both_all & reachable
    check(report, "reachable_run_both_tasks_exact_declared", run_both_reachable == DECLARED_REACHABLE_RUN_BOTH, sorted(run_both_reachable))
    check(report, "legacy_task75_run_both_inventory_and_unreachable", all_rty.get(75) == "2" and 75 not in reachable, {"rty": all_rty.get(75), "reachable": 75 in reachable})
    report["inventory"]["collision_settings_all_tasks"] = {str(task_id): all_rty[task_id] for task_id in sorted(all_rty)}
    report["inventory"]["reachable_from_268"] = sorted(reachable)

    oversized = []
    for task_id, actions in actions_by_id.items():
        if len(actions) > 500:
            oversized.append({
                "task_id": task_id,
                "name": text_of(by_id[task_id], "nme"),
                "action_count": len(actions),
                "reachable": task_id in reachable,
                "callers": sorted(callers.get(task_id, set())),
                "changed": task_id in changed,
                "added": task_id in added,
            })
    check(report, "no_new_helper_over_500", not any(item["added"] for item in oversized), oversized)
    report["inventory"]["over_500_tasks"] = oversized

    new_helper_calls = {(caller, target) for caller in EXPECTED_HELPERS for target in graph.get(caller, set())}
    send_related_ids = {71, 223, 225, 226, 227, 231, 262}
    check(report, "no_new_helper_send_path", not any(target in send_related_ids for _, target in new_helper_calls), sorted(new_helper_calls))
    check(report, "production_send_confirmation_archive_tasks_byte_equal", all(raw_base[task_id] == raw_candidate[task_id] for task_id in send_related_ids), sorted(send_related_ids))
    check(report, "json_true_zero", candidate_text.count('"json":true') == 0, candidate_text.count('"json":true'))
    check(report, "se_true_zero", candidate_text.count("<se>true</se>") == 0, candidate_text.count("<se>true</se>"))
    check(report, "encoding_counts_preserved_or_expected", candidate_text.count("§") == base_text.count("§"), {"base": base_text.count("§"), "candidate": candidate_text.count("§")})
    check(report, "mojibake_markers_not_added", all(candidate_text.count(marker) == base_text.count(marker) for marker in ("Ãƒ", "ï¿½", "Ã‚Â§")), {marker: [base_text.count(marker), candidate_text.count(marker)] for marker in ("Ãƒ", "ï¿½", "Ã‚Â§")})
    check(report, "private_key_marker_count_preserved", candidate_text.count("%OpenAIKey") == base_text.count("%OpenAIKey"), {"base": base_text.count("%OpenAIKey"), "candidate": candidate_text.count("%OpenAIKey")})

    failures = [name for name, result in report["checks"].items() if not result["pass"]]
    report["summary"] = {
        "status": "PASS" if not failures else "FAIL",
        "check_count": len(report["checks"]),
        "failure_count": len(failures),
        "failures": failures,
        "task_count": len(tasks),
        "profile_count": len(children(root, "Profile")),
        "scene_count": len(children(root, "Scene")),
        "action_count": sum(len(actions) for actions in actions_by_id.values()),
        "changed_existing": sorted(changed),
        "added_helpers": sorted(added),
        "reachable_count": len(reachable),
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
