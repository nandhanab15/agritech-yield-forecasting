## Task 4: Feature Engineering & Temporal Train/Test Split

Feature matrix `X` was created using temperature, humidity, CO2, and a temperature-humidity interaction feature. The target variable `y` is `yield_kg`.

A chronological 80/20 train/test split was used to avoid data leakage.

Train period: 2024-01-01 to 2024-10-18  
Train rows: 292

Test period: 2024-10-19 to 2024-12-30  
Test rows: 73

`MinMaxScaler` was fitted only on the training feature data. The test data was transformed using the scaler fitted on the training set, preventing leakage from the test set.

The final scaler was saved using joblib at:

`models/scaler.joblib`

Split artifacts were saved under `data/processed/`.