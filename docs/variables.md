# Variables in `merged_dataset.csv`

One row per student (enrolled, age 18-29, n = 1 085). `household_id` is the NHIS
`HHX` id. The NHIS special codes "refused / don't know / not ascertained"
(7/8/9, or 97/98/99) are turned into empty values in every module.

Codes below are taken from our cleaning code and the screenshots in
`docs/codebook/`. **Check them against the official NHIS codebook before using
them in the report.**

| Column | NHIS variable | Topic (module) | Notes |
|---|---|---|---|
| `household_id` | HHX | all | Unique id, used for merging |
| `age` | AGEP_A | work | 18-29 |
| `survey_weight` | WTFA_A | work | Use for population estimates |
| `weekly_work_hours` | EMPWKHRS3_A + EMPWRKLSW1_A | work | Usual weekly hours; 0 if not working last week |
| `nightly_sleep` | SLPHOURS_A | sleep | Hours per 24 h (3-20 in the sample) |
| `monthly_fullyRested` | SLPREST_A | sleep | 1 Never, 2 Some days, 3 Most days, 4 Every day |
| `monthly_troubleSleeping` | SLPFLL_A | sleep | Trouble falling asleep, same 1-4 scale |
| `monthly_troubleStayingAsleep` | SLPSTY_A | sleep | Same 1-4 scale |
| `anxiety_frequency` | ANXFREQ_A | mental_health | See `docs/codebook/ANXFREQ_A_explained.png` |
| `depression_frequency` | DEPFREQ_A | mental_health | See `docs/codebook/DEPFREQ_A_explained.png` |
| `serious_distress` | K6SPD_A | mental_health | See `docs/codebook/K6SPD_A_explained.png` |
| `gender` | SEX_A | demographics | 1 Male, 2 Female |
| `education_level` | EDUCP_A | demographics | See `docs/codebook/EDUCP_A_explained.png` |
| `kids_household` | PCNTKIDS_A | demographics | See `docs/codebook/PCNTKIDS_A_explained.png` |
| `family_income` | RATCAT_A | economy | Income-to-poverty category |
| `food_security` | FDSCAT4_A | economy | 1-4 |
| `food_security_level` | FDSCAT4_A | economy | Text: High, Marginal, Low, Very Low |
| `housing_cost` | HOUSECOST_A | economy | Text: YES / NO |
| `high_blpressure` | HYPEV_A | health | Text: YES / NO |
| `had_asthma` | ASEV_A | health | Text: YES / NO |
| `had_arthritis` | ARTHEV_A | health | Text: YES / NO |
| `had_diabetes` | DIBEV_A | health | Text: YES / NO |
| `activityLevelPerGuidelines` | PA18_02R_A | health | 1 Inactive, 2 Insufficiently active, 3 Sufficiently active |

## Known inconsistencies to agree on

- Some columns are numeric codes, others are text (YES/NO). Pick one style.
- Column names mix `snake_case` and `camelCase` (`monthly_fullyRested`).
