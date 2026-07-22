# AI Worker Handoff Packet

`PACKET_SCHEMA_VERSION =`
`HANDOFF_ID =`
`LANE_ID =`
`DIRECTION = CHATGPT_TO_CODEX | CODEX_TO_CHATGPT`
`STATUS = NEW | READY | RETURNED | HOLD | REJECTED | LANE_LOCKED`
`CREATED_UTC =`
`CURRENT_MAIN_SHA =`
`SOURCE_COMMIT_SHA =`
`SUPERSEDES =`
`EVIDENCE_CLASSIFICATION = PROVEN | INFERENCE | UNKNOWN`

## Immutability rule

Committed packets are immutable records. Corrections must use a new packet naming the prior packet in `SUPERSEDES`; they must not silently rewrite evidence history.

## Objective

## Proven facts

## Inference

## Unknowns

## Authorized work

## Protected scope

## Forbidden work

## Safe artifact identities

Filenames and SHA256 values only. No credentials, private links, phone numbers, messages, workbook data, or private artifact bytes.

## Required return

## Phone boundary

## Production authorization

`PRODUCTION_AUTHORIZED = NO`