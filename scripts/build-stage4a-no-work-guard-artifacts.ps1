param(
  [Parameter(Mandatory = $true)] [string]$PatchedXml,
  [Parameter(Mandatory = $true)] [string]$SourceXml,
  [Parameter(Mandatory = $true)] [string]$OutDir,
  [Parameter(Mandatory = $true)] [string]$PackagePath
)

$ErrorActionPreference = 'Stop'

function Write-TextFile {
  param([string]$Path, [string[]]$Lines)
  $dir = Split-Path -Parent $Path
  if (-not (Test-Path -LiteralPath $dir)) {
    New-Item -ItemType Directory -Path $dir | Out-Null
  }
  [IO.File]::WriteAllText($Path, ($Lines -join "`r`n"), [Text.UTF8Encoding]::new($false))
}

function ActNum {
  param([System.Xml.XmlElement]$Action)
  return [int](($Action.GetAttribute('sr')) -replace '^act', '')
}

function ActionsSorted {
  param([System.Xml.XmlElement]$Task)
  return @($Task.SelectNodes('Action')) | Sort-Object { ActNum $_ }
}

function StrArg {
  param([System.Xml.XmlElement]$Action, [string]$Arg)
  $node = $Action.SelectSingleNode("Str[@sr='$Arg']")
  if ($node) { return $node.InnerText }
  return ''
}

function TaskByName {
  param([System.Xml.XmlDocument]$Doc, [string]$Name)
  $matches = @($Doc.SelectNodes('//Task') | Where-Object { $_.nme -eq $Name })
  if ($matches.Count -eq 1) { return $matches[0] }
  return $null
}

function CountText {
  param([string]$Text, [string]$Pattern)
  return ([regex]::Matches($Text, $Pattern)).Count
}

if (-not (Test-Path -LiteralPath $OutDir)) {
  New-Item -ItemType Directory -Path $OutDir | Out-Null
}

$patched = (Resolve-Path -LiteralPath $PatchedXml).Path
$source = (Resolve-Path -LiteralPath $SourceXml).Path
$text = [IO.File]::ReadAllText($patched, [Text.Encoding]::UTF8)
[xml]$xml = $text

$tasks = @($xml.SelectNodes('//Task'))
$profiles = @($xml.SelectNodes('//Profile'))
$scenes = @($xml.SelectNodes('//Scene'))
$projects = @($xml.SelectNodes('//Project'))

$taskIds = [System.Collections.Generic.HashSet[string]]::new()
$taskNames = [System.Collections.Generic.HashSet[string]]::new()
$taskNameById = @{}
$duplicateTaskIds = @()
$duplicateTaskNames = @()
foreach ($task in $tasks) {
  $id = [string]$task.id
  $name = [string]$task.nme
  $taskNameById[$id] = $name
  if (-not $taskIds.Add($id)) { $duplicateTaskIds += $id }
  if (-not $taskNames.Add($name)) { $duplicateTaskNames += $name }
}

$missingProfileRefs = @()
foreach ($profile in $profiles) {
  $profileName = [string]$profile.nme
  foreach ($mid in @($profile.ChildNodes | Where-Object { $_.Name -match '^mid\d+$' })) {
    if (-not $taskIds.Contains($mid.InnerText)) {
      $missingProfileRefs += "$profileName -> $($mid.InnerText)"
    }
  }
}

$performRefs = @()
$missingPerformRefs = @()
foreach ($action in @($xml.SelectNodes("//Action[code='130']"))) {
  $target = StrArg $action 'arg0'
  if (-not $target) { continue }
  $sourceTask = [string]$action.ParentNode.nme
  $performRefs += [pscustomobject]@{ source = $sourceTask; target = $target; action = $action.GetAttribute('sr') }
  if (-not $taskNames.Contains($target)) {
    $missingPerformRefs += "$sourceTask/$($action.GetAttribute('sr')) -> $target"
  }
}

$clickTaskRefs = @([regex]::Matches($text, '<clickTask>(-?\d+)</clickTask>') | ForEach-Object { $_.Groups[1].Value })
$missingClickTaskRefs = @($clickTaskRefs | Where-Object { $_ -notmatch '^-' -and -not $taskIds.Contains($_) } | Sort-Object -Unique)

