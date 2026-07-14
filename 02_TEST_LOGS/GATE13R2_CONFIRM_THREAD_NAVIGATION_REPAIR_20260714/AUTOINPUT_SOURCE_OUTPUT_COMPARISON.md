# AutoInput Source/Output Comparison

Validator 1 compared direct XML nodes. Validator 2 independently located the same 72-node source subsequence in Task 231. All 12 copied AutoInput nodes match Task 223 field-for-field, including package/class, Continue After Error, timeout, target data, Structure Output, accessibility values, and complete plugin bundles. Output `sr` is the only placement difference.

### Task 223 action 480 to Task 231 action 23

Role: Task 223 exact Navigate up AutoInput

Source semantics:

```json
{
  "bundle": {
    "ActionId": "Navigate up",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Navigate up\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "0db0c9c7-cbc3-4a0f-9c05-faa3b1692fb1",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "Navigate up",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Navigate up\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "0db0c9c7-cbc3-4a0f-9c05-faa3b1692fb1",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 482 to Task 231 action 33

Role: Task 223 exact Chats AutoInput

Source semantics:

```json
{
  "bundle": {
    "ActionId": "Chats",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Chats\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "71e3320d-3471-43b5-ac64-071223b0d160",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "Chats",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Chats\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "71e3320d-3471-43b5-ac64-071223b0d160",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 487 to Task 231 action 44

Role: Task 223 exact search wrapper/action 487

Source semantics:

```json
{
  "bundle": {
    "ActionId": "Search",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Search\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "58cba9e0-476d-4b8b-98fa-2512850bf6cf",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "Search",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Search\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "58cba9e0-476d-4b8b-98fa-2512850bf6cf",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 493 to Task 231 action 50

Role: Task 223 exact search wrapper/action 493

Source semantics:

```json
{
  "bundle": {
    "ActionId": "Navigate up",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Navigate up\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "26ca64b5-feb0-416c-b364-d4055ba068db",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "Navigate up",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Navigate up\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "26ca64b5-feb0-416c-b364-d4055ba068db",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 495 to Task 231 action 52

Role: Task 223 exact search wrapper/action 495

Source semantics:

```json
{
  "bundle": {
    "ActionId": "Chats",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Chats\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "cebf54c1-ec1b-47b8-a745-39f47a420ddb",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "Chats",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Chats\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "cebf54c1-ec1b-47b8-a745-39f47a420ddb",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 500 to Task 231 action 57

Role: Task 223 exact search wrapper/action 500

Source semantics:

```json
{
  "bundle": {
    "ActionId": "Search",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Search\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "58cba9e0-476d-4b8b-98fa-2512850bf6cf",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "Search",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Search\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "58cba9e0-476d-4b8b-98fa-2512850bf6cf",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 507 to Task 231 action 64

Role: Task 223 exact search wrapper/action 507

Source semantics:

```json
{
  "bundle": {
    "ActionId": "com.enflick.android.TextNow:id/search_field",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "1",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "fc0ce789-e3ad-4f3b-a167-e66c2e7aa099",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "com.enflick.android.TextNow:id/search_field",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "1",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "fc0ce789-e3ad-4f3b-a167-e66c2e7aa099",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 508 to Task 231 action 65

Role: Task 223 exact search wrapper/action 508

Source semantics:

```json
{
  "bundle": {
    "ActionId": "com.enflick.android.TextNow:id/search_field",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "1",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "ea82fe3a-fdcd-40c8-b324-953fe6293728",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "com.enflick.android.TextNow:id/search_field",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "1",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "ea82fe3a-fdcd-40c8-b324-953fe6293728",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 514 to Task 231 action 71

Role: Task 223 exact search wrapper/action 514

Source semantics:

```json
{
  "bundle": {
    "ActionId": "Search",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Search\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "58cba9e0-476d-4b8b-98fa-2512850bf6cf",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "Search",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "0",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Text\nValue: Search\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "58cba9e0-476d-4b8b-98fa-2512850bf6cf",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 519 to Task 231 action 76

Role: Task 223 exact search wrapper/action 519

Source semantics:

```json
{
  "bundle": {
    "ActionId": "com.enflick.android.TextNow:id/search_field",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "1",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "fc0ce789-e3ad-4f3b-a167-e66c2e7aa099",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "com.enflick.android.TextNow:id/search_field",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "1",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "fc0ce789-e3ad-4f3b-a167-e66c2e7aa099",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 520 to Task 231 action 77

Role: Task 223 exact search wrapper/action 520

Source semantics:

```json
{
  "bundle": {
    "ActionId": "com.enflick.android.TextNow:id/search_field",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "1",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "fc0ce789-e3ad-4f3b-a167-e66c2e7aa099",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "com.enflick.android.TextNow:id/search_field",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "1",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: Id\nValue: com.enflick.android.TextNow:id/search_field\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "fc0ce789-e3ad-4f3b-a167-e66c2e7aa099",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 532 to Task 231 action 91

Role: Task 223 exact search-write/contact wrapper/action 532

Source semantics:

```json
{
  "bundle": {
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%kb_text_selected\nSelected Text\nText selected on the current input, if any</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%kb_text\nText\nText present on the current input, if any</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES2>%kb_text_after_cursor\nText After Cursor\nText after the cursor on the current input, if any</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES2><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES3>%kb_text_before_cursor\nText Before Cursor\nText before the cursor on the current input, if any</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES3></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;"
  },
  "class": "",
  "code": "328",
  "continue_after_error": null,
  "package": "deleteAll(),wait(300),write(%sendsearch)"
}
```

Output semantics:

```json
{
  "bundle": {
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%kb_text_selected\nSelected Text\nText selected on the current input, if any</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%kb_text\nText\nText present on the current input, if any</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES2>%kb_text_after_cursor\nText After Cursor\nText after the cursor on the current input, if any</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES2><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES3>%kb_text_before_cursor\nText Before Cursor\nText before the cursor on the current input, if any</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES3></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;"
  },
  "class": "",
  "code": "328",
  "continue_after_error": null,
  "package": "deleteAll(),wait(300),write(%sendsearch)"
}
```

Result: PASS, field-for-field equal excluding output `sr`.

### Task 223 action 543 to Task 231 action 102

Role: Task 223 exact search-write/contact wrapper/action 543

Source semantics:

```json
{
  "bundle": {
    "ActionId": "1",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "3",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: List\nValue: 1\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "34758ea0-9e05-4ee1-9f7a-b1e4c19e662e",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Output semantics:

```json
{
  "bundle": {
    "ActionId": "1",
    "ActionId-type": "java.lang.String",
    "ActionType": "16",
    "ActionType-type": "java.lang.String",
    "EnableDisableAccessibilityService": "<null>",
    "EnableDisableAccessibilityService-type": "java.lang.String",
    "FieldSelectionType": "3",
    "FieldSelectionType-type": "java.lang.String",
    "IsFirstAction": "false",
    "IsFirstAction-type": "java.lang.Boolean",
    "IsTaskerAction": "false",
    "IsTaskerAction-type": "java.lang.Boolean",
    "NearbyText": "<null>",
    "NearbyText-type": "java.lang.String",
    "Password": "<null>",
    "Password-type": "java.lang.String",
    "RepeatInterval": "<null>",
    "RepeatInterval-type": "java.lang.String",
    "RepeatTimes": "<null>",
    "RepeatTimes-type": "java.lang.String",
    "StoredAction": "<null>",
    "StoredAction-type": "java.lang.String",
    "TextToWrite": "<null>",
    "TextToWrite-type": "java.lang.String",
    "com.twofortyfouram.locale.intent.extra.BLURB": "Type: List\nValue: 1\nAction : Click",
    "com.twofortyfouram.locale.intent.extra.BLURB-type": "java.lang.String",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES": "<StringArray sr=\"\"><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0>%err\nError Code\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES0><_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1>%errmsg\nError Message\nOnly available if you select &lt;b&gt;Continue Task After Error&lt;/b&gt; and the action ends in error</_array_net.dinglisch.android.tasker.RELEVANT_VARIABLES1></StringArray>",
    "net.dinglisch.android.tasker.RELEVANT_VARIABLES-type": "[Ljava.lang.String;",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS": "ActionId FieldSelectionType ActionType plugininstanceid plugintypeid ",
    "net.dinglisch.android.tasker.extras.VARIABLE_REPLACE_KEYS-type": "java.lang.String",
    "net.dinglisch.android.tasker.subbundled": "true",
    "net.dinglisch.android.tasker.subbundled-type": "java.lang.Boolean",
    "plugininstanceid": "34758ea0-9e05-4ee1-9f7a-b1e4c19e662e",
    "plugininstanceid-type": "java.lang.String",
    "plugintypeid": "com.joaomgcd.autoinput.intent.IntentPerformAction",
    "plugintypeid-type": "java.lang.String"
  },
  "class": "com.joaomgcd.autoinput.activity.ActivityConfigPerformAction",
  "code": "1732635924",
  "continue_after_error": "false",
  "package": "com.joaomgcd.autoinput"
}
```

Result: PASS, field-for-field equal excluding output `sr`.
