# Linear Regression Baseline Report

## Model

A baseline Linear Regression model was trained using scaled train features.

## Features Used

- temperature_c_scaled
- humidity_pct_scaled
- co2_ppm_scaled
- temp_humid_interaction_scaled

## Train Metrics

- MAE: 1.00 kg
- RMSE: 1.46 kg
- R²: 0.177

## Test Metrics

- MAE: 0.96 kg
- RMSE: 1.20 kg
- R²: 0.312

## Coefficient Interpretation

- `temperature_c_scaled` has a positive coefficient of 2.4189.
- `humidity_pct_scaled` has a positive coefficient of 1.0205.
- `co2_ppm_scaled` has a negative coefficient of -1.0563.
- `temp_humid_interaction_scaled` has a positive coefficient of 1.0289.


Positive coefficients suggest that higher scaled values are associated with higher predicted yield. Negative coefficients suggest association with lower predicted yield.

Because the features are scaled, these coefficients should be interpreted over the scaled [0, 1] range, not directly per °C, %, or ppm.

## Baseline Comparison Note

The test R² is positive, so the model performs better than simply predicting the mean yield. This is acceptable for a baseline model.
