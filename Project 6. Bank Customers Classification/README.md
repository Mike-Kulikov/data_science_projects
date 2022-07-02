# Classification of bank customers #

## Table of contents 

[1. Project description](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%206.%20Bank%20Customers%20Classification#project-description)

[2. What case do we solve?](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%206.%20Bank%20Customers%20Classification#what-case-do-we-solve)

[3. Data overview](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%206.%20Bank%20Customers%20Classification#data-overview)

[4. Project stages](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%206.%20Bank%20Customers%20Classification#project-stages)

[5. Results](https://github.com/Mike-Kulikov/sf_data_science/tree/main/Project%206.%20Bank%20Customers%20Classification#results)


## Project description

We were provided with data on the latest marketing campaign conducted by a bank. The task was to encourage the customers to open a deposit.

We have to analyse this data, identify patterns, and find the decisive factors that influenced the fact that the client put money in this bank.

If we can do this, we will raise the bank's income and help it understand the target audience that needs to be attracted through advertising and various offers. The bank would like to be able to choose among its customers exactly those who are most likely to take a particular offer.

## What case do we solve?

**Business task**: to determine the characteristics by which the bank can identify customers who are most likely to open a deposit in the bank, and thereby increase the effectiveness of a marketing campaign.

**Technical task**: to build a machine learning model using provided characteristics of the clients to predict whether or not the clients will accept the offer to open a deposit in the bank.

## Data overview

The data has 17 values that could be grouped in several blocks:

**Bank customer data:**
- age;
- job (type of job);
- marital (marital status);
- education (education level);
- default (has a credit);
- housing (has a mortgage);
- loan (has a loan);
- balance.

**Related with the last contact of the current campaign:**
- contact (contact communication type);
- month (last contact month of year);
- day (last contact day of the week);
- duration (last contact duration, in seconds).

**Other attributes**
- campaign (number of contacts performed during this campaign and for this client);
- pdays (number of days that passed by after the client was last contacted from a previous campaign);
- previous (number of contacts performed before this campaign and for this client)
- poutcome (outcome of the previous marketing campaign).

**The target variable:** deposit (has the client subscribed a term deposit?) 

## Project stages

1. Primary data processing<br>
Within this part, we process missing values and outliers in the data.
2. Exploratory Data Analysis<br>
We explore the data, find the first patterns, and propose some hypotheses.
3. Data Preprocessing<br>
We recode and transform the data so that it can be used in solving a classification problem.
4. Classification: Logistic Regression and Decision Tree<br>
We build the first predictive model and evaluate its quality. We select the optimal model parameters in order to get the best result.
5. Classification: Model Ensembles and Forecasting<br>
We improve the first prediction using more complex algorithms and evaluate which model can be used to make better predictions.
        
## Results

The code is displayed in <a href="https://github.com/Mike-Kulikov/sf_data_science/blob/main/Project%206.%20Bank%20Customers%20Classification/Project%206.%20Bank%20Customers%20Classification.ipynb" target="_blank" rel="noopener">the following file</a>

We built several ML models:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- tacking Classifier
- Optuna

We achieved a number of methric results: accuracy around 0.81-0.82