# NHTS HH and trip data by division and weighted total
# Reference: https://nhts.ornl.gov/assets/codebook_v1.1.pdf
# hh_72 = hhpub.loc[hhpub['CDIVMSAR'] == 72]
# hh_53 = hhpub.loc[hhpub['CDIVMSAR'] == 53]
# hh_93 = hhpub.loc[hhpub['CDIVMSAR'] == 93]
# hh_23 = hhpub.loc[hhpub['CDIVMSAR'] == 23]
# hh_91 = hhpub.loc[hhpub['CDIVMSAR'] == 91]

# Sum all weighted households by division
# hh_72_weight_sum = hh_72['WTHHFIN'].sum()
# hh_53_weight_sum = hh_53['WTHHFIN'].sum()
# hh_93_weight_sum = hh_93['WTHHFIN'].sum()
# hh_23_weight_sum = hh_23['WTHHFIN'].sum()
# hh_91_weight_sum = hh_91['WTHHFIN'].sum()

# Join NHTS trip with HH data to analyze total weighted trips per HH
# tr_hh_72 = pd.merge(trippub, hh_72, left_on='HOUSEID', right_on='HOUSEID')
# tr_hh_53 = pd.merge(trippub, hh_53, left_on='HOUSEID', right_on='HOUSEID')
# tr_hh_93 = pd.merge(trippub, hh_93, left_on='HOUSEID', right_on='HOUSEID')
# tr_hh_23 = pd.merge(trippub, hh_23, left_on='HOUSEID', right_on='HOUSEID')
# tr_hh_91 = pd.merge(trippub, hh_91, left_on='HOUSEID', right_on='HOUSEID')

# NHTS trip data by division and weighted total
# tr_72_weight_sum = tr_hh_72['WTTRDFIN'].sum()
# tr_53_weight_sum = tr_hh_53['WTTRDFIN'].sum()
# tr_93_weight_sum = tr_hh_93['WTTRDFIN'].sum()
# tr_23_weight_sum = tr_hh_23['WTTRDFIN'].sum()
# tr_91_weight_sum = tr_hh_91['WTTRDFIN'].sum()

# Calculate weighted trip per household by division
# tr_per_hh_72 = tr_72_weight_sum / hh_72_weight_sum
# tr_per_hh_53 = tr_53_weight_sum / hh_53_weight_sum
# tr_per_hh_93 = tr_93_weight_sum / hh_93_weight_sum
# tr_per_hh_23 = tr_23_weight_sum / hh_23_weight_sum
# tr_per_hh_91 = tr_91_weight_sum / hh_91_weight_sum

# Create bar chart for trips by division
# tr_hh_divisions = {
#     'division': [
#         'West South Central > 1M w/o Subway',
#         'South Atlantic < 1M Residents',
#         'Pacific < 1M Residents',
#         'Mid-Atlantic < 1M Residents',
#         'Pacific > 1M Residents with Subway'
#     ],
#     'trip_per_hh': [
#         tr_per_hh_72,
#         tr_per_hh_53,
#         tr_per_hh_93,
#         tr_per_hh_23,
#         tr_per_hh_91
#     ]
# }
# tr_hh_divisions_plot = pd.DataFrame(tr_hh_divisions, columns = ['division', 'trip_per_hh'])

# ax = tr_hh_divisions_plot[['trip_per_hh']].plot(
#     kind='bar',
#     title ="Weighted Value",
#     figsize=(12, 6),
#     legend=True,
#     fontsize=12
# )
# x_labels = [
#     'West South Central > 1M w/o Subway',
#     'South Atlantic < 1M Residents',
#     'Pacific < 1M Residents',
#     'Mid-Atlantic < 1M Residents',
#     'Pacific > 1M Residents with Subway'
# ]
# plt.title('Annual Weighted Trips per Houshold by Division', fontsize=16)
# ax.set_xlabel("Division", fontsize=12)
# ax.set_ylabel("Annual Weighted Trips per Division (Count)", fontsize=12)
# ax.set_xticklabels(x_labels)
# plt.show()
