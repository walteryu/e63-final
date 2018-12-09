### Lessons Learned

Spark ML: Suitable technology to analyze reasonably large dataset; regression algorithms used to evaluate feature importance

Pros:
1. Industry standard for rapidly analyzing large datasets by utilizing RDDs, pipelines and built-in ML algorithms
2. Algorithm choices are sufficient for basic analysis
3. Supports data pipelines within Spark/Python environment

Cons:
1. Algorithm choices may be limited for future analysis
2. Scikit-Learn may be sufficient for many use cases
3. Data visualization is limited (Matlibplot)

GraphX: Suitable technology to analyze graph for potentially complex relationships between household and trip data tables

Pros:
1. One of the best choices for graph analysis if working with RDDs, Python and Jupyter Notebook (Good integration)
2. Supports dataframes; minimal integration required

Cons:
1. Not a mature module; jar file path broke code after working previously on HW11 and previous version of notebook
2. Not as full-featured as Neo4J or similar graph databases

NHTS Dataset:

1. Mass transit does not appear to directly influence driving behavior; however, trip distance/length has high significance
2. Urban areas have higher population so appear to have higher total trips but shorter distances; rural areas have lower population so have lower total trips but longer distances
3. Households with higher income appear to have higher vehicle count and usage; trip destination also has significance

### Conclusion

This project answered the questions posed in the introduction as follows:

1. What additional trends can be identified with machine learning and graph analysis?
<br></br>
<br></br>
**Households Table: Higher vehicle usage had high feature importance for predicting household vehicle count. Also, mass transit usage had low feature importance which implies it is independent of household vehicle count. Based on these results, it can be inferred that households in urban areas are more likely to be located near mass transit. However, mass usage has low feature importance with vehicle count whereas vehicle usage has has high feature importance for predicting household vehicle count.**
<br></br>
<br></br>
**Trips Table: Longer distance and duration trips had high feature importance for predicting vehicle miles traveled. Also, urban density had low feature importance which implies it is independent of vehicle miles traveled. Based on these results, it can be inferred that vehicle miles traveled is likely to be determined by trip distance and duration. However, urban density has low feature importance with vehicle miles traveled.**
<br></br>
<br></br>
**Vehicles Table: Household income and vehicle count had high feature importance for predicting vehicle miles traveled. Also, urban density had low feature importance which implies it is independent of annual vehicle miles traveled. Based on these results, it can be inferred that annual vehicle miles traveled is likely to be higher in households with higher income and vehicle count. However, urban density has low feature importance with annual vehicle miles traveled.**
<br></br>
<br></br>
**Driver Behavior: The analysis demonstrated that vehicle count and usage are not influenced by mass transit access; however, access does help reduce overall miles traveled and trip duration. Residents in areas without mass transit intuitively drive more frequently. Residents with high income typically had a higher vehicle count per household. As a result, residents in rural areas or higher income would be target demographics to analyze driving behavior.**
<br></br>
<br></br>

2. Can these trends help reduce average U.S. commute times?
<br></br>
<br></br>
**Since vehicle count and usage are influenced by income level and location, residents with higher income or in rural areas would be target demographics to analyze driving behavior. Additional analysis of trip type and comparison with vehicle usage may provide additional insights into changing driver behavior.**
<br></br>
<br></br>
**The analysis reinforces the intuitive notion that living within urban areas with access mass transit can help in reducing vehicle count and usage. As a result, additional outreach and media regarding this trend may influence residents who are interested in reducing vehicle usage to follow this recommendation.**
<br></br>
<br></br>

3. If so, then what are some recommendations to do so?
<br></br>
<br></br>
**Analyzing select demographics and trip types insight into how to influence driving behavior to reduce vehicle usage. In addition, living within an urban area with mass transit offers a convenient alternative to driving and intuitively reduces vehicle usage.**
<br></br>
<br></br>
**Reinforcing these results with a case study or public education campaign may generate additional support from the public and motivate residents to make adjustments. Public awareness may lead to support for future transportation planning and vehicle usage reduction efforts.**
<br></br>
<br></br>

### Next Steps

The following steps can be taken to continue project results:

1. Continue analysis of demographic types; specifically. residents with higher income or in rural areas.
2. Continue analysis of trip type; specifically, reason for taking shorter trips (commute, errands, etc.).
3. Continue graph analysis and build subgraphs of trips with multiple destinations.
4. Consider public education campaign to raise awareness of this issue.
