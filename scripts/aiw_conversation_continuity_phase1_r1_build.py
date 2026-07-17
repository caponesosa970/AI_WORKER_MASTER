from __future__ import annotations

import argparse
import hashlib
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import aiw_conversation_continuity_phase1_build as p1
import aiw_final_fixture_safety_repair as fixture


EXPECTED_BASE_SHA = "D69480C9A212430D5D46753E3A05CBF4DB52045A6A8F967605BD3A3631CAB66E"
AUTHORIZED_EXISTING = {263, 273, 282, 309, 317, 320, 324, 325}
ADDED_HELPERS = {327: "AIW Conversation Deferred Recheck"}
PHONE_PROVEN = {71, 199, 223, 225, 226, 227, 230, 231}
JOURNAL_RESOLUTION = {254, 255}
PRESERVED_CONVERSATION = ({262, 276, 278, 284} | set(range(310, 317)) |
                          set(range(318, 324)) | {326}) - AUTHORIZED_EXISTING
PRESERVED_FIXTURE = {268, 293} | set(range(295, 309))
T = fixture.TaskBuilder


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def journal_member_contract(t: T, index: int, prefix: str) -> None:
    """Count all ID records and exactly valid admitted records for one selected member."""
    t.if_([
        ("%AIWConversationMemberCount", 6, str(index - 1)),
        (f"%{prefix}_jid", 2, f"%AIWConversationMemberID{index}"),
    ], ["And"])
    t.add_value(f"%{prefix}_idmatch{index}")
    t.set(f"%{prefix}_save_raw", "%PSSenderRaw")
    t.set(f"%{prefix}_save_ticker", "%PSTickerRaw")
    t.set("%PSSenderRaw", f"%{prefix}_c(%{prefix}_jindex)")
    t.set("%PSTickerRaw", f"%{prefix}_j(%{prefix}_jindex)")
    t.perform("PROCESS Normalize Sender")
    t.set(f"%{prefix}_jkey", "%PSSenderKey")
    t.set("%PSSenderRaw", f"%{prefix}_save_raw")
    t.set("%PSTickerRaw", f"%{prefix}_save_ticker")
    t.if_([
        (f"%{prefix}_e(%{prefix}_jindex)", 4, r"^(RESOLVED_MAIN|RESOLVED_OVERFLOW)$"),
        (f"%{prefix}_l(%{prefix}_jindex)", 2, "TEXTNOW"),
        (f"%{prefix}_c(%{prefix}_jindex)", 2, f"%AIWConversationMemberSender{index}"),
        (f"%{prefix}_d(%{prefix}_jindex)", 2, f"%AIWConversationMemberMessage{index}"),
        (f"%{prefix}_jkey", 2, "%AIWConversationSenderKey"),
        (f"%{prefix}_k(%{prefix}_jindex)", 5, r"^[0-9]{10,16}$"),
    ], ["And", "And", "And", "And", "And"])
    t.add_value(f"%{prefix}_valid{index}")
    t.set(f"%AIWConversationMemberLoggedAt{index}", f"%{prefix}_k(%{prefix}_jindex)")
    t.endif()
    t.endif()


def build_quiet_select(root: ET.Element) -> T:
    get_template, _ = fixture.plugin_templates(root)
    arrays = [f"cgq_{c.lower()}" for c in "ABCDEFGHIJKLMN"]
    journal = fixture.make_get(get_template, "IngressJournal", "A2:N%AIWConversationJournalMax", arrays)
    t = T()
    t.set("%AIWConversationQuietResult", "CONVERSATION_QUIET_START")
    t.set("%AIWConversationMemberCount", "0")
    t.set("%AIWConversationExcessCount", "0")
    p1.require_schema(t, "%AIWConversationQuietResult")
    p1.invalid(t, "%PSSenderKey", "%AIWConversationQuietResult", "CONVERSATION_SENDER_HOLD")
    for index in range(1, 5):
        for suffix in ("Row", "ID", "Sender", "Message", "LoggedAt"):
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
        t.set(f"%AIWConversationMemberSender{index}", "%PSQSender(%cgq_index)")
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
    p1.read_twice(t, journal, arrays, "%cgq_journal_ok")
    t.if_([("%cgq_journal_ok", 3, "1")])
    t.set("%AIWConversationQuietResult", "CONVERSATION_JOURNAL_READ_HOLD")
    t.stop()
    t.endif()
    for index in range(1, 5):
        t.set(f"%cgq_idmatch{index}", "0")
        t.set(f"%cgq_valid{index}", "0")
    t.set("%cgq_jindex", "0")
    t.for_("%cgq_jid", "%cgq_b()")
    t.add_value("%cgq_jindex")
    for index in range(1, 5):
        journal_member_contract(t, index, "cgq")
    t.endfor()
    t.set("%AIWConversationNewestLoggedAt", "0")
    for index in range(1, 5):
        t.if_([("%AIWConversationMemberCount", 6, str(index - 1))])
        t.if_([
            (f"%cgq_idmatch{index}", 3, "1"),
            (f"%cgq_valid{index}", 3, "1"),
            (f"%AIWConversationMemberLoggedAt{index}", 5, r"^[0-9]{10,16}$"),
        ], ["Or", "Or"])
        t.set("%AIWConversationQuietResult", "CONVERSATION_JOURNAL_IDENTITY_HOLD")
        t.stop()
        t.endif()
        t.if_([(f"%AIWConversationMemberLoggedAt{index}", 7, "%AIWConversationNewestLoggedAt")])
        t.set("%AIWConversationNewestLoggedAt", f"%AIWConversationMemberLoggedAt{index}")
        t.endif()
        t.endif()
    t.set("%AIWConversationQuietCutoff", "%AIWConversationNewestLoggedAt+10000", maths=True)
    t.if_([("%TIMEMS", 6, "%AIWConversationQuietCutoff")])
    t.set("%AIWConversationQuietRecheckCutoff", "%AIWConversationQuietCutoff")
    t.set("%AIWConversationQuietRecheckSender", "%AIWConversationSenderKey")
    t.set("%AIWConversationQuietResult", "CONVERSATION_QUIET_WAIT_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationQuietResult", "CONVERSATION_QUIET_READY")
    return t


