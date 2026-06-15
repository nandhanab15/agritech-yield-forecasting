# Random Forest Hyperparameter Tuning Report

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

- n_estimators: 100
- max_depth: 16
- min_samples_leaf: 3

## Best Cross-Validation Score

- Best CV MAE: 0.3727 kg

## Tuned Model Performance

### Train Metrics

- MAE: 0.2041 kg
- RMSE: 0.3492 kg
- R2: 0.9497

### Test Metrics

- MAE: 0.3592 kg
- RMSE: 0.4550 kg
- R2: 0.9164

## Runtime

- Runtime: 4.79 seconds

The runtime was reasonable for a laptop because the grid was kept modest.

## Output Files

- Tuned model: models/random_forest_tuned.joblib
- Best parameters: models/rf_best_params.json
- Tuned metrics: reports/metrics_random_forest_tuned.json
- Grid search results: reports/rf_gridsearch_results.csv
- Report: reports/rf_tuning_report.md

## Conclusion

The tuned Random Forest model was evaluated once on the held-out test set after tuning. Hyperparameter tuning was performed only on the training data using TimeSeriesSplit to avoid data leakage.
