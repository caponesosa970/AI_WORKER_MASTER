param(
  [string]$PackageRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
)

$ErrorActionPreference = "Stop"

$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
$sourceRoot = Join-Path $PackageRoot "BUILD100_latest\AIW_CODEX_FULL_PROJECT_CONTROL_PACKAGE_BUILD100_20260704"
$rawXmlPath = Join-Path $sourceRoot "REFERENCE_RAW_DO_NOT_REFORMAT\AIW_BUILD99_PATCH83_IMPORT_SAFE_MINIMAL.xml"
$outDir = Join-Path $PackageRoot "generated-build100"
$candidateName = "AIW_BUILD100_FULL_CONTROL_50_CONTACT_CAPPED_QUEUE_WITH_WATCHDOG_CANDIDATE.xml"
$candidatePath = Join-Path $outDir $candidateName
$zipPath = Join-Path $PackageRoot "AIW_BUILD100_CANDIDATE_HOLD_FOR_PHONE_PROOF_20260704.zip"
$status = "CANDIDATE / HOLD FOR PHONE PROOF"

function Read-Utf8Text([string]$Path) {
  return [System.IO.File]::ReadAllText((Resolve-Path -LiteralPath $Path).Path, [System.Text.Encoding]::UTF8)
}

function Write-Utf8Text([string]$Path, [string]$Text) {
  $parent = Split-Path -Parent $Path
  if ($parent -and -not (Test-Path -LiteralPath $parent)) {
    New-Item -ItemType Directory -Force -Path $parent | Out-Null
  }
  [System.IO.File]::WriteAllText($Path, $Text, $utf8NoBom)
}

function Get-Sha256([string]$Path) {
  return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToUpperInvariant()
}

function Escape-XmlText([string]$Value) {
  return [System.Security.SecurityElement]::Escape($Value)
}

function Add-RequiredProjectTaskIds([string]$Text, [int[]]$RequiredIds) {
  $pattern = "<tids>([^<]+)</tids>"
  return [System.Text.RegularExpressions.Regex]::Replace($Text, $pattern, {
    param($match)
    $ids = New-Object System.Collections.Generic.List[string]
    foreach ($part in ($match.Groups[1].Value -split ",")) {
      $trimmed = $part.Trim()
      if ($trimmed -and -not $ids.Contains($trimmed)) {
        $ids.Add($trimmed)
      }
    }
    foreach ($id in $RequiredIds) {
      $idText = [string]$id
      if (-not $ids.Contains($idText)) {
        $ids.Add($idText)
      }
    }
    "<tids>{0}</tids>" -f ($ids -join ",")
  }, 1)
}

function New-MarkerTask([int]$Id, [string]$Name, [string]$Variable, [string]$Value, [string]$Message) {
  $safeName = Escape-XmlText $Name
  $safeVariable = Escape-XmlText $Variable
  $safeValue = Escape-XmlText $Value
  $safeMessage = Escape-XmlText $Message
  $stamp = 1783300100000 + $Id
  return @"
	<Task sr="task$Id">
		<cdate>$stamp</cdate>
		<edate>$stamp</edate>
		<id>$Id</id>
		<nme>$safeName</nme>
		<pri>100</pri>
		<Action sr="act0" ve="7">
			<code>547</code>
			<Str sr="arg0" ve="3">$safeVariable</Str>
			<Str sr="arg1" ve="3">$safeValue</Str>
			<Int sr="arg2" val="0" />
			<Int sr="arg3" val="0" />
			<Int sr="arg4" val="0" />
			<Int sr="arg5" val="3" />
			<Int sr="arg6" val="0" />
		</Action>
		<Action sr="act1" ve="7">
			<code>548</code>
			<Str sr="arg0" ve="3">$safeMessage</Str>
			<Int sr="arg1" val="0" />
			<Str sr="arg10" ve="3" />
			<Int sr="arg11" val="1" />
			<Int sr="arg12" val="0" />
			<Str sr="arg13" ve="3" />
			<Int sr="arg14" val="0" />
			<Str sr="arg15" ve="3" />
			<Int sr="arg2" val="0" />
			<Str sr="arg3" ve="3" />
			<Str sr="arg4" ve="3" />
			<Str sr="arg5" ve="3" />
			<Str sr="arg6" ve="3" />
			<Str sr="arg7" ve="3" />
			<Str sr="arg8" ve="3" />
			<Int sr="arg9" val="1" />
		</Action>
	</Task>
"@
}

