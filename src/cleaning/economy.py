"""Income, food security and housing cost."""

import pandas as pd

from src.sample import load_students, to_missing

RENAME = {
    "RATCAT_A": "family_income",
    "FDSCAT4_A": "food_security",
    "HOUSECOST_A": "housing_cost",
}
FOOD_SECURITY = {1: "High", 2: "Marginal", 3: "Low", 4: "Very Low"}


def clean() -> pd.DataFrame:
    df = load_students(list(RENAME)).rename(columns=RENAME)
    df["food_security"] = to_missing(df["food_security"], [7, 8, 9])
    df["food_security_level"] = df["food_security"].map(FOOD_SECURITY)
    df["housing_cost"] = to_missing(df["housing_cost"], [7, 8, 9]).map({1: "YES", 2: "NO"})
    return df