def active_gate_result(t: T) -> None:
    p1.load_group_globals(t)
    t.if_([("%AIWConversationState", 4, r"^(GROUP_REPLY_READY|GROUP_SEND_AWAITING_CONFIRM|GROUP_SEND_OUTCOME_REVIEW|GROUP_ANCHOR_ARCHIVED|GROUP_FINALIZING)$")])
    t.set("%AIWConversationPrepareResult", "CONVERSATION_GROUP_LIFECYCLE_ONLY")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationState", 2, "GROUP_REVIEW")])
    t.set("%AIWConversationPrepareResult", "CONVERSATION_GROUP_REVIEW_ONLY")
    t.stop()
    t.endif()
    t.set("%AIWConversationPrepareResult", "CONVERSATION_ACTIVE_GROUP_RECOVERY_HOLD")
    t.stop()


def build_prepare_group() -> T:
    t = T()
    t.set("%AIWConversationPrepareResult", "CONVERSATION_PREPARE_START")
    t.if_([("%par1", 2, "LIFECYCLE_GATE")])
    t.perform("AIW Conversation Ledger Locate", "ACTIVE")
    t.if_([("%AIWConversationLocateResult", 2, "CONVERSATION_LEDGER_NOT_FOUND")])
    t.set("%AIWConversationPrepareResult", "CONVERSATION_NO_ACTIVE_GROUP")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_FOUND")])
    t.set("%AIWConversationPrepareResult", "%AIWConversationLocateResult")
    t.stop()
    t.endif()
    active_gate_result(t)
    t.endif()
    t.set("%AIWConversationActive", "0")
    t.set("%AIWConversationSenderKey", "%PSSenderKey")
    t.perform("AIW Conversation Ledger Locate", "ANCHOR")
    t.if_([("%AIWConversationLocateResult", 2, "CONVERSATION_LEDGER_FOUND")])
    p1.load_group_globals(t)
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
    active_gate_result(t)
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
    p1.add_random(t, "%cgp_r1")
    p1.add_random(t, "%cgp_r2")
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


def normalize_to(t: T, raw: str, ticker: str, target: str, prefix: str) -> None:
    t.set(f"%{prefix}_save_raw", "%PSSenderRaw")
    t.set(f"%{prefix}_save_ticker", "%PSTickerRaw")
    t.set("%PSSenderRaw", raw)
    t.set("%PSTickerRaw", ticker)
    t.perform("PROCESS Normalize Sender")
    t.set(target, "%PSSenderKey")
    t.set("%PSSenderRaw", f"%{prefix}_save_raw")
    t.set("%PSTickerRaw", f"%{prefix}_save_ticker")


def set_member_flag(t: T, candidate_id: str, flag: str) -> None:
    t.set(flag, "0")
    for index in range(1, 5):
        t.if_([(candidate_id, 2, f"%AIWConversationMemberID{index}")])
        t.set(flag, "1")
        t.endif()


