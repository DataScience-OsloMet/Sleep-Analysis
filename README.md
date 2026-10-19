# Sleep-Analysis

DATA3800 – Mandatory assignment 2. How is sleep deprivation related to lifestyle choices?
Data: NHIS 2024 Sample Adult file (CDC).

## Setup

```bash
python -m venv .venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# Windows (Git Bash):    source .venv/Scripts/activate
# macOS/Linux:           source .venv/bin/activate
pip install -r requirements.txt
python scripts/download_data.py
```

## Data

The setup command downloads the **NHIS 2024 Sample Adult CSV** automatically
from the [CDC NHIS 2024 website](https://www.cdc.gov/nchs/nhis/2024-nhis.html)
and extracts it to `data/raw/adult24.csv`. If the file already exists, it is
not downloaded again.

The original and processed data files are not stored in Git. Each contributor
gets the original dataset locally by running the setup command.

## Structure

- `data/raw/` – original data (not tracked)
- `data/processed/` – cleaned data (not tracked)
- `src/` – reusable code (cleaning, analysis)
- `notebooks/` – EDA and analysis notebooks (one per person to avoid merge conflicts)
- `reports/figures/` – exported figures
