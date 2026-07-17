from __future__ import annotations

import argparse
import copy
import hashlib
import html
import json
import re
import time
import xml.etree.ElementTree as ET
from itertools import combinations
from pathlib import Path


EXPECTED_BASE_SHA = "9FB3A33852E12475CFA9A5D97F1157F67C69A9C0A007025CCD026BC9E26EB2A5"
AUTHORIZED_EXISTING = {237, 268, 270, 272, 276, 293}
HELPERS = {
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

COL_SEP = "|~AIW_FIXTURE_COL~|"
ROW_SEP = "|~AIW_FIXTURE_ROW~|"

ROLE_CONFIG = {
    "HIST_ARCHIVE": {
        "prefix": "%AIWFXHistArchive",
        "aliases": ["HIST_ARCHIVE"],
        "layer": "Archive",
        "columns": "A:C",
        "cap": 933,
        "status": "HISTORY",
    },
    "HIST_DEAD": {
        "prefix": "%AIWFXHistDead",
        "aliases": ["HIST_DEAD"],
        "layer": "DeadArchive",
        "columns": "A:A",
        "cap": 972,
        "status": "HISTORY",
    },
    "G14C_REAL": {
        "prefix": "%AIWFXG14CReal",
        "aliases": ["G14C_REAL", "REAL_SUCCESS"],
        "layer": "Sheet1",
        "columns": "A:Z",
        "cap": 980,
        "status": "NEW",
    },
    "G14C_RATE": {
        "prefix": "%AIWFXG14CRate",
        "aliases": ["G14C_RATE", "RATE_LIMIT_THEN_SUCCESS"],
        "layer": "Sheet1",
        "columns": "A:Z",
        "cap": 980,
        "status": "NEW",
    },
    "G14C_TIMEOUT": {
        "prefix": "%AIWFXG14CTimeout",
        "aliases": ["G14C_TIMEOUT", "TIMEOUT_EXHAUSTED"],
        "layer": "Sheet1",
        "columns": "A:Z",
        "cap": 980,
        "status": "NEW",
    },
    "G14C_QUOTA": {
        "prefix": "%AIWFXG14CQuota",
        "aliases": ["G14C_QUOTA", "QUOTA_429_NO_RETRY"],
        "layer": "Sheet1",
        "columns": "A:Z",
        "cap": 980,
        "status": "NEW",
    },
    "G14C_LEGACY": {
        "prefix": "%AIWFXG14CLegacy",
        "aliases": ["G14C_LEGACY", "LEGACY_RETRY_MIGRATION"],
        "layer": "Sheet1",
        "columns": "A:Z",
        "cap": 980,
        "status": "ERROR_OPENAI_RETRY",
    },
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=False)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


class TaskBuilder:
    def __init__(self) -> None:
        self.actions: list[str] = []

    def add(self, inner: str) -> None:
        self.actions.append(f'<Action sr="act{len(self.actions)}" ve="7">{inner}</Action>')

    def set(self, name: str, value: str, maths: bool = False) -> None:
        self.add(
            "<code>547</code>"
            f'<Str sr="arg0" ve="3">{esc(name)}</Str><Str sr="arg1" ve="3">{esc(value)}</Str>'
            f'<Int sr="arg2" val="0" /><Int sr="arg3" val="{1 if maths else 0}" />'
            '<Int sr="arg4" val="0" /><Int sr="arg5" val="3" /><Int sr="arg6" val="0" />'
        )

    def clear(self, name: str) -> None:
        self.add(
            "<code>549</code>"
            f'<Str sr="arg0" ve="3">{esc(name)}</Str>'
            '<Int sr="arg1" val="0" /><Int sr="arg2" val="0" /><Int sr="arg3" val="0" />'
        )

    def array_clear(self, name: str) -> None:
        self.add(f'<code>357</code><Str sr="arg0" ve="3">{esc(name)}</Str>')

    def add_value(self, name: str, amount: int = 1) -> None:
        self.add(
            "<code>888</code>"
            f'<Str sr="arg0" ve="3">{esc(name)}</Str><Int sr="arg1" val="{amount}" /><Int sr="arg2" val="0" />'
        )

    def if_(self, conditions: list[tuple[str, int, str]], joins: list[str] | None = None) -> None:
        joins = joins or []
        parts = ['<code>37</code><ConditionList sr="if">']
        for index, (lhs, op, rhs) in enumerate(conditions):
            parts.append(
                f'<Condition sr="c{index}" ve="3"><lhs>{esc(lhs)}</lhs><op>{op}</op><rhs>{esc(rhs)}</rhs></Condition>'
            )
            if index < len(conditions) - 1:
                parts.append(f'<bool{index}>{esc(joins[index] if index < len(joins) else "And")}</bool{index}>')
        parts.append("</ConditionList>")
        self.add("".join(parts))

    def else_(self) -> None:
        self.add("<code>43</code>")

    def endif(self) -> None:
        self.add("<code>38</code>")

    def for_(self, variable: str, items: str) -> None:
        self.add(
            "<code>39</code>"
            f'<Str sr="arg0" ve="3">{esc(variable)}</Str><Str sr="arg1" ve="3">{esc(items)}</Str>'
            '<Int sr="arg2" val="0" />'
        )

    def endfor(self) -> None:
        self.add("<code>40</code>")

    def wait(self, seconds: int) -> None:
        self.add(
            f'<code>30</code><Int sr="arg0" val="0" /><Int sr="arg1" val="{seconds}" />'
            '<Int sr="arg2" val="0" /><Int sr="arg3" val="0" /><Int sr="arg4" val="0" />'
        )

    def stop(self) -> None:
        self.add('<code>137</code><Int sr="arg0" val="0" /><Str sr="arg1" ve="3" />')

    def perform(self, task_name: str, par1: str = "", par2: str = "") -> None:
        self.add(
            "<code>130</code>"
            f'<Str sr="arg0" ve="3">{esc(task_name)}</Str><Int sr="arg1"><var>100</var></Int>'
            '<Int sr="arg10" val="0" />'
            f'<Str sr="arg2" ve="3">{esc(par1)}</Str><Str sr="arg3" ve="3">{esc(par2)}</Str>'
            '<Str sr="arg4" ve="3" /><Int sr="arg5" val="0" /><Int sr="arg6" val="0" />'
            '<Str sr="arg7" ve="3" /><Int sr="arg8" val="0" /><Int sr="arg9" val="0" />'
        )

    def plugin(self, action: ET.Element) -> None:
        node = copy.deepcopy(action)
        node.set("sr", f"act{len(self.actions)}")
        self.actions.append(ET.tostring(node, encoding="unicode", short_empty_elements=True))


def raw_tasks(text: str) -> dict[int, str]:
    return {
        int(match.group(1)): match.group(0)
        for match in re.finditer(r'<Task sr="task(\d+)".*?</Task>', text, flags=re.DOTALL)
    }


def task_by_name(root: ET.Element, name: str) -> ET.Element:
    matches = [task for task in root.findall("Task") if task.findtext("nme") == name]
    if len(matches) != 1:
        raise RuntimeError(f"Task {name!r}: expected one, found {len(matches)}")
    return matches[0]


def plugin_templates(root: ET.Element) -> tuple[ET.Element, ET.Element]:
    get_action = next(
        action for action in task_by_name(root, "FINAL Confirm One Bound Row").findall("Action")
        if action.get("sr") == "act45"
    )
    update_action = next(
        action for action in task_by_name(root, "FINAL Send One Bound Row").findall("Action")
        if action.get("sr") == "act366"
    )
    if get_action.findtext("code") != "1810865467" or update_action.findtext("code") != "1461810131":
        raise RuntimeError("Source-proven AutoSheets templates changed")
    return get_action, update_action


def ensure_continue_after_error(action: ET.Element) -> None:
    code = action.find("code")
    if code is None:
        raise RuntimeError("Plugin action has no code")
    se = action.find("se")
    if se is None:
        se = ET.Element("se")
        se.text = "false"
        action.insert(list(action).index(code) + 1, se)
    else:
        se.text = "false"
    arg4 = action.find("Int[@sr='arg4']")
    if arg4 is not None:
        arg4.set("val", "1")


def plugin_parts(action: ET.Element) -> tuple[ET.Element, dict[str, object], ET.Element | None]:
    vals = action.find("Bundle/Vals")
    params_node = vals.find("parameters") if vals is not None else None
    if vals is None or params_node is None or not params_node.text:
        raise RuntimeError("AutoSheets template has no parameters")
    return params_node, json.loads(params_node.text), vals.find("com.twofortyfouram.locale.intent.extra.BLURB")


def set_relevant_variables(action: ET.Element, output_names: list[str]) -> None:
    relevant = action.find("Bundle/Vals/net.dinglisch.android.tasker.RELEVANT_VARIABLES")
    if relevant is None:
        return
    entries: list[str] = []
    for index, name in enumerate(output_names):
        entries.append(
            f'<_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES{index}>%{name}()\n{name}\n{name}'
            f'</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES{index}>'
        )
    offset = len(entries)
    entries.append(
        f'<_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES{offset}>%err\nError Code\n'
        f'Available with Continue Task After Error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES{offset}>'
    )
    entries.append(
        f'<_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES{offset + 1}>%errmsg\nError Message\n'
        f'Available with Continue Task After Error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES{offset + 1}>'
    )
    relevant.text = '<StringArray sr="">' + "".join(entries) + "</StringArray>"


def make_get(template: ET.Element, sheet: str, range_text: str, output_names: list[str]) -> ET.Element:
    action = copy.deepcopy(template)
    ensure_continue_after_error(action)
    params_node, params, blurb = plugin_parts(action)
    names = ",".join(output_names)
    params["_spreadSheet"]["sheetName"] = sheet
    params["output"]["range"] = range_text
    params["output"]["outputNames"] = names
    params["output"]["json"] = False
    params_node.text = json.dumps(params, separators=(",", ":"), ensure_ascii=False)
    if blurb is not None:
        blurb.text = (
            f"Spreadsheet configured\nSheet Name: {sheet}\nMode: Columns\n"
            f"Output Array Names: {names}\nRange: {range_text}"
        )
    set_relevant_variables(action, output_names)
    return action


def make_update(template: ET.Element, sheet: str, reference: str, fields: list[str]) -> ET.Element:
    action = copy.deepcopy(template)
    ensure_continue_after_error(action)
    params_node, params, blurb = plugin_parts(action)
    params["_spreadSheet"]["sheetName"] = sheet
    params["_spreadSheet"]["createSheetIfNeeded"] = False
    params["_cellsByReference"]["reference"] = reference
    params["_sheetData"]["data"] = COL_SEP.join(fields)
    params["_sheetData"]["majorDimension"] = "0"
    params["_sheetData"]["mode"] = "1"
    params["_sheetData"]["separator"] = COL_SEP
    params["_sheetData"]["lineSeparator"] = ROW_SEP
    params["_offlineSettings"]["updateLaterIfOffline"] = False
    params_node.text = json.dumps(params, separators=(",", ":"), ensure_ascii=False)
    if blurb is not None:
        blurb.text = (
            f"Spreadsheet configured\nSheet Name: {sheet}\nCell Reference: {reference}\n"
            f"Rows Or Columns: Rows\nData fields: {len(fields)}\nMode: Parsed"
        )
    return action


def invalid_to_flag(t: TaskBuilder, value: str, flag: str, *, blank_invalid: bool = True) -> None:
    patterns = [r"(?s)^%.*$", r"(?is).*#ERROR.*"]
    if blank_invalid:
        patterns.insert(0, r"(?s)^\s*$")
    for pattern in patterns:
        t.if_([(value, 4, pattern)])
        t.set(flag, "0")
        t.endif()


def require_equal(t: TaskBuilder, value: str, expected: str, flag: str) -> None:
    t.if_([(value, 3, expected)])
    t.set(flag, "0")
    t.endif()


def add_profile_state(t: TaskBuilder, profile: str, enabled: bool) -> None:
    t.add(
        '<code>159</code>'
        f'<Str sr="arg0" ve="3">{esc(profile)}</Str><Int sr="arg1" val="{1 if enabled else 0}" />'
    )


def action_list(raw_task: str) -> list[str]:
    return re.findall(r"<Action\b.*?</Action>", raw_task, flags=re.DOTALL)


def renumber(actions: list[str]) -> list[str]:
    return [re.sub(r'<Action sr="act\d+"', f'<Action sr="act{index}"', action, count=1) for index, action in enumerate(actions)]


def replace_actions(raw_task: str, actions: list[str]) -> str:
    stripped = re.sub(r"<Action\b.*?</Action>", "", raw_task, flags=re.DOTALL)
    insert_at = stripped.rfind("</Task>")
    return stripped[:insert_at] + "".join(renumber(actions)) + stripped[insert_at:]


def replace_string_arg(action: str, sr: str, new_value: str) -> str:
    pattern = rf'(<Str sr="{re.escape(sr)}" ve="3">).*?(</Str>)'
    result, count = re.subn(pattern, lambda m: m.group(1) + esc(new_value) + m.group(2), action, count=1, flags=re.DOTALL)
    if count != 1:
        raise RuntimeError(f"Unable to replace {sr} in action")
    return result


def task_xml(task_id: int, name: str, builder: TaskBuilder) -> str:
    stamp = int(time.time() * 1000)
    return (
        f'<Task sr="task{task_id}"><cdate>{stamp}</cdate><edate>{stamp}</edate>'
        f'<id>{task_id}</id><nme>{esc(name)}</nme><pri>100</pri><rty>0</rty><stayawake>true</stayawake>'
        + "".join(builder.actions)
        + "</Task>"
    )


def build_resolve_config() -> TaskBuilder:
    t = TaskBuilder()
    t.set("%AIWFixtureResolveResult", "FIXTURE_RESOLVE_START")
    t.set("%AIWFixtureBoundResolved", "0")
    for field in (
        "Role", "ConfiguredRole", "Layer", "Row", "Max", "Columns", "ID", "Sender", "Message",
        "Status", "RunID", "AuthToken", "CheckMode", "Cap",
    ):
        t.clear(f"%AIWFixtureBound{field}")
    for role, spec in ROLE_CONFIG.items():
        alias_regex = "^(?:" + "|".join(re.escape(alias) for alias in spec["aliases"]) + ")$"
        prefix = spec["prefix"]
        t.if_([("%par1", 4, alias_regex)])
        t.set("%AIWFixtureBoundRole", role)
        t.set("%AIWFixtureBoundConfiguredRole", f"{prefix}Role")
        t.set("%AIWFixtureBoundLayer", f"{prefix}Layer")
        t.set("%AIWFixtureBoundRow", f"{prefix}Row")
        t.set("%AIWFixtureBoundMax", f"{prefix}Max")
        t.set("%AIWFixtureBoundColumns", f"{prefix}Columns")
        t.set("%AIWFixtureBoundID", f"{prefix}ID")
        t.set("%AIWFixtureBoundSender", f"{prefix}Sender")
        t.set("%AIWFixtureBoundMessage", f"{prefix}Message")
        t.set("%AIWFixtureBoundStatus", f"{prefix}Status")
        t.set("%AIWFixtureBoundExpectedLayer", spec["layer"])
        t.set("%AIWFixtureBoundExpectedColumns", spec["columns"])
        t.set("%AIWFixtureBoundExpectedStatus", spec["status"])
        t.set("%AIWFixtureBoundCap", str(spec["cap"]))
        t.set("%AIWFixtureBoundCheckMode", "CONFIG")
        t.set("%AIWFixtureBoundRunID", "%AIWValidationRunID")
        t.set("%AIWFixtureBoundAuthToken", "%AIWFXAuthToken")
        t.set("%AIWFixtureBoundResolved", "1")
        t.endif()
    t.if_([("%AIWFixtureBoundResolved", 3, "1")])
    t.set("%AIWFixtureResolveResult", "FIXTURE_ROLE_HOLD")
    t.stop()
    t.endif()
    t.set("%fxr_valid", "1")
    for value in (
        "%AIWValidationRunID", "%AIWFXAuthRunID", "%AIWFXAuthToken", "%AIWFixtureBoundConfiguredRole",
        "%AIWFixtureBoundLayer", "%AIWFixtureBoundRow", "%AIWFixtureBoundMax", "%AIWFixtureBoundColumns",
        "%AIWFixtureBoundID", "%AIWFixtureBoundSender", "%AIWFixtureBoundMessage", "%AIWFixtureBoundStatus",
    ):
        invalid_to_flag(t, value, "%fxr_valid")
    require_equal(t, "%AIWFXConfigVersion", "FIXTURE_CONTRACT_V1", "%fxr_valid")
    t.if_([("%AIWFXAuthState", 5, r"^(ARMED|ACTIVE)$")])
    t.set("%fxr_valid", "0")
    t.endif()
    require_equal(t, "%AIWFXAuthRunID", "%AIWValidationRunID", "%fxr_valid")
    require_equal(t, "%AIWFixtureBoundConfiguredRole", "%AIWFixtureBoundRole", "%fxr_valid")
    require_equal(t, "%AIWFixtureBoundLayer", "%AIWFixtureBoundExpectedLayer", "%fxr_valid")
    require_equal(t, "%AIWFixtureBoundColumns", "%AIWFixtureBoundExpectedColumns", "%fxr_valid")
    require_equal(t, "%AIWFixtureBoundStatus", "%AIWFixtureBoundExpectedStatus", "%fxr_valid")
    t.if_([("%AIWFixtureBoundRow", 5, r"^[0-9]{1,4}$"), ("%AIWFixtureBoundMax", 5, r"^[0-9]{1,4}$")], ["Or"])
    t.set("%fxr_valid", "0")
    t.endif()
    t.if_([("%AIWFixtureBoundID", 5, r"^AIWFX-%AIWValidationRunID-[A-Z0-9_-]+$")])
    t.set("%fxr_valid", "0")
    t.endif()
    t.if_([("%AIWFixtureBoundSender", 5, r"^AIW_VALIDATION_%AIWValidationRunID_[A-Z0-9_-]+$")])
    t.set("%fxr_valid", "0")
    t.endif()
    t.if_([("%AIWFixtureBoundMessage", 5, r"^AIW validation %AIWValidationRunID [A-Z0-9_-]+$")])
    t.set("%fxr_valid", "0")
    t.endif()
    t.if_([("%fxr_valid", 3, "1")])
    t.set("%AIWFixtureResolveResult", "FIXTURE_CONFIG_HOLD")
    t.set("%AIWFixtureBoundResolved", "0")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureBoundRow", 6, "2"), ("%AIWFixtureBoundRow", 7, "%AIWFixtureBoundMax"), ("%AIWFixtureBoundMax", 7, "%AIWFixtureBoundCap")], ["Or", "Or"])
    t.set("%AIWFixtureResolveResult", "FIXTURE_OUT_OF_BOUNDS_HOLD")
    t.set("%AIWFixtureBoundResolved", "0")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureBoundLayer", 2, "Sheet1"), ("%AIWFixtureBoundRow", 4, r"^(144|145|146|147)$")], ["And"])
    t.set("%AIWFixtureResolveResult", "FIXTURE_PROTECTED_ROW_HOLD")
    t.set("%AIWFixtureBoundResolved", "0")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureBoundLayer", 2, "Sheet1"), ("%AIWFXProtectedSheet1Rows", 4, r"(^|,)%AIWFixtureBoundRow(,|$)")], ["And"])
    t.set("%AIWFixtureResolveResult", "FIXTURE_PROTECTED_ROW_HOLD")
    t.set("%AIWFixtureBoundResolved", "0")
    t.stop()
    t.endif()
    t.set("%AIWFixtureResolveResult", "FIXTURE_BINDING_READY")
    return t


def build_resolve_runtime() -> TaskBuilder:
    t = TaskBuilder()
    t.set("%AIWFixtureResolveResult", "RUNTIME_FIXTURE_RESOLVE_START")
    t.set("%AIWFixtureBoundResolved", "0")
    t.set("%fxrr_matches", "0")
    for field in ("Role", "Layer", "Row", "Max", "Columns", "ID", "Sender", "Message", "Status", "RunID", "AuthToken", "CheckMode", "Cap"):
        t.clear(f"%AIWFixtureBound{field}")
    mappings = [
        ("MAIN", "%AIWPhase1MainRow", "%AIWPhase1MainID", "PHASE1_MAIN", None),
        ("MAIN", "%AIWPhase2MainRow1", "%AIWPhase2FirstMovedID", "PHASE2_MAIN_FIRST", None),
        ("MAIN", "%AIWPhase2MainRow2", "%AIWPhase2FIFOID1", "PHASE2_MAIN_FIFO1", None),
        ("MAIN", "%AIWPhase2MainRow3", "%AIWPhase2FIFOID2", "PHASE2_MAIN_FIFO2", None),
        ("MAIN", "%AIWValidationLastMainRow", "%AIWPhase6TestID", "PHASE6_MAIN", "6"),
        ("OVERFLOW", "%AIWPhase1OverflowRow", "%AIWPhase1OverflowID", "PHASE1_OVERFLOW", None),
        ("OVERFLOW", "%AIWPhase2OverflowRow1", "%AIWPhase2FIFOID1", "PHASE2_OVERFLOW_FIFO1", None),
        ("OVERFLOW", "%AIWPhase2OverflowRow2", "%AIWPhase2FIFOID2", "PHASE2_OVERFLOW_FIFO2", None),
        ("JOURNAL", "%AIWPhase1JournalRow1", "%AIWPhase1MainID", "PHASE1_JOURNAL_MAIN", None),
        ("JOURNAL", "%AIWPhase1JournalRow2", "%AIWPhase1OverflowID", "PHASE1_JOURNAL_OVERFLOW", None),
        ("JOURNAL", "%AIWPhase2JournalRow1", "%AIWPhase2FIFOID1", "PHASE2_JOURNAL_FIFO1", None),
        ("JOURNAL", "%AIWPhase2JournalRow2", "%AIWPhase2FIFOID2", "PHASE2_JOURNAL_FIFO2", None),
        ("JOURNAL", "%AIWValidationLastJournalRow", "%AIWPhase6TestID", "PHASE6_JOURNAL", "6"),
        ("JOURNAL", "%AIWPhase4JournalRow", "%AIWPhase4InboundID", "PHASE4_JOURNAL", None),
    ]
    for layer, row_var, id_var, role, required_phase in mappings:
        conditions = [("%par1", 2, layer), ("%par2", 2, row_var), (row_var, 4, r"^[0-9]{1,4}$")]
        if required_phase is not None:
            conditions.append(("%AIWValidationPhase", 2, required_phase))
        t.if_(conditions, ["And"] * (len(conditions) - 1))
        t.add_value("%fxrr_matches")
        t.set("%AIWFixtureBoundRole", role)
        t.set("%AIWFixtureBoundLayer", layer)
        t.set("%AIWFixtureBoundRow", row_var)
        t.set("%AIWFixtureBoundID", id_var)
        t.endif()
    t.if_([("%fxrr_matches", 3, "1")])
    t.set("%AIWFixtureResolveResult", "RUNTIME_FIXTURE_OWNERSHIP_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureBoundLayer", 2, "MAIN")])
    t.set("%AIWFixtureBoundLayer", "Sheet1")
    t.set("%AIWFixtureBoundMax", "%AIWFXMainMax")
    t.set("%AIWFixtureBoundColumns", "%AIWFXMainColumns")
    t.set("%AIWFixtureBoundCap", "980")
    t.endif()
    t.if_([("%AIWFixtureBoundLayer", 2, "OVERFLOW")])
    t.set("%AIWFixtureBoundLayer", "OverflowInbox")
    t.set("%AIWFixtureBoundMax", "%AIWFXOverflowMax")
    t.set("%AIWFixtureBoundColumns", "%AIWFXOverflowColumns")
    t.set("%AIWFixtureBoundCap", "986")
    t.endif()
    t.if_([("%AIWFixtureBoundLayer", 2, "JOURNAL")])
    t.set("%AIWFixtureBoundLayer", "IngressJournal")
    t.set("%AIWFixtureBoundMax", "%AIWFXJournalMax")
    t.set("%AIWFixtureBoundColumns", "%AIWFXJournalColumns")
    t.set("%AIWFixtureBoundCap", "1001")
    t.endif()
    t.set("%AIWFixtureBoundRunID", "%AIWValidationRunID")
    t.set("%AIWFixtureBoundAuthToken", "%AIWFXAuthToken")
    t.set("%AIWFixtureBoundCheckMode", "RUNTIME")
    t.set("%AIWFixtureBoundStatus", "RUNTIME_OWNED")
    t.set("%AIWFixtureBoundResolved", "1")
    t.set("%fxrr_valid", "1")
    for value in ("%AIWFixtureBoundID", "%AIWFixtureBoundRow", "%AIWFixtureBoundMax", "%AIWFixtureBoundColumns", "%AIWFXAuthToken"):
        invalid_to_flag(t, value, "%fxrr_valid")
    require_equal(t, "%AIWFXAuthState", "ACTIVE", "%fxrr_valid")
    require_equal(t, "%AIWFXAuthRunID", "%AIWValidationRunID", "%fxrr_valid")
    require_equal(t, "%AIWFXAuthConsumedRun", "%AIWValidationRunID", "%fxrr_valid")
    t.if_([("%AIWFixtureBoundID", 5, r"^[0-9]{20,40}$")])
    t.set("%fxrr_valid", "0")
    t.endif()
    t.if_([("%AIWFixtureBoundRow", 5, r"^[0-9]{1,4}$"), ("%AIWFixtureBoundMax", 5, r"^[0-9]{1,4}$")], ["Or"])
    t.set("%fxrr_valid", "0")
    t.endif()
    t.if_([("%AIWFixtureBoundLayer", 2, "Sheet1"), ("%AIWFixtureBoundColumns", 3, "A:Z")], ["And"])
    t.set("%fxrr_valid", "0")
    t.endif()
    t.if_([("%AIWFixtureBoundLayer", 4, r"^(OverflowInbox|IngressJournal)$"), ("%AIWFixtureBoundColumns", 3, "A:N")], ["And"])
    t.set("%fxrr_valid", "0")
    t.endif()
    t.if_([("%fxrr_valid", 3, "1")])
    t.set("%AIWFixtureResolveResult", "RUNTIME_FIXTURE_CONFIG_HOLD")
    t.set("%AIWFixtureBoundResolved", "0")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureBoundRow", 6, "2"), ("%AIWFixtureBoundRow", 7, "%AIWFixtureBoundMax"), ("%AIWFixtureBoundMax", 7, "%AIWFixtureBoundCap")], ["Or", "Or"])
    t.set("%AIWFixtureResolveResult", "FIXTURE_OUT_OF_BOUNDS_HOLD")
    t.set("%AIWFixtureBoundResolved", "0")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureBoundLayer", 2, "Sheet1"), ("%AIWFixtureBoundRow", 4, r"^(144|145|146|147)$")], ["And"])
    t.set("%AIWFixtureResolveResult", "FIXTURE_PROTECTED_ROW_HOLD")
    t.set("%AIWFixtureBoundResolved", "0")
    t.stop()
    t.endif()
    t.set("%AIWFixtureResolveResult", "RUNTIME_FIXTURE_BINDING_READY")
    return t


