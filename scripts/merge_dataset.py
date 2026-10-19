"""Combine everyone's cleaned files into one dataset: data/processed/merged_dataset.csv

Run after the cleaning notebooks:  python scripts/merge_dataset.py

The files are put side by side, row by row. This only works if every file
contains the same students in the same order, so the script stops if the row
counts differ or if a column name appears in more than one file.
"""

import sys
from pathlib import Path

import pandas as pd

PROCESSED = Path(__file__).resolve().parents[1] / "data" / "processed"
FILES = [
    "jorgen_clean.csv",
    "kristines_processed.csv",
    "endre_clean.csv",
    "lykke_clean.csv",
]
OUT_FILE = PROCESSED / "merged_dataset.csv"


def main():
    missing = [name for name in FILES if not (PROCESSED / name).exists()]
    if missing:
        sys.exit(f"ERROR: missing files in data/processed: {', '.join(missing)}\nRun the cleaning notebooks first.")

    parts = {name: pd.read_csv(PROCESSED / name, low_memory=False) for name in FILES}

    rows = {name: len(df) for name, df in parts.items()}
    if len(set(rows.values())) != 1:
        sys.exit(f"ERROR: the files have different numbers of rows: {rows}")

    seen = {}
    for name, df in parts.items():
        for column in df.columns:
            if column in seen:
                sys.exit(f"ERROR: column '{column}' is in both {seen[column]} and {name}. Rename one of them.")
            seen[column] = name

    merged = pd.concat(parts.values(), axis=1)
    merged.to_csv(OUT_FILE, index=False)

    print(f"Merged {len(FILES)} files into {OUT_FILE.name}: {merged.shape[0]} rows, {merged.shape[1]} columns")
    missing_values = merged.isna().sum()
    print("Missing values per column (only columns with any):")
    print(missing_values[missing_values > 0].to_string() or "  none")


if __name__ == "__main__":
    main()
