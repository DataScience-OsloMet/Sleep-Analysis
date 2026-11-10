# Sleep-Analysis

DATA3800 group project (OsloMet, autumn 2026).

**Question:** can we predict which students sleep too little, and how much do weekly work hours contribute?
The data is from one point in time, so it can show that work and sleep go together, not that work causes short sleep.

**Data:** [NHIS 2024 Sample Adult file](https://www.cdc.gov/nchs/nhis/documentation/2024-nhis.html) (CDC),
a US health survey. Sample: currently enrolled students aged 18-29 (1 085 people). One row is one student.

## Get started

1. Install [uv](https://docs.astral.sh/uv/) (once). It fetches the right Python (3.14.7, set in `.python-version`)
   and the exact package versions in `uv.lock` (pandas, scikit-learn, matplotlib, seaborn and others).
2. In the project folder, run:

```bash
uv sync
```

3. Open the project folder in VS Code, open `notebooks/01_cleaning.ipynb`, click
   **Select Kernel** (top right) and choose `.venv`. Run all cells. The first run downloads
   the data from the CDC to `data/raw/` and writes `data/processed/clean_dataset.csv`.

You do not need to activate `.venv` yourself. In the terminal, put `uv run` in front of a command.
To only download the data, run `uv run python -m src.data`.

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

All tasks are on the [project board](https://github.com/orgs/DataScience-OsloMet/projects/1). One card is one task.

1. **Pick a card** in **Klar** and assign yourself. The card moves to **In Progress** by itself.
2. **Make a branch** from the latest `main` (use the card's number in the name):

   ```bash
   git switch main
   git pull
   git switch -c 19-baseline
   ```

3. **Do the work.** Before you push, run **Restart and Run All** so the notebook runs from top to bottom.
4. **Push and open a pull request** on GitHub. Write `Closes #19` in the description, and drag the card to **PR**.
5. **Someone else looks at it and merges.** The card moves to **Done** and the issue closes by itself.

Rules:

- Never push straight to `main`.
- Only one person works in a notebook at a time.
- A card with a red blocked icon waits for another card. Leave it until that one is done.
- Every Monday, move next week's cards that are not blocked from **Backlog** to **Klar**.

In the code:

- Later notebooks read `data/processed/clean_dataset.csv`, never the raw file.
- New or changed variable: edit its section in `01_cleaning.ipynb` and update `docs/variables.md`.
- Save report figures in `reports/figures/` (`from src.config import FIGURES`).

## If something goes wrong

- **"uv: command not found"**: install uv (step 1) and open a new terminal.
- **"No module named pandas" or "No module named src"**: wrong kernel. Click **Select Kernel** and choose `.venv`.
  If `.venv` is not in the list, run `uv sync` again.
- **"CERTIFICATE_VERIFY_FAILED" when downloading**: the code retries with your operating system's
  certificates and then with curl. If it still fails, download
  [adult24csv.zip](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2024/adult24csv.zip)
  in your browser, unzip it and put `adult24.csv` in `data/raw/`.