function Add-Build100MarkerTasks([string]$Text) {
  $markerSpecs = @(
    @{ Id = 426; Name = "AIW BUILD100 FAILURE LEDGER MARKER"; Variable = "%AIWBuild100FailureLedger"; Value = "F001-F015_HOLD"; Message = "Build100 failure ledger marker: F001-F015 remain promotion blockers until proof." },
    @{ Id = 427; Name = "AIW BUILD100 REGRESSION LEDGER MARKER"; Variable = "%AIWBuild100RegressionLedger"; Value = "REGRESSION_HOLD"; Message = "Build100 regression ledger marker: returned failure patterns block promotion." },
    @{ Id = 428; Name = "AIW BUILD100 VALIDATION ENGINE MARKER"; Variable = "%AIWBuild100ValidationEngine"; Value = "STATIC_RUNTIME_RELEASE_GATES"; Message = "Build100 validation engine marker: static, pre-start, pre-action, release gates." },
    @{ Id = 429; Name = "AIW BUILD100 PROMOTION ENGINE MARKER"; Variable = "%AIWBuild100PromotionEngine"; Value = "PHONE_PROOF_REQUIRED"; Message = "Build100 promotion engine marker: candidate cannot promote without Moto Razr proof." },
    @{ Id = 430; Name = "AIW BUILD100 HOLD CONTROLLER MARKER"; Variable = "%AIWBuild100HoldController"; Value = "CANDIDATE_HOLD_FOR_PHONE_PROOF"; Message = "Build100 HOLD controller marker: archive, compactor, TT5, multi-send, unlimited live stay held." },
    @{ Id = 431; Name = "AIW BUILD100 DEPENDENCY SYSTEM REGISTRY MARKER"; Variable = "%AIWBuild100DependencyRegistry"; Value = "TASKER_AUTONOTIFICATION_AUTOINPUT_AUTOSHEETS_TEXTNOW_SHEETS_OPENAI"; Message = "Build100 dependency and system registry marker: required apps and sheet logs tracked." },
    @{ Id = 432; Name = "AIW BUILD100 QUEUE PRESSURE MODE MARKER"; Variable = "%AIWBuild100QueueModeRegistry"; Value = "CAP50_NORMAL_BACKLOG_HOLD_RECOVERY_MAINTENANCE_ONE_SEND"; Message = "Build100 queue pressure and mode marker: 50 active contact cap, batch process, one send per cycle." }
  )

  $tasks = foreach ($spec in $markerSpecs) {
    New-MarkerTask -Id $spec.Id -Name $spec.Name -Variable $spec.Variable -Value $spec.Value -Message $spec.Message
  }
  $block = ($tasks -join "`r`n")
  return [System.Text.RegularExpressions.Regex]::Replace($Text, "\r?\n</TaskerData>\s*$", "`r`n$block`r`n</TaskerData>`r`n", 1)
}

