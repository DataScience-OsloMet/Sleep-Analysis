"""The study sample: students aged 18-29 from the NHIS 2024 Sample Adult file."""

import pandas as pd

from src.config import NHIS_FILE
from src.data import download_nhis

ID_COLUMN = "HHX"  # NHIS household id, unique per respondent in this sample


def load_students(columns: list[str]) -> pd.DataFrame:
    """Return the sample (currently enrolled, age 18-29) with only the given NHIS columns.

    The id column is always included and kept as the index, so every person's
    cleaned table can later be joined on it instead of on row order.
    """
    download_nhis()
    wanted = list(dict.fromkeys([ID_COLUMN, "AGEP_A", "SCHCURENR_A", *columns]))
    raw = pd.read_csv(NHIS_FILE, usecols=wanted, low_memory=False)
    students = raw[(raw["SCHCURENR_A"] == 1) & raw["AGEP_A"].between(18, 29)]
    keep = [c for c in wanted if c != "SCHCURENR_A" and (c != "AGEP_A" or "AGEP_A" in columns)]
    return students[keep].set_index(ID_COLUMN)


def to_missing(series: pd.Series, codes) -> pd.Series:
    """Replace NHIS 'refused / don't know / not ascertained' codes with NaN."""
    return series.mask(series.isin(codes))
