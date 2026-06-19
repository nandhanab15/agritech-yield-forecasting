\# Monitoring Plan



\## Objective



The purpose of monitoring is to track prediction activity, identify data drift, detect unusual prediction behavior, and determine when model retraining is required.



\## Prediction Logging



Each prediction request should record:



\* Timestamp (UTC)

\* Temperature (°C)

\* Humidity (%)

\* CO₂ concentration (ppm)

\* Predicted yield (kg)



Sample log format:



| timestamp\_utc             | temp\_c | humidity\_pct | co2\_ppm | predicted\_kg |

| ------------------------- | ------ | ------------ | ------- | ------------ |

| 2026-06-19T10:30:00+00:00 | 24.0   | 85.0         | 900     | 25.55        |



\## Input Drift Monitoring



Monitor environmental sensor values to ensure they remain similar to the data used during training.



Warning conditions:



\* Temperature consistently below 18°C or above 30°C

\* Humidity consistently below 75%

\* CO₂ consistently above 1500 ppm

\* Frequent values near slider limits



\## Prediction Drift Monitoring



Monitor prediction outputs over time.



Warning conditions:



\* Average predicted yield changes significantly

\* Predictions frequently exceed historical maximum yield

\* Predictions frequently fall below historical minimum yield



\## Concept Drift Scenarios



Possible causes of concept drift include:



\* Sensor recalibration or firmware updates

\* Seasonal environmental changes

\* Different mushroom substrate batches

\* Changes in irrigation or ventilation strategy

\* New cultivation methods



These changes may alter the relationship between environmental variables and yield.



\## Retraining Triggers



Model retraining should be considered when:



1\. New production data becomes available.

2\. Prediction error increases significantly.

3\. Input distributions differ from training data.

4\. New cultivation practices are introduced.

5\. Seasonal patterns change yield behavior.



\## Retraining Frequency



Recommended review schedule:



\* Weekly review of prediction logs

\* Monthly review of prediction trends

\* Full retraining every 3–6 months if new data is available



\## Iteration Roadmap



\### Improvement 1: Additional Features



Add more environmental variables such as:



\* Light intensity

\* Soil moisture

\* Airflow measurements



\### Improvement 2: Automated Retraining



Create a scheduled retraining pipeline that updates the model when sufficient new data is collected.



\### Improvement 3: Alerting System



Generate alerts when:



\* Predictions exceed historical maximum yield

\* Inputs fall outside recommended operating ranges

\* Large shifts in prediction distributions occur



\## Business Impact



Monitoring helps identify model degradation early and improves confidence in production forecasts. Effective monitoring reduces forecasting risk and supports more reliable farm planning decisions.



