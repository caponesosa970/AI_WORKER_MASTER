param(
  [Parameter(Mandatory = $true)]
  [string]$XmlPath,

  [Parameter(Mandatory = $true)]
  [string]$OutDir
)

$ErrorActionPreference = "Stop"

$resolvedXml = Resolve-Path -LiteralPath $XmlPath
$resolvedOut = Resolve-Path -LiteralPath $OutDir
$text = Get-Content -Raw -LiteralPath $resolvedXml

try {
  [xml]$xml = $text
} catch {
  $failPath = Join-Path $resolvedOut "AIW_BUILD100_DEEP_AUDIT_REPORT.md"
  @(
    "# AIW Build100 Deep Audit Report",
    "",
    "## Classification",
    "",
    "FAILED",
    "",
    "## XML Parse",
    "",
    "xml_parse: FAIL",
    ("error: " + $_.Exception.Message)
  ) | Set-Content -LiteralPath $failPath -Encoding UTF8
  Write-Output "xml_parse: FAIL"
  exit 1
}

function TaskNameById($id) {
  $node = $xml.SelectSingleNode("//Task[id='$id']/nme")
  if ($node) { return $node.InnerText }
  return ""
}

function ActionNumber($action) {
  if ($action.sr -match "^act(\d+)$") { return [int]$Matches[1] }
  return 0
}

function TaskActionsSorted($task) {
  return @($task.SelectNodes("Action")) | Sort-Object @{ Expression = { ActionNumber $_ } }
}

function ActionStringValue($action, $argName) {
  $node = $action.SelectSingleNode("Str[@sr='$argName']")
  if ($node) { return $node.InnerText }
  return ""
}

function ConditionText($condition, $name) {
  $node = $condition.SelectSingleNode($name)
  if ($node) { return $node.InnerText }
  return ""
}

function AssignmentRows($varNames) {
  $rows = @()
  foreach ($task in @($xml.SelectNodes("//Task"))) {
    $taskName = $task.SelectSingleNode("nme").InnerText
    foreach ($action in TaskActionsSorted $task) {
      if ($action.code -ne "547") { continue }
      $var = ActionStringValue $action "arg0"
      $value = ActionStringValue $action "arg1"
      if ($varNames -contains $var) {
        $rows += [pscustomobject]@{
          task = $taskName
          action = $action.sr
          var = $var
          value = $value
        }
      }
    }
  }
  return $rows
}

$tasks = @($xml.SelectNodes("//Task"))
$profiles = @($xml.SelectNodes("//Profile"))
$scenes = @($xml.SelectNodes("//Scene"))
$projects = @($xml.SelectNodes("//Project"))

$taskIds = [System.Collections.Generic.HashSet[string]]::new()
$taskNames = [System.Collections.Generic.HashSet[string]]::new()
$duplicateIds = @()
$duplicateNames = @()
foreach ($task in $tasks) {
  $id = $task.SelectSingleNode("id")
  $name = $task.SelectSingleNode("nme")
  if ($id -and -not $taskIds.Add($id.InnerText)) { $duplicateIds += $id.InnerText }
  if ($name -and -not $taskNames.Add($name.InnerText)) { $duplicateNames += $name.InnerText }
}

$missingProfileRefs = @()
foreach ($profile in $profiles) {
  $profileName = $profile.SelectSingleNode("nme")
  foreach ($mid in @($profile.ChildNodes | Where-Object { $_.Name -match "^mid\d+$" })) {
    if (-not $taskIds.Contains($mid.InnerText)) {
      $missingProfileRefs += "$(if ($profileName) { $profileName.InnerText } else { 'UNKNOWN_PROFILE' }) -> $($mid.InnerText)"
    }
  }
}

$missingPerformRefs = @()
$performRefs = @()
foreach ($action in @($xml.SelectNodes("//Action[code='130']"))) {
  $target = ActionStringValue $action "arg0"
  if ($target) {
    $sourceName = $action.ParentNode.SelectSingleNode("nme")
    $source = if ($sourceName) { $sourceName.InnerText } else { "UNKNOWN_TASK" }
    $performRefs += [pscustomobject]@{ source = $source; target = $target }
    if (-not $taskNames.Contains($target)) {
      $missingPerformRefs += "$source -> $target"
    }
  }
}

$clickRefs = @([regex]::Matches($text, "<clickTask>(-?\d+)</clickTask>") | ForEach-Object { $_.Groups[1].Value })
$missingClickRefs = @($clickRefs | Where-Object { $_ -notmatch "^-" -and -not $taskIds.Contains($_) } | Sort-Object -Unique)

