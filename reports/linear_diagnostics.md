# Linear Regression Diagnostics

## Residual Definition

Residuals were calculated as:

`Residual = Actual Yield - Predicted Yield`

This means positive residuals indicate that the model under-predicted yield, while negative residuals indicate that the model over-predicted yield.

## Diagnostic Figures

- `reports/figures/residuals_linear_vs_predicted.png`
- `reports/figures/residuals_linear_vs_humidity.png`
- `reports/figures/residuals_linear.png`

## Residual Summary

- Mean residual: -0.090 kg
- Maximum absolute residual: 0.890 kg

## Diagnostic Findings

- Residuals were plotted against predicted yield to check whether the model errors were randomly distributed.
- Residuals were also plotted against scaled humidity to check whether humidity-related nonlinear patterns were present.
- Some residual variation is expected because mushroom yield may depend on nonlinear biological factors and environmental interactions that a simple linear model cannot fully capture.

## Modeling Recommendation

The Linear Regression model should be kept as an interpretable baseline. However, because residual patterns may indicate nonlinear relationships, a nonlinear model such as Random Forest should be tested next to determine whether it improves predictive accuracy.

## Conclusion

The residual analysis supports using Linear Regression as a baseline model while exploring more flexible models in the next stage.
