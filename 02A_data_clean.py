# Module 2A - Data Clean:
import csv
import pandas as pd
import numpy as np
import scipy
from scipy import stats
pd.options.mode.chained_assignment = None

# Plotting packages; documentation consulted for examples:
# Reference: https://seaborn.pydata.org/examples/index.html
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (15.0, 7.5)

# Statistics packages
import statsmodels
from statsmodels.formula.api import ols

# Image import packages
from IPython.display import Image
from IPython.core.display import HTML

# Data Source - National Household Transportation Survey (NHTS)
# Reference: https://nhts.ornl.gov/

# Load trash volume data
hhpub = pd.DataFrame.from_csv('./data/hhpub.csv', index_col=None)
perpub = pd.DataFrame.from_csv('./data/perpub.csv', index_col=None)
trippub = pd.DataFrame.from_csv('./data/trippub.csv', index_col=None)
vehpub = pd.DataFrame.from_csv('./data/vehpub.csv', index_col=None)

# Drop all zero values
hhpub.loc[hhpub.WTHHFIN > 0]
trippub.loc[trippub.WTTRDFIN > 0]

# Remove outliers which are not within 3 standard deviations from mean
hhpub = hhpub[
    np.abs(hhpub.WTHHFIN - hhpub.WTHHFIN.mean()) <= (3*hhpub.WTHHFIN.std())
]
trippub = trippub[
    np.abs(trippub.WTTRDFIN - trippub.WTTRDFIN.mean()) <= (3*trippub.WTTRDFIN.std())
]

# Drop null values since they do not contribute to total
hhpub.dropna(subset=['HOUSEID'], inplace=True)
hhpub.dropna(subset=['HHSTATE'], inplace=True)
hhpub.dropna(subset=['WTHHFIN'], inplace=True)
hhpub.dropna(subset=['CDIVMSAR'], inplace=True)
trippub.dropna(subset=['HOUSEID'], inplace=True)
trippub.dropna(subset=['WTTRDFIN'], inplace=True)
trippub.dropna(subset=['CDIVMSAR'], inplace=True)
perpub.dropna(subset=['CDIVMSAR'], inplace=True)
vehpub.dropna(subset=['ANNMILES'], inplace=True)

# NHTS HH and trip data by division, weighted total and subway
hh_21 = hhpub.loc[hhpub['CDIVMSAR'] == 21]
hh_22 = hhpub.loc[hhpub['CDIVMSAR'] == 22]
hh_31 = hhpub.loc[hhpub['CDIVMSAR'] == 31]
hh_32 = hhpub.loc[hhpub['CDIVMSAR'] == 32]
hh_51 = hhpub.loc[hhpub['CDIVMSAR'] == 51]
hh_52 = hhpub.loc[hhpub['CDIVMSAR'] == 52]
hh_62 = hhpub.loc[hhpub['CDIVMSAR'] == 62]
hh_63 = hhpub.loc[hhpub['CDIVMSAR'] == 63]
hh_91 = hhpub.loc[hhpub['CDIVMSAR'] == 91]
hh_92 = hhpub.loc[hhpub['CDIVMSAR'] == 92]

# Spark and ML Setup
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row, SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

from pyspark.ml import Pipeline
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.feature import Normalizer
from pyspark.ml.regression import GBTRegressor
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.evaluation import RegressionEvaluator

spark = SparkSession.builder.appName("nhts").getOrCreate()

# Load csv file and process data:
hhpub_sp = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("./data/hhpub.csv")

# Load csv file and process data:
trippub_sp = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("./data/trippub.csv")

# Load csv file and process data:
vehpub_sp = spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("./data/vehpub.csv")