def emit_bounded_read(t: TaskBuilder, action: ET.Element, arrays: list[str], prefix: str) -> None:
    t.set("%fxi_read_ok", "0")
    t.for_("%fxi_try", "1,2")
    t.if_([("%fxi_read_ok", 3, "1")])
    t.if_([("%fxi_try", 7, "1")])
    t.wait(3)
    t.endif()
    for name in arrays:
        t.array_clear(f"%{name}")
        t.clear(f"%{name}1")
        t.clear(f"%{prefix}_{name}_value")
        t.clear(f"%{prefix}_{name}_blank")
    t.clear("%err")
    t.clear("%errmsg")
    t.add_value("%AIWFixtureInspectReads")
    t.plugin(action)
    t.set("%fxi_read_ok", "1")
    t.if_([("%err", 4, r"^[1-9][0-9]*$")])
    t.set("%fxi_read_ok", "0")
    t.endif()
    t.if_([("%err", 4, r"(?s)^%.*$|(?is).*#ERROR.*")])
    t.set("%fxi_read_ok", "0")
    t.endif()
    for name in arrays:
        t.if_([(f"%{name}(#)", 7, "1")])
        t.set("%fxi_read_ok", "0")
        t.endif()
    t.endif()
    t.endfor()
    t.if_([("%fxi_read_ok", 3, "1")])
    t.set("%AIWFixtureInspectResult", "FIXTURE_READ_PLUGIN_HOLD")
    t.stop()
    t.endif()
    for name in arrays:
        t.set(f"%{prefix}_{name}_value", f"%{name}(1)")
        t.set(f"%{prefix}_{name}_blank", "0")
        t.if_([(f"%{name}(#)", 2, "0"), (f"%{prefix}_{name}_value", 4, rf"(?s)^$|^[%]{re.escape(name)}[0-9]+$")], ["Or"])
        t.set(f"%{prefix}_{name}_blank", "1")
        t.endif()
        t.if_([(f"%{prefix}_{name}_value", 4, r"(?is).*#ERROR.*")])
        t.set("%fxi_read_ok", "0")
        t.endif()
    t.if_([("%fxi_read_ok", 3, "1")])
    t.set("%AIWFixtureInspectResult", "FIXTURE_READ_UNRESOLVED_HOLD")
    t.stop()
    t.endif()


