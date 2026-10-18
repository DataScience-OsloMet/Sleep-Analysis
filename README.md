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
```

## Data

Download the NHIS 2024 Sample Adult CSV from the CDC and place it in `data/raw/`.
The data is not stored in git.

## Structure

- `data/raw/` – original data (not tracked)
- `data/processed/` – cleaned data (not tracked)
- `src/` – reusable code (cleaning, analysis)
- `notebooks/` – EDA and analysis notebooks (one per person to avoid merge conflicts)
- `reports/figures/` – exported figures
