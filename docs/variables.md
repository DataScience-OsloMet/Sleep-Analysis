# Variables in the cleaned datasets

`notebooks/01_cleaning.ipynb` writes two files to `data/processed/`. Both have one row per student
(currently enrolled, age 18-29, n = 1 085), in the same order:

- **`clean_dataset.csv`**: some columns are readable text (YES/NO, Never ... Every Day). Good for tables and figures.
- **`clean_dataset_numeric.csv`**: every column is a number, using the NHIS codes. Use this one for modelling.
  It has the same columns, except `food_security_level`, which is a text copy of `food_security`.

`household_id` is the NHIS `HHX` id and is unique per student. The NHIS special codes
"refused / not ascertained / don't know" (7/8/9, or 97/98/99) are empty values (NaN) in both files.

Codes are taken from the cleaning notebook and the screenshots in `docs/codebook/`.
**Check them against the official NHIS codebook before using them in the report.**

| Column | NHIS variable | Section | `clean_dataset.csv` | `clean_dataset_numeric.csv` |
|---|---|---|---|---|
| `household_id` | HHX | 1.2 | Unique id | Same |
| `age` | AGEP_A | 1.2 | 18-29 | Same |
| `survey_weight` | WTFA_A | 1.3 Work | Population weight. Not a model feature | Same |
| `weekly_work_hours` | EMPWKHRS3_A + EMPWRKLSW1_A | 1.3 Work | Usual weekly hours; 0 if not working last week | Same |
| `sleep_hours_per_night` | SLPHOURS_A | 1.4 Sleep | Hours per 24 h (3-20 in the sample) | Same |
| `past_month_felt_rested` | SLPREST_A | 1.4 Sleep | Never, Some Days, Most days, Every Day | 1 Never, 2 Some days, 3 Most days, 4 Every day |
| `past_month_trouble_falling_asleep` | SLPFLL_A | 1.4 Sleep | Same labels | Same 1-4 codes |
| `past_month_trouble_staying_asleep` | SLPSTY_A | 1.4 Sleep | Same labels | Same 1-4 codes |
| `sex` | SEX_A | 1.4 Sleep | Male, Female | 1 Male, 2 Female |
| `short sleep` | | | 1, 0 | under 7 hours, over 7 hours" |
| `activity_guideline_status` | PA18_02R_A | 1.4 Sleep | Inactive, Insufficiently active, Sufficiently active | 1 Inactive, 2 Insufficiently active, 3 Sufficiently active |
| `anxiety_frequency` | ANXFREQ_A | 1.5 Mental health | 1-5, see `codebook/ANXFREQ_A_explained.png` | Same |
| `depression_frequency` | DEPFREQ_A | 1.5 Mental health | 1-5, see `codebook/DEPFREQ_A_explained.png` | Same |
| `serious_distress` | K6SPD_A | 1.5 Mental health | See `codebook/K6SPD_A_explained.png` | Same |
| `kids_household` | PCNTKIDS_A | 1.5 Mental health | See `codebook/PCNTKIDS_A_explained.png` | Same |
| `education_level` | EDUCP_A | 1.5 Mental health | See `codebook/EDUCP_A_explained.png` | Same |
| `family_income` | RATCAT_A | 1.6 Economy | Income-to-poverty category, 1-14 | Same |
| `food_security` | FDSCAT4_A | 1.6 Economy | 1 High, 2 Marginal, 3 Low, 4 Very low | Same |
| `housing_cost` | HOUSECOST_A | 1.6 Economy | YES, NO | 1 yes, 0 no |
| `high_bloodpressure` | HYPEV_A | 1.6 Health | YES, NO | 1 yes, 0 no |
| `had_asthma` | ASEV_A | 1.6 Health | YES, NO | 1 yes, 0 no |
| `had_arthritis` | ARTHEV_A | 1.6 Health | YES, NO | 1 yes, 0 no |
| `had_diabetes` | DIBEV_A | 1.6 Health | YES, NO | 1 yes, 0 no |
| `food_security_level` | FDSCAT4_A | 1.6 Economy | High, Marginal, Low, Very Low (text copy of `food_security`) | Not included |

## Still to do

- **No target column yet.** `short_sleep` (1 if `sleep_hours_per_night` < 7) is added in #9.
- **Codes not yet checked** against the official NHIS codebook (#11).
