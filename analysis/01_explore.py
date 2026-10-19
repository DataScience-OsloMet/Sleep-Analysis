# %% [markdown]
# # Work hours and sleep: first look
# Run cell by cell in VS Code ("Run Cell" above each `# %%`), or the whole file:
# First build the data once:  `python scripts/run_all.py`

# %%
import pandas as pd
import matplotlib.pyplot as plt

from src.config import PROCESSED

df = pd.read_csv(PROCESSED / "merged_dataset.csv")
print(df.shape)
df.head()

# %% Work hour groups
df["hours_group"] = pd.cut(
    df["weekly_work_hours"],
    bins=[-1, 0, 9, 19, 29, 200],
    labels=["0", "1-9", "10-19", "20-29", "30+"],
)
df["hours_group"].value_counts().sort_index()

# %% Sleep by hour group (survey-weighted mean of nightly sleep)
def weighted_mean(g):
    g = g.dropna(subset=["nightly_sleep"])
    return (g["nightly_sleep"] * g["survey_weight"]).sum() / g["survey_weight"].sum()

sleep_by_group = df.groupby("hours_group", observed=True).apply(weighted_mean, include_groups=False)
sleep_by_group

# %%
sleep_by_group.plot.bar(ylabel="Hours of sleep per night", title="Sleep by weekly work hours")
plt.tight_layout()
plt.show()
