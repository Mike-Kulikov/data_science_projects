# Predicting a Biological Response #

## Table of contents 

[1. Project description](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%205.%20Predicting%20a%20Biological%20Response#project-description)

[2. What case do we solve?](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%205.%20Predicting%20a%20Biological%20Response#what-case-do-we-solve)

[3. Data overview](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%205.%20Predicting%20a%20Biological%20Response#data-overview)

[4. Project stages](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%205.%20Predicting%20a%20Biological%20Response#project-stages)

[5. Results](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%205.%20Predicting%20a%20Biological%20Response#results)


## Project description

A representative of a large real-estate agency has approached us with the following problem:

<i>“My realtors spend a disastrous amount of time sorting listings and looking for great deals. Therefore, their reaction speed, and, frankly speaking, the quality of the analysis does not reach the level of our competitors. This affects our financial performance.

Your task is to develop a model that would allow us to beat competitors in terms of the speed and quality of transactions."</i>

The objective of the project is to develop a service for predicting the cost of properties based on the history of offers.

## What case do we solve?

We are given with a dataset representing properties listed in the US. The objectives are:

- Clean the dataset
- Oplimise the features for the neads of the project
- Create a number of machine-learning models to predict price using the given features

## Data overview

The full dataset is [here](https://drive.google.com/file/d/11-ZNNIdcQ7TbT8Y0nsQ3Q0eiYQP__NIW/view?usp=share_link).

There are 377,185 lines representing different properties and 18 columns describing their features.

Each property has the following features:
1. status
2. private pool
3. propertyType
4. street
5. baths
6. homeFacts
7. fireplace
8. city
9. schools
10. sqft
11. zipcode
12. beds
13. state
14. stories
15. mls-id
16. PrivatePool
17. MlsId
18. target - price of the property, the predicting value

## Project stages

The project consists of the following parts:

- 1) Project Overview
- 2) Explonatory Data Analysis - Part 1
    * Data Overview
- 3) Feature Engeneering
    * target
    * status
    * private pool & PrivatePool
    * propertyType
    * street
    * baths
    * homeFacts
        - remodeled year
        - heating,
        - cooling,
        - parking
        - lotsize
    * fireplace
    * city
    * schools
        - schools rating
        - schools distance
    * sqft
    * beds
    * stories
    * year built
    * price/sq.ft. & lot_size & sqft
- 4) Baseline
    * Prepare the data
    * Evaluation metrics
    * Linear Regression
- 5) Explonatory Data Analysis - Part 2
    * Categorical features
    * Removing outliers
    * Correlation heat map
    * Encoding categorical features
- 6) Modeling
    * Linear Regression
    * Light Gradient Boosted Machine Regressor
    * Gradient Boosting
    * Extreme Gradient Boosting
    * Random Forest
    * Stacking Regressor
- 7) Results
    * Conclusion
        
## Results

The code is displayed in <a href="https://github.com/Mike-Kulikov/sf_data_science/blob/main/Project%205.%20Predicting%20a%20Biological%20Response/Project%205%20-%20Predicting%20a%20Biological%20Response.ipynb" target="_blank" rel="noopener">the following file</a>

1. The best results are shown by the **Random Forest Regressor** model. The Mean Absolute Error became **$59,434.88**, which is quite a lot. The Mean Absolute Percent Error is **15.47%**. The R^2 score (coefficient of determination) shows a relatively good **0.85** (on a scale from -1 to 1).

2. Overall, the original dataset has a lot of issues and inconsistencies. Cleaning and unwrapping of these issues were one of the main objectives of this project, which was accomplished successfully.

3. Another objective of this project was to demonstrate different machine-learning algorithms. The hyperparameters for all models were found using **Optuna**, a hyperparameter optimization framework. We left these calculations outside this Notebook as they are quite time-consuming.