def scan_active_contract(
    t: T,
    *,
    candidate_id: str,
    sender: str,
    message: str,
    ticker: str,
    required_status: str,
    prefix: str,
) -> None:
    normalize_to(t, sender, ticker, f"%{prefix}_active_key", f"{prefix}_active")
    t.if_([(f"%{prefix}_active_key", 2, "%AIWConversationSenderKey")])
    set_member_flag(t, candidate_id, f"%{prefix}_member")
    t.if_([(f"%{prefix}_member", 2, "0")])
    t.set(f"%{prefix}_idmatches", "0")
    t.set(f"%{prefix}_valid", "0")
    t.set(f"%{prefix}_loggedat", "")
    t.set(f"%{prefix}_jindex", "0")
    t.for_(f"%{prefix}_jid", "%cgf_b()")
    t.add_value(f"%{prefix}_jindex")
    t.if_([(f"%{prefix}_jid", 2, candidate_id)])
    t.add_value(f"%{prefix}_idmatches")
    normalize_to(t, f"%cgf_c(%{prefix}_jindex)", f"%cgf_j(%{prefix}_jindex)", f"%{prefix}_jkey", f"{prefix}_j")
    t.if_([
        (f"%cgf_e(%{prefix}_jindex)", 4, required_status),
        (f"%cgf_l(%{prefix}_jindex)", 2, "TEXTNOW"),
        (f"%cgf_c(%{prefix}_jindex)", 2, sender),
        (f"%cgf_d(%{prefix}_jindex)", 2, message),
        (f"%{prefix}_jkey", 2, "%AIWConversationSenderKey"),
        (f"%cgf_k(%{prefix}_jindex)", 5, r"^[0-9]{10,16}$"),
    ], ["And", "And", "And", "And", "And"])
    t.add_value(f"%{prefix}_valid")
    t.set(f"%{prefix}_loggedat", f"%cgf_k(%{prefix}_jindex)")
    t.endif()
    t.endif()
    t.endfor()
    t.if_([(f"%{prefix}_idmatches", 3, "1"), (f"%{prefix}_valid", 3, "1")], ["Or"])
    t.set("%cgf_contract_hold", "1")
    t.else_()
    t.if_([(f"%{prefix}_loggedat", 6, "%AIWConversationBoundAt")])
    t.set("%cgf_stale", "1")
    t.endif()
    t.endif()
    t.endif()
    t.endif()


