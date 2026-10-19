"""Combine all processed datasets into one dataset."""

from pathlib import Path

import pandas as pd

from src.config import PROCESSED


OUTPUT_PATH = PROCESSED / "combined_dataset.csv"


def combine_processed_datasets(
    input_dir: Path = PROCESSED,
    output_path: Path = OUTPUT_PATH,
) -> pd.DataFrame:
    """Combine processed CSV files side by side, keeping one row per respondent."""
    input_paths = sorted(
        path
        for path in input_dir.glob("*.csv")
        if path.resolve() != output_path.resolve()
    )
    if not input_paths:
        raise FileNotFoundError(f"No processed CSV files found in {input_dir}")

    datasets = [pd.read_csv(path) for path in input_paths]
    row_counts = {path.name: len(dataset) for path, dataset in zip(input_paths, datasets)}
    if len(set(row_counts.values())) != 1:
        details = ", ".join(f"{name}: {count} rows" for name, count in row_counts.items())
        raise ValueError(
            "Processed datasets must have the same number of rows before they "
            f"can be combined: {details}"
        )

    combined = pd.concat(datasets, axis=1)
    duplicate_columns = combined.columns[combined.columns.duplicated()].tolist()
    if duplicate_columns:
        raise ValueError(
            "Processed datasets contain duplicate column names: "
            + ", ".join(duplicate_columns)
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(output_path, index=False)
    print(f"Combined {len(input_paths)} datasets into {output_path} ({combined.shape})")
    return combined


if __name__ == "__main__":
    combine_processed_datasets()
