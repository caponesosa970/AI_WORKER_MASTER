param(
  [Parameter(Mandatory = $true)]
  [string]$SourceXml,

  [Parameter(Mandatory = $true)]
  [string]$OutputXml
)

$ErrorActionPreference = 'Stop'

function Get-TaskNode {
  param(
    [System.Xml.XmlDocument]$Doc,
    [string]$Name
  )
  $matches = @($Doc.SelectNodes('//Task') | Where-Object { $_.nme -eq $Name })
  if ($matches.Count -ne 1) {
    throw "Expected one task named '$Name', found $($matches.Count)."
  }
  return $matches[0]
}

function Get-ActionNode {
  param(
    [System.Xml.XmlElement]$Task,
    [int]$Number
  )
  $sr = "act$Number"
  $matches = @($Task.Action | Where-Object { $_.GetAttribute('sr') -eq $sr })
  if ($matches.Count -ne 1) {
    throw "Expected one action '$sr' in task '$($Task.nme)', found $($matches.Count)."
  }
  return $matches[0]
}

function Get-ActionNumber {
  param([System.Xml.XmlElement]$Action)
  return [int](($Action.GetAttribute('sr')) -replace '^act', '')
}

function Shift-Actions {
  param(
    [System.Xml.XmlElement]$Task,
    [int]$From,
    [int]$By
  )
  $actions = @($Task.Action) | Sort-Object { Get-ActionNumber $_ } -Descending
  foreach ($action in $actions) {
    $n = Get-ActionNumber $action
    if ($n -ge $From) {
      $action.SetAttribute('sr', "act$($n + $By)")
    }
  }
}

function Set-StrArg {
  param(
    [System.Xml.XmlElement]$Action,
    [string]$Arg,
    [string]$Value
  )
  $node = $Action.SelectSingleNode("Str[@sr='$Arg']")
  if (-not $node) {
    throw "Action $($Action.GetAttribute('sr')) does not have Str $Arg."
  }
  $node.InnerText = $Value
}

function Set-IfCondition {
  param(
    [System.Xml.XmlElement]$Action,
    [string]$Left,
    [string]$Operator,
    [string]$Right
  )
  $condition = $Action.SelectSingleNode('ConditionList/Condition[@sr="c0"]')
  if (-not $condition) {
    throw "Action $($Action.GetAttribute('sr')) does not have a c0 condition."
  }
  $condition.SelectSingleNode('lhs').InnerText = $Left
  $condition.SelectSingleNode('op').InnerText = $Operator
  $condition.SelectSingleNode('rhs').InnerText = $Right
}

function New-VarSet {
  param(
    [System.Xml.XmlElement]$Template,
    [string]$Name,
    [string]$Value
  )
  $node = [System.Xml.XmlElement]$Template.CloneNode($true)
  Set-StrArg $node 'arg0' $Name
  Set-StrArg $node 'arg1' $Value
  return $node
}

function New-IfEqualsOne {
  param(
    [System.Xml.XmlElement]$Template,
    [string]$Name
  )
  $node = [System.Xml.XmlElement]$Template.CloneNode($true)
  Set-IfCondition $node $Name '2' '1'
  return $node
}

function New-PerformTask {
  param(
    [System.Xml.XmlElement]$Template,
    [string]$TaskName
  )
  $node = [System.Xml.XmlElement]$Template.CloneNode($true)
  Set-StrArg $node 'arg0' $TaskName
  return $node
}

function Insert-ActionsBefore {
  param(
    [System.Xml.XmlDocument]$Doc,
    [System.Xml.XmlElement]$Task,
    [int]$BeforeNumber,
    [System.Xml.XmlElement[]]$NewActions
  )
  $target = Get-ActionNode $Task $BeforeNumber
  Shift-Actions $Task $BeforeNumber $NewActions.Count

  for ($i = 0; $i -lt $NewActions.Count; $i++) {
    $NewActions[$i].SetAttribute('sr', "act$($BeforeNumber + $i)")
    [void]$Task.InsertBefore($Doc.CreateWhitespace("`r`n`t`t"), $target)
    [void]$Task.InsertBefore($NewActions[$i], $target)
  }
}

if (-not (Test-Path -LiteralPath $SourceXml)) {
  throw "Source XML not found: $SourceXml"
}

$outDir = Split-Path -Parent $OutputXml
if (-not (Test-Path -LiteralPath $outDir)) {
  New-Item -ItemType Directory -Path $outDir | Out-Null
}

