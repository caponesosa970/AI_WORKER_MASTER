from __future__ import annotations

import argparse
import copy
import hashlib
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import aiw_final_fixture_safety_repair as fixture


EXPECTED_BASE_SHA = "58A5229EB7F6892C03AD799BB7A4C3144C59ACD4DEC0E5B2235F0AAF68EEF76B"
AUTHORIZED_EXISTING = {262, 273, 276, 278, 282, 284}
PROTECTED_PHONE_TASKS = {71, 199, 223, 225, 226, 227, 230, 231}
LEGACY_UNREACHABLE = {27, 28, 69, 222}

HELPERS = {
    309: "AIW Conversation Quiet Select",
    310: "AIW Conversation Owner",
    311: "AIW Conversation Ledger Read Exact",
    312: "AIW Conversation Ledger Locate",
    313: "AIW Conversation Ledger Create",
    314: "AIW Conversation Member Verify",
    315: "AIW Conversation Member Bind",
    316: "AIW Conversation Ledger Transition",
    317: "AIW Conversation Prepare Group",
    318: "AIW Conversation Archive History",
    319: "AIW Conversation Prompt Build",
    320: "AIW Conversation Pre Send Guard",
    321: "AIW Conversation Send State",
    322: "AIW Conversation Finalize Companions",
    323: "AIW Conversation Recovery",
    324: "AIW Conversation Schema Check",
    325: "AIW Conversation Validation Audit",
    326: "AIW Conversation Validation Cleanup",
}

SCHEMA_VERSION = "AIW_CONVERSATION_V1"
GROUP_STATES = (
    "GROUP_BINDING",
    "GROUP_BOUND",
    "GROUP_PROCESSING",
    "GROUP_REPLY_READY",
    "GROUP_SEND_AWAITING_CONFIRM",
    "GROUP_SEND_OUTCOME_REVIEW",
    "GROUP_ANCHOR_ARCHIVED",
    "GROUP_FINALIZING",
    "GROUP_COMPLETE",
    "GROUP_REVIEW",
)

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

T = fixture.TaskBuilder


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def excel_column(index: int) -> str:
    value = ""
    while index:
        index, rem = divmod(index - 1, 26)
        value = chr(65 + rem) + value
    return value


COLS = [excel_column(i) for i in range(1, len(HEADERS) + 1)]
LAST_COL = COLS[-1]
LEDGER_GLOBALS = [f"%AICGL_{col}" for col in COLS]


def add_random(t: T, name: str, low: int = 100000, high: int = 999999) -> None:
    t.add(
        "<code>545</code>"
        f'<Str sr="arg0" ve="3">{fixture.esc(name)}</Str>'
        f'<Int sr="arg1" val="{low}" /><Int sr="arg2" val="{high}" />'
    )


def regex_replace(t: T, name: str, pattern: str, replacement: str = "") -> None:
    t.add(
        "<code>598</code>"
        f'<Str sr="arg0" ve="3">{fixture.esc(name)}</Str>'
        f'<Str sr="arg1" ve="3">{fixture.esc(pattern)}</Str>'
        '<Int sr="arg2" val="0" /><Int sr="arg3" val="1" /><Int sr="arg4" val="0" />'
        f'<Str sr="arg5" ve="3">{fixture.esc(replacement)}</Str>'
        '<Int sr="arg6" val="1" /><Str sr="arg7" ve="3" />'
    )


def read_twice(t: T, action: ET.Element, arrays: list[str], ok: str) -> None:
    t.set(ok, "0")
    t.for_("%cg_try", "1,2")
    t.if_([(ok, 3, "1")])
    for name in arrays:
        t.array_clear(f"%{name}")
    t.clear("%err")
    t.clear("%errmsg")
    t.plugin(action)
    t.set(ok, "1")
    t.if_([("%err", 4, r"^[1-9][0-9]*$|(?s)^%.*$|(?is).*#ERROR.*")])
    t.set(ok, "0")
    t.endif()
    t.endif()
    t.endfor()


def checked_write(t: T, action: ET.Element, ok: str) -> None:
    t.clear("%err")
    t.clear("%errmsg")
    t.plugin(action)
    t.set(ok, "1")
    t.if_([("%err", 4, r"^[1-9][0-9]*$|(?s)^%.*$|(?is).*#ERROR.*")])
    t.set(ok, "0")
    t.endif()


def require_schema(t: T, result: str) -> None:
    t.if_([
        ("%AIWConversationSchemaReady", 3, "1"),
        ("%AIWConversationSchemaResult", 3, "CONVERSATION_SCHEMA_READY"),
        ("%AIWConversationGroupMax", 5, r"^[0-9]+$"),
        ("%AIWConversationMainMax", 5, r"^[0-9]+$"),
        ("%AIWConversationArchiveMax", 5, r"^[0-9]+$"),
    ], ["Or", "Or", "Or", "Or"])
    t.set(result, "CONVERSATION_SCHEMA_HOLD")
    t.stop()
    t.endif()


def invalid(t: T, value: str, result: str, hold: str) -> None:
    t.if_([(value, 4, r"(?s)^\s*$|^%.*$|(?is).*#ERROR.*")])
    t.set(result, hold)
    t.stop()
    t.endif()


def load_group_globals(t: T) -> None:
    mappings = {
        "%AIWConversationGroupID": "B",
        "%AIWConversationSenderKey": "C",
        "%AIWConversationAnchorRow": "D",
        "%AIWConversationAnchorID": "E",
        "%AIWConversationMemberCount": "F",
        "%AIWConversationState": "O",
        "%AIWConversationQuietCutoff": "P",
        "%AIWConversationBoundAt": "Q",
        "%AIWConversationReply": "R",
        "%AIWConversationOwnerToken": "Y",
        "%AIWConversationOwnerStarted": "Z",
        "%AIWConversationLedgerRow": "AA",
        "%AIWConversationFreezeLoggedAt": "AB",
        "%AIWConversationBoundMask": "AG",
        "%AIWConversationArchivedMask": "AH",
        "%AIWConversationRunContext": "AJ",
        "%AIWConversationRole": "AP",
    }
    for target, col in mappings.items():
        t.set(target, f"%AICGL_{col}")
    for index, (rcol, icol, mcol) in enumerate(
        [("G", "H", "AK"), ("I", "J", "AL"), ("K", "L", "AM"), ("M", "N", "AN")], 1
    ):
        t.set(f"%AIWConversationMemberRow{index}", f"%AICGL_{rcol}")
        t.set(f"%AIWConversationMemberID{index}", f"%AICGL_{icol}")
        t.set(f"%AIWConversationMemberMessage{index}", f"%AICGL_{mcol}")


def build_owner() -> T:
    t = T()
    t.set("%AIWConversationOwnerResult", "CONVERSATION_OWNER_START")
    t.set("%cgo_command", "%par1")
    t.set("%cgo_token", "%par2")
    invalid(t, "%cgo_token", "%AIWConversationOwnerResult", "CONVERSATION_OWNER_TOKEN_HOLD")
    t.if_([("%cgo_token", 5, r"^AIWCG[0-9]{20,40}$")])
    t.set("%AIWConversationOwnerResult", "CONVERSATION_OWNER_TOKEN_HOLD")
    t.stop()
    t.endif()
    t.if_([("%cgo_command", 5, r"^(ACQUIRE|RELEASE)$")])
    t.set("%AIWConversationOwnerResult", "CONVERSATION_OWNER_COMMAND_HOLD")
    t.stop()
    t.endif()
    t.set("%cgo_owner_blank", "0")
    t.set("%cgo_started_blank", "0")
    t.if_([("%AIWConversationOwner", 4, r"(?s)^\s*$|^%.*$")])
    t.set("%cgo_owner_blank", "1")
    t.endif()
    t.if_([("%AIWConversationOwnerStartedAt", 4, r"(?s)^\s*$|^%.*$")])
    t.set("%cgo_started_blank", "1")
    t.endif()
    t.if_([("%cgo_owner_blank", 3, "%cgo_started_blank")])
    t.set("%AIWConversationOwnerResult", "CONVERSATION_OWNER_PARTIAL_PAIR_HOLD")
    t.stop()
    t.endif()
    t.if_([("%cgo_command", 2, "ACQUIRE")])
    t.if_([("%cgo_owner_blank", 2, "1")])
    t.set("%AIWConversationOwner", "%cgo_token")
    t.set("%AIWConversationOwnerStartedAt", "%TIMES")
    t.endif()
    t.if_([("%AIWConversationOwner", 3, "%cgo_token")])
    t.set("%AIWConversationOwnerResult", "CONVERSATION_OWNER_BUSY_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationOwnerResult", "CONVERSATION_OWNER_ACQUIRED")
    t.else_()
    t.if_([("%AIWConversationOwner", 3, "%cgo_token")])
    t.set("%AIWConversationOwnerResult", "CONVERSATION_OWNER_NOT_OWNED_HOLD")
    t.stop()
    t.endif()
    t.clear("%AIWConversationOwnerStartedAt")
    t.clear("%AIWConversationOwner")
    t.set("%AIWConversationOwnerResult", "CONVERSATION_OWNER_RELEASED_EXACT")
    t.endif()
    return t


def build_ledger_read(root: ET.Element) -> T:
    get_template, _ = fixture.plugin_templates(root)
    arrays = [f"cgl_{col.lower()}" for col in COLS]
    action = fixture.make_get(
        get_template, "ConversationGroups",
        f"A%AIWConversationLedgerRow:{LAST_COL}%AIWConversationLedgerRow", arrays,
    )
    t = T()
    t.set("%AIWConversationLedgerReadResult", "CONVERSATION_LEDGER_READ_START")
    t.set("%AIWConversationLedgerReadReady", "0")
    t.set("%AIWConversationLedgerBlank", "0")
    require_schema(t, "%AIWConversationLedgerReadResult")
    t.if_([("%AIWConversationLedgerRow", 5, r"^[0-9]+$")])
    t.set("%AIWConversationLedgerReadResult", "CONVERSATION_LEDGER_ROW_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationLedgerRow", 7, "%AIWConversationGroupMax")])
    t.set("%AIWConversationLedgerReadResult", "CONVERSATION_LEDGER_OUT_OF_BOUNDS_HOLD")
    t.stop()
    t.endif()
    read_twice(t, action, arrays, "%cgl_ok")
    t.if_([("%cgl_ok", 3, "1")])
    t.set("%AIWConversationLedgerReadResult", "CONVERSATION_LEDGER_PLUGIN_HOLD")
    t.stop()
    t.endif()
    t.set("%cgl_nonblank", "0")
    for col, array, target in zip(COLS, arrays, LEDGER_GLOBALS):
        t.set(target, f"%{array}(1)")
        t.if_([(target, 4, rf"(?s)^%{array}(?:\(1\)|[0-9]*)$|^%.*\(#\)$")])
        t.set(target, "")
        t.else_()
        t.set("%cgl_nonblank", "1")
        t.endif()
    t.if_([("%cgl_nonblank", 2, "0")])
    t.set("%AIWConversationLedgerBlank", "1")
    t.endif()
    t.set("%AIWConversationLedgerReadReady", "1")
    t.set("%AIWConversationLedgerReadResult", "CONVERSATION_LEDGER_READ_READY")
    return t


