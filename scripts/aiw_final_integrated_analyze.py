from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from typing import Any


VAR_RE = re.compile(r"%[A-Za-z][A-Za-z0-9_]*(?:\([^)]*\))?")
TASK_RE = re.compile(r'<Task\s+sr="task(\d+)".*?</Task>', re.DOTALL)
CONTROL_CODES = {37: "IF", 38: "END_IF", 39: "FOR", 40: "END_FOR", 43: "ELSE"}
WRITE_CODES = {547, 549, 357, 888}
SECRET_PATTERNS = {
    "openai_key": re.compile(rb"sk-[A-Za-z0-9_-]{12,}"),
    "google_api_key": re.compile(rb"AIza[0-9A-Za-z_-]{20,}"),
    "bearer_token": re.compile(rb"Bearer\s+[A-Za-z0-9._~+/=-]{12,}", re.I),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sr_number(value: str | None) -> int:
    match = re.search(r"(-?\d+)$", value or "")
    return int(match.group(1)) if match else -1


def task_raw_map(text: str) -> dict[int, str]:
    return {int(match.group(1)): match.group(0) for match in TASK_RE.finditer(text)}


def action_text(action: ET.Element) -> str:
    return ET.tostring(action, encoding="unicode")


def str_arg(action: ET.Element, sr: str) -> str:
    node = action.find(f"Str[@sr='{sr}']")
    return (node.text or "") if node is not None else ""


def plugin_parameters(action: ET.Element) -> dict[str, Any] | None:
    node = action.find("Bundle/Vals/parameters")
    if node is None or not node.text:
        return None
    try:
        value = json.loads(node.text)
    except json.JSONDecodeError:
        return {"_parse_error": True, "_sha256": sha256(node.text.encode("utf-8"))}
    if isinstance(value, dict):
        return value
    return {"_non_object": type(value).__name__}


def plugin_summary(action: ET.Element) -> dict[str, Any] | None:
    params = plugin_parameters(action)
    vals = action.find("Bundle/Vals")
    if params is None and vals is None:
        return None
    xml = action_text(action)
    lowered = xml.lower()
    if "autosheets" in lowered or "_spreadsheet" in json.dumps(params or {}).lower():
        kind = "AutoSheets"
    elif "autoinput" in lowered:
        kind = "AutoInput"
    elif "autonotification" in lowered:
        kind = "AutoNotification"
    elif "taskerm" in lowered or "joaomgcd" in lowered:
        kind = "TaskerPlugin"
    else:
        kind = "Plugin"
    se_node = action.find("se")
    arg4 = action.find("Int[@sr='arg4']")
    result: dict[str, Any] = {
        "kind": kind,
        "se": None if se_node is None else (se_node.text or ""),
        "arg4": None if arg4 is None else arg4.get("val"),
        "parameters_sha256": None,
    }
    params_node = action.find("Bundle/Vals/parameters")
    if params_node is not None and params_node.text:
        result["parameters_sha256"] = sha256(params_node.text.encode("utf-8"))
    if params and kind == "AutoSheets":
        spreadsheet = params.get("_spreadSheet", {}) if isinstance(params, dict) else {}
        output = params.get("output", {}) if isinstance(params, dict) else {}
        cells = params.get("_cellsByReference", {}) if isinstance(params, dict) else {}
        sheet_data = params.get("_sheetData", {}) if isinstance(params, dict) else {}
        offline = params.get("_offlineSettings", {}) if isinstance(params, dict) else {}
        result.update(
            {
                "sheet": spreadsheet.get("sheetName"),
                "create_sheet_if_needed": spreadsheet.get("createSheetIfNeeded"),
                "range": output.get("range"),
                "output_names": output.get("outputNames"),
                "json": output.get("json"),
                "reference": cells.get("reference"),
                "offline_update": offline.get("updateLaterIfOffline"),
                "major_dimension": sheet_data.get("majorDimension"),
                "field_count": len(str(sheet_data.get("data", "")).split(str(sheet_data.get("separator", "\u0000"))))
                if sheet_data.get("data") is not None
                else None,
            }
        )
    elif params and kind == "AutoInput":
        flat_keys: list[str] = []
        stack: list[tuple[str, Any]] = [("", params)]
        while stack:
            prefix, value = stack.pop()
            if isinstance(value, dict):
                for key, child in value.items():
                    full = f"{prefix}.{key}" if prefix else str(key)
                    flat_keys.append(full)
                    stack.append((full, child))
        result["parameter_keys"] = sorted(set(flat_keys))
    return result


def analyze_control(task_id: int, actions: list[ET.Element]) -> list[dict[str, Any]]:
    stack: list[tuple[str, int]] = []
    issues: list[dict[str, Any]] = []
    for action in actions:
        sr = sr_number(action.get("sr"))
        code = int(action.findtext("code", "-1"))
        if code == 37:
            stack.append(("IF", sr))
        elif code == 39:
            stack.append(("FOR", sr))
        elif code == 43:
            if not stack or stack[-1][0] != "IF":
                issues.append({"task_id": task_id, "sr": sr, "issue": "ELSE_WITHOUT_IF"})
        elif code == 38:
            if not stack or stack[-1][0] != "IF":
                issues.append({"task_id": task_id, "sr": sr, "issue": "END_IF_MISMATCH"})
            else:
                stack.pop()
        elif code == 40:
            if not stack or stack[-1][0] != "FOR":
                issues.append({"task_id": task_id, "sr": sr, "issue": "END_FOR_MISMATCH"})
            else:
                stack.pop()
    for kind, sr in stack:
        issues.append({"task_id": task_id, "sr": sr, "issue": f"UNCLOSED_{kind}"})
    return issues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("xml", type=Path)
    parser.add_argument("out_dir", type=Path)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    data = args.xml.read_bytes()
    text = data.decode("utf-8")
    root = ET.fromstring(data)
    raw_tasks = task_raw_map(text)
    tasks_by_id = {int(task.findtext("id", "-1")): task for task in root.findall("Task")}
    names_to_id = {task.findtext("nme", ""): task_id for task_id, task in tasks_by_id.items()}
    task_records: list[dict[str, Any]] = []
    call_graph: dict[str, list[str]] = {}
    var_readers: dict[str, set[str]] = defaultdict(set)
    var_writers: dict[str, set[str]] = defaultdict(set)
    plugins: list[dict[str, Any]] = []
    control_issues: list[dict[str, Any]] = []
    duplicate_action_sr: list[dict[str, Any]] = []
    action_gaps: list[dict[str, Any]] = []

    for task_id in sorted(tasks_by_id):
        task = tasks_by_id[task_id]
        name = task.findtext("nme", "")
        actions = sorted(task.findall("Action"), key=lambda item: sr_number(item.get("sr")))
        action_srs = [sr_number(action.get("sr")) for action in actions]
        if len(action_srs) != len(set(action_srs)):
            duplicate_action_sr.append({"task_id": task_id, "task": name, "srs": action_srs})
        expected = list(range(len(action_srs)))
        if action_srs != expected:
            action_gaps.append({"task_id": task_id, "task": name, "actual": action_srs, "expected": expected})
        control_issues.extend(analyze_control(task_id, actions))
        calls: list[str] = []
        codes: dict[str, int] = defaultdict(int)
        properties = {child.tag: child.text for child in task if child.tag != "Action"}
        for action in actions:
            code = int(action.findtext("code", "-1"))
            codes[str(code)] += 1
            xml = action_text(action)
            variables = set(VAR_RE.findall(xml))
            write_targets: set[str] = set()
            if code in WRITE_CODES:
                target = str_arg(action, "arg0")
                if target.startswith("%"):
                    write_targets.add(re.sub(r"\(.*\)$", "", target))
            for variable in variables:
                normalized = re.sub(r"\(.*\)$", "", variable)
                if normalized not in write_targets:
                    var_readers[normalized].add(name)
            for target in write_targets:
                var_writers[target].add(name)
            if code == 130:
                target = str_arg(action, "arg0")
                if target:
                    calls.append(target)
            summary = plugin_summary(action)
            if summary is not None:
                plugins.append(
                    {
                        "task_id": task_id,
                        "task": name,
                        "action_sr": sr_number(action.get("sr")),
                        "code": code,
                        **summary,
                    }
                )
        call_graph[name] = calls
        task_records.append(
            {
                "id": task_id,
                "name": name,
                "sr": task.get("sr"),
                "rty": task.findtext("rty"),
                "priority": task.findtext("pri"),
                "stay_awake": task.findtext("stayawake"),
                "action_count": len(actions),
                "codes": dict(sorted(codes.items(), key=lambda item: int(item[0]))),
                "calls": calls,
                "raw_sha256": sha256(raw_tasks.get(task_id, "").encode("utf-8")),
                "properties": properties,
            }
        )

    missing_calls = [
        {"caller": caller, "target": target}
        for caller, targets in call_graph.items()
        for target in targets
        if target not in names_to_id
    ]
    profiles = []
    missing_profile_refs = []
    for profile in root.findall("Profile"):
        record = {
            "id": profile.findtext("id"),
            "name": profile.findtext("nme"),
            "p_state": profile.findtext("pState"),
            "mid0": profile.findtext("mid0"),
            "mid1": profile.findtext("mid1"),
        }
        profiles.append(record)
        for field in ("mid0", "mid1"):
            value = record[field]
            if value and int(value) not in tasks_by_id:
                missing_profile_refs.append({"profile": record["name"], "field": field, "task_id": value})

    scenes = []
    missing_scene_refs = []
    for scene in root.findall("Scene"):
        scene_xml = ET.tostring(scene, encoding="unicode")
        click_ids = [int(value) for value in re.findall(r"<clickTask>(\d+)</clickTask>", scene_xml)]
        scenes.append({"name": scene.findtext("nme"), "click_tasks": click_ids})
        for task_id in click_ids:
            if task_id not in tasks_by_id:
                missing_scene_refs.append({"scene": scene.findtext("nme"), "task_id": task_id})

    project = root.find("Project")
    project_tids = []
    project_scenes: list[str] = []
    if project is not None:
        project_tids = [int(value) for value in (project.findtext("tids") or "").split(",") if value.strip().isdigit()]
        project_scenes = [value for value in (project.findtext("scenes") or "").split(",") if value]
    project_missing_tasks = sorted(set(tasks_by_id) - set(project_tids))

    variables = {
        variable: {
            "readers": sorted(var_readers.get(variable, set())),
            "writers": sorted(var_writers.get(variable, set())),
        }
        for variable in sorted(set(var_readers) | set(var_writers))
    }
    lock_variables = {
        variable: record
        for variable, record in variables.items()
        if re.search(r"(?i)(owner|lock|busy|processing|sending|confirming|archiving|startedat)$", variable)
    }
    task_names = [record["name"] for record in task_records]
    task_ids = [record["id"] for record in task_records]
    task_srs = [record["sr"] for record in task_records]
    report = {
        "source": {"filename": args.xml.name, "bytes": len(data), "sha256": sha256(data)},
        "root": root.tag,
        "task_count": len(task_records),
        "profile_count": len(profiles),
        "scene_count": len(scenes),
        "total_actions": sum(record["action_count"] for record in task_records),
        "duplicate_task_ids": sorted({value for value in task_ids if task_ids.count(value) > 1}),
        "duplicate_task_names": sorted({value for value in task_names if task_names.count(value) > 1}),
        "duplicate_task_sr": sorted({value for value in task_srs if task_srs.count(value) > 1}),
        "duplicate_action_sr": duplicate_action_sr,
        "action_gaps": action_gaps,
        "control_issues": control_issues,
        "missing_calls": missing_calls,
        "missing_profile_refs": missing_profile_refs,
        "missing_scene_refs": missing_scene_refs,
        "project_missing_tasks": project_missing_tasks,
        "project_scenes": project_scenes,
        "profiles": profiles,
        "scenes": scenes,
        "tasks": task_records,
        "secret_marker_counts": {name: len(pattern.findall(data)) for name, pattern in SECRET_PATTERNS.items()},
        "mojibake_counts": {
            "literal_A_circumflex_section": text.count("\u00c2\u00a7"),
            "literal_A_tilde": text.count("\u00c3"),
            "section_sign": text.count("\u00a7"),
            "replacement_char": text.count("\ufffd"),
        },
    }
    outputs = {
        "SYSTEM_INVENTORY.json": report,
        "CALL_GRAPH.json": call_graph,
        "VARIABLE_OWNERSHIP.json": variables,
        "LOCK_OWNERSHIP.json": lock_variables,
        "PLUGIN_AUDIT.json": plugins,
    }
    for filename, value in outputs.items():
        (args.out_dir / filename).write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "source": report["source"],
                "topology": [report["task_count"], report["profile_count"], report["scene_count"], report["total_actions"]],
                "control_issues": len(control_issues),
                "missing_calls": len(missing_calls),
                "missing_profile_refs": len(missing_profile_refs),
                "missing_scene_refs": len(missing_scene_refs),
                "project_missing_tasks": len(project_missing_tasks),
                "plugin_actions": len(plugins),
                "variables": len(variables),
                "lock_variables": len(lock_variables),
                "secret_marker_counts": report["secret_marker_counts"],
                "mojibake_counts": report["mojibake_counts"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
