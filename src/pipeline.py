"""Clean every person's variables and merge them into data/processed/merged_dataset.csv.

Run from the project folder:  python -m src.pipeline
"""

import pandas as pd

from src.cleaning import CLEANERS
from src.config import PROCESSED
from src.sample import ID_COLUMN

OUT_FILE = PROCESSED / "merged_dataset.csv"


def build() -> pd.DataFrame:
    parts = {}
    for name, clean in CLEANERS.items():
        parts[name] = clean()
        print(f"{name}: {parts[name].shape[0]} rows, {parts[name].shape[1]} columns")

    sizes = {name: len(df) for name, df in parts.items()}
    if len(set(sizes.values())) != 1:
        raise ValueError(f"Cleaners returned different numbers of rows: {sizes}")

    seen = {}
    for name, df in parts.items():
        if not df.index.is_unique:
            raise ValueError(f"{name}: {ID_COLUMN} is not unique")
        for column in df.columns:
            if column in seen:
                raise ValueError(f"Column '{column}' is in both {seen[column]} and {name}. Rename one.")
            seen[column] = name

    merged = pd.concat(parts.values(), axis=1, join="inner", verify_integrity=False)
    if len(merged) != sizes["work"]:
        raise ValueError("Respondents differ between cleaners, merge lost rows")
    return merged.reset_index().rename(columns={ID_COLUMN: "household_id"})


def main():
    merged = build()
    PROCESSED.mkdir(parents=True, exist_ok=True)
    merged.to_csv(OUT_FILE, index=False)
    print(f"\nWrote {OUT_FILE}: {merged.shape[0]} rows, {merged.shape[1]} columns")
    missing = merged.isna().sum()
    print("Missing values per column:")
    print(missing[missing > 0].to_string() or "  none")


if __name__ == "__main__":
    main()
