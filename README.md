# Sleep-Analysis

DATA3800 group project: does working alongside studies affect students' sleep?
Data: NHIS 2024 Sample Adult file (CDC).

## Get started

1. Install [uv](https://docs.astral.sh/uv/) (once). It fetches the right Python (3.14.7) for you.
2. In the project folder, run:

```bash
python scripts/setup.py      # once: creates .venv, installs packages, downloads the data
python scripts/notebook.py   # opens JupyterLab
```

You do not need to activate `.venv`. In VS Code, open a notebook, click
**Select Kernel** and choose `.venv`.

## If something goes wrong

- **"needs Python 3.14.7"**: install uv (step 1), then run `python scripts/setup.py` again.
- **".venv uses Python X"**: delete the `.venv` folder and run the setup again.
- **"No module named pandas" in a notebook**: wrong kernel. Start with `python scripts/notebook.py`, or choose `.venv` in VS Code.

## Folders

- `data/raw/` – original data (downloaded by the setup, not in Git)
- `data/processed/` – cleaned data (not in Git)
- `notebooks/` – one cleaning notebook per person
- `scripts/` – setup and start scripts
- `src/` – shared code
- `reports/figures/` – exported figures
