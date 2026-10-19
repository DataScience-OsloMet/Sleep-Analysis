"""Run every notebook in notebooks/ (in alphabetical order), then merge_dataset.py.

Run from the project folder:  python scripts/run_all.py

The notebooks are executed in the project's .venv. Their saved files in
notebooks/ are not changed. Only the CSV files in data/processed/ are written.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"
VENV_PYTHON = ROOT / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def main():
    if not VENV_PYTHON.exists():
        sys.exit("No .venv yet. Run this first:  python scripts/setup.py")
    if not (ROOT / "data" / "raw" / "adult24.csv").exists():
        sys.exit("The data is missing. Run this first:  python scripts/setup.py")

    notebooks = sorted(NOTEBOOKS.glob("*.ipynb"))
    with tempfile.TemporaryDirectory() as scratch:
        for notebook in notebooks:
            print(f"Running {notebook.name} ...", flush=True)
            result = subprocess.run(
                [str(VENV_PYTHON), "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
                 notebook.name, "--output-dir", scratch],
                cwd=NOTEBOOKS,  # the notebooks use paths relative to their own folder
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print(result.stderr[-1500:])
                sys.exit(f"ERROR: {notebook.name} failed (see the message above). Nothing was merged.")

    print(f"\nRan {len(notebooks)} notebooks. Merging ...\n", flush=True)
    subprocess.run([str(VENV_PYTHON), "scripts/merge_dataset.py"], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
