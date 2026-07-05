param(
    [Parameter(Mandatory=$true)]
    [string]$RunlogPath,

    [string]$OutDir = "C:\Users\Shadow\Documents\ai work\AI_WORKER_MASTER\03_PHONE_PROOF"
)

$ErrorActionPreference = "Stop"

if (!(Test-Path -LiteralPath $RunlogPath)) {
    throw "Runlog not found: $RunlogPath"
}

if (!(Test-Path -LiteralPath $OutDir)) {
    New-Item -Path $OutDir -ItemType Directory -Force | Out-Null
}

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$report = Join-Path $OutDir "AIW_STAGE4B_SEND_DRYRUN_RUNLOG_AUDIT_$timestamp.md"
$shaCsv = Join-Path $OutDir "SHA256_STAGE4B_SEND_DRYRUN_RUNLOG_AUDIT_$timestamp.csv"

$text = Get-Content -LiteralPath $RunlogPath -Raw
$lines = Get-Content -LiteralPath $RunlogPath

function Count-Literal([string]$needle) {
    if ([string]::IsNullOrEmpty($needle)) { return 0 }
    return ([regex]::Matches($text, [regex]::Escape($needle))).Count
}

function Count-Regex([string]$pattern) {
    return ([regex]::Matches($text, $pattern, [Text.RegularExpressions.RegexOptions]::IgnoreCase)).Count
}

function Count-TaskEvent([string]$task, [string]$event) {
    $escaped = [regex]::Escape($task)
    return Count-Regex("T\s+$event\s+ID[^\r\n]*\s$escaped(\r?\n|$)")
}

function Task-Row([string]$task) {
    [pscustomobject]@{
        Task = $task
        Running = Count-TaskEvent $task "Running"
        ExitOK = Count-TaskEvent $task "ExitOK"
        ExitErr = Count-TaskEvent $task "ExitErr"
    }
}

$required = @(
    "SS Safe Send Dry-Run"
)

$blocked = @(
    "FINAL Send Sheet",
    "SS Controlled One-Row Send Proof",
    "AIW SEND 1",
    "FINAL Send Sheet LEGACY",
    "AIW AUTO LIVE START V1",
    "AIW AUTO LIVE TICK V1",
    "APP Start AI Worker",
    "FINAL-Z-WOKER Every 2m Tick",
    "FINAL Archive Done Rows",
    "AIW DeadArchive",
    "AIW Compactor",
    "APP Archive Heavy Cleanup",
    "TT5"
)

$requiredRows = $required | ForEach-Object { Task-Row $_ }
$blockedRows = $blocked | ForEach-Object { Task-Row $_ }

$ssRun = $requiredRows[0].Running
$ssOk = $requiredRows[0].ExitOK
$ssErr = $requiredRows[0].ExitErr
$blockedRan = @($blockedRows | Where-Object { $_.Running -gt 0 -or $_.ExitOK -gt 0 -or $_.ExitErr -gt 0 }).Count

$noReady = Count-Literal "NO_READY"
$dryPass = (Count-Literal "DRYRUN_CONTACT_PICK_PASS") + (Count-Literal "SEND_DRYRUN_PASS")
$sendNo = Count-Literal "SEND=NO"
$sentOne0 = Count-Regex "Var Set,\s*%SSSentOne=0"
$sentOne1 = Count-Regex "Var Set,\s*%SSSentOne=1"
$buttonSend = Count-Literal "button_send"
$messageBox = Count-Literal "edit_text_out"
$textNowMarker = Count-Literal "com.enflick.android.TextNow"
$exitErr = Count-Literal "T ExitErr"
$actionErr = Count-Literal "A Err"
$handledAutoSheetsErr = Count-Regex "A Err[^\r\n]*AIW PROOF Log Event\.com\.joaomgcd\.autosheets"
$unhandledActionErr = [Math]::Max(0, $actionErr - $handledAutoSheetsErr)

$classification = "HOLD"
if ($ssErr -gt 0 -or $exitErr -gt 0 -or $blockedRan -gt 0 -or $buttonSend -gt 0 -or $sentOne1 -gt 0 -or $unhandledActionErr -gt 0) {
    $classification = "FAILED"
} elseif ($ssRun -ge 1 -and $ssOk -ge 1 -and $noReady -gt 0 -and $dryPass -eq 0 -and $buttonSend -eq 0 -and $messageBox -eq 0 -and $blockedRan -eq 0) {
    $classification = "CANDIDATE / STAGE4B NO-READY HOLD PASS / HOLD FOR CONTACT-SELECTION DRY-RUN"
} elseif ($ssRun -ge 1 -and $ssOk -ge 1 -and $dryPass -gt 0 -and $sentOne0 -gt 0 -and $sendNo -gt 0 -and $buttonSend -eq 0 -and $messageBox -eq 0 -and $blockedRan -eq 0) {
    $classification = "CANDIDATE / STAGE4B CONTACT-SELECTION DRY-RUN PASS / HOLD FOR NEXT PROOF"
}

$runlogHash = (Get-FileHash -LiteralPath $RunlogPath -Algorithm SHA256).Hash

function Markdown-TaskTable($rows) {
    $out = New-Object System.Collections.Generic.List[string]
    $out.Add("| Task | T Running | T ExitOK | T ExitErr |")
    $out.Add("|---|---:|---:|---:|")
    foreach ($row in $rows) {
        $out.Add("| $($row.Task) | $($row.Running) | $($row.ExitOK) | $($row.ExitErr) |")
    }
    return ($out -join "`r`n")
}

$requiredTable = Markdown-TaskTable $requiredRows
$blockedTable = Markdown-TaskTable $blockedRows

$reportText = @"
# AIW Stage4B Send Dry-Run Runlog Audit

## Classification

$classification

## Source

- Runlog: $RunlogPath
- Runlog bytes: $((Get-Item -LiteralPath $RunlogPath).Length)
- Runlog lines: $($lines.Count)
- Runlog SHA256: $runlogHash

## Required Stage4B Task

$requiredTable

## Blocked/Danger Path Scan

$blockedTable

## Marker Counts

| Check | Count |
|---|---:|
| NO_READY | $noReady |
| DRYRUN_CONTACT_PICK_PASS + SEND_DRYRUN_PASS | $dryPass |
| SEND=NO | $sendNo |
| %SSSentOne=0 | $sentOne0 |
| %SSSentOne=1 | $sentOne1 |
| TextNow marker | $textNowMarker |
| edit_text_out marker | $messageBox |
| button_send marker | $buttonSend |
| T ExitErr | $exitErr |
| A Err | $actionErr |
| Handled AutoSheets proof-log fallback A Err | $handledAutoSheetsErr |
| Unhandled A Err | $unhandledActionErr |

## Result Rules

- NO_READY pass requires SS Safe Send Dry-Run ExitOK, NO_READY marker, no blocked tasks, no message box marker, no button_send marker, and no unhandled errors.
- Contact-selection dry-run pass requires SS Safe Send Dry-Run ExitOK, dry-run pass marker, SEND=NO, %SSSentOne=0, no blocked tasks, no message box marker, no button_send marker, and no unhandled errors.
- Any real send path, button_send marker, %SSSentOne=1, blocked task run, ExitErr, or unhandled A Err is FAILED.

## Next Step If Passes

- If NO_READY passes: prepare exactly one approved READY_TO_SEND test row, then rerun SS Safe Send Dry-Run for contact-selection proof.
- If contact-selection dry-run passes: remain HOLD until the next approved proof layer.

Do not claim locked.
Do not claim ready.
Do not claim live-send proof.
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
}
