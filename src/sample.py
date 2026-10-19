"""The study sample: students aged 18-29 from the NHIS 2024 Sample Adult file."""

from functools import cache

import pandas as pd

from src.data import load_nhis

ID_COLUMN = "HHX"  # NHIS household id, unique per respondent


@cache
def _students() -> pd.DataFrame:
    raw = load_nhis()
    enrolled = raw["SCHCURENR_A"] == 1
    return raw[enrolled & raw["AGEP_A"].between(18, 29)].set_index(ID_COLUMN)


def load_students(columns: list[str]) -> pd.DataFrame:
    """Return the sample (currently enrolled, age 18-29) with only the given NHIS columns.

    The table is indexed by household id, so each topic's cleaned table can be
    joined on it instead of on row order.
    """
    return _students()[columns].copy()


def to_missing(series: pd.Series, codes) -> pd.Series:
    """Replace NHIS 'refused / don't know / not ascertained' codes with NaN."""
    return series.mask(series.isin(codes))
