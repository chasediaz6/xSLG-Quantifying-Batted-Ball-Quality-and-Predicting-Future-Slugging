# xSLG-Quantifying-Batted-Ball-Quality-and-Predicting-Future-Slugging
Utilizing batted ball data in baseball to develop an Expected Slugging (xSLG) metric that quantifies batted ball quality with XGBoost. The xSLG metric is then incorporated into a stacked model to predict a players future slugging %.

## Overview
In baseball, there are many statistics we can use to evaluate a batter's offensive production. One of the most commonly used statistics is slugging percentage (SLG). 
SLG is a statistic telling us the average bases earned per at-bat, calculated by summing the total bases a player has earned through hits and dividing that by the total number of at-bats. A player capable of producing extra-base hits fairly often will have a higher SLG than a player who primarily hits singles. The formula for slugging percentage is:

### **$$SLG= \frac{Total\ Bases}{At-Bats}$$**

For example, if a batter has 10 at-bats on the season, recording 3 hits - 2 singles and a triple, his SLG would be .500, since he recorded 5 total bases over his 10 at bats. $SLG = \frac{5}{10} = .500$

**The goal of this project is to estimate a player's "true" slugging, by developing an expected slugging (xSLG) model using batted ball data. There is random noise and luck involved in a players SLG, which impacts their SLG over the course of a season.**

## Approach
My approach to estimate a players xSLG, and predict future slugging can be broken down into 2 parts. 

**1. Develop an xSLG model that summarizes batted ball statistics:**
- Utilizing ensemble models (XGBoost and Random Forest), develop an xSLG model summarizing batted ball data against SLG (total bases). 
   
**2. Incorporate the xSLG metric and other significant features into a "stacked" model to predict future SLG**
- Train a linear regression model to predict a player's second half (2H) SLG using xSLG and other significant features as inputs. 

## Results

The stacked linear model achieved the following results:
- 68% accuracy in predicting whether a player's SLG would increase or decrease in the 2nd half
- ~19% less RMSE than baseline
- 37.7% of player seaons had less than .05 error

## Files

This repository contains the following files and folders, organized as follows:

#### **Data**
- data_dictionary.xlsx: Detailed descriptions of features in the data, including their names, data types, and meanings.
- raw
   - batted_ball.csv: Original batted ball dataset.
   - second_half_slugging.csv: Original second half slugging dataset.
- processed
   - processed_batted_ball.csv: Batted ball dataset after cleaning and preprocessing.
   - processed_second_half_slugging.csv: Second half slugging dataset after cleaning, imputation and preprocessing.
- model_predictions
   - stacked_model_predictions.csv: Slugging predictions generated by the stacked model.

#### **Notebooks**
- 01_EDA_&_Preprocessing.ipynb: Exploratory data analysis and preprocessing of the raw datasets.
- 02_Modeling.ipynb: Model development and training process, including feature engineering and model selection.
- 03_Results_&_Evaluation.ipynb: Evaluation of model performance and analysis of results.

#### **Report**
- report.pdf: Comprehensive project report with in-depth description of my approach, methodology, results, and conclusions.
