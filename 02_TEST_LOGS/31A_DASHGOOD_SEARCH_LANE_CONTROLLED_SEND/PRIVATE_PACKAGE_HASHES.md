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

The narrow 31B AutoSheets-only package is superseded by the current 31B transaction-safety package.

| Artifact | SHA256 |
|---|---|
| superseded narrow 31B full private XML | `0B984F8CADCBCCA4915676F76C269F927ADED0473C34043F15609F1720C60007` |
| superseded narrow 31B private ZIP | `4C529BF48A8DD71B64B0B6B2B62801A0C5C536BD1CA8B6B5DB478723B8150EA3` |
| final superseding 31B full private XML | `156D44624EF534DB8F0D4E81F0E873A44FE8A9560B26D1C260348AFA4ED8B820` |
| final superseding 31B private ZIP | `B6C8126034AE775157105A0343F627464AF1F1626B44584CA9140DA3B0D3B67D` |

## 31B Private Package Facts

- XML is full-project Tasker import: YES
- Task-only XML: NO
- Source 31A1 XML SHA256: `1C1FAF33EA30B69E8F35478AA8E93E58A2AA4ABB967CAA8F5EA927506BBF1B6E`
- Only task 224 changed: YES
- AutoSheets attempts maximum: `2`
- Final AutoSheets failure releases lock: YES
- Final AutoSheets failure closes AllowSend: YES
- Send authorization consumed into local latch before TextNow: YES
- Global `%AIW27BAllowSend` closed before TextNow and on every exit: YES
- Pre-Send `SENDING` write/readback before TextNow: YES
- Post-Send `SEND_CLICKED_AWAITING_CONFIRM` write: YES
- Task 224 `DONE` write: NO
- Task 224 final sent proof: NO
- AutoInput nodes changed: NO
- Current private key printed: NO
- Current private key changed: NO
- ZIP integrity: PASS
- Phone proof claimed for 31B: NO
- Phone import approved by Codex: NO
