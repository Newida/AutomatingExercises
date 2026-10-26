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

## Current state (solve, then slides)

`auto_exercises sheet.pdf` runs in two phases.

**Phase 1: check inputs. It complains until it has everything.**

1. Checks the PDF (exists, readable, not encrypted) and creates `sheet_solutions/` next to it (with the PDF, its text and one PNG per page in `source/`).
2. A short agent run (`prompts/check_inputs.md`, log `check.log`) reads the sheet and writes `source/requirements.json`: every external file the tasks need (data sets, provided code), with the tasks that use it and where the sheet says to get it, plus every Python package the sheet expects that is not installed.
3. The script then checks this list. It looks for files next to the PDF, anywhere in `sheet_data/` and in any `--data DIR`, and checks packages in `.venv`.
4. If anything is missing it stops with exit code 2 and lists what is missing, which tasks need it and how to fix it. Nothing is solved yet. Rerun the same command once the inputs are there: the folder and the list are reused, so the check does not run again. If the list is wrong, edit `requirements.json`, or start over with `--force`.

**Phase 2: solve. No human in the loop.**

5. All found files are copied into `data/`. Then a Claude Code agent (`claude -p`, no web access, `prompts/solve.md`) solves everything without asking questions, logging to `agent.log`. It writes:
   - `exercises.md`: a list of every problem and task, with source pages
   - `solutions/problem-X.md`: for each task: idea, step-by-step solution, result, check, pitfalls and takeaways
   - `code/` and `figures/`: runnable Python and the plots it makes
   - `REPORT.md`: status per task (solved/partial/blocked), how it was checked, confidence, and open questions
6. Exits with code 0 only if the agent finished and wrote `REPORT.md`.

Options: `--model`, `--data DIR` (repeatable), `--force` (start over), `--dry-run` (prepare the folder and print the prompt without starting an agent).

Setup: the script is `bin/auto_exercises`, symlinked into `~/.local/bin`. All agents use one Python environment, `.venv/` (Python 3.12; numpy, scipy, sympy, pandas, matplotlib, seaborn, scikit-learn, jax, torch, torchvision, CPU only; `csv` is built in). It is defined in `env/requirements.txt` and built by `bin/setup_env`. Agents never install packages: the input check complains about missing ones before solving, and a solver that still finds one missing marks the task `BLOCKED (missing package ...)` and lists it under **Missing dependencies** in `REPORT.md`. To add a package: append it to `env/requirements.txt` and run `bin/setup_env`.


### Phase 3: slides

A fresh agent turns the solutions into slides using the shared template:

- `templates/slides/exslides.sty`: the look (colours, boxes, footer). Change the design only here.
- `templates/slides/slides.tex`: the skeleton with patterns: title, overview, per problem a divider, per task
  (1) what is asked, (2) idea, (3) solution steps with `\pause`, (4) code, (5) figure, (6) result + check,
  (7) pitfalls & takeaway; summary table at the end.
- `prompts/slides.md`: rules for the slide agent (one thought per slide, words for every step, numbers must
  match the solutions, doubts go to `NOTES.md`, never invent plots).
- `bin/build_slides DIR`: builds `slides.pdf` (with reveal steps, for presenting) and `handout.pdf`
  (one page per slide, for students); fails on LaTeX errors or leftover `<<placeholders>>`.

Output: `<sheet>_solutions/slides/` with `slides.tex`, `slides.pdf`, `handout.pdf`, `NOTES.md` (for the instructor).
Remake only the slides of an already solved sheet: `auto_exercises sheet.pdf --slides-only`.

Not built yet: independent checking of the solutions.

## Input

The pipeline takes exactly one input: **one PDF file that contains all the exercises** (an exercise sheet).

### File

- Format: PDF (`.pdf`), one file per run.
- Content: one exercise sheet, i.e. all exercises that the slides should cover.
- The PDF is the only source of truth for the exercise statements. Nothing else (no solutions, no lecture notes) is required.
