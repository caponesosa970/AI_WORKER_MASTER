from __future__ import annotations

import argparse
import hashlib
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import aiw_conversation_continuity_phase1_build as p1
import aiw_final_fixture_safety_repair as fixture


EXPECTED_BASE_SHA = "9EB0A9FD6B3E342E4022AEE20022683F1BF08A54E65892A099565A3542D0A758"
AUTHORIZED_EXISTING = {273, 320, 325}
PHONE_PROVEN = {71, 199, 223, 225, 226, 227, 230, 231}
EXPLICITLY_FROZEN = {254, 255, 262, 263, 282, 309, 317, 327}
T = fixture.TaskBuilder


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def patch_task320(raw: str) -> str:
    actions = fixture.action_list(raw)
    if len(actions) != 364:
        raise RuntimeError(f"Unexpected R1 Task 320 action count: {len(actions)}")

    # Lifecycle-only states must continue to bypass the pre-click freshness gate.
    if "CONVERSATION_GROUP_STATE_HOLD" not in actions[83] or "<code>38</code>" not in actions[85]:
        raise RuntimeError("Task 320 lifecycle boundary moved")

    contract = T()
    contract.set("%AIWConversationMemberCapacity", "%AICGL_AI")
    contract.set("%cgf_freshness_cutoff", "%AIWConversationBoundAt")
    contract.set("%cgf_capacity_contract_ok", "1")
    contract.if_([
        ("%AIWConversationMemberCount", 5, r"^[1-4]$"),
        ("%AIWConversationMemberCapacity", 5, r"^[1-4]$"),
        ("%AIWConversationFreezeLoggedAt", 5, r"^[0-9]{10,16}$"),
        ("%AIWConversationBoundAt", 5, r"^[0-9]{10,16}$"),
    ], ["Or", "Or", "Or"])
    contract.set("%cgf_capacity_contract_ok", "0")
    contract.endif()
    contract.if_([
        ("%AIWConversationMemberCount", 7, "%AIWConversationMemberCapacity"),
        ("%AIWConversationFreezeLoggedAt", 7, "%AIWConversationBoundAt"),
    ], ["Or"])
    contract.set("%cgf_capacity_contract_ok", "0")
    contract.endif()
    contract.if_([("%cgf_capacity_contract_ok", 3, "1")])
    contract.set("%AIWConversationPreSendResult", "CONVERSATION_PRE_SEND_CAPACITY_CONTRACT_HOLD")
    contract.stop()
    contract.endif()
    contract.if_([("%AIWConversationMemberCount", 2, "%AIWConversationMemberCapacity")])
    contract.set("%cgf_freshness_cutoff", "%AIWConversationFreezeLoggedAt")
    contract.endif()

    replacements = 0
    updated: list[str] = []
    for action in actions:
        action, count = re.subn(
            r"(<rhs>)%AIWConversationBoundAt(</rhs>)",
            r"\1%cgf_freshness_cutoff\2",
            action,
        )
        replacements += count
        updated.append(action)
    if replacements != 3:
        raise RuntimeError(f"Expected three Task 320 cutoff replacements, found {replacements}")
    updated[86:86] = contract.actions
    return fixture.replace_actions(raw, updated)


def patch_task273(raw: str) -> str:
    actions = fixture.action_list(raw)
    if len(actions) != 38:
        raise RuntimeError(f"Unexpected R1 Task 273 action count: {len(actions)}")
    joined = "".join(actions)
    required = {
        "PHASE4_CONVERSATION_R1_START": "PHASE4_CONVERSATION_R2_START",
        "AIW PHASE 4 R1": "AIW PHASE 4 R2",
        "PHASE4_CONVERSATION_R1_PASS": "PHASE4_CONVERSATION_R2_PASS",
    }
    for old, new in required.items():
        if joined.count(old) != 1:
            raise RuntimeError(f"Task 273 marker count for {old}: {joined.count(old)}")
        joined = joined.replace(old, new, 1)
    actions = re.findall(r"<Action\b.*?</Action>", joined, flags=re.DOTALL)

    capacity = T()
    capacity.perform("AIW Conversation Validation Audit", "CAPACITY_CONTRACT")
    capacity.if_([("%AIWConversationValidationReady", 3, "1")])
    capacity.set("%AIWValidationPhaseResult", "%AIWConversationValidationResult")
    capacity.set("%AIWValidationRealSendAuthorized", "0")
    capacity.perform("APP Stop AI Worker")
    capacity.stop()
    capacity.endif()
    # Insert after the ADMITTED result block and before the existing stop/POST boundary.
    actions[26:26] = capacity.actions
    return fixture.replace_actions(raw, actions)


