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

# Scikit-Learn ML packages; documentation consulted for examples:
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

# df_imms_labor = pd.DataFrame.from_csv('../csv_files/imms_labor.csv', index_col=None)

# print(list(df_imms_labor))
# df_imms_labor_d1 = df_imms_labor.loc[df_imms_labor['District'] == 1]

# Load D4 labor data
# ds_labor_d4 = ws.datasets['imms_labor_d4.csv']
# df_imms_labor_d4 = ds_labor_d4.to_dataframe()

# Load D4 labor data, positive values only
# ds_labor_d4_positives = ws.datasets['imms_labor_d4_positives.csv']
# df_imms_labor_d4_positives = ds_labor_d4_positives.to_dataframe()

# Load cleaned labor data
# ds_labor_d4_clean = ws.datasets['labor_d4_all_clean.csv']
# df_labor_d4_clean = ds_labor_d4_clean.to_dataframe()

# Load cleaned labor/BPM data
# ds_labor_d4_clean_bpm = ws.datasets['labor_d4_clean_bpm_r2.csv']
# labor_d4_clean_bpm = ds_labor_d4_clean_bpm.to_dataframe()

# Load FY1718 data for D4 EMM analysis
# ds_labor_d4_FY1718 = ws.datasets['labor_d4_FY1718.csv']
# labor_d4_FY1718 = ds_labor_d4_FY1718.to_dataframe()

# Convert BPM and EPM columns from string to numeric, then divide them
# cols = ['BPM', 'EPM']
# labor_d4_clean_bpm[cols] = labor_d4_clean_bpm[cols].apply(
#     pd.to_numeric, errors='coerce'
# )
# labor_d4_clean_bpm['Midpoint'] = (labor_d4_clean_bpm['Column A']+labor_d4_clean_bpm['Column B'])/2
# labor_d4_clean_bpm['Midpoint'] = labor_d4_clean_bpm[['BPM', 'EPM']].mean(axis=1)

# Load scored label data
# ds_scored_labels = ws.datasets['labor_d4_boosted_tree.csv']
# df_scored_labels = ds_scored_labels.to_dataframe()

# Sort by D4 trash collection data
# df_imms_cy_d1 = df_imms_cy.loc[df_imms_cy['District'] == 1]

# Remove outliers which are not within 3 standard deviations from mean
# df_imms_cy = df_imms_cy[np.abs(df_imms_cy.Quantity - df_imms_cy.Quantity.mean()) <= (3*df_imms_cy.Quantity.std())]

# Drop null values since they do not contribute to trash volume
# df_imms_cy.dropna(subset=['Quantity'], inplace=True)

# Sort for CY only from D4 labor dataset
# labor_d1_cy = df_imms_labor_d1.loc[df_imms_labor_d1.Unit == 'CUYD']

# Sort for litter and AAH codes (D40050 & D41050)
# labor_d1_cy = df_imms_labor_d1.loc[df_imms_labor_d1.Activity == 'D40050']

# Sort for D42050 accounting code only from statewide labor dataset
# df_imms_aah = df_imms_cy.loc[df_imms_cy.Code == 'D41050']
# df_imms_encampment = df_imms_cy.loc[df_imms_cy.Code == 'D42050']

# Drop all zero values
# df_imms_cy.loc[df_imms_cy.Quantity > 0]

# labor_d1_cy.loc[labor_d1_cy.PY > 0]

# Change date type from string into datetime
# df_imms_cy["InspectionDate"] = pd.to_datetime(df_imms_cy["InspectionDate"])

# Copy year/month into separate column as numeric values
# df_imms_cy['Year'] = df_imms_cy['InspectionDate'].dt.year
# df_imms_cy['Month'] = df_imms_cy['InspectionDate'].dt.month
# df_imms_cy_d1['Year'] = df_imms_cy_d1['InspectionDate'].dt.year
# df_imms_cy_d1['Month'] = df_imms_cy_d1['InspectionDate'].dt.month

print('Script done running!')
