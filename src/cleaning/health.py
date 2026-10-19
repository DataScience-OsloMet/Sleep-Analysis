"""Chronic conditions and physical activity."""

import pandas as pd

from src.sample import load_students, to_missing

RENAME = {
    "HYPEV_A": "high_blpressure",
    "ASEV_A": "had_asthma",
    "ARTHEV_A": "had_arthritis",
    "DIBEV_A": "had_diabetes",
    "PA18_02R_A": "activityLevelPerGuidelines",
}
CONDITIONS = ["high_blpressure", "had_asthma", "had_arthritis", "had_diabetes"]


def clean() -> pd.DataFrame:
    df = load_students(list(RENAME)).rename(columns=RENAME)
    for column in CONDITIONS:
        df[column] = to_missing(df[column], [7, 8, 9]).map({1: "YES", 2: "NO"})
    df["activityLevelPerGuidelines"] = to_missing(df["activityLevelPerGuidelines"], [8])
    return df