def capacity_validation_mode() -> T:
    t = T()
    t.if_([("%par1", 2, "CAPACITY_CONTRACT")])
    p1.invalid(t, "%AIWConversationValidationGroupID", "%AIWConversationValidationResult", "CONVERSATION_VALIDATION_CAPACITY_GROUP_HOLD")
    t.set("%AIWConversationGroupID", "%AIWConversationValidationGroupID")
    t.perform("AIW Conversation Ledger Locate", "GROUP")
    t.if_([("%AIWConversationLocateResult", 3, "CONVERSATION_LEDGER_FOUND")])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_CAPACITY_LOCATE_HOLD")
    t.stop()
    t.endif()
    p1.load_group_globals(t)
    t.set("%AIWConversationMemberCapacity", "%AICGL_AI")
    t.set("%AIWConversationDerivedFreshnessCutoff", "%AIWConversationBoundAt")
    t.set("%cgv_capacity_ok", "1")
    t.if_([
        ("%AIWConversationMemberCount", 5, r"^[1-4]$"),
        ("%AIWConversationMemberCapacity", 5, r"^[1-4]$"),
        ("%AIWConversationFreezeLoggedAt", 5, r"^[0-9]{10,16}$"),
        ("%AIWConversationBoundAt", 5, r"^[0-9]{10,16}$"),
    ], ["Or", "Or", "Or"])
    t.set("%cgv_capacity_ok", "0")
    t.endif()
    t.if_([
        ("%AIWConversationMemberCount", 7, "%AIWConversationMemberCapacity"),
        ("%AIWConversationFreezeLoggedAt", 7, "%AIWConversationBoundAt"),
    ], ["Or"])
    t.set("%cgv_capacity_ok", "0")
    t.endif()
    t.if_([("%cgv_capacity_ok", 3, "1")])
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_CAPACITY_CONTRACT_HOLD")
    t.stop()
    t.endif()
    t.if_([("%AIWConversationMemberCount", 2, "%AIWConversationMemberCapacity")])
    t.set("%AIWConversationDerivedFreshnessCutoff", "%AIWConversationFreezeLoggedAt")
    t.endif()
    t.set("%AIWConversationValidationReady", "1")
    t.set("%AIWConversationValidationResult", "CONVERSATION_VALIDATION_CAPACITY_CONTRACT_READY")
    t.stop()
    t.endif()
    return t


def patch_task325(raw: str) -> str:
    actions = fixture.action_list(raw)
    if len(actions) != 307:
        raise RuntimeError(f"Unexpected R1 Task 325 action count: {len(actions)}")
    if "CONVERSATION_VALIDATION_MODE_HOLD" not in actions[-1]:
        raise RuntimeError("Task 325 default HOLD boundary moved")
    mode = capacity_validation_mode()
    actions[-1:-1] = mode.actions
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
    ET.fromstring(base)
    source = fixture.raw_tasks(text)
    replacements = {
        273: patch_task273(source[273]),
        320: patch_task320(source[320]),
        325: patch_task325(source[325]),
    }
    for task_id, node in replacements.items():
        text, count = re.subn(
            rf'<Task sr="task{task_id}".*?</Task>', lambda _: node,
            text, count=1, flags=re.DOTALL,
        )
        if count != 1:
            raise RuntimeError(f"Task {task_id} replacement count {count}")

    output = text.encode("utf-8")
    root = ET.fromstring(output)
    final = fixture.raw_tasks(text)
    changed = sorted(task_id for task_id in source if source[task_id] != final.get(task_id))
    added = sorted(set(final) - set(source))
    if changed != sorted(AUTHORIZED_EXISTING):
        raise RuntimeError(f"Unauthorized existing-task change: {changed}")
    if added:
        raise RuntimeError(f"Unexpected helper set: {added}")
    for task_id in set(source) - AUTHORIZED_EXISTING:
        if source[task_id] != final[task_id]:
            raise RuntimeError(f"Task {task_id} changed outside authorization")
    for task_id in PHONE_PROVEN | EXPLICITLY_FROZEN:
        if source[task_id] != final[task_id]:
            raise RuntimeError(f"Protected task {task_id} changed")
    if len(root.findall("Profile")) != 4 or len(root.findall("Scene")) != 2:
        raise RuntimeError("Profile/scene topology changed")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(output)
    print(f"BASE_SHA256={sha256(base)}")
    print(f"OUTPUT_SHA256={sha256(output)}")
    print(f"OUTPUT_BYTES={len(output)}")
    print(f"CHANGED_EXISTING={changed}")
    print(f"ADDED_HELPERS={added}")
    for task_id in sorted(AUTHORIZED_EXISTING):
        count = len(root.find(f"Task[@sr='task{task_id}']").findall("Action"))
        print(f"TASK={task_id}|ACTIONS={count}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"BUILD_FAILED={type(exc).__name__}:{exc}", file=sys.stderr)
        raise