$projectTaskMissing = @()
$projectTaskOrphans = @()
$projectSceneMissing = @()
$projectSceneOrphans = @()
foreach ($project in $projects) {
  $projectTaskIds = [System.Collections.Generic.HashSet[string]]::new()
  $projectScenes = [System.Collections.Generic.HashSet[string]]::new()
  if ($project.tids) {
    foreach ($id in ([string]$project.tids).Split(',')) {
      if ($id.Trim()) { [void]$projectTaskIds.Add($id.Trim()) }
    }
  }
  if ($project.scenes) {
    foreach ($sceneName in ([string]$project.scenes).Split(',')) {
      if ($sceneName.Trim()) { [void]$projectScenes.Add($sceneName.Trim()) }
    }
  }
  foreach ($task in $tasks) {
    if (-not $projectTaskIds.Contains([string]$task.id)) {
      $projectTaskMissing += "$($task.id):$($task.nme)"
    }
  }
  foreach ($id in $projectTaskIds) {
    if (-not $taskIds.Contains($id)) { $projectTaskOrphans += $id }
  }
  foreach ($scene in $scenes) {
    if (-not $projectScenes.Contains([string]$scene.nme)) {
      $projectSceneMissing += [string]$scene.nme
    }
  }
  foreach ($sceneName in $projectScenes) {
    if (-not @($scenes | Where-Object { $_.nme -eq $sceneName }).Count) {
      $projectSceneOrphans += $sceneName
    }
  }
}

$blockIssues = @()
foreach ($task in $tasks) {
  $stack = New-Object System.Collections.ArrayList
  foreach ($action in ActionsSorted $task) {
    $code = [string]$action.code
    $act = $action.GetAttribute('sr')
    if ($code -eq '37') {
      [void]$stack.Add([pscustomobject]@{ type = 'IF'; action = $act })
    } elseif ($code -eq '39') {
      [void]$stack.Add([pscustomobject]@{ type = 'FOR'; action = $act })
    } elseif ($code -eq '43') {
      if ($stack.Count -eq 0 -or $stack[$stack.Count - 1].type -ne 'IF') { $blockIssues += "$($task.nme) $act ELSE without IF" }
    } elseif ($code -eq '38') {
      if ($stack.Count -eq 0 -or $stack[$stack.Count - 1].type -ne 'IF') { $blockIssues += "$($task.nme) $act END IF mismatch" }
      else { $stack.RemoveAt($stack.Count - 1) }
    } elseif ($code -eq '40') {
      if ($stack.Count -eq 0 -or $stack[$stack.Count - 1].type -ne 'FOR') { $blockIssues += "$($task.nme) $act END FOR mismatch" }
      else { $stack.RemoveAt($stack.Count - 1) }
    }
  }
  foreach ($open in $stack) { $blockIssues += "$($task.nme) unclosed $($open.type) from $($open.action)" }
}

[xml]$sourceXmlForBlocks = [IO.File]::ReadAllText($source, [Text.Encoding]::UTF8)
$sourceBlockIssues = @()
foreach ($task in @($sourceXmlForBlocks.SelectNodes('//Task'))) {
  $stack = New-Object System.Collections.ArrayList
  foreach ($action in @($task.SelectNodes('Action')) | Sort-Object { ActNum $_ }) {
    $code = [string]$action.code
    $act = $action.GetAttribute('sr')
    if ($code -eq '37') {
      [void]$stack.Add([pscustomobject]@{ type = 'IF'; action = $act })
    } elseif ($code -eq '39') {
      [void]$stack.Add([pscustomobject]@{ type = 'FOR'; action = $act })
    } elseif ($code -eq '43') {
      if ($stack.Count -eq 0 -or $stack[$stack.Count - 1].type -ne 'IF') { $sourceBlockIssues += "$($task.nme) $act ELSE without IF" }
    } elseif ($code -eq '38') {
      if ($stack.Count -eq 0 -or $stack[$stack.Count - 1].type -ne 'IF') { $sourceBlockIssues += "$($task.nme) $act END IF mismatch" }
      else { $stack.RemoveAt($stack.Count - 1) }
    } elseif ($code -eq '40') {
      if ($stack.Count -eq 0 -or $stack[$stack.Count - 1].type -ne 'FOR') { $sourceBlockIssues += "$($task.nme) $act END FOR mismatch" }
      else { $stack.RemoveAt($stack.Count - 1) }
    }
  }
  foreach ($open in $stack) { $sourceBlockIssues += "$($task.nme) unclosed $($open.type) from $($open.action)" }
}
$newBlockIssues = @($blockIssues | Where-Object { $_ -notin $sourceBlockIssues })

