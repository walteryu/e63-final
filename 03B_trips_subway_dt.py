# Module 3B - Trip Distance Factors with Decision Tree Algorithm:

# Implement and analyze decision tree regression with Spark ML
# Reference: HW10, Q5

# Reference: https://stackoverflow.com/questions/46956026/how-to-convert-column-with-string-type-to-int-form-in-pyspark-data-frame
trippub_sp = trippub_sp.withColumn("CDIVMSAR", trippub_sp["CDIVMSAR"].cast(IntegerType()))
trippub_sp = trippub_sp.withColumn("HBPPOPDN", trippub_sp["HBPPOPDN"].cast(IntegerType()))
trippub_sp = trippub_sp.withColumn("HBRESDN", trippub_sp["HBRESDN"].cast(IntegerType()))
trippub_sp = trippub_sp.withColumn("TRPMILES", trippub_sp["TRPMILES"].cast(IntegerType()))
trippub_sp = trippub_sp.withColumn("TRPTRANS", trippub_sp["TRPTRANS"].cast(IntegerType()))
trippub_sp = trippub_sp.withColumn("MSACAT", trippub_sp["MSACAT"].cast(IntegerType()))
trippub_sp = trippub_sp.withColumn("TRVLCMIN", trippub_sp["TRVLCMIN"].cast(IntegerType()))
trippub_sp = trippub_sp.withColumn("VMT_MILE", trippub_sp["VMT_MILE"].cast(IntegerType()))
trippub_sp = trippub_sp.withColumn("URBAN", trippub_sp["URBAN"].cast(IntegerType()))

# Per slide 37 of lab 10 notes, prepare data for ML:
# vectorAssembler = VectorAssembler(inputCols=['CDIVMSAR', 'HBPPOPDN', 'HBRESDN', 'TRPMILES', 'MSACAT', 'TRVLCMIN', 'URBAN'], outputCol='features')
vectorAssembler = VectorAssembler(inputCols=['CDIVMSAR', 'TRPMILES', 'MSACAT', 'TRVLCMIN', 'URBAN'], outputCol='features')

# Normalize each Vector using $L^1$ norm.
# Reference: https://spark.apache.org/docs/latest/ml-features.html#normalizer
# normalizer = Normalizer(inputCol="features", outputCol="normFeatures", p=1.0)
# l1NormData = normalizer.transform(trippub_sp)

vtrippub_sp = vectorAssembler.transform(trippub_sp)
vtrippub_sp

# Per slide 38 of lab 10 notes, split into train/test datasets:
splits = vtrippub_sp.randomSplit([0.7, 0.3])
train = splits[0]
test = splits[1]

# Per slide 47 of lab 10 notes, prepare data for ML:
dt = DecisionTreeRegressor(featuresCol='features', labelCol='VMT_MILE')
dt_model = dt.fit(train)

# Per slide 40 of lab 10 notes, describe summary:
# print("DT Model Summary:")
# train.describe().show()

# Per slide 47 of lab 10 notes, create output table:
dt_predictions = dt_model.transform(test)
# dt_predictions.select("prediction","CDIVMSAR","HBPPOPDN","HBRESDN","TRPMILES","MSACAT","TRVLCMIN","URBAN","features").show(10)
dt_predictions.select("prediction","CDIVMSAR","TRPMILES","MSACAT","TRVLCMIN","URBAN","features").show(10)

# Per slide 47 of lab 10 notes, evaluate accuracy:
dt_evaluator = RegressionEvaluator(labelCol="VMT_MILE", predictionCol="prediction", metricName="rmse")
rmse = dt_evaluator.evaluate(dt_predictions)
print("Root Mean Squared Error (RMSE) on test data = %g" % rmse)
print('')

# Per slide 47 of lab 10 notes, evaluate accuracy:
dt_evaluator = RegressionEvaluator(labelCol="VMT_MILE", predictionCol="prediction", metricName="r2")
r2 = dt_evaluator.evaluate(dt_predictions)
print("R Squared (R2) on test data = %g" % r2)
print('')

# Print feature importance:
# Reference: https://towardsdatascience.com/building-a-linear-regression-with-pyspark-and-mllib-d065c3ba246a
print('Feature Importance:')
print(dt_model.featureImportances)

# Plot bar chart for feature importance:
feature_importance = {
    'feature': [0,1,2,3,4],
    'score': [0.0455287970717,0.69210811385,0.0037337743339,0.225841999204,0.0327873155401]
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
    'Census Division',
    'Trip Distance (Miles)',
    'Census Division Population',
    'Trip Duration (Minutes)',
    'Urban Density'
]
plt.title('Factors Influencing Trip Distance - Feature Importance (Gradient Boosted Tree Algorithm)', fontsize=16)
ax.set_xlabel("Feature, Factors Influencing Trip Distance", fontsize=12)
ax.set_ylabel("Feature Importance Score (0=Low; 1=High)", fontsize=12)
ax.set_xticklabels(x_labels)
plt.show()