def build_ledger_locate(root: ET.Element) -> T:
    get_template, _ = fixture.plugin_templates(root)
    arrays = [f"cgs_{col.lower()}" for col in COLS]
    action = fixture.make_get(
        get_template, "ConversationGroups", f"A2:{LAST_COL}%AIWConversationGroupMax", arrays,
    )
    t = T()
    t.set("%AIWConversationLocateResult", "CONVERSATION_LOCATE_START")
    t.set("%AIWConversationLedgerFound", "0")
    t.set("%cgs_matches", "0")
    require_schema(t, "%AIWConversationLocateResult")
    read_twice(t, action, arrays, "%cgs_ok")
    t.if_([("%cgs_ok", 3, "1")])
    t.set("%AIWConversationLocateResult", "CONVERSATION_LOCATE_PLUGIN_HOLD")
    t.stop()
    t.endif()
    t.set("%cgs_index", "0")
    t.for_("%cgs_dummy", "%cgs_b()")
    t.add_value("%cgs_index")
    t.set("%cgs_match", "0")
    t.if_([("%par1", 2, "ANCHOR"), ("%cgs_d(%cgs_index)", 2, "%PSMainRow"), ("%cgs_e(%cgs_index)", 2, "%PSSelectedId")], ["And", "And"])
    t.set("%cgs_match", "1")
    t.endif()
    t.if_([("%par1", 2, "GROUP"), ("%cgs_b(%cgs_index)", 2, "%AIWConversationGroupID")], ["And"])
    t.set("%cgs_match", "1")
    t.endif()
    t.if_([("%par1", 2, "ACTIVE"), ("%cgs_b(%cgs_index)", 4, r"^AIWCG[0-9]{20,40}$"), ("%cgs_o(%cgs_index)", 5, r"^GROUP_COMPLETE$")], ["And", "And"])
    t.set("%cgs_match", "1")
    t.endif()
    t.if_([("%cgs_match", 2, "1")])
    t.add_value("%cgs_matches")
    t.set("%AIWConversationLedgerRow", "%cgs_index+1", maths=True)
    t.endif()
    t.endfor()
    t.if_([("%cgs_matches", 7, "1")])
    t.set("%AIWConversationLocateResult", "CONVERSATION_LOCATE_CONFLICT_HOLD")
    t.stop()
    t.endif()
    t.if_([("%cgs_matches", 2, "0")])
    t.set("%AIWConversationLocateResult", "CONVERSATION_LEDGER_NOT_FOUND")
    t.stop()
    t.endif()
    t.perform("AIW Conversation Ledger Read Exact")
    t.if_([("%AIWConversationLedgerReadReady", 3, "1"), ("%AIWConversationLedgerBlank", 3, "0")], ["Or"])
    t.set("%AIWConversationLocateResult", "CONVERSATION_LOCATE_READBACK_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationLedgerFound", "1")
    t.set("%AIWConversationLocateResult", "CONVERSATION_LEDGER_FOUND")
    return t


def build_ledger_create(root: ET.Element) -> T:
    get_template, update_template = fixture.plugin_templates(root)
    slot = fixture.make_get(get_template, "ConversationGroupSlotView", "A2:A2", ["cgslot"])
    write = fixture.make_update(
        update_template, "ConversationGroups", "A%AIWConversationLedgerRow", LEDGER_GLOBALS,
    )
    t = T()
    t.set("%AIWConversationLedgerCreateResult", "CONVERSATION_LEDGER_CREATE_START")
    require_schema(t, "%AIWConversationLedgerCreateResult")
    t.if_([("%AIWConversationOwnerResult", 3, "CONVERSATION_OWNER_ACQUIRED"), ("%AIWConversationOwner", 3, "%AIWConversationOwnerToken")], ["Or"])
    t.set("%AIWConversationLedgerCreateResult", "CONVERSATION_LEDGER_OWNER_HOLD")
    t.stop()
    t.endif()
    read_twice(t, slot, ["cgslot"], "%cgslot_ok")
    t.if_([("%cgslot_ok", 3, "1"), ("%cgslot(#)", 3, "1")], ["Or"])
    t.set("%AIWConversationLedgerCreateResult", "CONVERSATION_LEDGER_SLOT_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationLedgerRow", "%cgslot(1)")
    t.if_([("%AIWConversationLedgerRow", 5, r"^[2-9][0-9]*$")])
    t.set("%AIWConversationLedgerCreateResult", "CONVERSATION_LEDGER_SLOT_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationLedgerRow", 7, "%AIWConversationGroupMax")])
    t.set("%AIWConversationLedgerCreateResult", "CONVERSATION_LEDGER_CAPACITY_FULL_HOLD")
    t.stop()
    t.endif()
    t.perform("AIW Conversation Ledger Read Exact")
    t.if_([("%AIWConversationLedgerReadReady", 3, "1"), ("%AIWConversationLedgerBlank", 3, "1")], ["Or"])
    t.set("%AIWConversationLedgerCreateResult", "CONVERSATION_LEDGER_SLOT_NOT_BLANK_HOLD")
    t.stop()
    t.endif()
    add_random(t, "%cgc_r1")
    add_random(t, "%cgc_r2")
    t.set("%AIWConversationGroupID", "AIWCG%TIMEMS%cgc_r1%cgc_r2")
    t.perform("AIW Conversation Ledger Locate", "GROUP")
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_NOT_FOUND")])
    t.set("%AIWConversationLedgerCreateResult", "CONVERSATION_GROUP_ID_COLLISION_HOLD")
    t.stop()
    t.endif()
    values = {col: "" for col in COLS}
    values.update({
        "A": SCHEMA_VERSION,
        "B": "%AIWConversationGroupID",
        "C": "%AIWConversationSenderKey",
        "D": "%PSMainRow",
        "E": "%PSSelectedId",
        "F": "%AIWConversationMemberCount",
        "G": "%AIWConversationMemberRow1", "H": "%AIWConversationMemberID1",
        "I": "%AIWConversationMemberRow2", "J": "%AIWConversationMemberID2",
        "K": "%AIWConversationMemberRow3", "L": "%AIWConversationMemberID3",
        "M": "%AIWConversationMemberRow4", "N": "%AIWConversationMemberID4",
        "O": "GROUP_BINDING", "P": "%AIWConversationQuietCutoff", "Q": "%TIMEMS",
        "S": "0", "T": "NONE", "U": "%TIMEMS", "V": "UNCONFIRMED",
        "W": "ANCHOR_NOT_ARCHIVED", "X": "0", "Y": "%AIWConversationOwnerToken",
        "Z": "%AIWConversationOwnerStarted", "AA": "%AIWConversationLedgerRow",
        "AB": "%AIWConversationNewestLoggedAt", "AC": "HISTORY_NOT_BUILT", "AD": "0",
        "AE": "PROMPT_NOT_BUILT", "AF": "1", "AG": "1", "AH": "",
        "AI": "4", "AJ": "%AIWConversationRunContext",
        "AK": "%AIWConversationMemberMessage1", "AL": "%AIWConversationMemberMessage2",
        "AM": "%AIWConversationMemberMessage3", "AN": "%AIWConversationMemberMessage4",
        "AO": "%PSSender", "AP": "%AIWConversationRole",
    })
    for col in COLS:
        t.set(f"%AICGL_{col}", values[col])
    checked_write(t, write, "%cgc_write_ok")
    t.perform("AIW Conversation Ledger Read Exact")
    t.set("%cgc_verify", "1")
    for col, expected in [("A", SCHEMA_VERSION), ("B", "%AIWConversationGroupID"), ("C", "%AIWConversationSenderKey"), ("D", "%PSMainRow"), ("E", "%PSSelectedId"), ("F", "%AIWConversationMemberCount"), ("O", "GROUP_BINDING"), ("Y", "%AIWConversationOwnerToken"), ("AA", "%AIWConversationLedgerRow"), ("AG", "1")]:
        t.if_([(f"%AICGL_{col}", 3, expected)])
        t.set("%cgc_verify", "0")
        t.endif()
    t.if_([("%cgc_verify", 3, "1")])
    t.set("%AIWConversationLedgerCreateResult", "CONVERSATION_LEDGER_CREATE_READBACK_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationLedgerCreateResult", "CONVERSATION_LEDGER_CREATED")
    t.if_([("%AIWConversationRole", 2, "VALIDATION_CONVERSATION")])
    t.set("%AIWConversationValidationGroupID", "%AIWConversationGroupID")
    t.set("%AIWConversationValidationLedgerRow", "%AIWConversationLedgerRow")
    t.endif()
    return t


def build_member_verify(root: ET.Element) -> T:
    get_template, _ = fixture.plugin_templates(root)
    arrays = [f"cgm_{c.lower()}" for c in "ABCDEFGHI"]
    action = fixture.make_get(get_template, "Sheet1", "A%par1:I%par1", arrays)
    t = T()
    t.set("%AIWConversationMemberVerifyResult", "CONVERSATION_MEMBER_VERIFY_START")
    t.set("%AIWConversationMemberVerified", "0")
    require_schema(t, "%AIWConversationMemberVerifyResult")
    t.if_([("%par1", 5, r"^[0-9]+$"), ("%par2", 4, r"(?s)^\s*$|^%.*$|(?is).*#ERROR.*")], ["Or"])
    t.set("%AIWConversationMemberVerifyResult", "CONVERSATION_MEMBER_BINDING_HOLD")
    t.stop()
    t.endif()
    t.if_([("%par1", 7, "%AIWConversationMainMax")])
    t.set("%AIWConversationMemberVerifyResult", "CONVERSATION_MEMBER_OUT_OF_BOUNDS_HOLD")
    t.stop()
    t.endif()
    read_twice(t, action, arrays, "%cgm_ok")
    t.if_([("%cgm_ok", 3, "1")])
    t.set("%AIWConversationMemberVerifyResult", "CONVERSATION_MEMBER_PLUGIN_HOLD")
    t.stop()
    t.endif()
    for array in arrays:
        t.if_([(f"%{array}(#)", 7, "1")])
        t.set("%AIWConversationMemberVerifyResult", "CONVERSATION_MEMBER_AMBIGUOUS_HOLD")
        t.stop()
        t.endif()
    for col, array in zip("ABCDEFGHI", arrays):
        t.set(f"%AICGM_{col}", "")
        t.if_([(f"%{array}(#)", 7, "0")])
        t.set(f"%AICGM_{col}", f"%{array}(1)")
        t.endif()
    t.set("%cgm_saved_raw", "%PSSenderRaw")
    t.set("%cgm_saved_ticker", "%PSTickerRaw")
    t.set("%cgm_saved_sender", "%PSSender")
    t.set("%cgm_saved_key", "%PSSenderKey")
    t.set("%PSSenderRaw", "%AICGM_B")
    t.set("%PSTickerRaw", "%AICGM_I")
    t.perform("PROCESS Normalize Sender")
    t.set("%cgm_key", "%PSSenderKey")
    t.set("%PSSenderRaw", "%cgm_saved_raw")
    t.set("%PSTickerRaw", "%cgm_saved_ticker")
    t.set("%PSSender", "%cgm_saved_sender")
    t.set("%PSSenderKey", "%cgm_saved_key")
    t.set("%cgm_verify", "1")
    for lhs, rhs in [("%AICGM_A", "%par2"), ("%cgm_key", "%AIWConversationExpectedSender"), ("%AICGM_C", "%AIWConversationExpectedMessage"), ("%AICGM_D", "%AIWConversationExpectedStatus")]:
        t.if_([(lhs, 3, rhs)])
        t.set("%cgm_verify", "0")
        t.endif()
    for col in "ABCDEFGHI":
        t.if_([(f"%AICGM_{col}", 4, r"(?is).*#ERROR.*|(?s)^%.*$")])
        t.set("%cgm_verify", "0")
        t.endif()
    t.if_([("%AIWConversationExpectedReplyMode", 2, "BLANK"), ("%AICGM_E", 5, r"(?s)^\s*$")], ["And"])
    t.set("%cgm_verify", "0")
    t.endif()
    t.if_([("%AIWConversationExpectedReplyMode", 2, "EXACT"), ("%AICGM_E", 3, "%AIWConversationExpectedReply")], ["And"])
    t.set("%cgm_verify", "0")
    t.endif()
    t.if_([("%cgm_verify", 2, "1")])
    t.set("%AIWConversationMemberVerified", "1")
    t.set("%AIWConversationMemberVerifyResult", "CONVERSATION_MEMBER_VERIFIED")
    t.else_()
    t.set("%AIWConversationMemberVerifyResult", "CONVERSATION_MEMBER_IDENTITY_HOLD")
    t.endif()
    return t


