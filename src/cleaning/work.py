"""Age, survey weight and weekly work hours."""

import pandas as pd

from src.sample import load_students, to_missing

RENAME = {
    "AGEP_A": "age",
    "WTFA_A": "survey_weight",
    "EMPWRKLSW1_A": "worked_last_week",
    "EMPWKHRS3_A": "usual_weekly_hours",
}


def clean() -> pd.DataFrame:
    df = load_students(list(RENAME)).rename(columns=RENAME)
    hours = to_missing(df["usual_weekly_hours"], [97, 98, 99])
    hours = hours.mask(df["worked_last_week"] == 2, 0)  # did not work -> 0 hours
    df["weekly_work_hours"] = hours.astype("Int64")
    return df[["age", "survey_weight", "weekly_work_hours"]]
