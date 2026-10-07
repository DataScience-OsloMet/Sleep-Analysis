import io
import zipfile
import urllib.request

import pandas as pd

from src.config import NHIS_FILE, NHIS_URL, RAW


def download_nhis(force: bool = False):
    """Download and unzip the NHIS 2024 Sample Adult CSV into data/raw/ (skipped if it exists)."""
    if NHIS_FILE.exists() and not force:
        return NHIS_FILE
    RAW.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {NHIS_URL} ...")
    req = urllib.request.Request(NHIS_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        payload = resp.read()
    with zipfile.ZipFile(io.BytesIO(payload)) as z:
        csv_names = [n for n in z.namelist() if n.lower().endswith(".csv")]
        z.extract(csv_names[0], RAW)
        extracted = RAW / csv_names[0]
    if extracted != NHIS_FILE:
        extracted.replace(NHIS_FILE)
    return NHIS_FILE


def load_nhis(usecols=None) -> pd.DataFrame:
    """Load the Sample Adult file (downloads it first if missing)."""
    download_nhis()
    return pd.read_csv(NHIS_FILE, usecols=usecols, low_memory=False)
