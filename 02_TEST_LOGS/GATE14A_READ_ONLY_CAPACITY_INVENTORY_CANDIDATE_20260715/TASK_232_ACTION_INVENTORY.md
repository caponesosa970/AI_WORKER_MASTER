# Gate 14A Read-Only Capacity Inventory Candidate

- Main source commit: `1b73c48c77b05b2518c47d30387778f86b647576`
- Base: `GATE13R2_FULL_PROJECT_TASKER_IMPORT__CONFIRM_THREAD_NAVIGATION_PRIVATE.xml`
- Base SHA256: `1C4D13872C3D6B4579AA698F9E7D2F50F3E81467A4CBD4EAD63CD567087832A7`
- Candidate XML SHA256: `832BEB0F9764EB2838B08A582648097C49197C2A366931196E5F0311860529EF`
- Tracker: `13/14 locked = 93%` (unchanged)
- Runtime phone proof: NOT CLAIMED
- Phone import approval: NO
- Capacity proof: NOT CLAIMED

## Full Action Inventory

The plugin row intentionally omits the private spreadsheet identifier while retaining the exact public-safe sheet, range, mode, outputs, timeout, and Continue After Error setting.

| Index | `sr` | Code | Exact public-safe action |
| ---: | --- | ---: | --- |
| 0 | `act0` | `547` | Variable Set %armed = %AIWG14AllowInventory |
| 1 | `act1` | `37` | If %AIWG14AllowInventory op2 1 |
| 2 | `act2` | `547` | Variable Set %AIWG14AllowInventory = 0 |
| 3 | `act3` | `38` | End If |
| 4 | `act4` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_START |
| 5 | `act5` | `549` | Variable Clear %AIWG14InventoryError |
| 6 | `act6` | `549` | Variable Clear %AIWG14RunIdResult |
| 7 | `act7` | `549` | Variable Clear %AIWG14ExpectedCountResult |
| 8 | `act8` | `549` | Variable Clear %AIWG14FirstSourceRow |
| 9 | `act9` | `549` | Variable Clear %AIWG14LastSourceRow |
| 10 | `act10` | `549` | Variable Clear %AIWG14ObservedRows |
| 11 | `act11` | `549` | Variable Clear %AIWG14ObservedIds |
| 12 | `act12` | `549` | Variable Clear %AIWG14ObservedSenders |
| 13 | `act13` | `547` | Variable Set %AIWG14InventoryCount = 0 |
| 14 | `act14` | `547` | Variable Set %AIWG14UniqueIdCount = 0 |
| 15 | `act15` | `547` | Variable Set %AIWG14UniqueSenderCount = 0 |
| 16 | `act16` | `547` | Variable Set %AIWG14DuplicateIdCount = 0 |
| 17 | `act17` | `547` | Variable Set %AIWG14DuplicateSenderCount = 0 |
| 18 | `act18` | `547` | Variable Set %AIWG14BlankRequiredCount = 0 |
| 19 | `act19` | `547` | Variable Set %AIWG14WrongStatusCount = 0 |
| 20 | `act20` | `547` | Variable Set %AIWG14NonblankReplyCount = 0 |
| 21 | `act21` | `547` | Variable Set %AIWG14UnresolvedCount = 0 |
| 22 | `act22` | `547` | Variable Set %AIWG14ErrorCellCount = 0 |
| 23 | `act23` | `547` | Variable Set %AIWG14OrderErrorCount = 0 |
| 24 | `act24` | `547` | Variable Set %AIWG14ReadAttempts = 0 |
| 25 | `act25` | `547` | Variable Set %AIWG14InventoryDuration = 0 |
| 26 | `act26` | `547` | Variable Set %start_time = %TIMES |
| 27 | `act27` | `37` | If %armed op3 1 |
| 28 | `act28` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_NOT_ARMED |
| 29 | `act29` | `547` | Variable Set %AIWG14InventoryError = Gate 14A inventory authorization was not armed |
| 30 | `act30` | `547` | Variable Set %end_time = %TIMES |
| 31 | `act31` | `547` | Variable Set %AIWG14InventoryDuration = %end_time-%start_time |
| 32 | `act32` | `137` | Stop |
| 33 | `act33` | `38` | End If |
| 34 | `act34` | `547` | Variable Set %run_id = %AIWG14RunId |
| 35 | `act35` | `547` | Variable Set %expected = %AIWG14ExpectedCount |
| 36 | `act36` | `547` | Variable Set %AIWG14RunIdResult = %run_id |
| 37 | `act37` | `547` | Variable Set %AIWG14ExpectedCountResult = %expected |
| 38 | `act38` | `37` | If %run_id op5 ^[A-Z0-9_-]{4,32}$ OR %expected op5 ^(1\|5\|10\|25\|50)$ |
| 39 | `act39` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_INPUT_HOLD |
| 40 | `act40` | `547` | Variable Set %AIWG14InventoryError = Run ID or expected count failed the Gate 14A input contract |
| 41 | `act41` | `547` | Variable Set %end_time = %TIMES |
| 42 | `act42` | `547` | Variable Set %AIWG14InventoryDuration = %end_time-%start_time |
| 43 | `act43` | `137` | Stop |
| 44 | `act44` | `38` | End If |
| 45 | `act45` | `547` | Variable Set %prefix = G14CAP-%run_id- |
| 46 | `act46` | `547` | Variable Set %read_ok = 0 |
| 47 | `act47` | `549` | Variable Clear %last_read_error |
| 48 | `act48` | `39` | For %g14_attempt in 1,2 |
| 49 | `act49` | `37` | If %read_ok op3 1 |
| 50 | `act50` | `37` | If %g14_attempt op7 1 |
| 51 | `act51` | `30` | Wait 3 seconds |
| 52 | `act52` | `38` | End If |
| 53 | `act53` | `549` | Variable Clear %g14_id |
| 54 | `act54` | `549` | Variable Clear %g14_sender |
| 55 | `act55` | `549` | Variable Clear %g14_message |
| 56 | `act56` | `549` | Variable Clear %g14_status |
| 57 | `act57` | `549` | Variable Clear %g14_reply |
| 58 | `act58` | `549` | Variable Clear %g14_touch |
| 59 | `act59` | `549` | Variable Clear %g14_button |
| 60 | `act60` | `549` | Variable Clear %g14_time |
| 61 | `act61` | `549` | Variable Clear %g14_ticker |
| 62 | `act62` | `549` | Variable Clear %err |
| 63 | `act63` | `549` | Variable Clear %errmsg |
| 64 | `act64` | `547` | Variable Set %AIWG14ReadAttempts = %g14_attempt |
| 65 | `act65` | `1810865467` | AutoSheets Get Data; Sheet1!A2:I201; columns; nine arrays; 60-second timeout; Continue After Error ON |
| 66 | `act66` | `547` | Variable Set %read_ok = 1 |
| 67 | `act67` | `549` | Variable Clear %last_read_error |
| 68 | `act68` | `37` | If %err op4 ^[0-9]+$ |
| 69 | `act69` | `547` | Variable Set %read_ok = 0 |
| 70 | `act70` | `547` | Variable Set %last_read_error = AutoSheets read error %err: %errmsg |
| 71 | `act71` | `38` | End If |
| 72 | `act72` | `37` | If %err op5 ^[0-9]+$ AND %g14_id(#) op3 %g14_sender(#) |
| 73 | `act73` | `547` | Variable Set %read_ok = 0 |
| 74 | `act74` | `547` | Variable Set %last_read_error = AutoSheets output arrays were not aligned |
| 75 | `act75` | `38` | End If |
| 76 | `act76` | `37` | If %err op5 ^[0-9]+$ AND %g14_id(#) op3 %g14_message(#) |
| 77 | `act77` | `547` | Variable Set %read_ok = 0 |
| 78 | `act78` | `547` | Variable Set %last_read_error = AutoSheets output arrays were not aligned |
| 79 | `act79` | `38` | End If |
| 80 | `act80` | `37` | If %err op5 ^[0-9]+$ AND %g14_id(#) op3 %g14_status(#) |
| 81 | `act81` | `547` | Variable Set %read_ok = 0 |
| 82 | `act82` | `547` | Variable Set %last_read_error = AutoSheets output arrays were not aligned |
| 83 | `act83` | `38` | End If |
| 84 | `act84` | `37` | If %err op5 ^[0-9]+$ AND %g14_id(#) op3 %g14_reply(#) |
| 85 | `act85` | `547` | Variable Set %read_ok = 0 |
| 86 | `act86` | `547` | Variable Set %last_read_error = AutoSheets output arrays were not aligned |
| 87 | `act87` | `38` | End If |
| 88 | `act88` | `37` | If %err op5 ^[0-9]+$ AND %g14_id(#) op3 %g14_touch(#) |
| 89 | `act89` | `547` | Variable Set %read_ok = 0 |
| 90 | `act90` | `547` | Variable Set %last_read_error = AutoSheets output arrays were not aligned |
| 91 | `act91` | `38` | End If |
| 92 | `act92` | `37` | If %err op5 ^[0-9]+$ AND %g14_id(#) op3 %g14_button(#) |
| 93 | `act93` | `547` | Variable Set %read_ok = 0 |
| 94 | `act94` | `547` | Variable Set %last_read_error = AutoSheets output arrays were not aligned |
| 95 | `act95` | `38` | End If |
| 96 | `act96` | `37` | If %err op5 ^[0-9]+$ AND %g14_id(#) op3 %g14_time(#) |
| 97 | `act97` | `547` | Variable Set %read_ok = 0 |
| 98 | `act98` | `547` | Variable Set %last_read_error = AutoSheets output arrays were not aligned |
| 99 | `act99` | `38` | End If |
| 100 | `act100` | `37` | If %err op5 ^[0-9]+$ AND %g14_id(#) op3 %g14_ticker(#) |
| 101 | `act101` | `547` | Variable Set %read_ok = 0 |
| 102 | `act102` | `547` | Variable Set %last_read_error = AutoSheets output arrays were not aligned |
| 103 | `act103` | `38` | End If |
| 104 | `act104` | `38` | End If |
| 105 | `act105` | `40` | End For |
| 106 | `act106` | `37` | If %read_ok op3 1 |
| 107 | `act107` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_READ_HOLD |
| 108 | `act108` | `547` | Variable Set %AIWG14InventoryError = %last_read_error |
| 109 | `act109` | `547` | Variable Set %end_time = %TIMES |
| 110 | `act110` | `547` | Variable Set %AIWG14InventoryDuration = %end_time-%start_time |
| 111 | `act111` | `137` | Stop |
| 112 | `act112` | `38` | End If |
| 113 | `act113` | `547` | Variable Set %row_index = 0 |
| 114 | `act114` | `547` | Variable Set %previous_source_row = 0 |
| 115 | `act115` | `547` | Variable Set %delimiter_error_count = 0 |
| 116 | `act116` | `549` | Variable Clear %accepted_ids |
| 117 | `act117` | `549` | Variable Clear %accepted_senders |
| 118 | `act118` | `39` | For %row_dummy in %g14_id() |
| 119 | `act119` | `888` | Variable Add %row_index +1 |
| 120 | `act120` | `547` | Variable Set %row_id = %g14_id(%row_index) |
| 121 | `act121` | `547` | Variable Set %row_sender = %g14_sender(%row_index) |
| 122 | `act122` | `547` | Variable Set %row_message = %g14_message(%row_index) |
| 123 | `act123` | `547` | Variable Set %row_status = %g14_status(%row_index) |
| 124 | `act124` | `547` | Variable Set %row_reply = %g14_reply(%row_index) |
| 125 | `act125` | `547` | Variable Set %row_touch = %g14_touch(%row_index) |
| 126 | `act126` | `547` | Variable Set %row_button = %g14_button(%row_index) |
| 127 | `act127` | `547` | Variable Set %row_time = %g14_time(%row_index) |
| 128 | `act128` | `547` | Variable Set %row_ticker = %g14_ticker(%row_index) |
| 129 | `act129` | `37` | If %row_id op4 ^G14CAP-%run_id- |
| 130 | `act130` | `888` | Variable Add %AIWG14InventoryCount +1 |
| 131 | `act131` | `547` | Variable Set %source_row = %row_index+1 |
| 132 | `act132` | `37` | If %AIWG14InventoryCount op2 1 |
| 133 | `act133` | `547` | Variable Set %AIWG14FirstSourceRow = %source_row |
| 134 | `act134` | `43` | Else |
| 135 | `act135` | `37` | If %source_row op7 %previous_source_row |
| 136 | `act136` | `547` | Variable Set %order_checked = 1 |
| 137 | `act137` | `43` | Else |
| 138 | `act138` | `888` | Variable Add %AIWG14OrderErrorCount +1 |
| 139 | `act139` | `38` | End If |
| 140 | `act140` | `38` | End If |
| 141 | `act141` | `547` | Variable Set %previous_source_row = %source_row |
| 142 | `act142` | `547` | Variable Set %AIWG14LastSourceRow = %source_row |
| 143 | `act143` | `37` | If %AIWG14InventoryCount op2 1 |
| 144 | `act144` | `547` | Variable Set %AIWG14ObservedRows = %source_row |
| 145 | `act145` | `547` | Variable Set %AIWG14ObservedIds = %row_id |
| 146 | `act146` | `547` | Variable Set %AIWG14ObservedSenders = %row_sender |
| 147 | `act147` | `43` | Else |
| 148 | `act148` | `547` | Variable Set %AIWG14ObservedRows = %AIWG14ObservedRows\|%source_row |
| 149 | `act149` | `547` | Variable Set %AIWG14ObservedIds = %AIWG14ObservedIds\|%row_id |
| 150 | `act150` | `547` | Variable Set %AIWG14ObservedSenders = %AIWG14ObservedSenders\|%row_sender |
| 151 | `act151` | `38` | End If |
| 152 | `act152` | `547` | Variable Set %id_seen_count = 0 |
| 153 | `act153` | `37` | If %AIWG14InventoryCount op7 1 |
| 154 | `act154` | `39` | For %seen_id in %accepted_ids() |
| 155 | `act155` | `37` | If %seen_id op2 %row_id |
| 156 | `act156` | `888` | Variable Add %id_seen_count +1 |
| 157 | `act157` | `38` | End If |
| 158 | `act158` | `40` | End For |
| 159 | `act159` | `38` | End If |
| 160 | `act160` | `37` | If %id_seen_count op7 0 |
| 161 | `act161` | `888` | Variable Add %AIWG14DuplicateIdCount +1 |
| 162 | `act162` | `43` | Else |
| 163 | `act163` | `888` | Variable Add %AIWG14UniqueIdCount +1 |
| 164 | `act164` | `38` | End If |
| 165 | `act165` | `547` | Variable Set %accepted_ids(%AIWG14InventoryCount) = %row_id |
| 166 | `act166` | `547` | Variable Set %sender_seen_count = 0 |
| 167 | `act167` | `37` | If %AIWG14InventoryCount op7 1 |
| 168 | `act168` | `39` | For %seen_sender in %accepted_senders() |
| 169 | `act169` | `37` | If %seen_sender op2 %row_sender |
| 170 | `act170` | `888` | Variable Add %sender_seen_count +1 |
| 171 | `act171` | `38` | End If |
| 172 | `act172` | `40` | End For |
| 173 | `act173` | `38` | End If |
| 174 | `act174` | `37` | If %sender_seen_count op7 0 |
| 175 | `act175` | `888` | Variable Add %AIWG14DuplicateSenderCount +1 |
| 176 | `act176` | `43` | Else |
| 177 | `act177` | `888` | Variable Add %AIWG14UniqueSenderCount +1 |
| 178 | `act178` | `38` | End If |
| 179 | `act179` | `547` | Variable Set %accepted_senders(%AIWG14InventoryCount) = %row_sender |
| 180 | `act180` | `37` | If %row_id op4 (?s)^\s*$ |
| 181 | `act181` | `888` | Variable Add %AIWG14BlankRequiredCount +1 |
| 182 | `act182` | `38` | End If |
| 183 | `act183` | `37` | If %row_sender op4 (?s)^\s*$ |
| 184 | `act184` | `888` | Variable Add %AIWG14BlankRequiredCount +1 |
| 185 | `act185` | `38` | End If |
| 186 | `act186` | `37` | If %row_message op4 (?s)^\s*$ |
| 187 | `act187` | `888` | Variable Add %AIWG14BlankRequiredCount +1 |
| 188 | `act188` | `38` | End If |
| 189 | `act189` | `37` | If %row_status op4 (?s)^\s*$ |
| 190 | `act190` | `888` | Variable Add %AIWG14BlankRequiredCount +1 |
| 191 | `act191` | `38` | End If |
| 192 | `act192` | `37` | If %row_status op3 G14_CAPACITY_STAGED |
| 193 | `act193` | `888` | Variable Add %AIWG14WrongStatusCount +1 |
| 194 | `act194` | `38` | End If |
| 195 | `act195` | `37` | If %row_reply op5 (?s)^\s*$ |
| 196 | `act196` | `888` | Variable Add %AIWG14NonblankReplyCount +1 |
| 197 | `act197` | `38` | End If |
| 198 | `act198` | `37` | If %row_id op4 (?s)^%.*$ |
| 199 | `act199` | `888` | Variable Add %AIWG14UnresolvedCount +1 |
| 200 | `act200` | `38` | End If |
| 201 | `act201` | `37` | If %row_id op4 (?is).*#ERROR.* |
| 202 | `act202` | `888` | Variable Add %AIWG14ErrorCellCount +1 |
| 203 | `act203` | `38` | End If |
| 204 | `act204` | `37` | If %row_sender op4 (?s)^%.*$ |
| 205 | `act205` | `888` | Variable Add %AIWG14UnresolvedCount +1 |
| 206 | `act206` | `38` | End If |
| 207 | `act207` | `37` | If %row_sender op4 (?is).*#ERROR.* |
| 208 | `act208` | `888` | Variable Add %AIWG14ErrorCellCount +1 |
| 209 | `act209` | `38` | End If |
| 210 | `act210` | `37` | If %row_message op4 (?s)^%.*$ |
| 211 | `act211` | `888` | Variable Add %AIWG14UnresolvedCount +1 |
| 212 | `act212` | `38` | End If |
| 213 | `act213` | `37` | If %row_message op4 (?is).*#ERROR.* |
| 214 | `act214` | `888` | Variable Add %AIWG14ErrorCellCount +1 |
| 215 | `act215` | `38` | End If |
| 216 | `act216` | `37` | If %row_status op4 (?s)^%.*$ |
| 217 | `act217` | `888` | Variable Add %AIWG14UnresolvedCount +1 |
| 218 | `act218` | `38` | End If |
| 219 | `act219` | `37` | If %row_status op4 (?is).*#ERROR.* |
| 220 | `act220` | `888` | Variable Add %AIWG14ErrorCellCount +1 |
| 221 | `act221` | `38` | End If |
| 222 | `act222` | `37` | If %row_reply op4 (?s)^%.*$ |
| 223 | `act223` | `888` | Variable Add %AIWG14UnresolvedCount +1 |
| 224 | `act224` | `38` | End If |
| 225 | `act225` | `37` | If %row_reply op4 (?is).*#ERROR.* |
| 226 | `act226` | `888` | Variable Add %AIWG14ErrorCellCount +1 |
| 227 | `act227` | `38` | End If |
| 228 | `act228` | `37` | If %row_touch op4 (?s)^%.*$ |
| 229 | `act229` | `888` | Variable Add %AIWG14UnresolvedCount +1 |
| 230 | `act230` | `38` | End If |
| 231 | `act231` | `37` | If %row_touch op4 (?is).*#ERROR.* |
| 232 | `act232` | `888` | Variable Add %AIWG14ErrorCellCount +1 |
| 233 | `act233` | `38` | End If |
| 234 | `act234` | `37` | If %row_button op4 (?s)^%.*$ |
| 235 | `act235` | `888` | Variable Add %AIWG14UnresolvedCount +1 |
| 236 | `act236` | `38` | End If |
| 237 | `act237` | `37` | If %row_button op4 (?is).*#ERROR.* |
| 238 | `act238` | `888` | Variable Add %AIWG14ErrorCellCount +1 |
| 239 | `act239` | `38` | End If |
| 240 | `act240` | `37` | If %row_time op4 (?s)^%.*$ |
| 241 | `act241` | `888` | Variable Add %AIWG14UnresolvedCount +1 |
| 242 | `act242` | `38` | End If |
| 243 | `act243` | `37` | If %row_time op4 (?is).*#ERROR.* |
| 244 | `act244` | `888` | Variable Add %AIWG14ErrorCellCount +1 |
| 245 | `act245` | `38` | End If |
| 246 | `act246` | `37` | If %row_ticker op4 (?s)^%.*$ |
| 247 | `act247` | `888` | Variable Add %AIWG14UnresolvedCount +1 |
| 248 | `act248` | `38` | End If |
| 249 | `act249` | `37` | If %row_ticker op4 (?is).*#ERROR.* |
| 250 | `act250` | `888` | Variable Add %AIWG14ErrorCellCount +1 |
| 251 | `act251` | `38` | End If |
| 252 | `act252` | `37` | If %row_id op4 .*\\|.* |
| 253 | `act253` | `888` | Variable Add %delimiter_error_count +1 |
| 254 | `act254` | `38` | End If |
| 255 | `act255` | `37` | If %row_sender op4 .*\\|.* |
| 256 | `act256` | `888` | Variable Add %delimiter_error_count +1 |
| 257 | `act257` | `38` | End If |
| 258 | `act258` | `38` | End If |
| 259 | `act259` | `40` | End For |
| 260 | `act260` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_PASS |
| 261 | `act261` | `549` | Variable Clear %AIWG14InventoryError |
| 262 | `act262` | `37` | If %AIWG14InventoryCount op3 %expected |
| 263 | `act263` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_COUNT_HOLD |
| 264 | `act264` | `547` | Variable Set %AIWG14InventoryError = Observed count did not equal the approved expected count |
| 265 | `act265` | `38` | End If |
| 266 | `act266` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14DuplicateIdCount op7 0 |
| 267 | `act267` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_DUPLICATE_ID_HOLD |
| 268 | `act268` | `547` | Variable Set %AIWG14InventoryError = Duplicate Gate 14A IDs were detected |
| 269 | `act269` | `38` | End If |
| 270 | `act270` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14DuplicateSenderCount op7 0 |
| 271 | `act271` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_DUPLICATE_SENDER_HOLD |
| 272 | `act272` | `547` | Variable Set %AIWG14InventoryError = Duplicate Gate 14A senders were detected |
| 273 | `act273` | `38` | End If |
| 274 | `act274` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14WrongStatusCount op7 0 |
| 275 | `act275` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_STATUS_HOLD |
| 276 | `act276` | `547` | Variable Set %AIWG14InventoryError = A matching-prefix row had the wrong status |
| 277 | `act277` | `38` | End If |
| 278 | `act278` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14NonblankReplyCount op7 0 |
| 279 | `act279` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_REPLY_HOLD |
| 280 | `act280` | `547` | Variable Set %AIWG14InventoryError = A matching-prefix row had a nonblank reply |
| 281 | `act281` | `38` | End If |
| 282 | `act282` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14OrderErrorCount op7 0 |
| 283 | `act283` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_ORDER_HOLD |
| 284 | `act284` | `547` | Variable Set %AIWG14InventoryError = Source-row order validation failed |
| 285 | `act285` | `38` | End If |
| 286 | `act286` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14BlankRequiredCount op7 0 |
| 287 | `act287` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_FIELD_HOLD |
| 288 | `act288` | `547` | Variable Set %AIWG14InventoryError = A required field or inventory integrity check failed |
| 289 | `act289` | `38` | End If |
| 290 | `act290` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14UnresolvedCount op7 0 |
| 291 | `act291` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_FIELD_HOLD |
| 292 | `act292` | `547` | Variable Set %AIWG14InventoryError = A required field or inventory integrity check failed |
| 293 | `act293` | `38` | End If |
| 294 | `act294` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14ErrorCellCount op7 0 |
| 295 | `act295` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_FIELD_HOLD |
| 296 | `act296` | `547` | Variable Set %AIWG14InventoryError = A required field or inventory integrity check failed |
| 297 | `act297` | `38` | End If |
| 298 | `act298` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %delimiter_error_count op7 0 |
| 299 | `act299` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_FIELD_HOLD |
| 300 | `act300` | `547` | Variable Set %AIWG14InventoryError = A required field or inventory integrity check failed |
| 301 | `act301` | `38` | End If |
| 302 | `act302` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14UniqueIdCount op3 %expected |
| 303 | `act303` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_FIELD_HOLD |
| 304 | `act304` | `547` | Variable Set %AIWG14InventoryError = A required field or inventory integrity check failed |
| 305 | `act305` | `38` | End If |
| 306 | `act306` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14UniqueSenderCount op3 %expected |
| 307 | `act307` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_FIELD_HOLD |
| 308 | `act308` | `547` | Variable Set %AIWG14InventoryError = A required field or inventory integrity check failed |
| 309 | `act309` | `38` | End If |
| 310 | `act310` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14FirstSourceRow op5 ^[0-9]+$ |
| 311 | `act311` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_FIELD_HOLD |
| 312 | `act312` | `547` | Variable Set %AIWG14InventoryError = A required field or inventory integrity check failed |
| 313 | `act313` | `38` | End If |
| 314 | `act314` | `37` | If %AIWG14InventoryResult op2 INVENTORY_PASS AND %AIWG14LastSourceRow op5 ^[0-9]+$ |
| 315 | `act315` | `547` | Variable Set %AIWG14InventoryResult = INVENTORY_FIELD_HOLD |
| 316 | `act316` | `547` | Variable Set %AIWG14InventoryError = A required field or inventory integrity check failed |
| 317 | `act317` | `38` | End If |
| 318 | `act318` | `547` | Variable Set %end_time = %TIMES |
| 319 | `act319` | `547` | Variable Set %AIWG14InventoryDuration = %end_time-%start_time |
| 320 | `act320` | `137` | Stop |
