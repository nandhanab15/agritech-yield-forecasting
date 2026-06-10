import numpy as np
import pandas as pd
from pathlib import Path

Path("data/raw").mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(42)
n = 1000

timestamps = pd.date_range(
    start="2025-01-01",
    periods=n,
    freq="h"
)

temperature_c = rng.normal(22, 2, n)
humidity_pct = rng.normal(75, 8, n)
co2_ppm = rng.normal(900, 150, n)

yield_kg = (
    0.3 * temperature_c
    + 0.05 * humidity_pct
    + 0.002 * co2_ppm
    + rng.normal(0, 1, n)
)

df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature_c": temperature_c.round(2),
    "humidity_pct": humidity_pct.round(2),
    "co2_ppm": co2_ppm.round(2),
    "yield_kg": yield_kg.round(2)
})

for col in ["temperature_c", "humidity_pct", "co2_ppm"]:
    missing_idx = rng.choice(df.index, size=25, replace=False)
    df.loc[missing_idx, col] = np.nan

yield_missing_idx = rng.choice(df.index, size=10, replace=False)
df.loc[yield_missing_idx, "yield_kg"] = np.nan

duplicate_rows = df.sample(20, random_state=42)
df = pd.concat([df, duplicate_rows], ignore_index=True)

output_path = "data/raw/polyhouse_sensors_1000.csv"
df.to_csv(output_path, index=False)

print("Dataset Created Successfully!")
print("Shape:", df.shape)
print("Missing values:")
print(df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Saved to:", output_path)