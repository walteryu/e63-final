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

# ML packages; documentation consulted for examples:
# Reference: https://chrisalbon.com/#articles
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Image import packages
from IPython.display import Image
from IPython.core.display import HTML

# Load trash volume data
hhpub = pd.DataFrame.from_csv('./hhpub.csv', index_col=None)
perpub = pd.DataFrame.from_csv('./perpub.csv', index_col=None)
trippub = pd.DataFrame.from_csv('./trippub.csv', index_col=None)
vehpub = pd.DataFrame.from_csv('./vehpub.csv', index_col=None)

# print("Before data clean:")
# print("")
# print("hhpub shape:")
# print(hhpub.shape)
# print("")
# print("perpub shape:")
# print(perpub.shape)
# print("")
# print("trippub shape:")
# print(trippub.shape)
# print("")
# print("vehpub shape:")
# print(vehpub.shape)
# print("")

# Drop null values since they do not contribute to total
hhpub.dropna(subset=['HOUSEID'], inplace=True)
hhpub.dropna(subset=['HHSTATE'], inplace=True)
hhpub.dropna(subset=['WTHHFIN'], inplace=True)
hhpub.dropna(subset=['CDIVMSAR'], inplace=True)
trippub.dropna(subset=['HOUSEID'], inplace=True)
trippub.dropna(subset=['WTTRDFIN'], inplace=True)
trippub.dropna(subset=['CDIVMSAR'], inplace=True)
perpub.dropna(subset=['CDIVMSAR'], inplace=True)
# vehpub.dropna(subset=[''], inplace=True)

hhpub_cdivmsar = hhpub.groupby('CDIVMSAR')['CDIVMSAR']\
  .agg(['count']).sort_values(by=['count'], ascending=False)
  # .head(20)

ax = hhpub_cdivmsar[['count']].plot(
    kind='bar',
    title ="Division",
    figsize=(12, 6),
    legend=True,
    fontsize=12
)
plt.title('Bar Chart for Household Count by Division', fontsize=16)
ax.set_xlabel("Division Code", fontsize=12)
ax.set_ylabel("Household Count", fontsize=12)
plt.show()

trippub_cdivmsar = trippub.groupby('CDIVMSAR')['CDIVMSAR']\
  .agg(['count']).sort_values(by=['count'], ascending=False)
  # .head(20)

ax = trippub_cdivmsar[['count']].plot(
    kind='bar',
    title ="Division",
    figsize=(12, 6),
    legend=True,
    fontsize=12
)
plt.title('Bar Chart for Trip Count by Division', fontsize=16)
ax.set_xlabel("Division Code", fontsize=12)
ax.set_ylabel("Trip Count", fontsize=12)
plt.show()

perpub_cdivmsar = perpub.groupby('CDIVMSAR')['CDIVMSAR']\
  .agg(['count']).sort_values(by=['count'], ascending=False)
  # .head(20)

ax = perpub_cdivmsar[['count']].plot(
    kind='bar',
    title ="Division",
    figsize=(12, 6),
    legend=True,
    fontsize=12
)
plt.title('Bar Chart for Peron Count by Division', fontsize=16)
ax.set_xlabel("Division Code", fontsize=12)
ax.set_ylabel("Person Count", fontsize=12)
plt.show()

# Drop all zero values
hhpub.loc[hhpub.WTHHFIN > 0]
trippub.loc[trippub.WTTRDFIN > 0]

# print("After removing zero values:")
# print("")
# print("hhpub shape:")
# print(hhpub.shape)
# print("")
# print("trippub shape:")
# print(trippub.shape)
# print("")

# Remove outliers which are not within 3 standard deviations from mean
hhpub = hhpub[np.abs(hhpub.WTHHFIN - hhpub.WTHHFIN.mean()) <= (3*hhpub.WTHHFIN.std())]
trippub = trippub[np.abs(trippub.WTTRDFIN - trippub.WTTRDFIN.mean()) <= (3*trippub.WTTRDFIN.std())]

# print("After removing outlier values:")
# print("")
# print("hhpub shape:")
# print(hhpub.shape)
# print("")
# print("trippub shape:")
# print(trippub.shape)
# print("")

# Convert BPM and EPM columns from string to numeric, then divide them
# cols = ['BPM', 'EPM']
# labor_d4_clean_bpm[cols] = labor_d4_clean_bpm[cols].apply(
#     pd.to_numeric, errors='coerce'
# )
# labor_d4_clean_bpm['Midpoint'] = (labor_d4_clean_bpm['Column A']+labor_d4_clean_bpm['Column B'])/2
# labor_d4_clean_bpm['Midpoint'] = labor_d4_clean_bpm[['BPM', 'EPM']].mean(axis=1)

# Change date type from string into datetime
# df_imms_cy["InspectionDate"] = pd.to_datetime(df_imms_cy["InspectionDate"])

# Copy year/month into separate column as numeric values
# df_imms_cy['Year'] = df_imms_cy['InspectionDate'].dt.year
# df_imms_cy['Month'] = df_imms_cy['InspectionDate'].dt.month
# df_imms_cy_d1['Year'] = df_imms_cy_d1['InspectionDate'].dt.year
# df_imms_cy_d1['Month'] = df_imms_cy_d1['InspectionDate'].dt.month

print('Script done running!')
