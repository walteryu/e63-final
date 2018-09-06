# hhpub.dropna(subset=['BESTMILE'], inplace=True)
# trippub.dropna(subset=['BESTMILE'], inplace=True)
# perpub.dropna(subset=['BESTMILE'], inplace=True)
# vehpub.dropna(subset=['BESTMILE'], inplace=True)

# print("Vehicle Dataset Head:")
# print("")
# print(vehpub.head())
# print(vehpub['ANNMILES'].head())

# Join NHTS vehicle with HH data to analyze total annual miles per HH
veh_hh_ca = pd.merge(vehpub, hh_ca, left_on='HOUSEID', right_on='HOUSEID')
veh_hh_ga = pd.merge(vehpub, hh_ga, left_on='HOUSEID', right_on='HOUSEID')
veh_hh_nc = pd.merge(vehpub, hh_nc, left_on='HOUSEID', right_on='HOUSEID')
veh_hh_ny = pd.merge(vehpub, hh_ny, left_on='HOUSEID', right_on='HOUSEID')
veh_hh_tx = pd.merge(vehpub, hh_tx, left_on='HOUSEID', right_on='HOUSEID')
veh_hh_wi = pd.merge(vehpub, hh_wi, left_on='HOUSEID', right_on='HOUSEID')

# NHTS annual miles by state and weighted total
veh_ca_weight_sum = veh_hh_ca['ANNMILES'].sum()
veh_ga_weight_sum = veh_hh_ga['ANNMILES'].sum()
veh_nc_weight_sum = veh_hh_nc['ANNMILES'].sum()
veh_ny_weight_sum = veh_hh_ny['ANNMILES'].sum()
veh_tx_weight_sum = veh_hh_tx['ANNMILES'].sum()
veh_wi_weight_sum = veh_hh_wi['ANNMILES'].sum()

# Calculate weighted trip per household by state
veh_per_hh_ca = veh_ca_weight_sum / hh_ca_weight_sum
veh_per_hh_ga = veh_ga_weight_sum / hh_ga_weight_sum
veh_per_hh_nc = veh_nc_weight_sum / hh_nc_weight_sum
veh_per_hh_ny = veh_ny_weight_sum / hh_ny_weight_sum
veh_per_hh_tx = veh_tx_weight_sum / hh_tx_weight_sum
veh_per_hh_wi = veh_wi_weight_sum / hh_wi_weight_sum

veh_hh_states = {
    'state': ['California', 'Georgia', 'North Carolina', 'New York', 'Texas', 'Wisconsin'],
    'vehip_per_hh': [veh_per_hh_ca, veh_per_hh_ga, veh_per_hh_nc, veh_per_hh_ny, veh_per_hh_tx, veh_per_hh_wi]
}
veh_hh_states_plot = pd.DataFrame(veh_hh_states, columns = ['state', 'vehip_per_hh'])

ax = veh_hh_states_plot[['vehip_per_hh']].plot(kind='bar', title ="Weighted Value", figsize=(12, 6), legend=True, fontsize=12)
x_labels = ['CA', 'GA', 'NC', 'NY', 'TX', 'WI']
plt.title('Annual Annual Miles per Weighted Houshold by State', fontsize=16)
ax.set_xlabel("Household State", fontsize=12)
ax.set_ylabel("Annual Miles per Weighted Household (Count)", fontsize=12)
ax.set_xticklabels(x_labels)
plt.show()
