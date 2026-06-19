import streamlit as st
import numpy as np
import pandas as pd
from src.logging_utils import log_prediction
try:
    from src.predict import predict_yield
except FileNotFoundError:
    st.error(
        "Model artifacts are missing. Please run the training pipeline before starting the app."
    )
    st.stop()


@st.cache_resource
def load_prediction_function():
    return predict_yield


predict_fn = load_prediction_function()

st.set_page_config(
    page_title="Mushroom Yield Forecast",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 Polyhouse Yield Predictor")
st.caption("Interactive mushroom yield forecasting from sensor readings")

st.sidebar.header("Sensor Readings")

temperature = st.sidebar.slider(
    "Temperature (°C)",
    min_value=18.0,
    max_value=30.0,
    value=24.0,
    step=0.1
)

humidity = st.sidebar.slider(
    "Humidity (%)",
    min_value=70.0,
    max_value=95.0,
    value=85.0,
    step=0.5
)

co2 = st.sidebar.slider(
    "CO₂ (ppm)",
    min_value=500,
    max_value=1500,
    value=900,
    step=10
)

st.markdown(
    """
    Use the sidebar controls to enter current polyhouse sensor readings.
    Click the prediction button to estimate daily mushroom yield.
    """
)

if humidity < 75:
    st.warning("Humidity is below the recommended mushroom growing range.")

if temperature < 20 or temperature > 28:
    st.warning("Temperature is outside the ideal cultivation range.")

if co2 < 600 or co2 > 1200:
    st.warning("CO₂ level is outside the typical operating range.")

if st.button("Predict Yield"):
    with st.spinner("Generating yield prediction..."):
        predicted_yield = predict_fn(temperature, humidity, co2)
    log_prediction(temperature, humidity, co2, predicted_yield)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Estimated Daily Yield",
            value=f"{predicted_yield:.2f} kg"
        )

    with col2:
        st.metric(
            label="Model Test MAE",
            value="0.28 kg"
        )

    st.success(
        f"The predicted mushroom yield is approximately "
        f"{predicted_yield:.2f} kg per day."
    )

st.subheader("What-if Analysis: Humidity Sweep")

humid_range = np.linspace(70, 98, 29)

predictions = [
    predict_fn(temperature, h, co2)
    for h in humid_range
]

chart_df = pd.DataFrame({
    "Humidity (%)": humid_range,
    "Predicted Yield (kg)": predictions
})

st.line_chart(
    chart_df,
    x="Humidity (%)",
    y="Predicted Yield (kg)"
)

with st.expander("Model Information"):
    st.markdown(
        """
        ### Champion Model

        Linear Regression

        ### Performance Summary

        - Test MAE: 0.2812 kg
        - Test RMSE: 0.3532 kg
        - Test R²: 0.9496

        ### Training Data

        - Data range: 2025-01-02 to 2027-09-27
        - Split method: Chronological 80/20 train-test split

        ### Version

        v0.1-model

        ### Reliability Note

        Predictions are most reliable within the sensor ranges used during training.
        This tool is advisory and should support, not replace, grower judgment.
        """
    )

st.markdown("---")

st.markdown(
    """
    ### Documentation

    Related project reports:

    - `reports/model_comparison.md`
    - `reports/eda_notes.md`
    - `reports/cv_results.md`
    - `reports/app_testing_validation.md`
    """
)