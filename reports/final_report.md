\# Mushroom Yield Forecast — Technical Report



\## Executive Summary



This project presents an end-to-end machine learning solution for forecasting daily oyster mushroom yield using environmental sensor data collected from a polyhouse environment. The objective was to predict daily mushroom yield from temperature (°C), relative humidity (%), and carbon dioxide (ppm) measurements, enabling growers to make informed cultivation and harvest planning decisions.



The project followed the complete machine learning lifecycle, including data ingestion, cleaning, exploratory data analysis, feature engineering, model development, hyperparameter tuning, deployment, and post-deployment monitoring. Three regression models were evaluated: Linear Regression, Random Forest, and Tuned Random Forest.



Based on comparative evaluation using Cross-Validation MAE, Test MAE, Test RMSE, Test R², and model interpretability, \*\*Linear Regression\*\* was selected as the champion model. It achieved the best predictive performance on the unseen test dataset with a \*\*Test MAE of 0.2812 kg\*\*, \*\*Test RMSE of 0.3532 kg\*\*, and \*\*Test R² of 0.9496\*\*. These results indicate that the model typically predicts daily mushroom yield within approximately \*\*0.28 kg\*\* of the actual value while maintaining excellent explanatory capability.



The final model was integrated into a Streamlit web application that allows users to estimate mushroom yield interactively by adjusting environmental sensor values. The application was successfully deployed on Streamlit Community Cloud, enabling public access without requiring users to install Python or machine learning libraries.



To support long-term reliability, lightweight prediction logging, monitoring strategies, drift detection guidelines, and retraining triggers were documented. Together, these components provide a complete demonstration of a production-oriented machine learning workflow for agritech applications.



\*\*Live Application:\*\*

https://agritech-yield-forecasting-k4n4so84ckvuh5jhfixbzq.streamlit.app/



\## 1. Problem Statement and Agritech Context



Mushroom cultivation requires precise control of environmental conditions to achieve consistent yield and product quality. Factors such as temperature, relative humidity, and carbon dioxide concentration directly influence mushroom growth, making continuous environmental monitoring essential for successful production. However, estimating daily yield manually can be difficult because multiple environmental variables interact simultaneously.



The objective of this project was to develop a machine learning model capable of predicting daily oyster mushroom yield using environmental sensor data collected from a polyhouse environment. The predicted yield can assist growers in planning harvest operations, labor allocation, inventory management, and market supply while reducing uncertainty in production.



The project followed a complete machine learning workflow beginning with data generation and ingestion, followed by data cleaning, exploratory data analysis, feature engineering, model development, hyperparameter tuning, model evaluation, deployment, and monitoring. The final prediction model was integrated into a Streamlit web application, allowing users to estimate mushroom yield through an interactive interface.



This project demonstrates how machine learning can support precision agriculture by converting environmental sensor readings into actionable yield forecasts. The resulting application serves as a decision-support tool for growers while also illustrating a production-ready machine learning workflow suitable for agritech applications.



\## 2. Data Sources and Cleaning



The dataset used in this project consisted of environmental sensor readings collected from a simulated mushroom polyhouse. The data represented daily growing conditions and corresponding mushroom yield, providing a realistic dataset for developing and evaluating machine learning models.



\### Dataset Description



The dataset contained the following variables:



| Feature       | Unit      | Description                          |

| ------------- | --------- | ------------------------------------ |

| timestamp     | Date/Time | Date of sensor observation           |

| temperature\_c | °C        | Air temperature inside the polyhouse |

| humidity\_pct  | %         | Relative humidity                    |

| co2\_ppm       | ppm       | Carbon dioxide concentration         |

| yield\_kg      | kg        | Daily mushroom yield                 |



The initial dataset contained \*\*1,025 observations\*\*, including intentionally introduced missing values, duplicate records, and invalid sensor readings to simulate real-world data quality issues.



\### Data Cleaning Process



A dedicated data cleaning pipeline was implemented to improve data quality before model development. The following preprocessing steps were performed:



\* Parsed timestamps into the appropriate datetime format.

\* Removed duplicate observations while retaining the latest valid record.

\* Identified and handled missing sensor values using controlled forward-fill operations.

\* Removed observations containing invalid environmental measurements outside acceptable operating ranges.

\* Verified data types and ensured consistency across all columns.

\* Preserved the target variable (`yield\_kg`) without artificial imputation.



After preprocessing, the cleaned dataset contained \*\*926 valid observations\*\*, which were used for all subsequent exploratory analysis, feature engineering, and machine learning tasks.



\### Data Quality Summary



