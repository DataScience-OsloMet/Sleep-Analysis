"""Sex, education and children in the household."""

import pandas as pd

from src.sample import load_students, to_missing

RENAME = {
    "SEX_A": "gender",
    "EDUCP_A": "education_level",
    "PCNTKIDS_A": "kids_household",
}


def clean() -> pd.DataFrame:
    df = load_students(list(RENAME)).rename(columns=RENAME)
    df["gender"] = to_missing(df["gender"], [7, 9])
    df["education_level"] = to_missing(df["education_level"], [97, 98, 99])
    df["kids_household"] = to_missing(df["kids_household"], [7, 8, 9])
    return df
