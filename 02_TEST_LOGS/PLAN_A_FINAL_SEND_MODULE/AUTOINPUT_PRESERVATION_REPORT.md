# AutoInput Preservation Report

## Independent Results

- Direct normalized XML/plugin-bundle comparator: PASS.
- Separate semantic field comparator: PASS.
- Compared AutoInput nodes: 14.
- Compared source actions and associated waits/keyboard/launch nodes in builder map: 35.
- Invented AutoInput targets: 0.

## Node Summary

| # | Role | Source | Source action | Type/selection | Value | Action | Timeout | Continue After Error | Structure Output | XML equal | Semantic equal |
| ---: | --- | --- | ---: | --- | --- | --- | ---: | --- | --- | --- | --- |
| 1 | Navigate up | V15A | 72 | Text | `Navigate up` | `16` | 4 | 0 | false | PASS | PASS |
| 2 | Chats | V15A | 74 | Text | `Chats` | `16` | 4 | 0 | false | PASS | PASS |
| 3 | Text Search | Dashgood | 184 | Text | `Search` | `16` | 12 | 0 | false | PASS | PASS |
| 4 | Reset Navigate up | Dashgood | 190 | Text | `Navigate up` | `16` | 2 | 0 | false | PASS | PASS |
| 5 | Reset Chats | Dashgood | 192 | Text | `Chats` | `16` | 2 | 0 | false | PASS | PASS |
| 6 | Retry Text Search | Dashgood | 197 | Text | `Search` | `16` | 12 | 0 | false | PASS | PASS |
| 7 | Search field 1 | Dashgood | 208 | Id | `com.enflick.android.TextNow:id/search_field` | `16` | 12 | 0 | false | PASS | PASS |
| 8 | Search field 2 | Dashgood | 209 | Id | `com.enflick.android.TextNow:id/search_field` | `16` | 12 | 0 | false | PASS | PASS |
| 9 | Field-retry Text Search | Dashgood | 215 | Text | `Search` | `16` | 12 | 0 | false | PASS | PASS |
| 10 | Retry Search field 1 | Dashgood | 220 | Id | `com.enflick.android.TextNow:id/search_field` | `16` | 12 | 0 | false | PASS | PASS |
| 11 | Retry Search field 2 | Dashgood | 221 | Id | `com.enflick.android.TextNow:id/search_field` | `16` | 12 | 0 | false | PASS | PASS |
| 12 | Contact List 1 | V15A | 99 | List | `1` | `16` | 15 | 0 | false | PASS | PASS |
| 13 | Message box | V15A | 108 | Id | `com.enflick.android.TextNow:id/edit_text_out` | `16` | 15 | 0 | false | PASS | PASS |
| 14 | Send button | V15A | 123 | Id | `com.enflick.android.TextNow:id/button_send` | `16` | 15 | 0 | false | PASS | PASS |

## Complete Bundle Field Comparison

### 1. Navigate up

Source: V15A action `72`. Source normalized SHA256: `415CA0FCDE4C3A0696F7F2843853170A13663F2374E564525BEAA8A2127B285D`. Output normalized SHA256: `415CA0FCDE4C3A0696F7F2843853170A13663F2374E564525BEAA8A2127B285D`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `0` | `0` | PASS |
| Value / ActionId | `Navigate up` | `Navigate up` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `4` | `4` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `Navigate up` | `Navigate up` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `0` | `0` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Text\nValue: Navigate up\nAction : Click` | `Type: Text\nValue: Navigate up\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES` | `[Tasker relevant-variable metadata; source/output exact]` | `[Tasker relevant-variable metadata; source/output exact]` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES-type` | `[Ljava.lang.String;` | `[Ljava.lang.String;` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `0db0c9c7-cbc3-4a0f-9c05-faa3b1692fb1` | `0db0c9c7-cbc3-4a0f-9c05-faa3b1692fb1` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 2. Chats

Source: V15A action `74`. Source normalized SHA256: `B810CAE1FB357CF9AF5D1D09D4509F659A4AA6299AF11CFA3DB983BBBF0CAF71`. Output normalized SHA256: `B810CAE1FB357CF9AF5D1D09D4509F659A4AA6299AF11CFA3DB983BBBF0CAF71`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `0` | `0` | PASS |
| Value / ActionId | `Chats` | `Chats` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `4` | `4` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `Chats` | `Chats` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `0` | `0` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Text\nValue: Chats\nAction : Click` | `Type: Text\nValue: Chats\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES` | `[Tasker relevant-variable metadata; source/output exact]` | `[Tasker relevant-variable metadata; source/output exact]` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES-type` | `[Ljava.lang.String;` | `[Ljava.lang.String;` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `71e3320d-3471-43b5-ac64-071223b0d160` | `71e3320d-3471-43b5-ac64-071223b0d160` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 3. Text Search

