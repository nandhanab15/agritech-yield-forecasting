# Linear Regression Baseline Report

## Model

A baseline Linear Regression model was trained using scaled train features.

## Features Used

- temperature_c_scaled
- humidity_pct_scaled
- co2_ppm_scaled
- temp_humid_interaction_scaled

## Train Metrics

- MAE: 0.30 kg
- RMSE: 0.48 kg
- R²: 0.904

## Test Metrics

- MAE: 0.28 kg
- RMSE: 0.35 kg
- R²: 0.950

## Coefficient Interpretation

- `temperature_c_scaled` has a positive coefficient of 6.1082.
- `humidity_pct_scaled` has a positive coefficient of 2.6324.
- `co2_ppm_scaled` has a negative coefficient of -2.7993.
- `temp_humid_interaction_scaled` has a positive coefficient of 0.9876.


Positive coefficients suggest that higher scaled values are associated with higher predicted yield. Negative coefficients suggest association with lower predicted yield.

Because the features are scaled, these coefficients should be interpreted over the scaled [0, 1] range, not directly per °C, %, or ppm.

## Baseline Comparison Note

The test R² is positive, so the model performs better than simply predicting the mean yield. This is acceptable for a baseline model.
