# Module 2C - HH Vehicle Count Factors with Decision Tree Algorithm:

# Implement and analyze decision tree regression with Spark ML
# Reference: HW10, Q5

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row, SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.evaluation import RegressionEvaluator

spark = SparkSession.builder.appName("nhts").getOrCreate()

# Load csv file and process data:
hhpub_sp = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("./data/hhpub.csv")

# Reference: https://stackoverflow.com/questions/46956026/how-to-convert-column-with-string-type-to-int-form-in-pyspark-data-frame
hhpub_sp = hhpub_sp.withColumn("BIKE", hhpub_sp["BIKE"].cast(IntegerType()))
hhpub_sp = hhpub_sp.withColumn("BUS", hhpub_sp["BUS"].cast(IntegerType()))
hhpub_sp = hhpub_sp.withColumn("CAR", hhpub_sp["CAR"].cast(IntegerType()))
hhpub_sp = hhpub_sp.withColumn("HHVEHCNT", hhpub_sp["HHVEHCNT"].cast(IntegerType()))
hhpub_sp = hhpub_sp.withColumn("PARA", hhpub_sp["PARA"].cast(IntegerType()))
hhpub_sp = hhpub_sp.withColumn("PLACE", hhpub_sp["PLACE"].cast(IntegerType()))
hhpub_sp = hhpub_sp.withColumn("PRICE", hhpub_sp["PRICE"].cast(IntegerType()))
hhpub_sp = hhpub_sp.withColumn("PTRANS", hhpub_sp["PTRANS"].cast(IntegerType()))

# Per slide 37 of lab 10 notes, prepare data for ML:
vectorAssembler = VectorAssembler(inputCols=['BIKE', 'BUS', 'CAR', 'PARA', 'PLACE', 'PRICE', 'PTRANS'], outputCol='features')
vhhpub_sp = vectorAssembler.transform(hhpub_sp)
vhhpub_sp

# Per slide 38 of lab 10 notes, split into train/test datasets:
splits = vhhpub_sp.randomSplit([0.7, 0.3])
train = splits[0]
test = splits[1]

# Per slide 47 of lab 10 notes, prepare data for ML:
dt = DecisionTreeRegressor(featuresCol='features', labelCol='HHVEHCNT')
dt_model = dt.fit(train)

# Per slide 40 of lab 10 notes, describe summary:
# print("DT Model Summary:")
# train.describe().show()

# Per slide 47 of lab 10 notes, create output table:
dt_predictions = dt_model.transform(test)
dt_predictions.select("prediction","BIKE","BUS","CAR","PARA","PLACE","PRICE","PTRANS","features").show(10)

# Per slide 47 of lab 10 notes, evaluate accuracy:
dt_evaluator = RegressionEvaluator(labelCol="HHVEHCNT", predictionCol="prediction", metricName="rmse")
rmse = dt_evaluator.evaluate(dt_predictions)
print("Root Mean Squared Error (RMSE) on test data = %g" % rmse)
print('')

# Per slide 47 of lab 10 notes, evaluate accuracy:
dt_evaluator = RegressionEvaluator(labelCol="HHVEHCNT", predictionCol="prediction", metricName="r2")
r2 = dt_evaluator.evaluate(dt_predictions)
print("R Squared (R2) on test data = %g" % r2)
print('')

# Print feature importance:
# Reference: https://towardsdatascience.com/building-a-linear-regression-with-pyspark-and-mllib-d065c3ba246a
print('Feature Importance:')
print(dt_model.featureImportances)
