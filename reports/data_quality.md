# Polyhouse Data Quality Report

## Dataset Overview

Total observations: 365

Date range: 2024-01-01 to 2024-12-30

Sampling frequency: 1 days 00:00:00

Rows passing validity checks: 100.0%


## Summary Statistics

|               |   count |   mean |   std |    min |    25% |    50% |    75% |     max |    cv |
|:--------------|--------:|-------:|------:|-------:|-------:|-------:|-------:|--------:|------:|
| temperature_c |     365 |  21.99 |  1.41 |  18.15 |  21.01 |  21.97 |  22.88 |   26.37 | 0.064 |
| humidity_pct  |     365 |  86.74 |  3.07 |  78.1  |  84.6  |  86.7  |  88.7  |   94.8  | 0.035 |
| co2_ppm       |     365 | 901.16 | 78.27 | 608    | 854    | 904    | 949    | 1154    | 0.087 |
| yield_kg      |     365 |  17.14 |  0.68 |  15.31 |  16.7  |  17.13 |  17.63 |   18.85 | 0.04  |

## Yield Analysis

- Mean yield: 17.14 kg

- Median yield: 17.13 kg

- Mean and median yield are very similar, suggesting little skew in harvested yield.


## Data Quality Metrics

- Total rows: 365

- Valid rows: 365

- Percentage passing validity rules: 100.0%


## Agritech Interpretation

- Humidity values appear concentrated within the expected mushroom-growing range.

- Temperature values remain within acceptable oyster mushroom cultivation limits.

- CO₂ variability can reflect ventilation cycles and should be examined during modeling.

- Yield variability appears sufficient for future predictive modeling.
