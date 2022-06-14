# Predicting a Biological Response #

## Table of contents 

[1. Project description](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%205.%20Predicting%20a%20Biological%20Response#project-description)

[2. What case do we solve?](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%205.%20Predicting%20a%20Biological%20Response#what-case-do-we-solve)

[3. Data overview](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%205.%20Predicting%20a%20Biological%20Response#data-overview)

[4. Project stages](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%205.%20Predicting%20a%20Biological%20Response#project-stages)

[5. Results](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%205.%20Predicting%20a%20Biological%20Response#results)


## Project description

The project is based on the [Kaggle: Predicting a Biological Response](https://www.kaggle.com/c/bioresponse) Competition

The objective of the competition is to help us build as good a model as possible so that we can, as optimally as this data allows, relate molecular information, to an actual biological response.

## What case do we solve?

The main objective of this project is to apply two machine learning methods to the data: Logistic Regression and Random Forest.

For each of these methods, we will upply for different hyperparameters optimisation techniques:
- GridSeachCV,
- RandomizedSearchCV,
- Hyperopt,
- Optuna

## Data overview

Each line represents a molecula. 

The first column (Activity) describes the experiment data - the biological response [0, 1];

The rest of the columns (D1 through D1776) represent molecular descriptors these are caclulated properties that can capture some of the characteristics of the molecule - for example size, shape, or elemental constitution.

## Project stages

The project consists of the following parts:

- Data Loading
- Optimise the hyperparameters
    * Logistic Regression
        - GridSeachCV
        - RandomizedSearchCV,
        - Hyperopt,
        - Optuna
    * Random Forest
        - GridSeachCV
        - RandomizedSearchCV,
        - Hyperopt,
        - Optuna
        
## Results

The code is displayed in <a href="https://github.com/Mike-Kulikov/sf_data_science/blob/main/Project%205.%20Predicting%20a%20Biological%20Response/Project%205%20-%20Predicting%20a%20Biological%20Response.ipynb" target="_blank" rel="noopener">the following file</a>

<b>LogisticRegression</b>
* f1_score for the test set (default parameters) is <b>0.78</b>
* GridSearchCV parameter optimisation - f1_score is <b>0.78</b> - the metric is not improved
* RandomizedSearchCV parameter optimisation - f1_score is <b>0.78</b> - the metric is not improved
* Hyperopt parameter optimisation - f1_score is <b>0.79</b> - the metric is improved
* Optuna parameter optimisation - f1_score is <b>0.80</b> - the metric is improved


<b>RandomForestClassifier</b>
* f1_score for the test set (default parameters) is <b>0.80</b>
* GridSearchCV parameter optimisation - f1_score is <b>0.80</b> - the metric is not improved
* RandomizedSearchCV parameter optimisation - f1_score is <b>0.80</b> - the metric is not improved
* Hyperopt parameter optimisation - f1_score is <b>0.81</b> - the metric is improved
* Optuna parameter optimisation - f1_score is <b>0.81</b> - the metric is improved