$doc = [System.Xml.XmlDocument]::new()
$doc.PreserveWhitespace = $true
$doc.Load($SourceXml)

$queue = Get-TaskNode $doc 'FINAL Queue Cycle'
$r4a = Get-TaskNode $doc 'QC R4A APP Tick No-Work Proof'

if ($doc.OuterXml -match '%AIWStage4ANoWorkProof') {
  throw 'Source XML already contains %AIWStage4ANoWorkProof; refusing to double-patch.'
}

$queueIfTemplate = Get-ActionNode $queue 7
$queueVarTemplate = Get-ActionNode $queue 32
$queueProofTemplate = Get-ActionNode $r4a 83
$queueStopTemplate = Get-ActionNode $queue 56
$queueEndIfTemplate = Get-ActionNode $queue 57

$guardActions = @(
  (New-IfEqualsOne $queueIfTemplate '%AIWStage4ANoWorkProof'),
  (New-VarSet $queueVarTemplate '%QCDebug' 'STAGE4A NO-WORK GUARD BLOCKED FINAL Send Sheet'),
  (New-VarSet $queueVarTemplate '%SSResult' 'NO_WORK_NO_SEND'),
  (New-VarSet $queueVarTemplate '%SSReadyCount' '0'),
  (New-VarSet $queueVarTemplate '%AIWorkerLastError' 'Stage4A no-work guard blocked FINAL Send Sheet'),
  (New-VarSet $queueVarTemplate '%AIWProofEvent' 'STAGE4A_NO_WORK_NO_SEND'),
  (New-VarSet $queueVarTemplate '%AIWProofStage' 'R4A_NO_WORK_GUARD'),
  (New-VarSet $queueVarTemplate '%AIWProofResult' 'PASS_NO_WORK'),
  (New-VarSet $queueVarTemplate '%AIWProofError' 'NONE'),
  (New-VarSet $queueVarTemplate '%AIWProofDetails' 'Stage4A no-work guard blocked FINAL Send Sheet before any send task'),
  (New-PerformTask $queueProofTemplate 'AIW PROOF Log Event'),
  (New-VarSet $queueVarTemplate '%AIWorkerBusy' '0'),
  (New-VarSet $queueVarTemplate '%AIWStage4ANoWorkProof' '0'),
  ([System.Xml.XmlElement]$queueStopTemplate.CloneNode($true)),
  ([System.Xml.XmlElement]$queueEndIfTemplate.CloneNode($true))
)

Insert-ActionsBefore $doc $queue 50 $guardActions

$r4aVarTemplate = Get-ActionNode $r4a 54
$stageOn = New-VarSet $r4aVarTemplate '%AIWStage4ANoWorkProof' '1'
Insert-ActionsBefore $doc $r4a 55 @($stageOn)

$stageOffAfterTick = New-VarSet $r4aVarTemplate '%AIWStage4ANoWorkProof' '0'
Insert-ActionsBefore $doc $r4a 85 @($stageOffAfterTick)

$stageOffFinal = New-VarSet $r4aVarTemplate '%AIWStage4ANoWorkProof' '0'
Insert-ActionsBefore $doc $r4a 97 @($stageOffFinal)

$doc.Save($OutputXml)

[xml]$verify = Get-Content -LiteralPath $OutputXml -Raw
$verifyQueue = Get-TaskNode $verify 'FINAL Queue Cycle'
$verifyR4A = Get-TaskNode $verify 'QC R4A APP Tick No-Work Proof'

$queueSendActs = @($verifyQueue.Action | Where-Object {
  $_.code -eq '130' -and $_.SelectSingleNode("Str[@sr='arg0']").InnerText -eq 'FINAL Send Sheet'
} | Sort-Object { Get-ActionNumber $_ } | ForEach-Object { $_.GetAttribute('sr') })

$stageFlagActions = @($verifyR4A.Action | Where-Object {
  $_.SelectSingleNode("Str[@sr='arg0']") -and $_.SelectSingleNode("Str[@sr='arg0']").InnerText -eq '%AIWStage4ANoWorkProof'
} | Sort-Object { Get-ActionNumber $_ } | ForEach-Object {
  "$($_.GetAttribute('sr'))=$($_.SelectSingleNode("Str[@sr='arg1']").InnerText)"
})

[pscustomobject]@{
  OutputXml = $OutputXml
  QueueSendActions = ($queueSendActs -join ',')
  Stage4AFlagActions = ($stageFlagActions -join ',')
  SHA256 = (Get-FileHash -LiteralPath $OutputXml -Algorithm SHA256).Hash
} | Format-List
