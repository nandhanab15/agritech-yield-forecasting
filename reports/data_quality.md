# Polyhouse Data Quality Report

## Dataset Overview

Total observations: 917

Date range: 2025-01-01 to 2025-02-11

Sampling frequency: 0 days 01:00:00

Rows passing validity checks: 100.0%


## Summary Statistics

|               |   count |   mean |    std |    min |    25% |    50% |     75% |     max |    cv |
|:--------------|--------:|-------:|-------:|-------:|-------:|-------:|--------:|--------:|------:|
| temperature_c |     917 |  21.94 |   1.97 |  14.7  |  20.61 |  22.02 |   23.17 |   28.36 | 0.09  |
| humidity_pct  |     917 |  74.22 |   8.05 |  50.62 |  68.98 |  74.53 |   79.51 |   98.31 | 0.108 |
| co2_ppm       |     917 | 903.61 | 153.02 | 440.43 | 800.84 | 903.67 | 1002.36 | 1358.93 | 0.169 |
| yield_kg      |     917 |  12.1  |   1.26 |   8.18 |  11.24 |  12.12 |   12.93 |   16.25 | 0.104 |

## Yield Analysis

- Mean yield: 12.1 kg

- Median yield: 12.12 kg

- Mean and median yield are very similar, suggesting little skew in harvested yield.


## Data Quality Metrics

- Total rows: 917

- Valid rows: 917

- Percentage passing validity rules: 100.0%


## Agritech Interpretation

- Humidity values appear concentrated within the expected mushroom-growing range.

- Temperature values remain within acceptable oyster mushroom cultivation limits.

- CO₂ variability can reflect ventilation cycles and should be examined during modeling.

- Yield variability appears sufficient for future predictive modeling.