$queue = TaskByName $xml 'FINAL Queue Cycle'
$r4a = TaskByName $xml 'QC R4A APP Tick No-Work Proof'
if (-not $queue -or -not $r4a) { throw 'Required Stage4A task or queue task is missing.' }

$queueActions = ActionsSorted $queue
$sendActions = @($queueActions | Where-Object { $_.code -eq '130' -and (StrArg $_ 'arg0') -eq 'FINAL Send Sheet' })
$firstSendAct = if ($sendActions.Count) { ActNum $sendActions[0] } else { -1 }
$guardIf = @($queueActions | Where-Object { $_.code -eq '37' -and $_.OuterXml -match '%AIWStage4ANoWorkProof' } | Select-Object -First 1)
$guardAct = if ($guardIf.Count) { ActNum $guardIf[0] } else { -1 }
$guardHasStop = $false
$guardHasLog = $false
$guardHasClear = $false
if ($guardAct -ge 0) {
  foreach ($action in $queueActions) {
    $n = ActNum $action
    if ($n -le $guardAct) { continue }
    if ($action.code -eq '38') { break }
    if ($action.code -eq '137') { $guardHasStop = $true }
    if ($action.code -eq '130' -and (StrArg $action 'arg0') -eq 'AIW PROOF Log Event') { $guardHasLog = $true }
    if ($action.code -eq '547' -and (StrArg $action 'arg0') -eq '%AIWStage4ANoWorkProof' -and (StrArg $action 'arg1') -eq '0') { $guardHasClear = $true }
  }
}

$forbiddenTargets = @('FINAL Send Sheet','SS Controlled One-Row Send Proof','SS Safe Send Dry-Run','AIW SEND 1','FINAL Send Sheet LEGACY','TextNow','AIW AUTO LIVE START V1','AIW AUTO LIVE TICK V1','APP Start AI Worker','TT5')
$r4aPerformTargets = @($r4a.SelectNodes("Action[code='130']") | ForEach-Object { StrArg $_ 'arg0' })
$r4aDirectForbidden = @($r4aPerformTargets | Where-Object {
  $target = $_
  @($forbiddenTargets | Where-Object { $target -like "$_*" -or $target -eq $_ }).Count -gt 0
})
$stageFlagValues = @($r4a.SelectNodes("Action[code='547']") | Where-Object { (StrArg $_ 'arg0') -eq '%AIWStage4ANoWorkProof' } | Sort-Object { ActNum $_ } | ForEach-Object { "$($_.GetAttribute('sr'))=$(StrArg $_ 'arg1')" })

$capExpected = @{
  '%AIWMaxActiveContacts' = '50'
  '%AIWProcessBatchCapNormal' = '2'
  '%AIWProcessBatchCapBacklog' = '5'
  '%AIWSendBatchCap' = '1'
  '%AIWTickMode' = 'NORMAL'
}
$capFindings = @()
foreach ($name in $capExpected.Keys) {
  $matches = @($xml.SelectNodes("//Action[code='547']") | Where-Object { (StrArg $_ 'arg0') -eq $name -and (StrArg $_ 'arg1') -eq $capExpected[$name] })
  $capFindings += "$name=$($capExpected[$name]) present=$([bool]$matches.Count)"
}

