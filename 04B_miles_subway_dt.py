# Module 4B - Vehicle Mileage Factors with Decision Tree Algorithm:

# Implement and analyze decision tree regression with Spark ML
# Reference: HW10, Q5

# Reference: https://stackoverflow.com/questions/46956026/how-to-convert-column-with-string-type-to-int-form-in-pyspark-data-frame
vehpub_sp = vehpub_sp.withColumn("ANNMILES", vehpub_sp["ANNMILES"].cast(IntegerType()))
vehpub_sp = vehpub_sp.withColumn("DRVRCNT", vehpub_sp["DRVRCNT"].cast(IntegerType()))
vehpub_sp = vehpub_sp.withColumn("HHFAMINC", vehpub_sp["HHFAMINC"].cast(IntegerType()))
vehpub_sp = vehpub_sp.withColumn("HHSIZE", vehpub_sp["HHSIZE"].cast(IntegerType()))
vehpub_sp = vehpub_sp.withColumn("HHVEHCNT", vehpub_sp["HHVEHCNT"].cast(IntegerType()))
vehpub_sp = vehpub_sp.withColumn("URBAN", vehpub_sp["URBAN"].cast(IntegerType()))
vehpub_sp = vehpub_sp.withColumn("URBANSIZE", vehpub_sp["URBANSIZE"].cast(IntegerType()))

# Per slide 37 of lab 10 notes, prepare data for ML:
vectorAssembler = VectorAssembler(inputCols=['DRVRCNT', 'HHFAMINC', 'HHSIZE', 'HHVEHCNT', 'URBAN', 'URBANSIZE'], outputCol='features')

# Normalize each Vector using $L^1$ norm.
# Reference: https://spark.apache.org/docs/latest/ml-features.html#normalizer
# normalizer = Normalizer(inputCol="features", outputCol="normFeatures", p=1.0)
# l1NormData = normalizer.transform(vehpub_sp)

vvehpub_sp = vectorAssembler.transform(vehpub_sp)
vvehpub_sp

# Per slide 38 of lab 10 notes, split into train/test datasets:
splits = vvehpub_sp.randomSplit([0.7, 0.3])
train = splits[0]
test = splits[1]

# Per slide 47 of lab 10 notes, prepare data for ML:
dt = DecisionTreeRegressor(featuresCol='features', labelCol='ANNMILES')
dt_model = dt.fit(train)

# Per slide 40 of lab 10 notes, describe summary:
# print("DT Model Summary:")
# train.describe().show()

# Per slide 47 of lab 10 notes, create output table:
dt_predictions = dt_model.transform(test)
dt_predictions.select("prediction","DRVRCNT","HHFAMINC","HHSIZE","HHVEHCNT","URBAN","URBANSIZE","features").show(10)

# Per slide 47 of lab 10 notes, evaluate accuracy:
dt_evaluator = RegressionEvaluator(labelCol="ANNMILES", predictionCol="prediction", metricName="rmse")
rmse = dt_evaluator.evaluate(dt_predictions)
print("Root Mean Squared Error (RMSE) on test data = %g" % rmse)
print('')

# Per slide 47 of lab 10 notes, evaluate accuracy:
dt_evaluator = RegressionEvaluator(labelCol="ANNMILES", predictionCol="prediction", metricName="r2")
r2 = dt_evaluator.evaluate(dt_predictions)
print("R Squared (R2) on test data = %g" % r2)
print('')

# Print feature importance:
# Reference: https://towardsdatascience.com/building-a-linear-regression-with-pyspark-and-mllib-d065c3ba246a
print('Feature Importance:')
print(dt_model.featureImportances)
