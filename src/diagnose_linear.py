from pathlib import Path
import pandas as pd
import joblib
import matplotlib.pyplot as plt

TEST_PATH = Path("data/processed/test_features.parquet")
MODEL_PATH = Path("models/linear_regression.joblib")
FIG_DIR = Path("reports/figures")
REPORT_PATH = Path("reports/linear_diagnostics.md")

FIG_DIR.mkdir(parents=True, exist_ok=True)
Path("reports").mkdir(parents=True, exist_ok=True)

test = pd.read_parquet(TEST_PATH)
model = joblib.load(MODEL_PATH)

feature_cols = [
    "temperature_c_scaled",
    "humidity_pct_scaled",
    "co2_ppm_scaled",
    "temp_humid_interaction_scaled"
]

X_test = test[feature_cols]
y_test = test["yield_kg"]

pred_test = model.predict(X_test)

residuals = y_test - pred_test

# Plot 1: Residuals vs Predicted Yield
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(pred_test, residuals, alpha=0.5)
ax.axhline(0, linestyle="--")
ax.set_xlabel("Predicted Yield (kg)")
ax.set_ylabel("Residual (Actual - Predicted) kg")
ax.set_title("Linear Regression: Residuals vs Predicted Yield")
plt.tight_layout()
plt.savefig(FIG_DIR / "residuals_linear_vs_predicted.png", dpi=150)
plt.close()

# Plot 2: Residuals vs Humidity
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(test["humidity_pct_scaled"], residuals, alpha=0.5)
ax.axhline(0, linestyle="--")
ax.set_xlabel("Scaled Humidity")
ax.set_ylabel("Residual (Actual - Predicted) kg")
ax.set_title("Linear Regression: Residuals vs Humidity")
plt.tight_layout()
plt.savefig(FIG_DIR / "residuals_linear_vs_humidity.png", dpi=150)
plt.close()

# Optional combined figure
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].scatter(pred_test, residuals, alpha=0.5)
axes[0].axhline(0, linestyle="--")
axes[0].set_xlabel("Predicted Yield (kg)")
axes[0].set_ylabel("Residual (Actual - Predicted) kg")
axes[0].set_title("Residuals vs Predicted")

axes[1].scatter(test["humidity_pct_scaled"], residuals, alpha=0.5)
axes[1].axhline(0, linestyle="--")
axes[1].set_xlabel("Scaled Humidity")
axes[1].set_ylabel("Residual (Actual - Predicted) kg")
axes[1].set_title("Residuals vs Humidity")

plt.tight_layout()
plt.savefig(FIG_DIR / "residuals_linear.png", dpi=150)
plt.close()

mean_residual = residuals.mean()
max_abs_residual = residuals.abs().max()

report = f"""# Linear Regression Diagnostics

## Residual Definition

Residuals were calculated as:

`Residual = Actual Yield - Predicted Yield`

This means positive residuals indicate that the model under-predicted yield, while negative residuals indicate that the model over-predicted yield.

## Diagnostic Figures

- `reports/figures/residuals_linear_vs_predicted.png`
- `reports/figures/residuals_linear_vs_humidity.png`
- `reports/figures/residuals_linear.png`

## Residual Summary

- Mean residual: {mean_residual:.3f} kg
- Maximum absolute residual: {max_abs_residual:.3f} kg

## Diagnostic Findings

- Residuals were plotted against predicted yield to check whether the model errors were randomly distributed.
- Residuals were also plotted against scaled humidity to check whether humidity-related nonlinear patterns were present.
- Some residual variation is expected because mushroom yield may depend on nonlinear biological factors and environmental interactions that a simple linear model cannot fully capture.

## Modeling Recommendation

The Linear Regression model should be kept as an interpretable baseline. However, because residual patterns may indicate nonlinear relationships, a nonlinear model such as Random Forest should be tested next to determine whether it improves predictive accuracy.

## Conclusion

The residual analysis supports using Linear Regression as a baseline model while exploring more flexible models in the next stage.
"""

REPORT_PATH.write_text(report, encoding="utf-8")

print("Linear diagnostics complete.")
print(f"Mean residual: {mean_residual:.3f} kg")
print(f"Max absolute residual: {max_abs_residual:.3f} kg")
print("Saved figure -> reports/figures/residuals_linear_vs_predicted.png")
print("Saved figure -> reports/figures/residuals_linear_vs_humidity.png")
print("Saved figure -> reports/figures/residuals_linear.png")
print("Saved report -> reports/linear_diagnostics.md")