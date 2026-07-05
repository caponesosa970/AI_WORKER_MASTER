param(
    [Parameter(Mandatory=$true)]
    [string]$RunlogPath,

    [string]$OutDir = "C:\Users\Shadow\Documents\ai work\AI_WORKER_MASTER\03_PHONE_PROOF"
)

$ErrorActionPreference = "Stop"

if (!(Test-Path -LiteralPath $RunlogPath)) {
    throw "Runlog not found: $RunlogPath"
}

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

$rawName = [IO.Path]::GetFileNameWithoutExtension($RunlogPath)
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$report = Join-Path $OutDir "AIW_STAGE3A_CLOSEOUT_RUNLOG_AUDIT_$timestamp.md"
$shaCsv = Join-Path $OutDir "SHA256_STAGE3A_CLOSEOUT_RUNLOG_AUDIT_$timestamp.csv"

$text = Get-Content -LiteralPath $RunlogPath -Raw
$lines = Get-Content -LiteralPath $RunlogPath

function Count-Simple([string]$needle) {
    return ($lines | Select-String -SimpleMatch $needle).Count
}

function Count-Regex([string]$pattern) {
    return ($lines | Select-String -Pattern $pattern).Count
}

function Task-Stats([string]$name) {
    [pscustomobject]@{
        Name = $name
        Total = Count-Simple $name
        Running = Count-Regex (" T Running\s+ID[^ ]+\s+" + [regex]::Escape($name) + "$")
        ExitOK = Count-Regex (" T ExitOK\s+ID[^ ]+\s+" + [regex]::Escape($name) + "$")
        ExitErr = Count-Regex (" T ExitErr\s+ID[^ ]+\s+" + [regex]::Escape($name) + "$")
    }
}

$required = @(
    "AIW AUTO LIVE STOP V1",
    "APP Safe Mode ON",
    "APP Reset Locks",
    "APP Status Snapshot",
    "APP Status Snapshot Simple"
) | ForEach-Object { Task-Stats $_ }

$danger = @(
    "FINAL Send Sheet",
    "FINAL Queue Cycle",
    "FINAL-Z-WOKER Every 2m Tick",
    "APP Start AI Worker",
    "APP Run Tick Once",
    "AIW AUTO LIVE START V1",
    "AIW AUTO LIVE TICK V1",
    "AIW SEND 1",
    "FINAL Archive Done Rows",
    "AIW DeadArchive",
    "AIW Compactor"
) | ForEach-Object { Task-Stats $_ }

$exitErr = Count-Regex " T ExitErr\s+"
$actionErr = Count-Regex " A Err\s+"
$handledAutoSheetsErr = 0
for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]
    if ($line -notmatch " A Err\s+" -or $line -notmatch "AIW PROOF Log Event|AutoSheets|autosheets|com\.joaomgcd\.autosheets") {
        continue
    }
    $windowEnd = [Math]::Min($lines.Count - 1, $i + 5)
    $window = ($lines[$i..$windowEnd] -join "`n")
    if ($window -match " A OK\s+.*AIW PROOF Log Event\.com\.joaomgcd\.autosheets" -and $window -match "%AIWProofWriteResult=OK|AIWProofWriteResult=OK|T ExitOK\s+.*AIW PROOF Log Event") {
        $handledAutoSheetsErr += 1
    }
}
$unhandledActionErr = [Math]::Max(0, $actionErr - $handledAutoSheetsErr)
$requiredStopOk = @($required | Where-Object { $_.Name -eq "AIW AUTO LIVE STOP V1" -and $_.ExitOK -ge 1 }).Count -gt 0
$safeModeOk = @($required | Where-Object { $_.Name -eq "APP Safe Mode ON" -and $_.ExitOK -ge 1 }).Count -gt 0
$resetOk = @($required | Where-Object { $_.Name -eq "APP Reset Locks" -and $_.ExitOK -ge 1 }).Count -gt 0
$snapshotOk = @($required | Where-Object { ($_.Name -eq "APP Status Snapshot" -or $_.Name -eq "APP Status Snapshot Simple") -and $_.ExitOK -ge 1 }).Count -gt 0
$dangerRan = @($danger | Where-Object { $_.Running -gt 0 -or $_.ExitOK -gt 0 -or $_.ExitErr -gt 0 }).Count -gt 0

$classification = "HOLD"
if ($exitErr -gt 0 -or $dangerRan) {
    $classification = "FAILED"
} elseif ($requiredStopOk -and $safeModeOk -and $resetOk -and $snapshotOk -and $exitErr -eq 0 -and $unhandledActionErr -eq 0) {
    $classification = "CANDIDATE / CLOSEOUT RUNLOG PASS / STILL NEED PROFILE OFF SCREENSHOT IF NOT INCLUDED"
}

$requiredRows = ($required | ForEach-Object { "| $($_.Name) | $($_.Running) | $($_.ExitOK) | $($_.ExitErr) |" }) -join "`n"
$dangerRows = ($danger | ForEach-Object { "| $($_.Name) | $($_.Running) | $($_.ExitOK) | $($_.ExitErr) |" }) -join "`n"
$runlogHash = (Get-FileHash -LiteralPath $RunlogPath -Algorithm SHA256).Hash

$reportText = @"
# AIW Stage3A Closeout Runlog Audit

## Classification

$classification

## Source

- Runlog: $RunlogPath
- Runlog bytes: $((Get-Item -LiteralPath $RunlogPath).Length)
- Runlog lines: $($lines.Count)
- Runlog SHA256: $runlogHash

## Required Closeout Tasks

| Task | T Running | T ExitOK | T ExitErr |
|---|---:|---:|---:|
$requiredRows

## Dangerous Path Scan

| Path | T Running | T ExitOK | T ExitErr |
|---|---:|---:|---:|
$dangerRows

## Error Counts

| Check | Count |
|---|---:|
| T ExitErr | $exitErr |
| A Err | $actionErr |
| Handled AutoSheets proof-log fallback A Err | $handledAutoSheetsErr |
| Unhandled A Err | $unhandledActionErr |

## Result Rules

- PASS requires stop, safe mode, reset locks, and status snapshot to exit OK.
- PASS also requires no dangerous path and no unhandled errors.
- Profile OFF proof must still be provided by screenshot or runlog evidence if not visible in this runlog.

## Next Step

If this closeout passes and profile OFF proof is captured, next layer is Stage4A Process-Only Proof.

Not send.
Not timer.
Not live.
"@

Set-Content -LiteralPath $report -Value $reportText -Encoding UTF8

@(
    [pscustomobject]@{File=[IO.Path]::GetFileName($RunlogPath); Path=$RunlogPath; SHA256=$runlogHash; Bytes=(Get-Item -LiteralPath $RunlogPath).Length; Classification="SOURCE RUNLOG"}
    [pscustomobject]@{File=[IO.Path]::GetFileName($report); Path=$report; SHA256=(Get-FileHash -LiteralPath $report -Algorithm SHA256).Hash; Bytes=(Get-Item -LiteralPath $report).Length; Classification="AUDIT REPORT"}
) | Export-Csv -LiteralPath $shaCsv -NoTypeInformation -Encoding UTF8

[pscustomobject]@{
    Classification = $classification
    Report = $report
    ReportSHA256 = (Get-FileHash -LiteralPath $report -Algorithm SHA256).Hash
    ShaCsv = $shaCsv
    ShaCsvSHA256 = (Get-FileHash -LiteralPath $shaCsv -Algorithm SHA256).Hash
} | ConvertTo-Json
