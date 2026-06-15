# Model Comparison and Champion Selection

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

| Model               |   CV MAE (kg) |   Test MAE (kg) |   Test RMSE (kg) |   Test R2 | Interpretability                        |
|:--------------------|--------------:|----------------:|-----------------:|----------:|:----------------------------------------|
| Linear Regression   |        0.2983 |          0.2812 |           0.3532 |    0.9496 | High - coefficients are easy to explain |
| Random Forest       |        0.3922 |          0.3597 |           0.4639 |    0.9131 | Medium - feature importance available   |
| Tuned Random Forest |        0.3727 |          0.3592 |           0.455  |    0.9164 | Medium - tuned model is more complex    |

## Champion Model

The selected champion model is:

**Linear Regression**

## Champion Selection Rationale

Linear Regression was selected as the champion model because it achieved the lowest test MAE, lowest test RMSE, highest test R2, and strong cross-validation stability.

Although Random Forest and Tuned Random Forest are capable of modeling nonlinear patterns, they did not outperform Linear Regression on the current dataset. Linear Regression is also easier to interpret for farm stakeholders because its coefficients directly show how temperature, humidity, CO2, and their interaction influence yield predictions.

## Agritech Metric Interpretation

In mushroom cultivation, MAE is especially useful because it translates directly into expected yield error in kilograms. Underestimating yield may lead to insufficient harvest labor planning, while overestimating yield may disappoint buyers or affect supply commitments.

For the selected Linear Regression model, the test MAE is approximately 0.2812 kg, meaning predictions are typically within about 0.28 kg of the actual daily yield.

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
