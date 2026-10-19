"""Open JupyterLab using the project's .venv. No activation needed.

Run from the project folder:  python scripts/notebook.py
Extra arguments go to Jupyter, e.g.  python scripts/notebook.py --no-browser
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV_PYTHON = ROOT / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def main():
    if not VENV_PYTHON.exists():
        sys.exit("No .venv yet. Run this first:  python scripts/setup.py")
    if subprocess.run([str(VENV_PYTHON), "-c", "import jupyterlab"], capture_output=True).returncode != 0:
        sys.exit("JupyterLab is missing from .venv. Run this first:  python scripts/setup.py")
    subprocess.run(
        [str(VENV_PYTHON), "-m", "jupyter", "lab", "--notebook-dir", str(ROOT), *sys.argv[1:]],
        cwd=ROOT,
    )


if __name__ == "__main__":
    main()
