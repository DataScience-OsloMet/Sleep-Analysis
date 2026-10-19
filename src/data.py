"""Download and load the NHIS 2024 Sample Adult file.

Run `uv run python -m src.data` to download it by hand. The pipeline also
downloads it automatically when it is missing.
"""

import shutil
import ssl
import subprocess
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

from src.config import NHIS_FILE, NHIS_URL, RAW


def _fetch(url: str, destination: Path) -> None:
    """Download url to destination.

    If the certificate check fails (common on school networks, VPNs and with
    antivirus), retry with the operating system's certificates, then with curl.
    """
    try:
        urllib.request.urlretrieve(url, destination)
        return
    except urllib.error.URLError as error:
        if not isinstance(error.reason, ssl.SSLError):
            raise
        print("Certificate check failed. Retrying with the operating system's certificates ...")

    try:
        import truststore

        truststore.inject_into_ssl()
        urllib.request.urlretrieve(url, destination)
        return
    except (ImportError, OSError):
        pass

    curl = shutil.which("curl")
    if curl:
        print("Retrying with curl ...")
        subprocess.run([curl, "-fL", "-o", str(destination), url], check=True)
        return

    raise OSError("all download attempts failed")


def download_nhis() -> Path:
    """Download and unzip adult24.csv into data/raw/ (skipped if it already exists)."""
    if NHIS_FILE.exists():
        return NHIS_FILE
    RAW.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        archive_path = Path(tmp) / "adult24csv.zip"
        print(f"Downloading {NHIS_URL} ...")
        try:
            _fetch(NHIS_URL, archive_path)
        except (OSError, subprocess.CalledProcessError) as error:
            raise RuntimeError(
                f"Could not download the dataset from {NHIS_URL}\n"
                f"Download the zip in your browser, unzip it, and put adult24.csv in {RAW}."
            ) from error

        with zipfile.ZipFile(archive_path) as archive:
            member = next((n for n in archive.namelist() if Path(n).name.lower() == "adult24.csv"), None)
            if member is None:
                raise RuntimeError("The CDC archive does not contain adult24.csv")
            shutil.move(archive.extract(member, tmp), NHIS_FILE)

    print(f"Saved {NHIS_FILE}")
    return NHIS_FILE


def load_nhis(usecols=None) -> pd.DataFrame:
    """Load the Sample Adult file (downloads it first if missing)."""
    download_nhis()
    return pd.read_csv(NHIS_FILE, usecols=usecols, low_memory=False)


if __name__ == "__main__":
    download_nhis()
