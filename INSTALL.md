# Install instructions (for Claude)

If the user pasted the link to this repository and asked you to install it, follow these steps in order.
Reply to the user in their language (Greek). Windows + PowerShell only.

Do not ask for API keys, passwords or tokens. Do not change anything outside the folders named below.

## 1. Check prerequisites

Run `git --version`, `python --version` and `docker --version`.
- `git` or `python` missing: tell the user to install it (git-scm.com, python.org), then stop.
- `docker` missing: continue, but tell the user at the end that Docker Desktop is needed for the metadata tab (docker.com/products/docker-desktop).

## 2. Get the repo

```powershell
$dest = Join-Path $env:USERPROFILE "final-check"
if (Test-Path $dest) { git -C $dest pull } else { git clone https://github.com/nitrogenxv/final-check $dest }
```

## 3. Run the installer

```powershell
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\final-check\install.ps1"
```

It copies `skill\SKILL.md` to `~\.claude\skills\final-check`, clones `watermarks-remover` next to the repo and sets the user variables `FINAL_CHECK_DIR` and `WATERMARKS_REMOVER_DIR`.

## 4. Verify

- `Test-Path "$env:USERPROFILE\.claude\skills\final-check\SKILL.md"` is True
- `[Environment]::GetEnvironmentVariable("FINAL_CHECK_DIR","User")` points to the repo and `meta_check.py` exists there
- `watermarks-remover\compose.yaml` exists next to the repo

## 5. Optional text tab

The text-reading tab needs the Claude skill `ai-detector-check` (not part of this repo). Check whether it is in your skill list. If not, tell the user the text tab will be skipped and only the metadata check runs.

## 6. Tell the user

- Close and reopen Claude Code so the skill and variables load.
- Docker Desktop must be installed. The check starts Docker Desktop and the local service by itself if they are stopped; the very first run builds the service and takes a few minutes.
- Usage: `/final-check "C:\path\to\report.docx"`
- The check is not proof of authorship; they should also check whether their course requires disclosing AI use.