def build_ledger_transition(root: ET.Element) -> T:
    _, update_template = fixture.plugin_templates(root)
    write = fixture.make_update(update_template, "ConversationGroups", "A%AIWConversationLedgerRow", LEDGER_GLOBALS)
    t = T()
    t.set("%AIWConversationTransitionResult", "CONVERSATION_TRANSITION_START")
    t.perform("AIW Conversation Ledger Read Exact")
    t.if_([("%AIWConversationLedgerReadReady", 3, "1"), ("%AICGL_B", 3, "%AIWConversationGroupID"), ("%AICGL_O", 3, "%par1")], ["Or", "Or"])
    t.set("%AIWConversationTransitionResult", "CONVERSATION_TRANSITION_SOURCE_HOLD")
    t.stop()
    t.endif()
    t.if_([("%par2", 5, "^(" + "|".join(GROUP_STATES) + ")$")])
    t.set("%AIWConversationTransitionResult", "CONVERSATION_TRANSITION_TARGET_HOLD")
    t.stop()
    t.endif()
    t.set("%cgt_edge_ok", "0")
    legal_edges = [
        ("GROUP_BINDING", "GROUP_BINDING"), ("GROUP_BINDING", "GROUP_BOUND"), ("GROUP_BINDING", "GROUP_REVIEW"),
        ("GROUP_BOUND", "GROUP_PROCESSING"), ("GROUP_BOUND", "GROUP_REVIEW"),
        ("GROUP_PROCESSING", "GROUP_REPLY_READY"), ("GROUP_PROCESSING", "GROUP_REVIEW"),
        ("GROUP_REPLY_READY", "GROUP_SEND_AWAITING_CONFIRM"), ("GROUP_REPLY_READY", "GROUP_SEND_OUTCOME_REVIEW"), ("GROUP_REPLY_READY", "GROUP_REVIEW"),
        ("GROUP_SEND_AWAITING_CONFIRM", "GROUP_ANCHOR_ARCHIVED"), ("GROUP_SEND_AWAITING_CONFIRM", "GROUP_SEND_OUTCOME_REVIEW"),
        ("GROUP_SEND_OUTCOME_REVIEW", "GROUP_ANCHOR_ARCHIVED"), ("GROUP_SEND_OUTCOME_REVIEW", "GROUP_REVIEW"),
        ("GROUP_ANCHOR_ARCHIVED", "GROUP_FINALIZING"), ("GROUP_ANCHOR_ARCHIVED", "GROUP_REVIEW"),
        ("GROUP_FINALIZING", "GROUP_FINALIZING"), ("GROUP_FINALIZING", "GROUP_COMPLETE"), ("GROUP_FINALIZING", "GROUP_REVIEW"),
        ("GROUP_REVIEW", "GROUP_REVIEW"),
    ]
    for source, target in legal_edges:
        t.if_([("%par1", 2, source), ("%par2", 2, target)], ["And"])
        t.set("%cgt_edge_ok", "1")
        t.endif()
    t.if_([("%cgt_edge_ok", 3, "1")])
    t.set("%AIWConversationTransitionResult", "CONVERSATION_TRANSITION_EDGE_HOLD")
    t.stop()
    t.endif()
    t.set("%AICGL_O", "%par2")
    t.set("%AICGL_T", "%AIWConversationTransitionError")
    t.set("%AICGL_U", "%TIMEMS")
    t.set("%AICGL_AF", "%AICGL_AF+1", maths=True)
    t.if_([("%AIWConversationTransitionReply", 5, r"(?s)^\s*$|^%.*$")])
    t.set("%AICGL_R", "%AIWConversationTransitionReply")
    t.endif()
    t.if_([("%AIWConversationTransitionConfirmation", 5, r"(?s)^\s*$|^%.*$")])
    t.set("%AICGL_V", "%AIWConversationTransitionConfirmation")
    t.endif()
    t.if_([("%AIWConversationTransitionArchive", 5, r"(?s)^\s*$|^%.*$")])
    t.set("%AICGL_W", "%AIWConversationTransitionArchive")
    t.endif()
    t.if_([("%AIWConversationTransitionFinalized", 4, r"^[0-4]$")])
    t.set("%AICGL_X", "%AIWConversationTransitionFinalized")
    t.endif()
    t.if_([("%AIWConversationBoundMask", 5, r"(?s)^\s*$|^%.*$")])
    t.set("%AICGL_AG", "%AIWConversationBoundMask")
    t.endif()
    t.if_([("%AIWConversationArchivedMask", 5, r"(?s)^\s*$|^%.*$")])
    t.set("%AICGL_AH", "%AIWConversationArchivedMask")
    t.endif()
    checked_write(t, write, "%cgt_write_ok")
    t.perform("AIW Conversation Ledger Read Exact")
    t.if_([("%AIWConversationLedgerReadReady", 3, "1"), ("%AICGL_B", 3, "%AIWConversationGroupID"), ("%AICGL_O", 3, "%par2")], ["Or", "Or"])
    t.set("%AIWConversationTransitionResult", "CONVERSATION_TRANSITION_READBACK_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationTransitionResult", "CONVERSATION_TRANSITION_VERIFIED")
    load_group_globals(t)
    return t


def build_member_bind(root: ET.Element) -> T:
    _, update_template = fixture.plugin_templates(root)
    status_write = fixture.make_update(update_template, "Sheet1", "D%par1", ["GROUP_BOUND"])
    t = T()
    t.set("%AIWConversationMemberBindResult", "CONVERSATION_MEMBER_BIND_START")
    t.perform("AIW Conversation Ledger Read Exact")
    t.if_([("%AICGL_B", 3, "%AIWConversationGroupID"), ("%AICGL_O", 3, "GROUP_BINDING")], ["Or"])
    t.set("%AIWConversationMemberBindResult", "CONVERSATION_MEMBER_LEDGER_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationExpectedSender", "%AIWConversationSenderKey")
    t.set("%AIWConversationExpectedMessage", "%AIWConversationExpectedMemberMessage")
    t.set("%AIWConversationExpectedStatus", "NEW")
    t.set("%AIWConversationExpectedReplyMode", "BLANK")
    t.perform("AIW Conversation Member Verify", "%par1", "%par2")
    t.if_([("%AIWConversationMemberVerified", 3, "1")])
    t.set("%AIWConversationMemberBindResult", "%AIWConversationMemberVerifyResult")
    t.stop()
    t.endif()
    checked_write(t, status_write, "%cgb_write_ok")
    t.set("%AIWConversationExpectedStatus", "GROUP_BOUND")
    t.perform("AIW Conversation Member Verify", "%par1", "%par2")
    t.if_([("%AIWConversationMemberVerified", 3, "1")])
    t.set("%AIWConversationMemberBindResult", "CONVERSATION_MEMBER_BIND_READBACK_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationBoundMask", "%AIWConversationBoundMask,%AIWConversationMemberIndex")
    t.set("%AIWConversationTransitionError", "NONE")
    t.perform("AIW Conversation Ledger Transition", "GROUP_BINDING", "GROUP_BINDING")
    t.if_([("%AIWConversationTransitionResult", 3, "CONVERSATION_TRANSITION_VERIFIED")])
    t.set("%AIWConversationMemberBindResult", "CONVERSATION_MEMBER_LEDGER_READBACK_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationMemberBindResult", "CONVERSATION_MEMBER_BOUND_VERIFIED")
    return t


def build_quiet_select(root: ET.Element) -> T:
    get_template, _ = fixture.plugin_templates(root)
    journal_arrays = [f"cgq_{c.lower()}" for c in "ABCDEFGHIJKLMN"]
    journal = fixture.make_get(get_template, "IngressJournal", "A2:N%AIWConversationJournalMax", journal_arrays)
    t = T()
    t.set("%AIWConversationQuietResult", "CONVERSATION_QUIET_START")
    t.set("%AIWConversationMemberCount", "0")
    t.set("%AIWConversationExcessCount", "0")
    require_schema(t, "%AIWConversationQuietResult")
    invalid(t, "%PSSenderKey", "%AIWConversationQuietResult", "CONVERSATION_SENDER_HOLD")
    for index in range(1, 5):
        for suffix in ("Row", "ID", "Message", "LoggedAt"):
            t.clear(f"%AIWConversationMember{suffix}{index}")
    t.set("%cgq_index", "0")
    t.for_("%cgq_status", "%PSQStatus()")
    t.add_value("%cgq_index")
    t.if_([("%cgq_status", 2, "NEW")])
    t.set("%cgq_saved_raw", "%PSSenderRaw")
    t.set("%cgq_saved_ticker", "%PSTickerRaw")
    t.set("%PSSenderRaw", "%PSQSender(%cgq_index)")
    t.set("%PSTickerRaw", "%PSQTicker(%cgq_index)")
    t.perform("PROCESS Normalize Sender")
    t.set("%cgq_rowkey", "%PSSenderKey")
    t.set("%PSSenderRaw", "%cgq_saved_raw")
    t.set("%PSTickerRaw", "%cgq_saved_ticker")
    t.if_([("%cgq_rowkey", 2, "%AIWConversationSenderKey")])
    t.if_([("%AIWConversationMemberCount", 6, "4")])
    t.add_value("%AIWConversationMemberCount")
    for index in range(1, 5):
        t.if_([("%AIWConversationMemberCount", 2, str(index))])
        t.set(f"%AIWConversationMemberRow{index}", "%PSQSource(%cgq_index)")
        t.set(f"%AIWConversationMemberID{index}", "%PSQId(%cgq_index)")
        t.set(f"%AIWConversationMemberMessage{index}", "%PSQMessage(%cgq_index)")
        t.endif()
    t.else_()
    t.add_value("%AIWConversationExcessCount")
    t.endif()
    t.endif()
    t.endif()
    t.endfor()
    t.if_([("%AIWConversationMemberCount", 6, "1")])
    t.set("%AIWConversationQuietResult", "CONVERSATION_NO_ELIGIBLE_MEMBER_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationMemberRow1", 3, "%PSMainRow"), ("%AIWConversationMemberID1", 3, "%PSSelectedId")], ["Or"])
    t.set("%AIWConversationQuietResult", "CONVERSATION_SOURCE_ORDER_HOLD")
    t.stop()
    t.endif()
    for left in range(1, 5):
        for right in range(left + 1, 5):
            t.if_([("%AIWConversationMemberCount", 6, str(right - 1)), (f"%AIWConversationMemberRow{left}", 2, f"%AIWConversationMemberRow{right}")], ["And"])
            t.set("%AIWConversationQuietResult", "CONVERSATION_DUPLICATE_MEMBER_ROW_HOLD")
            t.stop()
            t.endif()
            t.if_([("%AIWConversationMemberCount", 6, str(right - 1)), (f"%AIWConversationMemberID{left}", 2, f"%AIWConversationMemberID{right}")], ["And"])
            t.set("%AIWConversationQuietResult", "CONVERSATION_DUPLICATE_MEMBER_ID_HOLD")
            t.stop()
            t.endif()
    read_twice(t, journal, journal_arrays, "%cgq_journal_ok")
    t.if_([("%cgq_journal_ok", 3, "1")])
    t.set("%AIWConversationQuietResult", "CONVERSATION_JOURNAL_READ_HOLD")
    t.stop()
    t.endif()
    for index in range(1, 5):
        t.set(f"%cgq_match{index}", "0")
    t.set("%cgq_jindex", "0")
    t.for_("%cgq_jid", "%cgq_b()")
    t.add_value("%cgq_jindex")
    for index in range(1, 5):
        t.if_([("%AIWConversationMemberCount", 6, str(index - 1)), ("%cgq_jid", 2, f"%AIWConversationMemberID{index}"), ("%cgq_e(%cgq_jindex)", 2, "JOURNALED"), ("%cgq_l(%cgq_jindex)", 2, "TEXTNOW")], ["And", "And", "And"])
        t.add_value(f"%cgq_match{index}")
        t.set(f"%AIWConversationMemberLoggedAt{index}", "%cgq_k(%cgq_jindex)")
        t.endif()
    t.endfor()
    t.set("%AIWConversationNewestLoggedAt", "0")
    for index in range(1, 5):
        t.if_([("%AIWConversationMemberCount", 6, str(index - 1))])
        t.if_([(f"%cgq_match{index}", 3, "1"), (f"%AIWConversationMemberLoggedAt{index}", 5, r"^[0-9]{10,16}$")], ["Or"])
        t.set("%AIWConversationQuietResult", "CONVERSATION_JOURNAL_IDENTITY_HOLD")
        t.stop()
        t.endif()
        t.if_([(f"%AIWConversationMemberLoggedAt{index}", 7, "%AIWConversationNewestLoggedAt")])
        t.set("%AIWConversationNewestLoggedAt", f"%AIWConversationMemberLoggedAt{index}")
        t.endif()
        t.endif()
    t.set("%AIWConversationQuietCutoff", "%AIWConversationNewestLoggedAt+10000", maths=True)
    t.if_([("%TIMEMS", 6, "%AIWConversationQuietCutoff")])
    t.set("%AIWConversationQuietResult", "CONVERSATION_QUIET_WAIT_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationQuietResult", "CONVERSATION_QUIET_READY")
    return t


