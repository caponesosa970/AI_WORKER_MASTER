# Exact Changed Task And Action List

Existing runtime tasks changed: Task 225 only. New runtime task: Task 231 only. Project tids adds 231.

| Task | Action | Change |
| --- | --- | --- |
| 225 | base action 174 | Replace standalone TextNow Launch App with Task 231 call wrapper. |
| 225 | base action 175 | Replace standalone settle Wait with explicit `THREAD_NAV_READY` guard. |
| 225 | before base action 352 | Add ready-only wrapper close so navigation HOLD skips screen-read confirmation and still reaches common lock cleanup. |
| 231 | 0 | output: fail-closed default result |
| 231 | 1 | output: fail-closed default detail |
| 231 | 2 | input: bind normalized sender |
| 231 | 3 | control: initialize navigation gate |
| 231 | 4 | control: initialize UI failure flag |
| 231 | 5 | control: clear UI error |
| 231 | 6 | input: exact ten-digit sender required |
| 231 | 7 | input: invalid sender detail |
| 231 | 8 | input: block navigation |
| 231 | 9 | input: end sender validation |
| 231 | 10 | navigation: valid-input gate |
| 231 | 11 | navigation: bind exact Task 223 search variable |
| 231 | 12 | launch: clear err |
| 231 | 13 | launch: clear errmsg |
| 231 | 14 | Task 223 exact TextNow launch |
| 231 | 15 | Task 223 exact launch settle wait |
| 231 | 16 | launch: numeric error check |
| 231 | 17 | launch: mark failure |
| 231 | 18 | launch: preserve failure |
| 231 | 19 | launch: end error check |
| 231 | 20 | navigate-up: prior-step success gate |
| 231 | 21 | navigate-up: clear err |
| 231 | 22 | navigate-up: clear errmsg |
| 231 | 23 | Task 223 exact Navigate up AutoInput |
| 231 | 24 | Task 223 exact Navigate up settle wait |
| 231 | 25 | navigate-up: numeric error check |
| 231 | 26 | navigate-up: mark failure |
| 231 | 27 | navigate-up: preserve failure |
| 231 | 28 | navigate-up: end error check |
| 231 | 29 | navigate-up: end success gate |
| 231 | 30 | chats: prior-step success gate |
| 231 | 31 | chats: clear err |
| 231 | 32 | chats: clear errmsg |
| 231 | 33 | Task 223 exact Chats AutoInput |
| 231 | 34 | Task 223 exact Chats settle wait |
| 231 | 35 | chats: numeric error check |
| 231 | 36 | chats: mark failure |
| 231 | 37 | chats: preserve failure |
| 231 | 38 | chats: end error check |
| 231 | 39 | chats: end success gate |
| 231 | 40 | search: prior-step success gate |
| 231 | 41 | Task 223 exact search wrapper/action 484 |
| 231 | 42 | Task 223 exact search wrapper/action 485 |
| 231 | 43 | Task 223 exact search wrapper/action 486 |
| 231 | 44 | Task 223 exact search wrapper/action 487 |
| 231 | 45 | Task 223 exact search wrapper/action 488 |
| 231 | 46 | Task 223 exact search wrapper/action 489 |
| 231 | 47 | Task 223 exact search wrapper/action 490 |
| 231 | 48 | Task 223 exact search wrapper/action 491 |
| 231 | 49 | Task 223 exact search wrapper/action 492 |
| 231 | 50 | Task 223 exact search wrapper/action 493 |
| 231 | 51 | Task 223 exact search wrapper/action 494 |
| 231 | 52 | Task 223 exact search wrapper/action 495 |
| 231 | 53 | Task 223 exact search wrapper/action 496 |
| 231 | 54 | Task 223 exact search wrapper/action 497 |
| 231 | 55 | Task 223 exact search wrapper/action 498 |
| 231 | 56 | Task 223 exact search wrapper/action 499 |
| 231 | 57 | Task 223 exact search wrapper/action 500 |
| 231 | 58 | Task 223 exact search wrapper/action 501 |
| 231 | 59 | Task 223 exact search wrapper/action 502 |
| 231 | 60 | Task 223 exact search wrapper/action 503 |
| 231 | 61 | Task 223 exact search wrapper/action 504 |
| 231 | 62 | Task 223 exact search wrapper/action 505 |
| 231 | 63 | Task 223 exact search wrapper/action 506 |
| 231 | 64 | Task 223 exact search wrapper/action 507 |
| 231 | 65 | Task 223 exact search wrapper/action 508 |
| 231 | 66 | Task 223 exact search wrapper/action 509 |
| 231 | 67 | Task 223 exact search wrapper/action 510 |
| 231 | 68 | Task 223 exact search wrapper/action 511 |
| 231 | 69 | Task 223 exact search wrapper/action 512 |
| 231 | 70 | Task 223 exact search wrapper/action 513 |
| 231 | 71 | Task 223 exact search wrapper/action 514 |
| 231 | 72 | Task 223 exact search wrapper/action 515 |
| 231 | 73 | Task 223 exact search wrapper/action 516 |
| 231 | 74 | Task 223 exact search wrapper/action 517 |
| 231 | 75 | Task 223 exact search wrapper/action 518 |
| 231 | 76 | Task 223 exact search wrapper/action 519 |
| 231 | 77 | Task 223 exact search wrapper/action 520 |
| 231 | 78 | Task 223 exact search wrapper/action 521 |
| 231 | 79 | Task 223 exact search wrapper/action 522 |
| 231 | 80 | Task 223 exact search wrapper/action 523 |
| 231 | 81 | Task 223 exact search wrapper/action 524 |
| 231 | 82 | Task 223 exact search wrapper/action 525 |
| 231 | 83 | Task 223 exact search wrapper/action 526 |
| 231 | 84 | Task 223 exact search wrapper/action 527 |
| 231 | 85 | search: end success gate |
| 231 | 86 | contact: search-success gate |
| 231 | 87 | Task 223 exact search-write/contact wrapper/action 528 |
| 231 | 88 | Task 223 exact search-write/contact wrapper/action 529 |
| 231 | 89 | Task 223 exact search-write/contact wrapper/action 530 |
| 231 | 90 | Task 223 exact search-write/contact wrapper/action 531 |
| 231 | 91 | Task 223 exact search-write/contact wrapper/action 532 |
| 231 | 92 | Task 223 exact search-write/contact wrapper/action 533 |
| 231 | 93 | Task 223 exact search-write/contact wrapper/action 534 |
| 231 | 94 | Task 223 exact search-write/contact wrapper/action 535 |
| 231 | 95 | Task 223 exact search-write/contact wrapper/action 536 |
| 231 | 96 | Task 223 exact search-write/contact wrapper/action 537 |
| 231 | 97 | Task 223 exact search-write/contact wrapper/action 538 |
| 231 | 98 | Task 223 exact search-write/contact wrapper/action 539 |
| 231 | 99 | Task 223 exact search-write/contact wrapper/action 540 |
| 231 | 100 | Task 223 exact search-write/contact wrapper/action 541 |
| 231 | 101 | Task 223 exact search-write/contact wrapper/action 542 |
| 231 | 102 | Task 223 exact search-write/contact wrapper/action 543 |
| 231 | 103 | Task 223 exact search-write/contact wrapper/action 544 |
| 231 | 104 | Task 223 exact search-write/contact wrapper/action 545 |
| 231 | 105 | Task 223 exact search-write/contact wrapper/action 546 |
| 231 | 106 | Task 223 exact search-write/contact wrapper/action 547 |
| 231 | 107 | Task 223 exact search-write/contact wrapper/action 548 |
| 231 | 108 | contact: end search-success gate |
| 231 | 109 | post-contact: contact-success gate |
| 231 | 110 | Task 223 exact post-contact settle wait |
| 231 | 111 | post-contact: end contact-success gate |
| 231 | 112 | result: navigation success gate |
| 231 | 113 | result: exact navigation completed |
| 231 | 114 | result: clear error on success |
| 231 | 115 | result: navigation failed |
| 231 | 116 | result: explicit fail-closed result |
| 231 | 117 | result: preserve exact navigation error |
| 231 | 118 | result: end navigation result |
| 231 | 119 | navigation: end valid-input gate |
| 231 | 120 | terminal: return to Task 225 |
