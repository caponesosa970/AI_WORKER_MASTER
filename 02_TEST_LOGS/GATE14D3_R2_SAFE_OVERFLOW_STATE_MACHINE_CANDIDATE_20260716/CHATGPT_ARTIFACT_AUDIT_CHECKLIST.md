# ChatGPT Artifact Audit Checklist

- [ ] Verify XML SHA256 and size.
- [ ] Verify ZIP SHA256, one entry, and byte equality.
- [ ] Verify 97 tasks / 4 disabled profiles / 1 scene.
- [ ] Verify only Tasks 33, 35, 68, 215, 217, 218, 219, and 220 changed among existing tasks.
- [ ] Verify Tasks 242-245 are the only additions.
- [ ] Verify legacy hard-release incoming callers equal zero.
- [ ] Verify every Get Data node has Array Clear plus bounded error routing.
- [ ] Verify owner-token acquisition/release and no age stealing.
- [ ] Verify OriginalID and OverflowID separation.
- [ ] Verify unresolved-state barrier and LoggedAt/source-row FIFO.
- [ ] Verify OVERFLOW_ADMITTING payload readback precedes NEW.
- [ ] Verify MAIN_COMMITTED and DRAINED readbacks.
- [ ] Verify partial reconciliation has zero second main write.
- [ ] Verify capacity 999 / max row 1000 and no overwrite.
- [ ] Verify five controlled modes and outputs.
- [ ] Verify forbidden path scan and privacy scan.
- [ ] Keep status CANDIDATE / HOLD; do not merge or import yet.