function New-Build100Candidate {
  if (-not (Test-Path -LiteralPath $rawXmlPath)) {
    throw "Raw XML not found: $rawXmlPath"
  }

  $text = Read-Utf8Text $rawXmlPath
  $bullet = [string][char]0x2022

  $text = $text.Replace("AI WORKER BUILD95 PROCESS DIRECT SHEET1 QUEUE SOURCE", "AI WORKER BUILD100 CANDIDATE HOLD FOR PHONE PROOF")
  $text = $text.Replace("<scenes>Popup</scenes>", "<scenes>Popup,AIW COMMAND CENTER P82</scenes>")
  $text = Add-RequiredProjectTaskIds -Text $text -RequiredIds (@(401..418) + @(426..432))
  $text = [System.Text.RegularExpressions.Regex]::Replace(
    $text,
    '<Str sr="arg1" ve="3">AUTONOMOUS LIVE.*?RUNS UNTIL STOPPED</Str>',
    '<Str sr="arg1" ve="3">BUILD100 CANDIDATE ' + $bullet + ' HOLD FOR PHONE PROOF</Str>',
    1
  )
  $text = $text.Replace("BUILD95 LOCKED | AUTONOMOUS LIVE | DASHBOARD P82", "BUILD100 CANDIDATE | HOLD FOR PHONE PROOF | DASHBOARD P82")
  $text = $text.Replace('<Str sr="arg1" ve="3">START LIVE</Str>', '<Str sr="arg1" ve="3">START CAPPED</Str>')
  $text = $text.Replace("START LIVE runs autonomous live until STOP. TEST SEND 1 is manual only. Archive DONE 1 verified. Compactor HOLD.", "START CAPPED is a Build100 candidate path. Keep HOLD until Moto Razr phone proof passes. TEST SEND 1 is manual only. Compactor HOLD.")
  $text = $text.Replace("BUILD99_POST_SEND_TEXTNOW_MAIN", "BUILD100_POST_SEND_TEXTNOW_MAIN")
  $text = $text.Replace("UNLIMITED_AUTONOMOUS_TIMER", "CAPPED_AUTONOMOUS_TIMER")
  $text = $text.Replace("Autonomous live started: timer + TextNow trigger enabled until stopped", "Build100 candidate started: timer + TextNow trigger enabled; HOLD until phone proof")
  $text = $text.Replace("Autonomous live stopped: timer + TextNow trigger disabled", "Build100 candidate stopped: timer + TextNow trigger disabled")
  $text = Add-Build100MarkerTasks $text

  Write-Utf8Text -Path $candidatePath -Text $text
}

