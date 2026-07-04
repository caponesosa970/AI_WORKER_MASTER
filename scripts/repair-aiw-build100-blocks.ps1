param(
  [Parameter(Mandatory = $true)]
  [string]$SourceXml,

  [Parameter(Mandatory = $true)]
  [string]$OutXml,

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

function Get-ActionNumber {
  param([string]$ActionBlock)

  if ($ActionBlock -match '<Action sr="act(\d+)" ve="7">') {
    return [int]$Matches[1]
  }
  throw "Could not read action sr"
}

function Get-ActionKind {
  param([string]$ActionBlock)

  if ($ActionBlock -match '<code>(\d+)</code>') {
    switch ($Matches[1]) {
      "37" { return "IF" }
      "38" { return "ENDIF" }
      "39" { return "FOR" }
      "40" { return "ENDFOR" }
      "43" { return "ELSE" }
      default { return "OTHER" }
    }
  }
  return "OTHER"
}

function Renumber-Actions {
  param([object[]]$Actions)

  $out = New-Object System.Collections.Generic.List[string]
  for ($i = 0; $i -lt $Actions.Count; $i++) {
    $block = [string]$Actions[$i].Block
    $block = [regex]::Replace($block, '<Action sr="act\d+" ve="7">', "<Action sr=`"act$i`" ve=`"7`">", 1)
    $out.Add($block)
  }
  return @($out.ToArray())
}

function Assert-BlocksBalanced {
  param(
    [string]$TaskName,
    [object[]]$Actions
  )

  $stack = New-Object System.Collections.ArrayList
  $issues = New-Object System.Collections.Generic.List[string]
  for ($i = 0; $i -lt $Actions.Count; $i++) {
    $kind = Get-ActionKind -ActionBlock ([string]$Actions[$i])
    $act = "act$i"
    if ($kind -eq "IF") {
      [void]$stack.Add([pscustomobject]@{ type = "IF"; action = $act })
    } elseif ($kind -eq "FOR") {
      [void]$stack.Add([pscustomobject]@{ type = "FOR"; action = $act })
    } elseif ($kind -eq "ELSE") {
      if ($stack.Count -eq 0 -or $stack[$stack.Count - 1].type -ne "IF") {
        $issues.Add(($TaskName + " " + $act + " ELSE without active IF"))
      }
    } elseif ($kind -eq "ENDIF") {
      if ($stack.Count -eq 0 -or $stack[$stack.Count - 1].type -ne "IF") {
        $issues.Add(($TaskName + " " + $act + " ENDIF mismatch"))
      } else {
        $stack.RemoveAt($stack.Count - 1)
      }
    } elseif ($kind -eq "ENDFOR") {
      if ($stack.Count -eq 0 -or $stack[$stack.Count - 1].type -ne "FOR") {
        $issues.Add(($TaskName + " " + $act + " ENDFOR mismatch"))
      } else {
        $stack.RemoveAt($stack.Count - 1)
      }
    }
  }

  foreach ($open in $stack) {
    $issues.Add(($TaskName + " unclosed " + $open.type + " from " + $open.action))
  }
  if ($issues.Count) {
    throw ("Balanced assertion failed: " + ($issues -join "; "))
  }
}

function Get-TaskActionParts {
  param(
    [string]$TaskName,
    [string]$Block
  )

  $matches = [regex]::Matches($Block, '(?s)\t\t<Action sr="act\d+" ve="7">.*?\t\t</Action>')
  if ($matches.Count -eq 0) { throw "No actions found in $TaskName" }

  $first = $matches[0]
  $last = $matches[$matches.Count - 1]
  $prefix = $Block.Substring(0, $first.Index)
  $suffix = $Block.Substring($last.Index + $last.Length)

  $actions = New-Object System.Collections.Generic.List[object]
  foreach ($match in $matches) {
    $actionBlock = $match.Value
    $actions.Add([pscustomobject]@{
      Number = Get-ActionNumber -ActionBlock $actionBlock
      Kind = Get-ActionKind -ActionBlock $actionBlock
      Block = $actionBlock
    })
  }

  return [pscustomobject]@{
    Prefix = $prefix
    Suffix = $suffix
    Actions = @($actions | Sort-Object Number)
  }
}

function Repair-SimpleTaskBlocks {
  param(
    [string]$Text,
    [string]$TaskName
  )

  $bounds = Get-TaskBounds -Text $Text -TaskName $TaskName
  $parts = Get-TaskActionParts -TaskName $TaskName -Block $bounds.Block

  $kept = New-Object System.Collections.Generic.List[object]
  $misplaced = New-Object System.Collections.ArrayList
  $stack = New-Object System.Collections.ArrayList

  foreach ($action in $parts.Actions) {
    if ($action.Kind -eq "IF") {
      [void]$stack.Add([pscustomobject]@{ type = "IF"; action = $action })
      $kept.Add($action)
    } elseif ($action.Kind -eq "FOR") {
      [void]$stack.Add([pscustomobject]@{ type = "FOR"; action = $action })
      $kept.Add($action)
    } elseif ($action.Kind -eq "ELSE") {
      if ($stack.Count -eq 0 -or $stack[$stack.Count - 1].type -ne "IF") {
        throw "Cannot simple-repair bad ELSE in $TaskName at act$($action.Number)"
      }
      $kept.Add($action)
    } elseif ($action.Kind -eq "ENDIF") {
      if ($stack.Count -gt 0 -and $stack[$stack.Count - 1].type -eq "IF") {
        $stack.RemoveAt($stack.Count - 1)
        $kept.Add($action)
      } else {
        [void]$misplaced.Add([pscustomobject]@{ type = "IF"; action = $action })
      }
    } elseif ($action.Kind -eq "ENDFOR") {
      if ($stack.Count -gt 0 -and $stack[$stack.Count - 1].type -eq "FOR") {
        $stack.RemoveAt($stack.Count - 1)
        $kept.Add($action)
      } else {
        [void]$misplaced.Add([pscustomobject]@{ type = "FOR"; action = $action })
      }
    } else {
      $kept.Add($action)
    }
  }

  $append = New-Object System.Collections.Generic.List[object]
  for ($i = $stack.Count - 1; $i -ge 0; $i--) {
    $need = $stack[$i].type
    $found = -1
    for ($j = 0; $j -lt $misplaced.Count; $j++) {
      if ($misplaced[$j].type -eq $need) {
        $found = $j
        break
      }
    }
    if ($found -lt 0) {
      throw "No misplaced $need closer available for $TaskName"
    }
    $append.Add($misplaced[$found].action)
    $misplaced.RemoveAt($found)
  }

  if ($misplaced.Count -gt 0) {
    throw "Unused misplaced closer remains in $TaskName"
  }

  foreach ($action in $append) {
    $kept.Add($action)
  }

  $renumbered = Renumber-Actions -Actions @($kept.ToArray())
  Assert-BlocksBalanced -TaskName $TaskName -Actions @($renumbered)
  $newBlock = $parts.Prefix + ($renumbered -join $nl) + $parts.Suffix
  $changes.Add(($TaskName + ": balanced misplaced close actions and renumbered action sr values"))
  return Replace-TaskBlock -Text $Text -Bounds $bounds -NewBlock $newBlock
}

function Repair-TT5OverflowDrainCap {
  param([string]$Text)

  $taskName = "TT5 Overflow Drain Cap"
  $bounds = Get-TaskBounds -Text $Text -TaskName $taskName
  $parts = Get-TaskActionParts -TaskName $taskName -Block $bounds.Block
  $byNumber = @{}
  foreach ($action in $parts.Actions) {
    $byNumber[$action.Number] = $action
  }

  $order = @(0, 1, 10, 11, 12, 13, 14, 15, 16, 17, 2, 3, 4, 5, 6, 7, 8, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27)
  $newActions = New-Object System.Collections.Generic.List[object]
  foreach ($number in $order) {
    if (-not $byNumber.ContainsKey($number)) { throw "$taskName missing act$number" }
    $newActions.Add($byNumber[$number])
  }

  $renumbered = Renumber-Actions -Actions @($newActions.ToArray())
  Assert-BlocksBalanced -TaskName $taskName -Actions @($renumbered)
  $newBlock = $parts.Prefix + ($renumbered -join $nl) + $parts.Suffix
  $changes.Add(($taskName + ": rebuilt For/If/Else order from existing actions and renumbered action sr values"))
  return Replace-TaskBlock -Text $Text -Bounds $bounds -NewBlock $newBlock
}

foreach ($taskName in @(
  "FINAL Worker Watchdog Full",
  "APP Health Check",
  "WD DeadArchive Move Cap 3",
  "TT5 Log Current Message To OverflowInbox",
  "TT5 Overflow Drain One",
  "FINAL Archive Done Rows"
)) {
  $text = Repair-SimpleTaskBlocks -Text $text -TaskName $taskName
}

$text = Repair-TT5OverflowDrainCap -Text $text

$outDir = Split-Path -Parent $OutXml
if (-not (Test-Path -LiteralPath $outDir)) {
  New-Item -ItemType Directory -Path $outDir | Out-Null
}
[IO.File]::WriteAllText($OutXml, $text, [Text.UTF8Encoding]::new($false))

$reportLines = @()
$reportLines += "# AIW Build100 Block Structure Repair Report"
$reportLines += ""
$reportLines += "Source XML: $sourcePath"
$reportLines += "Output XML: $OutXml"
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

Write-Output "out_xml: $OutXml"
Write-Output "block_repair_report: $ReportPath"
Write-Output ("changes: " + $changes.Count)