def build_pre_send(root: ET.Element) -> T:
    get_template, _ = fixture.plugin_templates(root)
    journal_arrays = [f"cgf_{c.lower()}" for c in "ABCDEFGHIJKLMN"]
    overflow_arrays = [f"cgfo_{c.lower()}" for c in "ABCDEFGHIJKLMN"]
    journal = fixture.make_get(get_template, "IngressJournal", "A2:N%AIWConversationJournalMax", journal_arrays)
    overflow = fixture.make_get(get_template, "OverflowInbox", "A2:N986", overflow_arrays)
    t = T()
    t.set("%AIWConversationPreSendResult", "CONVERSATION_PRE_SEND_START")
    t.perform("AIW Conversation Ledger Locate", "ANCHOR")
    t.if_([("%AIWConversationLocateResult", 2, "CONVERSATION_LEDGER_NOT_FOUND")])
    t.perform("AIW Conversation Ledger Locate", "ACTIVE")
    t.if_([("%AIWConversationLocateResult", 2, "CONVERSATION_LEDGER_FOUND")])
    p1.load_group_globals(t)
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
    p1.load_group_globals(t)
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
    t.perform("PROCESS Queue Health")
    t.perform("PROCESS Load Queue Globals")
    p1.read_twice(t, journal, journal_arrays, "%cgf_journal_ok")
    t.if_([("%cgf_journal_ok", 3, "1")])
    t.set("%AIWConversationPreSendResult", "CONVERSATION_FRESHNESS_JOURNAL_HOLD")
    t.stop()
    t.endif()
    p1.read_twice(t, overflow, overflow_arrays, "%cgfo_ok")
    t.if_([("%cgfo_ok", 3, "1")])
    t.set("%AIWConversationPreSendResult", "CONVERSATION_FRESHNESS_OVERFLOW_HOLD")
    t.stop()
    t.endif()
    t.set("%cgf_stale", "0")
    t.set("%cgf_contract_hold", "0")
    # Unresolved journal events are authoritative before admission and have no Sheet1/Overflow row yet.
    t.set("%cgf_unresolved_index", "0")
    t.for_("%cgf_unresolved_id", "%cgf_b()")
    t.add_value("%cgf_unresolved_index")
    t.if_([("%cgf_e(%cgf_unresolved_index)", 2, "JOURNALED"), ("%cgf_l(%cgf_unresolved_index)", 2, "TEXTNOW"), ("%cgf_k(%cgf_unresolved_index)", 5, r"^[0-9]{10,16}$")], ["And", "And"])
    normalize_to(t, "%cgf_c(%cgf_unresolved_index)", "%cgf_j(%cgf_unresolved_index)", "%cgf_unresolved_key", "cgf_unresolved")
    t.if_([("%cgf_unresolved_key", 2, "%AIWConversationSenderKey")])
    set_member_flag(t, "%cgf_unresolved_id", "%cgf_unresolved_member")
    t.if_([("%cgf_unresolved_member", 2, "0"), ("%cgf_k(%cgf_unresolved_index)", 6, "%AIWConversationBoundAt")], ["And"])
    t.set("%cgf_stale", "1")
    t.endif()
    t.endif()
    t.endif()
    t.endfor()
    # Active Sheet1 candidates must have exactly one admitted journal contract.
    t.set("%cgf_qindex", "0")
    t.for_("%cgf_qstatus", "%PSQStatus()")
    t.add_value("%cgf_qindex")
    t.if_([("%cgf_qstatus", 2, "NEW")])
    scan_active_contract(
        t,
        candidate_id="%PSQId(%cgf_qindex)",
        sender="%PSQSender(%cgf_qindex)",
        message="%PSQMessage(%cgf_qindex)",
        ticker="%PSQTicker(%cgf_qindex)",
        required_status=r"^(RESOLVED_MAIN|RESOLVED_OVERFLOW)$",
        prefix="cgfq",
    )
    t.endif()
    t.endfor()
    # Active Overflow rows are authoritative only with RESOLVED_OVERFLOW.
    t.set("%cgfo_index", "0")
    t.for_("%cgfo_status", "%cgfo_e()")
    t.add_value("%cgfo_index")
    t.if_([("%cgfo_status", 4, r"^(PENDING|DRAINING|MAIN_COMMITTED|OVERFLOW_REVIEW)$")])
    scan_active_contract(
        t,
        candidate_id="%cgfo_b(%cgfo_index)",
        sender="%cgfo_c(%cgfo_index)",
        message="%cgfo_d(%cgfo_index)",
        ticker="%cgfo_j(%cgfo_index)",
        required_status=r"^RESOLVED_OVERFLOW$",
        prefix="cgfoa",
    )
    t.endif()
    t.endfor()
    t.if_([("%cgf_contract_hold", 2, "1")])
    t.set("%AIWConversationTransitionError", "PRE_SEND_JOURNAL_CONTRACT_REVIEW")
    t.perform("AIW Conversation Ledger Transition", "GROUP_REPLY_READY", "GROUP_REVIEW")
    t.set("%AIWConversationPreSendResult", "CONVERSATION_PRE_SEND_JOURNAL_CONTRACT_HOLD")
    t.stop()
    t.endif()
    t.if_([("%cgf_stale", 2, "1")])
    t.set("%AIWConversationTransitionError", "PRE_SEND_MEMBERSHIP_STALE_REVIEW")
    t.perform("AIW Conversation Ledger Transition", "GROUP_REPLY_READY", "GROUP_REVIEW")
    t.set("%AIWConversationPreSendResult", "CONVERSATION_PRE_SEND_STALE_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationPreSendResult", "CONVERSATION_GROUP_SEND_READY")
    return t


def build_schema(root: ET.Element) -> T:
    get_template, _ = fixture.plugin_templates(root)
    values = ["cgsc_version", "cgsc_result", "cgsc_physical", "cgsc_configured", "cgsc_archive", "cgsc_main", "cgsc_journal"]
    check = fixture.make_get(get_template, "ConversationSchemaCheck", "A2:G2", values)
    header_names = [f"cgsh_{c.lower()}" for c in p1.COLS]
    header = fixture.make_get(get_template, "ConversationGroups", f"A1:{p1.LAST_COL}1", header_names)
    slot = fixture.make_get(get_template, "ConversationGroupSlotView", "A2:A2", ["cgss_slot"])
    t = T()
    t.set("%AIWConversationSchemaResult", "CONVERSATION_SCHEMA_START")
    t.set("%AIWConversationSchemaReady", "0")
    p1.read_twice(t, check, values, "%cgsc_ok")
    t.if_([("%cgsc_ok", 3, "1")])
    t.set("%AIWConversationSchemaResult", "CONVERSATION_SCHEMA_PLUGIN_HOLD")
    t.stop()
    t.endif()
    t.set("%cgsc_valid", "1")
    for name, value in [("cgsc_version", p1.SCHEMA_VERSION), ("cgsc_result", "PASS")]:
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
    t.if_([("%AIWConversationGroupPhysicalMax", 6, "%AIWConversationGroupMax"), ("%AIWConversationGroupMax", 7, "1000"), ("%AIWConversationGroupMax", 6, "2")], ["Or", "Or"])
    t.set("%cgsc_valid", "0")
    t.endif()
    p1.read_twice(t, header, header_names, "%cgsh_ok")
    t.if_([("%cgsh_ok", 3, "1")])
    t.set("%cgsc_valid", "0")
    t.endif()
    for name, expected in zip(header_names, p1.HEADERS):
        t.if_([(f"%{name}(#)", 3, "1"), (f"%{name}(1)", 3, expected)], ["Or"])
        t.set("%cgsc_valid", "0")
        t.endif()
    p1.read_twice(t, slot, ["cgss_slot"], "%cgss_ok")
    t.if_([("%cgss_ok", 3, "1"), ("%cgss_slot(#)", 3, "1")], ["Or"])
    t.set("%cgsc_valid", "0")
    t.else_()
    t.if_([("%cgss_slot(1)", 3, "FULL"), ("%cgss_slot(1)", 5, r"^[0-9]+$")], ["And"])
    t.set("%cgsc_valid", "0")
    t.endif()
    t.endif()
    t.if_([("%cgsc_valid", 2, "1")])
    t.set("%AIWConversationSchemaReady", "1")
    t.set("%AIWConversationSchemaResult", "CONVERSATION_SCHEMA_READY")
    t.else_()
    t.set("%AIWConversationSchemaResult", "CONVERSATION_SCHEMA_HOLD")
    t.endif()
    return t


