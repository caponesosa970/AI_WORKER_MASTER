param(
  [Parameter(Mandatory = $true)]
  [string]$XmlPath
)

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
$duplicateIds = @()
$duplicateNames = @()

foreach ($task in $tasks) {
  $idNode = $task.SelectSingleNode("id")
  $nameNode = $task.SelectSingleNode("nme")

  if ($idNode) {
    if (-not $taskIds.Add($idNode.InnerText)) {
      $duplicateIds += $idNode.InnerText
    }
  }

  if ($nameNode) {
    if (-not $taskNames.Add($nameNode.InnerText)) {
      $duplicateNames += $nameNode.InnerText
    }
  }
}

$missingProfileRefs = @()
foreach ($profile in $profiles) {
  foreach ($mid in @($profile.ChildNodes | Where-Object { $_.Name -match "^mid\d+$" })) {
    if (-not $taskIds.Contains($mid.InnerText)) {
      $profileName = $profile.SelectSingleNode("nme")
      $missingProfileRefs += [pscustomobject]@{
        profile = if ($profileName) { $profileName.InnerText } else { "" }
        task_id = $mid.InnerText
      }
    }
  }
}

$missingPerformRefs = @()
foreach ($action in @($xml.SelectNodes("//Action[code='130']"))) {
  $target = $action.SelectSingleNode("Str[@sr='arg0']")
  if ($target -and $target.InnerText -and -not $taskNames.Contains($target.InnerText)) {
    $sourceName = $action.ParentNode.SelectSingleNode("nme")
    $missingPerformRefs += [pscustomobject]@{
      source = if ($sourceName) { $sourceName.InnerText } else { "" }
      target = $target.InnerText
    }
  }
}

$clickRefs = @([regex]::Matches($text, "<clickTask>(-?\d+)</clickTask>") | ForEach-Object { $_.Groups[1].Value })
$missingClickRefs = @($clickRefs | Where-Object { $_ -notmatch "^-" -and -not $taskIds.Contains($_) } | Sort-Object -Unique)

$hash = Get-FileHash -Algorithm SHA256 -LiteralPath $resolved

$report = [ordered]@{
  file = $resolved.Path
  sha256 = $hash.Hash
  xml_parse = "PASS"
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
  build95_marker_count = ([regex]::Matches($text, "BUILD95")).Count
  build99_marker_count = ([regex]::Matches($text, "BUILD99")).Count
  build100_marker_count = ([regex]::Matches($text, "BUILD100")).Count
  patch83_marker_count = ([regex]::Matches($text, "PATCH83")).Count
  json_true_count = ([regex]::Matches($text, "json:true")).Count
  se_true_count = ([regex]::Matches($text, "<se>true</se>")).Count
  mojibake_A_count = ([regex]::Matches($text, [string][char]0x00C3)).Count
  section_sign_count = ([regex]::Matches($text, [string][char]0x00A7)).Count
  openai_key_marker_present = ($text.Contains("OPENAI_API_KEY") -or $text.Contains("sk-"))
  textnow_marker_count = ([regex]::Matches($text, "TextNow", "IgnoreCase")).Count
  auto_live_tick_present = $text.Contains("AIW AUTO LIVE TICK V1")
  watchdog_marker_count = ([regex]::Matches($text, "watchdog", "IgnoreCase")).Count
  recovery_marker_count = ([regex]::Matches($text, "recovery", "IgnoreCase")).Count
  failure_ledger_marker_count = ([regex]::Matches($text, "failure ledger", "IgnoreCase")).Count
  regression_ledger_marker_count = ([regex]::Matches($text, "regression ledger", "IgnoreCase")).Count
}

$report.GetEnumerator() | ForEach-Object {
  "{0}: {1}" -f $_.Key, $_.Value
}

if ($missingProfileRefs.Count -or $missingPerformRefs.Count -or $missingClickRefs.Count) {
  exit 2
}

