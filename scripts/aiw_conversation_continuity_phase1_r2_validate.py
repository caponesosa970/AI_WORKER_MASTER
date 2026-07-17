from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import aiw_conversation_continuity_phase1_r1_validate as r1v


EXPECTED_BASE_SHA = "9EB0A9FD6B3E342E4022AEE20022683F1BF08A54E65892A099565A3542D0A758"
AUTHORIZED = {273, 320, 325}
PHONE_PROVEN = {71, 199, 223, 225, 226, 227, 230, 231}
EXPLICITLY_FROZEN = {254, 255, 262, 263, 282, 309, 317, 327}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def strings(action: ET.Element) -> dict[str, str]:
    return {node.get("sr", ""): node.text or "" for node in action.findall("Str")}


def assignments(task: ET.Element) -> list[tuple[str, str]]:
    result = []
    for action in r1v.actions(task):
        if action.findtext("code") == "547":
            value = strings(action)
            result.append((value.get("arg0", ""), value.get("arg1", "")))
    return result


def plugin_fingerprints(task: ET.Element) -> list[str]:
    result = []
    for action in r1v.actions(task):
        if int(action.findtext("code", "-1")) not in (1810865467, 1461810131):
            continue
        copy = ET.fromstring(ET.tostring(action, encoding="unicode"))
        copy.set("sr", "actX")
        result.append(ET.tostring(copy, encoding="unicode"))
    return result


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
    root = ET.fromstring(candidate_bytes)
    base_tasks = r1v.task_map(base_root)
    tasks = r1v.task_map(root)
    base_raw = r1v.raw_blocks(base_text, "Task", r"<id>(\d+)</id>")
    raw = r1v.raw_blocks(candidate_text, "Task", r"<id>(\d+)</id>")
    changed = sorted(i for i in base_raw if base_raw[i] != raw.get(i))
    added = sorted(set(raw) - set(base_raw))
    checks: list[dict[str, object]] = []

    def check(name: str, passed: bool, evidence: object = None) -> None:
        checks.append({"name": name, "pass": bool(passed), "evidence": evidence})

    check("base_sha_exact", sha(base_bytes) == EXPECTED_BASE_SHA, sha(base_bytes))
    check("candidate_utf8_no_bom", not candidate_bytes.startswith(b"\xef\xbb\xbf"))
    check("xml_root_taskerdata", root.tag == "TaskerData", root.tag)
    check("changed_existing_exact", changed == sorted(AUTHORIZED), changed)
    check("added_tasks_zero", not added, added)
    check("unauthorized_tasks_raw_identical", all(base_raw[i] == raw[i] for i in set(base_raw) - AUTHORIZED), len(base_raw) - len(AUTHORIZED))
    check("phone_proven_raw_identical", all(base_raw[i] == raw[i] for i in PHONE_PROVEN), sorted(PHONE_PROVEN))
    check("explicit_frozen_raw_identical", all(base_raw[i] == raw[i] for i in EXPLICITLY_FROZEN), sorted(EXPLICITLY_FROZEN))
    base_profiles = r1v.raw_blocks(base_text, "Profile", r"<id>(\d+)</id>")
    profiles = r1v.raw_blocks(candidate_text, "Profile", r"<id>(\d+)</id>")
    base_scenes = {m.group(1): m.group(0) for m in re.finditer(r'<Scene sr="([^"]+)".*?</Scene>', base_text, re.DOTALL)}
    scenes = {m.group(1): m.group(0) for m in re.finditer(r'<Scene sr="([^"]+)".*?</Scene>', candidate_text, re.DOTALL)}
    check("profiles_raw_identical", profiles == base_profiles, len(profiles))
    check("scenes_raw_identical", scenes == base_scenes, len(scenes))
    check("profiles_disabled_state_preserved", all(base_profiles[i] == profiles[i] for i in profiles))
    check("control_stacks_balanced", all(r1v.balanced(task) for task in tasks.values()), [i for i, task in tasks.items() if not r1v.balanced(task)])

    names = [task.findtext("nme", "") for task in tasks.values()]
    check("duplicate_task_ids_zero", len(tasks) == len(set(tasks)), len(tasks))
    check("duplicate_task_names_zero", len(names) == len(set(names)), len(names) - len(set(names)))
    graph = r1v.graph(tasks)
    missing_perform = sorted({target for targets in graph.values() for target in targets if target not in tasks})
    profile_refs = {int(node.text) for profile in root.findall("Profile") for node in profile if re.fullmatch(r"mid\d+", node.tag) and node.text}
    scene_refs = {int(node.text) for scene in root.findall("Scene") for node in scene.iter("clickTask") if node.text and not node.text.startswith("-")}
    project = root.find("Project")
    project_ids = {int(v) for v in (project.findtext("tids", "") if project is not None else "").split(",") if v}
    check("missing_perform_refs_zero", not missing_perform, missing_perform)
    check("missing_profile_refs_zero", not (profile_refs - set(tasks)), sorted(profile_refs - set(tasks)))
    check("missing_scene_refs_zero", not (scene_refs - set(tasks)), sorted(scene_refs - set(tasks)))
    check("missing_project_refs_zero", not (set(tasks) - project_ids), sorted(set(tasks) - project_ids))

    task320 = tasks[320]
    text320 = r1v.decoded_text(task320)
    assign320 = assignments(task320)
    rhs320 = [condition.findtext("rhs", "") for condition in task320.iter("Condition")]
    check("member_capacity_loaded_from_ledger_ai", ("%AIWConversationMemberCapacity", "%AICGL_AI") in assign320)
    check("default_cutoff_bound_at", ("%cgf_freshness_cutoff", "%AIWConversationBoundAt") in assign320)
    check("full_cutoff_freeze_logged_at", ("%cgf_freshness_cutoff", "%AIWConversationFreezeLoggedAt") in assign320)
    check("numeric_count_capacity_contract", text320.count("^[1-4]$") >= 2)
    check("numeric_timestamp_contract", text320.count("^[0-9]{10,16}$") >= 2)
    check("count_not_above_capacity", "%AIWConversationMemberCount" in text320 and "%AIWConversationMemberCapacity" in text320 and "<op>7</op>" in raw[320])
    check("freeze_not_after_bind", "%AIWConversationFreezeLoggedAt" in text320 and "%AIWConversationBoundAt" in text320 and "CONVERSATION_PRE_SEND_CAPACITY_CONTRACT_HOLD" in text320)
    check("three_freshness_paths_use_derived_cutoff", rhs320.count("%cgf_freshness_cutoff") == 3, rhs320.count("%cgf_freshness_cutoff"))
    check("no_freshness_path_uses_bound_directly", raw[320].count("<rhs>%AIWConversationBoundAt</rhs>") == 1, raw[320].count("<rhs>%AIWConversationBoundAt</rhs>"))
    hold_pos = text320.find("CONVERSATION_PRE_SEND_CAPACITY_CONTRACT_HOLD")
    ready_pos = text320.find("CONVERSATION_GROUP_SEND_READY")
    check("capacity_hold_precedes_send_eligibility", 0 <= hold_pos < ready_pos, {"hold": hold_pos, "ready": ready_pos})
    check("task320_no_send_perform", "FINAL Send Sheet" not in {name for _, name in r1v.performs(task320)}, r1v.performs(task320))
    check("task320_action_count_below_500", len(r1v.actions(task320)) == 380, len(r1v.actions(task320)))

    task273 = tasks[273]
    task325 = tasks[325]
    check("phase4_r2_marker", "PHASE4_CONVERSATION_R2_START" in raw[273] and "PHASE4_CONVERSATION_R2_PASS" in raw[273])
    check("phase4_calls_capacity_contract", [name for _, name in r1v.performs(task273)].count("AIW Conversation Validation Audit") == 4 and "CAPACITY_CONTRACT" in raw[273])
    check("validation_capacity_mode_present", "CONVERSATION_VALIDATION_CAPACITY_CONTRACT_READY" in raw[325] and "CAPACITY_CONTRACT" in raw[325])
    check("validation_mode_uses_same_cutoff_rule", all(value in raw[325] for value in ("%AICGL_AI", "%AIWConversationDerivedFreshnessCutoff", "%AIWConversationFreezeLoggedAt", "%AIWConversationBoundAt")))
    check("authorized_task_action_counts", {i: len(r1v.actions(tasks[i])) for i in AUTHORIZED} == {273: 45, 320: 380, 325: 367}, {i: len(r1v.actions(tasks[i])) for i in AUTHORIZED})

    check("changed_task_plugin_actions_preserved", all(plugin_fingerprints(base_tasks[i]) == plugin_fingerprints(tasks[i]) for i in AUTHORIZED), {i: len(plugin_fingerprints(tasks[i])) for i in AUTHORIZED})
    send_callers = sorted(i for i, task in tasks.items() if "FINAL Send Sheet" in {name for _, name in r1v.performs(task)})
    production = r1v.reachable(graph, {199})
    check("single_reachable_send_path_preserved", sorted(set(send_callers) & production) == [262], {"all": send_callers, "reachable": sorted(set(send_callers) & production)})
    check("task327_unchanged_and_registered", base_raw[327] == raw[327] and 327 in project_ids)
    check("no_new_helper", set(tasks) == set(base_tasks))
    check("section_sign_count_preserved", base_text.count("§") == candidate_text.count("§"), {"base": base_text.count("§"), "candidate": candidate_text.count("§")})
    check("mojibake_count_preserved", base_text.count("Â§") == candidate_text.count("Â§"), {"base": base_text.count("Â§"), "candidate": candidate_text.count("Â§")})
    check("private_xml_not_redacted", "PRIVATE" in args.candidate.name and "REDACTED" not in args.candidate.name.upper())

    report = {
        "status": "PASS" if all(item["pass"] for item in checks) else "FAIL",
        "independent_validator": True,
        "base_sha256": sha(base_bytes),
        "candidate_sha256": sha(candidate_bytes),
        "candidate_bytes": len(candidate_bytes),
        "topology": {
            "tasks": len(tasks), "profiles": len(profiles), "scenes": len(scenes),
            "actions": sum(len(r1v.actions(task)) for task in tasks.values()),
        },
        "checks": checks,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "checks": len(checks), "failed": [item["name"] for item in checks if not item["pass"]], "topology": report["topology"]}, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