The cleaning process successfully removed inconsistent records while preserving realistic environmental variation. The resulting dataset provided a reliable foundation for model training and evaluation, reducing the likelihood of biased predictions caused by missing values or erroneous sensor measurements.



\## 3. Exploratory Data Analysis



Exploratory Data Analysis (EDA) was performed to understand the distribution of environmental variables, identify relationships with mushroom yield, detect potential outliers, and support feature selection for model development. Summary statistics, correlation analysis, and visualization techniques were used to gain insights into the dataset before training machine learning models.



\### Data Quality Assessment



The cleaned dataset was reviewed to verify its overall quality and suitability for modeling. Summary statistics confirmed that temperature, humidity, CO₂ concentration, and yield values were within realistic operating ranges after preprocessing. Missing values and duplicate records had been successfully removed during the cleaning stage.



\### Correlation Analysis



The correlation heatmap was generated to examine relationships among the variables.



!\[Correlation Heatmap](figures/corr\_heatmap.png)



\*\*Figure 1. Correlation Heatmap:\*\* This figure illustrates the strength and direction of relationships between environmental variables and mushroom yield. It helps identify which features are most informative for prediction and supports the selection of input variables for the machine learning models.



\### Temperature vs Yield



A scatter plot was used to examine the relationship between temperature and mushroom yield.



!\[Temperature vs Yield](figures/temperature\_vs\_yield.png)



\*\*Figure 2. Temperature vs Yield:\*\* The plot indicates a generally positive relationship between temperature and yield within the observed cultivation range. Maintaining stable temperatures can contribute to more consistent mushroom production.



\### Humidity vs Yield



Humidity was analyzed because it plays a critical role in mushroom growth.



!\[Humidity vs Yield](figures/humidity\_vs\_yield.png)



\*\*Figure 3. Humidity vs Yield:\*\* Higher humidity levels generally correspond to improved mushroom yield. The plot supports the importance of maintaining adequate humidity inside the polyhouse to promote healthy crop development.



\### CO₂ vs Yield



The relationship between carbon dioxide concentration and yield was also examined.



!\[CO₂ vs Yield](figures/co2\_vs\_yield.png)



\*\*Figure 4. CO₂ vs Yield:\*\* CO₂ concentration showed a weaker relationship with yield than temperature and humidity. However, maintaining appropriate ventilation remains important because excessive CO₂ levels may negatively affect crop growth.



\### Key Insights



The exploratory analysis produced several important observations:



\* Humidity showed the strongest positive relationship with mushroom yield.

\* Temperature demonstrated a moderate positive relationship with yield.

\* CO₂ concentration had a weaker but still relevant influence on production.

\* Most observations were concentrated within realistic environmental ranges after data cleaning.

\* The observed relationships justified retaining temperature, humidity, and CO₂ as the primary predictor variables for model development.



\## 4. Feature Engineering and Validation Strategy



Feature engineering was performed to improve the predictive capability of the machine learning models while preserving the interpretability of the environmental variables. The objective was to transform the raw sensor readings into a format suitable for model training and evaluation.



\### Feature Engineering



The primary predictor variables used in this project were:



\* Temperature (°C)

\* Relative Humidity (%)

\* Carbon Dioxide (ppm)



To capture the interaction between environmental conditions, an additional feature representing the interaction between temperature and humidity was created. This feature helps the model learn how the combined effect of these variables influences mushroom yield rather than considering them independently.



The dataset was then prepared for modeling by applying feature scaling using the MinMaxScaler. Scaling ensured that numerical variables were transformed to a consistent range, improving numerical stability during model training and maintaining compatibility with the saved preprocessing pipeline.



\### Validation Strategy



A chronological train-test split was used instead of a random split because the dataset represents time-series observations. Using a temporal split better reflects real-world deployment, where models are trained using historical data and make predictions on future observations.



The dataset was divided into:



\* \*\*Training Set (80%)\*\* – Used for feature engineering, model training, and hyperparameter tuning.

\* \*\*Test Set (20%)\*\* – Reserved exclusively for final model evaluation.



To further improve model selection, \*\*TimeSeriesSplit cross-validation\*\* was used during hyperparameter tuning of the Random Forest model. This validation approach preserves the chronological order of observations and reduces the risk of information leakage between training and validation folds.



\### Importance of Temporal Validation



A temporal validation strategy provides a more realistic estimate of model performance because future observations are never used during training. This approach is particularly important in agritech forecasting applications where environmental conditions evolve over time. Using chronological validation increases confidence that the deployed model will generalize effectively to future growing conditions.



\## 5. Models Evaluated