def validation_journal_read(root: ET.Element):
    get_template, _ = fixture.plugin_templates(root)
    arrays = [f"cgv_{c.lower()}" for c in "ABCDEFGHIJKLMN"]
    return arrays, fixture.make_get(get_template, "IngressJournal", "A2:N%AIWConversationJournalMax", arrays)


def build_validation_audit(root: ET.Element) -> T:
    arrays, journal = validation_journal_read(root)
    t = T()
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_START")
    t.set("%AIWConversationValidationReady", "0")
    p1.require_schema(t, "%AIWConversationValidationResult")
    p1.invalid(t, "%AIWConversationValidationContact", "%AIWConversationValidationResult", "CONVERSATION_VALIDATION_CONTACT_HOLD")
    p1.invalid(t, "%AIWValidationRunID", "%AIWConversationValidationResult", "CONVERSATION_VALIDATION_RUN_HOLD")
    t.if_([("%par1", 2, "PRE_JOURNALED")])
    p1.read_twice(t, journal, arrays, "%cgv_ok")
    t.if_([("%cgv_ok", 3, "1")])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_JOURNAL_HOLD")
    t.stop()
    t.endif()
    t.set("%cgv_count", "0")
    t.set("%cgv_index", "0")
    t.for_("%cgv_id", "%cgv_b()")
    t.add_value("%cgv_index")
    normalize_to(t, "%cgv_c(%cgv_index)", "%cgv_j(%cgv_index)", "%cgv_key", "cgv_pre")
    t.if_([
        ("%cgv_key", 2, "%AIWConversationValidationContact"),
        ("%cgv_e(%cgv_index)", 2, "JOURNALED"),
        ("%cgv_l(%cgv_index)", 2, "TEXTNOW"),
        ("%cgv_k(%cgv_index)", 5, r"^[0-9]{10,16}$"),
        ("%cgv_id", 5, r"(?s)^\s*$|^%.*$|(?is).*#ERROR.*"),
        ("%cgv_d(%cgv_index)", 5, r"(?s)^\s*$|^%.*$|(?is).*#ERROR.*"),
    ], ["And", "And", "And", "And", "And"])
    t.add_value("%cgv_count")
    t.if_([("%cgv_count", 6, "4")])
    for index in range(1, 5):
        t.if_([("%cgv_count", 2, str(index))])
        t.set(f"%AIWPhase4JournalRow{index}", "%cgv_index+1", maths=True)
        t.set(f"%AIWPhase4EventID{index}", "%cgv_id")
        t.set(f"%AIWPhase4EventSender{index}", "%cgv_c(%cgv_index)")
        t.set(f"%AIWPhase4EventMessage{index}", "%cgv_d(%cgv_index)")
        t.endif()
    t.endif()
    t.endif()
    t.endfor()
    t.if_([("%cgv_count", 6, "2"), ("%cgv_count", 7, "4")], ["Or"])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_EVENT_COUNT_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWPhase4EventCount", "%cgv_count")
    for left in range(1, 5):
        for right in range(left + 1, 5):
            t.if_([("%AIWPhase4EventCount", 6, str(right - 1)), (f"%AIWPhase4EventID{left}", 2, f"%AIWPhase4EventID{right}")], ["And"])
            t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_DUPLICATE_ID_HOLD")
            t.stop()
            t.endif()
    t.set("%AIWConversationValidationReady", "1")
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_JOURNALED_READY")
    t.stop()
    t.endif()
    t.if_([("%par1", 2, "ADMITTED")])
    p1.read_twice(t, journal, arrays, "%cgv_ok")
    t.if_([("%cgv_ok", 3, "1")])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_ADMISSION_READ_HOLD")
    t.stop()
    t.endif()
    t.set("%cgv_admitted_ok", "1")
    for index in range(1, 5):
        t.if_([("%AIWPhase4EventCount", 6, str(index - 1))])
        t.set(f"%cgv_idmatch{index}", "0")
        t.set(f"%cgv_valid{index}", "0")
        t.set("%cgv_index", "0")
        t.for_("%cgv_id", "%cgv_b()")
        t.add_value("%cgv_index")
        t.if_([("%cgv_id", 2, f"%AIWPhase4EventID{index}")])
        t.add_value(f"%cgv_idmatch{index}")
        normalize_to(t, "%cgv_c(%cgv_index)", "%cgv_j(%cgv_index)", "%cgv_key", f"cgv_admit{index}")
        t.if_([
            ("%cgv_e(%cgv_index)", 4, r"^(RESOLVED_MAIN|RESOLVED_OVERFLOW)$"),
            ("%cgv_l(%cgv_index)", 2, "TEXTNOW"),
            ("%cgv_c(%cgv_index)", 2, f"%AIWPhase4EventSender{index}"),
            ("%cgv_d(%cgv_index)", 2, f"%AIWPhase4EventMessage{index}"),
            ("%cgv_key", 2, "%AIWConversationValidationContact"),
            ("%cgv_k(%cgv_index)", 5, r"^[0-9]{10,16}$"),
        ], ["And", "And", "And", "And", "And"])
        t.add_value(f"%cgv_valid{index}")
        t.endif()
        t.endif()
        t.endfor()
        t.if_([(f"%cgv_idmatch{index}", 3, "1"), (f"%cgv_valid{index}", 3, "1")], ["Or"])
        t.set("%cgv_admitted_ok", "0")
        t.endif()
        t.endif()
    t.if_([("%cgv_admitted_ok", 3, "1")])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_ADMISSION_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationValidationReady", "1")
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_ADMITTED_READY")
    t.stop()
    t.endif()
    t.if_([("%par1", 2, "POST")])
    t.set("%AIWConversationGroupID", "%AIWConversationValidationGroupID")
    t.perform("AIW Conversation Ledger Locate", "GROUP")
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_FOUND"), ("%AICGL_O", 3, "GROUP_COMPLETE"), ("%AICGL_AJ", 3, "%AIWValidationRunID"), ("%AICGL_AP", 3, "VALIDATION_CONVERSATION")], ["Or", "Or", "Or"])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_COMPLETE_HOLD")
    t.stop()
    t.endif()
    p1.load_group_globals(t)
    t.set("%AIWConversationValidationGroupID", "%AIWConversationGroupID")
    t.set("%AIWConversationValidationLedgerRow", "%AIWConversationLedgerRow")
    t.if_([("%SSSentOne", 3, "1"), ("%AIWPhase4Confirmed", 3, "1"), ("%AIWPhase4Archived", 3, "1")], ["Or", "Or"])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_SEND_ARCHIVE_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationValidationReady", "1")
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_POST_PASS")
    t.stop()
    t.endif()
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_MODE_HOLD")
    return t


