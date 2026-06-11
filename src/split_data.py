import pandas as pd
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler
import joblib

INPUT = Path("data/processed/02_cleaned.parquet")
PROCESSED = Path("data/processed")
MODELS = Path("models")
REPORTS = Path("reports")

PROCESSED.mkdir(parents=True, exist_ok=True)
MODELS.mkdir(parents=True, exist_ok=True)
REPORTS.mkdir(parents=True, exist_ok=True)

df = pd.read_parquet(INPUT)
df["temp_humid_interaction"] = df["temperature_c"] * df["humidity_pct"] / 100

df["temperature_lag1"] = df["temperature_c"].shift(1)
df["humidity_lag1"] = df["humidity_pct"].shift(1)
df["co2_lag1"] = df["co2_ppm"].shift(1)

df["temperature_3day_mean"] = df["temperature_c"].rolling(window=3).mean()
df["humidity_3day_mean"] = df["humidity_pct"].rolling(window=3).mean()
df["co2_3day_mean"] = df["co2_ppm"].rolling(window=3).mean()

df = df.dropna().reset_index(drop=True)
df = df.sort_values("timestamp").reset_index(drop=True)
df["temp_humid_interaction"] = (
    df["temperature_c"] * df["humidity_pct"] / 100
)
feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "temp_humid_interaction",
    "temperature_lag1",
    "humidity_lag1",
    "co2_lag1",
    "temperature_3day_mean",
    "humidity_3day_mean",
    "co2_3day_mean"
]
target_col = "yield_kg"

X = df[feature_cols]
y = df[target_col]

split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index].copy()
X_test = X.iloc[split_index:].copy()
y_train = y.iloc[:split_index].copy()
y_test = y.iloc[split_index:].copy()

train_dates = df["timestamp"].iloc[:split_index]
test_dates = df["timestamp"].iloc[split_index:]

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=[col + "_scaled" for col in feature_cols]
)

X_test_scaled = pd.DataFrame(
    X_test_scaled,
    columns=[col + "_scaled" for col in feature_cols]
)

train_output = pd.concat(
    [
        train_dates.reset_index(drop=True),
        X_train.reset_index(drop=True),
        X_train_scaled,
        y_train.reset_index(drop=True)
    ],
    axis=1
)

test_output = pd.concat(
    [
        test_dates.reset_index(drop=True),
        X_test.reset_index(drop=True),
        X_test_scaled,
        y_test.reset_index(drop=True)
    ],
    axis=1
)

train_output.to_parquet(PROCESSED / "train_features.parquet", index=False)
test_output.to_parquet(PROCESSED / "test_features.parquet", index=False)

joblib.dump(scaler, MODELS / "scaler.joblib")

report = f"""# Task 4 Split Summary

## Objective

Build feature matrix X and target y using cleaned polyhouse sensor data.  
A chronological train/test split was used to avoid data leakage.

## Feature Columns

- temperature_c
- humidity_pct
- co2_ppm

## Target Column

- yield_kg

## Split Method

The dataset was sorted by timestamp and split chronologically using an 80:20 ratio.

## Row Counts

- Total rows: {len(df)}
- Train rows: {len(X_train)}
- Test rows: {len(X_test)}

## Date Ranges

- Train start date: {train_dates.min()}
- Train end date: {train_dates.max()}
- Test start date: {test_dates.min()}
- Test end date: {test_dates.max()}

## Scaling

MinMaxScaler was fitted only on the training feature set.  
The test feature set was transformed using the scaler fitted on training data only.

## Leakage Prevention

No test data was used while fitting the scaler.
"""

with open(REPORTS / "split_report.md", "w", encoding="utf-8") as f:
    f.write(report)

print("Task 4 complete.")
print("Train rows:", len(X_train))
print("Test rows:", len(X_test))
print("Scaler saved -> models/scaler.joblib")
print("Train features saved -> data/processed/train_features.parquet")
print("Test features saved -> data/processed/test_features.parquet")
print("Split report saved -> reports/split_report.md")