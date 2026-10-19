"""Download the NHIS 2024 Sample Adult dataset from the CDC."""

from __future__ import annotations

import shutil
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path


DATA_URL = (
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2024/"
    "adult24csv.zip"
)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "raw"
DATA_PATH = DATA_DIR / "adult24.csv"


def download_data() -> None:
    """Download and extract adult24.csv unless it is already present."""
    if DATA_PATH.exists():
        print(f"Dataset already exists: {DATA_PATH}")
        return

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as temporary_directory:
        archive_path = Path(temporary_directory) / "adult24csv.zip"
        print("Downloading NHIS 2024 Sample Adult dataset from the CDC...")
        try:
            urllib.request.urlretrieve(DATA_URL, archive_path)
        except (OSError, urllib.error.URLError) as error:
            raise RuntimeError(f"Could not download the dataset from {DATA_URL}") from error

        try:
            with zipfile.ZipFile(archive_path) as archive:
                member = next(
                    (
                        name
                        for name in archive.namelist()
                        if Path(name).name.lower() == "adult24.csv"
                    ),
                    None,
                )
                if member is None:
                    raise RuntimeError("The CDC archive does not contain adult24.csv")

                extracted_path = Path(archive.extract(member, temporary_directory))
                shutil.move(str(extracted_path), DATA_PATH)
        except (OSError, zipfile.BadZipFile) as error:
            raise RuntimeError("The downloaded CDC archive could not be unpacked") from error

    print(f"Dataset saved to: {DATA_PATH}")


if __name__ == "__main__":
    download_data()
