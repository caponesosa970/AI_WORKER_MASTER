# 29A Authoritative Source Decision

Decision: NO AUTHORITATIVE SOURCE FOUND

Repair authorization: DENIED BY SOURCE-TRUTH RULE

## Required Standard

The requested repair was authorized only if an exact SEARCH_ICON source met all four requirements:

| Requirement | Result |
|---|---|
| Phone-exported or directly created by Sosa | Not proven for the candidate repair action |
| Supported by successful historical phone behavior | Not proven with a complete raw runlog tied to the exact source |
| Not contradicted by newer phone proof | Not met for V15A `menu_search` source |
| Fully inspectable field-by-field | Static XML can be inspected, but phone-visible action setup remains disputed |

## Why V15A Cannot Be Used Directly

The V15A `FINAL Send Sheet` SEARCH_ICON action is the `menu_search` ID action shape. That is the same family of action that the current 27B phone proof flagged as not Sosa-created and that failed at SEARCH_ICON.

Using it again would repeat the exact failure class:

- a static source says the action is present
- a report calls it preserved
- phone proof rejects the visible action setup

That is not a valid repair basis.

## Why The Older Text-Based Search Action Cannot Be Used Yet

The older text-based `Search` action is potentially valuable. It is not junk. It may be the correct direction.

It still cannot be used for this repair because the current proof package does not show:

- an exported Sosa-created source for that exact action
- a complete successful historical run tied to that exact source
- phone-visible field proof for the exact AutoInput action
- clean controller approval to replace only SEARCH_ICON with that shape

## Required Missing Proof

To authorize a future one-action repair, ChatGPT needs one of these:

1. A fresh Sosa phone export of the expected SEARCH_ICON AutoInput action, with no private key material.
2. A known-good Tasker XML source plus raw successful runlog proving the exact SEARCH_ICON action in that source.
3. A phone-visible AutoInput field screenshot/export showing the exact expected SEARCH_ICON setup, plus controller approval to copy that exact field set.

Until then:

- Do not patch SEARCH_ICON.
- Do not run 27B again.
- Do not approve phone import.
- Keep controlled send HOLD.
