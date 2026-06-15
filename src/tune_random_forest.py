from pathlib import Path
import json
import time

import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

TRAIN_PATH = Path("data/processed/train_features.parquet")
TEST_PATH = Path("data/processed/test_features.parquet")

MODEL_PATH = Path("models/random_forest_tuned.joblib")
PARAMS_PATH = Path("models/rf_best_params.json")
METRICS_PATH = Path("reports/metrics_random_forest_tuned.json")
CV_RESULTS_PATH = Path("reports/rf_gridsearch_results.csv")
REPORT_PATH = Path("reports/rf_tuning_report.md")

Path("models").mkdir(parents=True, exist_ok=True)
Path("reports").mkdir(parents=True, exist_ok=True)

train = pd.read_parquet(TRAIN_PATH)
test = pd.read_parquet(TEST_PATH)

feature_cols = [
    "temperature_c_scaled",
    "humidity_pct_scaled",
    "co2_ppm_scaled",
    "temp_humid_interaction_scaled",
]

target_col = "yield_kg"

X_train = train[feature_cols]
y_train = train[target_col]

X_test = test[feature_cols]
y_test = test[target_col]

tscv = TimeSeriesSplit(n_splits=3)

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 8, 16],
    "min_samples_leaf": [1, 3, 5],
}

rf = RandomForestRegressor(
    random_state=42,
    n_jobs=-1,
)

search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=tscv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1,
    refit=True,
    return_train_score=True,
)

start_time = time.time()
search.fit(X_train, y_train)
runtime_seconds = time.time() - start_time

best_model = search.best_estimator_
best_params = search.best_params_
best_cv_mae = -search.best_score_

pred_train = best_model.predict(X_train)
pred_test = best_model.predict(X_test)

train_mae = mean_absolute_error(y_train, pred_train)
train_rmse = np.sqrt(mean_squared_error(y_train, pred_train))
train_r2 = r2_score(y_train, pred_train)

test_mae = mean_absolute_error(y_test, pred_test)
test_rmse = np.sqrt(mean_squared_error(y_test, pred_test))
test_r2 = r2_score(y_test, pred_test)

joblib.dump(best_model, MODEL_PATH)

with open(PARAMS_PATH, "w", encoding="utf-8") as f:
    json.dump(best_params, f, indent=4)

metrics = {
    "best_params": best_params,
    "best_cv_mae": round(float(best_cv_mae), 4),
    "runtime_seconds": round(float(runtime_seconds), 2),
    "train": {
        "mae": round(float(train_mae), 4),
        "rmse": round(float(train_rmse), 4),
        "r2": round(float(train_r2), 4),
    },
    "test": {
        "mae": round(float(test_mae), 4),
        "rmse": round(float(test_rmse), 4),
        "r2": round(float(test_r2), 4),
    },
}

with open(METRICS_PATH, "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=4)

cv_results = pd.DataFrame(search.cv_results_)
cv_results.to_csv(CV_RESULTS_PATH, index=False)

report = f"""# Random Forest Hyperparameter Tuning Report

## Objective

GridSearchCV was used to tune Random Forest hyperparameters using TimeSeriesSplit cross-validation on the training dataset only.

## Parameter Grid

- n_estimators: [50, 100, 200]
- max_depth: [None, 8, 16]
- min_samples_leaf: [1, 3, 5]

## Parameter Rationale

- n_estimators controls the number of trees in the forest.
- max_depth controls how deep each tree can grow and helps reduce overfitting.
- min_samples_leaf controls the minimum number of samples required in each leaf node and helps smooth predictions.

## Cross-Validation Strategy

TimeSeriesSplit with 3 splits was used to preserve chronological order.

The test dataset was not used during GridSearchCV.

## Best Parameters

- n_estimators: {best_params["n_estimators"]}
- max_depth: {best_params["max_depth"]}
- min_samples_leaf: {best_params["min_samples_leaf"]}

## Best Cross-Validation Score

- Best CV MAE: {best_cv_mae:.4f} kg

## Tuned Model Performance

### Train Metrics

- MAE: {train_mae:.4f} kg
- RMSE: {train_rmse:.4f} kg
- R2: {train_r2:.4f}

### Test Metrics

- MAE: {test_mae:.4f} kg
- RMSE: {test_rmse:.4f} kg
- R2: {test_r2:.4f}

## Runtime

- Runtime: {runtime_seconds:.2f} seconds

The runtime was reasonable for a laptop because the grid was kept modest.

## Output Files

- Tuned model: models/random_forest_tuned.joblib
- Best parameters: models/rf_best_params.json
- Tuned metrics: reports/metrics_random_forest_tuned.json
- Grid search results: reports/rf_gridsearch_results.csv
- Report: reports/rf_tuning_report.md

## Conclusion

The tuned Random Forest model was evaluated once on the held-out test set after tuning. Hyperparameter tuning was performed only on the training data using TimeSeriesSplit to avoid data leakage.
"""

REPORT_PATH.write_text(report, encoding="utf-8")

print("Random Forest GridSearchCV complete.")
print(f"Runtime: {runtime_seconds:.2f} seconds")
print()
print("Best params:")
print(best_params)
print(f"Best CV MAE: {best_cv_mae:.4f} kg")
print()
print("Tuned Random Forest Train Metrics:")
print(f"Train MAE:  {train_mae:.4f} kg")
print(f"Train RMSE: {train_rmse:.4f} kg")
print(f"Train R2:   {train_r2:.4f}")
print()
print("Tuned Random Forest Test Metrics:")
print(f"Test MAE:   {test_mae:.4f} kg")
print(f"Test RMSE:  {test_rmse:.4f} kg")
print(f"Test R2:    {test_r2:.4f}")
print()
print(f"Model saved -> {MODEL_PATH}")
print(f"Best params saved -> {PARAMS_PATH}")
print(f"Metrics saved -> {METRICS_PATH}")
print(f"CV results saved -> {CV_RESULTS_PATH}")
print(f"Report saved -> {REPORT_PATH}")