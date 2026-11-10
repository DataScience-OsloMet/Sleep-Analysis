# Variables in `clean_dataset.csv`

One row per student (currently enrolled, age 18-29, n = 1 085), made by
`notebooks/01_cleaning.ipynb`. `household_id` is the NHIS `HHX` id and is unique per student.
The NHIS special codes "refused / not ascertained / don't know" (7/8/9, or 97/98/99)
are empty values (NaN).

Codes are taken from the cleaning notebook and the screenshots in `docs/codebook/`.
**Check them against the official NHIS codebook before using them in the report.**

| Column | NHIS variable | Section | Values |
|---|---|---|---|
| `household_id` | HHX | 1.2 | Unique id |
| `age` | AGEP_A | 1.2 | 18-29 |
| `survey_weight` | WTFA_A | 1.3 Work | Use for population estimates, not as a model feature |
| `weekly_work_hours` | EMPWKHRS3_A + EMPWRKLSW1_A | 1.3 Work | Usual weekly hours; 0 if not working last week |
| `nightly_sleep` | SLPHOURS_A | 1.4 Sleep | Hours per 24 h (3-20 in the sample) |
| `monthly_fullyRested` | SLPREST_A | 1.4 Sleep | Text: Never, Some Days, Most days, Every Day |
| `monthly_troubleSleeping` | SLPFLL_A | 1.4 Sleep | Trouble falling asleep, same labels |
| `monthly_troubleStayingAsleep` | SLPSTY_A | 1.4 Sleep | Same labels |
| `gender` | SEX_A | 1.4 Sleep | Text: Male, Female |
| `activityLevelPerGuidelines` | PA18_02R_A | 1.4 Sleep | Text: Inactive, Insufficiently active, Sufficiently active |
| `anxiety_frequency` | ANXFREQ_A | 1.5 Mental health | 1-5, see `codebook/ANXFREQ_A_explained.png` |
| `depression_frequency` | DEPFREQ_A | 1.5 Mental health | 1-5, see `codebook/DEPFREQ_A_explained.png` |
| `serious_distress` | K6SPD_A | 1.5 Mental health | See `codebook/K6SPD_A_explained.png` |
| `kids_household` | PCNTKIDS_A | 1.5 Mental health | See `codebook/PCNTKIDS_A_explained.png` |
| `education_level` | EDUCP_A | 1.5 Mental health | See `codebook/EDUCP_A_explained.png` |
| `family_income` | RATCAT_A | 1.6 Economy | Income-to-poverty category, 1-14 |
| `food_security` | FDSCAT4_A | 1.6 Economy | 1 High, 2 Marginal, 3 Low, 4 Very low |
| `housing_cost` | HOUSECOST_A | 1.6 Economy | Text: YES, NO |
| `high_blpressure` | HYPEV_A | 1.6 Health | Text: YES, NO |
| `had_asthma` | ASEV_A | 1.6 Health | Text: YES, NO |
| `had_arthritis` | ARTHEV_A | 1.6 Health | Text: YES, NO |
| `had_diabetes` | DIBEV_A | 1.6 Health | Text: YES, NO |
| `food_security_level` | FDSCAT4_A | 1.6 Economy | Text copy of `food_security` |

## Open questions for the group

- **Text or numbers?** Some columns are text (YES/NO, Never ... Every Day), others are number codes.
  Models need numbers, so the text columns must be encoded before modelling, or changed to numbers here.
- **Column names** mix `snake_case` and `camelCase` (`monthly_fullyRested`).
- **No target column yet.** For classification, add for example `short_sleep = nightly_sleep < 7`.
