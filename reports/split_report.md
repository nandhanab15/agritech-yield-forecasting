# Task 4 Split Summary

## Objective

Build feature matrix X and target y using cleaned polyhouse sensor data.  
A chronological train/test split was used to avoid data leakage.

## Feature Columns

- temperature_c
- humidity_pct
- co2_ppm

## Target Column

- yield_kg

## Split Method

The dataset was sorted by timestamp and split chronologically using an 80:20 ratio.

## Row Counts

- Total rows: 925
- Train rows: 740
- Test rows: 185

## Date Ranges

- Train start date: 2025-01-04 00:00:00
- Train end date: 2027-03-18 00:00:00
- Test start date: 2027-03-19 00:00:00
- Test end date: 2027-09-27 00:00:00

## Scaling

MinMaxScaler was fitted only on the training feature set.  
The test feature set was transformed using the scaler fitted on training data only.

## Leakage Prevention

No test data was used while fitting the scaler.
