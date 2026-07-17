# AutoSheets And Readback Report

Every new Get Data node:

- clears every indexed output with Tasker Array Clear code 357;
- clears `%err` and `%errmsg`;
- has Continue Task After Error enabled;
- routes numeric nonzero error only;
- permits at most two attempts with one bounded three-second wait.

Every authoritative destination is read directly. View output never authorizes a write by itself.

Every update has offline queueing disabled and sheet creation disabled. A plugin-reported update error may count as success only when exact readback proves the requested state.