def emit_blank_and_valid_classification(t: TaskBuilder, arrays: list[str], prefix: str) -> None:
    t.set("%fxi_all_blank", "1")
    for name in arrays:
        t.if_([(f"%{prefix}_{name}_blank", 3, "1")])
        t.set("%fxi_all_blank", "0")
        t.endif()
    t.if_([("%fxi_all_blank", 2, "1")])
    t.set("%AIWFixtureInspectClass", "BLANK")
    t.set("%AIWFixtureInspectResult", "FIXTURE_ROW_BLANK")
    t.stop()
    t.endif()


def require_cell_equal(t: TaskBuilder, prefix: str, name: str, expected: str) -> None:
    t.if_([(f"%{prefix}_{name}_blank", 2, "1"), (f"%{prefix}_{name}_value", 3, expected)], ["Or"])
    t.set("%fxi_owned", "0")
    t.endif()


def require_cell_nonblank(t: TaskBuilder, prefix: str, name: str) -> None:
    t.if_([(f"%{prefix}_{name}_blank", 2, "1"), (f"%{prefix}_{name}_value", 4, r"(?s)^%.*$|(?is).*#ERROR.*")], ["Or"])
    t.set("%fxi_owned", "0")
    t.endif()


def require_cell_blank(t: TaskBuilder, prefix: str, name: str) -> None:
    t.if_([(f"%{prefix}_{name}_blank", 3, "1")])
    t.set("%fxi_owned", "0")
    t.endif()


