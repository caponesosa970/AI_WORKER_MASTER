# Exact Changed Task And Action List

Existing changed tasks: none.

Added tasks:

| ID | Name | Actions | Raw task SHA256 |
|---|---|---:|---|
| 238 | PROCESS Controlled Capacity Batch | 389 | `0F51FCF661A4C94FFF03221D4DA240C2FC3D95B2A8F9643DAA5B58C751E08F1E` |
| 239 | AIW GATE14D CONTROLLED CAPACITY TEST | 86 | `CE9DD8DA52899746C309A89C28E3E6D06EEF8B84AADD6BA18E4E0C892A853905` |

Project registry change: append task IDs `238,239` exactly once.

Task 238 uses two cloned source-proven AutoSheets Get Data nodes for exact precheck and terminal readback. Task 239 contains the one-shot authorization and calls Task 238 once.
