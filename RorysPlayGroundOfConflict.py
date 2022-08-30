
# Standard modules
import pandas as pd
import geopandas as gpd
from pprint import pprint
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

covid_date=pd.to_datetime("17 November 2019",infer_datetime_format=True)
print(f"{covid_date=}")

# def filterDateTime():
#
#
# def days_between(d1, d2):
#     d1 = datetime.strptime(d1, "%d %B %Y")
#     d2 = datetime.strptime(d2, "%d %B %Y")
#     return ((d2 - d1).days)

def addMapToAx(ax):
    """
    Plot events on a map

    Parameters:
        ax

    Returns:

    """
    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

    base = world.plot(ax=ax,color='white', edgecolor='black')
    ax.set_aspect('equal')
    ax.set_xlabel("longitude")
    ax.set_ylabel("latitude")

    return world

def setNumEvents(world,df):
    num_event_arr = np.zeros(len(world))
    for iso_num,iso_country in enumerate(world.iso_a3.values):
        iso_selection_bool = df.iso3.values == iso_country
        selected_rows = df[iso_selection_bool]
        num_event_arr[iso_num] = len(selected_rows)
    num_event_arr[num_event_arr==0] = np.nan
    world['num_events'] = num_event_arr

if __name__=="__main__":
    df=pd.read_csv("TeamConflict/conflict_data_acled_2018_2021.csv")
    df['event_date']=pd.to_datetime(df['event_date'],infer_datetime_format=True)
    event_types=df['event_type'].unique()

    for event in event_types:
        fig,axs=plt.subplots(2,1,figsize=[20,10])
        for ii,ax in enumerate(axs):
            world=addMapToAx(ax)
            filter_event_df=df[df['event_type']==event]
            if ii==0:
                filter_event_df=filter_event_df[filter_event_df['event_date']<=covid_date]
                ax.set_title(f"{event} pre covid")
            else:
                filter_event_df=filter_event_df[filter_event_df['event_date']>covid_date]
                ax.set_title(f"{event} post covid")
            print(world)
            setNumEvents(world,filter_event_df)
            # filter_event_df.plot.scatter(x='longitude',y='latitude',ax=ax)
            # ax.hexbin(filter_event_df['longitude'],filter_event_df['latitude'],
            #           bins='log',mincnt=100,gridsize=50)
            # fig.colorbar(c)
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="5%", pad=0.1)
            world.plot(column='num_events',ax=ax, legend=True,cmap="OrRd",
                       cax=cax,legend_kwds={'label': "Number of Events"})
        fig.savefig(rf"plots/{event.replace('/','_')}_count.png",dpi=300,
                    bbox_inches="tight")
