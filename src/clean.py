import pandas as pd
from pathlib import Path

INPUT = Path("data/interim/01_loaded.parquet")
PROCESSED = Path("data/processed")
DOCS = Path("docs")

PROCESSED.mkdir(parents=True, exist_ok=True)
DOCS.mkdir(parents=True, exist_ok=True)

df = pd.read_parquet(INPUT)
original_rows = len(df)

# Missing report before cleaning
missing_before = pd.DataFrame({
    "missing_count": df.isna().sum(),
    "missing_percentage": (df.isna().sum() / len(df) * 100).round(2)
})

print("\nMissing Values Before Cleaning:")
print(missing_before)

# Validity rules
valid = (
    df["humidity_pct"].between(50, 100)
    & df["temperature_c"].between(10, 35)
    & df["co2_ppm"].between(400, 2000)
)

df = df[valid].copy()

# Forward-fill sensor columns only
sensor_cols = ["temperature_c", "humidity_pct", "co2_ppm"]
df[sensor_cols] = df[sensor_cols].ffill(limit=2)

# Never impute target column
df = df.dropna(subset=["yield_kg"])

# Remove duplicate timestamps
df = df.drop_duplicates(subset=["timestamp"], keep="last")

cleaned_rows = len(df)
rows_removed = original_rows - cleaned_rows

# Missing report after cleaning
missing_after = pd.DataFrame({
    "missing_count": df.isna().sum(),
    "missing_percentage": (df.isna().sum() / len(df) * 100).round(2)
})

print("\nMissing Values After Cleaning:")
print(missing_after)

# Save cleaned data
df.to_parquet(PROCESSED / "02_cleaned.parquet", index=False)

# Save sample of 50+ rows
df.head(50).to_csv(PROCESSED / "cleaned_sample_50_rows.csv", index=False)

# Cleaning log
log = f"""# Cleaning Log

## Input File
- data/interim/01_loaded.parquet

## Output Files
- data/processed/02_cleaned.parquet
- data/processed/cleaned_sample_50_rows.csv

## Missing Values Before Cleaning

{missing_before.to_markdown()}

## Missing Values After Cleaning

{missing_after.to_markdown()}

## Cleaning Strategy

- temperature_c: Forward-filled short gaps up to 2 rows because sensor readings may temporarily fail due to logger or power issues.
- humidity_pct: Forward-filled short gaps up to 2 rows because humidity sensors may briefly miss readings.
- co2_ppm: Forward-filled short gaps up to 2 rows because CO₂ sensors may have short communication drops.
- yield_kg: Not imputed. Missing target values are removed to avoid label leakage.

## Validity Rules

- humidity_pct must be between 50 and 100.
- temperature_c must be between 10 and 35 °C.
- co2_ppm must be between 400 and 2000 ppm.
- yield_kg must not be null.

## Duplicate Handling

Duplicate timestamp rows were removed using keep="last".

## Row Count Summary

- Original rows: {original_rows}
- Cleaned rows: {cleaned_rows}
- Rows removed: {rows_removed}
"""

with open(DOCS / "cleaning_log.md", "w", encoding="utf-8") as f:
    f.write(log)

print(f"\nCleaned file saved: data/processed/02_cleaned.parquet")
print(f"Sample saved: data/processed/cleaned_sample_50_rows.csv")
print(f"Cleaning log saved: docs/cleaning_log.md")
print(f"Clean rows: {cleaned_rows}")