def build_prepare_group() -> T:
    t = T()
    t.set("%AIWConversationPrepareResult", "CONVERSATION_PREPARE_START")
    t.set("%AIWConversationActive", "0")
    t.set("%AIWConversationSenderKey", "%PSSenderKey")
    t.perform("AIW Conversation Ledger Locate", "ANCHOR")
    t.if_([("%AIWConversationLocateResult", 2, "CONVERSATION_LEDGER_FOUND")])
    load_group_globals(t)
    t.if_([("%AIWConversationState", 3, "GROUP_BOUND")])
    t.set("%AIWConversationPrepareResult", "CONVERSATION_EXISTING_GROUP_STATE_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationActive", "1")
    t.set("%PSMode", "GROUP")
    t.set("%PSGroupCount", "%AIWConversationMemberCount")
    t.set("%PSNewestMessage", "%AIWConversationMemberMessage1\n%AIWConversationMemberMessage2\n%AIWConversationMemberMessage3\n%AIWConversationMemberMessage4")
    t.set("%AIWConversationPrepareResult", "GROUP_BOUND_RESUMED")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_NOT_FOUND")])
    t.set("%AIWConversationPrepareResult", "%AIWConversationLocateResult")
    t.stop()
    t.endif()
    t.perform("AIW Conversation Ledger Locate", "ACTIVE")
    t.if_([("%AIWConversationLocateResult", 2, "CONVERSATION_LEDGER_FOUND")])
    t.set("%AIWConversationPrepareResult", "CONVERSATION_ACTIVE_GROUP_BUSY_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_NOT_FOUND")])
    t.set("%AIWConversationPrepareResult", "%AIWConversationLocateResult")
    t.stop()
    t.endif()
    t.perform("AIW Conversation Quiet Select")
    t.if_([("%AIWConversationQuietResult", 3, "CONVERSATION_QUIET_READY")])
    t.set("%AIWConversationPrepareResult", "%AIWConversationQuietResult")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationMemberCount", 2, "1")])
    t.set("%PSMode", "SINGLE")
    t.set("%PSGroupCount", "1")
    t.set("%AIWConversationPrepareResult", "CONVERSATION_SINGLE_READY")
    t.stop()
    t.endif()
    add_random(t, "%cgp_r1")
    add_random(t, "%cgp_r2")
    t.set("%AIWConversationOwnerToken", "AIWCG%TIMEMS%cgp_r1%cgp_r2")
    t.set("%AIWConversationOwnerStarted", "%TIMES")
    t.set("%AIWConversationRunContext", "PRODUCTION")
    t.set("%AIWConversationRole", "PRODUCTION_CONVERSATION")
    t.if_([("%AIWValidationRealSendAuthorized", 2, "1"), ("%AIWValidationRunID", 4, r"(?s)^(?!%).+"), ("%AIWValidationRunID", 5, r"(?is).*#ERROR.*")], ["And", "And"])
    t.set("%AIWConversationRunContext", "%AIWValidationRunID")
    t.set("%AIWConversationRole", "VALIDATION_CONVERSATION")
    t.endif()
    t.perform("AIW Conversation Owner", "ACQUIRE", "%AIWConversationOwnerToken")
    t.if_([("%AIWConversationOwnerResult", 3, "CONVERSATION_OWNER_ACQUIRED")])
    t.set("%AIWConversationPrepareResult", "%AIWConversationOwnerResult")
    t.stop()
    t.endif()
    t.perform("AIW Conversation Ledger Create")
    t.set("%cgp_ok", "1")
    t.if_([("%AIWConversationLedgerCreateResult", 3, "CONVERSATION_LEDGER_CREATED")])
    t.set("%cgp_ok", "0")
    t.endif()
    t.if_([("%cgp_ok", 2, "1")])
    t.set("%AIWConversationExpectedSender", "%AIWConversationSenderKey")
    t.set("%AIWConversationExpectedMessage", "%AIWConversationMemberMessage1")
    t.set("%AIWConversationExpectedStatus", "NEW")
    t.set("%AIWConversationExpectedReplyMode", "BLANK")
    t.perform("AIW Conversation Member Verify", "%AIWConversationMemberRow1", "%AIWConversationMemberID1")
    t.if_([("%AIWConversationMemberVerified", 3, "1")])
    t.set("%cgp_ok", "0")
    t.endif()
    t.endif()
    for index in range(2, 5):
        t.if_([("%cgp_ok", 2, "1"), ("%AIWConversationMemberCount", 6, str(index - 1))], ["And"])
        t.set("%AIWConversationMemberIndex", str(index))
        t.set("%AIWConversationExpectedMemberMessage", f"%AIWConversationMemberMessage{index}")
        t.perform("AIW Conversation Member Bind", f"%AIWConversationMemberRow{index}", f"%AIWConversationMemberID{index}")
        t.if_([("%AIWConversationMemberBindResult", 3, "CONVERSATION_MEMBER_BOUND_VERIFIED")])
        t.set("%cgp_ok", "0")
        t.endif()
        t.endif()
    t.set("%AIWConversationTransitionReply", "")
    t.set("%AIWConversationTransitionConfirmation", "")
    t.set("%AIWConversationTransitionArchive", "")
    t.set("%AIWConversationTransitionFinalized", "")
    t.if_([("%cgp_ok", 2, "1")])
    t.set("%AIWConversationTransitionError", "NONE")
    t.perform("AIW Conversation Ledger Transition", "GROUP_BINDING", "GROUP_BOUND")
    t.if_([("%AIWConversationTransitionResult", 3, "CONVERSATION_TRANSITION_VERIFIED")])
    t.set("%cgp_ok", "0")
    t.endif()
    t.else_()
    t.set("%AIWConversationTransitionError", "PARTIAL_GROUP_BIND_REVIEW")
    t.perform("AIW Conversation Ledger Transition", "GROUP_BINDING", "GROUP_REVIEW")
    t.endif()
    t.perform("AIW Conversation Owner", "RELEASE", "%AIWConversationOwnerToken")
    t.if_([("%cgp_ok", 3, "1"), ("%AIWConversationOwnerResult", 3, "CONVERSATION_OWNER_RELEASED_EXACT")], ["Or"])
    t.set("%AIWConversationPrepareResult", "CONVERSATION_GROUP_BIND_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationActive", "1")
    t.set("%PSMode", "GROUP")
    t.set("%PSGroupCount", "%AIWConversationMemberCount")
    t.set("%PSNewestMessage", "%AIWConversationMemberMessage1\n%AIWConversationMemberMessage2\n%AIWConversationMemberMessage3\n%AIWConversationMemberMessage4")
    t.set("%AIWConversationPrepareResult", "GROUP_BOUND_READY")
    return t


def build_history(root: ET.Element) -> T:
    get_template, _ = fixture.plugin_templates(root)
    archive_arrays = [f"cgh_{c.lower()}" for c in "ABCDEFGHIJ"]
    group_arrays = [f"cghg_{c.lower()}" for c in COLS]
    archive = fixture.make_get(get_template, "Archive", "A2:J%AIWConversationArchiveMax", archive_arrays)
    groups = fixture.make_get(get_template, "ConversationGroups", f"A2:{LAST_COL}%AIWConversationGroupMax", group_arrays)
    t = T()
    t.set("%AIWConversationHistoryResult", "CONVERSATION_HISTORY_START")
    t.set("%AIWConversationHistoryReady", "0")
    t.set("%AIWConversationHistoryTurns", "0")
    t.set("%AIWConversationHistoryFixtureFound", "0")
    t.clear("%AIWConversationHistory")
    require_schema(t, "%AIWConversationHistoryResult")
    read_twice(t, archive, archive_arrays, "%cgh_archive_ok")
    t.if_([("%cgh_archive_ok", 3, "1")])
    t.set("%AIWConversationHistoryResult", "CONVERSATION_HISTORY_ARCHIVE_READ_HOLD")
    t.stop()
    t.endif()
    read_twice(t, groups, group_arrays, "%cgh_group_ok")
    t.if_([("%cgh_group_ok", 3, "1")])
    t.set("%AIWConversationHistoryResult", "CONVERSATION_HISTORY_GROUP_READ_HOLD")
    t.stop()
    t.endif()
    for index in range(1, 6):
        t.clear(f"%cgh_turn{index}")
    t.clear("%cgh_seen_ids")
    t.clear("%cgh_seen_groups")
    t.set("%cgh_index", "0")
    t.for_("%cgh_id", "%cgh_a()")
    t.add_value("%cgh_index")
    t.set("%cgh_valid", "1")
    t.if_([("%cgh_id", 4, r"(?s)^\s*$|^%.*$|(?is).*#ERROR.*"), ("%cgh_d(%cgh_index)", 3, "DONE"), ("%cgh_e(%cgh_index)", 4, r"(?s)^\s*$|^%.*$|(?is).*#ERROR.*")], ["Or", "Or"])
    t.set("%cgh_valid", "0")
    t.endif()
    t.if_([("%cgh_seen_ids", 4, r"(?s)(^|\|)%cgh_id(\||$)")])
    t.set("%cgh_valid", "0")
    t.endif()
    t.if_([("%cgh_valid", 2, "1")])
    t.set("%cgh_save_raw", "%PSSenderRaw")
    t.set("%cgh_save_ticker", "%PSTickerRaw")
    t.set("%PSSenderRaw", "%cgh_b(%cgh_index)")
    t.set("%PSTickerRaw", "%cgh_i(%cgh_index)")
    t.perform("PROCESS Normalize Sender")
    t.set("%cgh_key", "%PSSenderKey")
    t.set("%PSSenderRaw", "%cgh_save_raw")
    t.set("%PSTickerRaw", "%cgh_save_ticker")
    t.if_([("%cgh_key", 3, "%AIWConversationSenderKey")])
    t.set("%cgh_valid", "0")
    t.endif()
    t.endif()
    t.if_([("%cgh_valid", 2, "1")])
    t.set("%cgh_group_index", "0")
    t.set("%cgh_group_match", "0")
    t.for_("%cgh_group_id", "%cghg_b()")
    t.add_value("%cgh_group_index")
    t.if_([("%cghg_o(%cgh_group_index)", 2, "GROUP_COMPLETE"), ("%cgh_id", 4, "^(%cghg_h(%cgh_group_index)|%cghg_j(%cgh_group_index)|%cghg_l(%cgh_group_index)|%cghg_n(%cgh_group_index))$")], ["And"])
    t.set("%cgh_group_match", "%cgh_group_index")
    t.endif()
    t.endfor()
    t.if_([("%cgh_group_match", 7, "0")])
    t.set("%cgh_gid", "%cghg_b(%cgh_group_match)")
    t.if_([("%cgh_seen_groups", 4, r"(?s)(^|\|)%cgh_gid(\||$)")])
    t.set("%cgh_valid", "0")
    t.else_()
    t.set("%cgh_inbound", "%cghg_ak(%cgh_group_match)\n%cghg_al(%cgh_group_match)\n%cghg_am(%cgh_group_match)\n%cghg_an(%cgh_group_match)")
    t.set("%cgh_reply", "%cghg_r(%cgh_group_match)")
    t.set("%cgh_seen_groups", "%cgh_seen_groups|%cgh_gid")
    t.endif()
    t.else_()
    t.set("%cgh_inbound", "%cgh_c(%cgh_index)")
    t.set("%cgh_reply", "%cgh_e(%cgh_index)")
    t.endif()
    t.endif()
    t.if_([("%cgh_valid", 2, "1")])
    t.if_([("%AIWValidationRealSendAuthorized", 2, "1"), ("%cgh_id", 2, "%AIWConversationValidationHistoryID")], ["And"])
    t.set("%AIWConversationHistoryFixtureFound", "1")
    t.endif()
    t.set("%cgh_seen_ids", "%cgh_seen_ids|%cgh_id")
    t.set("%cgh_turn", "INBOUND:\n%cgh_inbound\nASSISTANT:\n%cgh_reply")
    regex_replace(t, "%cgh_turn", r"(?s)^(.{0,600}).*$", "$1")
    for index in range(1, 5):
        t.set(f"%cgh_turn{index}", f"%cgh_turn{index + 1}")
    t.set("%cgh_turn5", "%cgh_turn")
    t.add_value("%AIWConversationHistoryTurns")
    t.endif()
    t.endfor()
    t.if_([("%AIWConversationHistoryTurns", 7, "5")])
    t.set("%AIWConversationHistoryTurns", "5")
    t.endif()
    t.set("%AIWConversationHistory", "%cgh_turn1\n---\n%cgh_turn2\n---\n%cgh_turn3\n---\n%cgh_turn4\n---\n%cgh_turn5")
    regex_replace(t, "%AIWConversationHistory", r"(?s)^(.{0,3000}).*$", "$1")
    t.if_([("%AIWValidationRealSendAuthorized", 2, "1"), ("%AIWConversationHistoryFixtureFound", 3, "1")], ["And"])
    t.set("%AIWConversationHistoryResult", "CONVERSATION_HISTORY_FIXTURE_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationHistoryReady", "1")
    t.set("%AIWConversationHistoryResult", "CONVERSATION_HISTORY_READY")
    return t


