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

# Plot bar chart for feature importance:
# Reference: https://chrisalbon.com/python/data_visualization/matplotlib_bar_plot/
feature_importance = {
    'feature': [0,1,2,3,4,5,6],
    'score': [0.0446868452557,0.0586268748168,0.863075112975,0.000791107496273,0.000836709931205,0.00322482332894,0.0287585261961]
}
feature_importance_plot = pd.DataFrame(
    feature_importance,
    columns = ['feature', 'score']
)

# Plot bar chart for feature importance:
# Reference: https://chrisalbon.com/python/data_visualization/matplotlib_bar_plot/
ax = feature_importance_plot['score'].plot(
    kind='bar',
    title ="Weighted Value",
    figsize=(12, 6),
    legend=True,
    fontsize=12
)
x_labels = [
    'Bike Usage',
    'Bus Usage',
    'Vehicle Usage',
    'Para-Transit Usage',
    'Transit is Financial Burden',
    'Gas Price Influence',
    'Mass Transit Price Influence',
]
plt.title('Factors Influencing Household Vehicle Count - Feature Importance (Gradient Boosted Tree Algorithm)', fontsize=16)
ax.set_xlabel("Feature, Factors Influencing Household Vehicle Count", fontsize=12)
ax.set_ylabel("Feature Importance Score (0=Low; 1=High)", fontsize=12)
ax.set_xticklabels(x_labels)
plt.show()
