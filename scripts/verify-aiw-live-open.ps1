param(
  [Parameter(Mandatory = $true)]
  [string]$XmlPath,

  [string]$OutDir = ""
)

$ErrorActionPreference = "Stop"

$resolved = Resolve-Path -LiteralPath $XmlPath
$text = Get-Content -Raw -LiteralPath $resolved

try {
  [xml]$xml = $text
} catch {
  Write-Output "xml_parse: FAIL"
  Write-Output ("error: " + $_.Exception.Message)
  exit 1
}

$tasks = @($xml.SelectNodes("//Task"))
$profiles = @($xml.SelectNodes("//Profile"))
$scenes = @($xml.SelectNodes("//Scene"))

$taskIds = [System.Collections.Generic.HashSet[string]]::new()
$taskNames = [System.Collections.Generic.HashSet[string]]::new()
$duplicateTaskIds = @()
$duplicateTaskNames = @()

foreach ($task in $tasks) {
  $id = $task.SelectSingleNode("id")
  $name = $task.SelectSingleNode("nme")

  if ($id -and -not $taskIds.Add($id.InnerText)) {
    $duplicateTaskIds += $id.InnerText
  }

  if ($name -and -not $taskNames.Add($name.InnerText)) {
    $duplicateTaskNames += $name.InnerText
  }
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
foreach ($action in @($xml.SelectNodes("//Action[code='130']"))) {
  $target = $action.SelectSingleNode("Str[@sr='arg0']")
  if ($target -and $target.InnerText -and -not $taskNames.Contains($target.InnerText)) {
    $sourceName = $action.ParentNode.SelectSingleNode("nme")
    $missingPerformRefs += "$(if ($sourceName) { $sourceName.InnerText } else { 'UNKNOWN_TASK' }) -> $($target.InnerText)"
  }
}

$clickRefs = @([regex]::Matches($text, "<clickTask>(-?\d+)</clickTask>") | ForEach-Object { $_.Groups[1].Value })
$missingClickRefs = @($clickRefs | Where-Object { $_ -notmatch "^-" -and -not $taskIds.Contains($_) } | Sort-Object -Unique)

$project = $xml.SelectSingleNode("//Project")
$definedTasksNotInProject = @()
$definedScenesNotInProject = @()
$projectHasTesterIds = $false

if ($project) {
  $projectTaskIds = [System.Collections.Generic.HashSet[string]]::new()
  $projectSceneNames = [System.Collections.Generic.HashSet[string]]::new()

  $tidsNode = $project.SelectSingleNode("tids")
  if ($tidsNode) {
    foreach ($id in $tidsNode.InnerText.Split(",")) {
      $trimmed = $id.Trim()
      if ($trimmed) {
        [void]$projectTaskIds.Add($trimmed)
      }
    }
  }

  $scenesNode = $project.SelectSingleNode("scenes")
  if ($scenesNode) {
    foreach ($sceneName in $scenesNode.InnerText.Split(",")) {
      $trimmed = $sceneName.Trim()
      if ($trimmed) {
        [void]$projectSceneNames.Add($trimmed)
      }
    }
  }

  if ($projectTaskIds.Count -gt 0) {
    foreach ($task in $tasks) {
      $id = $task.SelectSingleNode("id")
      if ($id -and -not $projectTaskIds.Contains($id.InnerText)) {
        $name = $task.SelectSingleNode("nme")
        $definedTasksNotInProject += "$(if ($name) { $name.InnerText } else { $id.InnerText })"
      }
    }
  }

  if ($projectSceneNames.Count -gt 0) {
    foreach ($scene in $scenes) {
      $name = $scene.SelectSingleNode("nme")
      if ($name -and -not $projectSceneNames.Contains($name.InnerText)) {
        $definedScenesNotInProject += $name.InnerText
      }
    }
  }

  $projectHasTesterIds = @("500", "501", "502", "503" | Where-Object { -not $projectTaskIds.Contains($_) }).Count -eq 0
}

$testerNames = @(
  "TEST HOLD - APP Start AI Worker",
  "TEST HOLD - APP Run Tick Once",
  "TEST HOLD - FINAL Send Sheet LEGACY",
  "TEST HOLD - APP Config Setup"
)
$missingTesterTasks = @($testerNames | Where-Object { -not $taskNames.Contains($_) })

$liveRelatedZeroAssignments = @()
$liveAssignments = @()
foreach ($task in $tasks) {
  $taskNameNode = $task.SelectSingleNode("nme")
  $taskName = if ($taskNameNode) { $taskNameNode.InnerText } else { "UNKNOWN_TASK" }
  foreach ($action in @($task.SelectNodes("Action[code='547']"))) {
    $var = $action.SelectSingleNode("Str[@sr='arg0']")
    $value = $action.SelectSingleNode("Str[@sr='arg1']")
    if ($var -and $var.InnerText -in @("%AIWV19MPhoneLiveHold", "%AIWV19MSendLiveHold", "%AIWAutoLive")) {
      $valueText = if ($value) { $value.InnerText } else { "" }
      $liveAssignments += "$taskName $($action.sr) $($var.InnerText)=$valueText"
      if ($valueText -eq "0") {
        $liveRelatedZeroAssignments += "$taskName $($action.sr) $($var.InnerText)"
      }
    }
  }
}

$hash = Get-FileHash -Algorithm SHA256 -LiteralPath $resolved

$report = [ordered]@{
  file = $resolved.Path
  sha256 = $hash.Hash
  xml_parse = "PASS"
  root = $xml.DocumentElement.Name
  task_count = $tasks.Count
  profile_count = $profiles.Count
  scene_count = $scenes.Count
  duplicate_task_id_count = @($duplicateTaskIds | Sort-Object -Unique).Count
  duplicate_task_name_count = @($duplicateTaskNames | Sort-Object -Unique).Count
  missing_profile_task_refs = $missingProfileRefs.Count
  missing_perform_task_refs = $missingPerformRefs.Count
  click_task_ref_count = $clickRefs.Count
  missing_click_task_refs = $missingClickRefs.Count
  defined_tasks_not_in_project_count = $definedTasksNotInProject.Count
  defined_scenes_not_in_project_count = $definedScenesNotInProject.Count
  tester_tasks_present = ($missingTesterTasks.Count -eq 0)
  project_tids_contains_500_503 = $projectHasTesterIds
  live_related_zero_assignments = $liveRelatedZeroAssignments.Count
  build95_marker_count = ([regex]::Matches($text, "BUILD95")).Count
  build99_marker_count = ([regex]::Matches($text, "BUILD99")).Count
  build100_marker_count = ([regex]::Matches($text, "BUILD100")).Count
  json_true_count = ([regex]::Matches($text, "json:true")).Count
  se_true_count = ([regex]::Matches($text, "<se>true</se>")).Count
  mojibake_A_count = ([regex]::Matches($text, [string][char]0x00C3)).Count
  section_sign_count = ([regex]::Matches($text, [string][char]0x00A7)).Count
  openai_key_marker_present = ($text.Contains("OPENAI_API_KEY") -or $text.Contains("sk-"))
  textnow_marker_count = ([regex]::Matches($text, "TextNow", "IgnoreCase")).Count
  auto_live_tick_present = $text.Contains("AIW AUTO LIVE TICK V1")
}

$lines = @()
$report.GetEnumerator() | ForEach-Object {
  $lines += "{0}: {1}" -f $_.Key, $_.Value
}

$failed = @()
foreach ($key in @(
  "duplicate_task_id_count",
  "duplicate_task_name_count",
  "missing_profile_task_refs",
  "missing_perform_task_refs",
  "missing_click_task_refs",
  "defined_tasks_not_in_project_count",
  "defined_scenes_not_in_project_count",
  "live_related_zero_assignments",
  "build95_marker_count",
  "build99_marker_count",
  "json_true_count",
  "se_true_count",
  "mojibake_A_count"
)) {
  if ([int]$report[$key] -ne 0) {
    $failed += $key
  }
}

if (-not $report["tester_tasks_present"]) {
  $failed += "tester_tasks_present"
}

if (-not $report["project_tids_contains_500_503"]) {
  $failed += "project_tids_contains_500_503"
}

if (-not $report["auto_live_tick_present"]) {
  $failed += "auto_live_tick_present"
}

if ($failed.Count) {
  $lines += "gate_result: FAIL"
  $lines += "failed_gates: " + ($failed -join ",")
} else {
  $lines += "gate_result: PASS"
}

if ($OutDir) {
  $outResolved = Resolve-Path -LiteralPath $OutDir
  $auditPath = Join-Path $outResolved "OPTIMIZED_VERIFY_REPORT.txt"
  $lines | Set-Content -LiteralPath $auditPath -Encoding UTF8
}

$lines | ForEach-Object { Write-Output $_ }

if ($failed.Count) {
  exit 2
}

