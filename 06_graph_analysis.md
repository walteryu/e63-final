### Graph Analysis of Commute Time with Spark and GraphX

Spark and GraphX were used to identify additional trends from the dataset as follows:

1. Create graph between household and trip tables
2. Analyze graph to identify additional relationships
3. In and out-degree relationships validated ML analysis results

Divisions with highest trip count are as follows (10 highest listed):

1. West/South Central (AR, LA, OK, TX) > 1M population w/o subway system
2. South Atlantic (DE, FL, GA, MD, NC, SC, WV, VA) < 1M population
3. Pacific (AK, CA, HI, OR, WA) < 1M population
4. Mid-Atlantic (NY, NJ, PA) < 1M population
5. Pacific (AK, CA, HI, OR, WA) > 1M population w/subway system
6. Pacific (AK, CA, HI, OR, WA) > 1M population w/o subway system
7. East North Central (IL, IN, MI, OH, WI) < 1M population
8. Mid-Atlantic (NY, NJ, PA) > 1M population w/subway system
9. West/South Central (AR, LA, OK, TX) < 1M population
10. South Atlantic (DE, FL, GA, MD, NC, SC, WV, VA) < 1M population

Results were as follows:

1. In-Degree relationships showed that most trips were less than 5 miles which suggests residents may be driving to complete parts of their commute not covered by mass transit or choosing to drive on short trips instead of taking mass transit.
2. Out-Degree relationships showed that the census divisions with the highest trip count typically had less than 1M in population and/or lack access to mass transit.
3. Although previous analysis demonstrated that trip count was equally distributed between divisions, the graph analysis shows that divisions with lower population density and without mass transit access were connected with high total trip count. However since these were shorter trips, it suggests that residents in these areas drive additional trips due to lack of mass transit access.
4. These results validate the trends observed in ML analysis; specifically, driving behavior is associated with urban density and access to mass transit.
