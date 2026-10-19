"""Income, food security, housing cost and chronic conditions."""

import pandas as pd

from src.sample import load_students, to_missing

RENAME = {
    "RATCAT_A": "family_income",
    "FDSCAT4_A": "food_security",
    "HOUSECOST_A": "housing_cost",
    "HYPEV_A": "high_blpressure",
    "ASEV_A": "had_asthma",
    "ARTHEV_A": "had_arthritis",
    "DIBEV_A": "had_diabetes",
}
YES_NO = ["housing_cost", "high_blpressure", "had_asthma", "had_arthritis", "had_diabetes"]
FOOD_SECURITY = {1: "High", 2: "Marginal", 3: "Low", 4: "Very Low"}


def clean() -> pd.DataFrame:
    df = load_students(list(RENAME)).rename(columns=RENAME)
    for column in ["food_security", *YES_NO]:
        df[column] = to_missing(df[column], [7, 8, 9])
    for column in YES_NO:
        df[column] = df[column].map({1: "YES", 2: "NO"})
    df["food_security_level"] = df["food_security"].map(FOOD_SECURITY)
    return df
