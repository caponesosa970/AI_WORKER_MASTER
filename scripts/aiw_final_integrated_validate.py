from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict, deque
from pathlib import Path
from xml.dom import minidom


PROTECTED_IDS = {223, 225, 226, 231, 233, 235}
EXPECTED_CHANGED = {68, 73, 74, 130, 131, 147, 153, 183, 199, 236, 247}
EXPECTED_ADDED = {
    248, 249, 250, 252, 254, 255, 256, 258, 259, 260, 262, 263, 264, 265,
    266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279,
    280, 281, 282, 283, 284, 286, 289, 291, 292, 293, 294,
}
UNSAFE_LEGACY_IDS = {18, 19, 24, 31, 34, 73, 74, 147, 154, 236, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247}
CRITICAL_AWAKE = {68, 248, 249, 250, 252, 254, 255, 256, 258, 259, 260, 262, 263, 264, 268, 277, 278, 281, 282, 284, 286, 289, 291, 292, 293, 294}
RUN_BOTH = {68, 199, 248, 263, 286}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def element_children(node):
    return [child for child in node.childNodes if child.nodeType == child.ELEMENT_NODE]


def first_child(node, tag: str):
    return next((child for child in element_children(node) if child.tagName == tag), None)


def text_of(node, tag: str, default: str = "") -> str:
    child = first_child(node, tag)
    if child is None:
        return default
    return "".join(part.data for part in child.childNodes if part.nodeType in (part.TEXT_NODE, part.CDATA_SECTION_NODE))


def direct_children(node, tag: str):
    return [child for child in element_children(node) if child.tagName == tag]


def action_number(action) -> int:
    match = re.fullmatch(r"act(\d+)", action.getAttribute("sr"))
    return int(match.group(1)) if match else -1


def string_arg(action, sr: str) -> str:
    for child in direct_children(action, "Str"):
        if child.getAttribute("sr") == sr:
            return "".join(part.data for part in child.childNodes if part.nodeType == part.TEXT_NODE)
    return ""


def int_arg(action, sr: str) -> str:
    for child in direct_children(action, "Int"):
        if child.getAttribute("sr") == sr:
            return child.getAttribute("val")
    return ""


def raw_tasks(text: str) -> dict[int, str]:
    return {
        int(match.group(1)): match.group(0)
        for match in re.finditer(r'<Task sr="task(\d+)".*?</Task>', text, flags=re.DOTALL)
    }


