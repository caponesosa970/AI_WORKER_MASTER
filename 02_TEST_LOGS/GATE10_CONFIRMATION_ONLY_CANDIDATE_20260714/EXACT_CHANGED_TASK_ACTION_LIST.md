# Exact Changed Task And Action List

Only Task 224 is replaced and Task 225 is added. Project `tids` adds 225. Every other task node is raw-byte identical.

## Task 224: AIW GATE10 CONTROLLED CONFIRM TEST

| Action | Type | Purpose |
| ---: | --- | --- |
| 0 | If | launcher: require explicit one-time arm |
| 1 | Variable Set | launcher: not armed failure |
| 2 | Variable Set | launcher: not armed result |
| 3 | Variable Set | launcher: not armed error |
| 4 | Stop | launcher: stop without worker call |
| 5 | End If | launcher: end arm check |
| 6 | Variable Set | launcher: consume one-time authorization |
| 7 | Perform Task | launcher: call permanent confirmation worker exactly once |
| 8 | Stop | launcher: stop after one worker call |

## Task 225: FINAL Confirm One Bound Row

| Action | Type | Purpose |
| ---: | --- | --- |
| 0 | Variable Set | input: copy source row |
| 1 | Variable Set | input: copy expected ID |
| 2 | Variable Search Replace | input: normalize source row |
| 3 | Variable Search Replace | input: normalize expected ID |
| 4 | If | guard: source row must be numeric |
| 5 | Variable Set | guard: parameter failure flag |
| 6 | Variable Set | guard: invalid row result |
| 7 | Variable Set | guard: invalid row error |
| 8 | Stop | guard: stop before lock and UI |
| 9 | End If | guard: end numeric row check |
| 10 | If | guard: source row must exceed header |
| 11 | Variable Set | guard: header row failure flag |
| 12 | Variable Set | guard: header row result |
| 13 | Variable Set | guard: header row error |
| 14 | Stop | guard: stop before lock and UI |
| 15 | End If | guard: end header row check |
| 16 | If | guard: expected ID must be concrete |
| 17 | Variable Set | guard: expected ID failure flag |
| 18 | Variable Set | guard: expected ID result |
| 19 | Variable Set | guard: expected ID error |
| 20 | Stop | guard: stop before lock and UI |
| 21 | End If | guard: end expected ID check |
| 22 | If | lock: block concurrent confirmation |
| 23 | Variable Set | lock: blocked flag |
| 24 | Variable Set | lock: blocked failure flag |
| 25 | Variable Set | lock: blocked result |
| 26 | Variable Set | lock: blocked error |
| 27 | Stop | lock: stop without releasing foreign lock |
| 28 | End If | lock: end busy check |
| 29 | Variable Set | lock: acquire dedicated confirmation lock |
| 30 | Variable Set | lock: record acquisition time |
| 31 | Variable Set | lock: record local ownership |
| 32 | Variable Set | flow: enable transaction |
| 33 | Variable Set | result: default failed false |
| 34 | Variable Set | result: default blocked false |
| 35 | Variable Set | result: start marker |
| 36 | Variable Set | result: exact source row |
| 37 | If | row read: enter |
| 38 | Variable Clear | row read attempt 1: clear confirm_id |
| 39 | Variable Clear | row read attempt 1: clear confirm_sender |
| 40 | Variable Clear | row read attempt 1: clear confirm_message |
| 41 | Variable Clear | row read attempt 1: clear confirm_status |
| 42 | Variable Clear | row read attempt 1: clear confirm_reply |
| 43 | Variable Clear | row read attempt 1: clear err |
| 44 | Variable Clear | row read attempt 1: clear errmsg |
| 45 | AutoSheets plugin action | row read: AutoSheets Get Data attempt 1 |
| 46 | If | row read: immediate numeric error check attempt 1 |
| 47 | Variable Set | row read: save combined plugin error attempt 1 |
| 48 | Variable Set | row read: plugin attempt 1 failed |
| 49 | Else | row read: no numeric plugin error attempt 1 |
| 50 | Variable Set | row read: plugin attempt 1 returned |
| 51 | End If | row read: end immediate error check attempt 1 |
| 52 | If | row read: validate attempt 1 outputs |
| 53 | If | row read attempt 1: confirm_id count must equal one |
| 54 | Variable Set | row read attempt 1: invalidate count |
| 55 | End If | row read attempt 1: end count check |
| 56 | If | row read attempt 1: confirm_id value validity |
| 57 | Variable Set | row read attempt 1: invalidate value |
| 58 | End If | row read attempt 1: end value check |
| 59 | If | row read attempt 1: confirm_sender count must equal one |
| 60 | Variable Set | row read attempt 1: invalidate count |
| 61 | End If | row read attempt 1: end count check |
| 62 | If | row read attempt 1: confirm_sender value validity |
| 63 | Variable Set | row read attempt 1: invalidate value |
| 64 | End If | row read attempt 1: end value check |
| 65 | If | row read attempt 1: confirm_status count must equal one |
| 66 | Variable Set | row read attempt 1: invalidate count |
| 67 | End If | row read attempt 1: end count check |
| 68 | If | row read attempt 1: confirm_status value validity |
| 69 | Variable Set | row read attempt 1: invalidate value |
| 70 | End If | row read attempt 1: end value check |
| 71 | If | row read attempt 1: confirm_reply count must equal one |
| 72 | Variable Set | row read attempt 1: invalidate count |
| 73 | End If | row read attempt 1: end count check |
| 74 | If | row read attempt 1: confirm_reply value validity |
| 75 | Variable Set | row read attempt 1: invalidate value |
| 76 | End If | row read attempt 1: end value check |
| 77 | End If | row read: end output validation attempt 1 |
| 78 | If | row read: retry only after first failure |
| 79 | Wait | row read: exact three second retry wait |
| 80 | Variable Clear | row read attempt 2: clear confirm_id |
| 81 | Variable Clear | row read attempt 2: clear confirm_sender |
| 82 | Variable Clear | row read attempt 2: clear confirm_message |
| 83 | Variable Clear | row read attempt 2: clear confirm_status |
| 84 | Variable Clear | row read attempt 2: clear confirm_reply |
| 85 | Variable Clear | row read attempt 2: clear err |
| 86 | Variable Clear | row read attempt 2: clear errmsg |
| 87 | AutoSheets plugin action | row read: AutoSheets Get Data attempt 2 |
| 88 | If | row read: immediate numeric error check attempt 2 |
| 89 | Variable Set | row read: save combined plugin error attempt 2 |
| 90 | Variable Set | row read: plugin attempt 2 failed |
| 91 | Else | row read: no numeric plugin error attempt 2 |
| 92 | Variable Set | row read: plugin attempt 2 returned |
| 93 | End If | row read: end immediate error check attempt 2 |
| 94 | If | row read: validate attempt 2 outputs |
| 95 | If | row read attempt 2: confirm_id count must equal one |
| 96 | Variable Set | row read attempt 2: invalidate count |
| 97 | End If | row read attempt 2: end count check |
| 98 | If | row read attempt 2: confirm_id value validity |
| 99 | Variable Set | row read attempt 2: invalidate value |
| 100 | End If | row read attempt 2: end value check |
| 101 | If | row read attempt 2: confirm_sender count must equal one |
| 102 | Variable Set | row read attempt 2: invalidate count |
| 103 | End If | row read attempt 2: end count check |
| 104 | If | row read attempt 2: confirm_sender value validity |
| 105 | Variable Set | row read attempt 2: invalidate value |
| 106 | End If | row read attempt 2: end value check |
| 107 | If | row read attempt 2: confirm_status count must equal one |
| 108 | Variable Set | row read attempt 2: invalidate count |
| 109 | End If | row read attempt 2: end count check |
| 110 | If | row read attempt 2: confirm_status value validity |
| 111 | Variable Set | row read attempt 2: invalidate value |
| 112 | End If | row read attempt 2: end value check |
| 113 | If | row read attempt 2: confirm_reply count must equal one |
| 114 | Variable Set | row read attempt 2: invalidate count |
| 115 | End If | row read attempt 2: end count check |
| 116 | If | row read attempt 2: confirm_reply value validity |
| 117 | Variable Set | row read attempt 2: invalidate value |
| 118 | End If | row read attempt 2: end value check |
| 119 | End If | row read: end output validation attempt 2 |
| 120 | End If | row read: end one-retry wrapper |
| 121 | If | row read: final failure |
| 122 | Variable Set | row read: failure flag |
| 123 | Variable Set | row read: failure result |
| 124 | Variable Set | row read: final error |
| 125 | Variable Set | row read: stop flow |
| 126 | End If | row read: end final failure |
| 127 | End If | row read: exit |
| 128 | If | binding: enter |
| 129 | Variable Set | binding: ID |
| 130 | Variable Set | binding: sender |
| 131 | Variable Set | binding: status |
| 132 | Variable Set | binding: exact reply |
| 133 | Variable Search Replace | binding: normalize ID |
| 134 | Variable Search Replace | binding: normalize sender |
| 135 | Variable Search Replace | binding: normalize status |
| 136 | Variable Search Replace | binding: normalize reply boundaries |
| 137 | If | binding: exact ID mismatch |
| 138 | Variable Set | binding: mismatch failure |
| 139 | Variable Set | binding: mismatch result |
| 140 | Variable Set | binding: mismatch error |
| 141 | Variable Set | binding: stop on mismatch |
| 142 | End If | binding: end ID mismatch |
| 143 | If | binding: exact status check |
| 144 | Variable Set | binding: wrong status failure |
| 145 | Variable Set | binding: wrong status result |
| 146 | Variable Set | binding: wrong status error |
| 147 | Variable Set | binding: stop on wrong status |
| 148 | End If | binding: end status check |
| 149 | If | binding: sender validity |
| 150 | Variable Set | binding: invalid sender failure |
| 151 | Variable Set | binding: invalid sender result |
| 152 | Variable Set | binding: invalid sender error |
| 153 | Variable Set | binding: stop on invalid sender |
| 154 | End If | binding: end sender check |
| 155 | If | binding: reply validity |
| 156 | Variable Set | binding: invalid reply failure |
| 157 | Variable Set | binding: invalid reply result |
| 158 | Variable Set | binding: invalid reply error |
| 159 | Variable Set | binding: stop on invalid reply |
| 160 | End If | binding: end reply check |
| 161 | Variable Set | identity: sender digit candidate |
| 162 | Variable Search Replace | identity: remove sender formatting |
| 163 | If | identity: remove leading country code only |
| 164 | Variable Search Replace | identity: strip leading country code |
| 165 | End If | identity: end country code normalization |
| 166 | If | identity: normalized sender must be ten digits |
| 167 | Variable Set | identity: sender normalization failure |
| 168 | Variable Set | identity: invalid sender result |
| 169 | Variable Set | identity: invalid sender error |
| 170 | Variable Set | identity: stop on invalid normalized sender |
| 171 | End If | identity: end normalized sender check |
| 172 | End If | binding: exit |
| 173 | If | screen confirmation: enter |
| 174 | Launch App | screen confirmation: exact Plan A TextNow launch |
| 175 | Wait | screen confirmation: exact source settle wait |
| 176 | Variable Clear | screen confirmation: clear text output |
| 177 | Variable Clear | screen confirmation: clear package output |
| 178 | Variable Clear | screen confirmation: clear err |
| 179 | Variable Clear | screen confirmation: clear errmsg |
| 180 | Get Screen Info (Assistant) | screen confirmation: exact phone-exported Get Screen Info Assistant |
| 181 | If | screen confirmation: immediate screen-read error check |
| 182 | Variable Set | screen confirmation: preserve screen-read error |
| 183 | Variable Set | screen confirmation: error failure flag |
| 184 | Variable Set | screen confirmation: screen-read failure result |
| 185 | Variable Set | screen confirmation: screen-read failure error |
| 186 | Variable Set | screen confirmation: stop after action error |
| 187 | End If | screen confirmation: end screen-read error check |
| 188 | If | screen confirmation: exact package check |
| 189 | Variable Set | screen confirmation: wrong package failure |
| 190 | Variable Set | screen confirmation: wrong package result |
| 191 | Variable Set | screen confirmation: wrong package error |
| 192 | Variable Set | screen confirmation: stop on wrong package |
| 193 | End If | screen confirmation: end exact package check |
| 194 | If | screen confirmation: raw JSON validity |
| 195 | Variable Set | screen confirmation: malformed data failure |
| 196 | Variable Set | screen confirmation: malformed data result |
| 197 | Variable Set | screen confirmation: malformed data error |
| 198 | Variable Set | screen confirmation: stop on malformed data |
| 199 | End If | screen confirmation: end raw JSON validity |
| 200 | If | screen confirmation: parse ordered text array |
| 201 | Variable Set | screen confirmation: native structured JSON text count |
| 202 | If | screen confirmation: structured count must resolve |
| 203 | Variable Set | screen confirmation: structured parse failure |
| 204 | Variable Set | screen confirmation: unresolved structured data result |
| 205 | Variable Set | screen confirmation: unresolved structured data error |
| 206 | Variable Set | screen confirmation: stop on unresolved structure |
| 207 | End If | screen confirmation: end structured count check |
| 208 | End If | screen confirmation: end parse gate |
| 209 | If | screen confirmation: evaluate exact ordered elements |
| 210 | Variable Set | screen confirmation: identity default false |
| 211 | Variable Set | screen confirmation: exact reply count zero |
| 212 | Variable Set | screen confirmation: adjacency pending false |
| 213 | Variable Set | screen confirmation: adjacency default false |
| 214 | Variable Set | screen confirmation: adjacency failure default false |
| 215 | For | screen confirmation: ordered native JSON text loop |
| 216 | Variable Set | screen confirmation: identity candidate |
| 217 | Variable Search Replace | screen confirmation: normalize visible digits |
| 218 | If | screen confirmation: visible country code check |
| 219 | Variable Search Replace | screen confirmation: strip visible country code |
| 220 | End If | screen confirmation: end visible country code check |
| 221 | If | screen confirmation: exact normalized sender identity |
| 222 | Variable Set | screen confirmation: identity positively matched |
| 223 | End If | screen confirmation: end sender identity match |
| 224 | If | screen confirmation: non-empty ordered element |
| 225 | If | screen confirmation: inspect immediate non-empty successor |
| 226 | If | screen confirmation: exact Sent adjacency |
| 227 | Variable Set | screen confirmation: exact adjacency passed |
| 228 | Else | screen confirmation: successor is not Sent |
| 229 | Variable Set | screen confirmation: adjacency failed |
| 230 | End If | screen confirmation: end exact Sent comparison |
| 231 | Variable Set | screen confirmation: consume adjacency expectation |
| 232 | End If | screen confirmation: end successor inspection |
| 233 | If | screen confirmation: exact complete reply element |
| 234 | Variable Add | screen confirmation: increment exact reply count |
| 235 | Variable Set | screen confirmation: require next non-empty Sent |
| 236 | End If | screen confirmation: end exact reply match |
| 237 | End If | screen confirmation: end non-empty element |
| 238 | End For | screen confirmation: end ordered JSON loop |
| 239 | Variable Set | screen confirmation: positive default false |
| 240 | If | screen confirmation: exact identity unique reply and immediate Sent gate |
| 241 | Variable Set | screen confirmation: all positive checks passed |
| 242 | End If | screen confirmation: end positive gate |
| 243 | If | screen confirmation: uncertainty hold |
| 244 | Variable Set | screen confirmation: uncertainty failure flag |
| 245 | Variable Set | screen confirmation: uncertainty result |
| 246 | Variable Set | screen confirmation: uncertainty error |
| 247 | Variable Set | screen confirmation: stop before DONE |
| 248 | End If | screen confirmation: end uncertainty hold |
| 249 | End If | screen confirmation: end exact evaluation |
| 250 | End If | screen confirmation: exit |
| 251 | If | DONE: positive confirmation only |
| 252 | Variable Clear | DONE update attempt 1: clear err |
| 253 | Variable Clear | DONE update attempt 1: clear errmsg |
| 254 | AutoSheets plugin action | DONE update: AutoSheets Update Data attempt 1 |
| 255 | If | DONE update: immediate numeric error check attempt 1 |
| 256 | Variable Set | DONE update: save combined plugin error attempt 1 |
| 257 | Variable Set | DONE update: update attempt 1 failed |
| 258 | Else | DONE update: no numeric update error attempt 1 |
| 259 | Variable Set | DONE update: update attempt 1 returned |
| 260 | End If | DONE update: end immediate error check attempt 1 |
| 261 | If | DONE update: retry only after first failure |
| 262 | Wait | DONE update: exact three second retry wait |
| 263 | Variable Clear | DONE update attempt 2: clear err |
| 264 | Variable Clear | DONE update attempt 2: clear errmsg |
| 265 | AutoSheets plugin action | DONE update: AutoSheets Update Data attempt 2 |
| 266 | If | DONE update: immediate numeric error check attempt 2 |
| 267 | Variable Set | DONE update: save combined plugin error attempt 2 |
| 268 | Variable Set | DONE update: update attempt 2 failed |
| 269 | Else | DONE update: no numeric update error attempt 2 |
| 270 | Variable Set | DONE update: update attempt 2 returned |
| 271 | End If | DONE update: end immediate error check attempt 2 |
| 272 | End If | DONE update: end one-retry wrapper |
| 273 | If | DONE: update failed twice |
| 274 | Variable Set | DONE: update failure flag |
| 275 | Variable Set | DONE: update failure result |
| 276 | Variable Set | DONE: update failure error |
| 277 | Variable Set | DONE: stop after update failure |
| 278 | End If | DONE: end update failure |
| 279 | If | DONE: exact readback only after update returned |
| 280 | Variable Clear | DONE readback attempt 1: clear done_verify_id |
| 281 | Variable Clear | DONE readback attempt 1: clear done_verify_sender |
| 282 | Variable Clear | DONE readback attempt 1: clear done_verify_message |
| 283 | Variable Clear | DONE readback attempt 1: clear done_verify_status |
| 284 | Variable Clear | DONE readback attempt 1: clear err |
| 285 | Variable Clear | DONE readback attempt 1: clear errmsg |
| 286 | AutoSheets plugin action | DONE readback: AutoSheets Get Data attempt 1 |
| 287 | If | DONE readback: immediate numeric error check attempt 1 |
| 288 | Variable Set | DONE readback: save combined plugin error attempt 1 |
| 289 | Variable Set | DONE readback: plugin attempt 1 failed |
| 290 | Else | DONE readback: no numeric plugin error attempt 1 |
| 291 | Variable Set | DONE readback: plugin attempt 1 returned |
| 292 | End If | DONE readback: end immediate error check attempt 1 |
| 293 | If | DONE readback: validate attempt 1 outputs |
| 294 | If | DONE readback attempt 1: done_verify_id count must equal one |
| 295 | Variable Set | DONE readback attempt 1: invalidate count |
| 296 | End If | DONE readback attempt 1: end count check |
| 297 | If | DONE readback attempt 1: done_verify_id value validity |
| 298 | Variable Set | DONE readback attempt 1: invalidate value |
| 299 | End If | DONE readback attempt 1: end value check |
| 300 | If | DONE readback attempt 1: done_verify_status count must equal one |
| 301 | Variable Set | DONE readback attempt 1: invalidate count |
| 302 | End If | DONE readback attempt 1: end count check |
| 303 | If | DONE readback attempt 1: done_verify_status value validity |
| 304 | Variable Set | DONE readback attempt 1: invalidate value |
| 305 | End If | DONE readback attempt 1: end value check |
| 306 | End If | DONE readback: end output validation attempt 1 |
| 307 | If | DONE readback: retry only after first failure |
| 308 | Wait | DONE readback: exact three second retry wait |
| 309 | Variable Clear | DONE readback attempt 2: clear done_verify_id |
| 310 | Variable Clear | DONE readback attempt 2: clear done_verify_sender |
| 311 | Variable Clear | DONE readback attempt 2: clear done_verify_message |
| 312 | Variable Clear | DONE readback attempt 2: clear done_verify_status |
| 313 | Variable Clear | DONE readback attempt 2: clear err |
| 314 | Variable Clear | DONE readback attempt 2: clear errmsg |
| 315 | AutoSheets plugin action | DONE readback: AutoSheets Get Data attempt 2 |
| 316 | If | DONE readback: immediate numeric error check attempt 2 |
| 317 | Variable Set | DONE readback: save combined plugin error attempt 2 |
| 318 | Variable Set | DONE readback: plugin attempt 2 failed |
| 319 | Else | DONE readback: no numeric plugin error attempt 2 |
| 320 | Variable Set | DONE readback: plugin attempt 2 returned |
| 321 | End If | DONE readback: end immediate error check attempt 2 |
| 322 | If | DONE readback: validate attempt 2 outputs |
| 323 | If | DONE readback attempt 2: done_verify_id count must equal one |
| 324 | Variable Set | DONE readback attempt 2: invalidate count |
| 325 | End If | DONE readback attempt 2: end count check |
| 326 | If | DONE readback attempt 2: done_verify_id value validity |
| 327 | Variable Set | DONE readback attempt 2: invalidate value |
| 328 | End If | DONE readback attempt 2: end value check |
| 329 | If | DONE readback attempt 2: done_verify_status count must equal one |
| 330 | Variable Set | DONE readback attempt 2: invalidate count |
| 331 | End If | DONE readback attempt 2: end count check |
| 332 | If | DONE readback attempt 2: done_verify_status value validity |
| 333 | Variable Set | DONE readback attempt 2: invalidate value |
| 334 | End If | DONE readback attempt 2: end value check |
| 335 | End If | DONE readback: end output validation attempt 2 |
| 336 | End If | DONE readback: end one-retry wrapper |
| 337 | Variable Set | DONE: readback confirmation default false |
| 338 | If | DONE: exact ID and status readback gate |
| 339 | Variable Set | DONE: exact readback confirmed |
| 340 | End If | DONE: end exact readback gate |
| 341 | If | DONE: successful terminal state |
| 342 | Variable Set | DONE: success failure flag false |
| 343 | Variable Set | DONE: success result |
| 344 | Variable Set | DONE: success status note |
| 345 | Variable Set | DONE: success final result |
| 346 | Else | DONE: readback not confirmed |
| 347 | Variable Set | DONE: readback uncertainty failure |
| 348 | Variable Set | DONE: readback uncertainty result |
| 349 | Variable Set | DONE: readback uncertainty error |
| 350 | End If | DONE: end terminal result |
| 351 | End If | DONE: end readback block |
| 352 | End If | DONE: exit positive-only block |
| 353 | If | lock release: owned lock only |
| 354 | Variable Set | lock release: save result |
| 355 | Variable Set | lock release: save final error |
| 356 | Variable Set | lock release: clear dedicated lock |
| 357 | Variable Clear | lock release: clear timestamp |
| 358 | Variable Set | lock release: clear local ownership |
| 359 | Variable Set | lock release: restore result |
| 360 | Variable Set | lock release: restore final error |
| 361 | End If | lock release: end owned release |
| 362 | Stop | terminal: stop confirmation transaction |
