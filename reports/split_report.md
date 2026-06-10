# Train/Test Split Report

## Split Method

Chronological 80/20 split was used.

The dataset was sorted by timestamp before splitting to prevent future data from appearing in the training set.

## Feature Columns

- temperature_c
- humidity_pct
- co2_ppm
- temp_humid_interaction = temperature_c * humidity_pct / 100

## Target Column

- yield_kg

## Train Period

- Start date: 2025-01-01 00:00:00
- End date: 2025-02-03 12:00:00
- Rows: 733

## Test Period

- Start date: 2025-02-03 13:00:00
- End date: 2025-02-11 15:00:00
- Rows: 184

## Leakage Prevention

MinMaxScaler was fitted only on the training feature data.

The test data was transformed using the scaler fitted on the training data.

No target values were used to create input features.

The test set remains later in time than the training set.

## Output Files

- data/processed/train_features.parquet
- data/processed/test_features.parquet
- models/minmax_scaler_train.joblib
