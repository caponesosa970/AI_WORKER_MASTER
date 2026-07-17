from __future__ import annotations

import argparse
import json
from pathlib import Path

import aiw_conversation_continuity_phase1_r1_migration_validate as r1m


LIVE = {
    "SystemConfig": "1000 x 26", "Sheet1": "980 x 103", "QueueView": "979 x 26",
    "OverflowInbox": "986 x 92", "OverflowView": "1000 x 26",
    "OverflowSlotView": "1000 x 26", "Archive": "933 x 26", "DeadArchive": "972 x 87",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    text = args.manifest.read_text(encoding="utf-8")
    checks: list[dict[str, object]] = []

    def check(name: str, passed: bool, evidence: object = None) -> None:
        checks.append({"name": name, "pass": bool(passed), "evidence": evidence})

    check("r2_authority", "Conversation Continuity P1 R2" in text and "non-destructive migration authority" in text)
    check("minimum_not_exact_resize", "minimum runtime requirement" in text and "Target physical rows x columns" not in text)
    check("never_shrink_contract", all(value in text for value in ("Never shrink a row count", "column count", "existing grid range", "extension column", "populated cell")))
    check("controller_live_dimensions_complete", all(f"`{tab}` | {grid}" in text for tab, grid in LIVE.items()), LIVE)
    check("systemconfig_preserve_existing", "SystemConfig!A1:J2" in text and "Preserve `A1:J2` exactly" in text)
    check("systemconfig_blank_reread", "re-read `A3:D16`" in text and "require every cell blank" in text)
    system_section = text.split("### SystemConfig", 1)[1].split("### Sheet1", 1)[0]
    check("systemconfig_no_row1_rewrite", "Do not write or replace row 1" in system_section and "Headers `A1:D1`" not in system_section)
    required_rows = {
        3: "SchemaVersion", 4: "MainMaxRow", 5: "OverflowMaxRow", 6: "JournalMaxRow",
        7: "ReleaseMode", 8: "DeadArchiveEnabled", 9: "CompactorEnabled",
        10: "ConversationSchemaVersion", 11: "ConversationGroupMaxRow",
        12: "ConversationMemberCapacity", 13: "ConversationQuietSeconds",
        14: "Sheet1PhysicalMaxRow", 15: "ArchivePhysicalMaxRow", 16: "DeadArchivePhysicalMaxRow",
    }
    check("systemconfig_rows_exact", all(f"| {row} | `{key}` |" in text for row, key in required_rows.items()), required_rows)
    check("vlookup_ab_preserved", text.count("SystemConfig!A:B") >= 6, text.count("SystemConfig!A:B"))
    check("sheet_extension_preserved", "Sheet1!J:CY" in text and "Columns `J:CY`" in text)
    check("queue_extension_preserved", "QueueView!K:Z" in text)
    check("overflow_extension_preserved", "OverflowInbox!O:CN" in text and "columns `O:CN`" in text)
    check("archive_extension_preserved", "Archive!K:Z" in text and "add 67 rows" in text.lower())
    check("deadarchive_extension_preserved", "DeadArchive!N:CI" in text and "add 28 rows" in text.lower())
    check("archive_rows_add_only", "Add exactly 67 rows" in text and "Do not shrink columns" in text)
    check("deadarchive_rows_add_only", "Add exactly 28 rows" in text and "Do not shrink columns" in text)
    check("queueview_preserve_if_match", "Preserve `QueueView!A1` when it already matches" in text)
    check("only_existing_overflow_anchors_replace", "only authorized existing-view replacements are `OverflowView!A1` and `OverflowSlotView!A2`" in text)
    check("header_aliases_preserved", "header aliases" in text and "runtime authority is positional" in text)
    check("protected_rows_144_147", "Sheet1` rows `144:147`" in text and "never fixtures" in text)
    check("row999_not_fixture", "Archive` row 999" in text and "DeadArchive` row 999" in text)
    check("dynamic_fixtures_only", "Do not select or guess validation fixture rows" in text)
    check("historical_rows_complete", all(f"Sheet1!A{row}:Z{row}" in text for row in (69, 72, 73, 141)))
    check("historical_status_only_plan", "Change only column D from exact `NEW` to exact `REVIEW_HOLD`" in text)
    check("historical_protected_columns", "A:C and E:Z are unchanged" in text)
    check("historical_never_send_archive_clear", all(value in text for value in ("`PROCESSING`", "`READY_TO_SEND`", "`DONE`", "Never Archive or clear")))
    check("historical_not_applied", "HISTORICAL ROWS UNCHANGED" in text)
    check("all_r1_formula_contracts_retained", all(value in text for value in r1m.FORMULAS.values()), sorted(r1m.FORMULAS))
    check("conversation_schema_formula_retained", "TEXTJOIN(\"|\",FALSE,ConversationGroups!A1:AP1)" in text)
    check("migration_readback_matrix", "no preexisting dimension to decrease" in text and "Prove only the approved SystemConfig block" in text)
    check("rollback_non_destructive", "never overwrite preserved cells while rolling back" in text and "retain all original columns" in text)
    check("plan_not_applied", "NON-DESTRUCTIVE PLAN ONLY / NOT APPLIED" in text)

    report = {
        "status": "PASS" if all(item["pass"] for item in checks) else "FAIL",
        "controller_dimensions_source": True,
        "live_workbook_accessed": False,
        "checks": checks,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "checks": len(checks), "failed": [item["name"] for item in checks if not item["pass"]]}, indent=2))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
