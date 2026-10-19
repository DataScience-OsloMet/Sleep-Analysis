"""Sleep outcomes: hours per night and how often rested / trouble sleeping."""

import pandas as pd

from src.sample import load_students, to_missing

RENAME = {
    "SLPHOURS_A": "nightly_sleep",
    "SLPREST_A": "monthly_fullyRested",
    "SLPFLL_A": "monthly_troubleSleeping",
    "SLPSTY_A": "monthly_troubleStayingAsleep",
}


def clean() -> pd.DataFrame:
    df = load_students(list(RENAME)).rename(columns=RENAME)
    df["nightly_sleep"] = to_missing(df["nightly_sleep"], [97, 98, 99])
    for column in ["monthly_fullyRested", "monthly_troubleSleeping", "monthly_troubleStayingAsleep"]:
        df[column] = to_missing(df[column], [7, 8, 9])
    return df
