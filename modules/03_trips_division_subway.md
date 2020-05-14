### Trips per Household by Census Divisions - Data Analysis

The average trips per household by division were calculated to identify commute trends; as a result, the household table was sorted for census divisions as follows:

1. Selected census divisions with the 5 highest total of weighted households per the NHTS codebook.
2. Divisions were further sorted by ones with and without subway system.
3. The households identified in these divisions were then matched with trips.
4. The weighted trip values within each division were totaled, then divided by total households.
5. Result was average weighted trips per household by division.

The divisions identified with highest total trips per households were as follows:

1. Mid-Atlantic > 1M with Subway
2. Mid-Atlantic > 1M w/o Subway
3. East North Central > 1M with Subway
4. East North Central > 1M w/o Subway
5. South Atlantic > 1M with Subway
6. South Atlantic > 1M w/o Subway
7. East South Central > 1M with Subway
8. East South Central > 1M w/o Subway
9. Pacific > 1M with Subway
10. Pacific > 1M w/o Subway

The results were plotted in the chart below with the following observations:

1. Trip Count: Total trip count was higher in all divisions with access to a subway system than those without access. This trend implies that households with access to a subway system tend to be more densely populated and result in higher trip count.
2. Trip Count Distribution: Trip count were distributed evenly between divisions despite household count differences which may be due to weight ranking or household formation (larger or smaller size).

### Trips per Household by Census Divisions - Spark ML

Decision tree and gradient boosted tree algorithms were used to continue analysis as follows:

1. Initial data analysis showed that divisions with higher population density had higher trip count regardless of household size; although this observation provides association between population density and mass transit, does it have any impact in reducing vehicle miles traveled?
2. The households table has vehicle mile traveled value; as a result, the algorithms were used to analyze data features for their impact on vehicle miles traveled. Specifically, factors such as trip details and urban density were analyzed.
3. Results showed that longer distance and duration trips had high feature importance for predicting vehicle miles traveled. Also, urban density had low feature importance which implies it is independent of vehicle miles traveled.
4. Based on these results, it can be inferred that vehicle miles traveled is likely to be determined by trip distance and duration. However, urban density has low feature importance with vehicle miles traveled.
5. These results are supported by the analysis of households table: vehicle usage is likely to be determined by trip and distance, not urban density, proximity to mass transit or mass transit usage.
6. Finally, the gradient boosted tree slightly improved accuracy above the decision tree algorithm.
