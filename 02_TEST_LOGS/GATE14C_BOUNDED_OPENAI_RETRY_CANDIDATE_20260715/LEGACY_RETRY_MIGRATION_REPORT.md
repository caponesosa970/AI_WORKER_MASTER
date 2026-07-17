# Legacy Retry Migration

Task 236 handles old `ERROR_OPENAI_RETRY` rows without another API request.

- validates row 2-201 and exact ID/sender/message;
- reads only exact `A:E`;
- requires current status `ERROR_OPENAI_RETRY`;
- preserves Reply exactly, blank or nonblank;
- writes only `ERROR_OPENAI_REVIEW`;
- reads exact `A:E` back;
- allows two bounded write attempts;
- accepts an update error only when exact readback proves success;
- never writes `NEW`;
- never acquires/releases the processing lock;
- wrong binding produces zero writes.

Task 70 no longer contains the old `ERROR_OPENAI_RETRY -> NEW` branch.
