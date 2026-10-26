# automatingExercises

## Goal

Build a fully automated system that creates exercise solution slides: slides I can present in the exercise class and that students can follow and understand on their own.

## Approach

We follow Tim Dettmers' guide on working with agents:
https://timdettmers.com/2026/01/13/use-agents-or-be-left-behind/

## Usage

The whole pipeline is started with one command, with the path to the exercise PDF as its only required argument:

```bash
auto_exercises path/to/sheet.pdf
```

- `auto_exercises` is a single command-line script; it runs every stage (read the PDF, solve, check, make slides) without further interaction.
- The PDF path is a positional argument, so no flag is needed (`auto_exercises sheet03.pdf`).
- Output goes to a new folder next to the PDF, named after it (e.g. `sheet03_solutions/`), containing the slides as PDF plus their editable LaTeX source.
- On success the script prints where the slides are; if it stops (see "When the pipeline stops"), it prints the reason and exits with a non-zero code.
- `auto_exercises --help` explains the usage.

## Current state (stage 1: solving)

`auto_exercises sheet.pdf` currently does:

1. Checks the PDF (exists, readable, not encrypted).
2. Creates `sheet_solutions/` next to the PDF. It refuses if the folder already exists; `--force` replaces it.
3. Puts the original PDF, its extracted text (`pdftotext -layout`) and one PNG per page into `source/`.
4. Starts a Claude Code agent (`claude -p`, no web access) in that folder with `prompts/solve.md`, and prints its progress. The full log goes to `agent.log`.
5. The agent writes:
   - `exercises.md`: a list of every problem and task, with source pages
   - `solutions/problem-X.md`: for each task: idea, step-by-step solution, result, check, pitfalls and takeaways
   - `code/` and `figures/`: runnable Python and the plots it makes
   - `REPORT.md`: status per task (solved/partial/blocked), how it was checked, confidence, and open questions
6. Exits with code 0 only if the agent finished and wrote `REPORT.md`.

Options: `--model`, `--force`, `--dry-run` (prepare the folder and print the prompt without starting the agent).

Setup: the script is `bin/auto_exercises`, symlinked into `~/.local/bin`. The agent runs Python from `.venv/` (numpy, scipy, matplotlib, pandas, sympy).

Not built yet: slides, independent checking of the solutions, and supplied data files (a task that needs a missing file, e.g. a CSV, is marked `BLOCKED`).

## Input

The pipeline takes exactly one input: **one PDF file that contains all the exercises** (an exercise sheet).

### File

- Format: PDF (`.pdf`), one file per run.
- Content: one exercise sheet, i.e. all exercises that the slides should cover.
- The PDF is the only source of truth for the exercise statements. Nothing else (no solutions, no lecture notes) is required.
