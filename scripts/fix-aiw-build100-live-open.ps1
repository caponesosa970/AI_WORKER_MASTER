param(
  [Parameter(Mandatory = $true)]
  [string]$SourceXml,

  [Parameter(Mandatory = $true)]
  [string]$FixedXml,

  [Parameter(Mandatory = $true)]
  [string]$ReportPath
)

$ErrorActionPreference = "Stop"

$sourcePath = (Resolve-Path -LiteralPath $SourceXml).Path
$text = [IO.File]::ReadAllText($sourcePath)
$nl = if ($text.Contains("`r`n")) { "`r`n" } else { "`n" }
$changes = New-Object System.Collections.Generic.List[string]

function Get-TaskBounds {
  param(
    [string]$Text,
    [string]$TaskName
  )

  $needle = "<nme>$TaskName</nme>"
  $nameIndex = $Text.IndexOf($needle, [StringComparison]::Ordinal)
  if ($nameIndex -lt 0) { throw "Task not found: $TaskName" }

  $startIndex = $Text.LastIndexOf("<Task ", $nameIndex, [StringComparison]::Ordinal)
  if ($startIndex -lt 0) { throw "Task start not found: $TaskName" }

  $endMarker = "</Task>"
  $endIndex = $Text.IndexOf($endMarker, $nameIndex, [StringComparison]::Ordinal)
  if ($endIndex -lt 0) { throw "Task end not found: $TaskName" }
  $endIndex += $endMarker.Length

  return [pscustomobject]@{
    Start = $startIndex
    End = $endIndex
    Block = $Text.Substring($startIndex, $endIndex - $startIndex)
  }
}

function Replace-TaskBlock {
  param(
    [string]$Text,
    [object]$Bounds,
    [string]$NewBlock
  )

  return $Text.Substring(0, $Bounds.Start) + $NewBlock + $Text.Substring($Bounds.End)
}

function Set-TaskActionVariable {
  param(
    [string]$Text,
    [string]$TaskName,
    [string]$ActionSr,
    [string]$VarName,
    [string]$NewValue
  )

  $bounds = Get-TaskBounds -Text $Text -TaskName $TaskName
  $block = $bounds.Block
  $actionPattern = "(?s)<Action sr=`"$ActionSr`" ve=`"7`">.*?</Action>"
  $actionMatch = [regex]::Match($block, $actionPattern)
  if (-not $actionMatch.Success) { throw "Action $ActionSr not found in $TaskName" }
  $action = $actionMatch.Value
  if ($action -notlike "*<Str sr=`"arg0`" ve=`"3`">$VarName</Str>*") {
    throw "Action $ActionSr in $TaskName is not $VarName"
  }
  $newAction = [regex]::Replace(
    $action,
    '<Str sr="arg1" ve="3">.*?</Str>',
    "<Str sr=`"arg1`" ve=`"3`">$NewValue</Str>",
    1
  )
  $newBlock = $block.Substring(0, $actionMatch.Index) + $newAction + $block.Substring($actionMatch.Index + $actionMatch.Length)
  $changes.Add(($TaskName + "/" + $ActionSr + ": " + $VarName + " set to " + $NewValue))
  return Replace-TaskBlock -Text $Text -Bounds $bounds -NewBlock $newBlock
}

function New-SetVariableAction {
  param(
    [int]$Number,
    [string]$VarName,
    [string]$Value
  )

  return @(
    "`t`t<Action sr=`"act$Number`" ve=`"7`">",
    "`t`t`t<code>547</code>",
    "`t`t`t<Str sr=`"arg0`" ve=`"3`">$VarName</Str>",
    "`t`t`t<Str sr=`"arg1`" ve=`"3`">$Value</Str>",
    "`t`t`t<Int sr=`"arg2`" val=`"0`" />",
    "`t`t`t<Int sr=`"arg3`" val=`"1`" />",
    "`t`t`t<Int sr=`"arg4`" val=`"0`" />",
    "`t`t`t<Int sr=`"arg5`" val=`"3`" />",
    "`t`t`t<Int sr=`"arg6`" val=`"0`" />",
    "`t`t</Action>"
  ) -join $script:nl
}