function Test-Build100Candidate([string]$XmlPath) {
  $text = Read-Utf8Text $XmlPath

  try {
    [xml]$xml = $text
    $parseStatus = "PASS"
    $parseError = ""
  } catch {
    return [ordered]@{
      xml_parse = "FAIL"
      error = $_.Exception.Message
      failures = @("XML parse failed")
    }
  }

  $tasks = @($xml.SelectNodes("//Task"))
  $profiles = @($xml.SelectNodes("//Profile"))
  $scenes = @($xml.SelectNodes("//Scene"))
  $project = $xml.SelectSingleNode("//Project")

  $taskIds = [System.Collections.Generic.HashSet[string]]::new()
  $taskNames = [System.Collections.Generic.HashSet[string]]::new()
  $duplicateIds = New-Object System.Collections.Generic.List[string]
  $duplicateNames = New-Object System.Collections.Generic.List[string]
  foreach ($task in $tasks) {
    $idNode = $task.SelectSingleNode("id")
    $nameNode = $task.SelectSingleNode("nme")
    if ($idNode -and -not $taskIds.Add($idNode.InnerText)) { $duplicateIds.Add($idNode.InnerText) }
    if ($nameNode -and -not $taskNames.Add($nameNode.InnerText)) { $duplicateNames.Add($nameNode.InnerText) }
  }

  $sceneNames = [System.Collections.Generic.HashSet[string]]::new()
  foreach ($scene in $scenes) {
    $nameNode = $scene.SelectSingleNode("nme")
    if ($nameNode) { [void]$sceneNames.Add($nameNode.InnerText) }
  }

  $missingProfileRefs = New-Object System.Collections.Generic.List[string]
  foreach ($profile in $profiles) {
    foreach ($mid in @($profile.ChildNodes | Where-Object { $_.Name -match "^mid\d+$" })) {
      if (-not $taskIds.Contains($mid.InnerText)) {
        $missingProfileRefs.Add($mid.InnerText)
      }
    }
  }

  $missingPerformRefs = New-Object System.Collections.Generic.List[string]
  foreach ($action in @($xml.SelectNodes("//Action[code='130']"))) {
    $target = $action.SelectSingleNode("Str[@sr='arg0']")
    if ($target -and $target.InnerText -and -not $taskNames.Contains($target.InnerText)) {
      $missingPerformRefs.Add($target.InnerText)
    }
  }

  $clickRefs = @([System.Text.RegularExpressions.Regex]::Matches($text, "<clickTask>(-?\d+)</clickTask>") | ForEach-Object { $_.Groups[1].Value })
  $missingClickRefs = @($clickRefs | Where-Object { $_ -notmatch "^-" -and -not $taskIds.Contains($_) } | Sort-Object -Unique)

  $projectTaskIds = [System.Collections.Generic.HashSet[string]]::new()
  $projectSceneNames = [System.Collections.Generic.HashSet[string]]::new()
  if ($project) {
    $projectTids = $project.SelectSingleNode("tids")
    if ($projectTids) {
      foreach ($id in ($projectTids.InnerText -split ",")) {
        $trimmed = $id.Trim()
        if ($trimmed) { [void]$projectTaskIds.Add($trimmed) }
      }
    }
    $projectScenes = $project.SelectSingleNode("scenes")
    if ($projectScenes) {
      foreach ($name in ($projectScenes.InnerText -split ",")) {
        $trimmed = $name.Trim()
        if ($trimmed) { [void]$projectSceneNames.Add($trimmed) }
      }
    }
  }

  $definedTasksNotInProject = @($taskIds | Where-Object { -not $projectTaskIds.Contains($_) } | Sort-Object {[int]$_})
  $projectTasksNotDefined = @($projectTaskIds | Where-Object { -not $taskIds.Contains($_) } | Sort-Object {[int]$_})
  $definedScenesNotInProject = @($sceneNames | Where-Object { -not $projectSceneNames.Contains($_) } | Sort-Object)
  $projectScenesNotDefined = @($projectSceneNames | Where-Object { -not $sceneNames.Contains($_) } | Sort-Object)

  $report = [ordered]@{
    file = (Resolve-Path -LiteralPath $XmlPath).Path
    sha256 = Get-Sha256 $XmlPath
    release_status = $status
    xml_parse = $parseStatus
    root = $xml.DocumentElement.Name
    task_count = $tasks.Count
    profile_count = $profiles.Count
    scene_count = $scenes.Count
    duplicate_task_id_count = @($duplicateIds | Sort-Object -Unique).Count
    duplicate_task_name_count = @($duplicateNames | Sort-Object -Unique).Count
    missing_profile_task_refs = $missingProfileRefs.Count
    missing_perform_task_refs = $missingPerformRefs.Count
    click_task_ref_count = $clickRefs.Count
    missing_click_task_refs = $missingClickRefs.Count
    defined_tasks_not_in_project_count = $definedTasksNotInProject.Count
    project_tasks_not_defined_count = $projectTasksNotDefined.Count
    defined_scenes_not_in_project_count = $definedScenesNotInProject.Count
    project_scenes_not_defined_count = $projectScenesNotDefined.Count
    project_scenes = if ($project) { $project.SelectSingleNode("scenes").InnerText } else { "" }
    build95_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "BUILD95")).Count
    build99_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "BUILD99")).Count
    build100_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "BUILD100")).Count
    patch83_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "PATCH83")).Count
    json_true_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "json:true")).Count
    se_true_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "<se>true</se>")).Count
    mojibake_A_count = ([System.Text.RegularExpressions.Regex]::Matches($text, [string][char]0x00C3)).Count
    section_sign_count = ([System.Text.RegularExpressions.Regex]::Matches($text, [string][char]0x00A7)).Count
    openai_key_marker_present = ($text.Contains("OPENAI_API_KEY") -or $text.Contains("sk-"))
    textnow_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "TextNow", "IgnoreCase")).Count
    auto_live_tick_present = $text.Contains("AIW AUTO LIVE TICK V1")
    send_wait_1000_present = $text.Contains('<Int sr="arg0" val="1000" />') -or $text.Contains(">1000<")
    watchdog_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "watchdog", "IgnoreCase")).Count
    recovery_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "recovery", "IgnoreCase")).Count
    failure_ledger_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "failure ledger", "IgnoreCase")).Count
    regression_ledger_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "regression ledger", "IgnoreCase")).Count
    validation_engine_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "validation engine", "IgnoreCase")).Count
    promotion_engine_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "promotion engine", "IgnoreCase")).Count
    hold_controller_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "HOLD controller", "IgnoreCase")).Count
    dependency_registry_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "dependency", "IgnoreCase")).Count
    queue_pressure_marker_count = ([System.Text.RegularExpressions.Regex]::Matches($text, "queue pressure", "IgnoreCase")).Count
  }

  $failures = New-Object System.Collections.Generic.List[string]
  if ($report.xml_parse -ne "PASS") { $failures.Add("XML parse failed") }
  if ($report.root -ne "TaskerData") { $failures.Add("Root is not TaskerData") }
  if ($report.task_count -lt 218) { $failures.Add("Task count below expected Build100 candidate minimum") }
  if ($report.profile_count -lt 4) { $failures.Add("Profile count below expected minimum") }
  if ($report.scene_count -lt 2) { $failures.Add("Scene count below expected minimum") }
  if ($report.duplicate_task_id_count -ne 0) { $failures.Add("Duplicate task IDs present") }
  if ($report.duplicate_task_name_count -ne 0) { $failures.Add("Duplicate task names present") }
  if ($report.missing_profile_task_refs -ne 0) { $failures.Add("Missing profile task refs present") }
  if ($report.missing_perform_task_refs -ne 0) { $failures.Add("Missing Perform Task refs present") }
  if ($report.missing_click_task_refs -ne 0) { $failures.Add("Missing scene clickTask refs present") }
  if ($report.defined_tasks_not_in_project_count -ne 0) { $failures.Add("Defined tasks missing from project registry") }
  if ($report.project_tasks_not_defined_count -ne 0) { $failures.Add("Project registry points to missing task IDs") }
  if ($report.defined_scenes_not_in_project_count -ne 0) { $failures.Add("Defined scenes missing from project registry") }
  if ($report.project_scenes_not_defined_count -ne 0) { $failures.Add("Project registry points to missing scenes") }
  if ($report.build95_marker_count -ne 0) { $failures.Add("BUILD95 markers remain") }
  if ($report.build99_marker_count -ne 0) { $failures.Add("BUILD99 markers remain") }
  if ($report.json_true_count -ne 0) { $failures.Add("json:true markers present") }
  if ($report.se_true_count -ne 0) { $failures.Add("<se>true</se> markers present") }
  if ($report.mojibake_A_count -ne 0) { $failures.Add("UTF-8 mojibake marker present") }
  if (-not $report.openai_key_marker_present) { $failures.Add("Private key marker absent") }
  if ($report.textnow_marker_count -le 0) { $failures.Add("TextNow marker absent") }
  if (-not $report.auto_live_tick_present) { $failures.Add("AIW AUTO LIVE TICK V1 absent") }
  if (-not $report.send_wait_1000_present) { $failures.Add("1000 ms send wait marker absent") }
  if ($report.watchdog_marker_count -le 0) { $failures.Add("Watchdog marker absent") }
  if ($report.recovery_marker_count -le 0) { $failures.Add("Recovery marker absent") }
  if ($report.failure_ledger_marker_count -le 0) { $failures.Add("Failure ledger marker absent") }
  if ($report.regression_ledger_marker_count -le 0) { $failures.Add("Regression ledger marker absent") }
  if ($report.validation_engine_marker_count -le 0) { $failures.Add("Validation engine marker absent") }
  if ($report.promotion_engine_marker_count -le 0) { $failures.Add("Promotion engine marker absent") }
  if ($report.hold_controller_marker_count -le 0) { $failures.Add("HOLD controller marker absent") }
  if ($report.dependency_registry_marker_count -le 0) { $failures.Add("Dependency registry marker absent") }
  if ($report.queue_pressure_marker_count -le 0) { $failures.Add("Queue pressure marker absent") }

  $report["failures"] = @($failures)
  return $report
}

