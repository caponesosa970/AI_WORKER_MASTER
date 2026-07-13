# Private Package Hashes - 31A / 31A1 / 31B

Private artifacts are stored outside the public repository. Do not commit private XML or ZIP files.

## Original 31A Rejected Package

ChatGPT rejected the original 31A private package because it carried the discontinued credential from an older 27B base.

| Artifact | SHA256 |
|---|---|
| full private XML | `D0F5F43DCE0BCD42ED75964ADDFFF078FCBEBC01637553153A280F478583CCD3` |
| private ZIP | `EB49A20A51C979E5ECF232875F7AB25CD26A79B7C930D558F32FBCCCFFFB9F97` |

Original 31A key result: REJECTED / DISCONTINUED.

## 31A1 Current-Key Repair Package

31A1 changed only the private credential literal. Runtime actions were not changed.

| Artifact | SHA256 |
|---|---|
| 31A1 full private XML | `1C1FAF33EA30B69E8F35478AA8E93E58A2AA4ABB967CAA8F5EA927506BBF1B6E` |
| 31A1 private ZIP | `C05103D3EE95185E6FB47523C2793A27D9DAECFDA55931C569952B7DB5023921` |

## Private Package Facts

- XML is full-project Tasker import: YES
- Task-only XML: NO
- 31A current private key claim: REJECTED / DISCONTINUED
- 31A1 current private key verified against current credential source SHA: YES
- Sanitized XML comparison after credential redaction: IDENTICAL
- Task 224 unchanged byte-for-byte: TRUE
- Runtime actions changed by 31A1: NO
- Current private key printed: NO
- ZIP integrity: PASS
- Phone proof claimed for 31A1: NO
- Phone import approved by Codex: NO

## 31B AutoSheets Preflight Retry Package

31B changes only task `224` AutoSheets row-read preflight error handling. It does not change the private credential, Search lane, AutoInput actions, downstream Send path, profiles, or scenes.

| Artifact | SHA256 |
|---|---|
| 31B full private XML | `0B984F8CADCBCCA4915676F76C269F927ADED0473C34043F15609F1720C60007` |
| 31B private ZIP | `4C529BF48A8DD71B64B0B6B2B62801A0C5C536BD1CA8B6B5DB478723B8150EA3` |

## 31B Private Package Facts

- XML is full-project Tasker import: YES
- Task-only XML: NO
- Source 31A1 XML SHA256: `1C1FAF33EA30B69E8F35478AA8E93E58A2AA4ABB967CAA8F5EA927506BBF1B6E`
- Only task 224 changed: YES
- AutoSheets attempts maximum: `2`
- Final AutoSheets failure releases lock: YES
- Final AutoSheets failure closes AllowSend: YES
- Current private key printed: NO
- Current private key changed: NO
- ZIP integrity: PASS
- Phone proof claimed for 31B: NO
- Phone import approved by Codex: NO