Three regression models were developed and evaluated to identify the most suitable approach for predicting daily mushroom yield from environmental sensor data. Each model was trained using the same training dataset and evaluated on the same untouched test dataset to ensure a fair comparison.



\### Linear Regression



Linear Regression was selected as the baseline model because it is simple, computationally efficient, and highly interpretable. The model estimates the relationship between environmental variables and mushroom yield using a linear equation, making it easy to explain how each feature contributes to the final prediction.



\### Random Forest



Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve predictive performance. Unlike Linear Regression, Random Forest can model nonlinear relationships and interactions between environmental variables without requiring explicit feature transformations.



Feature importance analysis was also performed to identify which environmental variables contributed most to the prediction process.



\### Tuned Random Forest



To improve Random Forest performance, hyperparameter optimization was performed using \*\*GridSearchCV\*\* with \*\*TimeSeriesSplit cross-validation\*\*.



The tuning process evaluated combinations of:



\* Number of decision trees (`n\_estimators`)

\* Maximum tree depth (`max\_depth`)

\* Minimum samples per leaf (`min\_samples\_leaf`)



The best-performing parameter combination was selected based on the lowest cross-validation Mean Absolute Error (MAE). The tuned model was then evaluated on the untouched test dataset and compared with the other models.



\### Evaluation Criteria



All three models were compared using the following performance metrics:



\* Cross-Validation Mean Absolute Error (CV MAE)

\* Test Mean Absolute Error (Test MAE)

\* Test Root Mean Squared Error (Test RMSE)

\* Test Coefficient of Determination (Test R²)

\* Model Interpretability



Among these metrics, \*\*Mean Absolute Error (MAE)\*\* was considered the most important because it directly represents the average prediction error in kilograms of mushroom yield, making it meaningful for practical agritech decision-making.



\## 6. Results and Champion Model Selection



After training and evaluating all candidate models, a comprehensive comparison was performed using both cross-validation and hold-out test metrics. The objective was to select a model that achieved high predictive accuracy while remaining reliable and interpretable for agritech decision support.



\### Model Comparison



The following evaluation metrics were used:



\* Cross-Validation Mean Absolute Error (CV MAE)

\* Test Mean Absolute Error (Test MAE)

\* Test Root Mean Squared Error (Test RMSE)

\* Test Coefficient of Determination (Test R²)

\* Model Interpretability



The final comparison is shown below.



| Model               | CV MAE (kg) | Test MAE (kg) | Test RMSE (kg) | Test R² | Interpretability                        |

| :------------------ | ----------: | ------------: | -------------: | ------: | :-------------------------------------- |

| Linear Regression   |      0.2983 |        0.2812 |         0.3532 |  0.9496 | High – coefficients are easy to explain |

| Random Forest       |      0.3922 |        0.3597 |         0.4639 |  0.9131 | Medium – feature importance available   |

| Tuned Random Forest |      0.3727 |        0.3592 |         0.4550 |  0.9164 | Medium – tuned model is more complex    |



\### Champion Model



Based on the evaluation results, \*\*Linear Regression\*\* was selected as the champion model for deployment.



Although both Random Forest models were capable of modelling nonlinear relationships, Linear Regression consistently achieved better predictive performance on the unseen test dataset. It produced the \*\*lowest Test MAE (0.2812 kg)\*\*, \*\*lowest Test RMSE (0.3532 kg)\*\*, and \*\*highest Test R² (0.9496)\*\* among all evaluated models.



In addition to its superior predictive performance, Linear Regression provides excellent interpretability. Its coefficients directly describe how changes in temperature, humidity, carbon dioxide concentration, and engineered interaction features influence the predicted mushroom yield. This level of transparency makes the model particularly suitable for growers and stakeholders who require understandable decision-support tools.



\### Agritech Interpretation



For mushroom cultivation, Mean Absolute Error (MAE) is a practical performance metric because it is measured directly in kilograms of yield. A \*\*Test MAE of 0.2812 kg\*\* indicates that the model's predictions differ from the actual daily mushroom yield by approximately \*\*0.28 kg on average\*\*. This level of accuracy is sufficient to support harvest planning, labor scheduling, and production management within the context of the available dataset.



\### Predicted vs Actual Performance



!\[Predicted vs Actual Yield](figures/pred\_vs\_actual.png)



\*\*Figure 5. Predicted vs Actual Yield:\*\* The predicted-versus-actual plot demonstrates that most predictions lie close to the ideal diagonal line, indicating strong agreement between predicted and observed mushroom yields. This visualization confirms the overall accuracy and consistency of the selected Linear Regression model on the unseen test dataset.



\### Final Recommendation



