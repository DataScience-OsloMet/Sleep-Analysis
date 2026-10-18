"""Clean Jørgen's NHIS 2024 variables (sample + work hours).

Reads data/raw/adult24.csv and writes data/processed/jorgen_clean.csv.
Run from the project root:  python src/clean_jorgen.py

Variables (NHIS 2024 Sample Adult):
    SCHCURENR_A   currently in school (1 = yes, 2 = no, 7/8/9 = refused/not ascertained/don't know)
    AGEP_A        age (85 = 85+, 97/99 = refused/don't know)
    WTFA_A        survey weight, used for every percentage
    EMPWKHRS3_A   usual hours worked per week (97/98/99 = refused/not ascertained/don't know)
    EMPWRKLSW1_A  worked last week (1 = yes, 2 = no, 9 = don't know)

Output: HHX (merge key), the original columns, and these new columns:
    worker        1 = worked last week, 0 = did not
    hours         hours worked per week (non-workers = 0)
    hours_group   0 = 0 h, 1 = 1-9 h, 2 = 10-19 h, 3 = 20-29 h, 4 = 30+ h
    works_20plus  1 = works 20+ h/week, 0 = less (RQ1)
Percentages must be weighted with WTFA_A (sum the weights, do not count rows).
"""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW_FILE = ROOT / "data" / "raw" / "adult24.csv"
OUT_FILE = ROOT / "data" / "processed" / "jorgen_clean.csv"

ID_COL = "HHX"  # household id, unique per row: the key for merging the team's files
ORIGINAL_COLS = ["SCHCURENR_A", "AGEP_A", "WTFA_A", "EMPWKHRS3_A", "EMPWRKLSW1_A"]
COLUMNS = [ID_COL] + ORIGINAL_COLS

AGE_MIN, AGE_MAX = 18, 29

# Hours-per-week groups as numeric codes, in increasing order of hours.
HOUR_BINS = [-1, 0, 9, 19, 29, float("inf")]
HOUR_GROUPS = {0: "0 h (not working)", 1: "1-9 h", 2: "10-19 h", 3: "20-29 h", 4: "30+ h"}
HOURS_THRESHOLD = 20  # RQ1: works 20+ hours per week


def select_students(df: pd.DataFrame):
    """Keep students aged 18-29. Returns (rows, log)."""
    log = [f"start: {len(df)} respondents"]
    df = df[df["AGEP_A"].between(AGE_MIN, AGE_MAX)]  # also drops age codes 97/99
    log.append(f"age {AGE_MIN}-{AGE_MAX}: {len(df)} rows")
    df = df[df["SCHCURENR_A"] == 1]  # 2 = not a student; 7/8/9 = unknown (dropped)
    log.append(f"currently in school (SCHCURENR_A == 1): {len(df)} rows")
    return df.copy(), log


def clean_work(df: pd.DataFrame):
    """Return the new work columns (same index as df) and a short log."""
    log = []
    status = df["EMPWRKLSW1_A"]
    worker = status.map({1: 1, 2: 0}).astype("Int64")  # 9 = don't know -> missing
    log.append(f"worked last week unknown (code 9) -> missing: {int(worker.isna().sum())} rows")

    # 97/98/99 are not real hours. Blank means "not asked", i.e. did not work.
    hours = df["EMPWKHRS3_A"].where(~df["EMPWKHRS3_A"].isin([97, 98, 99]))
    bad_codes = int(df["EMPWKHRS3_A"].isin([97, 98, 99]).sum())
    log.append(f"hours codes 97/98/99 -> missing: {bad_codes} rows")
    hours = hours.mask(worker == 0, 0)
    log.append(f"non-workers set to 0 hours: {int((worker == 0).sum())} rows")
    log.append(f"workers without valid hours (missing): {int(((worker == 1) & hours.isna()).sum())} rows")
    log.append(f"max hours: {hours.max():.0f}")

    new = pd.DataFrame(index=df.index)
    new["worker"] = worker
    new["hours"] = hours.astype("Int64")
    new["hours_group"] = pd.cut(hours, bins=HOUR_BINS, labels=False).astype("Int64")
    new["works_20plus"] = (hours >= HOURS_THRESHOLD).astype("Int64").where(hours.notna())
    return new, log


def main():
    raw = pd.read_csv(RAW_FILE, usecols=COLUMNS, low_memory=False)
    students, sample_log = select_students(raw)
    work, work_log = clean_work(students)
    df = pd.concat([students, work], axis=1)

    print("Sample:")
    for line in sample_log:
        print(f"  {line}")
    print("Work variables:")
    for line in work_log:
        print(f"  {line}")
    print(f"{ID_COL} unique: {df[ID_COL].is_unique}")

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_FILE, index=False)
    print(f"\nSaved {len(df)} rows to {OUT_FILE.relative_to(ROOT)}")

    print("\nHours groups (count, weighted %):")
    total = df["WTFA_A"].sum()
    for code, label in HOUR_GROUPS.items():
        m = df["hours_group"] == code
        print(f"  {code} = {label:<18} {int(m.sum()):>4}  {df.loc[m, 'WTFA_A'].sum() / total:6.1%}")
    m = df["works_20plus"] == 1
    print(f"Works 20+ h: {int(m.sum())} of {len(df)}, weighted {df.loc[m, 'WTFA_A'].sum() / total:.1%}")


if __name__ == "__main__":
    main()
