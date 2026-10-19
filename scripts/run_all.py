"""Clean all variables and write data/processed/merged_dataset.csv.

Run from the project folder:  python scripts/run_all.py
(The same as `python -m src.pipeline` inside the .venv.)
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = ROOT / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")

if not VENV_PYTHON.exists():
    sys.exit("No .venv yet. Run this first:  python scripts/setup.py")
sys.exit(subprocess.run([str(VENV_PYTHON), "-m", "src.pipeline"], cwd=ROOT).returncode)