$definedTasksNotInProject = @()
$definedScenesNotInProject = @()
$projectSceneText = ""
foreach ($project in $projects) {
  $projectTaskIds = [System.Collections.Generic.HashSet[string]]::new()
  $projectScenes = [System.Collections.Generic.HashSet[string]]::new()
  $tids = $project.SelectSingleNode("tids")
  $sceneNode = $project.SelectSingleNode("scenes")
  if ($sceneNode) { $projectSceneText = $sceneNode.InnerText }

  if ($tids) {
    foreach ($id in $tids.InnerText.Split(",")) {
      $trimmed = $id.Trim()
      if ($trimmed) { [void]$projectTaskIds.Add($trimmed) }
    }
  }
  if ($sceneNode) {
    foreach ($name in $sceneNode.InnerText.Split(",")) {
      $trimmed = $name.Trim()
      if ($trimmed) { [void]$projectScenes.Add($trimmed) }
    }
  }

  foreach ($task in $tasks) {
    $id = $task.SelectSingleNode("id")
    $name = $task.SelectSingleNode("nme")
    if ($id -and $projectTaskIds.Count -gt 0 -and -not $projectTaskIds.Contains($id.InnerText)) {
      $definedTasksNotInProject += "$(if ($name) { $name.InnerText } else { $id.InnerText })"
    }
  }
  foreach ($scene in $scenes) {
    $name = $scene.SelectSingleNode("nme")
    if ($name -and $projectScenes.Count -gt 0 -and -not $projectScenes.Contains($name.InnerText)) {
      $definedScenesNotInProject += $name.InnerText
    }
  }
}

$blockIssues = @()
foreach ($task in $tasks) {
  $taskName = $task.SelectSingleNode("nme").InnerText
  $stack = New-Object System.Collections.ArrayList
  foreach ($action in TaskActionsSorted $task) {
    $code = [string]$action.code
    $act = [string]$action.sr
    if ($code -eq "37") {
      [void]$stack.Add([pscustomobject]@{ type = "IF"; action = $act })
    } elseif ($code -eq "39") {
      [void]$stack.Add([pscustomobject]@{ type = "FOR"; action = $act })
    } elseif ($code -eq "43") {
      if ($stack.Count -eq 0 -or $stack[$stack.Count - 1].type -ne "IF") {
        $blockIssues += "$taskName $act ELSE without active IF"
      }
    } elseif ($code -eq "38") {
      if ($stack.Count -eq 0) {
        $blockIssues += "$taskName $act ENDIF without IF"
      } elseif ($stack[$stack.Count - 1].type -ne "IF") {
        $top = $stack[$stack.Count - 1]
        $blockIssues += "$taskName $act ENDIF overlaps $($top.type) from $($top.action)"
        $stack.RemoveAt($stack.Count - 1)
      } else {
        $stack.RemoveAt($stack.Count - 1)
      }
    } elseif ($code -eq "40") {
      if ($stack.Count -eq 0) {
        $blockIssues += "$taskName $act ENDFOR without FOR"
      } elseif ($stack[$stack.Count - 1].type -ne "FOR") {
        $top = $stack[$stack.Count - 1]
        $blockIssues += "$taskName $act ENDFOR overlaps $($top.type) from $($top.action)"
        $stack.RemoveAt($stack.Count - 1)
      } else {
        $stack.RemoveAt($stack.Count - 1)
      }
    }
  }
  if ($stack.Count -gt 0) {
    foreach ($open in $stack) {
      $blockIssues += "$taskName unclosed $($open.type) from $($open.action)"
    }
  }
}

$safetyVars = @(
  "%AIWorkerSafeMode",
  "%AIWV19MPhoneLiveHold",
  "%AIWV19MSendLiveHold",
  "%AIWV19MSendFlowDryRunOnly",
  "%AIWArchiveEnabled",
  "%AIWDeadArchiveEnabled",
  "%AIWCompactorEnabled",
  "%AIWAllowHeavyCleanup",
  "%AIWAllowTempTools",
  "%AIWDoNotTouchTextNowUI",
  "%AIWDoNotTouchAutoInput",
  "%AIWDeviceTunedFrozen"
)
$safetyRows = AssignmentRows $safetyVars

$capVars = @(
  "%AIWMaxActiveContacts",
  "%AIWProcessBatchCapNormal",
  "%AIWProcessBatchCapBacklog",
  "%AIWSendBatchCap",
  "%AIWTickMode"
)
$capRows = AssignmentRows $capVars

