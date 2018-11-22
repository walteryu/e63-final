# Module 2C - Household Count with Spark ML:

# Implement and analyze decision tree regression with Spark ML
# Reference: HW10, Q5

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row, SparkSession
from pyspark.sql.functions import *

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import DecisionTreeRegressor

spark = SparkSession.builder.appName("nhts").getOrCreate()

# Load csv file and process data:
hhpub_sp = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("./data/hhpub.csv")

# Reference: https://stackoverflow.com/questions/46956026/how-to-convert-column-with-string-type-to-int-form-in-pyspark-data-frame
hhpub_sp = hhpub_sp.withColumn("BIKE", hhpub_sp["BIKE"].cast(IntegerType()))
hhpub_sp = hhpub_sp.withColumn("HHVEHCNT", hhpub_sp["HHVEHCNT"].cast(IntegerType()))

# Per slide 37 of lab 10 notes, prepare data for ML:
vectorAssembler = VectorAssembler(inputCols= [hhpub_sp['BIKE']], outputCol= 'features')
vauto_mpg_df = vectorAssembler.transform(auto_mpg)
vauto_mpg_df

# Per slide 38 of lab 10 notes, split into train/test datasets:
splits = vauto_mpg_df.randomSplit([0.7, 0.3])
train = splits[0]
test = splits[1]

# Per slide 47 of lab 10 notes, prepare data for ML:
dt = DecisionTreeRegressor(featuresCol ='features', labelCol = hhpub_sp['HHVEHCNT'])
dt_model = dt.fit(train)

# Per slide 40 of lab 10 notes, describe summary:
print("DT Model Summary:")
train.describe().show()

# Per slide 47 of lab 10 notes, make predictions:
dt_predictions = dt_model.transform(test)
dt_predictions.select("prediction","_c0","features").show(5)

# Per slide 47 of lab 10 notes, evaluate accuracy:
dt_evaluator = RegressionEvaluator(labelCol="_c3", predictionCol="prediction", metricName="rmse")
rmse = dt_evaluator.evaluate(dt_predictions)
print("Root Mean Squared Error (RMSE) on test data = %g" % rmse)

# Per slide 47 of lab 10 notes, evaluate accuracy:
dt_evaluator = RegressionEvaluator(
labelCol="_c3", predictionCol="prediction", metricName="r2")
r2 = dt_evaluator.evaluate(dt_predictions)
print("R Squered (R2) on test data = %g" % r2)