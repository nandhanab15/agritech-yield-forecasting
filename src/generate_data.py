import numpy as np
import pandas as pd
from pathlib import Path

Path("data/raw").mkdir(parents=True, exist_ok=True)

rng = np.random.default_rng(42)
n = 365

temperature_c = rng.normal(22, 1.5, n)
humidity_pct = np.clip(rng.normal(87, 3, n), 75, 98)
co2_ppm = rng.normal(900, 80, n)

yield_kg = (
    8
    + 0.3 * temperature_c
    + 0.05 * humidity_pct
    - 0.002 * co2_ppm
    + rng.normal(0, 0.5, n)
)

df = pd.DataFrame({
    "timestamp": pd.date_range("2024-01-01", periods=n, freq="D"),
    "temperature_c": temperature_c.round(2),
    "humidity_pct": humidity_pct.round(1),
    "co2_ppm": co2_ppm.round(0),
    "yield_kg": yield_kg.round(2),
})

df.to_csv("data/raw/polyhouse_sensors.csv", index=False)

print("Dataset created successfully.")