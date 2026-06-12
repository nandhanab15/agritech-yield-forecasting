from pathlib import Path
import json
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

TRAIN_PATH = Path("data/processed/train_features.parquet")
TEST_PATH = Path("data/processed/test_features.parquet")
LINEAR_METRICS_PATH = Path("reports/metrics_linear.json")

MODEL_PATH = Path("models/random_forest.joblib")
METRICS_PATH = Path("reports/metrics_random_forest.json")
REPORT_PATH = Path("reports/random_forest_report.md")
FIG_PATH = Path("reports/figures/rf_importance.png")

Path("models").mkdir(parents=True, exist_ok=True)
Path("reports").mkdir(parents=True, exist_ok=True)
Path("reports/figures").mkdir(parents=True, exist_ok=True)

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

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

pred_train = rf.predict(X_train)
pred_test = rf.predict(X_test)

train_mae = mean_absolute_error(y_train, pred_train)
train_rmse = np.sqrt(mean_squared_error(y_train, pred_train))
train_r2 = r2_score(y_train, pred_train)

test_mae = mean_absolute_error(y_test, pred_test)
test_rmse = np.sqrt(mean_squared_error(y_test, pred_test))
test_r2 = r2_score(y_test, pred_test)

joblib.dump(rf, MODEL_PATH)

importances = pd.DataFrame({
    "feature": feature_cols,
    "importance": rf.feature_importances_
}).sort_values("importance", ascending=True)

plt.figure(figsize=(7, 4))
plt.barh(importances["feature"], importances["importance"])
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title("Random Forest Feature Importance")
plt.tight_layout()
plt.savefig(FIG_PATH, dpi=150)
plt.close()

linear_test = {}
if LINEAR_METRICS_PATH.exists():
    with open(LINEAR_METRICS_PATH, "r", encoding="utf-8") as f:
        linear_metrics = json.load(f)
        linear_test = linear_metrics.get("test", {})

metrics = {
    "random_forest": {
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
        "feature_importances": {
            row["feature"]: round(float(row["importance"]), 4)
            for _, row in importances.sort_values("importance", ascending=False).iterrows()
        }
    },
    "linear_regression_test": linear_test
}

with open(METRICS_PATH, "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=4)

comparison_note = "Random Forest improved over Linear Regression."
if linear_test:
    if test_r2 <= linear_test.get("r2", -999):
        comparison_note = "Random Forest did not improve R² over Linear Regression."
    else:
        comparison_note = "Random Forest improved R² over Linear Regression."

top_feature = importances.sort_values("importance", ascending=False).iloc[0]["feature"]

report = f"""# Random Forest Regression Report

## Model

A Random Forest Regressor was trained using the same leak-free train/test split used for the Linear Regression baseline.

## Features Used

- temperature_c_scaled
- humidity_pct_scaled
- co2_ppm_scaled
- temp_humid_interaction_scaled

## Random Forest Metrics

### Train

- MAE: {train_mae:.2f} kg
- RMSE: {train_rmse:.2f} kg
- R²: {train_r2:.3f}

### Test

- MAE: {test_mae:.2f} kg
- RMSE: {test_rmse:.2f} kg
- R²: {test_r2:.3f}

## Linear Regression Baseline

- MAE: {linear_test.get("mae", "not available")}
- RMSE: {linear_test.get("rmse", "not available")}
- R²: {linear_test.get("r2", "not available")}

## Comparison

{comparison_note}

## Feature Importance

The feature importance plot was saved to:

`reports/figures/rf_importance.png`

The most important feature according to Random Forest was:

`{top_feature}`

## Interpretation

Random Forest can capture nonlinear relationships and interactions between environmental variables. If its test performance improves over Linear Regression, the added complexity is justified. If the improvement is small, Linear Regression remains useful as a simpler and more interpretable baseline.

## Model Artifact

The trained Random Forest model was saved to:

`models/random_forest.joblib`
"""

REPORT_PATH.write_text(report, encoding="utf-8")

print("Random Forest training complete.")
print(f"RF Train MAE:  {train_mae:.2f} kg")
print(f"RF Train RMSE: {train_rmse:.2f} kg")
print(f"RF Train R2:   {train_r2:.3f}")
print()
print(f"RF Test MAE:   {test_mae:.2f} kg")
print(f"RF Test RMSE:  {test_rmse:.2f} kg")
print(f"RF Test R2:    {test_r2:.3f}")
print()
print("Feature importances:")
for _, row in importances.sort_values("importance", ascending=False).iterrows():
    print(f"{row['feature']}: {row['importance']:.4f}")

print()
print(f"Model saved -> {MODEL_PATH}")
print(f"Metrics saved -> {METRICS_PATH}")
print(f"Report saved -> {REPORT_PATH}")
print(f"Feature importance plot saved -> {FIG_PATH}")