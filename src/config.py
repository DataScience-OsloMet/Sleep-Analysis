from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
FIGURES = ROOT / "reports" / "figures"

# NHIS 2024 "Sample Adult" file (CDC publishes it as adult24csv.zip)
NHIS_URL = "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHIS/2024/adult24csv.zip"
NHIS_FILE = RAW / "adult24.csv"
