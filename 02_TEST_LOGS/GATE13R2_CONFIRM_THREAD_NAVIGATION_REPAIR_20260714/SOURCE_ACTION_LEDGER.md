# Source Action Ledger

Authoritative runtime source: Task 223, `FINAL Send One Bound Row`, from the exact Gate 13R1 base.

Selected boundary:

- First source node: action 478, exact TextNow Launch App.
- Search/reset/retry lane: actions 484-527.
- Search text entry and contact selection: actions 528-548.
- Final included node: action 550, exact post-contact settle wait.
- Excluded: action 553 `MESSAGE_BOX` marker, action 554 compose-focus AutoInput, reply typing, Send, and all post-Send behavior.

The helper adds fail-closed wrapper checks but does not alter any copied source node except the output `sr` location.

| Source Task | Source Action | Output Action | Role | Exact excluding `sr` |
| --- | ---: | ---: | --- | --- |
| 223 | 478 | 14 | Task 223 exact TextNow launch | PASS |
| 223 | 479 | 15 | Task 223 exact launch settle wait | PASS |
| 223 | 480 | 23 | Task 223 exact Navigate up AutoInput | PASS |
| 223 | 481 | 24 | Task 223 exact Navigate up settle wait | PASS |
| 223 | 482 | 33 | Task 223 exact Chats AutoInput | PASS |
| 223 | 483 | 34 | Task 223 exact Chats settle wait | PASS |
| 223 | 484 | 41 | Task 223 exact search wrapper/action 484 | PASS |
| 223 | 485 | 42 | Task 223 exact search wrapper/action 485 | PASS |
| 223 | 486 | 43 | Task 223 exact search wrapper/action 486 | PASS |
| 223 | 487 | 44 | Task 223 exact search wrapper/action 487 | PASS |
| 223 | 488 | 45 | Task 223 exact search wrapper/action 488 | PASS |
| 223 | 489 | 46 | Task 223 exact search wrapper/action 489 | PASS |
| 223 | 490 | 47 | Task 223 exact search wrapper/action 490 | PASS |
| 223 | 491 | 48 | Task 223 exact search wrapper/action 491 | PASS |
| 223 | 492 | 49 | Task 223 exact search wrapper/action 492 | PASS |
| 223 | 493 | 50 | Task 223 exact search wrapper/action 493 | PASS |
| 223 | 494 | 51 | Task 223 exact search wrapper/action 494 | PASS |
| 223 | 495 | 52 | Task 223 exact search wrapper/action 495 | PASS |
| 223 | 496 | 53 | Task 223 exact search wrapper/action 496 | PASS |
| 223 | 497 | 54 | Task 223 exact search wrapper/action 497 | PASS |
| 223 | 498 | 55 | Task 223 exact search wrapper/action 498 | PASS |
| 223 | 499 | 56 | Task 223 exact search wrapper/action 499 | PASS |
| 223 | 500 | 57 | Task 223 exact search wrapper/action 500 | PASS |
| 223 | 501 | 58 | Task 223 exact search wrapper/action 501 | PASS |
| 223 | 502 | 59 | Task 223 exact search wrapper/action 502 | PASS |
| 223 | 503 | 60 | Task 223 exact search wrapper/action 503 | PASS |
| 223 | 504 | 61 | Task 223 exact search wrapper/action 504 | PASS |
| 223 | 505 | 62 | Task 223 exact search wrapper/action 505 | PASS |
| 223 | 506 | 63 | Task 223 exact search wrapper/action 506 | PASS |
| 223 | 507 | 64 | Task 223 exact search wrapper/action 507 | PASS |
| 223 | 508 | 65 | Task 223 exact search wrapper/action 508 | PASS |
| 223 | 509 | 66 | Task 223 exact search wrapper/action 509 | PASS |
| 223 | 510 | 67 | Task 223 exact search wrapper/action 510 | PASS |
| 223 | 511 | 68 | Task 223 exact search wrapper/action 511 | PASS |
| 223 | 512 | 69 | Task 223 exact search wrapper/action 512 | PASS |
| 223 | 513 | 70 | Task 223 exact search wrapper/action 513 | PASS |
| 223 | 514 | 71 | Task 223 exact search wrapper/action 514 | PASS |
| 223 | 515 | 72 | Task 223 exact search wrapper/action 515 | PASS |
| 223 | 516 | 73 | Task 223 exact search wrapper/action 516 | PASS |
| 223 | 517 | 74 | Task 223 exact search wrapper/action 517 | PASS |
| 223 | 518 | 75 | Task 223 exact search wrapper/action 518 | PASS |
| 223 | 519 | 76 | Task 223 exact search wrapper/action 519 | PASS |
| 223 | 520 | 77 | Task 223 exact search wrapper/action 520 | PASS |
| 223 | 521 | 78 | Task 223 exact search wrapper/action 521 | PASS |
| 223 | 522 | 79 | Task 223 exact search wrapper/action 522 | PASS |
| 223 | 523 | 80 | Task 223 exact search wrapper/action 523 | PASS |
| 223 | 524 | 81 | Task 223 exact search wrapper/action 524 | PASS |
| 223 | 525 | 82 | Task 223 exact search wrapper/action 525 | PASS |
| 223 | 526 | 83 | Task 223 exact search wrapper/action 526 | PASS |
| 223 | 527 | 84 | Task 223 exact search wrapper/action 527 | PASS |
| 223 | 528 | 87 | Task 223 exact search-write/contact wrapper/action 528 | PASS |
| 223 | 529 | 88 | Task 223 exact search-write/contact wrapper/action 529 | PASS |
| 223 | 530 | 89 | Task 223 exact search-write/contact wrapper/action 530 | PASS |
| 223 | 531 | 90 | Task 223 exact search-write/contact wrapper/action 531 | PASS |
| 223 | 532 | 91 | Task 223 exact search-write/contact wrapper/action 532 | PASS |
| 223 | 533 | 92 | Task 223 exact search-write/contact wrapper/action 533 | PASS |
| 223 | 534 | 93 | Task 223 exact search-write/contact wrapper/action 534 | PASS |
| 223 | 535 | 94 | Task 223 exact search-write/contact wrapper/action 535 | PASS |
| 223 | 536 | 95 | Task 223 exact search-write/contact wrapper/action 536 | PASS |
| 223 | 537 | 96 | Task 223 exact search-write/contact wrapper/action 537 | PASS |
| 223 | 538 | 97 | Task 223 exact search-write/contact wrapper/action 538 | PASS |
| 223 | 539 | 98 | Task 223 exact search-write/contact wrapper/action 539 | PASS |
| 223 | 540 | 99 | Task 223 exact search-write/contact wrapper/action 540 | PASS |
| 223 | 541 | 100 | Task 223 exact search-write/contact wrapper/action 541 | PASS |
| 223 | 542 | 101 | Task 223 exact search-write/contact wrapper/action 542 | PASS |
| 223 | 543 | 102 | Task 223 exact search-write/contact wrapper/action 543 | PASS |
| 223 | 544 | 103 | Task 223 exact search-write/contact wrapper/action 544 | PASS |
| 223 | 545 | 104 | Task 223 exact search-write/contact wrapper/action 545 | PASS |
| 223 | 546 | 105 | Task 223 exact search-write/contact wrapper/action 546 | PASS |
| 223 | 547 | 106 | Task 223 exact search-write/contact wrapper/action 547 | PASS |
| 223 | 548 | 107 | Task 223 exact search-write/contact wrapper/action 548 | PASS |
| 223 | 550 | 110 | Task 223 exact post-contact settle wait | PASS |
