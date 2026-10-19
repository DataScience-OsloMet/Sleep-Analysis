# Sleep-Analysis

DATA3800 group project: does working alongside studies affect students' sleep?
Data: NHIS 2024 Sample Adult file (CDC).

## Get started

1. Install [uv](https://docs.astral.sh/uv/) (once). It fetches the right Python (3.14.7) for you.
2. In the project folder, run once:

```bash
python scripts/setup.py      # creates .venv, installs packages, downloads the data
```

3. Open the project folder in VS Code, open a notebook in `notebooks/`, click
   **Select Kernel** (top right) and choose `.venv`.

You do not need to activate `.venv` yourself.

## If something goes wrong

- **"needs Python 3.14.7"**: install uv (step 1), then run `python scripts/setup.py` again.
- **".venv uses Python X"**: delete the `.venv` folder and run the setup again.
- **"No module named pandas" in a notebook**: wrong kernel. Click **Select Kernel** and choose `.venv`.

## Folders

- `data/raw/` – original data (downloaded by the setup, not in Git)
- `data/processed/` – cleaned data (not in Git)
- `notebooks/` – one cleaning notebook per person
- `scripts/` – setup script
- `src/` – shared code
- `reports/figures/` – exported figures