def one(report: dict, name: str, condition: bool, detail: object = None) -> None:
    report["checks"][name] = {"pass": bool(condition), "detail": detail}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("report", type=Path)
    parser.add_argument("--expected-base-sha", default="")
    args = parser.parse_args()

    base_bytes = args.base.read_bytes()
    candidate_bytes = args.candidate.read_bytes()
    base_text = base_bytes.decode("utf-8")
    candidate_text = candidate_bytes.decode("utf-8")
    base_dom = minidom.parseString(base_bytes)
    dom = minidom.parseString(candidate_bytes)
    root = dom.documentElement
    base_raw = raw_tasks(base_text)
    candidate_raw = raw_tasks(candidate_text)

    report: dict = {
        "validator": "independent-minidom-validator-v1",
        "source": {
            "base_sha256": sha(base_bytes),
            "candidate_sha256": sha(candidate_bytes),
            "candidate_bytes": len(candidate_bytes),
        },
        "checks": {},
        "findings": [],
    }
    expected_base_sha = args.expected_base_sha.upper()
    one(report, "authorized_base_sha", bool(expected_base_sha) and sha(base_bytes) == expected_base_sha, sha(base_bytes))
    one(report, "root_taskerdata", root.tagName == "TaskerData", root.tagName)

    tasks = direct_children(root, "Task")
    task_ids = [int(text_of(task, "id", "-1")) for task in tasks]
    task_names = [text_of(task, "nme") for task in tasks]
    by_id = {int(text_of(task, "id")): task for task in tasks}
    by_name = {text_of(task, "nme"): task for task in tasks}
    one(report, "duplicate_task_ids_zero", len(task_ids) == len(set(task_ids)), [k for k, v in Counter(task_ids).items() if v > 1])
    one(report, "duplicate_task_names_zero", len(task_names) == len(set(task_names)), [k for k, v in Counter(task_names).items() if v > 1])

    changed = {task_id for task_id in base_raw if base_raw[task_id] != candidate_raw.get(task_id)}
    added = set(candidate_raw) - set(base_raw)
    one(report, "changed_existing_exact", changed == EXPECTED_CHANGED, sorted(changed))
    one(report, "added_tasks_exact", added == EXPECTED_ADDED, sorted(added))
    protected_hashes = {}
    for task_id in sorted(PROTECTED_IDS):
        protected_hashes[str(task_id)] = {
            "base": sha(base_raw[task_id].encode("utf-8")),
            "candidate": sha(candidate_raw[task_id].encode("utf-8")),
        }
    one(
        report,
        "protected_tasks_byte_equal",
        all(item["base"] == item["candidate"] for item in protected_hashes.values()),
        protected_hashes,
    )

    project = direct_children(root, "Project")
    project_ids: set[int] = set()
    project_scenes: set[str] = set()
    if len(project) == 1:
        project_ids = {int(value) for value in text_of(project[0], "tids").split(",") if value}
        project_scenes = {value for value in text_of(project[0], "scenes").split(",") if value}
    one(report, "one_project_registry", len(project) == 1, len(project))
    one(report, "project_task_registry_complete", project_ids == set(task_ids), sorted(set(task_ids) - project_ids))

    profiles = direct_children(root, "Profile")
    profile_refs = [int(text_of(profile, "mid0", "-1")) for profile in profiles]
    one(report, "profile_task_refs_complete", all(ref in by_id for ref in profile_refs), profile_refs)
    profile_map = {int(text_of(profile, "id")): int(text_of(profile, "mid0")) for profile in profiles}
    one(report, "profile_entrypoints_exact", profile_map == {134: 265, 135: 283, 136: 68, 137: 72}, profile_map)

    scenes = direct_children(root, "Scene")
    scene_names = {text_of(scene, "nme") for scene in scenes}
    one(report, "project_scene_registry_complete", project_scenes == scene_names, sorted(scene_names))
    control_scenes = [scene for scene in scenes if text_of(scene, "nme") == "AIW FINAL CONTROL"]
    click_refs: list[int] = []
    for scene in control_scenes:
        for element in element_children(scene):
            click = text_of(element, "clickTask")
            if click and re.fullmatch(r"\d+", click):
                click_refs.append(int(click))
    one(report, "final_control_scene_exact_buttons", sorted(click_refs) == [130, 131, 266, 267, 279, 280], sorted(click_refs))

    graph: dict[int, list[int]] = defaultdict(list)
    missing_calls: list[dict] = []
    control_issues: list[dict] = []
    action_gaps: list[dict] = []
    plugin_issues: list[dict] = []
    task_actions: dict[int, list] = {}
    for task_id, task in by_id.items():
        actions = sorted(direct_children(task, "Action"), key=action_number)
        task_actions[task_id] = actions
        indices = [action_number(action) for action in actions]
        if indices != list(range(len(actions))):
            action_gaps.append({"task": task_id, "count": len(actions), "indices_head": indices[:20], "indices_tail": indices[-20:]})
        stack: list[str] = []
        for action in actions:
            code = text_of(action, "code")
            if code == "37":
                stack.append("if")
            elif code == "43":
                if not stack or stack[-1] != "if":
                    control_issues.append({"task": task_id, "sr": action_number(action), "issue": "else_without_if"})
            elif code == "38":
                if not stack or stack[-1] != "if":
                    control_issues.append({"task": task_id, "sr": action_number(action), "issue": "endif_without_if"})
                else:
                    stack.pop()
            elif code == "39":
                stack.append("for")
            elif code == "40":
                if not stack or stack[-1] != "for":
                    control_issues.append({"task": task_id, "sr": action_number(action), "issue": "endfor_without_for"})
                else:
                    stack.pop()
            elif code == "130":
                target = string_arg(action, "arg0")
                if target in by_name:
                    graph[task_id].append(int(text_of(by_name[target], "id")))
                elif target:
                    missing_calls.append({"task": task_id, "target": target})
            if code in {"1810865467", "1461810131"} and task_id in EXPECTED_ADDED:
                se = text_of(action, "se")
                arg4 = int_arg(action, "arg4")
                if se != "false" or arg4 != "1":
                    plugin_issues.append({"task": task_id, "sr": action_number(action), "se": se, "arg4": arg4})
        if stack:
            control_issues.append({"task": task_id, "issue": "unclosed", "stack": stack})
    one(report, "action_indices_contiguous", not action_gaps, action_gaps)
    one(report, "control_stacks_balanced", not control_issues, control_issues)
    one(report, "perform_task_refs_complete", not missing_calls, missing_calls)
    one(report, "new_plugin_actions_continue_and_route", not plugin_issues, plugin_issues)

    roots = set(profile_refs) | set(click_refs) | {268}
    reachable: set[int] = set()
    queue = deque(roots)
    while queue:
        current = queue.popleft()
        if current in reachable:
            continue
        reachable.add(current)
        queue.extend(graph.get(current, []))
    unsafe_reachable = sorted((UNSAFE_LEGACY_IDS & reachable) - {73, 74, 147, 236, 247, 283})
    one(report, "unsafe_legacy_runtime_unreachable", not unsafe_reachable, unsafe_reachable)
    blocked_controls = {73, 74, 147, 236, 247}
    one(
        report,
        "legacy_controls_fail_closed",
        all("UNSAFE_LEGACY_CONTROL_BLOCKED" in candidate_raw.get(task_id, "") or "OLD_D3A_TEST_LAUNCHER_BLOCKED" in candidate_raw.get(task_id, "") for task_id in blocked_controls),
        sorted(blocked_controls),
    )

    one(report, "critical_tasks_keep_awake", all(text_of(by_id[task_id], "stayawake") == "true" for task_id in CRITICAL_AWAKE), sorted(task_id for task_id in CRITICAL_AWAKE if text_of(by_id[task_id], "stayawake") != "true"))
    one(report, "run_both_only_declared_concurrency_tasks", all(text_of(by_id[task_id], "rty") == "2" for task_id in RUN_BOTH), {str(task_id): text_of(by_id[task_id], "rty") for task_id in sorted(RUN_BOTH)})

    task68 = candidate_raw[68]
    first_shared = min((task68.find(f"%{name}") for name in ("SNid", "SNsender", "SNmessage") if task68.find(f"%{name}") >= 0), default=-1)
    acquire_call = task68.find("AIW Ingress Owner")
    fallback = task68.find("%evt_sender</Str><Str sr=\"arg1\" ve=\"3\">%evt_ticker")
    journal_call = task68.find("AIW Ingress Journal Append Exact")
    queue_call = task68.find("FINAL Queue Cycle")
    one(report, "notification_locals_before_shared_globals", 0 <= acquire_call < first_shared, {"acquire": acquire_call, "first_shared": first_shared})
    one(report, "sender_fallback_before_ingress_acquire", 0 <= fallback < acquire_call, {"fallback": fallback, "acquire": acquire_call})
    one(report, "journal_before_queue_kick", 0 <= journal_call < queue_call, {"journal": journal_call, "queue": queue_call})

    q263 = task_actions[263]
    calls263 = [(index, string_arg(action, "arg0")) for index, action in enumerate(q263) if text_of(action, "code") == "130"]
    ordered_names = [
        "AIW Ingress Journal Drain One",
        "AIW Overflow Drain Transaction",
        "AIW Integrated Process One",
        "AIW Protected Send Confirm Archive One",
    ]
    positions = [next((index for index, name in calls263 if name == target), -1) for target in ordered_names]
    one(report, "queue_pipeline_order_exact", positions == sorted(positions) and all(value >= 0 for value in positions), dict(zip(ordered_names, positions)))
    overflow_call = positions[1]
    process_call = positions[2]
    gates_between = [
        action for index, action in enumerate(q263)
        if overflow_call < index < process_call and text_of(action, "code") == "37"
    ]
    one(report, "overflow_hold_gate_precedes_processing", bool(gates_between), len(gates_between))
    one(report, "one_followup_literal", candidate_raw[263].count("FOLLOWUP") == 2, candidate_raw[263].count("FOLLOWUP"))

    overflow_append = candidate_raw[255]
    overflow_drain = candidate_raw[258]
    one(report, "overflow_then_admission_lock_order_append", overflow_append.find("AIW Overflow Owner") < overflow_append.find("AIW Admission Owner"), None)
    one(report, "overflow_then_admission_lock_order_drain", overflow_drain.find("AIW Overflow Owner") < overflow_drain.find("AIW Admission Owner"), None)
    one(report, "overflow_failure_record_present", "AIW Overflow Failure Record" in overflow_drain and "%AIWOverflowAttempts+1" in candidate_raw[259], None)

    protected_flow = [223, 225, 226, 231, 233, 235]
    one(report, "protected_flow_tasks_reachable", all(task_id in reachable for task_id in protected_flow), sorted(task_id for task_id in protected_flow if task_id not in reachable))
    one(report, "final_orchestrator_exact_name", 268 in by_id and text_of(by_id[268], "nme") == "AIW FINAL RELEASE VALIDATION ORCHESTRATOR", text_of(by_id.get(268), "nme") if 268 in by_id else None)
    orchestrator_calls = [string_arg(action, "arg0") for action in task_actions[268] if text_of(action, "code") == "130"]
    one(report, "orchestrator_phases_zero_to_seven", orchestrator_calls.count("APP Stop AI Worker") == 1 and all(f"AIW Validation Phase {phase}" in orchestrator_calls for phase in range(8)), orchestrator_calls)

    one(report, "json_true_zero", candidate_text.count("\"json\":true") == 0, candidate_text.count("\"json\":true"))
    one(report, "se_true_zero", candidate_text.count("<se>true</se>") == 0, candidate_text.count("<se>true</se>"))
    one(report, "mojibake_zero", all(marker not in candidate_text for marker in ("Â§", "Ã", "�")), None)
    one(report, "section_sign_base_preserved_or_extended", candidate_text.count("§") >= base_text.count("§") and base_text.count("§") == 431, {"base": base_text.count("§"), "candidate": candidate_text.count("§")})
    key_markers = {"base": base_text.count("%OpenAIKey"), "candidate": candidate_text.count("%OpenAIKey")}
    one(report, "openai_key_marker_count_preserved", key_markers["base"] > 0 and key_markers["candidate"] == key_markers["base"], key_markers)
    one(report, "no_create_sheet_in_new_tasks", all('"createSheetIfNeeded":true' not in candidate_raw[task_id] for task_id in EXPECTED_ADDED), None)
    one(report, "no_offline_sheet_writes_in_new_tasks", all('"updateLaterIfOffline":true' not in candidate_raw[task_id] for task_id in EXPECTED_ADDED), None)

    failures = [name for name, value in report["checks"].items() if not value["pass"]]
    report["summary"] = {
        "status": "PASS" if not failures else "FAIL",
        "check_count": len(report["checks"]),
        "failure_count": len(failures),
        "failures": failures,
        "task_count": len(tasks),
        "profile_count": len(profiles),
        "scene_count": len(scenes),
        "reachable_task_count": len(reachable),
        "action_count": sum(len(actions) for actions in task_actions.values()),
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
