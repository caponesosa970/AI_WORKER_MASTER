# Source Mapping

## Admission

`GATE14D3 Overflow Admission Probe` calls the unchanged `PROCESS Controlled Capacity Batch` once with expected count 50. That source loops exactly 50 times with source row `148 + index`, so its reachable rows are exactly 149-198.

The probe reads row 199 before and after that call and requires exact ID, sender, message, NEW status, and blank Reply both times.

## Deferred Drain

The probe binds only row 199, then calls the unchanged processor lane: lock start, mark processing, prompt build, bounded HTTP wrapper, reply parse, verified success/failure commit, and owned lock release.

No copied production logic or second transaction engine was introduced.
