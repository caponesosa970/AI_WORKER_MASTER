# Static Validation And 30-Case Matrix

Independent validator result: PASS

## Matrix

1. PASS - Positive DONE row with no Archive duplicate
2. PASS - Bad source-row parameter
3. PASS - Bad expected-ID parameter
4. PASS - Wrong source ID
5. PASS - Status not DONE
6. PASS - Blank sender
7. PASS - Blank message
8. PASS - Blank reply
9. PASS - Literal variable field
10. PASS - #ERROR field
11. PASS - Archive lock busy
12. PASS - Send lock busy
13. PASS - Confirmation lock busy
14. PASS - Processing lock busy
15. PASS - Existing exact Archive match plus exact source row
16. PASS - Existing exact Archive match plus blank source row
17. PASS - Existing Archive ID conflict
18. PASS - Multiple Archive rows with same ID
19. PASS - No free Archive target row
20. PASS - Initial source read timeout
21. PASS - Archive scan timeout
22. PASS - Archive write failure
23. PASS - Archive readback mismatch
24. PASS - Source row changed after Archive copy
25. PASS - Source clear failure after verified Archive copy
26. PASS - Source clear readback mismatch
27. PASS - Retry after copy-success/clear-failure creates no duplicate
28. PASS - Every owned-lock terminal path releases exactly once
29. PASS - No unowned-lock release
30. PASS - No reachable Send, TextNow, confirmation, DeadArchive, Compactor, live, or broad Archive path

## Machine Assertions

- XML parse / TaskerData root: PASS
- Topology: 78 tasks / 4 profiles / 1 scene
- Duplicate task IDs/names/sr/action-sr: 0
- Missing Perform Task refs: 0
- Task 224 calls Task 226 exactly once
- Other Task 226 incoming references: 0
- Task 226 actions: 1,477
- Task 226 AutoSheets actions: 20
- AutoSheets Continue After Error: 20/20
- Get operations: 8 logical operations, exactly 2 attempts each
- Update operations: 2 logical operations, exactly 2 attempts each
- Numeric plugin error checks only; `^.+$` checks: 0
- Control-flow final If stack depth: 0 for Tasks 224 and 226
- Stop while Archive lock owned before release: 0
- Archive lock acquire nodes: 1
- Guarded Archive lock release blocks: 1
- ZIP contains one XML and ZIP bytes equal standalone XML: PASS
