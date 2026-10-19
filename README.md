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

## Run everything

To run all notebooks and then combine everyone's files into one dataset:

```bash
python scripts/run_all.py   # writes data/processed/merged_dataset.csv
```

## If something goes wrong

- **"needs Python 3.14.7"**: install uv (step 1), then run `python scripts/setup.py` again.
- **".venv uses Python X"**: delete the `.venv` folder and run the setup again.
- **"No module named pandas" in a notebook**: wrong kernel. Click **Select Kernel** and choose `.venv`.

## Folders

- `data/raw/` – original data (downloaded by the setup, not in Git)
- `data/processed/` – cleaned data and the combined dataset (not in Git)
- `notebooks/` – one cleaning notebook per person
- `scripts/` – setup, run-all and merge scripts
- `src/` – shared code
- `reports/figures/` – exported figures

After the cleaning notebooks have generated their processed CSV files, run:

```bash
python -m src.merge_dataset
```

This creates `data/processed/combined_dataset.csv` by combining the processed
files side by side, so each row remains one respondent. The input files must
contain the same respondents in the same order and have unique column names.
