# Install: skill for Claude Code + environment variables + clone of watermarks-remover.
foreach ($t in "git", "python") { if (-not (Get-Command $t -ErrorAction SilentlyContinue)) { throw "Missing $t. Install it and run again." } }
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) { Write-Warning "Docker not found. Docker Desktop is needed for the metadata check." }
$repo = $PSScriptRoot
$scope = if ($env:FINAL_CHECK_TEST) { "Process" } else { "User" }  # test mode: do not touch the real user variables
$skills = Join-Path $env:USERPROFILE ".claude\skills\final-check"
New-Item -ItemType Directory -Force $skills | Out-Null
Copy-Item (Join-Path $repo "skill\SKILL.md") $skills -Force
[Environment]::SetEnvironmentVariable("FINAL_CHECK_DIR", $repo, $scope)
$wr = Join-Path (Split-Path $repo) "watermarks-remover"
if (-not (Test-Path $wr)) {
    git clone -q https://github.com/guillaumemeyer/watermarks-remover.git $wr
    if ($LASTEXITCODE -ne 0) { throw "git clone of watermarks-remover failed." }
}
[Environment]::SetEnvironmentVariable("WATERMARKS_REMOVER_DIR", $wr, $scope)
Write-Host "Done. Restart Claude Code, open Docker Desktop, then run: /final-check `"C:\path\to\report.docx`""
