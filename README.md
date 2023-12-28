# xSLG-Quantifying-Batted-Ball-Quality-and-Predicting-Future-Slugging
Utilizing batted ball data in baseball to develop an Expected Slugging (xSLG) metric that quantifies batted ball quality with XGBoost. The xSLG metric is then incorporated into a stacked model to predict a players future slugging %.

## Overview
In baseball, there are many statistics we can use to evaluate the a hitter's production. One of the most well-known statistics is slugging percentage (SLG). 
SLG is a statistic that measures a hitter's power and ability to produce extra-base hits. It is calculated by summing the total bases a player reaches with hits and dividing that by the total number of at-bats. The formula for slugging percentage is:

### **$$SLG= \frac{Total\ Bases}{At-Bats}$$**

For example, if a batter has 10 at-bats on the season, recording 3 hits - 2 singles and a triple, his SLG would be .500, since he recorded 5 total bases over his 10 at bats. $SLG = \frac{5}{10} = .500$

The goal of this project is to estimate a player's "true" slugging, by developing an expected slugging (xSLG) model using batted ball data. There is random noise and luck involved in a players SLG, which impacts their SLG over the course of a season. 

## Approach
My approach to estimate a players xSLG, and predict future slugging can be broken down into 2 parts. 

**1. Develop an xSLG model that summarizes batted ball statistics:**
- Utilizing ensemble models (XGBoost and Random Forest), develop an xSLG model summarizing batted ball data against SLG (total bases). 
   
**2. Incorporate the xSLG metric and other significant features into a "stacked" model to predict future SLG**
- Train a linear regression model to predict a player's second half (2H) SLG using xSLG and other significant features as inputs. 

## Files

## Results