def emit_bound_guard(t: TaskBuilder) -> None:
    t.set("%fxi_bound_ok", "1")
    for value in ("%AIWFixtureBoundRole", "%AIWFixtureBoundLayer", "%AIWFixtureBoundRow", "%AIWFixtureBoundMax", "%AIWFixtureBoundColumns", "%AIWFixtureBoundID", "%AIWFixtureBoundRunID", "%AIWFixtureBoundAuthToken"):
        invalid_to_flag(t, value, "%fxi_bound_ok")
    require_equal(t, "%AIWFixtureBoundResolved", "1", "%fxi_bound_ok")
    require_equal(t, "%AIWFixtureBoundRunID", "%AIWValidationRunID", "%fxi_bound_ok")
    require_equal(t, "%AIWFixtureBoundAuthToken", "%AIWFXAuthToken", "%fxi_bound_ok")
    require_equal(t, "%AIWFXAuthRunID", "%AIWValidationRunID", "%fxi_bound_ok")
    t.if_([("%AIWFXAuthState", 5, r"^(ARMED|ACTIVE)$")])
    t.set("%fxi_bound_ok", "0")
    t.endif()
    t.if_([("%AIWFixtureBoundRow", 5, r"^[0-9]{1,4}$"), ("%AIWFixtureBoundMax", 5, r"^[0-9]{1,4}$")], ["Or"])
    t.set("%fxi_bound_ok", "0")
    t.endif()
    t.if_([("%fxi_bound_ok", 3, "1")])
    t.set("%AIWFixtureInspectResult", "FIXTURE_BOUND_AUTH_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureBoundRow", 6, "2"), ("%AIWFixtureBoundRow", 7, "%AIWFixtureBoundMax"), ("%AIWFixtureBoundMax", 7, "%AIWFixtureBoundCap")], ["Or", "Or"])
    t.set("%AIWFixtureInspectResult", "FIXTURE_OUT_OF_BOUNDS_HOLD")
    t.stop()
    t.endif()


def build_inspect_bound() -> TaskBuilder:
    t = TaskBuilder()
    t.set("%AIWFixtureInspectResult", "FIXTURE_INSPECT_START")
    t.set("%AIWFixtureInspectClass", "UNRESOLVED")
    t.set("%AIWFixtureInspectReads", "0")
    emit_bound_guard(t)
    t.if_([("%AIWFixtureBoundLayer", 2, "Sheet1")])
    t.perform("AIW Validation Fixture Inspect Sheet1", "%par1")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureBoundLayer", 4, r"^(Archive|DeadArchive)$")])
    t.perform("AIW Validation Fixture Inspect History", "%par1")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureBoundLayer", 4, r"^(OverflowInbox|IngressJournal)$")])
    t.perform("AIW Validation Fixture Inspect Queue Stores", "%par1")
    t.stop()
    t.endif()
    t.set("%AIWFixtureInspectResult", "FIXTURE_LAYER_HOLD")
    return t