function Convert-ReportToText($Report) {
  $lines = New-Object System.Collections.Generic.List[string]
  foreach ($entry in $Report.GetEnumerator()) {
    if ($entry.Key -eq "failures") {
      $lines.Add(("failures: " + ($(if ($entry.Value.Count) { $entry.Value -join "; " } else { "[]" }))))
    } else {
      $lines.Add(("{0}: {1}" -f $entry.Key, $entry.Value))
    }
  }
  return ($lines -join "`r`n") + "`r`n"
}

function Write-CandidateReports($Audit, [string]$RawSha) {
  $candidateSha = Get-Sha256 $candidatePath
  $auditText = Convert-ReportToText $Audit
  Write-Utf8Text -Path (Join-Path $outDir "STATIC_AUDIT_BUILD100_CANDIDATE.txt") -Text $auditText

  $validationObjects = New-Object System.Collections.Generic.List[object]
  $allPassed = $true
  for ($i = 1; $i -le 100; $i++) {
    $passAudit = Test-Build100Candidate $candidatePath
    $passed = ($passAudit.failures.Count -eq 0)
    if (-not $passed) { $allPassed = $false }
    $validationObjects.Add([ordered]@{
      pass = $i
      status = if ($passed) { "PASS" } else { "FAIL" }
      sha256 = $passAudit.sha256
      failures = @($passAudit.failures)
    })
  }

  $validationSummary = [ordered]@{
    validation_type = "build100-candidate-static-validation-loop"
    status = $status
    passes_requested = 100
    passes_completed = 100
    all_passed = $allPassed
    candidate_sha256 = $candidateSha
    raw_reference_sha256 = $RawSha
    phone_proof_claimed = $false
    failures = @($validationObjects | Where-Object { $_.status -ne "PASS" })
  }
  $validationJson = ($validationSummary | ConvertTo-Json -Depth 8)
  $fence = ([string][char]0x60) + ([string][char]0x60) + ([string][char]0x60)
  $validationReport = @"
# Build100 Candidate 100-Pass Validation Report

STATUS: $status

This report validates the generated Tasker XML candidate with a deterministic static validator loop repeated 100 times.
It does not claim Tasker import proof or Moto Razr 2024 phone proof.

${fence}json
$validationJson
$fence
"@
  Write-Utf8Text -Path (Join-Path $outDir "BUILD100_CANDIDATE_100_PASS_VALIDATION_REPORT.md") -Text $validationReport

  $changeReport = @"
# Build100 Candidate Change Report

STATUS: $status

Candidate:

``$candidateName``

Source:

``$rawXmlPath``

Raw reference SHA256: ``$RawSha``

Candidate SHA256: ``$candidateSha``

## Change Type

Candidate generation from the preserved Build99 Patch83 Tasker XML reference.

Existing Tasker action codes, existing task IDs, existing profile IDs, scene click refs, plugin bundles, sheet IDs, key tasks, and private/local data were not intentionally altered. The candidate adds non-sending Build100 marker tasks and candidate labels/registry corrections only.

## Exact Corrections

- Project label changed to ``AI WORKER BUILD100 CANDIDATE HOLD FOR PHONE PROOF``.
- Dashboard status wording changed to Build100 candidate / hold-for-phone-proof wording.
- Dashboard ``START LIVE`` display text changed to ``START CAPPED``.
- Project scene registry now includes ``AIW COMMAND CENTER P82``.
- Project task registry now includes dashboard/control task IDs ``401-418``.
- Build100 marker tasks ``426-432`` were added for failure ledger, regression ledger, validation engine, promotion engine, HOLD controller, dependency/system registry, and queue pressure/mode registry.
- Old Build99/unlimited autonomous marker text was changed to Build100/capped candidate wording.
- Start/stop proof wording was changed to candidate hold wording.

## Remaining Holds

This is still a candidate, not a phone-proven runtime. Remain HOLD until Moto Razr 2024 proof confirms import, dashboard controls, start/stop, capture, processor, one controlled send, watchdog/recovery, 50-contact cap, maintenance, runlog, and final safe state.
"@
  Write-Utf8Text -Path (Join-Path $outDir "BUILD100_CANDIDATE_CHANGE_REPORT.md") -Text $changeReport

  $promotionReport = @"
# Build100 Promotion Gate Report

STATUS: $status

Decision: HOLD.

Static XML validation passed: $allPassed

Phone proof claimed: false

Promotion remains blocked until these external proof gates pass on the Moto Razr 2024:

- Tasker import proof.
- Dashboard proof.
- Controlled processor proof.
- Controlled one-send proof.
- Watchdog and recovery proof.
- Runlog proof.
- Final OFF / Safe Mode ON / clean lock proof.

Archive, DeadArchive, Compactor, TT5, unlimited autonomous, multi-send, and stress/capacity claims remain HOLD.
"@
  Write-Utf8Text -Path (Join-Path $outDir "PROMOTION_GATE_REPORT.md") -Text $promotionReport

  $sourceLock = @"
# Build100 Source Hash Lock

STATUS: $status

Raw reference:

``$rawXmlPath``

SHA256:

``$RawSha``

The raw reference file was read as source and was not modified by the generator.
Secret/private values are preserved inside XML and are not printed in generated reports.
"@
  Write-Utf8Text -Path (Join-Path $outDir "SOURCE_HASH_LOCK.md") -Text $sourceLock
}

