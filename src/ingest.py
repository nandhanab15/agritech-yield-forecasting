import pandas as pd
from pathlib import Path

RAW = Path("data/raw/polyhouse_sensors.csv")
INTERIM = Path("data/interim")
INTERIM.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(
    RAW,
    parse_dates=["timestamp"]
)

print("\nSHAPE:", df.shape)
print("\nCOLUMNS:", df.columns)
print("\nDTYPES:\n", df.dtypes)
print("\nHEAD:\n", df.head())
print("\nINFO:")
print(df.info())

df.to_parquet(INTERIM / "01_loaded.parquet", index=False)

print("\nSaved -> data/interim/01_loaded.parquet")