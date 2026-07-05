# ChatGPT Audit Prompt - Stage 3A 2ndLine Same-Device Retry

Audit the attached ZIP:

`AIW_BUILD100_STAGE3A_2NDLINE_SAME_DEVICE_RETRY_HOLD_20260704.zip`

Use AI Worker Build100 rules.

Classify the retry only from the evidence in the ZIP.

Expected conservative status:

CANDIDATE / HOLD FOR PHONE PROOF

Stage-specific likely status:

HOLD / NEED FINAL RUN LOG AND TRIGGER STATE VERIFICATION

Important facts to verify:

- This was not a clean external-sender proof.
- 2ndLine on the same Moto sent exactly one visible test message.
- The actual sent text was `636`.
- Safe Mode ON proof exists.
- Trigger enabled/disabled screenshots exist.
- Post-test Tasker Run Log proof is missing.
- Tasker check/apply after trigger toggle was not explicitly confirmed.
- Sheet proof search did not find `STAGE3A` or `636` in AIWProofLog.
- Do not classify this as LOCKED.
- Do not claim Stage 3A complete.

Required output:

- Final classification using LOCKED / CANDIDATE / HOLD / HARD HOLD / FAILED.
- Missing proof list.
- Whether another phone cleanup proof is required before rerun.
- Whether any XML patch is justified from this retry.
