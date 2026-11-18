---
name: final-check
description: Final pre-submission check of a finished report (.docx). Runs the ai-detector-check reading (Mode B) and the file-metadata check (remove-ai-marks service), then merges both into one tabbed HTML report. Use when the user types /final-check FILE or says a report/assignment is finished and wants the final check.
---

# Final check (one command)

Usage: `/final-check "C:\path\to\report.docx"`. Output folder: `<file folder>\ai-check\` (create it).
Never modify the original file. Respond in the user's language (Greek).

## Steps

0. If `$env:FINAL_CHECK_DIR` is empty, tell the user to run `install.ps1` from the final-check repo. If the `ai-detector-check` skill is not installed, tell the user, skip steps 1 and 3 and run only step 2.
1. **Text reading (Mode B).** Follow the loaded `anthropic-skills:ai-detector-check` skill, Mode B:
   - Dry run to list paragraphs: find `detect.py` with `Get-ChildItem "$env:LOCALAPPDATA\Claude-Data" -Recurse -Filter detect.py` and run `python detect.py FILE` (sends nothing, exit code 2 is normal).
   - Rate each substantive paragraph (`human|ai|mixed|uncertain`, confidence, verbatim evidence <=12 words, short Greek `evidence_note`) per `references/claude-assessment-protocol.md`. Skip cover page, headings, equations, captions, references. Prior is human. Weak evidence means `uncertain`.
   - Save `ai-check\ratings.json` (with `ai_share_low`, `ai_share_high`, `verdict`) and render:
     `python render_report.py FILE ai-check\ratings.json --lang el --out ai-check\text-report.html`
   - If the user has `PANGRAM_API_KEY` / `GPTZERO_API_KEY` / `ORIGINALITY_API_KEY` and clearly consents to sending the text, Mode A is allowed; otherwise stay in Mode B and send nothing.
2. **File metadata.** Run:
   `python "$env:FINAL_CHECK_DIR\meta_check.py" FILE --out <file folder>\ai-check`
   It starts the local Docker service if needed (Docker Desktop must be running; exit code 2 means the service is down, tell the user and do not clean locally), runs inspect and clean on a copy, and writes `cleaning-visual.html`, `evidence.json` and `<name>.cleaned.docx`.
3. **Merge.** `python "$env:FINAL_CHECK_DIR\combine.py" ai-check\text-report.html ai-check\cleaning-visual.html ai-check\combined-report.html "Αναφορά ελέγχου AI: <file name>"`
4. **Deliver.** Send `combined-report.html` with SendUserFile (display render). It contains the full text of the assignment: keep it private, never publish it as an artifact unless asked.
5. **Summarise in 4-5 lines:** AI-share range (never a single number), flagged paragraphs, what metadata was found and removed, and whether visible text and run counts stayed identical.

## Rules

- This is an editor's reading and a metadata scan. Neither proves authorship, and neither predicts Turnitin or GPTZero. Never say "100% human", "safe" or "undetectable".
- One check, at most one re-check after an edit. Do not loop "rewrite, test, rewrite".
- Remind the user once to check whether the course requires disclosing AI use in drafting.
- Clean only the user's own files, only into a `*.cleaned.*` copy.
