# Exact Changed Task And Action List

Existing runtime tasks changed: 199 and 224.

New runtime task: 227.

Project registry change: Task 227 added to Project tids.

## Task 199

Action count: 180

| Action | Classified role |
| ---: | --- |
| 1 | mode: copy par1 |
| 2 | mode: trim par1 |
| 3 | mode: copy par2 |
| 4 | mode: trim par2 |
| 5 | mode: blank or unresolved par1 means production |
| 6 | mode: normalize production |
| 7 | mode: end production normalization |
| 8 | mode: unresolved par2 is blank |
| 9 | mode: clear unresolved par2 |
| 10 | mode: end par2 normalization |
| 11 | mode: initialize controlled flag |
| 12 | mode: initialize validity |
| 13 | mode: controlled token |
| 14 | mode: require ONE_CYCLE token |
| 15 | mode: reject controlled par2 |
| 16 | mode: controlled par2 valid |
| 17 | mode: mark controlled |
| 18 | mode: end controlled par2 check |
| 19 | mode: non-controlled token |
| 20 | mode: require production |
| 21 | mode: reject unknown token |
| 22 | mode: end production token check |
| 23 | mode: end controlled/production classification |
| 24 | mode: invalid token exit |
| 25 | mode: invalid token failure |
| 26 | mode: invalid token result |
| 27 | mode: invalid token error |
| 28 | mode: stop before busy ownership |
| 29 | mode: end invalid token exit |
| 30 | controlled entry: verify one-cycle latch |
| 31 | controlled entry: latch missing |
| 32 | controlled entry: latch failure |
| 33 | controlled entry: latch result |
| 34 | controlled entry: latch error |
| 35 | controlled entry: stop before router or busy |
| 36 | controlled entry: end latch check |
| 37 | controlled entry: consume latch before any read |
| 38 | controlled entry: end |
| 39 | production entry: preserve AIWorkerOn and watchdog |
| 40 | production entry: exact AIWorkerOn guard |
| 41 | production entry: exact stop when worker off |
| 42 | production entry: end worker-on guard |
| 43 | production entry: exact APP Watchdog Lite call |
| 44 | production entry: exact watchdog changed check |
| 45 | production entry: exact watchdog stop |
| 46 | production entry: end watchdog check |
| 47 | production entry: end production-only checks |
| 48 | busy: block existing owner |
| 49 | busy: controlled mode hold |
| 50 | busy: controlled blocked |
| 51 | busy: controlled failure |
| 52 | busy: controlled result |
| 53 | busy: controlled error |
| 54 | busy: production behavior |
| 55 | busy: preserve production KickPending |
| 56 | busy: end controlled/production behavior |
| 57 | busy: stop without releasing unowned busy |
| 58 | busy: end existing owner guard |
| 59 | maintenance: default off |
| 60 | maintenance: production-only frequency and watchdog |
| 61 | maintenance preflight: preserve source Task 199 action 12 |
| 62 | maintenance preflight: preserve source Task 199 action 13 |
| 63 | maintenance preflight: preserve source Task 199 action 14 |
| 64 | maintenance preflight: preserve source Task 199 action 15 |
| 65 | maintenance preflight: preserve source Task 199 action 16 |
| 66 | maintenance preflight: preserve source Task 199 action 17 |
| 67 | maintenance preflight: preserve source Task 199 action 18 |
| 68 | maintenance preflight: preserve source Task 199 action 19 |
| 69 | maintenance preflight: preserve source Task 199 action 20 |
| 70 | maintenance preflight: preserve source Task 199 action 21 |
| 71 | maintenance preflight: preserve source Task 199 action 22 |
| 72 | maintenance preflight: preserve source Task 199 action 23 |
| 73 | maintenance preflight: preserve source Task 199 action 24 |
| 74 | maintenance preflight: preserve source Task 199 action 25 |
| 75 | maintenance preflight: preserve source Task 199 action 26 |
| 76 | maintenance preflight: preserve source Task 199 action 27 |
| 77 | maintenance preflight: preserve source Task 199 action 28 |
| 78 | maintenance preflight: preserve source Task 199 action 29 |
| 79 | maintenance: end production-only preflight |
| 80 | busy: acquire ownership |
| 81 | busy: record local ownership |
| 82 | busy: clear prior kick on acquisition |
| 83 | cycle: start result |
| 84 | cycle: initialize continuation |
| 85 | cycle: initialize transition marker |
| 86 | cycle: initialize final result |
| 87 | router: call Task 227 exactly once before processing |
| 88 | router: capture route result |
| 89 | router: handled consumes the cycle |
| 90 | router: stop later work after handled |
| 91 | router: mark transition/block after handled |
| 92 | router: end handled handling |
| 93 | router: blocked consumes the cycle |
| 94 | router: stop later work after blocked |
| 95 | router: mark transition/block after blocked |
| 96 | router: end blocked handling |
| 97 | router: failed consumes the cycle |
| 98 | router: stop later work after failed |
| 99 | router: mark transition/block after failed |
| 100 | router: end failed handling |
| 101 | clear path: router permits process or Send |
| 102 | clear path: initialize normal production path |
| 103 | clear path: production processing only |
| 104 | production: preserve debug-only process |
| 105 | production: exact debug-only QUEUE Process If New |
| 106 | production: normal process path |
| 107 | production: mark normal path |
| 108 | production: preserve source Task 199 action 37 |
| 109 | production: preserve source Task 199 action 38 |
| 110 | production: preserve source Task 199 action 39 |
| 111 | production: preserve source Task 199 action 40 |
| 112 | production: preserve source Task 199 action 41 |
| 113 | production: preserve source Task 199 action 42 |
| 114 | production: preserve source Task 199 action 43 |
| 115 | production: preserve source Task 199 action 44 |
| 116 | production: preserve source Task 199 action 45 |
| 117 | production: preserve source Task 199 action 46 |
| 118 | production: preserve source Task 199 action 47 |
| 119 | production: preserve source Task 199 action 48 |
| 120 | production: preserve source Task 199 action 49 |
| 121 | production: preserve source Task 199 action 50 |
| 122 | production: preserve source Task 199 action 51 |
| 123 | production: preserve source Task 199 action 52 |
| 124 | production: preserve source Task 199 action 53 |
| 125 | production: preserve source Task 199 action 54 |
| 126 | production: preserve source Task 199 action 55 |
| 127 | production: preserve source Task 199 action 56 |
| 128 | production: preserve source Task 199 action 57 |
| 129 | production: preserve source Task 199 action 58 |
| 130 | production: preserve source Task 199 action 59 |
| 131 | production: preserve source Task 199 action 60 |
| 132 | production: preserve source Task 199 action 61 |
| 133 | production: preserve source Task 199 action 62 |
| 134 | production: preserve source Task 199 action 63 |
| 135 | production: preserve source Task 199 action 64 |
| 136 | production: preserve source Task 199 action 65 |
| 137 | production: preserve source Task 199 action 66 |
| 138 | production: preserve source Task 199 action 67 |
| 139 | production: preserve source Task 199 action 68 |
| 140 | production: end debug/normal path |
| 141 | clear path: end production processing |
| 142 | send selector: default blocked |
| 143 | send selector: controlled clear path authorization |
| 144 | send selector: controlled one-cycle allow |
| 145 | send selector: end controlled allow |
| 146 | send selector: production Safe Mode guard |
| 147 | send selector: production allow |
| 148 | send selector: end production allow |
| 149 | send selector: shared one Task 71 call node |
| 150 | send selector: exact FINAL Send Sheet call with QUEUE_CYCLE |
| 151 | send selector: capture selector/module result |
| 152 | send selector: any result except NO_READY ends transition chain |
| 153 | send selector: prevent same-chain confirmation or Archive |
| 154 | send selector: end transition marker |
| 155 | send selector: end shared call |
| 156 | maintenance: production-only no-transition path |
| 157 | maintenance: preserve FINAL Retry Error Rows |
| 158 | maintenance: preserve FINAL Review Ready Rows |
| 159 | maintenance: preserve source Task 199 action 84 |
| 160 | maintenance: preserve source Task 199 action 85 |
| 161 | maintenance: preserve source Task 199 action 86 |
| 162 | maintenance: preserve source Task 199 action 87 |
| 163 | maintenance: end production-only path |
| 164 | production: preserve normal cleanup variables |
| 165 | production: preserve AIWNextLogRow clear |
| 166 | production: preserve cleanup diagnostic |
| 167 | production: end normal cleanup |
| 168 | clear path: end |
| 169 | common epilogue: release only owned busy |
| 170 | common epilogue: save real final error |
| 171 | common epilogue: release AIWorkerBusy exactly once |
| 172 | common epilogue: clear ownership |
| 173 | common epilogue: restore real result |
| 174 | common epilogue: end owned release |
| 175 | recursion: production no-transition KickPending only |
| 176 | recursion: consume one pending kick |
| 177 | recursion: preserve bounded wait |
| 178 | recursion: preserve production self-call |
| 179 | recursion: end permitted production recursion |
| 180 | common epilogue: single final stop |

