# AutomatingExercises

Turn an exercise sheet (PDF) into solution slides with one command.

```bash
auto_exercises sheet03.pdf
```

Claude Code agents read the sheet, solve every task (with runnable Python code and plots) and then make a
Beamer slide deck that you can present in the exercise class and that students can follow on their own.
There is no human in the loop once the inputs are complete.

The approach follows Tim Dettmers' guide on working with agents:
https://timdettmers.com/2026/01/13/use-agents-or-be-left-behind/

## Setup

Linux (or macOS) with:

| Needed | For | Install (Debian/Ubuntu) |
|---|---|---|
| [Claude Code](https://claude.com/claude-code) CLI `claude`, logged in | the agents | `npm install -g @anthropic-ai/claude-code`, then run `claude` once to log in |
| Python 3.12 | the solver environment | `uv python install 3.12` (or your system's `python3.12`) |
| poppler (`pdftotext`, `pdftoppm`, `pdfinfo`) | reading the sheet, page images | `sudo apt install poppler-utils` |
| `pdflatex` with beamer, the metropolis theme, lmodern, listings, booktabs | building the slides | `sudo apt install texlive-latex-extra texlive-fonts-recommended lmodern` |

Then:

```bash
git clone <this repo> AutomatingExercises
cd AutomatingExercises
bin/setup_env                      # builds .venv/ from env/requirements.txt (a few GB: torch, jax)
ln -s "$PWD/bin/auto_exercises" ~/.local/bin/auto_exercises   # optional: call it from anywhere
```

`bin/setup_env` uses `python3.12` from your PATH; to use another interpreter, run `PYTHON=/path/to/python3.12 bin/setup_env`.

## Usage

```bash
auto_exercises path/to/sheet.pdf                      # full run: check inputs, solve, make slides
auto_exercises sheet.pdf --data ~/datasets            # extra folder to look for data files (repeatable)
auto_exercises sheet.pdf --slides-only                # only remake the slides of an already solved sheet
auto_exercises sheet.pdf --model sonnet --effort low  # cheaper / faster agents
auto_exercises --help
```

| Option | Meaning |
|---|---|
| `--model MODEL` | Claude model for every agent (default: Claude Code's default) |
| `--effort LEVEL` | `low`, `medium`, `high`, `xhigh`, `max`: reasoning effort for every agent. If the model does not support it, the run stops at once with the agent's error |
| `--style NAME` | personal presentation style: `styles/NAME.md` (default: `lukas`), a path to a `.md` file, or `none` (see [Your personal style](#your-personal-style)) |
| `--data DIR` | extra folder to search for data files the sheet needs (repeatable) |
| `--slides-only` | keep the solutions, only redo the slides (use this after changing the slide templates) |
| `--force` | delete an existing `<sheet>_solutions/` folder and start over |
| `--dry-run` | prepare the folder and print the solver prompt, without starting an agent |

The input is one PDF with the whole exercise sheet. Nothing else is needed: no solutions, no lecture notes.
Data files the sheet refers to (CSV files, provided code) are looked for next to the PDF, in `<sheet>_data/` and in every `--data DIR`.

### What happens

1. **Check inputs.** An agent reads the sheet and lists every data file and Python package it needs
   (`source/requirements.json`). If something is missing, the script stops with exit code 2 and says what is
   missing, which tasks need it and how to fix it. Add the files and rerun the same command; the check is not repeated.
2. **Solve.** An agent (no web access) solves every task and writes the solutions, code and a report.
3. **Slides.** A fresh agent turns the solutions into slides by filling in the slide template
   (see [the templates](#the-slides-templates-you-can-change)), builds them and looks at the slide images to fix layout problems.

Each stage stops at once with the agent's error message if the agent fails.

### Output

Everything goes to a new folder next to the PDF, `<sheet>_solutions/`:

| Path | Content |
|---|---|
| `slides/slides.pdf`, `slides/slides.tex` | the slides and their editable LaTeX source |
| `slides/NOTES.md` | for the instructor: low-confidence tasks, open questions, what was simplified, slide number and type of each task |
| `REPORT.md` | status (solved / partial / blocked) and confidence per task, how it was checked |
| `exercises.md` | list of all problems and tasks, with page numbers |
| `solutions/problem-*.md` | full worked solution per problem: idea, steps, result, check, pitfalls |
| `code/`, `figures/` | the Python scripts, their saved output (`code/*.out`) and the plots |
| `source/` | the sheet, its text, page images and the exact prompts that were used |
| `check.log`, `agent.log`, `slides.log` | full agent logs |

## The slides: templates you can change

The look and the structure of the slides are defined in four files, plus your personal style (next section). Change them to fit your course; every new
run (or `--slides-only`) picks up the changes.

| File | What it defines | Change it to ... |
|---|---|---|
| [`templates/slides/pattern.md`](templates/slides/pattern.md) | **which slides exist, in which order, and what each one says**, sentence by sentence | change how tasks are presented (see below) |
| [`templates/slides/exslides.sty`](templates/slides/exslides.sty) | the look: Metropolis theme, fonts, colours, code style, the coloured stage labels | change the design. The agent never edits this file, so every deck looks the same |
| [`templates/slides/slides.tex`](templates/slides/slides.tex) | an empty deck with one frame per kind of slide, showing only its layout (columns, tables, code, boxed result) | change the layout of a kind of slide, or add one for a new kind |
| [`prompts/slides.md`](prompts/slides.md) | the rules for the slide agent that hold for every slide: about 8 lines per slide at most, nothing smaller than `\footnotesize`, every step explained in words, numbers taken from the solutions, images cut from the sheet, ... | change the general writing and layout rules |

The stage labels (defined in `exslides.sty`) show on every slide where we are:
`\Refresh` (refresher), `\Given` (recap), `\Byhand` (step 1), `\Algo` (step 2), `\Impl` (step 3), `\Answer` (question and answer).

The other agents can be adapted the same way: `prompts/check_inputs.md` (input check) and `prompts/solve.md` (solver).
The Python packages available to the solver are in `env/requirements.txt` (add one, then rerun `bin/setup_env`).

### How `pattern.md` works

`pattern.md` is pasted into the slide agent's prompt as it is, and the agent follows it exactly. It is written
as plain sentences, one numbered line per slide, saying what the slide contains and in which order:

```markdown
4. The algorithm slide gives the method as numbered steps in words, from input to output, and ends with the main pitfall.
```

It has four parts:

1. **The deck**: title slide, refresher, then each problem in sheet order, then the takeaways.
2. **A problem's recap**: the Given slide (data, model, formulas), then an overview of its tasks.
3. **A task**: first the background the sheet puts before it, then its solution.
4. **Task types** (`## Task types`): the agent decides for each task which type it is and follows that type's pattern:
   - `### Computation (the default)`: what is asked, then step 1 by hand (a toy example only if the real data is
     too big or hides the point), step 2 algorithm, step 3 implementation, result and plot.
   - `### Question list` (a task that only asks questions, e.g. "think about ..."): question, short answer,
     next question, next answer, ...

### Adding a rule

- **Change what a slide says**: edit its sentence. Write what the slide *contains*, in order, in full sentences
  ("The result slide states the final answer in a box, then lists the independent checks.").
- **A rule for some tasks only**: add a sentence with the condition and, ideally, an example with its reason:
  "There is a toy slide only if the real data is too big to work through by hand or hides the point
  (for example ...); otherwise ...". The agent applies the reason to other sheets, so the reason matters more than the example.
- **A new task type**: add a block under `## Task types`, for example:

  ```markdown
  ### Proof

  The task asks to prove a statement, with no data and no code.
  1. The statement slide restates what is to be proven and names the assumptions.
  2. The idea slide gives the proof strategy in one or two sentences.
  3. The proof slides give the proof in numbered steps, one idea per slide, with every step explained in words.
  4. The last slide says where each assumption was used.
  ```

  Start with a sentence saying **when** a task is of this type, so the agent can recognise it; then one line per slide.
  If none of the types fits, the agent uses the default type.
- **A new kind of slide** (a new layout): also add an empty example frame for it to `slides.tex`, with a comment
  on its layout. A new stage label goes into `exslides.sty` (e.g. `\newcommand{\Proof}{\stage{hand}{Proof}}`)
  and into the label list in `prompts/slides.md`.

To try a change, remake the slides of a sheet that is already solved: `auto_exercises sheet.pdf --slides-only`
(this replaces only `slides/`). `slides/NOTES.md` lists the type the agent chose for each task.

## Your personal style

The pattern says *which* slides there are; a style profile in `styles/` says *how* they are written: the
voice, how things are explained, what is always stressed, phrases to use and to avoid. It is pasted into
the slide agent's prompt after the pattern. It only changes wording, tone and emphasis; where it conflicts
with the pattern or the slide rules, those win.

`styles/lukas.md` is the default. To use your own:

1. Copy it: `cp styles/lukas.md styles/yourname.md`, and rewrite each section for yourself
   (Voice, How I explain, What I always stress, Emphasis and look, Phrases I use, Never).
2. Add a few lines of your own writing at the end (a blog post, slides, an email to students). Examples are the
   strongest signal for the agent. Take them from **other topics** than the sheets, so the agent copies the style, not the content.
3. Run with `--style yourname` (or `--style path/to/file.md`). To make it your default, change `default="lukas"`
   of `--style` in `bin/auto_exercises`. `--style none` gives a neutral style.

Try it on a solved sheet with `--slides-only --style yourname`.

## Repository layout

```
bin/auto_exercises     the pipeline (Python script)
bin/build_slides DIR   compiles DIR/slides.tex, renders one image per slide, fails on errors or leftover placeholders
bin/setup_env          builds .venv/ from env/requirements.txt
env/requirements.txt   Python packages for the solver
prompts/               the prompts of the three agents (check_inputs.md, solve.md, slides.md)
templates/slides/      the slide templates (pattern.md, exslides.sty, slides.tex)
styles/                personal presentation styles (lukas.md, ...)
```

## Good to know

- **Time and cost**: a full sheet takes a while (the slide stage alone is often 10+ minutes). For quick tests
  use a short sheet, `--model sonnet` or `--effort low`.
- **Agents never install packages.** A missing package is reported by the input check; a task that still needs
  one is marked `BLOCKED` in `REPORT.md`.
- **Check the results.** The solver checks its own work and reports its confidence per task, but there is no
  independent check yet. Read `REPORT.md` and `slides/NOTES.md` before presenting.
- The agents run with `--permission-mode bypassPermissions` (no permission prompts) inside the output folder, without web access.
