param(
    [Parameter(Mandatory=$true)][string]$SourceXml,
    [Parameter(Mandatory=$true)][string]$OutDir
)

$ErrorActionPreference = 'Stop'

function New-SetVarAction {
    param(
        [xml]$Doc,
        [string]$Sr,
        [string]$Name,
        [string]$Value,
        [string]$Arg3 = '0'
    )
    $a = $Doc.CreateElement('Action')
    $a.SetAttribute('sr', $Sr)
    $a.SetAttribute('ve', '7')

    $code = $Doc.CreateElement('code')
    $code.InnerText = '547'
    [void]$a.AppendChild($code)

    $s0 = $Doc.CreateElement('Str')
    $s0.SetAttribute('sr', 'arg0')
    $s0.SetAttribute('ve', '3')
    $s0.InnerText = $Name
    [void]$a.AppendChild($s0)

    $s1 = $Doc.CreateElement('Str')
    $s1.SetAttribute('sr', 'arg1')
    $s1.SetAttribute('ve', '3')
    $s1.InnerText = $Value
    [void]$a.AppendChild($s1)

    foreach ($pair in @(
        @('arg2','0'),
        @('arg3',$Arg3),
        @('arg4','0'),
        @('arg5','3'),
        @('arg6','0')
    )) {
        $i = $Doc.CreateElement('Int')
        $i.SetAttribute('sr', $pair[0])
        $i.SetAttribute('val', $pair[1])
        [void]$a.AppendChild($i)
    }
    return $a
}

function New-IfEqualsAction {
    param([xml]$Doc, [string]$Sr, [string]$Lhs, [string]$Rhs)
    $a = $Doc.CreateElement('Action')
    $a.SetAttribute('sr', $Sr)
    $a.SetAttribute('ve', '7')
    $code = $Doc.CreateElement('code')
    $code.InnerText = '37'
    [void]$a.AppendChild($code)
    $cl = $Doc.CreateElement('ConditionList')
    $cl.SetAttribute('sr', 'if')
    $c = $Doc.CreateElement('Condition')
    $c.SetAttribute('sr', 'c0')
    $c.SetAttribute('ve', '3')
    foreach ($n in @('lhs','op','rhs')) {
        $e = $Doc.CreateElement($n)
        if ($n -eq 'lhs') { $e.InnerText = $Lhs }
        elseif ($n -eq 'op') { $e.InnerText = '2' }
        else { $e.InnerText = $Rhs }
        [void]$c.AppendChild($e)
    }
    [void]$cl.AppendChild($c)
    [void]$a.AppendChild($cl)
    return $a
}

function New-EndIfAction {
    param([xml]$Doc, [string]$Sr)
    $a = $Doc.CreateElement('Action')
    $a.SetAttribute('sr', $Sr)
    $a.SetAttribute('ve', '7')
    $code = $Doc.CreateElement('code')
    $code.InnerText = '38'
    [void]$a.AppendChild($code)
    return $a
}

function New-StopAction {
    param([xml]$Doc, [string]$Sr)
    $a = $Doc.CreateElement('Action')
    $a.SetAttribute('sr', $Sr)
    $a.SetAttribute('ve', '7')
    $code = $Doc.CreateElement('code')
    $code.InnerText = '137'
    [void]$a.AppendChild($code)
    $i = $Doc.CreateElement('Int')
    $i.SetAttribute('sr', 'arg0')
    $i.SetAttribute('val', '0')
    [void]$a.AppendChild($i)
    $s = $Doc.CreateElement('Str')
    $s.SetAttribute('sr', 'arg1')
    $s.SetAttribute('ve', '3')
    [void]$a.AppendChild($s)
    return $a
}

function Get-TaskByName {
    param([xml]$Doc, [string]$Name)
    $tasks = @($Doc.SelectNodes("//Task[nme='$Name']"))
    if ($tasks.Count -ne 1) {
        throw "Expected exactly one task named '$Name', found $($tasks.Count)."
    }
    return $tasks[0]
}

function Set-VarInTask {
    param($Task, [string]$Name, [string]$Value)
    $changed = 0
    foreach ($a in @($Task.SelectNodes("Action[code='547']"))) {
        $arg0 = $a.SelectSingleNode("Str[@sr='arg0']")
        $arg1 = $a.SelectSingleNode("Str[@sr='arg1']")
        if ($arg0 -and $arg1 -and $arg0.InnerText -eq $Name) {
            $arg1.InnerText = $Value
            $changed++
        }
    }
    return $changed
}

function Set-Or-InsertBeforeProofLog {
    param($Doc, $Task, [string]$Name, [string]$Value)
    if ((Set-VarInTask -Task $Task -Name $Name -Value $Value) -gt 0) { return }
    $proof = @($Task.SelectNodes("Action[code='130' and Str[@sr='arg0']='AIW PROOF Log Event']")) | Select-Object -First 1
    if (-not $proof) { throw "No proof log action found in task $($Task.nme)." }
    $new = New-SetVarAction -Doc $Doc -Sr 'act999' -Name $Name -Value $Value
    [void]$Task.InsertBefore($new, $proof)
}

