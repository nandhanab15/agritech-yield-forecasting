import streamlit as st

from src.predict import predict_yield


@st.cache_resource
def load_prediction_function():
    return predict_yield


predict_fn = load_prediction_function()

st.set_page_config(
    page_title="Mushroom Yield Forecast",
    layout="centered"
)

st.title("Polyhouse Yield Predictor")
st.caption("Agritech mushroom yield forecasting from sensor readings")

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

st.write("Adjust the sensor readings in the sidebar and click the button to estimate daily mushroom yield.")

if st.button("Predict Yield"):
    predicted_yield = predict_fn(temperature, humidity, co2)

    st.metric(
        label="Estimated Daily Yield",
        value=f"{predicted_yield:.2f} kg"
    )

    st.success("Prediction generated successfully.")

st.info(
    "This tool provides an advisory estimate based on the trained model. "
    "Predictions are most reliable within the sensor ranges used during training."
)