"""
Combined data cleaning for NHIS adult24.csv.

Sample: students (SCHCURENR_A == 1) aged 18-29.

Writes one CSV per person (same files as the original notebooks) plus
combined_clean.csv with every cleaned column side by side, one row per person.

Run from the project folder or from notebooks/:
    python clean_all.py
"""

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path.cwd() if (Path.cwd() / "data").exists() else Path.cwd().parent
RAW_PATH = ROOT / "data" / "raw" / "adult24.csv"
OUT_DIR = ROOT / "data" / "processed"

NA_VALUES = ["", " ", "-", "..", ":", "ukjent", "unknown"]


# ---------------------------------------------------------------------------
# Load and select the sample (done once for everyone)
# ---------------------------------------------------------------------------
def load_students() -> pd.DataFrame:
    df = pd.read_csv(RAW_PATH, na_values=NA_VALUES)

    by_age = df[df["AGEP_A"].between(18, 29)]  # also drops age codes 97/99
    unknown_school = by_age["SCHCURENR_A"].isin([7, 8, 9]).sum()
    students = by_age[by_age["SCHCURENR_A"] == 1].reset_index(drop=True)

    print(f"After age filter:          {len(by_age)}")
    print(f"Unknown school status:     {unknown_school} (left out)")
    print(f"Students 18-29:            {len(students)}")
    return students


# ---------------------------------------------------------------------------
# Unknown codes -> NaN (done once for every variable)
# ---------------------------------------------------------------------------
# 7 = Refused, 8 = Not ascertained, 9 = Don't know
UNKNOWN_7_9 = [
    "PA18_02R_A", "SEX_A", "SLPSTY_A", "SLPFLL_A", "SLPREST_A",    # Kristine
    "ANXFREQ_A", "DEPFREQ_A", "K6SPD_A", "PCNTKIDS_A",             # Endre
    "FDSCAT4_A", "HOUSECOST_A", "HYPEV_A", "ASEV_A", "ARTHEV_A", "DIBEV_A",  # Lykke
]

# 97 = Refused, 98 = Not ascertained, 99 = Don't know
UNKNOWN_97_99 = [
    "SLPHOURS_A",   # Kristine
    "EDUCP_A",      # Endre
    "EMPWKHRS3_A",  # Jørgen
]


def set_unknowns_to_nan(students: pd.DataFrame) -> pd.DataFrame:
    students = students.copy()
    students[UNKNOWN_7_9] = students[UNKNOWN_7_9].replace({7: np.nan, 8: np.nan, 9: np.nan})
    students[UNKNOWN_97_99] = students[UNKNOWN_97_99].replace({97: np.nan, 98: np.nan, 99: np.nan})
    return students


# ---------------------------------------------------------------------------
# Jørgen: weekly work hours
# ---------------------------------------------------------------------------
def clean_jorgen(students: pd.DataFrame) -> pd.DataFrame:
    out = pd.DataFrame({
        "household_id": students["HHX"],
        "age": students["AGEP_A"],
        "survey_weight": students["WTFA_A"],
    })

    hours = students["EMPWKHRS3_A"]
    hours = hours.mask(students["EMPWRKLSW1_A"] == 2, 0)  # did not work -> 0 hours
    out["weekly_work_hours"] = hours.astype("Int64")
    return out


# ---------------------------------------------------------------------------
# Kristine: sleep, sex, physical activity
# ---------------------------------------------------------------------------
def clean_kristine(students: pd.DataFrame) -> pd.DataFrame:
    out = students[
        ["PA18_02R_A", "SEX_A", "SLPSTY_A", "SLPFLL_A", "SLPREST_A", "SLPHOURS_A"]
    ].copy()

    sleep_freq = ["SLPSTY_A", "SLPFLL_A", "SLPREST_A"]

    out["PA18_02R_A"] = out["PA18_02R_A"].replace(
        {1: "Inactive", 2: "Insufficiently active", 3: "Sufficiently active"}
    )
    out["SEX_A"] = out["SEX_A"].replace({1: "Male", 2: "Female"})
    out[sleep_freq] = out[sleep_freq].replace(
        {1: "Never", 2: "Some Days", 3: "Most days", 4: "Every Day"}
    )

    return out.rename(columns={
        "PA18_02R_A": "activityLevelPerGuidelines",
        "SEX_A": "gender",
        "SLPSTY_A": "monthly_troubleStayingAsleep",
        "SLPFLL_A": "monthly_troubleSleeping",
        "SLPREST_A": "monthly_fullyRested",
        "SLPHOURS_A": "nightly_sleep",
    })


# ---------------------------------------------------------------------------
# Endre: anxiety, depression, distress, kids, education
# ---------------------------------------------------------------------------
def clean_endre(students: pd.DataFrame) -> pd.DataFrame:
    out = students[["ANXFREQ_A", "DEPFREQ_A", "K6SPD_A", "PCNTKIDS_A", "EDUCP_A"]].copy()

    return out.rename(columns={
        "ANXFREQ_A": "anxiety_frequency",
        "DEPFREQ_A": "depression_frequency",
        "K6SPD_A": "serious_distress",
        "PCNTKIDS_A": "kids_household",
        "EDUCP_A": "education_level",
    })


# ---------------------------------------------------------------------------
# Lykke: income, food security, housing cost, chronic conditions
# ---------------------------------------------------------------------------
FOOD_SECURITY_LABELS = {1: "High", 2: "Marginal", 3: "Low", 4: "Very Low"}


def clean_lykke(students: pd.DataFrame) -> pd.DataFrame:
    out = students[
        ["RATCAT_A", "FDSCAT4_A", "HOUSECOST_A", "HYPEV_A", "ASEV_A", "ARTHEV_A", "DIBEV_A"]
    ].copy()

    yes_no = ["HOUSECOST_A", "HYPEV_A", "ASEV_A", "ARTHEV_A", "DIBEV_A"]

    out[yes_no] = out[yes_no].replace({1: "YES", 2: "NO"})

    out = out.rename(columns={
        "RATCAT_A": "family_income",
        "FDSCAT4_A": "food_security",
        "HOUSECOST_A": "housing_cost",
        "HYPEV_A": "high_blpressure",
        "ASEV_A": "had_asthma",
        "ARTHEV_A": "had_arthritis",
        "DIBEV_A": "had_diabetes",
    })
    out["food_security_level"] = out["food_security"].map(FOOD_SECURITY_LABELS)
    return out


# ---------------------------------------------------------------------------
# Run everything
# ---------------------------------------------------------------------------
def save(df: pd.DataFrame, name: str) -> None:
    path = OUT_DIR / name
    df.to_csv(path, index=False)
    print(f"Saved {df.shape} -> {path}")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    students = set_unknowns_to_nan(load_students())

    parts = {
        "jorgen_clean.csv": clean_jorgen(students),
        "kristines_processed.csv": clean_kristine(students),
        "endre_clean.csv": clean_endre(students),
        "lykke_clean.csv": clean_lykke(students),
    }

    print()
    for name, part in parts.items():
        save(part, name)

    # All parts share the same rows in the same order, so they line up side by side.
    combined = pd.concat(parts.values(), axis=1)
    save(combined, "combined_clean.csv")

    print("\nMissing values in combined data:")
    print(combined.isna().sum().to_string())
    assert combined["household_id"].is_unique, "household_id should be unique"


if __name__ == "__main__":
    main()