def build_deferred_recheck() -> T:
    t = T()
    t.set("%AIWConversationQuietRecheckResult", "CONVERSATION_QUIET_RECHECK_START")
    t.if_([("%par1", 5, r"^[0-9]{10,16}$"), ("%par2", 4, r"(?s)^\s*$|^%.*$|(?is).*#ERROR.*")], ["Or"])
    t.set("%AIWConversationQuietRecheckResult", "CONVERSATION_QUIET_RECHECK_INPUT_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWStopRequested", 2, "1"), ("%AIWorkerOn", 3, "1")], ["Or"])
    t.set("%AIWConversationQuietRecheckResult", "CONVERSATION_QUIET_RECHECK_CANCELLED_STOP")
    t.stop()
    t.endif()
    t.if_([
        ("%AIWQueueOwner", 4, r"(?s)^(?!%).+"),
        ("%AIWConversationOwner", 4, r"(?s)^(?!%).+"),
        ("%AIWProcessing", 2, "1"),
        ("%AIWSending", 2, "1"),
        ("%AIWConfirming", 2, "1"),
        ("%AIWArchiving", 2, "1"),
    ], ["Or", "Or", "Or", "Or", "Or"])
    t.set("%AIWConversationQuietRecheckResult", "CONVERSATION_QUIET_RECHECK_LOCK_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWConversationQuietRecheckTarget", "%par1")
    t.set("%AIWConversationQuietRecheckSender", "%par2")
    t.set("%AIWConversationQuietRecheckResult", "CONVERSATION_QUIET_RECHECK_ARMED")
    t.for_("%cgdr_tick", ",".join(str(i) for i in range(1, 16)))
    t.if_([("%AIWStopRequested", 2, "1"), ("%AIWorkerOn", 3, "1")], ["Or"])
    t.clear("%AIWConversationQuietRecheckTarget")
    t.clear("%AIWConversationQuietRecheckSender")
    t.set("%AIWConversationQuietRecheckResult", "CONVERSATION_QUIET_RECHECK_CANCELLED_STOP")
    t.stop()
    t.endif()
    t.if_([("%TIMEMS", 6, "%AIWConversationQuietRecheckTarget")])
    t.wait(1)
    t.endif()
    t.endfor()
    t.if_([("%TIMEMS", 6, "%AIWConversationQuietRecheckTarget")])
    t.clear("%AIWConversationQuietRecheckTarget")
    t.clear("%AIWConversationQuietRecheckSender")
    t.set("%AIWConversationQuietRecheckResult", "CONVERSATION_QUIET_RECHECK_DEADLINE_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWStopRequested", 2, "1"), ("%AIWorkerOn", 3, "1")], ["Or"])
    t.clear("%AIWConversationQuietRecheckTarget")
    t.clear("%AIWConversationQuietRecheckSender")
    t.set("%AIWConversationQuietRecheckResult", "CONVERSATION_QUIET_RECHECK_CANCELLED_STOP")
    t.stop()
    t.endif()
    t.clear("%AIWConversationQuietRecheckTarget")
    t.clear("%AIWConversationQuietRecheckSender")
    t.perform("AIW Integrated Queue Cycle", "QUIET_RECHECK")
    t.set("%AIWConversationQuietRecheckResult", "CONVERSATION_QUIET_RECHECK_DISPATCHED")
    return t


