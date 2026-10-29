You are preparing to solve an exercise sheet. Before anyone solves anything, find out what the solver will need that is NOT contained in the sheet itself. Do not solve any exercise.

You work inside the solution directory (your current working directory).

## What you have

- `source/sheet.pdf`: the exercise sheet.
- `source/sheet.txt`: its text (`pdftotext -layout`).
- `source/pages/page-*.png`: one image per page; look at them when the text is unclear.
- Python environment for the solver: `{python}`. Already installed: {packages}.
- Files the user has put next to the sheet or in its data folders:

{available}

## What to look for

1. **Files**: every external file a task needs: data sets (CSV, TXT, NPY, images, ...), provided code skeletons or modules, any file the sheet says is "provided", "on eCampus", "attached", "from the website", etc. Use the exact file name the sheet gives. If the sheet gives no exact name, or a slightly different one, and one of the files the user has put there is clearly that file, use its exact name (as listed) and say so in `note`. Otherwise invent a short clear name and say so in `note`. List a needed file even if it is present; presence is checked afterwards.
2. **Python packages**: every package you think the solver needs to solve a task properly (the sheet says "use PyTorch", shows `import torch`, or the task is clearly meant for a library) that is not already installed. Use the pip name. The solver cannot install anything, so list it here rather than hope it works out.

Do not list things that the solver can produce itself (plots, its own code, synthetic data the sheet asks to generate) or things defined in the sheet.

## Output

Write exactly one file, `source/requirements.json`, and nothing else:

```json
{
  "files": [
    {"name": "dataMyspace201303.csv", "tasks": ["2.1.1", "2.2"], "what": "Google Trends time series for 'myspace'", "where": "what the sheet says about where to get it, or null", "note": null}
  ],
  "packages": [
    {"name": "torch", "tasks": ["2.8"], "why": "sheet says to implement the network in PyTorch"}
  ]
}
```

Use empty lists if nothing is needed. Be complete: a missing item here means the solver gets stuck later with no human to ask.
