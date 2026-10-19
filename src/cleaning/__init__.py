"""One module per person. Each exposes clean() -> DataFrame indexed by household_id."""

from src.cleaning import endre, jorgen, kristine, lykke

CLEANERS = {
    "jorgen": jorgen.clean,
    "kristine": kristine.clean,
    "endre": endre.clean,
    "lykke": lykke.clean,
}