Based on predictive accuracy, cross-validation stability, model simplicity, and interpretability, \*\*Linear Regression\*\* was selected as the final production model. It provides the best balance between performance and explainability and was therefore deployed within the Streamlit application for real-time mushroom yield prediction.



\## 7. Streamlit Application and Cloud Deployment



To make the prediction model accessible to non-technical users, the selected Linear Regression model was integrated into a Streamlit web application. The application provides an intuitive interface that allows users to enter environmental sensor values and receive an instant prediction of the expected daily mushroom yield.



\### Application Features



The Streamlit application includes the following functionality:



\* Interactive sliders for temperature (°C), humidity (%), and CO₂ concentration (ppm).

\* Real-time mushroom yield prediction in kilograms.

\* Model metadata displaying the deployed model and evaluation metrics.

\* Input validation with warnings for values outside the recommended operating range.

\* Loading spinner during prediction generation.

\* Friendly error messages if model artifacts are unavailable.

\* Prediction logging for monitoring future model performance.

\* Responsive interface suitable for demonstration and stakeholder evaluation.



\### User Interface



The final application interface is shown below.



!\[Streamlit Application](figures/streamlit\_app\_v2\_screenshot.png)



\*\*Figure 6. Streamlit Application:\*\* The deployed application enables users to estimate mushroom yield by adjusting environmental sensor values without requiring programming knowledge. The interface is designed to provide quick predictions while displaying relevant model information.



\### Cloud Deployment



The application was deployed using \*\*Streamlit Community Cloud\*\*, allowing the forecasting system to be accessed through a web browser without local installation.



Deployment involved the following steps:



1\. Pushing the latest application code, model artifacts, and dependencies to the GitHub repository.

2\. Configuring `app.py` as the Streamlit entry point.

3\. Installing dependencies from `requirements.txt`.

4\. Verifying that cloud predictions matched local predictions.

5\. Updating the project documentation with the deployment URL.



\### Public Deployment



\*\*GitHub Repository\*\*



https://github.com/nandhanab15/agritech-yield-forecasting



\*\*Live Streamlit Application\*\*



https://agritech-yield-forecasting-k4n4so84ckvuh5jhfixbzq.streamlit.app/



\### Deployment Validation



To ensure consistency between local development and the deployed application, identical environmental inputs were supplied to both the local prediction script and the cloud-hosted application.



Validation Input:



| Temperature (°C) | Humidity (%) | CO₂ (ppm) |

| ---------------: | -----------: | --------: |

|             24.0 |         85.0 |       900 |



Both the local application and the deployed Streamlit application produced the same prediction:



\*\*Predicted Yield:\*\* \*\*25.55 kg\*\*



This validation confirmed that the deployed application uses the same preprocessing pipeline, trained model, and inference logic as the local development environment.



\## 8. Monitoring and Future Iterations



Deploying a machine learning model is not the final stage of the project. Continuous monitoring is essential to ensure that the prediction system remains reliable as new environmental data becomes available. A lightweight monitoring strategy was developed to support model maintenance, identify performance degradation, and guide future improvements.



\### Prediction Logging



A structured prediction logging system was implemented to record every inference request generated by the application. Each prediction entry contains the following information:



\* Timestamp (UTC)

\* Temperature (°C)

\* Relative Humidity (%)

\* Carbon Dioxide Concentration (ppm)

\* Predicted Mushroom Yield (kg)



These logs allow prediction behaviour to be reviewed over time without storing personally identifiable information.



\### Monitoring Strategy



The monitoring plan focuses on identifying changes in both input data and prediction behaviour.



\*\*Input Drift Monitoring\*\*



The following conditions should be monitored regularly:



\* Temperature values outside the normal cultivation range.

\* Humidity values significantly lower or higher than historical observations.

\* Unusual CO₂ concentration patterns.

\* Sensor values consistently approaching the limits of the training data.



\*\*Prediction Drift Monitoring\*\*



Prediction outputs should also be monitored for abnormal behaviour, including:



\* Predictions exceeding historical maximum yield.

\* Predictions consistently below historical minimum yield.

\* Significant shifts in average predicted yield over time.

\* Sudden increases in prediction variability.



\### Concept Drift



Concept drift occurs when the relationship between environmental conditions and mushroom yield changes over time. Possible causes include:



\* Sensor recalibration or firmware updates.

\* Seasonal environmental variation.

\* New substrate batches.

\* Changes in irrigation practices.

\* Modified ventilation strategies.

\* Different mushroom cultivation methods.



Monitoring these factors helps determine whether the deployed model continues to represent current growing conditions.



\### Retraining Strategy



The model should be reviewed and retrained whenever one or more of the following conditions occur:



\* Availability of new production data.