Source: Dashgood action `184`. Source normalized SHA256: `CCE8B3784C56DEDA8767691DD82376E67626CEE65FD71D93730F9C0A1D2BE674`. Output normalized SHA256: `CCE8B3784C56DEDA8767691DD82376E67626CEE65FD71D93730F9C0A1D2BE674`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `0` | `0` | PASS |
| Value / ActionId | `Search` | `Search` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `12` | `12` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `Search` | `Search` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `0` | `0` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Text\nValue: Search\nAction : Click` | `Type: Text\nValue: Search\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES` | `[Tasker relevant-variable metadata; source/output exact]` | `[Tasker relevant-variable metadata; source/output exact]` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES-type` | `[Ljava.lang.String;` | `[Ljava.lang.String;` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `58cba9e0-476d-4b8b-98fa-2512850bf6cf` | `58cba9e0-476d-4b8b-98fa-2512850bf6cf` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 4. Reset Navigate up

Source: Dashgood action `190`. Source normalized SHA256: `A8D168CE2CDAD669A3B5C74B770D4375CEF8CBC97A8962597E57BB0D4BFDF145`. Output normalized SHA256: `A8D168CE2CDAD669A3B5C74B770D4375CEF8CBC97A8962597E57BB0D4BFDF145`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `0` | `0` | PASS |
| Value / ActionId | `Navigate up` | `Navigate up` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `2` | `2` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `Navigate up` | `Navigate up` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `0` | `0` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Text\nValue: Navigate up\nAction : Click` | `Type: Text\nValue: Navigate up\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES` | `[Tasker relevant-variable metadata; source/output exact]` | `[Tasker relevant-variable metadata; source/output exact]` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES-type` | `[Ljava.lang.String;` | `[Ljava.lang.String;` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `26ca64b5-feb0-416c-b364-d4055ba068db` | `26ca64b5-feb0-416c-b364-d4055ba068db` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 5. Reset Chats

Source: Dashgood action `192`. Source normalized SHA256: `CD952A658CFE449098EC1CFF66461983279E26A68419EB7D42AC678777F165DD`. Output normalized SHA256: `CD952A658CFE449098EC1CFF66461983279E26A68419EB7D42AC678777F165DD`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `0` | `0` | PASS |
| Value / ActionId | `Chats` | `Chats` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `2` | `2` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `Chats` | `Chats` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `0` | `0` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Text\nValue: Chats\nAction : Click` | `Type: Text\nValue: Chats\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES` | `[Tasker relevant-variable metadata; source/output exact]` | `[Tasker relevant-variable metadata; source/output exact]` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES-type` | `[Ljava.lang.String;` | `[Ljava.lang.String;` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `cebf54c1-ec1b-47b8-a745-39f47a420ddb` | `cebf54c1-ec1b-47b8-a745-39f47a420ddb` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 6. Retry Text Search

Source: Dashgood action `197`. Source normalized SHA256: `CCE8B3784C56DEDA8767691DD82376E67626CEE65FD71D93730F9C0A1D2BE674`. Output normalized SHA256: `CCE8B3784C56DEDA8767691DD82376E67626CEE65FD71D93730F9C0A1D2BE674`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `0` | `0` | PASS |
| Value / ActionId | `Search` | `Search` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `12` | `12` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `Search` | `Search` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `0` | `0` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Text\nValue: Search\nAction : Click` | `Type: Text\nValue: Search\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES` | `[Tasker relevant-variable metadata; source/output exact]` | `[Tasker relevant-variable metadata; source/output exact]` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES-type` | `[Ljava.lang.String;` | `[Ljava.lang.String;` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `58cba9e0-476d-4b8b-98fa-2512850bf6cf` | `58cba9e0-476d-4b8b-98fa-2512850bf6cf` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 7. Search field 1

Source: Dashgood action `208`. Source normalized SHA256: `23B26F610B8CDD6BD1B52933A30EEB241DE36DF71909496D0C00F5A6BD0570DF`. Output normalized SHA256: `23B26F610B8CDD6BD1B52933A30EEB241DE36DF71909496D0C00F5A6BD0570DF`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `1` | `1` | PASS |
| Value / ActionId | `com.enflick.android.TextNow:id/search_field` | `com.enflick.android.TextNow:id/search_field` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `12` | `12` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `com.enflick.android.TextNow:id/search_field` | `com.enflick.android.TextNow:id/search_field` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `1` | `1` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click` | `Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `fc0ce789-e3ad-4f3b-a167-e66c2e7aa099` | `fc0ce789-e3ad-4f3b-a167-e66c2e7aa099` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 8. Search field 2

