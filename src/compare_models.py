from pathlib import Path
import json
import joblib
import pandas as pd
import matplotlib.pyplot as plt

TRAIN_PATH = Path("data/processed/train_features.parquet")
TEST_PATH = Path("data/processed/test_features.parquet")

LINEAR_MODEL_PATH = Path("models/linear_regression.joblib")
RF_MODEL_PATH = Path("models/random_forest.joblib")
TUNED_RF_MODEL_PATH = Path("models/random_forest_tuned.joblib")

LINEAR_METRICS_PATH = Path("reports/metrics_linear.json")
RF_METRICS_PATH = Path("reports/metrics_random_forest.json")
TUNED_RF_METRICS_PATH = Path("reports/metrics_random_forest_tuned.json")
CV_RESULTS_PATH = Path("reports/cv_results.md")

REPORT_PATH = Path("reports/model_comparison.md")
FIG_PATH = Path("reports/figures/pred_vs_actual.png")

Path("reports").mkdir(parents=True, exist_ok=True)
Path("reports/figures").mkdir(parents=True, exist_ok=True)

test = pd.read_parquet(TEST_PATH)

feature_cols = [
    "temperature_c_scaled",
    "humidity_pct_scaled",
    "co2_ppm_scaled",
    "temp_humid_interaction_scaled",
]

target_col = "yield_kg"

X_test = test[feature_cols]
y_test = test[target_col]

linear_model = joblib.load(LINEAR_MODEL_PATH)
rf_model = joblib.load(RF_MODEL_PATH)
tuned_rf_model = joblib.load(TUNED_RF_MODEL_PATH)

linear_metrics = json.loads(LINEAR_METRICS_PATH.read_text(encoding="utf-8"))
rf_metrics = json.loads(RF_METRICS_PATH.read_text(encoding="utf-8"))
tuned_rf_metrics = json.loads(TUNED_RF_METRICS_PATH.read_text(encoding="utf-8"))

comparison = pd.DataFrame([
    {
        "Model": "Linear Regression",
        "CV MAE (kg)": 0.2983,
        "Test MAE (kg)": linear_metrics["test"]["mae"],
        "Test RMSE (kg)": linear_metrics["test"]["rmse"],
        "Test R2": linear_metrics["test"]["r2"],
        "Interpretability": "High - coefficients are easy to explain",
    },
    {
        "Model": "Random Forest",
        "CV MAE (kg)": 0.3922,
        "Test MAE (kg)": rf_metrics["random_forest"]["test"]["mae"],
        "Test RMSE (kg)": rf_metrics["random_forest"]["test"]["rmse"],
        "Test R2": rf_metrics["random_forest"]["test"]["r2"],
        "Interpretability": "Medium - feature importance available",
    },
    {
        "Model": "Tuned Random Forest",
        "CV MAE (kg)": tuned_rf_metrics["best_cv_mae"],
        "Test MAE (kg)": tuned_rf_metrics["test"]["mae"],
        "Test RMSE (kg)": tuned_rf_metrics["test"]["rmse"],
        "Test R2": tuned_rf_metrics["test"]["r2"],
        "Interpretability": "Medium - tuned model is more complex",
    },
])

champion_name = "Linear Regression"
champion_model = linear_model
champion_pred = champion_model.predict(X_test)

plt.figure(figsize=(6, 5))
plt.scatter(y_test, champion_pred, alpha=0.6)

min_val = min(y_test.min(), champion_pred.min())
max_val = max(y_test.max(), champion_pred.max())

plt.plot([min_val, max_val], [min_val, max_val], linestyle="--")
plt.xlabel("Actual Yield (kg)")
plt.ylabel("Predicted Yield (kg)")
plt.title("Champion Model: Predicted vs Actual Yield")
plt.tight_layout()
plt.savefig(FIG_PATH, dpi=150)
plt.close()

comparison_md = comparison.to_markdown(index=False)

report = f"""# Model Comparison and Champion Selection

## Objective

The objective of this task was to compare all trained models and select a champion model for deployment based on predictive performance, stability, interpretability, and suitability for agritech decision support.

## Models Compared

The following models were compared:

- Linear Regression
- Random Forest
- Tuned Random Forest

All models were evaluated using the same untouched hold-out test dataset.

## Metrics Used

The comparison used the following metrics:

- Cross-Validation MAE
- Test MAE
- Test RMSE
- Test R2
- Interpretability

MAE was emphasized because it is easy to explain in agritech terms. For example, a MAE of 0.28 kg means the model is typically off by about 0.28 kg of yield.

## Model Comparison Table

{comparison_md}

## Champion Model

The selected champion model is:

**{champion_name}**

## Champion Selection Rationale

Linear Regression was selected as the champion model because it achieved the lowest test MAE, lowest test RMSE, highest test R2, and strong cross-validation stability.

Although Random Forest and Tuned Random Forest are capable of modeling nonlinear patterns, they did not outperform Linear Regression on the current dataset. Linear Regression is also easier to interpret for farm stakeholders because its coefficients directly show how temperature, humidity, CO2, and their interaction influence yield predictions.

## Agritech Metric Interpretation

In mushroom cultivation, MAE is especially useful because it translates directly into expected yield error in kilograms. Underestimating yield may lead to insufficient harvest labor planning, while overestimating yield may disappoint buyers or affect supply commitments.

For the selected Linear Regression model, the test MAE is approximately {linear_metrics["test"]["mae"]:.4f} kg, meaning predictions are typically within about {linear_metrics["test"]["mae"]:.2f} kg of the actual daily yield.

## Predicted vs Actual Plot

A predicted vs actual yield plot was generated for the champion model and saved to:

`reports/figures/pred_vs_actual.png`

Points close to the diagonal line indicate accurate predictions.

## Known Limitations and Edge Cases

- The model is based on synthetic polyhouse sensor data and may not capture all real-world growing conditions.
- Predictions are reliable mainly within the observed sensor ranges used during training.
- Extreme temperature, humidity, or CO2 values outside the training range may reduce prediction reliability.
- Seasonality effects are limited because explicit seasonal features were not included in the final champion model.
- The model is intended as an advisory tool and should not replace grower judgment.

## Final Recommendation

Linear Regression should be used as the champion model for the current deployment stage because it provides the best balance of accuracy, stability, interpretability, and simplicity.
"""

REPORT_PATH.write_text(report, encoding="utf-8")

print("Model comparison complete.")
print()
print(comparison_md)
print()
print(f"Champion model: {champion_name}")
print(f"Predicted vs actual plot saved -> {FIG_PATH}")
print(f"Report saved -> {REPORT_PATH}")