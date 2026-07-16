# ChatGPT Artifact Audit Checklist

- [ ] Verify XML SHA `A7C577E6929E930938F0D48937332D19F441D2C1FFD9821E7047E397ECE74C07`.
- [ ] Verify ZIP SHA `6090E15356533E79F99B954437132515F62AB0073B5B4C035BEDCECB66FE6244`.
- [ ] Verify ZIP has one XML byte-equal to standalone.
- [ ] Verify topology 91 / 4 / 1 and all profiles disabled.
- [ ] Compare all 89 existing task blocks to the exact Gate 14C R1 base.
- [ ] Verify only Tasks 238 and 239 were added and registered once.
- [ ] Inspect authorization consumption and input/profile/STOP/lock guards.
- [ ] Inspect exact row formula 149-198 and count whitelist 5/10/25/50.
- [ ] Inspect fresh A:E precheck before every lock/write-capable processor call.
- [ ] Inspect one-row lock ownership and common release path.
- [ ] Inspect exact REVIEW_READY/Reply and ERROR_OPENAI_REVIEW readbacks.
- [ ] Verify no next row starts after HOLD or STOP.
- [ ] Verify no TextNow, Send, confirmation, DONE, Archive, Queue Cycle, profile, timer, or scene path.
- [ ] Keep phone import blocked until this exact artifact passes audit.
- [ ] Keep tracker at `13/14 locked = 93%` and 50 remaining checkpoints.
