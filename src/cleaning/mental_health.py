"""Anxiety, depression and psychological distress."""

import pandas as pd

from src.sample import load_students, to_missing

RENAME = {
    "ANXFREQ_A": "anxiety_frequency",
    "DEPFREQ_A": "depression_frequency",
    "K6SPD_A": "serious_distress",
}


def clean() -> pd.DataFrame:
    df = load_students(list(RENAME)).rename(columns=RENAME)
    for column in df.columns:
        df[column] = to_missing(df[column], [7, 8, 9])
    return df
