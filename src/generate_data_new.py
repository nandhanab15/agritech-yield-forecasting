import numpy as np
import pandas as pd
from pathlib import Path

Path("data/raw").mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(42)
n = 1000

timestamps = pd.date_range(start="2025-01-01", periods=n, freq="D")

temperature_c = rng.normal(24, 2.2, n)
humidity_pct = rng.normal(85, 5, n)
co2_ppm = rng.normal(900, 180, n)

temperature_c = np.clip(temperature_c, 18, 30)
humidity_pct = np.clip(humidity_pct, 70, 95)
co2_ppm = np.clip(co2_ppm, 500, 1500)

yield_kg = (
    5
    + 0.30 * temperature_c
    + 0.07 * humidity_pct
    - 0.001 * co2_ppm
    + rng.normal(0, 1.2, n)
)

df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature_c": temperature_c.round(2),
    "humidity_pct": humidity_pct.round(2),
    "co2_ppm": co2_ppm.round(2),
    "yield_kg": yield_kg.round(2)
})

for col in ["temperature_c", "humidity_pct", "co2_ppm"]:
    missing_idx = rng.choice(df.index, size=20, replace=False)
    df.loc[missing_idx, col] = np.nan

outlier_idx = rng.choice(df.index, size=20, replace=False)

df.loc[outlier_idx[:5], "temperature_c"] = 37
df.loc[outlier_idx[5:10], "humidity_pct"] = 45
df.loc[outlier_idx[10:15], "co2_ppm"] = 2300
df.loc[outlier_idx[15:], "yield_kg"] = 28

duplicate_rows = df.sample(25, random_state=42)
df = pd.concat([df, duplicate_rows], ignore_index=True)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

output_path = "data/raw/polyhouse_sensors_new.csv"
df.to_csv(output_path, index=False)

print("Realistic dataset created successfully!")
print("Shape:", df.shape)
print("Saved to:", output_path)
print("\nMissing values:")
print(df.isna().sum())
print("\nDuplicate rows:")
print(df.duplicated().sum())