def build_inspect_layers(root: ET.Element, selected_layers: set[str]) -> TaskBuilder:
    get_template, _ = plugin_templates(root)
    names_by_layer = {
        "Sheet1": [f"fx_{c}" for c in "abcdefghijklmnopqrstuvwxyz"],
        "Archive": [f"fx_{c}" for c in "abc"],
        "DeadArchive": ["fx_a"],
        "OverflowInbox": [f"fx_{c}" for c in "abcdefghijklmn"],
        "IngressJournal": [f"fx_{c}" for c in "abcdefghijklmn"],
    }
    ranges = {"Sheet1": "A%AIWFixtureBoundRow:Z%AIWFixtureBoundRow", "Archive": "A%AIWFixtureBoundRow:C%AIWFixtureBoundRow", "DeadArchive": "A%AIWFixtureBoundRow:A%AIWFixtureBoundRow", "OverflowInbox": "A%AIWFixtureBoundRow:N%AIWFixtureBoundRow", "IngressJournal": "A%AIWFixtureBoundRow:N%AIWFixtureBoundRow"}
    names_by_layer = {layer: names for layer, names in names_by_layer.items() if layer in selected_layers}
    reads = {layer: make_get(get_template, layer, ranges[layer], names) for layer, names in names_by_layer.items()}
    t = TaskBuilder()
    t.set("%AIWFixtureInspectResult", "FIXTURE_INSPECT_START")
    t.set("%AIWFixtureInspectClass", "UNRESOLVED")
    t.set("%AIWFixtureInspectReads", "0")
    emit_bound_guard(t)
    for layer, names in names_by_layer.items():
        t.if_([("%AIWFixtureBoundLayer", 2, layer)])
        emit_bounded_read(t, reads[layer], names, "fxv")
        emit_blank_and_valid_classification(t, names, "fxv")
        t.set("%fxi_owned", "1")
        if layer == "Sheet1":
            require_cell_equal(t, "fxv", "fx_a", "%AIWFixtureBoundID")
            if_config = [("%AIWFixtureBoundCheckMode", 2, "CONFIG")]
            t.if_(if_config)
            require_cell_equal(t, "fxv", "fx_b", "%AIWFixtureBoundSender")
            require_cell_equal(t, "fxv", "fx_c", "%AIWFixtureBoundMessage")
            t.if_([("%par1", 2, "SETUP_READBACK")])
            require_cell_equal(t, "fxv", "fx_d", "%AIWFixtureBoundStatus")
            t.else_()
            t.if_([("%fxv_fx_d_blank", 2, "1"), ("%fxv_fx_d_value", 5, r"^(NEW|PROCESSING|REVIEW_READY|ERROR_OPENAI_RETRY|ERROR_OPENAI_TIMEOUT|ERROR_OPENAI_RATE_LIMIT|ERROR_OPENAI_QUOTA|ERROR_OPENAI_PLUGIN|ERROR_OPENAI_REVIEW|SENT_REVIEW_REQUIRED)$")], ["Or"])
            t.set("%fxi_owned", "0")
            t.endif()
            t.endif()
            t.endif()
            t.if_([("%AIWFixtureBoundCheckMode", 2, "RUNTIME")])
            require_cell_nonblank(t, "fxv", "fx_b")
            require_cell_nonblank(t, "fxv", "fx_c")
            require_cell_nonblank(t, "fxv", "fx_d")
            t.endif()
            for c in "jklmnopqrstuvwxyz":
                require_cell_blank(t, "fxv", f"fx_{c}")
        elif layer == "Archive":
            require_cell_equal(t, "fxv", "fx_a", "%AIWFixtureBoundID")
            require_cell_equal(t, "fxv", "fx_b", "%AIWFixtureBoundSender")
            require_cell_equal(t, "fxv", "fx_c", "%AIWFixtureBoundMessage")
        elif layer == "DeadArchive":
            require_cell_equal(t, "fxv", "fx_a", "%AIWFixtureBoundID")
        elif layer in {"OverflowInbox", "IngressJournal"}:
            require_cell_equal(t, "fxv", "fx_b", "%AIWFixtureBoundID")
            for c in ("a", "c", "d", "e", "k", "l", "m"):
                require_cell_nonblank(t, "fxv", f"fx_{c}")
        t.if_([("%fxi_owned", 2, "1")])
        t.set("%AIWFixtureInspectClass", "OWNED")
        t.set("%AIWFixtureInspectResult", "FIXTURE_ROW_OWNED")
        t.else_()
        t.set("%AIWFixtureInspectClass", "OCCUPIED")
        t.set("%AIWFixtureInspectResult", "FIXTURE_ROW_OCCUPIED_HOLD")
        t.endif()
        t.stop()
        t.endif()
    t.set("%AIWFixtureInspectResult", "FIXTURE_LAYER_HELPER_HOLD")
    return t


def emit_quick_bound_guard(t: TaskBuilder) -> None:
    t.if_([
        ("%AIWFixtureBoundResolved", 3, "1"),
        ("%AIWFixtureBoundRunID", 3, "%AIWValidationRunID"),
        ("%AIWFixtureBoundAuthToken", 3, "%AIWFXAuthToken"),
        ("%AIWFXAuthState", 5, r"^(ARMED|ACTIVE)$"),
    ], ["Or", "Or", "Or"])
    t.set("%AIWFixtureInspectResult", "FIXTURE_BOUND_AUTH_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureBoundRow", 6, "2"), ("%AIWFixtureBoundRow", 7, "%AIWFixtureBoundMax"), ("%AIWFixtureBoundMax", 7, "%AIWFixtureBoundCap")], ["Or", "Or"])
    t.set("%AIWFixtureInspectResult", "FIXTURE_OUT_OF_BOUNDS_HOLD")
    t.stop()
    t.endif()


def build_sheet1_read(root: ET.Element) -> TaskBuilder:
    get_template, _ = plugin_templates(root)
    arrays = [f"AIWFXR_{c.upper()}" for c in "abcdefghijklmnopqrstuvwxyz"]
    read = make_get(get_template, "Sheet1", "A%AIWFixtureBoundRow:Z%AIWFixtureBoundRow", arrays)
    t = TaskBuilder()
    t.set("%AIWFixtureLayerReadResult", "FIXTURE_LAYER_READ_START")
    t.set("%AIWFixtureInspectReads", "0")
    emit_quick_bound_guard(t)
    emit_bounded_read(t, read, arrays, "fxg")
    t.set("%AIWFixtureLayerReadResult", "FIXTURE_LAYER_READ_READY")
    return t


def build_sheet1_classify() -> TaskBuilder:
    t = TaskBuilder()
    t.set("%AIWFixtureInspectResult", "FIXTURE_SHEET1_CLASSIFY_START")
    t.set("%AIWFixtureInspectClass", "UNRESOLVED")
    emit_quick_bound_guard(t)
    t.set("%fxs_all_blank", "1")
    for c in "abcdefghijklmnopqrstuvwxyz":
        array = f"AIWFXR_{c.upper()}"
        flag = f"%fxs_{c}_blank"
        t.set(flag, "0")
        t.if_([(f"%{array}(#)", 2, "0"), (f"%{array}(1)", 4, rf"(?s)^$|^[%]{array}[0-9]+$")], ["Or"])
        t.set(flag, "1")
        t.endif()
        t.if_([(flag, 3, "1")])
        t.set("%fxs_all_blank", "0")
        t.endif()
        t.if_([(f"%{array}(1)", 4, r"(?is).*#ERROR.*")])
        t.set("%AIWFixtureInspectResult", "FIXTURE_READ_UNRESOLVED_HOLD")
        t.stop()
        t.endif()
    t.if_([("%fxs_all_blank", 2, "1")])
    t.set("%AIWFixtureInspectClass", "BLANK")
    t.set("%AIWFixtureInspectResult", "FIXTURE_ROW_BLANK")
    t.stop()
    t.endif()
    t.set("%fxi_owned", "1")
    t.if_([("%fxs_a_blank", 2, "1"), ("%AIWFXR_A(1)", 3, "%AIWFixtureBoundID")], ["Or"])
    t.set("%fxi_owned", "0")
    t.endif()
    t.if_([("%AIWFixtureBoundCheckMode", 2, "CONFIG")])
    for c, expected in (("b", "%AIWFixtureBoundSender"), ("c", "%AIWFixtureBoundMessage")):
        t.if_([(f"%fxs_{c}_blank", 2, "1"), (f"%AIWFXR_{c.upper()}(1)", 3, expected)], ["Or"])
        t.set("%fxi_owned", "0")
        t.endif()
    t.if_([("%par1", 2, "SETUP_READBACK")])
    t.if_([("%fxs_d_blank", 2, "1"), ("%AIWFXR_D(1)", 3, "%AIWFixtureBoundStatus")], ["Or"])
    t.set("%fxi_owned", "0")
    t.endif()
    t.else_()
    t.if_([("%fxs_d_blank", 2, "1"), ("%AIWFXR_D(1)", 5, r"^(NEW|PROCESSING|REVIEW_READY|ERROR_OPENAI_RETRY|ERROR_OPENAI_TIMEOUT|ERROR_OPENAI_RATE_LIMIT|ERROR_OPENAI_QUOTA|ERROR_OPENAI_PLUGIN|ERROR_OPENAI_REVIEW|SENT_REVIEW_REQUIRED)$")], ["Or"])
    t.set("%fxi_owned", "0")
    t.endif()
    t.endif()
    t.endif()
    t.if_([("%AIWFixtureBoundCheckMode", 2, "RUNTIME")])
    for c in "bcd":
        t.if_([(f"%fxs_{c}_blank", 2, "1"), (f"%AIWFXR_{c.upper()}(1)", 4, r"(?s)^%.*$|(?is).*#ERROR.*")], ["Or"])
        t.set("%fxi_owned", "0")
        t.endif()
    t.endif()
    for c in "jklmnopqrstuvwxyz":
        t.if_([(f"%fxs_{c}_blank", 3, "1")])
        t.set("%fxi_owned", "0")
        t.endif()
    t.if_([("%fxi_owned", 2, "1")])
    t.set("%AIWFixtureInspectClass", "OWNED")
    t.set("%AIWFixtureInspectResult", "FIXTURE_ROW_OWNED")
    t.else_()
    t.set("%AIWFixtureInspectClass", "OCCUPIED")
    t.set("%AIWFixtureInspectResult", "FIXTURE_ROW_OCCUPIED_HOLD")
    t.endif()
    return t


def build_sheet1_inspect_router() -> TaskBuilder:
    t = TaskBuilder()
    t.set("%AIWFixtureInspectResult", "FIXTURE_SHEET1_INSPECT_START")
    t.perform("AIW Validation Fixture Read Sheet1")
    t.if_([("%AIWFixtureLayerReadResult", 3, "FIXTURE_LAYER_READ_READY")])
    t.set("%AIWFixtureInspectResult", "%AIWFixtureLayerReadResult")
    t.stop()
    t.endif()
    t.perform("AIW Validation Fixture Classify Sheet1", "%par1")
    return t


