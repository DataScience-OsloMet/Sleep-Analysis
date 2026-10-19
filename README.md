# Sleep-Analysis

DATA3800 group project: does working alongside studies affect students' sleep?
Data: NHIS 2024 Sample Adult file (CDC). Sample: enrolled students aged 18-29 (1 085 people).

## Get started

1. Install [uv](https://docs.astral.sh/uv/) (once). It fetches the right Python and packages for you.
2. In the project folder:

```bash
uv sync                          # creates .venv and installs the exact package versions
uv run python -m src.pipeline    # downloads the data (first time) and writes data/processed/merged_dataset.csv
```

3. Open the folder in VS Code (accept the recommended extensions). Open a file in
   `analysis/`; each `# %%` line is a cell, click **Run Cell** above it and pick the
   `.venv` kernel if asked.

No activating of `.venv` is needed. Use `uv run <command>` in the terminal.

## How it fits together

```
data/raw/adult24.csv            downloaded from the CDC (not in Git)
        |
src/sample.py                   the sample: enrolled students aged 18-29, indexed by household id
        |
src/cleaning/<topic>.py         one file per topic: work, sleep, mental_health, demographics, economy, health
        |                       each has clean() -> table with readable column names and NaN for "don't know"
src/pipeline.py                 merges all topics on household_id, checks for duplicates / lost rows
        |
data/processed/merged_dataset.csv
        |
analysis/*.py                   analysis with `# %%` cells, figures go to reports/figures/
```

- **Add or change a variable:** edit the file for its topic in `src/cleaning/`, update
  `docs/variables.md`, run the pipeline again.
- **New topic:** create `src/cleaning/<topic>.py` with a `clean()` function and list it in
  `src/cleaning/__init__.py`.
- **Analysis:** one numbered file per question in `analysis/`, e.g. `02_sleep_by_hours.py`.

## If something goes wrong

- **"uv: command not found"**: install uv (step 1) and reopen the terminal.
- **Certificate error when downloading**: the code retries with your operating system's certificates and then curl. If it still fails, download [adult24csv.zip](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2024/adult24csv.zip), unzip it and put `adult24.csv` in `data/raw/`.
- **"No module named pandas" in VS Code**: wrong kernel. Click **Select Kernel** and choose `.venv`.
- **"No module named src"**: run from the project folder (VS Code setting `jupyter.notebookFileRoot` is already set).

## Folders

- `analysis/` analysis scripts · `src/` pipeline code · `data/` raw and processed data (not in Git)
- `docs/` variable overview and codebook screenshots · `reports/figures/` exported figures
