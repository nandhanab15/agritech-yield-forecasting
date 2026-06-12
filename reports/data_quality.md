# Polyhouse Data Quality Report

## Dataset Overview

Total observations: 927

Date range: 2025-01-02 to 2027-09-27

Sampling frequency: 1 days 00:00:00

Rows passing validity checks: 100.0%


## Summary Statistics

|               |   count |   mean |    std |    min |    25% |    50% |     75% |     max |    cv |
|:--------------|--------:|-------:|-------:|-------:|-------:|-------:|--------:|--------:|------:|
| temperature_c |     927 |  23.94 |   2.16 |  18    |  22.51 |  24.03 |   25.3  |   30    | 0.09  |
| humidity_pct  |     927 |  84.58 |   4.94 |  70    |  81.34 |  84.85 |   88.07 |   95    | 0.058 |
| co2_ppm       |     927 | 906.06 | 181.9  | 500    | 778.16 | 905.1  | 1029.51 | 1450.72 | 0.201 |
| yield_kg      |     927 |  25.43 |   1.56 |  19.96 |  24.46 |  25.45 |   26.4  |   30.14 | 0.061 |

## Yield Analysis

- Mean yield: 25.43 kg

- Median yield: 25.45 kg

- Mean and median yield are very similar, suggesting little skew in harvested yield.


## Data Quality Metrics

- Total rows: 927

- Valid rows: 927

- Percentage passing validity rules: 100.0%


## Agritech Interpretation

- Humidity values appear concentrated within the expected mushroom-growing range.

- Temperature values remain within acceptable oyster mushroom cultivation limits.

- CO₂ variability can reflect ventilation cycles and should be examined during modeling.

- Yield variability appears sufficient for future predictive modeling.
