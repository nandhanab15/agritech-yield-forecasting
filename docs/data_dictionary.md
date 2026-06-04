\# Data Dictionary



\## Polyhouse Sensor Dataset



This document describes the columns present in the `polyhouse\_sensors.csv` dataset used for mushroom yield analysis.



| Column Name   | Description                                        | Unit                    |

| ------------- | -------------------------------------------------- | ----------------------- |

| timestamp     | Date and time when the sensor reading was recorded | Datetime                |

| temperature\_c | Temperature inside the polyhouse environment       | Degrees Celsius (°C)    |

| humidity\_pct  | Relative humidity inside the polyhouse             | Percent (%)             |

| co2\_ppm       | Carbon dioxide concentration inside the polyhouse  | Parts Per Million (ppm) |

| yield\_kg      | Harvested mushroom yield                           | Kilograms (kg)          |



\## Agritech Significance



\### temperature\_c



Temperature affects the metabolic rate and growth conditions of mushrooms. Large temperature variations can impact yield and flush timing.



\### humidity\_pct



Humidity supports fruiting body development and helps maintain suitable growing conditions for mushrooms.



\### co2\_ppm



Carbon dioxide concentration influences ventilation requirements. Elevated CO₂ levels can negatively affect oyster mushroom yield.



\### yield\_kg



Yield represents the harvested mushroom production and serves as the target variable for analysis and future predictive modeling.



\## Dataset Source



The dataset was synthetically generated for internship training purposes and contains daily polyhouse sensor readings along with corresponding mushroom yield values.



