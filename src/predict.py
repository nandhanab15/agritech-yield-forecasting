from pathlib import Path
import json
import joblib
import pandas as pd

MODEL_DIR = Path("models")

MODEL_PATH = MODEL_DIR / "linear_regression.joblib"
SCALER_PATH = MODEL_DIR / "scaler.joblib"
FEATURE_COLS_PATH = MODEL_DIR / "feature_cols.json"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
feature_config = json.loads(FEATURE_COLS_PATH.read_text(encoding="utf-8"))

raw_feature_cols = feature_config["raw_feature_cols"]
model_feature_cols = feature_config["model_feature_cols"]


def make_prediction(temperature: float, humidity: float, co2: float) -> float:
    temp_humid_interaction = temperature * humidity / 100

    raw_row = pd.DataFrame(
        [[
            temperature,
            humidity,
            co2,
            temp_humid_interaction,
            temperature,
            humidity,
            co2,
            temperature,
            humidity,
            co2,
        ]],
        columns=raw_feature_cols,
    )

    scaled_values = scaler.transform(raw_row)

    all_scaled_cols = [col + "_scaled" for col in raw_feature_cols]

    scaled_row_all = pd.DataFrame(
        scaled_values,
        columns=all_scaled_cols,
    )

    model_input = scaled_row_all[model_feature_cols]

    prediction = model.predict(model_input)[0]

    return round(float(prediction), 2)


def predict_yield(temperature_c: float, humidity_pct: float, co2_ppm: float) -> float:
    return make_prediction(temperature_c, humidity_pct, co2_ppm)


if __name__ == "__main__":
    result = make_prediction(24.0, 85.0, 900.0)
    print(f"Predicted yield: {result} kg")