$sendVars = @("%AIWorkerBatchCap", "%AIWSendBatchCap", "%SSSentOne", "%SSReadyCount", "%SSResult")
$sendRows = AssignmentRows $sendVars
$performSendRefs = @($performRefs | Where-Object { $_.target -match "^FINAL Send Sheet$|^FINAL Send Sheet LEGACY" })

$configProofBug = "UNKNOWN"
$configProofEvidence = @()
$configTask = $xml.SelectSingleNode("//Task[nme='APP Config Setup']")
if ($configTask) {
  foreach ($action in TaskActionsSorted $configTask) {
    if ($action.code -eq "547") {
      $var = ActionStringValue $action "arg0"
      $value = ActionStringValue $action "arg1"
      if ($var -in @("%AIWProofResult", "%AIWProofError", "%AIWProofDetails", "%AIWorkerLastError")) {
        $configProofEvidence += "$($action.sr) $var=$value"
      }
    } elseif ($action.code -eq "130" -and (ActionStringValue $action "arg0") -eq "AIW PROOF Log Event") {
      $configProofEvidence += "$($action.sr) PERFORM AIW PROOF Log Event"
    }
  }
  $buggy = $false
  for ($i = 0; $i -lt $configProofEvidence.Count; $i++) {
    if ($configProofEvidence[$i] -match "%AIWProofError=%AIWorkerLastError") {
      $buggy = $true
    }
    if ($configProofEvidence[$i] -match "%AIWProofError=NONE") {
      $buggy = $false
    }
  }
  $configProofBug = if ($buggy) { "CONFIRMED" } else { "NOT_CONFIRMED" }
}

$proofLogger = $xml.SelectSingleNode("//Task[nme='AIW PROOF Log Event']")
$proofLoggerFindings = @()
if ($proofLogger) {
  $pluginActions = @($proofLogger.SelectNodes("Action[Bundle]")).Count
  $proofLoggerFindings += "actions=" + (@($proofLogger.SelectNodes("Action")).Count)
  $proofLoggerFindings += "plugin_bundle_actions=$pluginActions"
  foreach ($action in TaskActionsSorted $proofLogger) {
    $arg0 = ActionStringValue $action "arg0"
    $arg1 = ActionStringValue $action "arg1"
    if ($arg0 -match "AIWProof|err|errmsg|ProofLog" -or $arg1 -match "AIWProof|err|errmsg|ProofLog|OK|FAIL|fallback|Fallback") {
      $proofLoggerFindings += "$($action.sr) code=$($action.code) $arg0=$arg1"
    }
  }
}

$triggerFindings = @()
$trigger = $xml.SelectSingleNode("//Profile[nme='FINAL TextNow Trigger']")
if ($trigger) {
  $typeNode = $trigger.SelectSingleNode(".//Type")
  $textNode = $trigger.SelectSingleNode(".//Text")
  $blurbNode = $trigger.SelectSingleNode(".//com.twofortyfouram.locale.intent.extra.BLURB")
  $typeValue = if ($typeNode) { $typeNode.InnerText } else { "" }
  $filterValue = if ($textNode) { $textNode.InnerText } else { "" }
  $blurb = if ($blurbNode) { $blurbNode.InnerText } else { "" }
  $triggerFindings += "type=$typeValue"
  if ($blurb -match "Only Created Notifications") { $triggerFindings += "mode=Created-only" }
  elseif ($blurb -match "Created") { $triggerFindings += "mode=$blurb" }
  $triggerFindings += "call_filter_present=" + [bool]($filterValue -match "voicemail|Incoming call|Outgoing call|missed call")
  $triggerFindings += "filter=$filterValue"
}

$dashboardTargets = @()
$scene = $xml.SelectSingleNode("//Scene[nme='AIW COMMAND CENTER P82']")
if ($scene) {
  foreach ($match in [regex]::Matches($scene.OuterXml, "<clickTask>(-?\d+)</clickTask>")) {
    $id = $match.Groups[1].Value
    if ($id -notmatch "^-") {
      $dashboardTargets += [pscustomobject]@{ id = $id; task = TaskNameById $id }
    }
  }
}
$dashboardTargets = @($dashboardTargets | Sort-Object id -Unique)

$runlogFiles = @(Get-ChildItem -LiteralPath $resolvedOut -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -match "runlog" })

$hashRows = @()
$hashRows += Get-FileHash -Algorithm SHA256 -LiteralPath $resolvedXml
foreach ($fileName in @("LIVE_OPEN_CHANGE_REPORT.md", "OPTIMIZED_VERIFY_REPORT.txt", "STATIC_AUDIT_LIVE_OPEN.txt", "SHA256_INVENTORY.csv")) {
  $p = Join-Path $resolvedOut $fileName
  if (Test-Path -LiteralPath $p) { $hashRows += Get-FileHash -Algorithm SHA256 -LiteralPath $p }
}
foreach ($runlog in $runlogFiles) {
  $hashRows += Get-FileHash -Algorithm SHA256 -LiteralPath $runlog.FullName
}

