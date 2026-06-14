# Cross-Validation Results

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

[0.2901, 0.2618, 0.3307, 0.3228, 0.2859]

- Mean CV MAE: 0.2983 kg
- Standard Deviation: 0.0253 kg

### Random Forest

Fold MAE values:

[0.4711, 0.3456, 0.4043, 0.377, 0.363]

- Mean CV MAE: 0.3922 kg
- Standard Deviation: 0.0439 kg

## Train, CV, and Test Comparison

| Model | Train MAE | CV Mean MAE | Hold-Out Test MAE |
|---|---:|---:|---:|
| Linear Regression | 0.2977 | 0.2983 | 0.2812 |
| Random Forest | 0.1310 | 0.3922 | 0.3597 |

## Overfitting Analysis

Linear Regression showed stable performance because its training MAE, cross-validation MAE, and hold-out test MAE were close to each other.

Random Forest achieved a much lower training MAE than its cross-validation and hold-out test MAE. This indicates mild overfitting because the model fits the training data more closely than unseen validation or test data.

## Variance Across Folds

Lower standard deviation across folds indicates more stable model performance.

Linear Regression had a CV MAE standard deviation of 0.0253 kg.

Random Forest had a CV MAE standard deviation of 0.0439 kg.

## Recommendation

Cross-validation confirms that Linear Regression is stable and performs strongly on this dataset. Random Forest also performs well, but it shows mild overfitting due to the gap between train MAE and validation/test MAE.

Hyperparameter tuning, such as limiting tree depth or increasing `min_samples_leaf`, can be explored in the next stage to reduce Random Forest overfitting.

## Output

This report was saved to:

`reports/cv_results.md`
