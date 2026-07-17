from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


REQUIRED_TABS = [
    "SystemConfig", "Sheet1", "QueueView", "Sheet1SlotView", "OverflowInbox",
    "OverflowSlotView", "OverflowView", "Archive", "DeadArchive", "IngressJournal",
    "IngressSlotView", "IngressView", "IdentityProbe", "IdentityProbeResult", "ProofLedger",
    "ProofLedgerSlotView", "RuntimeState", "ValidationControl", "RecoveryProbe", "SchemaCheck",
    "ConversationGroups", "ConversationGroupSlotView", "ConversationSchemaCheck",
]

FORMULAS = {
    "QueueView!A1": '={"SourceRow","ID","Sender","Message","Status","Reply","Touch","Button","Time","Ticker";IFNA(FILTER({ROW(Sheet1!A2:A),Sheet1!A2:I},REGEXMATCH(Sheet1!D2:D,"^(NEW|PROCESSING|READY_TO_SEND|SENDING|SEND_CLICKED_AWAITING_CONFIRM|SEND_OUTCOME_UNKNOWN_REVIEW|POST_SEND_STATUS_UPDATE_FAILED|HOLD_PRE_SEND_FAILED|DONE|REVIEW_READY|REVIEW_HOLD|REVIEW_REJECTED|EDIT_REPLY|SKIP_MANUAL)$")),{"","","","","","","","","",""})}',
    "Sheet1SlotView!A2": '=IF(AND(ValidationControl!B2="FORCE_MAIN_FULL",ValidationControl!B3<>"NONE"),"FULL",IFERROR(MATCH(TRUE,INDEX(Sheet1!A2:A201="",0),0)+1,"FULL"))',
    "OverflowSlotView!A2": '=IFERROR(MATCH(TRUE,INDEX(OverflowInbox!A2:A986="",0),0)+1,"FULL")',
    "IngressSlotView!A2": '=IFERROR(MATCH(TRUE,INDEX(IngressJournal!A2:A1001="",0),0)+1,"FULL")',
    "ProofLedgerSlotView!A2": '=IFERROR(MATCH(TRUE,INDEX(ProofLedger!A2:A5001="",0),0)+1,"FULL")',
    "ConversationGroupSlotView!A2": '=IFERROR(MATCH(TRUE,INDEX(ConversationGroups!A2:A1000="",0),0)+1,"FULL")',
    "SchemaCheck!B2": '=IF(AND(A2="AIW_FINAL_V1",C2=201,D2=986,E2=1001,F2="FINAL_INTEGRATED"),"PASS","HOLD")',
    "ConversationSchemaCheck!A2": '=IFERROR(VLOOKUP("ConversationSchemaVersion",SystemConfig!A:B,2,FALSE),"MISSING")',
    "ConversationSchemaCheck!C2": '=ROWS(ConversationGroups!A:A)',
    "ConversationSchemaCheck!D2": '=IFERROR(VALUE(VLOOKUP("ConversationGroupMaxRow",SystemConfig!A:B,2,FALSE)),0)',
    "ConversationSchemaCheck!E2": '=ROWS(Archive!A:A)',
    "ConversationSchemaCheck!F2": '=ROWS(Sheet1!A:A)',
    "ConversationSchemaCheck!G2": '=ROWS(IngressJournal!A:A)',
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    data = args.manifest.read_bytes()
    text = data.decode("utf-8")
    checks: list[dict[str, object]] = []

    def check(name: str, passed: bool, evidence: object = None) -> None:
        checks.append({"name": name, "pass": bool(passed), "evidence": evidence})

    missing_tabs = [tab for tab in REQUIRED_TABS if f"`{tab}`" not in text]
    missing_formulas = [name for name, formula in FORMULAS.items() if formula not in text]
    check("all_required_tabs_declared", not missing_tabs, missing_tabs)
    check("all_exact_formula_markers_present", not missing_formulas, missing_formulas)
    check("overflow_view_formula_present", "OverflowInbox!A2:N986" in text and "OverflowView" in text)
    check("ingress_view_formula_present", "IngressJournal!A2:N1001" in text and "IngressView" in text)
    check("identity_formula_present", "IDENTITY_PROBE_HOLD" in text and "ID_COLLISION_REVIEW" in text and "HISTORICAL_DUPLICATE" in text)
    check("recovery_formula_set_complete", all(f"- `{cell}`:" in text for cell in ("A2", "B2", "C2", "D2", "E2", "F2")))
    check("conversation_schema_formula_complete", "TEXTJOIN(\"|\",FALSE,ConversationGroups!A1:AP1)" in text and "AIW_CONVERSATION_V1" in text)
    check("group_headers_complete", all(header in text for header in ("SchemaVersion", "GroupID", "Member4OriginalID", "GroupState", "QuietCutoffMs", "ConfirmedReply", "OwnerToken", "ArchivedMask", "Member4Message", "FixtureRole")))
    check("physical_counts_exact", all(value in text for value in ("980 x 26", "986 x 14", "1000 x 10", "1000 x 13", "1001 x 14", "5001 x 12", "1000 x 42")))
    check("archive_deadarchive_expansion_audited", "Expand the existing grid from its controller-observed 933 rows to exactly 1000 rows" in text and "Expand rows from the controller-observed 972 to exactly 1000" in text)
    check("no_older_manifest_dependency", all(phrase not in text.lower() for phrase in ("prior manifest remain", "older manifest remain", "apply the older", "points back to")))
    check("protected_sheet_rows_explicit", "`Sheet1` rows `144:147`" in text and "never fixtures" in text)
    check("row999_not_fixture", "Archive` row 999 and `DeadArchive` row 999 are not fixtures" in text and "Do not create a row-999 fixture" in text)
    check("no_guessed_fixture_row", "No row number appears in runtime as a fixture default" in text and "Do not select or guess validation fixture rows" in text)
    check("backup_order_present", "## Migration order" in text and "named backup" in text)
    check("read_only_verification_order_present", "## Read-only verification order" in text)
    check("rollback_order_present", "## Rollback order" in text)
    check("privacy_classification_present", text.count("private") >= 10)
    check("not_applied_status", "PLAN ONLY / NOT APPLIED" in text and "Codex did not open or mutate the live workbook" in text)
    check("schema_sentinels_exact", all(value in text for value in ("AIW_FINAL_V1", "FINAL_INTEGRATED", "AIW_CONVERSATION_V1", "ConversationGroupMaxRow", "ConversationMemberCapacity", "ConversationQuietSeconds")))
    check("runtime_defaults_stopped", "DesiredRun | 0 | MIGRATION | NONE" in text and "MainCapacityInjection | NORMAL" in text and "AuthorizedRunID | NONE" in text)
    check("utf8_no_bom", not data.startswith(b"\xef\xbb\xbf"))

    failures = [item for item in checks if not item["pass"]]
    report = {
        "status": "PASS" if not failures else "FAIL",
        "manifest": {"file": args.manifest.name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest().upper()},
        "required_tabs": REQUIRED_TABS,
        "formula_inventory": sorted(FORMULAS),
        "checks": checks,
        "failures": failures,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "checks": len(checks), "failures": [item["name"] for item in failures]}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