$jsonTrueCount = CountText $text 'json:true'
$seTrueCount = CountText $text '<se>true</se>'
$mojibakeCount = 0
foreach ($marker in @([char]0x00C3, [char]0x00C2, [char]0xFFFD)) {
  $mojibakeCount += CountText $text ([regex]::Escape([string]$marker))
}
$liveOpenCount = CountText $text 'LIVE_OPEN|LIVE OPEN|START LIVE OPEN'
$keyPresent = [bool]($text -match 'sk-|OPENAI_API_KEY|api[_-]?key|Authorization')

$sourceHash = Get-FileHash -LiteralPath $source -Algorithm SHA256
$patchedHash = Get-FileHash -LiteralPath $patched -Algorithm SHA256

$staticTxt = Join-Path $OutDir 'AIW_STAGE4A_NO_WORK_GUARD_STATIC_AUDIT_20260705.txt'
powershell -ExecutionPolicy Bypass -File (Join-Path (Split-Path -Parent $PSCommandPath) 'static-audit-tasker-xml.ps1') -XmlPath $patched | Set-Content -LiteralPath $staticTxt -Encoding UTF8

$structuralPass = (
  $duplicateTaskIds.Count -eq 0 -and
  $duplicateTaskNames.Count -eq 0 -and
  $missingProfileRefs.Count -eq 0 -and
  $missingPerformRefs.Count -eq 0 -and
  $missingClickTaskRefs.Count -eq 0 -and
  $projectTaskMissing.Count -eq 0 -and
  $projectTaskOrphans.Count -eq 0 -and
  $projectSceneMissing.Count -eq 0 -and
  $projectSceneOrphans.Count -eq 0 -and
  $newBlockIssues.Count -eq 0 -and
  $guardAct -ge 0 -and
  $firstSendAct -gt $guardAct -and
  $guardHasStop -and
  $guardHasLog -and
  $guardHasClear -and
  $r4aDirectForbidden.Count -eq 0
)
$classification = if ($structuralPass) { 'CANDIDATE / HOLD FOR PHONE RERUN' } else { 'HARD HOLD / STATIC PATCH ISSUE' }

$auditMd = Join-Path $OutDir 'AIW_STAGE4A_NO_WORK_GUARD_STATIC_AUDIT_20260705.md'
$audit = @(
  '# AIW Build100 Stage4A No-Work Guard Static Audit',
  '',
  "Patched XML: $patched",
  "Patched SHA256: $($patchedHash.Hash)",
  '',
  '## Result',
  '',
  "Classification: $classification",
  '',
  '## Required Checks',
  '',
  '- XML parse: PASS',
  "- Root: $($xml.DocumentElement.Name)",
  "- Task count: $($tasks.Count)",
  "- Profile count: $($profiles.Count)",
  "- Scene count: $($scenes.Count)",
  "- Duplicate task IDs: $($duplicateTaskIds.Count)",
  "- Duplicate task names: $($duplicateTaskNames.Count)",
  "- Missing project task refs: $($projectTaskOrphans.Count)",
  "- Defined tasks missing from project registry: $($projectTaskMissing.Count)",
  "- Missing project scene refs: $($projectSceneOrphans.Count)",
  "- Defined scenes missing from project registry: $($projectSceneMissing.Count)",
  "- Missing profile refs: $($missingProfileRefs.Count)",
  "- Missing scene clickTask refs: $($missingClickTaskRefs.Count)",
  "- Missing Perform Task refs: $($missingPerformRefs.Count)",
  "- Tasker block nesting issues: $($blockIssues.Count)",
  "- Source preexisting block nesting issues: $($sourceBlockIssues.Count)",
  "- New block nesting issues added by patch: $($newBlockIssues.Count)",
  "- json:true count: $jsonTrueCount",
  "- se_true_count: $seTrueCount",
  "- mojibake count: $mojibakeCount",
  "- live-open text/variable scan count: $liveOpenCount",
  "- KEY_PRESENT=$keyPresent",
  '- KEY_REDACTED_IN_REPORT=true',
  '',
  '## Stage4A Guard Scan',
  '',
  "- First FINAL Queue Cycle -> FINAL Send Sheet action: act$firstSendAct",
  "- Stage4A guard action: act$guardAct",
  "- Guard before first send: $($guardAct -ge 0 -and $firstSendAct -gt $guardAct)",
  "- Guard logs proof: $guardHasLog",
  "- Guard clears Stage4A flag: $guardHasClear",
  "- Guard stops before send task: $guardHasStop",
  "- QC R4A direct forbidden Perform Task refs: $($r4aDirectForbidden.Count)",
  "- QC R4A Stage4A flag actions: $($stageFlagValues -join '; ')",
  "- FINAL Queue Cycle send actions after patch: $(@($sendActions | ForEach-Object { $_.GetAttribute('sr') }) -join ', ')",
  '',
  '## Build100 Cap Variables'
)
foreach ($finding in $capFindings | Sort-Object) { $audit += "- $finding" }
$audit += ''
$audit += '## Block Issues'
$audit += ''
if ($newBlockIssues.Count) {
  $audit += 'New block issues added by this patch:'
  foreach ($issue in $newBlockIssues | Select-Object -First 100) { $audit += "- $issue" }
} elseif ($blockIssues.Count) {
  $audit += '- Stage4A patch added no new block issues.'
  $audit += '- Preexisting unrelated block issues remain on HOLD:'
  foreach ($issue in $blockIssues | Select-Object -First 100) { $audit += "- $issue" }
} else {
  $audit += '- PASS: If/End If and For/End For nesting balanced by numeric Tasker action order.'
}
Write-TextFile $auditMd $audit