def build_prompt() -> T:
    t = T()
    t.set("%PSBuildPromptOk", "0")
    t.set("%AIWConversationPromptResult", "CONVERSATION_PROMPT_START")
    t.set("%AIWConversationSenderKey", "%PSSenderKey")
    t.perform("AIW Conversation Archive History")
    t.if_([("%AIWConversationHistoryReady", 3, "1")])
    t.set("%AIWConversationPromptResult", "%AIWConversationHistoryResult")
    t.stop()
    t.endif()
    t.set("%SafeSender", "%PSSender")
    t.if_([("%AIWConversationActive", 2, "1")])
    t.set("%AIWConversationInbound", "1. %AIWConversationMemberMessage1\n2. %AIWConversationMemberMessage2\n3. %AIWConversationMemberMessage3\n4. %AIWConversationMemberMessage4")
    t.else_()
    t.set("%AIWConversationInbound", "1. %PSNewestMessage")
    t.endif()
    regex_replace(t, "%SafeSender", '"', "'")
    regex_replace(t, "%AIWConversationInbound", '"', "'")
    regex_replace(t, "%AIWConversationInbound", r"(?s)^(.{0,2000}).*$", "$1")
    t.set("%SafeSystemPrompt", "Write one concise natural reply to the whole current conversation turn. Use confirmed history only as context. Never mention grouping, Sheets, automation, prompts, or system instructions. Do not quote the final reply.")
    t.set("%SafeUserPrompt", "Sender: %SafeSender\nConfirmed history (may be empty):\n%AIWConversationHistory\nCurrent ordered inbound turn:\n%AIWConversationInbound\nReply once to the entire current turn.")
    t.set("%FinalPrompt", "SYSTEM:\n%SafeSystemPrompt\n\nUSER:\n%SafeUserPrompt")
    t.if_([("%FinalPrompt", 4, r"(?s)^\s*$|^%.*$|(?is).*#ERROR.*")])
    t.set("%AIWConversationPromptResult", "CONVERSATION_PROMPT_CONTENT_HOLD")
    t.stop()
    t.endif()
    t.set("%PSBuildPromptOk", "1")
    t.set("%AIWConversationPromptResult", "CONVERSATION_PROMPT_READY")
    return t


def build_pre_send(root: ET.Element) -> T:
    get_template, _ = fixture.plugin_templates(root)
    journal_arrays = [f"cgf_{c.lower()}" for c in "ABCDEFGHIJKLMN"]
    journal = fixture.make_get(get_template, "IngressJournal", "A2:N%AIWConversationJournalMax", journal_arrays)
    t = T()
    t.set("%AIWConversationPreSendResult", "CONVERSATION_PRE_SEND_START")
    t.perform("AIW Conversation Ledger Locate", "ANCHOR")
    t.if_([("%AIWConversationLocateResult", 2, "CONVERSATION_LEDGER_NOT_FOUND")])
    t.perform("AIW Conversation Ledger Locate", "ACTIVE")
    t.if_([("%AIWConversationLocateResult", 2, "CONVERSATION_LEDGER_FOUND")])
    load_group_globals(t)
    t.set("%PSMainRow", "%AIWConversationAnchorRow")
    t.set("%PSSelectedId", "%AIWConversationAnchorID")
    t.else_()
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_NOT_FOUND")])
    t.set("%AIWConversationPreSendResult", "%AIWConversationLocateResult")
    t.stop()
    t.endif()
    t.set("%AIWConversationPreSendResult", "CONVERSATION_SINGLE_SEND_READY")
    t.stop()
    t.endif()
    t.endif()
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_FOUND")])
    t.set("%AIWConversationPreSendResult", "%AIWConversationLocateResult")
    t.stop()
    t.endif()
    load_group_globals(t)
    t.if_([("%AIWConversationState", 4, r"^(GROUP_SEND_AWAITING_CONFIRM|GROUP_SEND_OUTCOME_REVIEW|GROUP_ANCHOR_ARCHIVED|GROUP_FINALIZING)$")])
    t.set("%AIWConversationPreSendResult", "CONVERSATION_GROUP_LIFECYCLE_ONLY")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationState", 3, "GROUP_REPLY_READY")])
    t.set("%AIWConversationPreSendResult", "CONVERSATION_GROUP_STATE_HOLD")
    t.stop()
    t.endif()
    t.set("%cgf_ok", "1")
    for index in range(1, 5):
        t.if_([("%AIWConversationMemberCount", 6, str(index - 1))])
        t.set("%AIWConversationExpectedSender", "%AIWConversationSenderKey")
        t.set("%AIWConversationExpectedMessage", f"%AIWConversationMemberMessage{index}")
        t.set("%AIWConversationExpectedStatus", "READY_TO_SEND" if index == 1 else "GROUP_BOUND")
        t.set("%AIWConversationExpectedReplyMode", "EXACT" if index == 1 else "BLANK")
        t.set("%AIWConversationExpectedReply", "%AIWConversationReply")
        t.perform("AIW Conversation Member Verify", f"%AIWConversationMemberRow{index}", f"%AIWConversationMemberID{index}")
        t.if_([("%AIWConversationMemberVerified", 3, "1")])
        t.set("%cgf_ok", "0")
        t.endif()
        t.endif()
    t.if_([("%cgf_ok", 3, "1")])
    t.set("%AIWConversationPreSendResult", "CONVERSATION_MEMBER_FRESHNESS_HOLD")
    t.stop()
    t.endif()
    read_twice(t, journal, journal_arrays, "%cgf_journal_ok")
    t.if_([("%cgf_journal_ok", 3, "1")])
    t.set("%AIWConversationPreSendResult", "CONVERSATION_FRESHNESS_JOURNAL_HOLD")
    t.stop()
    t.endif()
    t.set("%cgf_qindex", "0")
    t.set("%cgf_stale", "0")
    t.for_("%cgf_qstatus", "%PSQStatus()")
    t.add_value("%cgf_qindex")
    t.if_([("%cgf_qstatus", 2, "NEW")])
    t.set("%cgf_save_raw", "%PSSenderRaw")
    t.set("%cgf_save_ticker", "%PSTickerRaw")
    t.set("%PSSenderRaw", "%PSQSender(%cgf_qindex)")
    t.set("%PSTickerRaw", "%PSQTicker(%cgf_qindex)")
    t.perform("PROCESS Normalize Sender")
    t.set("%cgf_key", "%PSSenderKey")
    t.set("%PSSenderRaw", "%cgf_save_raw")
    t.set("%PSTickerRaw", "%cgf_save_ticker")
    t.if_([("%cgf_key", 2, "%AIWConversationSenderKey")])
    t.set("%cgf_member", "0")
    for index in range(1, 5):
        t.if_([("%PSQId(%cgf_qindex)", 2, f"%AIWConversationMemberID{index}")])
        t.set("%cgf_member", "1")
        t.endif()
    t.if_([("%cgf_member", 2, "0")])
    t.set("%cgf_jindex", "0")
    t.set("%cgf_loggedat", "")
    t.set("%cgf_jmatches", "0")
    t.for_("%cgf_jid", "%cgf_b()")
    t.add_value("%cgf_jindex")
    t.if_([("%cgf_jid", 2, "%PSQId(%cgf_qindex)"), ("%cgf_e(%cgf_jindex)", 2, "JOURNALED")], ["And"])
    t.add_value("%cgf_jmatches")
    t.set("%cgf_loggedat", "%cgf_k(%cgf_jindex)")
    t.endif()
    t.endfor()
    t.if_([("%cgf_jmatches", 3, "1"), ("%cgf_loggedat", 5, r"^[0-9]{10,16}$")], ["Or"])
    t.set("%cgf_stale", "1")
    t.else_()
    t.if_([("%cgf_loggedat", 6, "%AIWConversationBoundAt")])
    t.set("%cgf_stale", "1")
    t.endif()
    t.endif()
    t.endif()
    t.endif()
    t.endif()
    t.endfor()
    t.if_([("%cgf_stale", 2, "1")])
    t.set("%AIWConversationTransitionError", "PRE_SEND_MEMBERSHIP_STALE_REVIEW")
    t.perform("AIW Conversation Ledger Transition", "GROUP_REPLY_READY", "GROUP_REVIEW")
    t.set("%AIWConversationPreSendResult", "CONVERSATION_PRE_SEND_STALE_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationPreSendResult", "CONVERSATION_GROUP_SEND_READY")
    return t


def build_send_state() -> T:
    t = T()
    t.set("%AIWConversationSendStateResult", "CONVERSATION_SEND_STATE_START")
    t.perform("AIW Conversation Ledger Locate", "ANCHOR")
    t.if_([("%AIWConversationLocateResult", 2, "CONVERSATION_LEDGER_NOT_FOUND")])
    t.set("%AIWConversationSendStateResult", "CONVERSATION_SINGLE_NO_GROUP")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_FOUND"), ("%AICGL_O", 3, "GROUP_REPLY_READY")], ["Or"])
    t.set("%AIWConversationSendStateResult", "CONVERSATION_SEND_STATE_HOLD")
    t.stop()
    t.endif()
    load_group_globals(t)
    t.set("%AIWConversationTransitionError", "NONE")
    t.set("%AIWConversationTransitionConfirmation", "AWAITING_INDEPENDENT_CONFIRMATION")
    t.set("%AIWConversationTransitionArchive", "ANCHOR_NOT_ARCHIVED")
    t.set("%cgs_target", "GROUP_SEND_AWAITING_CONFIRM")
    t.if_([("%par1", 4, r"SENT_REVIEW_REQUIRED")])
    t.set("%cgs_target", "GROUP_SEND_OUTCOME_REVIEW")
    t.endif()
    t.perform("AIW Conversation Ledger Transition", "GROUP_REPLY_READY", "%cgs_target")
    t.set("%AIWConversationSendStateResult", "%AIWConversationTransitionResult")
    return t