\* Significant increase in prediction error.

\* Persistent input drift.

\* Evidence of concept drift.

\* Changes in cultivation practices or environmental control systems.



Regular reviews of prediction logs and performance metrics help maintain prediction accuracy throughout the model lifecycle.



\### Future Improvements



Several enhancements have been identified for future versions of the forecasting system:



1\. \*\*Additional Environmental Features\*\*

&#x20;  Incorporate variables such as light intensity, substrate moisture, airflow, and soil conditions to improve predictive accuracy.



2\. \*\*Automated Model Retraining\*\*

&#x20;  Develop an automated retraining pipeline that periodically updates the model using newly collected production data.



3\. \*\*Alert and Notification System\*\*

&#x20;  Generate warnings when sensor readings move outside expected operating ranges or when predicted yield exceeds historical limits.



4\. \*\*Real Farm Data Integration\*\*

&#x20;  Replace simulated training data with production sensor data collected from commercial mushroom farms.



5\. \*\*Advanced Monitoring Dashboard\*\*

&#x20;  Create an administrative dashboard for visualizing prediction logs, monitoring drift, and tracking long-term model performance.



The monitoring framework and future roadmap provide a foundation for maintaining and continuously improving the deployed machine learning system.



\## 9. Limitations



Although the developed forecasting system demonstrated strong predictive performance, several limitations should be acknowledged.



The dataset used for model development was synthetically generated to simulate realistic polyhouse environmental conditions. While this approach enabled systematic experimentation and model evaluation, the resulting model may not capture all complexities of real commercial mushroom farms.



Only three environmental variables—temperature, relative humidity, and carbon dioxide concentration—were used as primary predictors. Other factors such as substrate quality, irrigation frequency, light intensity, airflow, disease occurrence, and nutrient availability can also influence mushroom yield but were not included in the current dataset.



The deployed Linear Regression model assumes predominantly linear relationships between environmental variables and mushroom yield. Although this assumption performed well for the available dataset, more complex nonlinear relationships may exist under different cultivation conditions.



The prediction model is most reliable when input values remain within the environmental ranges represented in the training dataset. Predictions generated for extreme temperature, humidity, or CO₂ values should therefore be interpreted cautiously.



Finally, the application is intended to support decision-making rather than replace grower expertise. Environmental recommendations and harvest planning should always consider additional operational knowledge beyond machine learning predictions.



\---



\# Appendix – Reproduction Commands



The following commands allow the complete project workflow to be reproduced from a fresh environment.



\## 1. Create Virtual Environment



```powershell

python -m venv venv

```



\## 2. Activate Virtual Environment



```powershell

venv\\Scripts\\Activate.ps1

```



\## 3. Install Dependencies



```powershell

pip install -r requirements.txt

```



\## 4. Data Pipeline



```powershell

python src\\ingest.py

python src\\clean.py

```



\## 5. Model Training



```powershell

python src\\train\_linear.py

python src\\train\_random\_forest.py

python src\\tune\_random\_forest.py

python src\\compare\_models.py

```



\## 6. Run Prediction Tests



```powershell

pytest tests/

```



Expected output:



```text

=============================

2 passed

=============================

```



\## 7. Launch Streamlit Application



```powershell

streamlit run app.py

```



\## 8. Deployment



The deployed application is available at:



\*\*https://agritech-yield-forecasting-k4n4so84ckvuh5jhfixbzq.streamlit.app/\*\*



The project source code is available at:



\*\*https://github.com/nandhanab15/agritech-yield-forecasting\*\*



\---



\# Conclusion



This project successfully demonstrated the complete machine learning lifecycle for mushroom yield forecasting using environmental sensor data. Beginning with data generation and preprocessing, the project progressed through exploratory analysis, feature engineering, model development, hyperparameter tuning, model evaluation, deployment, and post-deployment monitoring.



Three regression models were evaluated, with \*\*Linear Regression\*\* selected as the champion model based on its superior predictive accuracy, low Mean Absolute Error, high coefficient of determination, and excellent interpretability. The final model was integrated into a Streamlit web application and deployed to the cloud, providing an accessible interface for real-time yield prediction.



Beyond model development, the project incorporated software engineering best practices including automated testing, prediction logging, monitoring planning, deployment documentation, and reproducibility guidelines. These additions improve maintainability and demonstrate readiness for future expansion.



Future work should focus on collecting real production data, incorporating additional environmental variables, automating model retraining, and implementing advanced monitoring capabilities. Overall, this project provides a practical demonstration of how machine learning can support precision agriculture by transforming environmental sensor data into actionable yield forecasts for mushroom cultivation.







