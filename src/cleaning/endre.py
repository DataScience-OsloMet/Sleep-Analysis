"""Mental health and background: anxiety, depression, distress, kids, education."""

import pandas as pd

from src.sample import load_students, to_missing

RENAME = {
    "ANXFREQ_A": "anxiety_frequency",
    "DEPFREQ_A": "depression_frequency",
    "K6SPD_A": "serious_distress",
    "PCNTKIDS_A": "kids_household",
    "EDUCP_A": "education_level",
}


def clean() -> pd.DataFrame:
    df = load_students(list(RENAME)).rename(columns=RENAME)
    for column in ["anxiety_frequency", "depression_frequency", "serious_distress", "kids_household"]:
        df[column] = to_missing(df[column], [7, 8, 9])
    df["education_level"] = to_missing(df["education_level"], [97, 98, 99])
    return df
