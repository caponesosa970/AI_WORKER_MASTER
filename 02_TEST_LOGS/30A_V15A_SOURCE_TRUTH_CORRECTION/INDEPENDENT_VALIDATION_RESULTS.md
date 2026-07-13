# Independent Validation Results

Status: TWO COMPARISONS AGREE

## Method 1 - XML Plugin-Bundle Parser

Tool:

`02_TEST_LOGS/30A_V15A_SOURCE_TRUTH_CORRECTION/tools/compare_search_icon.py`

Result:

- V15A SHA matched expected source SHA.
- 27B private XML parsed.
- SEARCH_ICON found in V15A `FINAL Send Sheet`.
- SEARCH_ICON found in 27B `AIW27B_V15A_PRESERVED_CONTROLLED_SEND_CANDIDATE`.
- Exact node bytes were not equal only because action `sr` differs.
- Node bytes were equal after preserving 27B action `sr`.
- No semantic drift was found excluding action `sr`.

Method 1 decision:

No SEARCH_ICON field drift.

## Method 2 - Independent PowerShell XML Comparison

Method:

Separate XML object traversal and direct field comparison.

Fields checked:

- code
- Structure Output XML field
- plugin package
- plugin activity
- timeout
- Continue Task After Error
- ActionId
- ActionType
- FieldSelectionType
- NearbyText
- TextToWrite
- ActionPoint
- BLURB
- plugininstanceid
- plugintypeid
- accessibility setting
- IsFirstAction
- IsTaskerAction
- Password
- RepeatInterval
- RepeatTimes
- StoredAction
- subbundled flag
- variable replacement keys
- relevant variable outputs

Result:

All checked fields matched. The only expected difference was action `sr`.

Method 2 decision:

No SEARCH_ICON field drift.

## Combined Decision

No runtime repair is authorized because no SEARCH_ICON drift exists.

The remaining failure is a phone/runtime/UI behavior problem, not an XML source-preservation problem.