def build_queue_inspect_router() -> TaskBuilder:
    t = TaskBuilder()
    t.set("%AIWFixtureInspectResult", "FIXTURE_QUEUE_INSPECT_START")
    t.if_([("%AIWFixtureBoundLayer", 2, "OverflowInbox")])
    t.perform("AIW Validation Fixture Inspect Overflow", "%par1")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureBoundLayer", 2, "IngressJournal")])
    t.perform("AIW Validation Fixture Inspect Journal", "%par1")
    t.stop()
    t.endif()
    t.set("%AIWFixtureInspectResult", "FIXTURE_QUEUE_LAYER_HOLD")
    return t


def validate_general_contract_values(t: TaskBuilder) -> None:
    t.set("%fxc_general_ok", "1")
    for value in ("%AIWFXMainMax", "%AIWFXOverflowMax", "%AIWFXJournalMax", "%AIWFXMainColumns", "%AIWFXOverflowColumns", "%AIWFXJournalColumns", "%AIWFXProtectedSheet1Rows"):
        invalid_to_flag(t, value, "%fxc_general_ok")
    require_equal(t, "%AIWFXMainColumns", "A:Z", "%fxc_general_ok")
    require_equal(t, "%AIWFXOverflowColumns", "A:N", "%fxc_general_ok")
    require_equal(t, "%AIWFXJournalColumns", "A:N", "%fxc_general_ok")
    t.if_([("%AIWFXMainMax", 5, r"^[0-9]{1,4}$"), ("%AIWFXOverflowMax", 5, r"^[0-9]{1,4}$"), ("%AIWFXJournalMax", 5, r"^[0-9]{1,4}$")], ["Or", "Or"])
    t.set("%fxc_general_ok", "0")
    t.endif()
    t.if_([("%AIWFXMainMax", 7, "980"), ("%AIWFXOverflowMax", 7, "986"), ("%AIWFXJournalMax", 7, "1001")], ["Or", "Or"])
    t.set("%fxc_general_ok", "0")
    t.endif()
    t.if_([("%AIWFXProtectedSheet1Rows", 5, r"(^|,)144(,|$)"), ("%AIWFXProtectedSheet1Rows", 5, r"(^|,)145(,|$)"), ("%AIWFXProtectedSheet1Rows", 5, r"(^|,)146(,|$)"), ("%AIWFXProtectedSheet1Rows", 5, r"(^|,)147(,|$)")], ["Or", "Or", "Or"])
    t.set("%fxc_general_ok", "0")
    t.endif()


def build_contract() -> TaskBuilder:
    t = TaskBuilder()
    t.set("%AIWFixtureContractResult", "FIXTURE_CONTRACT_START")
    t.set("%AIWFixtureContractReady", "0")
    t.set("%fxc_valid", "1")
    for value in ("%AIWValidationRunID", "%AIWFXConfigVersion", "%AIWFXAuthState", "%AIWFXAuthRunID", "%AIWFXAuthToken"):
        invalid_to_flag(t, value, "%fxc_valid")
    require_equal(t, "%AIWFXConfigVersion", "FIXTURE_CONTRACT_V1", "%fxc_valid")
    require_equal(t, "%AIWFXAuthRunID", "%AIWValidationRunID", "%fxc_valid")
    t.if_([("%AIWFXAuthToken", 5, r"^AIWFXAUTH-[A-Za-z0-9_-]{16,128}$")])
    t.set("%fxc_valid", "0")
    t.endif()
    t.if_([("%AIWFXAuthState", 5, r"^(ARMED|ACTIVE)$")])
    t.set("%fxc_valid", "0")
    t.endif()
    t.if_([("%AIWFXAuthState", 2, "ACTIVE"), ("%AIWFXAuthConsumedRun", 3, "%AIWValidationRunID")], ["And"])
    t.set("%fxc_valid", "0")
    t.endif()
    t.if_([("%AIWFXAuthState", 2, "ARMED"), ("%AIWFXAuthConsumedRun", 2, "%AIWValidationRunID")], ["And"])
    t.set("%fxc_valid", "0")
    t.endif()
    validate_general_contract_values(t)
    t.if_([("%fxc_general_ok", 3, "1")])
    t.set("%fxc_valid", "0")
    t.endif()
    prefixes = [spec["prefix"] for spec in ROLE_CONFIG.values()]
    sheet_prefixes = [spec["prefix"] for spec in ROLE_CONFIG.values() if spec["layer"] == "Sheet1"]
    for left, right in combinations(sheet_prefixes, 2):
        t.if_([(f"{left}Row", 2, f"{right}Row")])
        t.set("%fxc_valid", "0")
        t.endif()
    for left, right in combinations(prefixes, 2):
        t.if_([(f"{left}ID", 2, f"{right}ID")])
        t.set("%fxc_valid", "0")
        t.endif()
    t.if_([("%fxc_valid", 3, "1")])
    t.set("%AIWFixtureContractResult", "FIXTURE_CONTRACT_CONFIG_OR_CONFLICT_HOLD")
    t.stop()
    t.endif()
    roles = ",".join(ROLE_CONFIG)
    t.for_("%fxc_role", roles)
    t.perform("AIW Validation Fixture Resolve Config", "%fxc_role")
    t.if_([("%AIWFixtureResolveResult", 3, "FIXTURE_BINDING_READY")])
    t.set("%AIWFixtureContractResult", "%AIWFixtureResolveResult")
    t.stop()
    t.endif()
    t.perform("AIW Validation Fixture Inspect Bound", "CONTRACT")
    t.if_([("%AIWFXAuthState", 2, "ARMED"), ("%AIWFixtureInspectResult", 3, "FIXTURE_ROW_BLANK")], ["And"])
    t.set("%AIWFixtureContractResult", "%AIWFixtureInspectResult")
    t.stop()
    t.endif()
    t.if_([("%AIWFXAuthState", 2, "ACTIVE"), ("%AIWFixtureInspectResult", 5, r"^(FIXTURE_ROW_BLANK|FIXTURE_ROW_OWNED)$")], ["And"])
    t.set("%AIWFixtureContractResult", "%AIWFixtureInspectResult")
    t.stop()
    t.endif()
    t.endfor()
    t.if_([("%AIWFXAuthState", 2, "ARMED")])
    t.set("%AIWFXAuthConsumedRun", "%AIWValidationRunID")
    t.set("%AIWFXAuthState", "ACTIVE")
    t.endif()
    t.set("%AIWFixtureContractReady", "1")
    t.set("%AIWFixtureContractResult", "FIXTURE_CONTRACT_READY")
    return t


def emit_checked_write(t: TaskBuilder, action: ET.Element, ok_var: str, error_result: str) -> None:
    t.clear("%err")
    t.clear("%errmsg")
    t.plugin(action)
    t.set(ok_var, "1")
    t.if_([("%err", 4, r"^[1-9][0-9]*$")])
    t.set(ok_var, "0")
    t.endif()
    t.if_([("%err", 4, r"(?s)^%.*$|(?is).*#ERROR.*")])
    t.set(ok_var, "0")
    t.endif()
    t.if_([(ok_var, 3, "1")])
    t.set("%AIWFixtureWriteAdvisory", error_result)
    t.endif()


def build_setup(root: ET.Element) -> TaskBuilder:
    _, update_template = plugin_templates(root)
    writes = {
        "Sheet1": make_update(update_template, "Sheet1", "A%AIWFixtureBoundRow", ["%AIWFixtureBoundID", "%AIWFixtureBoundSender", "%AIWFixtureBoundMessage", "%AIWFixtureBoundStatus", "", "", "", "", ""]),
        "Archive": make_update(update_template, "Archive", "A%AIWFixtureBoundRow", ["%AIWFixtureBoundID", "%AIWFixtureBoundSender", "%AIWFixtureBoundMessage"]),
        "DeadArchive": make_update(update_template, "DeadArchive", "A%AIWFixtureBoundRow", ["%AIWFixtureBoundID"]),
    }
    t = TaskBuilder()
    t.set("%AIWFixtureSetupResult", "FIXTURE_SETUP_START")
    t.set("%AIWFixtureSetupVerified", "0")
    t.set("%AIWFixtureWriteAdvisory", "NONE")
    t.perform("AIW Validation Fixture Resolve Config", "%par1")
    t.if_([("%AIWFixtureResolveResult", 3, "FIXTURE_BINDING_READY")])
    t.set("%AIWFixtureSetupResult", "%AIWFixtureResolveResult")
    t.stop()
    t.endif()
    require_active_contract(t, "%AIWFixtureSetupResult")
    t.perform("AIW Validation Fixture Inspect Bound", "SETUP_PREWRITE")
    t.if_([("%AIWFixtureInspectResult", 2, "FIXTURE_ROW_OWNED")])
    t.set("%AIWFixtureSetupVerified", "1")
    t.set("%AIWFixtureSetupResult", "FIXTURE_SETUP_ALREADY_READY")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureInspectResult", 3, "FIXTURE_ROW_BLANK")])
    t.set("%AIWFixtureSetupResult", "%AIWFixtureInspectResult")
    t.stop()
    t.endif()
    for layer, action in writes.items():
        t.if_([("%AIWFixtureBoundLayer", 2, layer)])
        emit_checked_write(t, action, "%fxs_write_ok", "FIXTURE_SETUP_WRITE_PLUGIN_AMBIGUOUS")
        t.endif()
    t.perform("AIW Validation Fixture Inspect Bound", "SETUP_READBACK")
    t.if_([("%AIWFixtureInspectResult", 2, "FIXTURE_ROW_OWNED")])
    t.set("%AIWFixtureSetupVerified", "1")
    t.if_([("%fxs_write_ok", 2, "1")])
    t.set("%AIWFixtureSetupResult", "FIXTURE_SETUP_READY")
    t.else_()
    t.set("%AIWFixtureSetupResult", "FIXTURE_SETUP_READY_AFTER_AMBIGUOUS_WRITE")
    t.endif()
    t.else_()
    t.set("%AIWFixtureSetupResult", "FIXTURE_SETUP_READBACK_HOLD")
    t.endif()
    return t


