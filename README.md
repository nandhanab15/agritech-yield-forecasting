# Agritech Yield Forecasting

## Problem Statement

This project focuses on agritech data analysis and yield forecasting. The goal is to build a data pipeline that processes agricultural sensor data such as temperature, humidity, and CO₂ levels to support crop yield prediction and decision-making in controlled farming environments like polyhouses.\# Environment Setup



\## Prerequisites



\* Python 3.10 or later

\* PowerShell (Windows)



\## Create and Activate Virtual Environment



```powershell

python -m venv venv

```



Activate the virtual environment:



```powershell

venv\\Scripts\\Activate.ps1

```



\## Install Dependencies



```powershell

pip install --upgrade pip

pip install pandas numpy matplotlib scikit-learn jupyter streamlit joblib

```



\## Verify Installation



```powershell

pip list

```



\## Run the Smoke Test



The smoke test verifies that the project environment is working correctly.



```powershell

python src\\smoke\_test.py

```



Expected output:



```text

Polyhouse sensor snapshot:

&#x20; date: YYYY-MM-DD

&#x20; temperature\_c: 22.4

&#x20; humidity\_pct: 88.5

&#x20; co2\_ppm: 950

&#x20; yield\_kg: 12.3

Environment OK.

```



\## Project Structure



```text

data/

├── raw/

└── processed/



models/

notebooks/

src/

```

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