Source: Dashgood action `209`. Source normalized SHA256: `5E0886C2275B02E85D68DE4A74235C8D93428DAA3135DC59B08BA0B239982B2A`. Output normalized SHA256: `5E0886C2275B02E85D68DE4A74235C8D93428DAA3135DC59B08BA0B239982B2A`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `1` | `1` | PASS |
| Value / ActionId | `com.enflick.android.TextNow:id/search_field` | `com.enflick.android.TextNow:id/search_field` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `12` | `12` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `com.enflick.android.TextNow:id/search_field` | `com.enflick.android.TextNow:id/search_field` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `1` | `1` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click` | `Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `ea82fe3a-fdcd-40c8-b324-953fe6293728` | `ea82fe3a-fdcd-40c8-b324-953fe6293728` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 9. Field-retry Text Search

Source: Dashgood action `215`. Source normalized SHA256: `CCE8B3784C56DEDA8767691DD82376E67626CEE65FD71D93730F9C0A1D2BE674`. Output normalized SHA256: `CCE8B3784C56DEDA8767691DD82376E67626CEE65FD71D93730F9C0A1D2BE674`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `0` | `0` | PASS |
| Value / ActionId | `Search` | `Search` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `12` | `12` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `Search` | `Search` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `0` | `0` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Text\nValue: Search\nAction : Click` | `Type: Text\nValue: Search\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES` | `[Tasker relevant-variable metadata; source/output exact]` | `[Tasker relevant-variable metadata; source/output exact]` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES-type` | `[Ljava.lang.String;` | `[Ljava.lang.String;` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `58cba9e0-476d-4b8b-98fa-2512850bf6cf` | `58cba9e0-476d-4b8b-98fa-2512850bf6cf` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 10. Retry Search field 1

Source: Dashgood action `220`. Source normalized SHA256: `23B26F610B8CDD6BD1B52933A30EEB241DE36DF71909496D0C00F5A6BD0570DF`. Output normalized SHA256: `23B26F610B8CDD6BD1B52933A30EEB241DE36DF71909496D0C00F5A6BD0570DF`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `1` | `1` | PASS |
| Value / ActionId | `com.enflick.android.TextNow:id/search_field` | `com.enflick.android.TextNow:id/search_field` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `12` | `12` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `com.enflick.android.TextNow:id/search_field` | `com.enflick.android.TextNow:id/search_field` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `1` | `1` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click` | `Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `fc0ce789-e3ad-4f3b-a167-e66c2e7aa099` | `fc0ce789-e3ad-4f3b-a167-e66c2e7aa099` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 11. Retry Search field 2

Source: Dashgood action `221`. Source normalized SHA256: `23B26F610B8CDD6BD1B52933A30EEB241DE36DF71909496D0C00F5A6BD0570DF`. Output normalized SHA256: `23B26F610B8CDD6BD1B52933A30EEB241DE36DF71909496D0C00F5A6BD0570DF`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `1` | `1` | PASS |
| Value / ActionId | `com.enflick.android.TextNow:id/search_field` | `com.enflick.android.TextNow:id/search_field` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `12` | `12` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `com.enflick.android.TextNow:id/search_field` | `com.enflick.android.TextNow:id/search_field` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `1` | `1` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click` | `Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `fc0ce789-e3ad-4f3b-a167-e66c2e7aa099` | `fc0ce789-e3ad-4f3b-a167-e66c2e7aa099` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 12. Contact List 1

Source: V15A action `99`. Source normalized SHA256: `C52ED407AAA488ACE4DCCEDC9585A0F06612835E1731B2181C62CDD451BC0906`. Output normalized SHA256: `C52ED407AAA488ACE4DCCEDC9585A0F06612835E1731B2181C62CDD451BC0906`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `3` | `3` | PASS |
| Value / ActionId | `1` | `1` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `15` | `15` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `1` | `1` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `3` | `3` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: List\nValue: 1\nAction : Click` | `Type: List\nValue: 1\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES` | `[Tasker relevant-variable metadata; source/output exact]` | `[Tasker relevant-variable metadata; source/output exact]` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES-type` | `[Ljava.lang.String;` | `[Ljava.lang.String;` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `34758ea0-9e05-4ee1-9f7a-b1e4c19e662e` | `34758ea0-9e05-4ee1-9f7a-b1e4c19e662e` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 13. Message box