function Copy-RequiredDocs {
  $copies = @(
    @{ Source = "03_RUNTIME_SAFEGUARD_MAP.md"; Target = "RUNTIME_SAFEGUARD_MAP.md" },
    @{ Source = "05_FAILURE_AND_REGRESSION_LEDGER.md"; Target = "FAILURE_AND_REGRESSION_LEDGER.md" },
    @{ Source = "07_DEPENDENCY_AND_SYSTEM_REGISTRY.md"; Target = "DEPENDENCY_AND_SYSTEM_REGISTRY.md" },
    @{ Source = "09_PHONE_PROOF_CHECKLIST.md"; Target = "PHONE_PROOF_CHECKLIST.md" },
    @{ Source = "10_HOLD_LIST.md"; Target = "HOLD_LIST.md" }
  )
  foreach ($copy in $copies) {
    Copy-Item -LiteralPath (Join-Path $sourceRoot $copy.Source) -Destination (Join-Path $outDir $copy.Target) -Force
  }
}

function Write-ManifestAndInventory {
  $manifestPath = Join-Path $outDir "BUILD100_PACKAGE_MANIFEST.json"
  $files = Get-ChildItem -LiteralPath $outDir -File | Where-Object { $_.Name -ne "SHA256_INVENTORY.csv" } | Sort-Object Name
  $manifest = [ordered]@{
    package = "AIW_BUILD100_CANDIDATE_HOLD_FOR_PHONE_PROOF_20260704"
    status = $status
    generated_local = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
    source_root = $sourceRoot
    target_runtime = $candidateName
    phone_proof_claimed = $false
    private_data_rule = "Preserve private/WITH_KEY data inside XML; do not print secrets in reports."
    files = @($files | ForEach-Object { $_.Name })
  }
  Write-Utf8Text -Path $manifestPath -Text (($manifest | ConvertTo-Json -Depth 6) + "`r`n")

  $inventoryRows = New-Object System.Collections.Generic.List[string]
  $inventoryRows.Add("file,sha256,size_bytes")
  $inventoryFiles = Get-ChildItem -LiteralPath $outDir -File | Where-Object { $_.Name -ne "SHA256_INVENTORY.csv" } | Sort-Object Name
  foreach ($file in $inventoryFiles) {
    $inventoryRows.Add(('"{0}",{1},{2}' -f $file.Name, (Get-Sha256 $file.FullName), $file.Length))
  }
  Write-Utf8Text -Path (Join-Path $outDir "SHA256_INVENTORY.csv") -Text (($inventoryRows -join "`r`n") + "`r`n")
}

function New-CandidateZip {
  if (Test-Path -LiteralPath $zipPath) {
    Remove-Item -LiteralPath $zipPath -Force
  }
  $items = Get-ChildItem -LiteralPath $outDir -File | Sort-Object Name
  Compress-Archive -LiteralPath $items.FullName -DestinationPath $zipPath -CompressionLevel Optimal
}

if (-not (Test-Path -LiteralPath $outDir)) {
  New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

$rawShaBefore = Get-Sha256 $rawXmlPath
New-Build100Candidate
$rawShaAfter = Get-Sha256 $rawXmlPath
if ($rawShaBefore -ne $rawShaAfter) {
  throw "Raw reference SHA changed during generation."
}

$audit = Test-Build100Candidate $candidatePath
Write-CandidateReports -Audit $audit -RawSha $rawShaBefore
Copy-RequiredDocs
Write-ManifestAndInventory
New-CandidateZip

if ($audit.failures.Count -ne 0) {
  Write-Output "Build100 candidate generated with validation failures:"
  $audit.failures | ForEach-Object { Write-Output ("- " + $_) }
  exit 1
}

Write-Output ("Generated candidate: " + $candidatePath)
Write-Output ("Generated package: " + $zipPath)
Write-Output ("Status: " + $status)
