# Promotion Queue

This queue contains sanitized Markdown-only promotion requests and decisions.

## Safe packet naming

Use linked packet filenames in this format:

`YYYYMMDD_<LANE_ID>_PROMOTION_<SHORT_PURPOSE>.md`

Example:

`20260721_TEST_BRAIN_ARCHIVE_ALIGNMENT_PROMOTION_SECTION12.md`

## Queue Rules

- A lane record can request promotion, but it cannot promote itself.
- Merging this coordination folder does not promote evidence into Main.
- Only an explicit promotion record plus controller decision may change Main authority.
- Production Brain/context work remains unauthorized unless an explicit controller decision authorizes it.

## Forbidden Content

Do not store XML, credentials, API keys, inherited key patterns, private URLs, phone numbers, messages, workbook rows, screenshots, runlogs, or private artifact bytes.