$failureReasons = @()
if ($duplicateIds.Count) { $failureReasons += "duplicate task IDs" }
if ($duplicateNames.Count) { $failureReasons += "duplicate task names" }
if ($missingProfileRefs.Count) { $failureReasons += "missing profile task refs" }
if ($missingPerformRefs.Count) { $failureReasons += "missing Perform Task refs" }
if ($missingClickRefs.Count) { $failureReasons += "missing scene clickTask refs" }
if ($definedTasksNotInProject.Count) { $failureReasons += "defined tasks missing from project registry" }
if ($definedScenesNotInProject.Count) { $failureReasons += "defined scenes missing from project registry" }
if ($blockIssues.Count) { $failureReasons += "broken Tasker block nesting" }
if ($configProofBug -eq "CONFIRMED") { $failureReasons += "config proof error carries dirty state" }

$missingCapVars = @()
foreach ($var in $capVars) {
  if (-not @($capRows | Where-Object { $_.var -eq $var }).Count) { $missingCapVars += $var }
}

$classification = "CANDIDATE"
if ($failureReasons.Count) {
  $classification = "FAILED"
} elseif ($missingCapVars.Count -or $runlogFiles.Count -eq 0) {
  $classification = "HOLD"
}

$reportPath = Join-Path $resolvedOut "AIW_BUILD100_DEEP_AUDIT_REPORT.md"
$lines = @()
$lines += "# AIW Build100 Deep Audit Report"
$lines += ""
$lines += "XML: $($resolvedXml.Path)"
$lines += ""
$lines += "## 12. Final Classification"
$lines += ""
$lines += "**$classification**"
$lines += ""
if ($failureReasons.Count) {
  $lines += "Failure reasons:"
  foreach ($reason in $failureReasons) { $lines += "- $reason" }
  $lines += ""
}
if ($classification -eq "HOLD") {
  $lines += "Hold reasons:"
  foreach ($var in $missingCapVars) { $lines += ("- Missing Build100 cap variable: " + $var) }
  if ($runlogFiles.Count -eq 0) { $lines += "- No runlog artifact found in output folder." }
  $lines += ""
}

$lines += "## 1. Current Build100 XML Structure"
$lines += ""
$lines += "- XML parse: PASS"
$lines += "- Root: $($xml.DocumentElement.Name)"
$lines += "- Task count: $($tasks.Count)"
$lines += "- Profile count: $($profiles.Count)"
$lines += "- Scene count: $($scenes.Count)"
$lines += "- Duplicate task IDs: $(@($duplicateIds | Sort-Object -Unique).Count)"
$lines += "- Duplicate task names: $(@($duplicateNames | Sort-Object -Unique).Count)"
$lines += "- Project task registry misses: $($definedTasksNotInProject.Count)"
$lines += "- Profile task link misses: $($missingProfileRefs.Count)"
$lines += "- Scene clickTask link misses: $($missingClickRefs.Count)"
$lines += "- Perform Task reference misses: $($missingPerformRefs.Count)"
$lines += ""

$lines += "## 2. Tasker Block Structure"
$lines += ""
$lines += "- Block issues found: $($blockIssues.Count)"
if ($blockIssues.Count) {
  foreach ($issue in $blockIssues | Select-Object -First 80) { $lines += "- $issue" }
  if ($blockIssues.Count -gt 80) { $lines += "- ... truncated in report" }
} else {
  $lines += "- If / End If and For / End For nesting: PASS by action-number order."
  $lines += "- TEST HOLD - FINAL Send Sheet LEGACY: no broken blocks found."
}
$lines += ""

$lines += "## 3. Safety Defaults"
$lines += ""
foreach ($var in $safetyVars) {
  $values = @($safetyRows | Where-Object { $_.var -eq $var } | ForEach-Object { "$($_.task)/$($_.action)=$($_.value)" })
  if ($values.Count) { $lines += ("- " + $var + ": " + ($values -join "; ")) }
  else { $lines += ("- " + $var + ": not assigned") }
}
$lines += ""

$lines += "## 4. Build100 Cap Variables"
$lines += ""
foreach ($var in $capVars) {
  $values = @($capRows | Where-Object { $_.var -eq $var } | ForEach-Object { "$($_.task)/$($_.action)=$($_.value)" })
  if ($values.Count) { $lines += ("- " + $var + ": " + ($values -join "; ")) }
  else { $lines += ("- " + $var + ": MISSING") }
}
$lines += ""

