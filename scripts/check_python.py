"""Stop with a clear message if Python is not the version the project requires.

The required version is the single line in `.python-version`.
Run from the project root:  python scripts/check_python.py
"""

import sys
from pathlib import Path

VERSION_FILE = Path(__file__).resolve().parents[1] / ".python-version"


def check(required: str) -> bool:
    running = ".".join(str(part) for part in sys.version_info[:3])
    if running == required:
        print(f"OK: Python {running}")
        return True
    print(
        f"ERROR: this project requires Python {required}, but you are running {running}.\n"
        f"Remove .venv, install Python {required}, recreate .venv and activate it (see README)."
    )
    return False


if __name__ == "__main__":
    sys.exit(0 if check(VERSION_FILE.read_text().strip()) else 1)
