# Module 6A - Spark and GraphX Setup:
# Reference: Lecture 11 lecture notes and Lab 11 notebook

# Module 6A - Spark and GraphX Setup:
# Reference: Lecture 11 lecture notes and Lab 11 notebook
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark import SparkContext as sc
from pyspark.sql import SQLContext
from pyspark.sql.functions import *

appName = "nhts_graph"
spark = SparkSession.builder.appName(appName).config('spark.jars.packages','graphframes:graphframes:0.6.0-spark2.3-s_2.11').getOrCreate()

# Load CSV data:
hhpub_gx = spark.read.option("header","true")\
    .csv("./data/hhpub.csv")
perpub_gx = spark.read.option("header","true")\
    .csv("./data/perpub.csv")
trippub_gx = spark.read.option("header","true")\
    .csv("./data/trippub.csv")
vehpub_gx = spark.read.option("header","true")\
    .csv("./data/vehpub.csv")

print('Total Household Count:')
print(hhpub_gx.count())
print('Total People Count:')
print(perpub_gx.count())
print('Total Trip Count:')
print(trippub_gx.count())
print('Total Vehicle Count:')
print(vehpub_gx.count())

# Set vertices/edges:
hh_vertices = hhpub_gx
trip_edges = trippub_gx
hh_vertices = hhpub_gx.withColumnRenamed("CDIVMSAR", "id").distinct()
trip_edges = trippub_gx\
    .withColumnRenamed("CDIVMSAR", "src")\
    .withColumnRenamed("VMT_MILE", "dst")

# Create graph:
# spark = SparkSession.builder.appName(appName).config('spark.jars.packages','graphframes:graphframes:0.6.0-spark2.3-s_2.11').getOrCreate()
# !pyspark --packages graphframes:graphframes:0.6.0-spark2.3-s_2.11
from graphframes import *
graph = GraphFrame(hh_vertices, trip_edges  )
type(graph)
graph.cache()

# Summary statistics:
print('')
print("Total Number of Households: " + str(graph.vertices.count()))
print("Total Number of Relationships in Graph: " + str(graph.edges.count()))
print("Total Number of Relationships in Original Data: " + str(trip_edges.count()))

# print('')
# print('Show edges:')
# graph.edges.groupBy("src", "dst").count().orderBy(desc("count")).show(50)

# Graph degrees:
print('')
print('Query in-degrees:')
inDeg = graph.inDegrees
inDeg.orderBy(desc("inDegree")).show(50, False)

print('Query out-degrees:')
inDeg = graph.outDegrees
inDeg.orderBy(desc("outDegree")).show(50, False)

# Plot bar chart for feature importance:
feature_importance = {
    'feature': [0,1,2,3,4,5,6,7,8,9],
    'score': [132928,118494,65736,54929,54560,52612,44119,43126,41895,33562]
}
feature_importance_plot = pd.DataFrame(
    feature_importance,
    columns = ['feature', 'score']
)

ax = feature_importance_plot['score'].plot(
    kind='bar',
    title ="Weighted Value",
    figsize=(12, 6),
    legend=True,
    fontsize=12
)
x_labels = [
    'West/South Central > 1M population w/o subway system',
    'South Atlantic < 1M population',
    'Pacific < 1M population',
    'Mid-Atlantic < 1M population',
    'Pacific > 1M population w/subway system',
    'Pacific > 1M population w/o subway system',
    'East North Central < 1M population',
    'Mid-Atlantic > 1M population w/subway system',
    'West/South Central < 1M population',
    'South Atlantic < 1M population'
]
plt.title('Graph Connections between Division and Total Vehicle Trips', fontsize=16)
ax.set_xlabel("Census Division", fontsize=12)
ax.set_ylabel("Graph Connections", fontsize=12)
ax.set_xticklabels(x_labels)
plt.show()
