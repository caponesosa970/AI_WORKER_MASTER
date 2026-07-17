# Static Scenario Matrix

| Scenario | Result |
|---|---|
| Exact base SHA | PASS |
| Owner acquisition and matching-owner release | PASS |
| Unowned release | Rejected |
| Active owner | Busy HOLD; no steal |
| Sheet1 A:Z truly blank | Eligible for direct write |
| Sheet1 hidden protected field occupied | HOLD |
| Direct payload staging readback | PASS |
| NEW written only after staging readback | PASS |
| Overflow target rows 2-986 | Accepted |
| Overflow target above 986 | HOLD |
| Overflow A:N occupied | HOLD |
| Overflow PENDING write and readback | PASS |
| Exact active duplicate | Suppressed |
| Same ID with different payload | ID_COLLISION_REVIEW |
| Multiple active matches | DUPLICATE_MAIN_REVIEW |
| Archive match | Historical duplicate |
| DeadArchive match | EVENT_HISTORY_REVIEW |
| Same fixed millisecond ID generation | Distinct numeric sequence IDs |
| Special characters | Exact logical readback required |
| Unsupported mode | HOLD before lock/write |
| Unarmed launcher | Zero task call/write |
| Drain and Queue Cycle reachability | Zero |
| Profile enablement | Zero |

Runtime results remain HOLD for phone proof.
