# Sleep-Analysis

## Setup

The project uses **Python 3.14.7**, recorded in `.python-version`. `.venv/` is
created locally by each contributor and is not checked into Git.

### Recommended: uv (picks the right Python automatically)

[uv](https://docs.astral.sh/uv/) reads `.python-version`, downloads exactly
Python 3.14.7 if it is missing, and creates `.venv` with it.

```bash
uv venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# Windows (Git Bash):    source .venv/Scripts/activate
# macOS/Linux:           source .venv/bin/activate
uv pip install -r requirements.txt
python scripts/download_data.py
```

### Without uv

```bash
# Windows (PowerShell): use the Python launcher to select the required version
py -3.14 -m venv .venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# Windows (Git Bash):    source .venv/Scripts/activate
# macOS/Linux:           source .venv/bin/activate
python scripts/check_python.py  # stops with an error unless Python is exactly 3.14.7
python -m pip install -r requirements.txt
python scripts/download_data.py
```

If `python scripts/check_python.py` reports an error, remove `.venv`, install Python
3.14.7, and run the setup commands again. With `pyenv`, the `.python-version`
file selects the version automatically before creating `.venv`.

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
