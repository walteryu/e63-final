# Module 2D - HH Vehicle Count Factors with Gradient Boosted Tree (GBT) Algorithm:

# Implement and analyze decision tree regression with Spark ML
# Reference: HW10, Q5

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
gbt = GBTRegressor(featuresCol='features', labelCol='HHVEHCNT')
gbt_model = gbt.fit(train)

# Per slide 40 of lab 10 notes, describe summary:
# print("GBT Model Summary:")
# train.describe().show()

# Per slide 47 of lab 10 notes, create output table:
gbt_predictions = gbt_model.transform(test)
gbt_predictions.select("prediction","BIKE","BUS","CAR","PARA","PLACE","PRICE","PTRANS","features").show(10)

# Per slide 47 of lab 10 notes, evaluate accuracy:
gbt_evaluator = RegressionEvaluator(labelCol="HHVEHCNT", predictionCol="prediction", metricName="rmse")
rmse = gbt_evaluator.evaluate(gbt_predictions)
print("Root Mean Squared Error (RMSE) on test data = %g" % rmse)
print('')

# Per slide 47 of lab 10 notes, evaluate accuracy:
gbt_evaluator = RegressionEvaluator(labelCol="HHVEHCNT", predictionCol="prediction", metricName="r2")
r2 = gbt_evaluator.evaluate(gbt_predictions)
print("R Squared (R2) on test data = %g" % r2)
print('')

# Print feature importance:
# Reference: https://towardsdatascience.com/building-a-linear-regression-with-pyspark-and-mllib-d065c3ba246a
print('Feature Importance:')
print(gbt_model.featureImportances)