def require_active_contract(t: TaskBuilder, result_var: str) -> None:
    t.if_([("%AIWFixtureContractReady", 3, "1"), ("%AIWFixtureContractResult", 3, "FIXTURE_CONTRACT_READY"), ("%AIWFXAuthState", 3, "ACTIVE"), ("%AIWFXAuthConsumedRun", 3, "%AIWValidationRunID")], ["Or", "Or", "Or"])
    t.set(result_var, "FIXTURE_CONTRACT_NOT_ACTIVE_HOLD")
    t.stop()
    t.endif()


def build_cleanup_bound(root: ET.Element) -> TaskBuilder:
    _, update_template = plugin_templates(root)
    clears = {
        "Sheet1": make_update(update_template, "Sheet1", "A%AIWFixtureBoundRow", [""] * 9),
        "Archive": make_update(update_template, "Archive", "A%AIWFixtureBoundRow", [""] * 3),
        "DeadArchive": make_update(update_template, "DeadArchive", "A%AIWFixtureBoundRow", [""]),
        "OverflowInbox": make_update(update_template, "OverflowInbox", "A%AIWFixtureBoundRow", [""] * 14),
        "IngressJournal": make_update(update_template, "IngressJournal", "A%AIWFixtureBoundRow", [""] * 14),
    }
    t = TaskBuilder()
    t.set("%AIWFixtureCleanupCoreResult", "FIXTURE_CLEANUP_START")
    t.set("%AIWFixtureCleanupCoreVerified", "0")
    t.set("%AIWFixtureWriteAdvisory", "NONE")
    require_active_contract(t, "%AIWFixtureCleanupCoreResult")
    t.perform("AIW Validation Fixture Inspect Bound", "CLEANUP_PREWRITE")
    t.if_([("%AIWFixtureInspectResult", 2, "FIXTURE_ROW_BLANK")])
    t.set("%AIWFixtureCleanupCoreVerified", "1")
    t.set("%AIWFixtureCleanupCoreResult", "FIXTURE_ALREADY_CLEAN")
    t.stop()
    t.endif()
    t.if_([("%AIWFixtureInspectResult", 3, "FIXTURE_ROW_OWNED")])
    t.set("%AIWFixtureCleanupCoreResult", "%AIWFixtureInspectResult")
    t.stop()
    t.endif()
    for layer, action in clears.items():
        t.if_([("%AIWFixtureBoundLayer", 2, layer)])
        emit_checked_write(t, action, "%fxc_write_ok", "FIXTURE_CLEANUP_WRITE_PLUGIN_AMBIGUOUS")
        t.endif()
    t.perform("AIW Validation Fixture Inspect Bound", "CLEANUP_READBACK")
    t.if_([("%AIWFixtureInspectResult", 2, "FIXTURE_ROW_BLANK")])
    t.set("%AIWFixtureCleanupCoreVerified", "1")
    t.if_([("%fxc_write_ok", 2, "1")])
    t.set("%AIWFixtureCleanupCoreResult", "FIXTURE_CLEANUP_VERIFIED")
    t.else_()
    t.set("%AIWFixtureCleanupCoreResult", "FIXTURE_CLEANUP_VERIFIED_AFTER_AMBIGUOUS_WRITE")
    t.endif()
    t.else_()
    t.set("%AIWFixtureCleanupCoreResult", "FIXTURE_CLEANUP_READBACK_HOLD")
    t.endif()
    return t


def build_auth_close() -> TaskBuilder:
    t = TaskBuilder()
    t.set("%AIWFixtureAuthCloseResult", "FIXTURE_AUTH_CLOSE_START")
    require_active_contract(t, "%AIWFixtureAuthCloseResult")
    t.for_("%fxz_role", ",".join(ROLE_CONFIG))
    t.perform("AIW Validation Fixture Resolve Config", "%fxz_role")
    t.if_([("%AIWFixtureResolveResult", 3, "FIXTURE_BINDING_READY")])
    t.set("%AIWFixtureAuthCloseResult", "%AIWFixtureResolveResult")
    t.stop()
    t.endif()
    t.perform("AIW Validation Fixture Inspect Bound", "AUTH_CLOSE")
    t.if_([("%AIWFixtureInspectResult", 3, "FIXTURE_ROW_BLANK")])
    t.set("%AIWFixtureAuthCloseResult", "FIXTURE_AUTH_DIRTY_HOLD")
    t.stop()
    t.endif()
    t.endfor()
    t.set("%AIWFXAuthState", "USED")
    t.clear("%AIWFXAuthToken")
    t.set("%AIWFixtureContractReady", "0")
    t.set("%AIWFixtureContractResult", "FIXTURE_CONTRACT_CLOSED")
    t.set("%AIWFixtureAuthCloseResult", "FIXTURE_AUTHORIZATION_CLOSED")
    return t


def build_cleanup_router() -> TaskBuilder:
    t = TaskBuilder()
    t.set("%AIWValidationCleanupVerified", "0")
    t.set("%AIWValidationCleanupResult", "VALIDATION_CLEANUP_START")
    require_active_contract(t, "%AIWValidationCleanupResult")
    t.set("%fxroute", "0")
    t.if_([("%par1", 4, r"^(HIST_ARCHIVE|HIST_DEAD|G14C_REAL|G14C_RATE|G14C_TIMEOUT|G14C_QUOTA|G14C_LEGACY|REAL_SUCCESS|RATE_LIMIT_THEN_SUCCESS|TIMEOUT_EXHAUSTED|QUOTA_429_NO_RETRY|LEGACY_RETRY_MIGRATION)$")])
    t.perform("AIW Validation Fixture Resolve Config", "%par1")
    t.set("%fxroute", "1")
    t.endif()
    t.if_([("%par1", 4, r"^(MAIN|OVERFLOW|JOURNAL)$")])
    t.perform("AIW Validation Fixture Resolve Runtime", "%par1", "%par2")
    t.set("%fxroute", "1")
    t.endif()
    t.if_([("%fxroute", 3, "1"), ("%AIWFixtureBoundResolved", 3, "1")], ["Or"])
    t.set("%AIWValidationCleanupResult", "VALIDATION_CLEANUP_AUTHORIZATION_HOLD")
    t.stop()
    t.endif()
    t.perform("AIW Validation Fixture Cleanup Bound")
    t.set("%AIWValidationCleanupResult", "%AIWFixtureCleanupCoreResult")
    t.if_([("%AIWFixtureCleanupCoreVerified", 2, "1")])
    t.set("%AIWValidationCleanupVerified", "1")
    t.endif()
    return t


def build_phase7() -> TaskBuilder:
    t = TaskBuilder()
    t.set("%AIWValidationPhaseResult", "PHASE7_START")
    t.perform("APP Stop AI Worker")
    t.set("%AIWValidationRealSendAuthorized", "0")
    tracked = [
        ("MAIN", "%AIWPhase1MainRow"), ("MAIN", "%AIWPhase2MainRow1"),
        ("MAIN", "%AIWPhase2MainRow2"), ("MAIN", "%AIWPhase2MainRow3"),
        ("OVERFLOW", "%AIWPhase1OverflowRow"), ("OVERFLOW", "%AIWPhase2OverflowRow1"),
        ("OVERFLOW", "%AIWPhase2OverflowRow2"), ("JOURNAL", "%AIWPhase1JournalRow1"),
        ("JOURNAL", "%AIWPhase1JournalRow2"), ("JOURNAL", "%AIWPhase2JournalRow1"),
        ("JOURNAL", "%AIWPhase2JournalRow2"), ("JOURNAL", "%AIWPhase4JournalRow"),
    ]
    for layer, row in tracked:
        t.if_([(row, 4, r"^[0-9]+$")])
        t.perform("AIW Validation Cleanup Exact Row", layer, row)
        t.if_([("%AIWValidationCleanupVerified", 3, "1")])
        t.set("%AIWValidationPhaseResult", f"PHASE7_{layer}_CLEANUP_HOLD")
        t.stop()
        t.endif()
        t.endif()
    for role in ROLE_CONFIG:
        t.perform("AIW Validation Cleanup Exact Row", role)
        t.if_([("%AIWValidationCleanupVerified", 3, "1")])
        t.set("%AIWValidationPhaseResult", f"PHASE7_{role}_CLEANUP_HOLD")
        t.stop()
        t.endif()
    t.perform("AIW Validation Control Write", "NORMAL")
    t.if_([("%AIWValidationControlVerified", 3, "1")])
    t.set("%AIWValidationPhaseResult", "PHASE7_CONTROL_CLEANUP_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWReleaseValidationComplete", "1")
    t.set("%AIWValidationPhaseResult", "PHASE7_PASS")
    t.perform("AIW Proof Ledger Append", "PHASE7", "PHASE7_PASS")
    t.if_([("%AIWProofWriteVerified", 3, "1")])
    t.set("%AIWValidationPhaseResult", "PHASE7_PROOF_HOLD")
    t.stop()
    t.endif()
    t.perform("AIW Validation Fixture Authorization Close")
    t.if_([("%AIWFixtureAuthCloseResult", 3, "FIXTURE_AUTHORIZATION_CLOSED")])
    t.set("%AIWValidationPhaseResult", "PHASE7_FIXTURE_AUTH_CLOSE_HOLD")
    t.endif()
    return t


