# Random Forest Regression Report

## Model

A Random Forest Regressor was trained using the same leak-free train/test split used for the Linear Regression baseline.

## Features Used

- temperature_c_scaled
- humidity_pct_scaled
- co2_ppm_scaled
- temp_humid_interaction_scaled

## Random Forest Metrics

### Train

- MAE: 0.13 kg
- RMSE: 0.21 kg
- R²: 0.982

### Test

- MAE: 0.36 kg
- RMSE: 0.46 kg
- R²: 0.913

## Linear Regression Baseline

- MAE: 0.2812
- RMSE: 0.3532
- R²: 0.9496

## Comparison

Random Forest did not improve R² over Linear Regression.

## Feature Importance

The feature importance plot was saved to:

`reports/figures/rf_importance.png`

The most important feature according to Random Forest was:

`temp_humid_interaction_scaled`

## Interpretation

Random Forest can capture nonlinear relationships and interactions between environmental variables. If its test performance improves over Linear Regression, the added complexity is justified. If the improvement is small, Linear Regression remains useful as a simpler and more interpretable baseline.

## Model Artifact

The trained Random Forest model was saved to:

`models/random_forest.joblib`
