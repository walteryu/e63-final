### Annual Miles by Census Divisions - Data Analysis

The average miles per household by division were calculated to identify commute trends; as a result, the vehicle table was sorted as follows:

1. Households within each selected division were matched with vehicle values.
2. The annual miles for each joined value were totaled, then divided by total households.
3. Result was average annual miles per household by division.

Results were plotted in chart below with the following observations:

1. Total Miles: Total miles traveled were lower in divisions with access to a subway system than those without access to one (except for the South-Atlantic which had slightly higher miles traveled). This implies that more residents may be taking the subway and reducing the number of total miles traveled, although there may be a higher number of trips within these divisions as identified in the previous section.
2. Pacific/Atlantic Divisions: These divisions showed the largest decrease in miles traveled with access to a subway system than those without access. This implies that subway systems in more urban/densely populated divisions may reduce the total number of miles traveled and minimize impacts to the environment and infrastructure.

### Annual Miles by Census Divisions - Spark ML

Decision tree and gradient boosted tree algorithms were used to continue analysis as follows:

1. Initial data analysis showed that divisions with higher population density and access to mass transit were more likely to have lower annual miles traveled per household; although this observation provides association between population density, mass transit and annual miles traveled, do any other factors have an impact on vehicle miles traveled?
2. The vehicles table has an annual vehicle mile traveled value; as a result, the algorithms were used to analyze data features for their impact on annual vehicle miles traveled. Specifically, factors such as household income, vehicle count and urban density were analyzed.
3. Results showed that household income and vehicle count had high feature importance for predicting vehicle miles traveled. Also, urban density had low feature importance which implies it is independent of annual vehicle miles traveled.
4. Based on these results, annual vehicle miles traveled is likely to be higher in households with higher income and vehicle count. However, urban density has low feature importance with annual vehicle miles traveled.
5. Finally, the gradient boosted tree slightly improved accuracy above the decision tree algorithm.
