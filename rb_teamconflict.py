#
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

# conflict_data_file = 'conflict_data_acled_2018_2021_SUBSET.csv'
conflict_data_file = 'conflict_data_acled_2018_2021.csv'
df = pd.read_csv(conflict_data_file)
print(df.columns)

#from Rory function
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    
fig,axs=plt.subplots(1,1,figsize=[8,6])
world.boundary.plot(ax=axs,edgecolor='black',linewidth=0.5)
axs.set_aspect('equal')
axs.set_xlabel("Longitude")
axs.set_ylabel("Latitude")

num_event_arr = np.zeros(len(world))
for iso_num,iso_country in enumerate(world.iso_a3.values):

    iso_selection_bool = df.iso3.values == iso_country

    selected_rows = df[iso_selection_bool]

    num_event_arr[iso_num] = len(selected_rows)
    

divider = make_axes_locatable(axs)
cax = divider.append_axes("right", size="5%", pad=0.1)

num_event_arr[num_event_arr==0] = np.nan
world['num_events'] = num_event_arr
world.plot(column='num_events',ax=axs, legend=True,cmap="OrRd",
           cax=cax,legend_kwds={'label': "Number of Events"})

plt.savefig('figures/subset_map_num_events.pdf')
plt.show()