$changeMd = Join-Path $OutDir 'AIW_STAGE4A_NO_WORK_GUARD_CHANGE_REPORT_20260705.md'
Write-TextFile $changeMd @(
  '# AIW Build100 Stage4A No-Work Guard Change Report',
  '',
  "Source XML SHA256: $($sourceHash.Hash)",
  "Patched XML SHA256: $($patchedHash.Hash)",
  '',
  '## Scope',
  '',
  '- Small patch only.',
  '- Source private/local runtime data preserved in the patched XML.',
  '- No TextNow, AutoInput, trigger, timer/live start, archive, deadarchive, compactor, or TT5 logic was intentionally changed.',
  '- No API keys or secrets are printed in this report.',
  '',
  '## XML Changes',
  '',
  '- Added `%AIWStage4ANoWorkProof=1` inside `QC R4A APP Tick No-Work Proof` immediately before `APP Run Tick Once`.',
  '- Added cleanup `%AIWStage4ANoWorkProof=0` after the tick proof path and again at final cleanup.',
  '- Added a guarded block inside `FINAL Queue Cycle` before its first `FINAL Send Sheet` call.',
  '- Guard behavior: when `%AIWStage4ANoWorkProof=1`, set proof result `PASS_NO_WORK`, set `%SSResult=NO_WORK_NO_SEND`, log proof, release busy lock, clear the Stage4A flag, and stop before any send task runs.',
  '',
  '## Not Changed',
  '',
  '- Preexisting unrelated Tasker block warnings were not repaired in this patch.',
  '- Missing Build100 cap variable assignments were not added in this patch.',
  '- Those items remain on HOLD because this order was limited to the Stage4A no-work send-path guard.'
)

$holdMd = Join-Path $OutDir 'AIW_STAGE4A_NO_WORK_GUARD_REMAINING_HOLD_LIST_20260705.md'
Write-TextFile $holdMd @(
  '# AIW Build100 Stage4A Remaining HOLD List',
  '',
  'STATUS: CANDIDATE / HOLD FOR PHONE RERUN',
  '',
  'Remaining HOLD items:',
  '',
  '1. Import/apply the patched XML on the Moto Razr 2024 only after audit review.',
  '2. Run exactly `QC R4A APP Tick No-Work Proof`.',
  '3. Export a fresh Tasker runlog.',
  '4. Prove `FINAL Send Sheet = 0`.',
  '5. Prove `AIW SEND 1 = 0`.',
  '6. Prove no timer/live/archive/deadarchive/compactor/TT5 path ran.',
  '7. Preexisting unrelated Tasker block warnings remain: see static audit.',
  '8. Build100 cap variables are not found in this private XML: `%AIWMaxActiveContacts`, `%AIWProcessBatchCapNormal`, `%AIWProcessBatchCapBacklog`, `%AIWSendBatchCap`, `%AIWTickMode`.',
  '9. Keep Build100 out of LOCKED status until phone proof passes.'
)

