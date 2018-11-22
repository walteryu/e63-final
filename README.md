# CSCI E-63 Big Data Analytics - Fall 2018

## Final Project - U.S. Commute Time Reduction with Machine Learning (Spark ML)

### Author: Walter Yu, Graduate Degree Candidate

### Abstract

The average commute time within each U.S. census division has a large impact on its economy, productivity, infrastructure and environment. Longer commute times cause lost wages for workers with longer commute times, additional wearing of highway infrastructure and environmental impacts. As a result, this study evaluates commute patterns with the National Household Transportation Survey (NHTS) [dataset](https://nhts.ornl.gov/) provided by the Federal Highway Administration (FHWA) and whether public transportation or additional transportation planning could reduce commute times based on data analysis.

### Introduction

This project continues the analysis developed for the 2017 NHTS Data Challenge. Whereas the contest entry focused on exploratory data analysis (EDA) and visualization, this project will continue analysis with Spark and machine learning. Specifically, it seeks to answer the following questions:

1. What additional relationships between data can be identified with Spark ML?
2. Can these relationships identify trends to reduce average commute time?
3. If so, then what are some recommendations to do so?

Questions covered by the 2017 NHTS Data Challenge were as follows:

1. Which are the census divisions with the most trips per [household](https://nhts.ornl.gov/assets/2017UsersGuide.pdf)?
2. What are the average commute distance and time within those divisions?
3. Could public transportation or transportation planning reduce commute times?
4. What are some recommendations for improving commute times based on [demographic data](http://www.city-data.com/)?

### NHTS Data Analysis

The 2017 NHTS Data Challenge analyzed the households, trips and vehicles tables of the NHTS dataset to evaluate commute trends by census division. Specifically, the tables were analyzed to evaluate average commute distance and time. It provided an overview of U.S. commuter trends and recommendations to reduce average commute times.

### NHTS Machine Learning

Spark ML was used to continue the 2017 NHTS Data Challenge to evaluate relationships within the NHTS dataset tables. Specifically, relationships between average annual trips, miles traveled and commute time.

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

## Installation
Clone Github repository, then run notebook with [Python](https://www.python.org/) and [Jupyter Notebook](https://jupyter.org/).