function Add-CapVariables {
  param(
    [string]$Text,
    [string]$TaskName
  )

  $bounds = Get-TaskBounds -Text $Text -TaskName $TaskName
  $block = $bounds.Block
  if ($block.Contains("<Str sr=`"arg0`" ve=`"3`">%AIWMaxActiveContacts</Str>")) {
    $changes.Add(($TaskName + ": Build100 cap variables already present"))
    return $Text
  }

  $insert = @(
    (New-SetVariableAction -Number 77 -VarName "%AIWMaxActiveContacts" -Value "50"),
    (New-SetVariableAction -Number 78 -VarName "%AIWProcessBatchCapNormal" -Value "2"),
    (New-SetVariableAction -Number 79 -VarName "%AIWProcessBatchCapBacklog" -Value "5"),
    (New-SetVariableAction -Number 80 -VarName "%AIWSendBatchCap" -Value "1"),
    (New-SetVariableAction -Number 81 -VarName "%AIWTickMode" -Value "NORMAL")
  ) -join $nl

  $marker = "<Action sr=`"act8`" ve=`"7`">"
  $markerIndex = $block.IndexOf($marker, [StringComparison]::Ordinal)
  if ($markerIndex -lt 0) {
    throw "Insertion marker act8 not found in $TaskName"
  }

  $newBlock = $block.Substring(0, $markerIndex) + $insert + $nl + $block.Substring($markerIndex)
  $changes.Add(($TaskName + ": added Build100 cap variables act77-act81"))
  return Replace-TaskBlock -Text $Text -Bounds $bounds -NewBlock $newBlock
}

function Fix-LegacySendLoop {
  param(
    [string]$Text,
    [string]$TaskName
  )

  $bounds = Get-TaskBounds -Text $Text -TaskName $TaskName
  $block = $bounds.Block
  $actionMatches = [regex]::Matches($block, '(?s)\t\t<Action sr="act\d+" ve="7">.*?\t\t</Action>')
  if ($actionMatches.Count -eq 0) { throw "No actions found in $TaskName" }

  $first = $actionMatches[0]
  $last = $actionMatches[$actionMatches.Count - 1]
  $prefix = $block.Substring(0, $first.Index)
  $suffix = $block.Substring($last.Index + $last.Length)

  $endFor = $null
  $newActions = New-Object System.Collections.Generic.List[string]
  $maxAction = -1

  foreach ($match in $actionMatches) {
    $action = $match.Value
    if ($action -notmatch '<Action sr="act(\d+)" ve="7">') {
      throw "Could not read action sr in $TaskName"
    }
    $number = [int]$Matches[1]
    if ($number -gt $maxAction) { $maxAction = $number }

    if ($number -eq 105 -and $action -match '<code>40</code>') {
      $endFor = $action
      continue
    }

    if ($number -ge 106) {
      $newNumber = $number - 1
      $action = [regex]::Replace($action, '<Action sr="act\d+" ve="7">', "<Action sr=`"act$newNumber`" ve=`"7`">", 1)
    }
    $newActions.Add($action)
  }

  if (-not $endFor) { throw "Misplaced End For act105 not found in $TaskName" }
  if ($block -notmatch '<Action sr="act113" ve="7">\s*<code>39</code>') {
    throw "Expected For action act113 not found in $TaskName"
  }

  $endNumber = $maxAction
  $endFor = [regex]::Replace($endFor, '<Action sr="act\d+" ve="7">', "<Action sr=`"act$endNumber`" ve=`"7`">", 1)
  $newActions.Add($endFor)

  $numbers = @()
  foreach ($action in $newActions) {
    if ($action -match '<Action sr="act(\d+)" ve="7">') { $numbers += [int]$Matches[1] }
  }
  $dupes = @($numbers | Group-Object | Where-Object { $_.Count -gt 1 })
  if ($dupes.Count) { throw "Duplicate action sr after loop fix in $TaskName" }
  $missing = @()
  for ($i = 0; $i -le $maxAction; $i++) {
    if ($numbers -notcontains $i) { $missing += $i }
  }
  if ($missing.Count) { throw "Missing action sr after loop fix in ${TaskName}: $($missing -join ',')" }

  $newBlock = $prefix + ($newActions -join $nl) + $suffix
  $changes.Add(($TaskName + ": moved misplaced End For from act105 to act" + $endNumber + " and shifted act106-act" + $maxAction + " down"))
  return Replace-TaskBlock -Text $Text -Bounds $bounds -NewBlock $newBlock
}

$text = Set-TaskActionVariable -Text $text -TaskName "APP Config Setup" -ActionSr "act54" -VarName "%AIWProofError" -NewValue "NONE"
$text = Set-TaskActionVariable -Text $text -TaskName "TEST HOLD - APP Config Setup" -ActionSr "act54" -VarName "%AIWProofError" -NewValue "NONE"
$text = Add-CapVariables -Text $text -TaskName "APP Config Setup"
$text = Add-CapVariables -Text $text -TaskName "TEST HOLD - APP Config Setup"
$text = Fix-LegacySendLoop -Text $text -TaskName "FINAL Send Sheet LEGACY UI FROZEN V19M"
$text = Fix-LegacySendLoop -Text $text -TaskName "TEST HOLD - FINAL Send Sheet LEGACY"

$fixedDir = Split-Path -Parent $FixedXml
if (-not (Test-Path -LiteralPath $fixedDir)) {
  New-Item -ItemType Directory -Path $fixedDir | Out-Null
}

[IO.File]::WriteAllText($FixedXml, $text, [Text.UTF8Encoding]::new($false))

$reportLines = @()
$reportLines += "# AIW Build100 Live Open Fix Report"
$reportLines += ""
$reportLines += "Source XML: $sourcePath"
$reportLines += "Fixed XML: $FixedXml"
$reportLines += ""
$reportLines += "## Changes"
foreach ($change in $changes) {
  $reportLines += "- $change"
}

$reportDir = Split-Path -Parent $ReportPath
if (-not (Test-Path -LiteralPath $reportDir)) {
  New-Item -ItemType Directory -Path $reportDir | Out-Null
}
[IO.File]::WriteAllText($ReportPath, ($reportLines -join $nl), [Text.UTF8Encoding]::new($false))

Write-Output "fixed_xml: $FixedXml"
Write-Output "fix_report: $ReportPath"
Write-Output ("changes: " + $changes.Count)
