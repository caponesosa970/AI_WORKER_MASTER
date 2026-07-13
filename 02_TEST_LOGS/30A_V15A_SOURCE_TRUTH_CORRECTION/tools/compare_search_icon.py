import argparse
import copy
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path


def child_text(element, tag):
    child = element.find(tag)
    if child is None:
        return None
    return child.text or ""


def str_arg(action, sr):
    for child in action:
        if child.tag == "Str" and child.attrib.get("sr") == sr:
            return child.text or ""
    return None


def int_arg(action, sr):
    for child in action:
        if child.tag == "Int" and child.attrib.get("sr") == sr:
            return child.attrib.get("val") or child_text(child, "var") or "".join(child.itertext()).strip()
    return None


def bundle_values(action):
    bundle = action.find("Bundle[@sr='arg0']")
    values = {}
    if bundle is None:
        return values
    vals = bundle.find("Vals")
    if vals is None:
        return values
    for child in vals:
        if child.tag.endswith("-type"):
            continue
        values[child.tag] = child.text or ""
    return values


def task_by_name(root, name):
    for task in root.iter("Task"):
        if child_text(task, "nme") == name:
            return task
    raise ValueError(f"Task not found: {name}")


def action_after_step(task, step):
    actions = list(task.findall("Action"))
    for index, action in enumerate(actions):
        if child_text(action, "code") == "547" and str_arg(action, "arg0") == "%SSUIStep" and str_arg(action, "arg1") == step:
            if index + 1 >= len(actions):
                raise ValueError(f"No action after step: {step}")
            return index, action, actions[index + 1], actions
    raise ValueError(f"Step not found: {step}")


def action_summary(action):
    values = bundle_values(action)
    return {
        "sr": action.attrib.get("sr"),
        "code": child_text(action, "code"),
        "se": child_text(action, "se"),
        "arg0": str_arg(action, "arg0"),
        "arg1": str_arg(action, "arg1"),
        "arg2": str_arg(action, "arg2"),
        "timeout_arg3": int_arg(action, "arg3"),
        "continue_arg4": int_arg(action, "arg4"),
        "ActionId": values.get("ActionId", ""),
        "ActionType": values.get("ActionType", ""),
        "FieldSelectionType": values.get("FieldSelectionType", ""),
        "NearbyText": values.get("NearbyText", ""),
        "TextToWrite": values.get("TextToWrite", ""),
        "ActionPoint": values.get("ActionPoint", ""),
        "BLURB": values.get("com.twofortyfouram.locale.intent.extra.BLURB", ""),
        "plugininstanceid": values.get("plugininstanceid", ""),
        "plugintypeid": values.get("plugintypeid", ""),
        "bundle": values,
    }


def clone_with_sr(action, sr_value):
    cloned = copy.deepcopy(action)
    cloned.attrib["sr"] = sr_value
    return cloned


def xml_bytes(element):
    return ET.tostring(element, encoding="utf-8")


def local_context(actions, index):
    context = {}
    for offset in [-3, -2, -1, 0, 1, 2, 3, 4]:
        pos = index + offset
        if 0 <= pos < len(actions):
            action = actions[pos]
            context[str(offset)] = {
                "sr": action.attrib.get("sr"),
                "code": child_text(action, "code"),
                "arg0": str_arg(action, "arg0"),
                "arg1": str_arg(action, "arg1"),
                "arg2": str_arg(action, "arg2"),
            }
    return context


def load(path):
    data = path.read_bytes()
    return data, ET.fromstring(data), hashlib.sha256(data).hexdigest().upper()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--v15a", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    v15a_data, v15a_root, v15a_sha = load(Path(args.v15a))
    target_data, target_root, target_sha = load(Path(args.target))

    v15a_task = task_by_name(v15a_root, "FINAL Send Sheet")
    target_task = task_by_name(target_root, "AIW27B_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE")
    v_index, v_step, v_action, v_actions = action_after_step(v15a_task, "SEARCH_ICON")
    t_index, t_step, t_action, t_actions = action_after_step(target_task, "SEARCH_ICON")

    v_summary = action_summary(v_action)
    t_summary = action_summary(t_action)
    v_as_target_sr = clone_with_sr(v_action, t_action.attrib.get("sr", ""))
    exact_bytes_equal = xml_bytes(v_action) == xml_bytes(t_action)
    equal_if_sr_adjusted = xml_bytes(v_as_target_sr) == xml_bytes(t_action)
    semantic_fields = sorted(set(v_summary) | set(t_summary))
    semantic_drift = {}
    for key in semantic_fields:
        if key == "sr":
            continue
        if v_summary.get(key) != t_summary.get(key):
            semantic_drift[key] = {"v15a": v_summary.get(key), "target": t_summary.get(key)}

    output = {
        "v15a_sha256": v15a_sha,
        "target_sha256": target_sha,
        "v15a_action_index": v_index + 1,
        "target_action_index": t_index + 1,
        "v15a_action_sr": v_action.attrib.get("sr"),
        "target_action_sr": t_action.attrib.get("sr"),
        "exact_node_bytes_equal": exact_bytes_equal,
        "node_bytes_equal_if_sr_adjusted": equal_if_sr_adjusted,
        "semantic_drift_excluding_sr": semantic_drift,
        "v15a_summary": v_summary,
        "target_summary": t_summary,
        "v15a_context": local_context(v_actions, v_index),
        "target_context": local_context(t_actions, t_index),
    }
    Path(args.out).write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
