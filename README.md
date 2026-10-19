# Sleep-Analysis

DATA3800 group project: does working alongside studies affect students' sleep?
Data: NHIS 2024 Sample Adult file (CDC).

## Get started

1. Install [uv](https://docs.astral.sh/uv/) (once). It fetches the right Python (3.14.7) for you.
2. In the project folder, run once:

```bash
python scripts/setup.py      # creates .venv, installs packages, downloads the data
```

3. Build the dataset:

```bash
python scripts/run_all.py   # writes data/processed/merged_dataset.csv
```

You do not need to activate `.venv` yourself.

4. Analysis: open a file in `analysis/` in VS Code. Each `# %%` line starts a
cell; click **Run Cell** above it (choose the `.venv` kernel when asked). The
files are plain `.py`, so Git diffs are readable and nobody gets merge conflicts
in notebook JSON.

## How the cleaning works

Each person owns one file in `src/cleaning/` (`jorgen.py`, `kristine.py`,
`endre.py`, `lykke.py`) with a `clean()` function. All of them start from the
same sample (`src/sample.py`: enrolled students aged 18-29) and return a table
indexed by `household_id`. `src/pipeline.py` merges them on `household_id`
(not on row order) and stops with a clear error on duplicate columns or
mismatched respondents. To add a variable, edit your own file and re-run.
Put analysis and plots in `analysis/` (one numbered file per topic).

## If something goes wrong

- **"needs Python 3.14.7"**: install uv (step 1), then run `python scripts/setup.py` again.
- **".venv uses Python X"**: delete the `.venv` folder and run the setup again.
- **"CERTIFICATE_VERIFY_FAILED" when downloading the data**: update the project (`git pull`) and run `python scripts/setup.py` again, it retries automatically. If it still fails, download [adult24csv.zip](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2024/adult24csv.zip) in your browser, unzip it, put `adult24.csv` in `data/raw/`, and run the setup again.
- **"No module named pandas" in a notebook**: wrong kernel. Click **Select Kernel** and choose `.venv`.

## Folders

- `data/raw/` – original data (downloaded by the setup, not in Git)
- `data/processed/` – cleaned data and the combined dataset (not in Git)
- `notebooks/` – one cleaning notebook per person
- `scripts/` – setup, run-all and merge scripts
- `src/` – shared code
- `reports/figures/` – exported figures
