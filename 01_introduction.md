# CSCI E-63 Big Data Analytics - Fall 2018

## Final Project - Reducing U.S. Commute Time with Machine Learning (Spark ML)

### Author: Walter Yu, Graduate Degree Candidate

### Abstract

The average commute time within each U.S. census division has a large impact on its economy, productivity, infrastructure and environment. Longer commute times cause lost wages for workers with longer commute times, additional wearing of highway infrastructure and environmental impacts. As a result, this study evaluates commute patterns with the National Household Transportation Survey (NHTS) dataset$^{1}$ provided by the Federal Highway Administration (FHWA) and whether public transportation or additional transportation planning could reduce commute times based on data analysis.

### Introduction

This project continues the analysis developed for the 2017 NHTS Data Challenge. Whereas the contest entry focused on exploratory data analysis (EDA) and visualization, this project will continue analysis with Spark and machine learning. Specifically, it seeks to answer the following questions:

1. What additional relationships between data can be identified with Spark ML?
2. Can these relationships identify trends to reduce average commute time?
3. If so, then what are some recommendations to do so?

Questions covered by the 2017 NHTS Data Challenge were as follows:

1. Which are the census divisions with the most trips per household$^{2}$?
2. What are the average commute distance and time within those divisions?
3. Could public transportation or transportation planning reduce commute times?
4. What are some recommendations for improving commute times based on demographic data$^{3}$?

### Data Cleaning and Preparation

Data cleaning was completed prior to analysis; as a result, the datasets were cleaned to minimize the impact of outlier, missing or repeated values as follows:

1. Replaced empty and missing values since they may cause errors during analysis.
2. Removed negative values since they may skew summary statistics and results.
3. Removed outlier values by removing values greater or less than 3 standard deviations from the mean since they will skew results. Specifically, outlier values will skew summary statistics such as the mean, median and standard deviation.

After data cleaning, the household, trip and vehicle tables were sorted by census district to begin the analysis.

### NHTS Data Analysis

The 2017 NHTS Data Challenge analyzed the households, trips and vehicles tables of the NHTS dataset to evaluate commute trends by census division. Specifically, the tables were analyzed to evaluate average commute distance and time. It provided an overview of U.S. commuter trends and recommendations to reduce average commute times.

### NHTS Machine Learning

Spark ML was used to continue the 2017 NHTS Data Challenge to evaluate relationships within the NHTS dataset tables; specifically, relationships between average annual trips, miles traveled and commute time. As a result, tables were analyzed as follows:

1. Households - Which factors influence household vehicle count which is likely to result in more miles driven annually?
2. Trips - Which factors influence vehicle miles driven which results in more pollution and roadway congestion?
3. Vehicles - Which factors influence annual miles driven which results in more pollution and roadway congestion?

Analysis was completed with the Spark ML decision tree and gradient-boosted tree algorithms.

### Tools and Process

The tools and process listed below were used to analyze data and provide recommendations:

1. Jupyter Notebook - Exploratory data analysis and visualization were completed using this notebook.
2. Apache Spark and Spark ML - Modules used to develop analysis from 2017 NHTS Data Challenge.
3. Python Modules - The modules listed below will need to be installed in order to run this notebook.

  * Pandas
  * NumPy
  * SciPy
  * Seaborn
  * Matplotlib
  * PySpark (Spark ML)

### Installation
Clone Github repository, then run notebook with [Python](https://www.python.org/) and [Jupyter Notebook](https://jupyter.org/).