def patch_task237(raw: str) -> str:
    actions = action_list(raw)
    if len(actions) != 308:
        raise RuntimeError(f"Task 237 action count changed: {len(actions)}")
    for index in (67, 76, 85, 94, 103):
        actions[index] = replace_string_arg(actions[index], "arg1", "%AIWFixtureBoundRow")
    for index in (68, 77, 86, 95, 104):
        actions[index] = replace_string_arg(actions[index], "arg1", "%AIWFixtureBoundID")
    for index in (69, 70, 78, 79, 87, 88, 96, 97, 105, 106):
        actions[index] = replace_string_arg(actions[index], "arg1", "%AIWFixtureBoundSender")
    for index in (71, 72, 80, 81, 89, 90, 98, 99, 107, 108):
        actions[index] = replace_string_arg(actions[index], "arg1", "%AIWFixtureBoundMessage")
    for index in (73, 82, 91, 100, 109):
        actions[index] = replace_string_arg(actions[index], "arg1", "%AIWFixtureBoundStatus")
    gate = TaskBuilder()
    gate.perform("AIW Validation Fixture Setup Exact", "%AIWG14CMode")
    gate.if_([("%AIWFixtureSetupVerified", 3, "1")])
    gate.set("%AIWG14CResult", "GATE14C_FIXTURE_SETUP_HOLD")
    gate.set("%AIWG14CError", "%AIWFixtureSetupResult")
    gate.stop()
    gate.endif()
    actions[66:66] = gate.actions
    return replace_actions(raw, actions)


def patch_task268(raw: str) -> str:
    actions = action_list(raw)
    if len(actions) != 80:
        raise RuntimeError(f"Task 268 action count changed: {len(actions)}")
    gate = TaskBuilder()
    gate.perform("AIW Validation Fixture Contract")
    gate.if_([("%AIWFixtureContractResult", 3, "FIXTURE_CONTRACT_READY")])
    gate.set("%AIWValidationResult", "%AIWFixtureContractResult")
    gate.stop()
    gate.endif()
    actions[13:13] = gate.actions
    return replace_actions(raw, actions)


def patch_task270(raw: str) -> str:
    actions = action_list(raw)
    if len(actions) != 85:
        raise RuntimeError(f"Task 270 action count changed: {len(actions)}")
    setup = TaskBuilder()
    for role in ("HIST_ARCHIVE", "HIST_DEAD"):
        setup.perform("AIW Validation Fixture Setup Exact", role)
        setup.if_([("%AIWFixtureSetupVerified", 3, "1")])
        setup.set("%AIWValidationPhaseResult", f"PHASE1_{role}_SETUP_HOLD")
        setup.stop()
        setup.endif()
    actions[14:14] = setup.actions
    offset = len(setup.actions)
    replacements = {
        45: "%AIWFXHistArchiveID", 46: "%AIWFXHistArchiveSender", 47: "%AIWFXHistArchiveMessage",
        54: "%AIWFXHistDeadID", 55: "%AIWFXHistDeadSender", 56: "%AIWFXHistDeadMessage",
    }
    for old_index, value in replacements.items():
        actions[old_index + offset] = replace_string_arg(actions[old_index + offset], "arg1", value)
    return replace_actions(raw, actions)


def patch_task272(raw: str) -> str:
    actions = action_list(raw)
    if len(actions) != 69:
        raise RuntimeError(f"Task 272 action count changed: {len(actions)}")
    mappings = [(38, 40, "G14C_REAL"), (44, 46, "G14C_RATE"), (50, 52, "G14C_TIMEOUT"), (56, 58, "G14C_QUOTA")]
    for call_index, result_index, role in mappings:
        actions[call_index] = replace_string_arg(actions[call_index], "arg2", role)
        actions[call_index] = replace_string_arg(actions[call_index], "arg3", "")
        actions[result_index] = replace_string_arg(actions[result_index], "arg1", f"PHASE3_{role}_CLEANUP_HOLD")
    return replace_actions(raw, actions)


def insert_helpers_and_registry(text: str, nodes: dict[int, str]) -> str:
    project_match = re.search(r"<Project\b.*?</Project>", text, flags=re.DOTALL)
    if not project_match:
        raise RuntimeError("Project registry not found")
    project = project_match.group(0)
    tids_match = re.search(r"<tids>([^<]+)</tids>", project)
    if not tids_match:
        raise RuntimeError("Project task registry missing")
    existing = [int(value) for value in tids_match.group(1).split(",") if value]
    if set(nodes) & set(existing):
        raise RuntimeError(f"Helper ID collision: {sorted(set(nodes) & set(existing))}")
    tids = ",".join(str(value) for value in existing + sorted(nodes))
    project = project[:tids_match.start(1)] + tids + project[tids_match.end(1):]
    return text[:project_match.start()] + "".join(nodes[i] for i in sorted(nodes)) + project + text[project_match.end():]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    base = args.base.read_bytes()
    if sha256(base) != EXPECTED_BASE_SHA:
        raise RuntimeError(f"Authorized repair-base SHA mismatch: {sha256(base)}")
    if base.startswith(b"\xef\xbb\xbf"):
        raise RuntimeError("Repair base unexpectedly has UTF-8 BOM")
    text = base.decode("utf-8")
    root = ET.fromstring(base)
    source = raw_tasks(text)
    if not AUTHORIZED_EXISTING <= set(source):
        raise RuntimeError("Authorized task missing from base")
    builders = {
        295: build_resolve_config(),
        296: build_resolve_runtime(),
        297: build_inspect_bound(),
        298: build_contract(),
        299: build_setup(root),
        300: build_cleanup_bound(root),
        301: build_auth_close(),
        302: build_sheet1_inspect_router(),
        303: build_inspect_layers(root, {"Archive", "DeadArchive"}),
        304: build_queue_inspect_router(),
        305: build_inspect_layers(root, {"OverflowInbox"}),
        306: build_inspect_layers(root, {"IngressJournal"}),
        307: build_sheet1_read(root),
        308: build_sheet1_classify(),
    }
    for task_id, builder in builders.items():
        if len(builder.actions) >= 500:
            raise RuntimeError(f"New helper {task_id} has {len(builder.actions)} actions")
    replacements = {
        237: patch_task237(source[237]),
        268: patch_task268(source[268]),
        270: patch_task270(source[270]),
        272: patch_task272(source[272]),
        276: replace_actions(source[276], build_phase7().actions),
        293: replace_actions(source[293], build_cleanup_router().actions),
    }
    for task_id, node in replacements.items():
        text, count = re.subn(rf'<Task sr="task{task_id}".*?</Task>', lambda _: node, text, count=1, flags=re.DOTALL)
        if count != 1:
            raise RuntimeError(f"Task {task_id} replacement count {count}")
    helper_nodes = {task_id: task_xml(task_id, HELPERS[task_id], builders[task_id]) for task_id in sorted(HELPERS)}
    text = insert_helpers_and_registry(text, helper_nodes)
    output = text.encode("utf-8")
    ET.fromstring(output)
    final = raw_tasks(text)
    changed = sorted(task_id for task_id in source if source[task_id] != final.get(task_id))
    added = sorted(set(final) - set(source))
    if changed != sorted(AUTHORIZED_EXISTING):
        raise RuntimeError(f"Unexpected existing-task scope: {changed}")
    if added != sorted(HELPERS):
        raise RuntimeError(f"Unexpected helper set: {added}")
    for task_id in set(source) - AUTHORIZED_EXISTING:
        if source[task_id] != final[task_id]:
            raise RuntimeError(f"Unauthorized Task {task_id} changed")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(output)
    print(f"BASE_SHA256={sha256(base)}")
    print(f"OUTPUT_SHA256={sha256(output)}")
    print(f"OUTPUT_BYTES={len(output)}")
    print(f"CHANGED_EXISTING={changed}")
    print(f"ADDED_HELPERS={added}")
    for task_id in sorted(HELPERS):
        print(f"HELPER={task_id}|{HELPERS[task_id]}|ACTIONS={len(builders[task_id].actions)}")


if __name__ == "__main__":
    main()
