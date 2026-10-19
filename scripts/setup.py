"""One-command setup: create .venv with the required Python, install packages, download the data.

Run from the project folder:  python scripts/setup.py
Safe to run again: it skips what is already done.
"""

import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV = ROOT / ".venv"
VENV_PYTHON = VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
REQUIRED = (ROOT / ".python-version").read_text().strip()
UV = shutil.which("uv")


def run(command):
    print("$", " ".join(str(part) for part in command))
    subprocess.run([str(part) for part in command], check=True, cwd=ROOT)


def venv_version():
    result = subprocess.run(
        [str(VENV_PYTHON), "-c", "import platform; print(platform.python_version())"],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def create_venv():
    if UV:
        run([UV, "venv", "--python", REQUIRED, VENV])  # uv downloads the exact version if missing
    elif platform.python_version() == REQUIRED:
        run([sys.executable, "-m", "venv", VENV])
    else:
        sys.exit(
            f"ERROR: you are running Python {platform.python_version()}, but the project needs {REQUIRED}.\n"
            f"Easiest fix: install uv (https://docs.astral.sh/uv/) and run this script again,\n"
            f"it then fetches Python {REQUIRED} for you. Or install Python {REQUIRED} yourself."
        )


def main():
    if VENV_PYTHON.exists():
        found = venv_version()
        if found != REQUIRED:
            sys.exit(
                f"ERROR: .venv uses Python {found}, but the project needs {REQUIRED}.\n"
                "Delete the .venv folder and run this script again."
            )
        print(f".venv already uses Python {found}")
    else:
        create_venv()

    if UV:
        run([UV, "pip", "install", "--python", VENV_PYTHON, "-r", "requirements.txt"])
    else:
        run([VENV_PYTHON, "-m", "pip", "install", "-r", "requirements.txt"])

    run([VENV_PYTHON, "scripts/download_data.py"])
    print("\nDone. Open this folder in VS Code, open a notebook and select the .venv kernel.")


if __name__ == "__main__":
    main()