function Sort-ActionsBySrNumber {
    param($Task)
    $actions = @($Task.SelectNodes('Action')) | Sort-Object {
        if ($_.sr -match '^act(\d+)$') { [int]$Matches[1] } else { 1000000 }
    }
    foreach ($a in $actions) { [void]$Task.RemoveChild($a) }
    foreach ($a in $actions) { [void]$Task.AppendChild($a) }
}

function Renumber-ActionsInCurrentOrder {
    param($Task)
    $i = 0
    foreach ($a in @($Task.SelectNodes('Action'))) {
        $a.SetAttribute('sr', "act$i")
        $i++
    }
}

function Insert-BeforeActionNumber {
    param($Doc, $Task, [int]$BeforeNumber, [System.Xml.XmlElement[]]$NewActions)
    Sort-ActionsBySrNumber -Task $Task
    $before = $Task.SelectSingleNode("Action[@sr='act$BeforeNumber']")
    if (-not $before) { throw "Could not find act$BeforeNumber in task $($Task.nme)." }
    foreach ($new in $NewActions) {
        [void]$Task.InsertBefore($new, $before)
    }
    Renumber-ActionsInCurrentOrder -Task $Task
}

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$outXml = Join-Path $OutDir 'AIW_BUILD100_CONTROLLED_TEST_HOLD_FULL_TASKER.xml'

$doc = New-Object System.Xml.XmlDocument
$doc.PreserveWhitespace = $true
$doc.Load($SourceXml)

$rootProjectName = $doc.SelectSingleNode("//Project/name[text()='AI WORKER BUILD100 LIVE OPEN FULL CONTROL']")
if ($rootProjectName) { $rootProjectName.InnerText = 'AI WORKER BUILD100 CONTROLLED TEST HOLD' }

$replacements = @{
    'START LIVE OPEN' = 'HOLD START BLOCKED'
    'BUILD100 LIVE OPEN • FULL CONTROL' = 'BUILD100 CONTROLLED TEST HOLD'
    'BUILD100 LIVE OPEN | FULL CONTROL | DASHBOARD P82' = 'BUILD100 CONTROLLED TEST HOLD | DASHBOARD P82'
}
foreach ($str in @($doc.SelectNodes('//Str'))) {
    if ($replacements.ContainsKey($str.InnerText)) {
        $str.InnerText = $replacements[$str.InnerText]
    }
}

$safeDefaults = [ordered]@{
    '%AIWorkerSafeMode' = '1'
    '%AIWorkerBatchCap' = '1'
    '%AIWArchiveEnabled' = '0'
    '%AIWDeadArchiveEnabled' = '0'
    '%AIWCompactorEnabled' = '0'
    '%AIWAllowTempTools' = '0'
    '%AIWAllowHeavyCleanup' = '0'
    '%AIWDoNotTouchTextNowUI' = '1'
    '%AIWDoNotTouchAutoInput' = '1'
    '%AIWDeviceTunedFrozen' = '1'
    '%AIWDeviceTunedPatchAllowed' = '0'
    '%AIWV19MPhoneLiveHold' = '1'
    '%AIWV19MSendLiveHold' = '1'
    '%AIWV19MSendFlowDryRunOnly' = '1'
}

foreach ($taskName in @('APP Config Setup','APP Reset Locks','TEST HOLD - APP Config Setup')) {
    $t = Get-TaskByName -Doc $doc -Name $taskName
    foreach ($k in $safeDefaults.Keys) {
        [void](Set-VarInTask -Task $t -Name $k -Value $safeDefaults[$k])
    }
}

$config = Get-TaskByName -Doc $doc -Name 'APP Config Setup'
Set-Or-InsertBeforeProofLog -Doc $doc -Task $config -Name '%AIWorkerLastError' -Value 'CONFIG OK'
Set-Or-InsertBeforeProofLog -Doc $doc -Task $config -Name '%AIWProofError' -Value 'NONE'
Set-Or-InsertBeforeProofLog -Doc $doc -Task $config -Name '%AIWProofResult' -Value 'PASS'
Set-Or-InsertBeforeProofLog -Doc $doc -Task $config -Name '%AIWProofDetails' -Value 'APP Config Setup completed clean controlled safe config'
Set-VarInTask -Task $config -Name '%AIWPatchMode' -Value 'CONTROLLED_TEST_HOLD' | Out-Null
Set-VarInTask -Task $config -Name '%AIWNextPatchGate' -Value 'PHONE_PROOF_CONTROLLED_TEST_HOLD' | Out-Null
Set-VarInTask -Task $config -Name '%AIWDebugProofScope' -Value 'CONTROLLED_TEST_HOLD_ALL_MAJOR_SECTIONS' | Out-Null

$reset = Get-TaskByName -Doc $doc -Name 'APP Reset Locks'
Set-Or-InsertBeforeProofLog -Doc $doc -Task $reset -Name '%AIWProofError' -Value 'NONE'