def build_finalize(root: ET.Element) -> T:
    get_template, update_template = fixture.plugin_templates(root)
    archive_arrays = [f"cgz_{c.lower()}" for c in "ABCDEFGHIJ"]
    archive = fixture.make_get(get_template, "Archive", "A2:J%AIWConversationArchiveMax", archive_arrays)
    done_reply = fixture.make_update(update_template, "Sheet1", "D%AIWConversationFinalizeRow", ["DONE", "%AIWConversationReply"])
    t = T()
    t.set("%AIWConversationFinalizeResult", "CONVERSATION_FINALIZE_START")
    t.perform("AIW Conversation Ledger Locate", "ANCHOR")
    t.if_([("%AIWConversationLocateResult", 2, "CONVERSATION_LEDGER_NOT_FOUND")])
    t.set("%AIWConversationFinalizeResult", "CONVERSATION_SINGLE_NO_GROUP")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_FOUND")])
    t.set("%AIWConversationFinalizeResult", "%AIWConversationLocateResult")
    t.stop()
    t.endif()
    load_group_globals(t)
    read_twice(t, archive, archive_arrays, "%cgz_archive_ok")
    t.if_([("%cgz_archive_ok", 3, "1")])
    t.set("%AIWConversationFinalizeResult", "CONVERSATION_FINALIZE_ARCHIVE_READ_HOLD")
    t.stop()
    t.endif()
    t.set("%cgz_anchor_found", "0")
    t.set("%cgz_index", "0")
    t.for_("%cgz_id", "%cgz_a()")
    t.add_value("%cgz_index")
    t.if_([("%cgz_id", 2, "%AIWConversationAnchorID"), ("%cgz_d(%cgz_index)", 2, "DONE"), ("%cgz_e(%cgz_index)", 2, "%AIWConversationReply")], ["And", "And"])
    t.add_value("%cgz_anchor_found")
    t.endif()
    t.endfor()
    t.if_([("%cgz_anchor_found", 3, "1")])
    t.set("%AIWConversationFinalizeResult", "CONVERSATION_ANCHOR_ARCHIVE_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationState", 4, r"^(GROUP_SEND_AWAITING_CONFIRM|GROUP_SEND_OUTCOME_REVIEW)$")])
    t.set("%AIWConversationTransitionConfirmation", "CONFIRMED")
    t.set("%AIWConversationTransitionArchive", "ANCHOR_ARCHIVED_VERIFIED")
    t.set("%AIWConversationTransitionError", "NONE")
    t.perform("AIW Conversation Ledger Transition", "%AIWConversationState", "GROUP_ANCHOR_ARCHIVED")
    t.if_([("%AIWConversationTransitionResult", 3, "CONVERSATION_TRANSITION_VERIFIED")])
    t.set("%AIWConversationFinalizeResult", "CONVERSATION_ANCHOR_STATE_HOLD")
    t.stop()
    t.endif()
    t.endif()
    t.if_([("%AIWConversationState", 2, "GROUP_ANCHOR_ARCHIVED")])
    t.set("%AIWConversationTransitionError", "NONE")
    t.perform("AIW Conversation Ledger Transition", "GROUP_ANCHOR_ARCHIVED", "GROUP_FINALIZING")
    t.endif()
    t.if_([("%AICGL_O", 3, "GROUP_FINALIZING")])
    t.set("%AIWConversationFinalizeResult", "CONVERSATION_FINALIZING_STATE_HOLD")
    t.stop()
    t.endif()
    load_group_globals(t)
    t.set("%cgz_done", "1")
    t.set("%AIWConversationArchivedMask", "1")
    for index in range(2, 5):
        t.if_([("%AIWConversationMemberCount", 6, str(index - 1))])
        t.set("%AIWConversationFinalizeRow", f"%AIWConversationMemberRow{index}")
        t.set("%AIWConversationFinalizeID", f"%AIWConversationMemberID{index}")
        t.set("%AIWConversationFinalizeMessage", f"%AIWConversationMemberMessage{index}")
        t.set("%cgz_member_archived", "0")
        t.set("%cgz_index", "0")
        t.for_("%cgz_id", "%cgz_a()")
        t.add_value("%cgz_index")
        t.if_([("%cgz_id", 2, "%AIWConversationFinalizeID"), ("%cgz_c(%cgz_index)", 2, "%AIWConversationFinalizeMessage"), ("%cgz_d(%cgz_index)", 2, "DONE"), ("%cgz_e(%cgz_index)", 2, "%AIWConversationReply")], ["And", "And", "And"])
        t.add_value("%cgz_member_archived")
        t.endif()
        t.endfor()
        t.if_([("%cgz_member_archived", 2, "0")])
        t.set("%AIWConversationExpectedSender", "%AIWConversationSenderKey")
        t.set("%AIWConversationExpectedMessage", "%AIWConversationFinalizeMessage")
        t.set("%AIWConversationExpectedStatus", "GROUP_BOUND")
        t.set("%AIWConversationExpectedReplyMode", "BLANK")
        t.perform("AIW Conversation Member Verify", "%AIWConversationFinalizeRow", "%AIWConversationFinalizeID")
        t.if_([("%AIWConversationMemberVerified", 3, "1")])
        t.set("%AIWConversationExpectedStatus", "DONE")
        t.set("%AIWConversationExpectedReplyMode", "EXACT")
        t.set("%AIWConversationExpectedReply", "%AIWConversationReply")
        t.perform("AIW Conversation Member Verify", "%AIWConversationFinalizeRow", "%AIWConversationFinalizeID")
        t.else_()
        checked_write(t, done_reply, "%cgz_write_ok")
        t.set("%AIWConversationExpectedStatus", "DONE")
        t.set("%AIWConversationExpectedReplyMode", "EXACT")
        t.set("%AIWConversationExpectedReply", "%AIWConversationReply")
        t.perform("AIW Conversation Member Verify", "%AIWConversationFinalizeRow", "%AIWConversationFinalizeID")
        t.endif()
        t.if_([("%AIWConversationMemberVerified", 2, "1")])
        t.perform("FINAL Archive One Bound Row", "%AIWConversationFinalizeRow", "%AIWConversationFinalizeID")
        t.if_([("%SSResult", 2, "ARCHIVE_DONE_VERIFIED")])
        t.set("%cgz_member_archived", "1")
        t.endif()
        t.endif()
        t.endif()
        t.if_([("%cgz_member_archived", 3, "1")])
        t.set("%cgz_done", "0")
        t.else_()
        t.set("%AIWConversationArchivedMask", "%AIWConversationArchivedMask,%AIWConversationFinalizeID")
        t.set("%AIWConversationTransitionFinalized", str(index))
        t.set("%AIWConversationTransitionError", "NONE")
        t.perform("AIW Conversation Ledger Transition", "GROUP_FINALIZING", "GROUP_FINALIZING")
        t.endif()
        t.endif()
    t.if_([("%cgz_done", 3, "1")])
    t.set("%AIWConversationFinalizeResult", "CONVERSATION_COMPANION_FINALIZE_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationTransitionFinalized", "%AIWConversationMemberCount")
    t.set("%AIWConversationTransitionArchive", "ALL_MEMBERS_ARCHIVED_VERIFIED")
    t.set("%AIWConversationTransitionError", "NONE")
    t.perform("AIW Conversation Ledger Transition", "GROUP_FINALIZING", "GROUP_COMPLETE")
    t.if_([("%AIWConversationTransitionResult", 3, "CONVERSATION_TRANSITION_VERIFIED")])
    t.set("%AIWConversationFinalizeResult", "CONVERSATION_COMPLETE_READBACK_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationFinalizeResult", "CONVERSATION_GROUP_COMPLETE")
    return t


def build_recovery() -> T:
    t = T()
    t.set("%AIWConversationRecoveryResult", "CONVERSATION_RECOVERY_START")
    t.perform("AIW Conversation Ledger Locate", "ACTIVE")
    t.if_([("%AIWConversationLocateResult", 2, "CONVERSATION_LEDGER_NOT_FOUND")])
    t.if_([("%AIWConversationOwner", 4, r"(?s).+"), ("%AIWConversationOwner", 5, r"^%.*$")], ["And"])
    t.set("%AIWConversationRecoveryResult", "CONVERSATION_ORPHAN_OWNER_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationRecoveryResult", "CONVERSATION_RECOVERY_NO_ACTIVE")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_FOUND")])
    t.set("%AIWConversationRecoveryResult", "%AIWConversationLocateResult")
    t.stop()
    t.endif()
    load_group_globals(t)
    t.if_([("%AIWConversationOwner", 4, r"(?s).+"), ("%AIWConversationOwner", 5, r"^%.*$")], ["And"])
    t.if_([("%AIWConversationOwner", 3, "%AICGL_Y")])
    t.set("%AIWConversationRecoveryResult", "CONVERSATION_OWNER_CONFLICT_HOLD")
    t.stop()
    t.endif()
    t.set("%cgr_age", "%TIMES-%AIWConversationOwnerStartedAt", maths=True)
    t.if_([("%cgr_age", 6, "120")])
    t.set("%AIWConversationRecoveryResult", "CONVERSATION_OWNER_NOT_STALE_HOLD")
    t.stop()
    t.endif()
    t.clear("%AIWConversationOwnerStartedAt")
    t.clear("%AIWConversationOwner")
    t.endif()
    t.if_([("%AIWConversationState", 4, r"^(GROUP_ANCHOR_ARCHIVED|GROUP_FINALIZING)$")])
    t.set("%PSMainRow", "%AIWConversationAnchorRow")
    t.set("%PSSelectedId", "%AIWConversationAnchorID")
    t.perform("AIW Conversation Finalize Companions", "RECOVERY")
    t.if_([("%AIWConversationFinalizeResult", 3, "CONVERSATION_GROUP_COMPLETE")])
    t.set("%AIWConversationRecoveryResult", "%AIWConversationFinalizeResult")
    t.stop()
    t.endif()
    t.set("%AIWConversationRecoveryResult", "CONVERSATION_RECOVERY_FINALIZED")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationState", 4, r"^(GROUP_BINDING|GROUP_PROCESSING)$")])
    t.set("%AIWConversationTransitionError", "RECOVERY_PARTIAL_STATE_REVIEW")
    t.perform("AIW Conversation Ledger Transition", "%AIWConversationState", "GROUP_REVIEW")
    t.set("%AIWConversationRecoveryResult", "CONVERSATION_PARTIAL_STATE_REVIEW_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationState", 2, "GROUP_REVIEW")])
    t.set("%AIWConversationRecoveryResult", "CONVERSATION_REVIEW_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationState", 4, r"^(GROUP_BOUND|GROUP_REPLY_READY|GROUP_SEND_AWAITING_CONFIRM|GROUP_SEND_OUTCOME_REVIEW)$")])
    t.set("%AIWConversationRecoveryResult", "CONVERSATION_RECOVERY_SAFE")
    t.else_()
    t.set("%AIWConversationRecoveryResult", "CONVERSATION_RECOVERY_STATE_HOLD")
    t.endif()
    return t


def build_schema(root: ET.Element) -> T:
    get_template, _ = fixture.plugin_templates(root)
    values = ["cgsc_version", "cgsc_result", "cgsc_physical", "cgsc_configured", "cgsc_archive", "cgsc_main", "cgsc_journal"]
    check = fixture.make_get(get_template, "ConversationSchemaCheck", "A2:G2", values)
    header_names = [f"cgsh_{c.lower()}" for c in COLS]
    header = fixture.make_get(get_template, "ConversationGroups", f"A1:{LAST_COL}1", header_names)
    t = T()
    t.set("%AIWConversationSchemaResult", "CONVERSATION_SCHEMA_START")
    t.set("%AIWConversationSchemaReady", "0")
    read_twice(t, check, values, "%cgsc_ok")
    t.if_([("%cgsc_ok", 3, "1")])
    t.set("%AIWConversationSchemaResult", "CONVERSATION_SCHEMA_PLUGIN_HOLD")
    t.stop()
    t.endif()
    t.set("%cgsc_valid", "1")
    expected = [("cgsc_version", SCHEMA_VERSION), ("cgsc_result", "PASS")]
    for name, value in expected:
        t.if_([(f"%{name}(#)", 3, "1"), (f"%{name}(1)", 3, value)], ["Or"])
        t.set("%cgsc_valid", "0")
        t.endif()
    for name in values[2:]:
        t.if_([(f"%{name}(#)", 3, "1"), (f"%{name}(1)", 5, r"^[0-9]+$")], ["Or"])
        t.set("%cgsc_valid", "0")
        t.endif()
    t.set("%AIWConversationGroupPhysicalMax", "%cgsc_physical(1)")
    t.set("%AIWConversationGroupMax", "%cgsc_configured(1)")
    t.set("%AIWConversationArchiveMax", "%cgsc_archive(1)")
    t.set("%AIWConversationMainMax", "%cgsc_main(1)")
    t.set("%AIWConversationJournalMax", "%cgsc_journal(1)")
    t.if_([("%AIWConversationGroupPhysicalMax", 6, "%AIWConversationGroupMax"), ("%AIWConversationGroupMax", 7, "1000")], ["Or"])
    t.set("%cgsc_valid", "0")
    t.endif()
    read_twice(t, header, header_names, "%cgsh_ok")
    t.if_([("%cgsh_ok", 3, "1")])
    t.set("%cgsc_valid", "0")
    t.endif()
    for name, expected_header in zip(header_names, HEADERS):
        t.if_([(f"%{name}(#)", 3, "1"), (f"%{name}(1)", 3, expected_header)], ["Or"])
        t.set("%cgsc_valid", "0")
        t.endif()
    t.if_([("%cgsc_valid", 2, "1")])
    t.set("%AIWConversationSchemaReady", "1")
    t.set("%AIWConversationSchemaResult", "CONVERSATION_SCHEMA_READY")
    t.else_()
    t.set("%AIWConversationSchemaResult", "CONVERSATION_SCHEMA_HOLD")
    t.endif()
    return t


