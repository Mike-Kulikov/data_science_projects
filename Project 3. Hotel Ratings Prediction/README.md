# Hotel Ratings Prediction #

## Table of contents 

[1. Project Description](https://github.com/Mike-Kulikov/sf_data_science/blob/main/Hotel_Ratings_Prediction_Project_3/README.md)

[2. What case do we solve?](https://github.com/Mike-Kulikov/sf_data_science/blob/main/Hotel_Ratings_Prediction_Project_3/README.md#What-case-do-we-solve?)

[3. Data overview](https://github.com/Mike-Kulikov/sf_data_science/blob/main/Hotel_Ratings_Prediction_Project_3/README.md#Data-overview)

[4. Project stages](https://github.com/Mike-Kulikov/sf_data_science/blob/main/Hotel_Ratings_Prediction_Project_3/README.md#Project-stages)

[5. Results](https://github.com/Mike-Kulikov/sf_data_science/blob/main/Hotel_Ratings_Prediction_Project_3/README.md#Results)

[6. Outcomes](https://github.com/Mike-Kulikov/sf_data_science/blob/main/Hotel_Ratings_Prediction_Project_3/README.md#Outcomes)


## Project Description

Hotel rating prediction based on booking reviews

This project is an educational assignment for the EDA + Feature Engineering Module of the Introduction into Data Science Course by [Skill Factory](https://skillfactory.ru/)

## What case do we solve?

Imagine that you are a data scientist at the company Booking.com. One of the problems of the company is dishonest hotels that wind up their ratings. One way to discover such hotels is to build a model that predicts the rating of the hotel. If the predictions of the model are significantly different from the actual result, the hotel may be behaving dishonestly and worth checking.

The goal of this project is to create such a model.

## Data overview

The data can be dowloaded from [here](https://drive.google.com/file/d/1Qj0iYEbD64eVAaaBylJeIi3qvMzxf2C_/view?usp=sharing).
Also, this task was placed on [Kaggle](https://www.kaggle.com/t/cb7841e866d743f6843848ce328b0034)

The dataset is a table with 515,000+ rows and 17 columns:
- Hotel Address
- Review Date
- Average Score
- Hotel Name
- Reviewer Nationality
- Negative Review
- Review Total Negative Word Counts
- Positive Review
- Review Total Positive Word Counts
- Reviewer Score
- Total Number of Reviews Reviewer Has Given
- Total Number of Reviews
- Tags
- Days Since Review
- Additional Number of Scoring
- Lat
- Lng

## Project stages

The project consists of the following parts:

- Exploratory Data Analysis
    - Work with Duplicates and Nulls
    - Work with Dates and Time
    - Work with Geographical Locations
    - Work with Scores
    - Work with Tags
    - Reviews Text Analysis
- Values Assessment
- Check the multicollinearity
- Object-type values encoding
- Normalisation
- Training Set up

## Results

As a result of the project, a number of tasks were completed:
- I visualised different aspects of the data,
- The data was cleaned up
- I engineered new features based on internal and external sourses
- Sentiment analysis of the reviewes was made
- A prediction model was created

## Outcomes

All results are displayed in the main [file](https://github.com/Mike-Kulikov/sf_data_science/blob/main/Hotel%20Ratings%20Prediction%20Project_3/Mike%20Kulikov%20-%20SF-Project-3%20-%20Hotel%20Ratings.ipynb).
Also, they were submitted to the Kaggle competition [here](https://www.kaggle.com/code/mikekulikov/mike-kulikov-sf-project-3-hotel-ratings)

MAE: 0.8617125166427526
MAPE: 12.295353927561749