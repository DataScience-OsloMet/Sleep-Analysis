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

Download the **NHIS 2024 Sample Adult CSV** from the
[CDC NHIS 2024 website](https://www.cdc.gov/nchs/nhis/2024-nhis.html).

Place the downloaded file at:

```text
data/raw/adult24.csv
```

On Windows PowerShell, verify that the file is available before running the
notebooks:

```powershell
if (-not (Test-Path data/raw/adult24.csv)) {
    Write-Error "Missing data/raw/adult24.csv. Download the NHIS 2024 Sample Adult CSV first."
}
```

The original and processed data files are not stored in Git. Each contributor
must download the original dataset locally.

## Structure

- `data/raw/` – original data (not tracked)
- `data/processed/` – cleaned data (not tracked)
- `src/` – reusable code (cleaning, analysis)
- `notebooks/` – EDA and analysis notebooks (one per person to avoid merge conflicts)
- `reports/figures/` – exported figures
