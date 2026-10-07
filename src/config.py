from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "reports" / "figures"

# Update when the NHIS file is downloaded
NHIS_FILE = RAW / "samadult_2025.csv"
