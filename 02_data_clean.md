### Data Cleaning

The most important data and feedback were provided by Caltrans Maintenance since it manages trash collection operations on the state highway system. Specifically, 5 years of trash collection data from 2012 through 2017 consisting of nearly 100,000 records were analyzed, and results were verified with Maintenance field supervisors on a regular basis. Maintenance manager and supervisors have a depth of domain knowledge regarding trash collection best practices on the state highway system. In addition, Maintenance operates its own data management program to track all aspects of its operations, so feedback and data are a reliable and robust source of information.

As a result, trash collection data for each of the 12 Caltrans districts$^{8}$ was used to identify trash levels, data exploration and visualization. Data features of interest for the trash collection dataset are location (county, route and postmile) and trash collection volume (cubic yards, CY).

Most datasets require data cleaning prior to formal data analysis; as a result, the datasets were cleaned to minimize the impact of outlier, missing or repeated steps as follows:

1. Replaced empty and missing values since they will cause errors during analysis. Specifically, regression techniques require divisions, so such values would cause errors.
2. Removed duplicate values since they are erroneous and will skew data analysis results. Specifically, statistical and machine learning techniques rely heavily on the count of each value to assign them importance during analysis so double-counting will skew such results.
3. Removed negative values since they are erroneous and will skew results. Specifically, negative values will skew summary statistics2 such as the mean, median and standard deviation of trash collection volume within each highway corridor and/or segment.
4. Removed outlier values by removing values greater or less than 3 standard deviations from the mean since they will skew data analysis results. Specifically, outlier values will skew summary statistics such as the mean, median and standard deviation of trash collection volume within each highway corridor and/or segment.
