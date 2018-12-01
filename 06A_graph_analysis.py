# Module 6A - Spark and Neo4J Setup:
# Reference: Lecture 11 lecture notes and Lab 11 notebook

# Set vertices/edges:
hh_vertices = hhpub
trip_edges = trippub
hh_vertices = hhpub.withColumnRenamed("CDIVMSAR", "id").distinct()
trip_edges = trippub\
    .withColumnRenamed("CDIVMSAR", "src")\
    .withColumnRenamed("VMT_MILE", "dst")

# Create graph:
from graphframes import *
graph = GraphFrame(hh_vertices, trip_edges)
type(graph)
graph.cache()

# Summary statistics:
print("Total Number of Households: " + str(graph.vertices.count()))
print("Total Number of Relationships in Graph: " + str(graph.edges.count()))
print("Total Number of Relationships in Original Data: " + str(trip_edges.count()))

from pyspark.sql.functions import desc
print('Show edges:')
graph.edges.groupBy("src", "dst").count().orderBy(desc("count")).show(50)

# Graph degrees:
print('Query in-degrees:')
inDeg = graph.inDegrees
inDeg.orderBy(desc("inDegree")).show(50, False)

print('Query out-degrees:')
inDeg = graph.outDegrees
inDeg.orderBy(desc("outDegree")).show(50, False)
