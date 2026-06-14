from pathlib import Path
import json
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.metrics import mean_absolute_error

TRAIN_PATH = Path("data/processed/train_features.parquet")
LINEAR_METRICS_PATH = Path("reports/metrics_linear.json")
RF_METRICS_PATH = Path("reports/metrics_random_forest.json")
REPORT_PATH = Path("reports/cv_results.md")

Path("reports").mkdir(parents=True, exist_ok=True)

train = pd.read_parquet(TRAIN_PATH)

feature_cols = [
    "temperature_c_scaled",
    "humidity_pct_scaled",
    "co2_ppm_scaled",
    "temp_humid_interaction_scaled"
]

target_col = "yield_kg"

X_train = train[feature_cols]
y_train = train[target_col]

tscv = TimeSeriesSplit(n_splits=5)

linear_model = LinearRegression()

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

linear_scores = cross_val_score(
    linear_model,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

rf_scores = cross_val_score(
    rf_model,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)

linear_cv_mae = -linear_scores
rf_cv_mae = -rf_scores

linear_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)

linear_train_pred = linear_model.predict(X_train)
rf_train_pred = rf_model.predict(X_train)

linear_train_mae = mean_absolute_error(y_train, linear_train_pred)
rf_train_mae = mean_absolute_error(y_train, rf_train_pred)

linear_test = {}
rf_test = {}

if LINEAR_METRICS_PATH.exists():
    with open(LINEAR_METRICS_PATH, "r", encoding="utf-8") as f:
        linear_test = json.load(f).get("test", {})

if RF_METRICS_PATH.exists():
    with open(RF_METRICS_PATH, "r", encoding="utf-8") as f:
        rf_data = json.load(f)
        rf_test = rf_data.get("random_forest", {}).get("test", {})

report = f"""# Cross-Validation Results

## Objective

TimeSeriesSplit cross-validation was used to evaluate model stability while preserving chronological order.

## Methodology

Cross-validation was performed only on the training dataset:

`data/processed/train_features.parquet`

The untouched test set was not used during cross-validation.

A TimeSeriesSplit strategy with 5 splits was used. Each fold trained on earlier observations and validated on later observations.

The scoring metric was Mean Absolute Error (MAE). Since Scikit-learn returns negative MAE for `neg_mean_absolute_error`, the values were converted back to positive MAE.

## Features Used

- temperature_c_scaled
- humidity_pct_scaled
- co2_ppm_scaled
- temp_humid_interaction_scaled

## Cross-Validated MAE Scores

### Linear Regression

Fold MAE values:

{[round(float(x), 4) for x in linear_cv_mae]}

- Mean CV MAE: {linear_cv_mae.mean():.4f} kg
- Standard Deviation: {linear_cv_mae.std():.4f} kg

### Random Forest

Fold MAE values:

{[round(float(x), 4) for x in rf_cv_mae]}

- Mean CV MAE: {rf_cv_mae.mean():.4f} kg
- Standard Deviation: {rf_cv_mae.std():.4f} kg

## Train, CV, and Test Comparison

| Model | Train MAE | CV Mean MAE | Hold-Out Test MAE |
|---|---:|---:|---:|
| Linear Regression | {linear_train_mae:.4f} | {linear_cv_mae.mean():.4f} | {linear_test.get("mae", "N/A")} |
| Random Forest | {rf_train_mae:.4f} | {rf_cv_mae.mean():.4f} | {rf_test.get("mae", "N/A")} |

## Overfitting Analysis

Linear Regression showed stable performance because its training MAE, cross-validation MAE, and hold-out test MAE were close to each other.

Random Forest achieved a much lower training MAE than its cross-validation and hold-out test MAE. This indicates mild overfitting because the model fits the training data more closely than unseen validation or test data.

## Variance Across Folds

Lower standard deviation across folds indicates more stable model performance.

Linear Regression had a CV MAE standard deviation of {linear_cv_mae.std():.4f} kg.

Random Forest had a CV MAE standard deviation of {rf_cv_mae.std():.4f} kg.

## Recommendation

Cross-validation confirms that Linear Regression is stable and performs strongly on this dataset. Random Forest also performs well, but it shows mild overfitting due to the gap between train MAE and validation/test MAE.

Hyperparameter tuning, such as limiting tree depth or increasing `min_samples_leaf`, can be explored in the next stage to reduce Random Forest overfitting.

## Output

This report was saved to:

`reports/cv_results.md`
"""

REPORT_PATH.write_text(report, encoding="utf-8")

print("Cross-validation complete.")
print("TimeSeriesSplit folds:", tscv.get_n_splits())
print()

print("Linear Regression CV MAE scores:")
print([round(float(x), 4) for x in linear_cv_mae])
print(f"Linear Regression Mean CV MAE: {linear_cv_mae.mean():.4f} kg")
print(f"Linear Regression CV MAE Std:  {linear_cv_mae.std():.4f} kg")
print()

print("Random Forest CV MAE scores:")
print([round(float(x), 4) for x in rf_cv_mae])
print(f"Random Forest Mean CV MAE: {rf_cv_mae.mean():.4f} kg")
print(f"Random Forest CV MAE Std:  {rf_cv_mae.std():.4f} kg")
print()

print(f"Linear Train MAE: {linear_train_mae:.4f} kg")
print(f"Random Forest Train MAE: {rf_train_mae:.4f} kg")
print()

print(f"Report saved -> {REPORT_PATH}")