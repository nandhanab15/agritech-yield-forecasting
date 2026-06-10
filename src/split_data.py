from pathlib import Path
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

DATA_PATH = Path("data/processed/02_cleaned.parquet")
PROCESSED = Path("data/processed")
MODELS = Path("models")
REPORTS = Path("reports")

PROCESSED.mkdir(parents=True, exist_ok=True)
MODELS.mkdir(parents=True, exist_ok=True)
REPORTS.mkdir(parents=True, exist_ok=True)

df = pd.read_parquet(DATA_PATH).sort_values("timestamp").reset_index(drop=True)

df["temp_humid_interaction"] = (
    df["temperature_c"] * df["humidity_pct"] / 100
)

feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "temp_humid_interaction"
]

target_col = "yield_kg"

split_idx = int(len(df) * 0.8)

train = df.iloc[:split_idx].copy()
test = df.iloc[split_idx:].copy()

X_train_raw = train[feature_cols]
X_test_raw = test[feature_cols]

y_train = train[target_col]
y_test = test[target_col]

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train_raw)
X_test_scaled = scaler.transform(X_test_raw)

joblib.dump(scaler, MODELS / "minmax_scaler_train.joblib")

X_train = pd.DataFrame(X_train_scaled, columns=[c + "_scaled" for c in feature_cols])
X_test = pd.DataFrame(X_test_scaled, columns=[c + "_scaled" for c in feature_cols])

X_train["timestamp"] = train["timestamp"].values
X_test["timestamp"] = test["timestamp"].values
X_train["yield_kg"] = y_train.values
X_test["yield_kg"] = y_test.values

X_train.to_parquet(PROCESSED / "train_features.parquet", index=False)
X_test.to_parquet(PROCESSED / "test_features.parquet", index=False)

split_report = f"""# Train/Test Split Report

## Split Method

Chronological 80/20 split was used.

The dataset was sorted by timestamp before splitting to prevent future data from appearing in the training set.

## Feature Columns

- temperature_c
- humidity_pct
- co2_ppm
- temp_humid_interaction = temperature_c * humidity_pct / 100

## Target Column

- yield_kg

## Train Period

- Start date: {train["timestamp"].min()}
- End date: {train["timestamp"].max()}
- Rows: {len(train)}

## Test Period

- Start date: {test["timestamp"].min()}
- End date: {test["timestamp"].max()}
- Rows: {len(test)}

## Leakage Prevention

MinMaxScaler was fitted only on the training feature data.

The test data was transformed using the scaler fitted on the training data.

No target values were used to create input features.

The test set remains later in time than the training set.

## Output Files

- data/processed/train_features.parquet
- data/processed/test_features.parquet
- models/minmax_scaler_train.joblib
"""

(REPORTS / "split_report.md").write_text(split_report, encoding="utf-8")

print("Chronological split complete.")
print(f"Train rows: {len(train)}")
print(f"Test rows: {len(test)}")
print(f"Train: {train['timestamp'].min()} -> {train['timestamp'].max()}")
print(f"Test:  {test['timestamp'].min()} -> {test['timestamp'].max()}")
print("Scaler saved -> models/minmax_scaler_train.joblib")
print("Train features saved -> data/processed/train_features.parquet")
print("Test features saved -> data/processed/test_features.parquet")
print("Split report saved -> reports/split_report.md")