## Task 224

Action count: 11

| Action | Classified role |
| ---: | --- |
| 1 | launcher: require explicit one-cycle arm |
| 2 | launcher: not armed failure |
| 3 | launcher: not armed result |
| 4 | launcher: not armed error |
| 5 | launcher: stop without queue call |
| 6 | launcher: end arm guard |
| 7 | launcher: consume one-time authorization |
| 8 | launcher: arm one controlled queue invocation |
| 9 | launcher: call Task 199 exactly once |
| 10 | launcher: defensive latch cleanup after return |
| 11 | launcher: stop after one cycle |

## Task 227

Action count: 243

| Action | Classified role |
| ---: | --- |
| 1 | router entry: reset handled |
| 2 | router entry: reset blocked |
| 3 | router entry: reset failed |
| 4 | router entry: reset module |
| 5 | router entry: reset result |
| 6 | router entry: reset row |
| 7 | router entry: clear ID |
| 8 | router entry: clear error |
| 9 | router caller: require exact token |
| 10 | router caller: mark failure |
| 11 | router caller: deterministic result |
| 12 | router caller: error |
| 13 | router caller: stop without module or mutation |
| 14 | router caller: end token guard |
| 15 | router lock: inspect %AIWSending |
| 16 | router lock: block on %AIWSending |
| 17 | router lock: end %AIWSending |
| 18 | router lock: inspect %AIWConfirming |
| 19 | router lock: block on %AIWConfirming |
| 20 | router lock: end %AIWConfirming |
| 21 | router lock: inspect %AIWArchiving |
| 22 | router lock: block on %AIWArchiving |
| 23 | router lock: end %AIWArchiving |
| 24 | router lock: inspect %AIWProcessing |
| 25 | router lock: block on %AIWProcessing |
| 26 | router lock: end %AIWProcessing |
| 27 | router lock: inspect %AIWDeadArchiving |
| 28 | router lock: block on %AIWDeadArchiving |
| 29 | router lock: end %AIWDeadArchiving |
| 30 | router lock: inspect %AIWCompacting |
| 31 | router lock: block on %AIWCompacting |
| 32 | router lock: end %AIWCompacting |
| 33 | router lock: any active transaction lock |
| 34 | router lock: deterministic result |
| 35 | router lock: error |
| 36 | router lock: stop without releasing unowned lock |
| 37 | router lock: end blocked exit |
| 38 | router QueueView read: exact Task 71 source action |
| 39 | router QueueView read: exact Task 71 source action |
| 40 | router QueueView read: exact Task 71 source action |
| 41 | router QueueView read: exact Task 71 source action |
| 42 | router QueueView read: exact Task 71 source action |
| 43 | router QueueView read: exact Task 71 source action |
| 44 | router QueueView read: exact Task 71 source action |
| 45 | router QueueView read: exact Task 71 source action |
| 46 | router QueueView read: exact Task 71 source action |
| 47 | router QueueView read: exact Task 71 source action |
| 48 | router QueueView read: exact Task 71 source action |
| 49 | router QueueView read: exact Task 71 source action |
| 50 | router QueueView read: exact Task 71 source action |
| 51 | router QueueView read: exact Task 71 source action |
| 52 | router QueueView read: exact Task 71 source action |
| 53 | router QueueView read: exact Task 71 source action |
| 54 | router QueueView read: exact Task 71 source action |
| 55 | router QueueView read: exact Task 71 source action |
| 56 | router QueueView read: exact Task 71 source action |
| 57 | router QueueView read: exact Task 71 source action |
| 58 | router QueueView read: exact Task 71 source action |
| 59 | router QueueView read: exact Task 71 source action |
| 60 | router QueueView read: exact Task 71 source action |
| 61 | router QueueView read: exact Task 71 source action |
| 62 | router QueueView read: exact Task 71 source action |
| 63 | router QueueView read: exact Task 71 source action |
| 64 | router QueueView read: exact Task 71 source action |
| 65 | router QueueView read: exact Task 71 source action |
| 66 | router QueueView read: exact Task 71 source action |
| 67 | router QueueView read: exact Task 71 source action |
| 68 | router QueueView read: exact Task 71 source action |
| 69 | router QueueView read: exact Task 71 source action |
| 70 | router QueueView read: exact Task 71 source action |
| 71 | router QueueView read: exact Task 71 source action |
| 72 | router QueueView read: exact Task 71 source action |
| 73 | router QueueView read: exact Task 71 source action |
| 74 | router QueueView read: exact Task 71 source action |
| 75 | router QueueView read: exact Task 71 source action |
| 76 | router QueueView read: exact Task 71 source action |
| 77 | router QueueView read: exact Task 71 source action |
| 78 | router QueueView read: exact Task 71 source action |
| 79 | router QueueView read: exact Task 71 source action |
| 80 | router QueueView read: exact Task 71 source action |
| 81 | router QueueView read: exact Task 71 source action |
| 82 | router QueueView read: exact Task 71 source action |
| 83 | router QueueView read: exact Task 71 source action |
| 84 | router QueueView read: exact Task 71 source action |
| 85 | router QueueView read: exact Task 71 source action |
| 86 | router QueueView read: exact Task 71 source action |
| 87 | router QueueView read: exact Task 71 source action |
| 88 | router QueueView read: exact Task 71 source action |
| 89 | router QueueView read: exact Task 71 source action |
| 90 | router QueueView read: exact Task 71 source action |
| 91 | router QueueView read: exact Task 71 source action |
| 92 | router QueueView read: exact Task 71 source action |
| 93 | router QueueView read: exact Task 71 source action |
| 94 | router QueueView read: exact Task 71 source action |
| 95 | router QueueView read: exact Task 71 source action |
| 96 | router QueueView read: exact Task 71 source action |
| 97 | router QueueView read: exact Task 71 source action |
| 98 | router QueueView read: exact Task 71 source action |
| 99 | router QueueView read: exact Task 71 source action |
| 100 | router QueueView read: exact Task 71 source action |
| 101 | router QueueView read: exact Task 71 source action |
| 102 | router QueueView read: exact Task 71 source action |
| 103 | router QueueView read: exact Task 71 source action |
| 104 | router QueueView read: exact Task 71 source action |
| 105 | router QueueView read: exact Task 71 source action |
| 106 | router QueueView read: exact Task 71 source action |
| 107 | router QueueView read: exact Task 71 source action |
| 108 | router QueueView read: exact Task 71 source action |
| 109 | router QueueView read: exact Task 71 source action |
| 110 | router QueueView read: exact Task 71 source action |
| 111 | router QueueView read: exact Task 71 source action |
| 112 | router QueueView read: exact Task 71 source action |
| 113 | router QueueView read: exact Task 71 source action |
| 114 | router QueueView read: exact Task 71 source action |
| 115 | router QueueView read: exact Task 71 source action |
| 116 | router QueueView read: exact Task 71 source action |
| 117 | router QueueView read: exact Task 71 source action |
| 118 | router QueueView read: exact Task 71 source action |
| 119 | router QueueView read: exact Task 71 source action |
| 120 | router QueueView read: exact Task 71 source action |
| 121 | router QueueView read: exact Task 71 source action |
| 122 | router QueueView read: exact Task 71 source action |
| 123 | router QueueView read: exact Task 71 source action |
| 124 | router QueueView read: exact Task 71 source action |
| 125 | router QueueView read: exact Task 71 source action |
| 126 | router QueueView read: exact Task 71 source action |
| 127 | router QueueView read: exact Task 71 source action |
| 128 | router QueueView read: exact Task 71 source action |
| 129 | router QueueView read: exact Task 71 source action |
| 130 | router QueueView read: exact Task 71 source action |
| 131 | router QueueView read: exact Task 71 source action |
| 132 | router QueueView read: exact Task 71 source action |
| 133 | router QueueView read: exact Task 71 source action |
| 134 | router QueueView read: exact Task 71 source action |
| 135 | router QueueView read: exact Task 71 source action |
| 136 | router QueueView read: exact Task 71 source action |
| 137 | router QueueView read: exact Task 71 source action |
| 138 | router QueueView read: exact Task 71 source action |
| 139 | router QueueView read: exact Task 71 source action |
| 140 | router QueueView read: exact Task 71 source action |
| 141 | router QueueView read: both attempts failed |
| 142 | router QueueView read: mark failure |
| 143 | router QueueView read: deterministic result |
| 144 | router QueueView read: preserve error |
| 145 | router QueueView read: stop without module |
| 146 | router QueueView read: end failure |
| 147 | router scan: initialize index |
| 148 | router scan: initialize invalid binding count |
| 149 | router scan: initialize awaiting count |
| 150 | router scan: initialize dangerous count |
| 151 | router scan: initialize DONE count |
| 152 | router scan: initialize lowest DONE row |
| 153 | router scan: initialize awaiting row |
| 154 | router scan: clear awaiting ID |
| 155 | router scan: clear DONE ID |
| 156 | router scan: inspect every QueueView status |
| 157 | router scan: advance aligned array index |
| 158 | router scan: bind candidate SourceRow |
| 159 | router scan: bind candidate ID |
| 160 | router scan: unresolved or error status |
| 161 | router scan: block invalid status binding |
| 162 | router scan: end invalid status |
| 163 | router scan: lifecycle-relevant row |
| 164 | router scan: provisional binding valid |
| 165 | router scan: SourceRow must be 2 through 201 |
| 166 | router scan: invalidate SourceRow |
| 167 | router scan: end SourceRow validation |
| 168 | router scan: ID must be usable |
| 169 | router scan: invalidate ID |
| 170 | router scan: end ID validation |
| 171 | router scan: invalid lifecycle binding |
| 172 | router scan: remember invalid binding |
| 173 | router scan: valid lifecycle binding |
| 174 | router scan: awaiting confirmation |
| 175 | router scan: count awaiting confirmation |
| 176 | router scan: bind awaiting row |
| 177 | router scan: bind awaiting ID |
| 178 | router scan: end awaiting classification |
| 179 | router scan: dangerous unresolved state |
| 180 | router scan: count dangerous unresolved state |
| 181 | router scan: end dangerous classification |
| 182 | router scan: DONE Archive candidate |
| 183 | router scan: count DONE candidate |
| 184 | router scan: first DONE candidate |
| 185 | router scan: initialize lowest DONE SourceRow |
| 186 | router scan: initialize lowest DONE ID |
| 187 | router scan: later DONE candidate |
| 188 | router scan: numeric SourceRow lower than current |
| 189 | router scan: replace lowest DONE SourceRow |
| 190 | router scan: replace lowest DONE ID |
| 191 | router scan: end lower DONE comparison |
| 192 | router scan: end first/later DONE selection |
| 193 | router scan: end DONE classification |
| 194 | router scan: end valid binding branch |
| 195 | router scan: end lifecycle-relevant row |
| 196 | router scan: complete full QueueView scan |
| 197 | router decision: invalid lifecycle binding |
| 198 | router decision: block invalid binding |
| 199 | router decision: invalid binding result |
| 200 | router decision: invalid binding error |
| 201 | router decision: stop after invalid binding |
| 202 | router decision: end invalid binding |
| 203 | router priority 1: more than one awaiting row |
| 204 | router priority 1: block multiple awaiting |
| 205 | router priority 1: result |
| 206 | router priority 1: error |
| 207 | router priority 1: stop without module |
| 208 | router priority 1: end |
| 209 | router priority 2: dangerous unresolved state exists |
| 210 | router priority 2: block unresolved state |
| 211 | router priority 2: result |
| 212 | router priority 2: error |
| 213 | router priority 2: stop without module |
| 214 | router priority 2: end |
| 215 | router priority 3: exactly one awaiting row |
| 216 | router priority 3: consume cycle before confirmation call |
| 217 | router priority 3: module |
| 218 | router priority 3: route row |
| 219 | router priority 3: route ID |
| 220 | router priority 3: call Task 225 exactly once |
| 221 | router priority 3: copy module result |
| 222 | router priority 3: copy module failure |
| 223 | router priority 3: copy module blocked |
| 224 | router priority 3: copy module error |
| 225 | router priority 3: stop after one module |
| 226 | router priority 3: end |
| 227 | router priority 4: one or more DONE rows |
| 228 | router priority 4: consume cycle before Archive call |
| 229 | router priority 4: module |
| 230 | router priority 4: lowest numeric SourceRow |
| 231 | router priority 4: exact ID |
| 232 | router priority 4: call Task 226 exactly once |
| 233 | router priority 4: copy module result |
| 234 | router priority 4: copy module failure |
| 235 | router priority 4: copy module blocked |
| 236 | router priority 4: copy module error |
| 237 | router priority 4: stop after one module |
| 238 | router priority 4: end |
| 239 | router priority 5: no pending lifecycle state |
| 240 | router priority 5: leave cycle unhandled |
| 241 | router priority 5: leave cycle unblocked |
| 242 | router priority 5: leave cycle successful |
| 243 | router priority 5: return clear to Task 199 |

Unclassified changed tasks: 0.

Unclassified actions in Tasks 199, 224, and 227: 0.