Source: V15A action `108`. Source normalized SHA256: `842265F698FC33A1DCA9D8051BE7B2497E73901392560562CE926BC86E79390A`. Output normalized SHA256: `842265F698FC33A1DCA9D8051BE7B2497E73901392560562CE926BC86E79390A`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `1` | `1` | PASS |
| Value / ActionId | `com.enflick.android.TextNow:id/edit_text_out` | `com.enflick.android.TextNow:id/edit_text_out` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `15` | `15` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `com.enflick.android.TextNow:id/edit_text_out` | `com.enflick.android.TextNow:id/edit_text_out` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `1` | `1` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Id\nValue: com.enflick.android.TextNow:id/edit_text_out\nAction : Click` | `Type: Id\nValue: com.enflick.android.TextNow:id/edit_text_out\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES` | `[Tasker relevant-variable metadata; source/output exact]` | `[Tasker relevant-variable metadata; source/output exact]` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES-type` | `[Ljava.lang.String;` | `[Ljava.lang.String;` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `a44bef26-315e-41c4-8b5f-85a33a1ab0ff` | `a44bef26-315e-41c4-8b5f-85a33a1ab0ff` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

### 14. Send button

Source: V15A action `123`. Source normalized SHA256: `4EF69A3F4890E3FD168E165A65A3FCD55E6DE88982C8641E900E4CF1EE24C065`. Output normalized SHA256: `4EF69A3F4890E3FD168E165A65A3FCD55E6DE88982C8641E900E4CF1EE24C065`.

| Field | Source value | Output value | Result |
| --- | --- | --- | --- |
| Type / Field Selection Type | `1` | `1` | PASS |
| Value / ActionId | `com.enflick.android.TextNow:id/button_send` | `com.enflick.android.TextNow:id/button_send` | PASS |
| Action / ActionType | `16` | `16` | PASS |
| Text target | `<null>` | `<null>` | PASS |
| Point | `` | `` | PASS |
| Nearby text | `<null>` | `<null>` | PASS |
| Timeout | `15` | `15` | PASS |
| Continue Task After Error | `0` | `0` | PASS |
| Structure Output | `false` | `false` | PASS |
| Accessibility | `<null>` | `<null>` | PASS |
| Bundle `ActionId` | `com.enflick.android.TextNow:id/button_send` | `com.enflick.android.TextNow:id/button_send` | PASS |
| Bundle `ActionId-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `ActionType` | `16` | `16` | PASS |
| Bundle `ActionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `EnableDisableAccessibilityService` | `<null>` | `<null>` | PASS |
| Bundle `EnableDisableAccessibilityService-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `FieldSelectionType` | `1` | `1` | PASS |
| Bundle `FieldSelectionType-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `IsFirstAction` | `false` | `false` | PASS |
| Bundle `IsFirstAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `IsTaskerAction` | `false` | `false` | PASS |
| Bundle `IsTaskerAction-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `NearbyText` | `<null>` | `<null>` | PASS |
| Bundle `NearbyText-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `Password` | `<null>` | `<null>` | PASS |
| Bundle `Password-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatInterval` | `<null>` | `<null>` | PASS |
| Bundle `RepeatInterval-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `RepeatTimes` | `<null>` | `<null>` | PASS |
| Bundle `RepeatTimes-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `StoredAction` | `<null>` | `<null>` | PASS |
| Bundle `StoredAction-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `TextToWrite` | `<null>` | `<null>` | PASS |
| Bundle `TextToWrite-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB` | `Type: Id\nValue: com.enflick.android.TextNow:id/button_send\nAction : Click` | `Type: Id\nValue: com.enflick.android.TextNow:id/button_send\nAction : Click` | PASS |
| Bundle `com.twofortyfouram.locale.intent.extra.BLURB-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES` | `[Tasker relevant-variable metadata; source/output exact]` | `[Tasker relevant-variable metadata; source/output exact]` | PASS |
| Bundle `net.dinglisch.android.tasker.RELEVANT_VARIABLES-type` | `[Ljava.lang.String;` | `[Ljava.lang.String;` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | `ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ` | PASS |
| Bundle `net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled` | `true` | `true` | PASS |
| Bundle `net.dinglisch.android.tasker.subbundled-type` | `java.lang.Boolean` | `java.lang.Boolean` | PASS |
| Bundle `plugininstanceid` | `5dcd3e7d-2f18-4605-9bcd-0001e3703583` | `5dcd3e7d-2f18-4605-9bcd-0001e3703583` | PASS |
| Bundle `plugininstanceid-type` | `java.lang.String` | `java.lang.String` | PASS |
| Bundle `plugintypeid` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | `com.joaomgcd.autoinput.intent.IntentPerformAction` | PASS |
| Bundle `plugintypeid-type` | `java.lang.String` | `java.lang.String` | PASS |

## Associated Control Contract

- Initial Navigate up/Chats and their waits come from V15A.
- Search reset/retry, both search-field clicks, field retry, and their waits come from active Dashgood Task 71.
- Text Search error alone is not fatal; final search-field reach is the positive completion gate.
- Contact, message box, reply keyboard, and button_send come from V15A.
- All source/output plugin bundles compare exactly after removing only action `sr` location.
- Failure routing is new Plan A wrapper logic; it never calls the old generic dirty-stop helper from Task 223.
