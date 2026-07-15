# ChatGPT Artifact Audit Checklist

ChatGPT must independently verify the actual files, not only these reports:

1. Standalone XML SHA equals `FF08EEFFC6E3D6350CEA10924164FAC962797BE984C3643B4A5A68E1D1095195`.
2. ZIP SHA equals `8D23873ECFDA050A25E0C0F26CB4708E108154F7187DC485808014653F907A70`.
3. ZIP contains exactly `GATE11_FULL_PROJECT_TASKER_IMPORT__EXACT_ROW_ARCHIVE_PRIVATE.xml`.
4. ZIP XML bytes match standalone XML.
5. XML parses with TaskerData root and 78/4/1 topology.
6. Task 224 is the one-time Gate 11 launcher and calls Task 226 once.
7. Task 226 is the only new task and has no other incoming caller.
8. Tasks 71, 75, 199, 223, 225 and every other pre-existing task except 224 are raw-byte identical.
9. No profile/scene/reference change is hidden.
10. Task 226 reads only exact bound Sheet1 A:I and requires DONE.
11. Archive scan is exact A2:J1000 with exact duplicate count and first verified empty ID row.
12. Archive exact readback precedes source clear.
13. Immediate source revalidation precedes source clear.
14. Exact source A:I clear readback is required.
15. Existing-copy clear recovery cannot append a duplicate.
16. All 20 AutoSheets actions use Continue Task After Error and all operations are bounded to two attempts.
17. Every owned-lock exit releases once and unowned exits release zero times.
18. No Send, TextNow, confirmation, broad Archive, DeadArchive, Compactor, live, timer, capacity, or release path is reachable.
19. Credential occurrence is unchanged without printing it.
20. Public repository diff contains no private path, local path, test ID, phone number, credential, or private XML.

Passing this checklist still does not constitute phone proof or automatic phone-import approval.
