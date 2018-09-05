### Data Cleaning Process

Data cleaning was completed prior to formal data analysis; as a result, the datasets were cleaned to minimize the impact of outlier, missing or repeated steps as follows:

1. Replaced empty and missing values since they will cause errors during analysis. Specifically, regression techniques require divisions, so such values would cause errors.
2. Removed negative values since they are erroneous and will skew results. Specifically, negative values will skew summary statistics2 such as the mean, median and standard deviation of trash collection volume within each highway corridor and/or segment.
3. Removed outlier values by removing values greater or less than 3 standard deviations from the mean since they will skew data analysis results. Specifically, outlier values will skew summary statistics such as the mean, median and standard deviation of trash collection volume within each highway corridor and/or segment.
