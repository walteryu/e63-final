### Household Count by Division - Data Analysis

The weighted household count was calculated to identify the following:

1. Which divisions have the most households?
2. How do household count differ between divisions with and without subway systems?
3. Are there any other noticeable trends based on chart plot?

As a result, household count was plotted in the chart below with the following observations:

1. Total Count: The Pacific and Atlantic divisions had the highest count while the Central divisions; this trend is intuitive given that many costal states have higher populations than those in the midwest.
2. Subway Systems: The Pacific and Atlantic had more households with access to a subway system then those which did not have access; however, the Central divisions had more households without access to a subway system than those which did have access.
3. Subway Access: The trend observed above implies that the Pacific and Atlantic regions may have more urban areas with more households centered around transportation hubs instead of more rural or equal distribution of the population as in the Central divisions.
4. Based on these results, it can be inferred that household count is highest in the Pacific and Atlantic divisions with a higher percentage of households having access to a subway system whereas household count is lower the Central divisions with lower percentage of households having access to a subway system.

### Household Count by Division - Spark ML

Decision tree and gradient boosted tree algorithms were used to continue analysis as follows:

1. Initial data analysis showed that divisions with higher population density were more likely to have access to subways systems; although this observation provides association between population density and mass transit, does it have any impact in reducing vehicle usage?
2. The households table has a household vehicle count value; as a result, the algorithms were used to analyze data features for their impact on household vehicle count. Specifically, factors such as frequency of vehicle and mass transit were analyzed.
3. Results showed that higher vehicle usage had high feature importance for predicting household vehicle count. Also, mass transit usage had low feature importance which implies it is independent of household vehicle count.
4. Based on these results, it can be inferred that households in urban areas are more likely to be located near mass transit. However, mass usage has low feature importance with vehicle count whereas vehicle usage has has high feature importance for predicting household vehicle count.
5. Finally, the gradient boosted tree slightly improved accuracy above the decision tree algorithm.