$checklistMd = Join-Path $OutDir 'AIW_STAGE4A_NO_WORK_GUARD_PHONE_RERUN_CHECKLIST_20260705.md'
Write-TextFile $checklistMd @(
  '# AIW Build100 Stage4A Phone Rerun Checklist',
  '',
  '1. Import/apply the patched full Tasker XML.',
  '2. In Tasker, run exactly `QC R4A APP Tick No-Work Proof`.',
  '3. Do not run live start, timer, trigger, send test, archive, deadarchive, compactor, or TT5.',
  '4. Export the Tasker runlog.',
  '5. Required pass evidence:',
  '   - `QC R4A APP Tick No-Work Proof = ExitOK`',
  '   - `APP Reset Locks = ExitOK`',
  '   - `QC Selection Hardening Audit = ExitOK`',
  '   - `FINAL Queue Cycle = ExitOK` or guarded no-send stop',
  '   - `FINAL Send Sheet = 0`',
  '   - `AIW SEND 1 = 0`',
  '   - `timer/live/archive/deadarchive/compactor/TT5 = 0`',
  '6. Upload the fresh runlog for audit.'
)

$shaCsv = Join-Path $OutDir 'AIW_STAGE4A_NO_WORK_GUARD_SHA256_INVENTORY_20260705.csv'
$artifactPaths = @($source, $patched, $staticTxt, $auditMd, $changeMd, $holdMd, $checklistMd)
$csv = @('file,path,bytes,sha256')
foreach ($path in $artifactPaths) {
  $item = Get-Item -LiteralPath $path
  $hash = Get-FileHash -LiteralPath $path -Algorithm SHA256
  $csv += ('"{0}","{1}",{2},{3}' -f ($item.Name -replace '"','""'), ($item.FullName -replace '"','""'), $item.Length, $hash.Hash)
}
Write-TextFile $shaCsv $csv

$packageDir = Split-Path -Parent $PackagePath
if (-not (Test-Path -LiteralPath $packageDir)) { New-Item -ItemType Directory -Path $packageDir | Out-Null }
if (Test-Path -LiteralPath $PackagePath) { Remove-Item -LiteralPath $PackagePath -Force }
$stageDir = Join-Path $OutDir '_stage4a_no_work_guard_package_stage'
if (Test-Path -LiteralPath $stageDir) {
  $resolvedStage = (Resolve-Path -LiteralPath $stageDir).Path
  $resolvedOut = (Resolve-Path -LiteralPath $OutDir).Path
  if (-not $resolvedStage.StartsWith($resolvedOut, [StringComparison]::OrdinalIgnoreCase)) { throw "Unexpected staging path: $resolvedStage" }
  Remove-Item -LiteralPath $stageDir -Recurse -Force
}
New-Item -ItemType Directory -Path $stageDir | Out-Null
foreach ($path in @($patched, $staticTxt, $auditMd, $changeMd, $holdMd, $checklistMd, $shaCsv)) {
  Copy-Item -LiteralPath $path -Destination $stageDir
}
Compress-Archive -Path (Join-Path $stageDir '*') -DestinationPath $PackagePath -Force
$packageHash = Get-FileHash -LiteralPath $PackagePath -Algorithm SHA256
$packageHashPath = Join-Path $OutDir 'AIW_STAGE4A_NO_WORK_GUARD_PACKAGE_SHA256_20260705.txt'
Write-TextFile $packageHashPath @(
  "package=$PackagePath",
  "sha256=$($packageHash.Hash)",
  "status=$classification",
  'KEY_PRESENT=true',
  'KEY_REDACTED_IN_REPORT=true'
)

[pscustomobject]@{
  PatchedXml = $patched
  PatchedSha256 = $patchedHash.Hash
  StaticAudit = $auditMd
  ChangeReport = $changeMd
  ShaInventory = $shaCsv
  HoldList = $holdMd
  PhoneChecklist = $checklistMd
  Package = $PackagePath
  PackageSha256 = $packageHash.Hash
  Classification = $classification
} | Format-List
