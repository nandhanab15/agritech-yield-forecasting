\# Monitoring Plan



\## Objective



This document describes the lightweight monitoring plan for the deployed mushroom yield forecasting application.



The goal is to track prediction usage, detect unusual inputs, monitor prediction behavior, and define when the model should be retrained.



\## Deployment Information



Platform: Streamlit Community Cloud



Live App URL:



https://agritech-yield-forecasting-k4n4so84ckvuh5jhfixbzq.streamlit.app/



Main app file:



app.py



\## Model Artifact Handling



The deployed application loads model artifacts directly from the GitHub repository.



Required artifacts:



\- models/linear\_regression.joblib

\- models/scaler.joblib

\- models/feature\_cols.json



These artifacts are committed to the repository and are available during cloud deployment.



No external download step is required.



\## Dependency Handling



The cloud deployment uses `requirements.txt` to install required Python packages.



Critical packages include:



\- streamlit

\- pandas

\- numpy

\- scikit-learn

\- joblib

\- matplotlib

\- pyarrow



\## Prediction Logging Plan



For lightweight monitoring, each prediction event should record the following fields:



| Field | Description |

|---|---|

| timestamp | Date and time of prediction |

| temperature\_c | Input temperature in Celsius |

| humidity\_pct | Input humidity percentage |

| co2\_ppm | Input CO2 concentration |

| predicted\_yield\_kg | Model prediction in kilograms |

| warning\_flags | Any input warning shown to user |

| model\_version | Version of deployed model |



\## Example Prediction Log



| timestamp | temperature\_c | humidity\_pct | co2\_ppm | predicted\_yield\_kg | warning\_flags | model\_version |

|---|---:|---:|---:|---:|---|---|

| 2026-06-18 13:30:00 | 24.0 | 85.0 | 900 | 25.55 | none | v0.1-model |

| 2026-06-18 13:35:00 | 29.0 | 72.0 | 1300 | sample\_prediction | temperature\_warning, humidity\_warning, co2\_warning | v0.1-model |



\## Monitoring Checks



The following checks should be reviewed regularly:



1\. Input Drift



Compare new user inputs with the training sensor ranges.



Warning signs:



\- Temperature frequently below 20°C or above 28°C

\- Humidity frequently below 75%

\- CO2 frequently below 600 ppm or above 1200 ppm



2\. Prediction Drift



Monitor whether predicted yield values move outside the expected range.



Warning signs:



\- Very low predicted yield values

\- Very high predicted yield values

\- Sudden shifts in average predicted yield



3\. Data Quality Issues



Monitor unrealistic or invalid inputs.



Examples:



\- Humidity near the minimum or maximum slider range repeatedly

\- CO2 values consistently outside typical operating range

\- Inputs that do not reflect actual farm conditions



\## Retrain Triggers



The model should be retrained when one or more of the following conditions occur:



\- New real farm data becomes available.

\- Prediction error increases beyond the current test MAE benchmark.

\- Input sensor distributions shift significantly from training data.

\- New seasonal patterns appear in production data.

\- Farm equipment, ventilation, or cultivation process changes.

\- Actual yield feedback shows consistent overprediction or underprediction.



\## Retraining Frequency



Initial recommendation:



\- Review prediction logs weekly.

\- Review actual vs predicted yield monthly if real yield data is available.

\- Retrain the model every 3 to 6 months or whenever strong drift is detected.



\## Current Model Baseline



Champion model:



Linear Regression



Model version:



v0.1-model



Test metrics:



\- Test MAE: 0.2812 kg

\- Test RMSE: 0.3532 kg

\- Test R2: 0.9496



\## Notes



The deployed model is intended as a decision-support tool. It should support farm managers but should not replace grower judgment.



All future monitoring should consider agronomic context, real farm conditions, and sensor reliability.

