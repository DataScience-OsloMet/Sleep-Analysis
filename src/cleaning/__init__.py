"""One module per topic. Each exposes clean() -> DataFrame indexed by household id.

To add a variable, edit the module for its topic. To add a new topic, create
a module and list it here.
"""

from src.cleaning import demographics, economy, health, mental_health, sleep, work

CLEANERS = {
    "work": work.clean,
    "sleep": sleep.clean,
    "mental_health": mental_health.clean,
    "demographics": demographics.clean,
    "economy": economy.clean,
    "health": health.clean,
}