def patch_task263(raw: str) -> str:
    actions = fixture.action_list(raw)
    quiet = T()
    quiet.if_([("%AIWProcessOneResult", 2, "CONVERSATION_QUIET_WAIT_HOLD")])
    quiet.set("%AIWorkerBusy", "0")
    quiet.perform("AIW Queue Owner", "RELEASE", "%qc_owner")
    quiet.if_([("%AIWQueueLockResult", 3, "LOCK_RELEASED_EXACT")])
    quiet.set("%AIWQueueCycleResult", "QUEUE_RELEASE_HOLD")
    quiet.stop()
    quiet.endif()
    quiet.perform("AIW Conversation Deferred Recheck", "%AIWConversationQuietRecheckCutoff", "%AIWConversationQuietRecheckSender")
    quiet.set("%AIWQueueCycleResult", "%AIWConversationQuietRecheckResult")
    quiet.stop()
    quiet.endif()
    actions[31:31] = quiet.actions
    # Surface lifecycle wrapper outcomes instead of overwriting them with a generic verified label.
    target = next(i for i, action in enumerate(actions) if "<Str sr=\"arg0\" ve=\"3\">%AIWQueueCycleResult</Str><Str sr=\"arg1\" ve=\"3\">QUEUE_CYCLE_VERIFIED</Str>" in action)
    replacement = T()
    replacement.if_([("%AIWProcessOneResult", 4, r"^(CONVERSATION_GROUP_LIFECYCLE_ONLY|CONVERSATION_GROUP_REVIEW_ONLY)$")])
    replacement.set("%AIWQueueCycleResult", "%AIWProtectedSendResult")
    replacement.else_()
    replacement.set("%AIWQueueCycleResult", "QUEUE_CYCLE_VERIFIED")
    replacement.endif()
    actions[target:target + 1] = replacement.actions
    return fixture.replace_actions(raw, actions)


def patch_task282(raw: str) -> str:
    actions = fixture.action_list(raw)
    gate = T()
    gate.perform("AIW Conversation Prepare Group", "LIFECYCLE_GATE")
    gate.if_([("%AIWConversationPrepareResult", 3, "CONVERSATION_NO_ACTIVE_GROUP")])
    gate.set("%AIWProcessOneResult", "%AIWConversationPrepareResult")
    gate.stop()
    gate.endif()
    actions[1:1] = gate.actions
    return fixture.replace_actions(raw, actions)


