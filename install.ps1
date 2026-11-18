# Εγκατάσταση: skill στο Claude Code + μεταβλητή περιβάλλοντος + κλώνος του watermarks-remover.
$ErrorActionPreference = "Stop"
foreach ($t in "git", "python") { if (-not (Get-Command $t -ErrorAction SilentlyContinue)) { throw "Λείπει το $t. Εγκατάστησέ το και ξανατρέξε." } }
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) { Write-Warning "Δεν βρέθηκε το Docker. Χρειάζεται το Docker Desktop για τον έλεγχο μεταδεδομένων." }
$repo = $PSScriptRoot
$skills = Join-Path $env:USERPROFILE ".claude\skills\final-check"
New-Item -ItemType Directory -Force $skills | Out-Null
Copy-Item (Join-Path $repo "skill\SKILL.md") $skills -Force
[Environment]::SetEnvironmentVariable("FINAL_CHECK_DIR", $repo, "User")
$wr = Join-Path (Split-Path $repo) "watermarks-remover"
if (-not (Test-Path $wr)) { git clone https://github.com/guillaumemeyer/watermarks-remover.git $wr }
[Environment]::SetEnvironmentVariable("WATERMARKS_REMOVER_DIR", $wr, "User")
Write-Host "Έτοιμο. Κλείσε και ξανάνοιξε το Claude Code, άνοιξε το Docker Desktop και τρέξε /final-check `"C:\path\to\report.docx`""