def build_validation_audit(root: ET.Element) -> T:
    get_template, _ = fixture.plugin_templates(root)
    arrays = [f"cgv_{c.lower()}" for c in "ABCDEFGHIJKLMN"]
    journal = fixture.make_get(get_template, "IngressJournal", "A2:N%AIWConversationJournalMax", arrays)
    t = T()
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_START")
    t.set("%AIWConversationValidationReady", "0")
    require_schema(t, "%AIWConversationValidationResult")
    invalid(t, "%AIWConversationValidationContact", "%AIWConversationValidationResult", "CONVERSATION_VALIDATION_CONTACT_HOLD")
    invalid(t, "%AIWValidationRunID", "%AIWConversationValidationResult", "CONVERSATION_VALIDATION_RUN_HOLD")
    t.if_([("%par1", 2, "PRE")])
    read_twice(t, journal, arrays, "%cgv_ok")
    t.if_([("%cgv_ok", 3, "1")])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_JOURNAL_HOLD")
    t.stop()
    t.endif()
    t.set("%cgv_count", "0")
    t.set("%cgv_index", "0")
    t.for_("%cgv_id", "%cgv_b()")
    t.add_value("%cgv_index")
    t.set("%cgv_save_raw", "%PSSenderRaw")
    t.set("%cgv_save_ticker", "%PSTickerRaw")
    t.set("%PSSenderRaw", "%cgv_c(%cgv_index)")
    t.set("%PSTickerRaw", "%cgv_j(%cgv_index)")
    t.perform("PROCESS Normalize Sender")
    t.set("%cgv_key", "%PSSenderKey")
    t.set("%PSSenderRaw", "%cgv_save_raw")
    t.set("%PSTickerRaw", "%cgv_save_ticker")
    t.if_([("%cgv_key", 2, "%AIWConversationValidationContact"), ("%cgv_e(%cgv_index)", 2, "JOURNALED")], ["And"])
    t.add_value("%cgv_count")
    t.if_([("%cgv_count", 6, "4")])
    for index in range(1, 5):
        t.if_([("%cgv_count", 2, str(index))])
        t.set(f"%AIWPhase4JournalRow{index}", "%cgv_index+1", maths=True)
        t.set(f"%AIWPhase4EventID{index}", "%cgv_id")
        t.endif()
    t.endif()
    t.endif()
    t.endfor()
    t.if_([("%cgv_count", 6, "2"), ("%cgv_count", 7, "4")], ["Or"])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_EVENT_COUNT_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationValidationReady", "1")
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_PRE_READY")
    t.else_()
    t.set("%AIWConversationGroupID", "%AIWConversationValidationGroupID")
    t.perform("AIW Conversation Ledger Locate", "GROUP")
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_FOUND"), ("%AICGL_O", 3, "GROUP_COMPLETE"), ("%AICGL_AJ", 3, "%AIWValidationRunID"), ("%AICGL_AP", 3, "VALIDATION_CONVERSATION")], ["Or", "Or", "Or"])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_COMPLETE_HOLD")
    t.stop()
    t.endif()
    load_group_globals(t)
    t.set("%AIWConversationValidationGroupID", "%AIWConversationGroupID")
    t.set("%AIWConversationValidationLedgerRow", "%AIWConversationLedgerRow")
    t.if_([("%SSSentOne", 3, "1"), ("%AIWPhase4Confirmed", 3, "1"), ("%AIWPhase4Archived", 3, "1")], ["Or", "Or"])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_SEND_ARCHIVE_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationValidationReady", "1")
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_POST_PASS")
    t.endif()
    return t


def build_validation_cleanup(root: ET.Element) -> T:
    get_template, update_template = fixture.plugin_templates(root)
    archive_arrays = [f"cgvc_{c.lower()}" for c in "ABCDEFGHIJ"]
    archive_post_arrays = [f"cgvcp_{c.lower()}" for c in "ABCDEFGHIJ"]
    archive = fixture.make_get(get_template, "Archive", "A2:J%AIWConversationArchiveMax", archive_arrays)
    archive_post = fixture.make_get(get_template, "Archive", "A%AIWConversationValidationArchiveRow:J%AIWConversationValidationArchiveRow", archive_post_arrays)
    clear_archive = fixture.make_update(update_template, "Archive", "A%AIWConversationValidationArchiveRow", [""] * 10)
    clear_ledger = fixture.make_update(update_template, "ConversationGroups", "A%AIWConversationLedgerRow", [""] * len(COLS))
    t = T()
    t.set("%AIWConversationValidationCleanupResult", "CONVERSATION_VALIDATION_CLEANUP_START")
    t.set("%AIWConversationValidationCleanupVerified", "0")
    t.if_([("%AIWFixtureContractReady", 3, "1"), ("%AIWFXAuthState", 3, "ACTIVE"), ("%AIWFXAuthConsumedRun", 3, "%AIWValidationRunID")], ["Or", "Or"])
    t.set("%AIWConversationValidationCleanupResult", "CONVERSATION_VALIDATION_AUTH_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationLedgerRow", "%AIWConversationValidationLedgerRow")
    t.set("%AIWConversationGroupID", "%AIWConversationValidationGroupID")
    t.perform("AIW Conversation Ledger Read Exact")
    t.if_([("%AICGL_B", 3, "%AIWConversationGroupID"), ("%AICGL_O", 3, "GROUP_COMPLETE"), ("%AICGL_AJ", 3, "%AIWValidationRunID"), ("%AICGL_AP", 3, "VALIDATION_CONVERSATION")], ["Or", "Or", "Or"])
    t.set("%AIWConversationValidationCleanupResult", "CONVERSATION_VALIDATION_LEDGER_IDENTITY_HOLD")
    t.stop()
    t.endif()
    load_group_globals(t)
    read_twice(t, archive, archive_arrays, "%cgvc_ok")
    t.if_([("%cgvc_ok", 3, "1")])
    t.set("%AIWConversationValidationCleanupResult", "CONVERSATION_VALIDATION_ARCHIVE_READ_HOLD")
    t.stop()
    t.endif()
    for index in range(1, 5):
        t.if_([("%AIWConversationMemberCount", 6, str(index - 1))])
        t.set("%cgvc_matches", "0")
        t.set("%cgvc_index", "0")
        t.for_("%cgvc_id", "%cgvc_a()")
        t.add_value("%cgvc_index")
        t.if_([("%cgvc_id", 2, f"%AIWConversationMemberID{index}"), ("%cgvc_c(%cgvc_index)", 2, f"%AIWConversationMemberMessage{index}"), ("%cgvc_d(%cgvc_index)", 2, "DONE"), ("%cgvc_e(%cgvc_index)", 2, "%AIWConversationReply")], ["And", "And", "And"])
        t.add_value("%cgvc_matches")
        t.set("%AIWConversationValidationArchiveRow", "%cgvc_index+1", maths=True)
        t.endif()
        t.endfor()
        t.if_([("%cgvc_matches", 3, "1")])
        t.set("%AIWConversationValidationCleanupResult", "CONVERSATION_VALIDATION_ARCHIVE_IDENTITY_HOLD")
        t.stop()
        t.endif()
        checked_write(t, clear_archive, "%cgvc_write_ok")
        read_twice(t, archive_post, archive_post_arrays, "%cgvcp_ok")
        t.if_([("%cgvcp_ok", 3, "1")])
        t.set("%AIWConversationValidationCleanupResult", "CONVERSATION_VALIDATION_ARCHIVE_CLEAR_READ_HOLD")
        t.stop()
        t.endif()
        for post_name in archive_post_arrays:
            t.set("%cgvcp_value", f"%{post_name}(1)")
            t.if_([("%cgvcp_value", 5, rf"(?s)^\s*$|^%{post_name}(?:\(1\)|[0-9]*)$")])
            t.set("%AIWConversationValidationCleanupResult", "CONVERSATION_VALIDATION_ARCHIVE_CLEAR_HOLD")
            t.stop()
            t.endif()
        t.endif()
    checked_write(t, clear_ledger, "%cgvc_ledger_write_ok")
    t.perform("AIW Conversation Ledger Read Exact")
    t.if_([("%AIWConversationLedgerBlank", 3, "1")])
    t.set("%AIWConversationValidationCleanupResult", "CONVERSATION_VALIDATION_LEDGER_CLEAR_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationValidationCleanupVerified", "1")
    t.set("%AIWConversationValidationCleanupResult", "CONVERSATION_VALIDATION_CLEANUP_VERIFIED")
    return t


def patch_task282(raw: str) -> str:
    t = T()
    t.set("%AIWProcessOneResult", "PROCESS_ONE_START")
    t.perform("PROCESS Queue Health")
    t.perform("PROCESS Load Queue Globals")
    t.perform("PROCESS Select Candidate Row")
    t.if_([("%PSProcessThisRow", 3, "1")])
    t.set("%AIWProcessOneResult", "NO_NEW_ROWS")
    t.stop()
    t.endif()
    t.perform("PROCESS Live Row Guard")
    t.if_([("%PSLiveGuardPass", 3, "1")])
    t.set("%AIWProcessOneResult", "LIVE_ROW_GUARD_HOLD")
    t.stop()
    t.endif()
    t.perform("PROCESS Normalize Sender")
    t.set("%AIWConversationSenderKey", "%PSSenderKey")
    t.perform("AIW Conversation Prepare Group")
    t.if_([("%AIWConversationPrepareResult", 5, r"^(CONVERSATION_SINGLE_READY|GROUP_BOUND_READY|GROUP_BOUND_RESUMED)$")])
    t.set("%AIWProcessOneResult", "%AIWConversationPrepareResult")
    t.stop()
    t.endif()
    t.perform("PROCESS Validate Work Unit")
    t.if_([("%PSValidWork", 3, "1")])
    t.set("%AIWProcessOneResult", "WORK_UNIT_HOLD")
    t.stop()
    t.endif()
    t.perform("PROCESS Exact Row Transaction", "MARK_PROCESSING")
    t.if_([("%PSTxnVerified", 3, "1")])
    t.set("%AIWProcessOneResult", "%PSTxnResult")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationActive", 2, "1")])
    t.set("%AIWConversationTransitionError", "NONE")
    t.perform("AIW Conversation Ledger Transition", "GROUP_BOUND", "GROUP_PROCESSING")
    t.if_([("%AIWConversationTransitionResult", 3, "CONVERSATION_TRANSITION_VERIFIED")])
    t.set("%AIWProcessOneResult", "CONVERSATION_PROCESSING_STATE_HOLD")
    t.stop()
    t.endif()
    t.endif()
    t.perform("AIW Conversation Prompt Build")
    t.if_([("%PSBuildPromptOk", 3, "1")])
    t.set("%PSFailureStatus", "ERROR_OPENAI_RETRY")
    t.perform("PROCESS Exact Row Transaction", "COMMIT_FAILURE")
    t.if_([("%AIWConversationActive", 2, "1")])
    t.set("%AIWConversationTransitionError", "%AIWConversationPromptResult")
    t.perform("AIW Conversation Ledger Transition", "GROUP_PROCESSING", "GROUP_REVIEW")
    t.endif()
    t.set("%AIWProcessOneResult", "%AIWConversationPromptResult")
    t.stop()
    t.endif()
    t.perform("PROCESS OpenAI Bounded Retry")
    t.if_([("%PSHttpSuccess", 2, "1")])
    t.perform("PROCESS Parse Reply")
    t.set("%PSFinalStatus", "READY_TO_SEND")
    t.perform("PROCESS Exact Row Transaction", "COMMIT_SUCCESS")
    t.if_([("%PSTxnVerified", 2, "1")])
    t.set("%AIWProcessOneResult", "PROCESS_READY_TO_SEND_VERIFIED")
    t.if_([("%AIWConversationActive", 2, "1")])
    t.set("%AIWConversationTransitionReply", "%PSReply")
    t.set("%AIWConversationTransitionError", "NONE")
    t.perform("AIW Conversation Ledger Transition", "GROUP_PROCESSING", "GROUP_REPLY_READY")
    t.if_([("%AIWConversationTransitionResult", 3, "CONVERSATION_TRANSITION_VERIFIED")])
    t.set("%AIWProcessOneResult", "CONVERSATION_REPLY_LEDGER_HOLD")
    t.endif()
    t.endif()
    t.else_()
    t.set("%AIWProcessOneResult", "%PSTxnResult")
    t.endif()
    t.else_()
    t.set("%PSFailureStatus", "ERROR_OPENAI_RETRY")
    t.perform("PROCESS Exact Row Transaction", "COMMIT_FAILURE")
    t.if_([("%AIWConversationActive", 2, "1")])
    t.set("%AIWConversationTransitionError", "%PSApiOutcomeClass")
    t.perform("AIW Conversation Ledger Transition", "GROUP_PROCESSING", "GROUP_REVIEW")
    t.endif()
    t.set("%AIWProcessOneResult", "%PSApiOutcomeClass")
    t.endif()
    return fixture.replace_actions(raw, t.actions)