foreach ($taskName in @('APP Start AI Worker','TEST HOLD - APP Start AI Worker')) {
    $t = Get-TaskByName -Doc $doc -Name $taskName
    Set-VarInTask -Task $t -Name '%AIWProofResult' -Value 'PASS' | Out-Null
    Set-VarInTask -Task $t -Name '%AIWProofDetails' -Value 'APP Start AI Worker reached exit/end proof' | Out-Null
    Set-VarInTask -Task $t -Name '%AIWProofError' -Value 'NONE' | Out-Null
    Insert-BeforeActionNumber -Doc $doc -Task $t -BeforeNumber 5 -NewActions @(
        (New-SetVarAction -Doc $doc -Sr 'act999' -Name '%AIWProofResult' -Value 'HOLD_BLOCKED'),
        (New-SetVarAction -Doc $doc -Sr 'act999' -Name '%AIWProofError' -Value 'NONE'),
        (New-SetVarAction -Doc $doc -Sr 'act999' -Name '%AIWProofDetails' -Value 'Blocked correctly by live hold')
    )
}

foreach ($taskName in @('APP Run Tick Once','TEST HOLD - APP Run Tick Once')) {
    $t = Get-TaskByName -Doc $doc -Name $taskName
    Set-VarInTask -Task $t -Name '%AIWV19MPhoneLiveHold' -Value '1' | Out-Null
    Insert-BeforeActionNumber -Doc $doc -Task $t -BeforeNumber 8 -NewActions @(
        (New-SetVarAction -Doc $doc -Sr 'act999' -Name '%AIWProofResult' -Value 'HOLD_BLOCKED'),
        (New-SetVarAction -Doc $doc -Sr 'act999' -Name '%AIWProofError' -Value 'NONE'),
        (New-SetVarAction -Doc $doc -Sr 'act999' -Name '%AIWProofDetails' -Value 'Blocked correctly by live hold')
    )
}

$auto = Get-TaskByName -Doc $doc -Name 'AIW AUTO LIVE START V1'
Sort-ActionsBySrNumber -Task $auto
$beforeLive = $auto.SelectSingleNode("Action[@sr='act1']")
foreach ($new in @(
    (New-IfEqualsAction -Doc $doc -Sr 'act999' -Lhs '%AIWV19MPhoneLiveHold' -Rhs '1'),
    (New-SetVarAction -Doc $doc -Sr 'act999' -Name '%AIWProofResult' -Value 'HOLD_BLOCKED'),
    (New-SetVarAction -Doc $doc -Sr 'act999' -Name '%AIWProofError' -Value 'NONE'),
    (New-SetVarAction -Doc $doc -Sr 'act999' -Name '%AIWProofDetails' -Value 'Blocked correctly by live hold'),
    (New-StopAction -Doc $doc -Sr 'act999'),
    (New-EndIfAction -Doc $doc -Sr 'act999')
)) {
    [void]$auto.InsertBefore($new, $beforeLive)
}
Set-VarInTask -Task $auto -Name '%AIWV19MPhoneLiveHold' -Value '1' | Out-Null
Set-VarInTask -Task $auto -Name '%AIWV19MSendLiveHold' -Value '1' | Out-Null
Set-VarInTask -Task $auto -Name '%AIWV19MSendFlowDryRunOnly' -Value '1' | Out-Null
Set-VarInTask -Task $auto -Name '%AIWorkerSafeMode' -Value '1' | Out-Null
Set-VarInTask -Task $auto -Name '%AIWorkerBatchCap' -Value '1' | Out-Null
Set-VarInTask -Task $auto -Name '%AIWAutoLiveMode' -Value 'CONTROLLED_TEST_HOLD_BLOCKED' | Out-Null
Renumber-ActionsInCurrentOrder -Task $auto

foreach ($taskName in @('TEST HOLD - FINAL Send Sheet LEGACY')) {
    $t = Get-TaskByName -Doc $doc -Name $taskName
    Set-VarInTask -Task $t -Name '%AIWV19MSendLiveHold' -Value '1' | Out-Null
    Set-VarInTask -Task $t -Name '%AIWV19MSendFlowDryRunOnly' -Value '1' | Out-Null
    Set-VarInTask -Task $t -Name '%AIWSendBatchCap' -Value '1' | Out-Null
}

$settingsToConfirm = [ordered]@{
    '%AIWMaxActiveContacts' = '50'
    '%AIWProcessBatchCapNormal' = '2'
    '%AIWProcessBatchCapBacklog' = '5'
    '%AIWSendBatchCap' = '1'
    '%AIWTickMode' = 'NORMAL'
}
foreach ($taskName in @('APP Config Setup','APP Reset Locks','TEST HOLD - APP Config Setup')) {
    $t = Get-TaskByName -Doc $doc -Name $taskName
    foreach ($k in $settingsToConfirm.Keys) {
        [void](Set-VarInTask -Task $t -Name $k -Value $settingsToConfirm[$k])
    }
}

$doc.Save($outXml)
Write-Output $outXml
