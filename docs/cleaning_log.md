# Cleaning Log

## Input File
- data/interim/01_loaded.parquet

## Output Files
- data/processed/02_cleaned.parquet
- data/processed/cleaned_sample_50_rows.csv

## Missing Values Before Cleaning

|               |   missing_count |   missing_percentage |
|:--------------|----------------:|---------------------:|
| timestamp     |               0 |                 0    |
| temperature_c |              25 |                 2.45 |
| humidity_pct  |              25 |                 2.45 |
| co2_ppm       |              27 |                 2.65 |
| yield_kg      |              10 |                 0.98 |

## Missing Values After Cleaning

|               |   missing_count |   missing_percentage |
|:--------------|----------------:|---------------------:|
| timestamp     |               0 |                    0 |
| temperature_c |               0 |                    0 |
| humidity_pct  |               0 |                    0 |
| co2_ppm       |               0 |                    0 |
| yield_kg      |               0 |                    0 |

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

- Original rows: 1020
- Cleaned rows: 917
- Rows removed: 103
