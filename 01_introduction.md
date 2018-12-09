# CSCI E-63 Big Data Analytics - Final Project (Fall 2018)

## Reducing Commute Time with Machine Learning and Graph Analysis

### Author: Walter Yu, Graduate Degree Candidate

### Abstract

The average commute time within each U.S. census division has a large impact on its economy, productivity, infrastructure and environment. Longer commute times can lead to lost wages for workers, additional wearing of highway infrastructure and environmental impacts. As a result, this study evaluates U.S. commuter patterns with the National Household Transportation Survey (NHTS) dataset$^{1}$ provided by the Federal Highway Administration (FHWA) and whether public transportation or additional transportation planning could reduce commute times based on data analysis.

### Topic and Problem Statement

Topic: “Modern scientific instrumentation collects large volumes of data. If you have access to any such data examine whether Spark would bering any benefits to the analysis.”

Problem: Reduce commute time with Spark ML and GraphX by analyzing national highway usage data to reduce negative impacts on roadway infrastructure, worker productivity, livability and the environment.

### Introduction

This project continues the analysis developed for the 2017 NHTS Data Challenge. Whereas the contest entry focused on exploratory data analysis (EDA) and visualization, this project will continue analysis with machine learning and graph analysis. Specifically, it seeks to answer the following questions:

1. What additional trends can be identified with machine learning and graph analysis?
2. Can these trends help reduce average U.S. commute times?
3. If so, then what are some recommendations to do so?

Questions covered by the 2017 NHTS Data Challenge were as follows:

1. Which are the census divisions with the most trips per household$^{2}$?
2. What are the average commute distance and time within those divisions?
3. Could mass transit or transportation planning reduce commute times?
4. What are some recommendations for improving commute times based on demographic data$^{3}$?

### Data Cleaning and Preparation

Data cleaning was completed prior to analysis; as a result, the datasets were cleaned to minimize the impact of outlier, missing or repeated values as follows:

1. Replaced empty and missing values since they may cause errors during analysis.
2. Removed negative values since they may skew summary statistics and results.
3. Removed outlier values by removing values greater or less than 3 standard deviations.
4. Outlier values will skew summary statistics such as the mean, median and standard deviation.

After data cleaning, the household, trip and vehicle tables were sorted by census district to start analysis.

### Data Analysis

The 2017 NHTS Data Challenge contest entry analyzed the households, trips and vehicles tables of the NHTS dataset to evaluate commute trends by census division. Specifically, the tables were analyzed to evaluate average commute distance and time. It provided an overview of U.S. commuter trends and recommendations to reduce average commute times.

### Machine Learning

Spark ML was used to continue the 2017 NHTS Data Challenge to evaluate relationships within the NHTS dataset tables; specifically, relationships between average annual trips, miles traveled and commute time. As a result, tables were analyzed as follows:

1. Households - Which factors most influence household vehicle count and likely to result in more miles driven annually?
2. Trips - Which factors most influence vehicle miles driven and results in more pollution and roadway congestion?
3. Vehicles - Which factors most influence annual miles driven and results in more pollution and roadway congestion?

Analysis was completed with the Spark ML decision tree and gradient-boosted tree algorithms.

### Graph Analysis

Spark GraphX was used to evaluate relationships between the households and trips tables; specifically, relationships between census division and trip distance (miles driven) as follows:

1. Create graph between household and trip tables
2. Analyze graph to identify additional relationships
3. In and out-degree relationships validated ML analysis results

### Tools and Modules

The tools and modules listed below were used to analyze data and provide recommendations:

1. Jupyter Notebook - Analysis and documentation were completed using this notebook.
2. Spark ML - Module used to identify additional trends and feature importance.
3. Spark GraphX - Module used to analyze relationships between household and trip tables.
4. Python Modules - The modules listed below will need to be installed in order to run this notebook.

  * Pandas
  * NumPy
  * SciPy
  * Seaborn
  * Matplotlib
  * PySpark (Spark ML)

### Installation and Configuration

Configuration and Setup:
1. Module Installation: pip install <module_name>
2. Notebook Usage: import <module_name>

* Data Cleaning: NumPy, SciPy & Pandas
* Data Visualization: Matplotlib
* Spark ML: Decision Tree & Gradient-Boosted Tree Algorithms
* GraphX: Vertices/Edges & In/Out-Degree Functions
* Documentation: Jupyter Notebook