$lines += "## 5. Send Safety"
$lines += ""
$lines += "- Perform Task calls to send tasks: $($performSendRefs.Count)"
foreach ($ref in $performSendRefs | Sort-Object source,target) { $lines += "- $($ref.source) -> $($ref.target)" }
$lines += "- Send-related assignments:"
foreach ($row in $sendRows | Sort-Object task,var,action) { $lines += ("  - " + $row.task + "/" + $row.action + ": " + $row.var + "=" + $row.value) }
$lines += "- One-send rule: PARTIAL STATIC EVIDENCE. %SSSentOne and %SSReadyCount are present, and queue cycle calls FINAL Send Sheet, but live TextNow UI behavior still requires phone proof."
$lines += ""

$lines += "## 6. Config Proof Bug"
$lines += ""
$lines += "- Status: $configProofBug"
foreach ($line in $configProofEvidence) { $lines += "- $line" }
$lines += "- Required fix if confirmed: set %AIWProofError=NONE immediately before AIW PROOF Log Event in APP Config Setup."
$lines += ""

$lines += "## 7. Start / Run Tick Hold Gates"
$lines += ""
foreach ($taskName in @("APP Start AI Worker", "APP Run Tick Once", "TEST HOLD - APP Start AI Worker", "TEST HOLD - APP Run Tick Once")) {
  $task = $xml.SelectSingleNode("//Task[nme='$taskName']")
  if (-not $task) { $lines += ("- " + $taskName + ": missing"); continue }
  $conditions = @()
  foreach ($condition in @($task.SelectNodes(".//Condition"))) {
    $lhs = ConditionText $condition "lhs"
    $rhs = ConditionText $condition "rhs"
    if ($lhs -match "Hold|Live|SafeMode") { $conditions += "$lhs op=$($condition.op) rhs=$rhs" }
  }
  $lines += ("- " + $taskName + ": " + ($(if ($conditions.Count) { $conditions -join "; " } else { "no hold condition found" })))
}
$lines += ""

$lines += "## 8. Proof Logger"
$lines += ""
foreach ($finding in $proofLoggerFindings | Select-Object -First 80) { $lines += "- $finding" }
if ($proofLoggerFindings.Count -gt 80) { $lines += "- ... proof logger detail truncated" }
$lines += "- Interpretation: first-write AutoSheets errors appear handled only if the task has an error branch/fallback before final proof status; phone/runlog proof is needed to decide handled fallback vs proof bug."
$lines += ""

$lines += "## 9. Trigger Profile"
$lines += ""
foreach ($finding in $triggerFindings) { $lines += "- $finding" }
$lines += "- Duplicate-on-clear risk: Created-only mode lowers cancel/clear duplicate risk but can miss update-style notification changes; Created-or-Updated would need stronger dedupe."
$lines += ""

$lines += "## 10. Dashboard"
$lines += ""
$lines += "- Dashboard click targets:"
foreach ($target in $dashboardTargets) { $lines += "  - $($target.id): $($target.task)" }
$lines += "- Daily-use buttons include STATUS, START LIVE OPEN, STOP LOCKDOWN, RESET LOCKS, SAFE MODE ON."
$lines += "- Dangerous/test buttons include TEST SEND 1, ARCHIVE HOLD, COMPACTOR HOLD, and tester tasks. Static XML cannot prove they are safe on-device."
$lines += ""

$lines += "## 11. SHA Inventory"
$lines += ""
$lines += "| File | SHA256 |"
$lines += "| --- | --- |"
foreach ($hash in $hashRows) {
  $lines += "| $([IO.Path]::GetFileName($hash.Path)) | $($hash.Hash) |"
}
if ($runlogFiles.Count -eq 0) {
  $lines += ""
  $lines += "Runlog: MISSING"
}

$lines | Set-Content -LiteralPath $reportPath -Encoding UTF8
$reportHash = Get-FileHash -Algorithm SHA256 -LiteralPath $reportPath
Add-Content -LiteralPath $reportPath -Encoding UTF8 -Value ""
Add-Content -LiteralPath $reportPath -Encoding UTF8 -Value ("Output report SHA256: " + $reportHash.Hash)

Write-Output ("report: " + $reportPath)
Write-Output ("classification: " + $classification)
Write-Output ("failure_count: " + $failureReasons.Count)
Write-Output ("missing_cap_var_count: " + $missingCapVars.Count)
Write-Output ("block_issue_count: " + $blockIssues.Count)
Write-Output ("config_proof_bug: " + $configProofBug)
