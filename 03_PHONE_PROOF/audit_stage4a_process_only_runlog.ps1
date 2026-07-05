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

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$report = Join-Path $OutDir "AIW_STAGE4A_PROCESS_ONLY_RUNLOG_AUDIT_$timestamp.md"
$shaCsv = Join-Path $OutDir "SHA256_STAGE4A_PROCESS_ONLY_RUNLOG_AUDIT_$timestamp.csv"

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
    "QC R4A APP Tick No-Work Proof",
    "APP Reset Locks",
    "QC Selection Hardening Audit",
    "APP Run Tick Once",
    "FINAL Queue Cycle",
    "AIW PROOF Log Event"
) | ForEach-Object { Task-Stats $_ }

$blocked = @(
    "FINAL Send Sheet",
    "AIW SEND 1",
    "AIW AUTO LIVE START V1",
    "AIW AUTO LIVE TICK V1",
    "APP Start AI Worker",
    "FINAL-Z-WOKER Every 2m Tick",
    "FINAL Archive Done Rows",
    "AIW DeadArchive",
    "AIW Compactor",
    "APP Archive Heavy Cleanup",
    "TT5"
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

function Has-ExitOk([string]$name, [int]$min = 1) {
    return @($required | Where-Object { $_.Name -eq $name -and $_.ExitOK -ge $min }).Count -gt 0
}

$wrapperOk = Has-ExitOk "QC R4A APP Tick No-Work Proof"
$resetOk = Has-ExitOk "APP Reset Locks"
$selectionAuditOk = Has-ExitOk "QC Selection Hardening Audit" 2
$runTickOk = Has-ExitOk "APP Run Tick Once"
$queueCycleOk = Has-ExitOk "FINAL Queue Cycle"
$proofLogOk = Has-ExitOk "AIW PROOF Log Event"

$passMarkers = @(
    "QC_R4A_APP_TICK_NO_WORK_PASS",
    "PASS: R4A app tick no-work path is clean",
    "R4A_APP_TICK_NO_WORK",
    "PRE and POST selection clean. Queue cycle no-work path ran once"
)
$passMarkerHits = @($passMarkers | Where-Object { $text -like "*$_*" }).Count
$failMarkerHits = Count-Regex "FAIL/HOLD|FAIL_PRE_|FAIL_POST_|FAIL_BUSY_LOCK|PRE_NEW_ROWS_PRESENT|POST_NEW_ROWS_PRESENT"
$blockedRan = @($blocked | Where-Object { $_.Running -gt 0 -or $_.ExitOK -gt 0 -or $_.ExitErr -gt 0 }).Count -gt 0

$classification = "HOLD"
if ($exitErr -gt 0 -or $blockedRan -or $unhandledActionErr -gt 0) {
    $classification = "FAILED"
} elseif ($wrapperOk -and $resetOk -and $selectionAuditOk -and $runTickOk -and $queueCycleOk -and $proofLogOk -and $passMarkerHits -gt 0 -and $failMarkerHits -eq 0) {
    $classification = "CANDIDATE / STAGE4A PROCESS-ONLY PASS / HOLD FOR NEXT PROOF"
}

$requiredRows = ($required | ForEach-Object { "| $($_.Name) | $($_.Running) | $($_.ExitOK) | $($_.ExitErr) |" }) -join "`n"
$blockedRows = ($blocked | ForEach-Object { "| $($_.Name) | $($_.Running) | $($_.ExitOK) | $($_.ExitErr) |" }) -join "`n"
$runlogHash = (Get-FileHash -LiteralPath $RunlogPath -Algorithm SHA256).Hash

$reportText = @"
# AIW Stage4A Process-Only Runlog Audit

## Classification

$classification

## Source

- Runlog: $RunlogPath
- Runlog bytes: $((Get-Item -LiteralPath $RunlogPath).Length)
- Runlog lines: $($lines.Count)
- Runlog SHA256: $runlogHash

## Required Stage4A Tasks

| Task | T Running | T ExitOK | T ExitErr |
|---|---:|---:|---:|
$requiredRows

## Blocked/Danger Path Scan

| Path | T Running | T ExitOK | T ExitErr |
|---|---:|---:|---:|
$blockedRows

## Marker Counts

| Check | Count |
|---|---:|
| PASS marker hits | $passMarkerHits |
| FAIL/HOLD marker hits | $failMarkerHits |
| T ExitErr | $exitErr |
| A Err | $actionErr |
| Handled AutoSheets proof-log fallback A Err | $handledAutoSheetsErr |
| Unhandled A Err | $unhandledActionErr |

## Result Rules

- PASS requires `QC R4A APP Tick No-Work Proof`, `APP Run Tick Once`, `FINAL Queue Cycle`, and two `QC Selection Hardening Audit` runs to exit OK.
- PASS requires no blocked send/timer/live/archive/deadarchive/compactor paths.
- PASS requires no unhandled errors and no FAIL/HOLD markers.
- This proves process-only no-work behavior only.

## Next Step If Passes

Next layer is send dry-run/hold proof.

Not one-send.
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
