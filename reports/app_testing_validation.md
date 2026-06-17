\# App Testing, Validation and UX Polish



\## Objective



The objective was to validate the Streamlit yield prediction app before deployment by testing realistic sensor scenarios, checking prediction sanity, verifying CLI and UI parity, and improving user experience.



\## Test Scenarios



| Scenario | Temperature (°C) | Humidity (%) | CO2 (ppm) | Expected Sanity |

|---|---:|---:|---:|---|

| Optimal growing condition | 24.0 | 85.0 | 900 | Prediction should be realistic and within expected yield range |

| Dry spell | 24.0 | 72.0 | 900 | App should show humidity warning |

| Heat spike | 29.0 | 85.0 | 900 | App should show temperature warning |

| High CO2 condition | 24.0 | 85.0 | 1300 | App should show CO2 warning |

| Combined stress condition | 29.0 | 72.0 | 1300 | App should show multiple warnings |



\## Parity Check



The Streamlit app and command-line prediction use the same helper function:



`predict\_yield(temperature, humidity, co2)`



Example CLI command:



`python src\\predict.py`



Example CLI output:



`Predicted yield: 25.55 kg`



The Streamlit app also returns the same value for:



\- Temperature: 24.0 °C

\- Humidity: 85.0 %

\- CO2: 900 ppm



Expected matching output:



`25.55 kg`



\## UX Improvements



The app was polished with:



\- Page icon

\- Loading spinner during prediction

\- User-friendly warning messages

\- Consistent kg formatting

\- Model metadata expander

\- Humidity sensitivity chart



\## Missing Artifact Handling



The app includes defensive error handling. If model artifacts are missing, the user receives a friendly error message instead of a Python traceback.



\## Pytest Validation



Prediction tests were added in:



`tests/test\_predict.py`



The tests check that:



\- prediction output is a float

\- prediction is within a sensible kg range

\- different sensor inputs produce different predictions



Pytest result:



`2 passed`

