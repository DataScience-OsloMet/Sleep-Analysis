# Sleep-Analysis

DATA3800 group project: does working alongside studies affect students' sleep?
Data: NHIS 2024 Sample Adult file (CDC). Sample: currently enrolled students aged 18-29 (1 085 people).

## Get started

1. Install [uv](https://docs.astral.sh/uv/) (once). It fetches the right Python (3.14) and packages for you.
2. In the project folder, run:

```bash
uv sync
```

3. Open the project folder in VS Code, open `notebooks/01_cleaning.ipynb`, click
   **Select Kernel** (top right) and choose `.venv`. Run all cells. The first run downloads
   the data from the CDC to `data/raw/` and writes `data/processed/clean_dataset.csv`.

You do not need to activate `.venv` yourself. In the terminal, put `uv run` in front of a command.

## Run everything

Runs every notebook from top to bottom, in order, and saves the outputs in the notebooks:

```bash
uv run jupyter nbconvert --to notebook --execute --inplace notebooks/*.ipynb
```

## Folders

```
notebooks/          the analysis, one notebook per step, run in number order
  01_cleaning         raw NHIS file -> data/processed/clean_dataset.csv
  02_eda              (next) exploratory analysis and figures
  03_modelling        (next) baseline and models
  04_agent            (next) the GenAI component
src/                shared code: paths (config.py) and downloading the data (data.py)
data/raw/           the NHIS file, downloaded automatically (not in Git)
data/processed/     clean_dataset.csv (not in Git, made by 01_cleaning)
docs/               variables.md (every column and its codes) and codebook screenshots
reports/figures/    figures for the report
```

## How we work

- **`main` always runs.** Work on your own branch and merge through a pull request.
- **One notebook, one owner at a time.** Two people editing the same notebook gives conflicts
  that are hard to fix.
- **Restart and Run All before you push**, so the notebook is known to run from top to bottom.
- **Add or change a variable:** edit its section in `01_cleaning.ipynb`, update
  `docs/variables.md`, and run the notebook again.
- **Later notebooks** start with `pd.read_csv(PROCESSED / "clean_dataset.csv")` and never read the raw file.
- Save figures for the report with `fig.savefig(FIGURES / "name.png", dpi=200)` (`from src.config import FIGURES`).

## If something goes wrong

- **"uv: command not found"**: install uv (step 1) and open a new terminal.
- **"No module named pandas" or "No module named src"**: wrong kernel. Click **Select Kernel** and choose `.venv`.
  If `.venv` is not in the list, run `uv sync` again.
- **"CERTIFICATE_VERIFY_FAILED" when downloading**: the code retries with your operating system's
  certificates and then with curl. If it still fails, download
  [adult24csv.zip](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2024/adult24csv.zip)
  in your browser, unzip it and put `adult24.csv` in `data/raw/`.
