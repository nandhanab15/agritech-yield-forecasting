\---



\# Mushroom Yield Forecast



\## Zelbytes Agritech Capstone



\*\*Presented by:\*\* Nandhana B



\*\*AI Data Analyst (Beginner) Internship\*\*



\---



\# Problem Statement



\## Objective



Develop a machine learning system to predict daily mushroom yield using environmental sensor data collected from a polyhouse.



\## Why is this important?



\* Mushroom growth is highly sensitive to environmental conditions.

\* Manual yield estimation is often inaccurate.

\* Early yield prediction supports harvest planning and resource management.

\* Machine learning enables data-driven decision-making for precision agriculture.



\### Input Features



\* Temperature (°C)

\* Relative Humidity (%)

\* CO₂ Concentration (ppm)



\### Output



\* Predicted Daily Mushroom Yield (kg)



\---



\# Dataset



\## Data Source



The project used a simulated polyhouse dataset containing environmental sensor readings and mushroom yield values.



\### Features



| Feature     | Unit |

| ----------- | ---- |

| Temperature | °C   |

| Humidity    | %    |

| CO₂         | ppm  |

| Yield       | kg   |



\### Dataset Summary



\* Initial Records: \*\*1,025\*\*

\* Cleaned Records: \*\*926\*\*

\* Daily observations

\* Missing values and duplicates handled



\---



\# Data Pipeline



\## End-to-End Workflow



Raw Data



⬇



Data Ingestion



⬇



Data Cleaning



⬇



Exploratory Data Analysis (EDA)



⬇



Feature Engineering



⬇



Model Training



⬇



Model Comparison



⬇



Champion Model Selection



⬇



Streamlit Deployment



⬇



Monitoring \& Logging



\### Key Technologies



\* Python

\* Pandas

\* Scikit-learn

\* Streamlit

\* Git \& GitHub



\---



\# Exploratory Data Analysis (EDA)



\## Objectives



\* Understand relationships between environmental variables and mushroom yield.

\* Detect outliers and data quality issues.

\* Identify the most important predictor variables.



\### Key Findings



\* Humidity showed the strongest positive relationship with yield.

\* Temperature showed a moderate positive relationship with yield.

\* CO₂ had a weaker relationship but remained an important predictor.

\* Data cleaning improved overall dataset quality before model training.



\### Figures



\* Correlation Heatmap

\* Temperature vs Yield

\* Humidity vs Yield

\* CO₂ vs Yield



\---



\# Model Development



\## Models Evaluated



1\. Linear Regression

2\. Random Forest

3\. Tuned Random Forest (GridSearchCV)



\## Evaluation Metrics



\* Cross-Validation MAE

\* Test MAE

\* Test RMSE

\* Test R²



\## Champion Model



\*\*Linear Regression\*\*



\### Why it was selected



\* Lowest Test MAE (0.2812 kg)

\* Lowest Test RMSE (0.3532 kg)

\* Highest Test R² (0.9496)

\* High interpretability

\* Best overall performance on the unseen test dataset



\---



\# Results



\## Model Comparison



| Model               | Test MAE (kg) | Test RMSE (kg) |    Test R² |

| ------------------- | ------------: | -------------: | ---------: |

| Linear Regression   |    \*\*0.2812\*\* |     \*\*0.3532\*\* | \*\*0.9496\*\* |

| Random Forest       |        0.3597 |         0.4639 |     0.9131 |

| Tuned Random Forest |        0.3592 |         0.4550 |     0.9164 |



\## Final Model



✅ Champion Model: \*\*Linear Regression\*\*



Reason:



\* Highest accuracy

\* Lowest prediction error

\* Easy to interpret

\* Suitable for deployment



\---



\# Live Demo



\## Streamlit Application



Features demonstrated:



\* Temperature slider

\* Humidity slider

\* CO₂ slider

\* Instant yield prediction

\* Model information

\* Prediction logging



\### Live Deployment



https://agritech-yield-forecasting-k4n4so84ckvuh5jhfixbzq.streamlit.app/



\*(If internet is unavailable, show the Streamlit application screenshot from `reports/figures/streamlit\_app\_v2\_screenshot.png`.)\*



\---



\# Monitoring



\## Monitoring Strategy



Prediction logging includes:



\* Timestamp

\* Temperature

\* Humidity

\* CO₂

\* Predicted Yield



\### Retraining Triggers



\* Input drift

\* Concept drift

\* Increased prediction error

\* New production data

\* Seasonal changes



\---



\# Lessons Learned \& Future Work



\## Top Skills Learned



\* Data cleaning and preprocessing

\* Machine learning model development

\* Cloud deployment using Streamlit



\## Future Improvements



\* Collect real farm sensor data

\* Add more environmental features

\* Automate model retraining

\* Build monitoring dashboard

\* Improve drift detection



\---



\# Thank You



\## Thank You!



\### Repository



https://github.com/nandhanab15/agritech-yield-forecasting



\### Live Application



https://agritech-yield-forecasting-k4n4so84ckvuh5jhfixbzq.streamlit.app/



\### Questions?



