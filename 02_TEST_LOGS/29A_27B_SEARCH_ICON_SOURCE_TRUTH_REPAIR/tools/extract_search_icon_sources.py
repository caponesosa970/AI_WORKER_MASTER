import argparse
import hashlib
import json
import re
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


def vals(action):
    out = {}
    bundle = action.find("Bundle[@sr='arg0']")
    if bundle is None:
        return out
    values = bundle.find("Vals")
    if values is None:
        return out
    for child in list(values):
        if child.tag.endswith("-type"):
            continue
        out[child.tag] = child.text or ""
    return out


def action_summary(action):
    values = vals(action)
    return {
        "sr": action.attrib.get("sr"),
        "code": child_text(action, "code"),
        "se": child_text(action, "se"),
        "arg0": str_arg(action, "arg0"),
        "arg1": str_arg(action, "arg1"),
        "arg2": str_arg(action, "arg2"),
        "timeout_arg3": int_arg(action, "arg3"),
        "continue_arg4": int_arg(action, "arg4"),
        "ActionId": values.get("ActionId"),
        "ActionType": values.get("ActionType"),
        "FieldSelectionType": values.get("FieldSelectionType"),
        "NearbyText": values.get("NearbyText"),
        "TextToWrite": values.get("TextToWrite"),
        "ActionPoint": values.get("ActionPoint"),
        "BLURB": values.get("com.twofortyfouram.locale.intent.extra.BLURB"),
        "plugininstanceid": values.get("plugininstanceid"),
        "plugintypeid": values.get("plugintypeid"),
        "vals_keys": sorted(key for key in values if not key.endswith("-type")),
    }


def is_step_marker(action):
    return child_text(action, "code") == "547" and str_arg(action, "arg0") == "%SSUIStep"


def task_actions(path):
    data = path.read_bytes()
    root = ET.fromstring(data)
    sha = hashlib.sha256(data).hexdigest().upper()
    rows = []
    for task in root.iter("Task"):
        task_name = child_text(task, "nme") or "(unnamed)"
        actions = list(task.findall("Action"))
        for index, action in enumerate(actions):
            if is_step_marker(action):
                step = str_arg(action, "arg1") or ""
                next_action = actions[index + 1] if index + 1 < len(actions) else None
                if "SEARCH_ICON" in step and next_action is not None:
                    rows.append(
                        {
                            "source": path.name,
                            "sha256": sha,
                            "task": task_name,
                            "step_sr": action.attrib.get("sr"),
                            "step": step,
                            "plugin_after_step": action_summary(next_action),
                        }
                    )
            values = vals(action)
            blob = " ".join(
                [
                    values.get("ActionId") or "",
                    values.get("com.twofortyfouram.locale.intent.extra.BLURB") or "",
                ]
            )
            if child_text(action, "code") == "1732635924" and (
                "menu_search" in blob or re.search(r"\bSearch\b", blob)
            ):
                rows.append(
                    {
                        "source": path.name,
                        "sha256": sha,
                        "task": task_name,
                        "direct_plugin_sr": action.attrib.get("sr"),
                        "direct_plugin": action_summary(action),
                    }
                )
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", help="Write JSON to this path")
    parser.add_argument("xml", nargs="+", help="Tasker XML files to inspect")
    args = parser.parse_args()

    output = []
    for xml_path in args.xml:
        path = Path(xml_path)
        if not path.exists():
            output.append({"source": path.name, "missing": True})
            continue
        try:
            output.extend(task_actions(path))
        except Exception as exc:
            output.append({"source": path.name, "error": str(exc)})

    rendered = json.dumps(output, indent=2)
    if args.out:
        Path(args.out).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
