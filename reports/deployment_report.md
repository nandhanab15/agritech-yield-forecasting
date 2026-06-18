\# Cloud Deployment Report



\## Objective



The objective of this task was to deploy the Streamlit mushroom yield prediction app to a public cloud platform so mentors and stakeholders can access the application through a live URL.



\## Deployment Platform



Platform: Streamlit Community Cloud



\## Repository



GitHub Repository:



https://github.com/nandhanab15/agritech-yield-forecasting



\## Deployment Configuration



\- Branch: main

\- Main file path: app.py

\- Python version: python-3.11

\- Runtime file: runtime.txt

\- Dependencies file: requirements.txt



\## Required Model Artifacts



The app loads the following model artifacts from the repository:



\- models/linear\_regression.joblib

\- models/scaler.joblib

\- models/feature\_cols.json



These files are tracked in Git and available in the GitHub repository.



\## Local Test Prediction



Local command:



python src\\predict.py



Local output:



Predicted yield: 25.55 kg



Test input:



\- Temperature: 24.0 °C

\- Humidity: 85.0 %

\- CO2: 900 ppm



\## Cloud Deployment URL



To be added after successful deployment.



\## Cloud Prediction Validation



To be completed after successful deployment.



Expected cloud test input:



\- Temperature: 24.0 °C

\- Humidity: 85.0 %

\- CO2: 900 ppm



Expected cloud output:



25.55 kg



\## Notes



The first deployment failed because Streamlit Cloud attempted to use Python 3.14. A `runtime.txt` file was added to request Python 3.11 for better compatibility with pinned ML dependencies.



\## Deployment Status



In progress.

