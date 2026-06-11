from pathlib import Path
import json
import numpy as np
import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

TRAIN_PATH = Path("data/processed/train_features.parquet")
TEST_PATH = Path("data/processed/test_features.parquet")
MODEL_PATH = Path("models/linear_regression.joblib")
METRICS_PATH = Path("reports/metrics_linear.json")
REPORT_PATH = Path("reports/linear_regression_report.md")

Path("models").mkdir(parents=True, exist_ok=True)
Path("reports").mkdir(parents=True, exist_ok=True)

train = pd.read_parquet(TRAIN_PATH)
test = pd.read_parquet(TEST_PATH)

feature_cols = [
    "temperature_c_scaled",
    "humidity_pct_scaled",
    "co2_ppm_scaled",
    "temp_humid_interaction_scaled"
]
target_col = "yield_kg"

X_train = train[feature_cols]
y_train = train[target_col]

X_test = test[feature_cols]
y_test = test[target_col]

model = LinearRegression()
model.fit(X_train, y_train)

pred_train = model.predict(X_train)
pred_test = model.predict(X_test)

train_mae = mean_absolute_error(y_train, pred_train)
train_rmse = np.sqrt(mean_squared_error(y_train, pred_train))
train_r2 = r2_score(y_train, pred_train)

test_mae = mean_absolute_error(y_test, pred_test)
test_rmse = np.sqrt(mean_squared_error(y_test, pred_test))
test_r2 = r2_score(y_test, pred_test)

coefficients = {
    feature: round(float(coef), 4)
    for feature, coef in zip(feature_cols, model.coef_)
}

metrics = {
    "train": {
        "mae": round(float(train_mae), 4),
        "rmse": round(float(train_rmse), 4),
        "r2": round(float(train_r2), 4)
    },
    "test": {
        "mae": round(float(test_mae), 4),
        "rmse": round(float(test_rmse), 4),
        "r2": round(float(test_r2), 4)
    },
    "coefficients": coefficients,
    "intercept": round(float(model.intercept_), 4)
}

with open(METRICS_PATH, "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=4)

joblib.dump(model, MODEL_PATH)

report = f"""# Linear Regression Baseline Report

## Model

A baseline Linear Regression model was trained using scaled train features.

## Features Used

- temperature_c_scaled
- humidity_pct_scaled
- co2_ppm_scaled
- temp_humid_interaction_scaled

## Train Metrics

- MAE: {train_mae:.2f} kg
- RMSE: {train_rmse:.2f} kg
- R²: {train_r2:.3f}

## Test Metrics

- MAE: {test_mae:.2f} kg
- RMSE: {test_rmse:.2f} kg
- R²: {test_r2:.3f}

## Coefficient Interpretation

"""

for feature, coef in coefficients.items():
    direction = "positive" if coef > 0 else "negative"
    report += f"- `{feature}` has a {direction} coefficient of {coef}.\n"

report += """

Positive coefficients suggest that higher scaled values are associated with higher predicted yield. Negative coefficients suggest association with lower predicted yield.

Because the features are scaled, these coefficients should be interpreted over the scaled [0, 1] range, not directly per °C, %, or ppm.

## Baseline Comparison Note

"""

if test_r2 > 0:
    report += "The test R² is positive, so the model performs better than simply predicting the mean yield. This is acceptable for a baseline model.\n"
else:
    report += "The test R² is weak or negative, so the model performs poorly compared with predicting the mean yield. This should be investigated before using more complex models.\n"

REPORT_PATH.write_text(report, encoding="utf-8")

print("Linear Regression training complete.")
print(f"Train MAE:  {train_mae:.2f} kg")
print(f"Train RMSE: {train_rmse:.2f} kg")
print(f"Train R2:   {train_r2:.3f}")
print()
print(f"Test MAE:   {test_mae:.2f} kg")
print(f"Test RMSE:  {test_rmse:.2f} kg")
print(f"Test R2:    {test_r2:.3f}")
print()
print("Coefficients:")
for feature, coef in coefficients.items():
    print(f"{feature}: {coef}")

print()
print(f"Model saved -> {MODEL_PATH}")
print(f"Metrics saved -> {METRICS_PATH}")
print(f"Report saved -> {REPORT_PATH}")