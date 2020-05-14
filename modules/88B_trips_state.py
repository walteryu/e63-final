# Data exploration of NHTS datasets:
# print("Household Dataset Head:")
# print("")
# print(hhpub.head())
# print("")
# print("Per Person Dataset Head:")
# print("")
# print(perpub.head())
# print("")
# print("Per Trip Dataset Head:")
# print("")
# print(trippub.head())
# print("")
# print("Vehicle Dataset Head:")
# print("")
# print(vehpub.head())

# Sort NHTS household (HH) data by highest number
# Reference: https://nhts.ornl.gov/assets/codebook_v1.1.pdf

# NHTS HH and trip data by state with weighted total
# hh_ca = hhpub.loc[hhpub['HHSTATE'] == 'CA']
# hh_ga = hhpub.loc[hhpub['HHSTATE'] == 'GA']
# hh_nc = hhpub.loc[hhpub['HHSTATE'] == 'NC']
# hh_ny = hhpub.loc[hhpub['HHSTATE'] == 'NY']
# hh_tx = hhpub.loc[hhpub['HHSTATE'] == 'TX']
# hh_wi = hhpub.loc[hhpub['HHSTATE'] == 'WI']

# hh_ca_weight_sum = hh_ca['WTHHFIN'].sum()
# hh_ga_weight_sum = hh_ga['WTHHFIN'].sum()
# hh_nc_weight_sum = hh_nc['WTHHFIN'].sum()
# hh_ny_weight_sum = hh_ny['WTHHFIN'].sum()
# hh_tx_weight_sum = hh_tx['WTHHFIN'].sum()
# hh_wi_weight_sum = hh_wi['WTHHFIN'].sum()

# tr_hh_ca = pd.merge(trippub, hh_ca, left_on='HOUSEID', right_on='HOUSEID')
# tr_hh_ga = pd.merge(trippub, hh_ga, left_on='HOUSEID', right_on='HOUSEID')
# tr_hh_nc = pd.merge(trippub, hh_nc, left_on='HOUSEID', right_on='HOUSEID')
# tr_hh_ny = pd.merge(trippub, hh_ny, left_on='HOUSEID', right_on='HOUSEID')
# tr_hh_tx = pd.merge(trippub, hh_tx, left_on='HOUSEID', right_on='HOUSEID')
# tr_hh_wi = pd.merge(trippub, hh_wi, left_on='HOUSEID', right_on='HOUSEID')

# tr_ca_weight_sum = tr_hh_ca['WTTRDFIN'].sum()
# tr_ga_weight_sum = tr_hh_ga['WTTRDFIN'].sum()
# tr_nc_weight_sum = tr_hh_nc['WTTRDFIN'].sum()
# tr_ny_weight_sum = tr_hh_ny['WTTRDFIN'].sum()
# tr_tx_weight_sum = tr_hh_tx['WTTRDFIN'].sum()
# tr_wi_weight_sum = tr_hh_wi['WTTRDFIN'].sum()

# NHTS best estimate of annual miles by state
# tr_ca_weight_sum = tr_hh_ca['BESTMILE'].sum()
# tr_ga_weight_sum = tr_hh_ga['BESTMILE'].sum()
# tr_nc_weight_sum = tr_hh_nc['BESTMILE'].sum()
# tr_ny_weight_sum = tr_hh_ny['BESTMILE'].sum()
# tr_tx_weight_sum = tr_hh_tx['BESTMILE'].sum()
# tr_wi_weight_sum = tr_hh_wi['BESTMILE'].sum()

# Print out initial results for analysis
# print("Weighted Household Value by State - CA")
# print("")
# print(round(hh_ca_weight_sum, 2))
# print("")
# print("Weighted Household Value by State - GA")
# print("")
# print(round(hh_ga_weight_sum, 2))
# print("")
# print("Weighted Household Value by State - NC")
# print("")
# print(round(hh_nc_weight_sum, 2))
# print("")
# print("Weighted Household Value by State - NY")
# print("")
# print(round(hh_ny_weight_sum, 2))
# print("")
# print("Weighted Household Value by State - TX")
# print("")
# print(round(hh_tx_weight_sum, 2))
# print("")
# print("Weighted Household Value by State - WI")
# print("")
# print(round(hh_wi_weight_sum, 2))
# print("")

# Print out initial results for analysis
# print("Weighted Trip Value by State - CA")
# print("")
# print(round(tr_ca_weight_sum, 2))
# print("")
# print("Weighted Trip Value by State - GA")
# print("")
# print(round(tr_ga_weight_sum, 2))
# print("")
# print("Weighted Trip Value by State - NC")
# print("")
# print(round(tr_nc_weight_sum, 2))
# print("")
# print("Weighted Trip Value by State - NY")
# print("")
# print(round(tr_ny_weight_sum, 2))
# print("")
# print("Weighted Trip Value by State - TX")
# print("")
# print(round(tr_tx_weight_sum, 2))
# print("")
# print("Weighted Trip Value by State - WI")
# print("")
# print(round(tr_wi_weight_sum, 2))
# print("")

# Calculate weighted trip per household by state
# tr_per_hh_ca = tr_ca_weight_sum / hh_ca_weight_sum
# tr_per_hh_ga = tr_ga_weight_sum / hh_ga_weight_sum
# tr_per_hh_nc = tr_nc_weight_sum / hh_nc_weight_sum
# tr_per_hh_ny = tr_ny_weight_sum / hh_ny_weight_sum
# tr_per_hh_tx = tr_tx_weight_sum / hh_tx_weight_sum
# tr_per_hh_wi = tr_wi_weight_sum / hh_wi_weight_sum

# tr_hh_states = {
#     'state': ['California', 'Georgia', 'North Carolina', 'New York', 'Texas', 'Wisconsin'],
#     'trip_per_hh': [tr_per_hh_ca, tr_per_hh_ga, tr_per_hh_nc, tr_per_hh_ny, tr_per_hh_tx, tr_per_hh_wi]
# }
# tr_hh_states_plot = pd.DataFrame(tr_hh_states, columns = ['state', 'trip_per_hh'])

# ax = tr_hh_states_plot[['trip_per_hh']].plot(kind='bar', title ="Weighted Value", figsize=(12, 6), legend=True, fontsize=12)
# x_labels = ['CA', 'GA', 'NC', 'NY', 'TX', 'WI']
# plt.title('Annual Weighted Trips per Houshold by State', fontsize=16)
# ax.set_xlabel("Household State", fontsize=12)
# ax.set_ylabel("Annual Weighted Trips per Household (Count)", fontsize=12)
# ax.set_xticklabels(x_labels)
# plt.show()