def patch_task273(raw: str) -> str:
    t = T()
    t.set("%AIWValidationPhaseResult", "PHASE4_CONVERSATION_R1_START")
    t.if_([("%AIWConversationValidationHistoryID", 4, r"(?s)^\s*$|^%.*$|(?is).*#ERROR.*"), ("%AIWConversationValidationHistoryID", 3, "%AIWFXHistArchiveID")], ["Or"])
    t.set("%AIWValidationPhaseResult", "PHASE4_HISTORY_FIXTURE_HOLD")
    t.stop()
    t.endif()
    t.set("%AIWValidationRealSendAuthorized", "1")
    t.set("%AIWStopRequested", "0")
    t.set("%AIWorkerOn", "1")
    fixture.add_profile_state(t, "FINAL TextNow Trigger", True)
    t.add('<code>550</code><Str sr="arg0" ve="3">AIW PHASE 4 R1</Str><Str sr="arg1" ve="3">SEND 2 TO 4 RAPID TEST MESSAGES FROM THE APPROVED CONTACT. ONE SEND MAXIMUM.</Str><Int sr="arg2" val="1" /><Str sr="arg3" ve="3">Popup</Str>')
    t.wait(45)
    t.perform("AIW Conversation Validation Audit", "PRE_JOURNALED")
    t.if_([("%AIWConversationValidationReady", 3, "1")])
    t.set("%AIWValidationPhaseResult", "%AIWConversationValidationResult")
    t.set("%AIWValidationRealSendAuthorized", "0")
    t.perform("APP Stop AI Worker")
    t.stop()
    t.endif()
    t.perform("AIW Integrated Queue Cycle")
    t.perform("AIW Conversation Validation Audit", "ADMITTED")
    t.if_([("%AIWConversationValidationReady", 3, "1")])
    t.set("%AIWValidationPhaseResult", "%AIWConversationValidationResult")
    t.set("%AIWValidationRealSendAuthorized", "0")
    t.perform("APP Stop AI Worker")
    t.stop()
    t.endif()
    t.set("%AIWValidationRealSendAuthorized", "0")
    t.perform("APP Stop AI Worker")
    t.perform("AIW Conversation Validation Audit", "POST")
    t.if_([("%AIWConversationValidationReady", 3, "1")])
    t.set("%AIWValidationPhaseResult", "%AIWConversationValidationResult")
    t.stop()
    t.endif()
    t.set("%AIWValidationPhaseResult", "PHASE4_PASS")
    t.perform("AIW Proof Ledger Append", "PHASE4", "PHASE4_CONVERSATION_R1_PASS")
    t.if_([("%AIWProofWriteVerified", 3, "1")])
    t.set("%AIWValidationPhaseResult", "PHASE4_PROOF_HOLD")
    t.endif()
    return fixture.replace_actions(raw, t.actions)


def helper_xml(task_id: int, name: str, builder: T) -> str:
    raw = fixture.task_xml(task_id, name, builder)
    return raw.replace("<rty>0</rty>", "<rty>1</rty>", 1)


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
    builders = {
        309: build_quiet_select(root),
        317: build_prepare_group(),
        320: build_pre_send(root),
        324: build_schema(root),
        325: build_validation_audit(root),
        327: build_deferred_recheck(),
    }
    if len(builders[327].actions) >= 500:
        raise RuntimeError(f"Deferred helper exceeds 499 actions: {len(builders[327].actions)}")
    replacements = {
        263: patch_task263(source[263]),
        273: patch_task273(source[273]),
        282: patch_task282(source[282]),
        309: fixture.replace_actions(source[309], builders[309].actions),
        317: fixture.replace_actions(source[317], builders[317].actions),
        320: fixture.replace_actions(source[320], builders[320].actions),
        324: fixture.replace_actions(source[324], builders[324].actions),
        325: fixture.replace_actions(source[325], builders[325].actions),
    }
    for task_id, node in replacements.items():
        text, count = re.subn(rf'<Task sr="task{task_id}".*?</Task>', lambda _: node, text, count=1, flags=re.DOTALL)
        if count != 1:
            raise RuntimeError(f"Task {task_id} replacement count {count}")
    node = helper_xml(327, ADDED_HELPERS[327], builders[327])
    text = fixture.insert_helpers_and_registry(text, {327: node})
    output = text.encode("utf-8")
    ET.fromstring(output)
    final = fixture.raw_tasks(text)
    changed = sorted(task_id for task_id in source if source[task_id] != final.get(task_id))
    added = sorted(set(final) - set(source))
    if changed != sorted(AUTHORIZED_EXISTING):
        raise RuntimeError(f"Unauthorized existing-task change: {changed}")
    if added != [327]:
        raise RuntimeError(f"Unexpected helper set: {added}")
    for task_id in set(source) - AUTHORIZED_EXISTING:
        if source[task_id] != final[task_id]:
            raise RuntimeError(f"Task {task_id} changed outside authorization")
    for task_id in PHONE_PROVEN | JOURNAL_RESOLUTION | PRESERVED_CONVERSATION | PRESERVED_FIXTURE:
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
        print(f"TASK={task_id}|ACTIONS={len(builders[task_id].actions)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"BUILD_FAILED={type(exc).__name__}:{exc}", file=sys.stderr)
        raise