def patch_task262(raw: str) -> str:
    t = T()
    t.set("%AIWProtectedSendResult", "SEND_WRAPPER_START")
    t.set("%AIWProtectedSendClicked", "0")
    t.perform("AIW Conversation Pre Send Guard")
    t.if_([("%AIWConversationPreSendResult", 2, "CONVERSATION_GROUP_LIFECYCLE_ONLY")])
    t.perform("FINAL Queue Lifecycle Router")
    t.if_([("%SSResult", 2, "ARCHIVE_DONE_VERIFIED")])
    t.perform("AIW Conversation Finalize Companions", "ROUTER")
    t.endif()
    t.set("%AIWProtectedSendResult", "%SSResult")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationPreSendResult", 5, r"^(CONVERSATION_SINGLE_SEND_READY|CONVERSATION_GROUP_SEND_READY)$")])
    t.set("%AIWProtectedSendResult", "%AIWConversationPreSendResult")
    t.stop()
    t.endif()
    t.perform("FINAL Send Sheet")
    t.if_([("%SSSentOne", 2, "1")])
    t.set("%AIWProtectedSendClicked", "1")
    t.set("%AIWProtectedSendResult", "SEND_CLICKED_AWAITING_CONFIRM")
    t.perform("AIW Conversation Send State", "%SSResult")
    t.perform("FINAL Queue Lifecycle Router")
    t.if_([("%AIWValidationRealSendAuthorized", 2, "1"), ("%SSResult", 2, "ARCHIVE_DONE_VERIFIED")], ["And"])
    t.set("%AIWPhase4Confirmed", "1")
    t.set("%AIWPhase4Archived", "1")
    t.endif()
    t.if_([("%SSResult", 2, "ARCHIVE_DONE_VERIFIED")])
    t.perform("AIW Conversation Finalize Companions", "ROUTER")
    t.endif()
    t.stop()
    t.endif()
    t.if_([("%SSResult", 4, r"SEND_CLICKED_AWAITING_CONFIRM|SENT_REVIEW_REQUIRED")])
    t.set("%AIWProtectedSendClicked", "1")
    t.set("%AIWProtectedSendResult", "%SSResult")
    t.perform("AIW Conversation Send State", "%SSResult")
    t.perform("FINAL Queue Lifecycle Router")
    t.if_([("%AIWValidationRealSendAuthorized", 2, "1"), ("%SSResult", 2, "ARCHIVE_DONE_VERIFIED")], ["And"])
    t.set("%AIWPhase4Confirmed", "1")
    t.set("%AIWPhase4Archived", "1")
    t.endif()
    t.if_([("%SSResult", 2, "ARCHIVE_DONE_VERIFIED")])
    t.perform("AIW Conversation Finalize Companions", "ROUTER")
    t.endif()
    t.stop()
    t.endif()
    t.set("%AIWProtectedSendResult", "%SSResult")
    return fixture.replace_actions(raw, t.actions)


def patch_task273(raw: str) -> str:
    t = T()
    t.set("%AIWValidationPhaseResult", "PHASE4_CONVERSATION_START")
    t.if_([("%AIWConversationValidationHistoryID", 4, r"(?s)^\s*$|^%.*$|(?is).*#ERROR.*"), ("%AIWConversationValidationHistoryID", 3, "%AIWFXHistArchiveID")], ["Or"])
    t.set("%AIWValidationPhaseResult", "PHASE4_HISTORY_FIXTURE_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWValidationRealSendAuthorized", "1")
    t.set("%AIWStopRequested", "0")
    t.set("%AIWorkerOn", "1")
    fixture.add_profile_state(t, "FINAL TextNow Trigger", True)
    t.add('<code>550</code><Str sr="arg0" ve="3">AIW PHASE 4</Str><Str sr="arg1" ve="3">SEND 2 TO 4 RAPID TEST MESSAGES FROM THE APPROVED CONTACT. ONE SEND MAXIMUM.</Str><Int sr="arg2" val="1" /><Str sr="arg3" ve="3">Popup</Str>')
    t.wait(45)
    t.perform("AIW Conversation Validation Audit", "PRE")
    t.if_([("%AIWConversationValidationReady", 3, "1")])
    t.set("%AIWValidationPhaseResult", "%AIWConversationValidationResult")
    t.stop()
    t.endif()
    t.wait(10)
    t.perform("AIW Integrated Queue Cycle")
    t.set("%AIWValidationRealSendAuthorized", "0")
    t.perform("APP Stop AI Worker")
    t.perform("AIW Conversation Validation Audit", "POST")
    t.if_([("%AIWConversationValidationReady", 3, "1")])
    t.set("%AIWValidationPhaseResult", "%AIWConversationValidationResult")
    t.stop()
    t.endif()
    t.set("%AIWValidationPhaseResult", "PHASE4_PASS")
    t.perform("AIW Proof Ledger Append", "PHASE4", "PHASE4_CONVERSATION_PASS")
    t.if_([("%AIWProofWriteVerified", 3, "1")])
    t.set("%AIWValidationPhaseResult", "PHASE4_PROOF_HOLD")
    t.endif()
    return fixture.replace_actions(raw, t.actions)


def patch_task276(raw: str) -> str:
    actions = fixture.action_list(raw)
    insert = T()
    for index in range(1, 5):
        insert.if_([(f"%AIWPhase4JournalRow{index}", 4, r"^[0-9]+$")])
        insert.perform("AIW Validation Cleanup Exact Row", "JOURNAL", f"%AIWPhase4JournalRow{index}")
        insert.if_([("%AIWValidationCleanupVerified", 3, "1")])
        insert.set("%AIWValidationPhaseResult", f"PHASE7_CONVERSATION_JOURNAL_{index}_HOLD")
        insert.stop()
        insert.endif()
        insert.endif()
    insert.perform("AIW Conversation Validation Cleanup")
    insert.if_([("%AIWConversationValidationCleanupVerified", 3, "1")])
    insert.set("%AIWValidationPhaseResult", "%AIWConversationValidationCleanupResult")
    insert.stop()
    insert.endif()
    # Before the control cleanup and proof/authorization close.
    actions[122:122] = insert.actions
    return fixture.replace_actions(raw, actions)


def patch_task278(raw: str) -> str:
    actions = fixture.action_list(raw)
    gate = T()
    gate.perform("AIW Conversation Recovery")
    gate.if_([("%AIWConversationRecoveryResult", 5, r"^(CONVERSATION_RECOVERY_NO_ACTIVE|CONVERSATION_RECOVERY_SAFE|CONVERSATION_RECOVERY_FINALIZED)$")])
    gate.set("%AIWRecoveryResult", "%AIWConversationRecoveryResult")
    gate.stop()
    gate.endif()
    actions[225:225] = gate.actions
    return fixture.replace_actions(raw, actions)


def patch_task284(raw: str) -> str:
    actions = fixture.action_list(raw)
    gate = T()
    gate.perform("AIW Conversation Schema Check")
    gate.if_([("%AIWConversationSchemaResult", 3, "CONVERSATION_SCHEMA_READY")])
    gate.set("%sc_ok", "0")
    gate.endif()
    actions[109:109] = gate.actions
    return fixture.replace_actions(raw, actions)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    base = args.base.read_bytes()
    if sha256(base) != EXPECTED_BASE_SHA:
        raise RuntimeError(f"Authorized base SHA mismatch: {sha256(base)}")
    if base.startswith(b"\xef\xbb\xbf"):
        raise RuntimeError("Authorized base unexpectedly has a UTF-8 BOM")
    text = base.decode("utf-8")
    root = ET.fromstring(base)
    source = fixture.raw_tasks(text)
    get_template, update_template = fixture.plugin_templates(root)
    if get_template.findtext("code") != "1810865467" or update_template.findtext("code") != "1461810131":
        raise RuntimeError("Source-proven AutoSheets templates unavailable")
    builders = {
        309: build_quiet_select(root), 310: build_owner(), 311: build_ledger_read(root),
        312: build_ledger_locate(root), 313: build_ledger_create(root), 314: build_member_verify(root),
        315: build_member_bind(root), 316: build_ledger_transition(root), 317: build_prepare_group(),
        318: build_history(root), 319: build_prompt(), 320: build_pre_send(root),
        321: build_send_state(), 322: build_finalize(root), 323: build_recovery(),
        324: build_schema(root), 325: build_validation_audit(root), 326: build_validation_cleanup(root),
    }
    for task_id, builder in builders.items():
        if len(builder.actions) >= 500:
            raise RuntimeError(f"Helper {task_id} exceeds 499 actions: {len(builder.actions)}")
    replacements = {
        262: patch_task262(source[262]), 273: patch_task273(source[273]),
        276: patch_task276(source[276]), 278: patch_task278(source[278]),
        282: patch_task282(source[282]), 284: patch_task284(source[284]),
    }
    for task_id, node in replacements.items():
        text, count = re.subn(rf'<Task sr="task{task_id}".*?</Task>', lambda _: node, text, count=1, flags=re.DOTALL)
        if count != 1:
            raise RuntimeError(f"Task {task_id} replacement count {count}")
    nodes = {task_id: fixture.task_xml(task_id, HELPERS[task_id], builders[task_id]) for task_id in HELPERS}
    text = fixture.insert_helpers_and_registry(text, nodes)
    output = text.encode("utf-8")
    ET.fromstring(output)
    final = fixture.raw_tasks(text)
    changed = sorted(task_id for task_id in source if source[task_id] != final.get(task_id))
    added = sorted(set(final) - set(source))
    if changed != sorted(AUTHORIZED_EXISTING):
        raise RuntimeError(f"Unauthorized existing-task change: {changed}")
    if added != sorted(HELPERS):
        raise RuntimeError(f"Unexpected helper set: {added}")
    for task_id in set(source) - AUTHORIZED_EXISTING:
        if source[task_id] != final[task_id]:
            raise RuntimeError(f"Task {task_id} changed outside authorization")
    for task_id in PROTECTED_PHONE_TASKS | LEGACY_UNREACHABLE:
        if source[task_id] != final[task_id]:
            raise RuntimeError(f"Protected task {task_id} changed")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(output)
    print(f"BASE_SHA256={sha256(base)}")
    print(f"OUTPUT_SHA256={sha256(output)}")
    print(f"OUTPUT_BYTES={len(output)}")
    print(f"CHANGED_EXISTING={changed}")
    print(f"ADDED_HELPERS={added}")
    for task_id in sorted(builders):
        print(f"HELPER={task_id}|{HELPERS[task_id]}|ACTIONS={len(builders[task_id].actions)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"BUILD_FAILED={type(exc).__name__}:{exc}", file=sys.stderr)
        raise
