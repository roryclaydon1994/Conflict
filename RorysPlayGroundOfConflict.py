
# Standard modules
import pandas as pd
import geopandas as gpd
from pprint import pprint
import matplotlib.pyplot as plt

def createMap():
    """
    Plot events on a map

    Parameters:

    Returns:

    """
    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    fig,ax=plt.subplots(1,1,figsize=[20,20])
    base = world.plot(ax=ax,color='white', edgecolor='black')
    ax.set_aspect('equal')
    ax.set_xlabel("longitude")
    ax.set_ylabel("latitude")
    return fig,ax

if __name__=="__main__":
    df=pd.read_csv("TeamConflict/conflict_data_acled_2018_2021.csv")
    print(df.columns)
    event_types=df['event_type'].unique()

    for event in event_types:
        fig,ax=createMap()
        filter_event_df=df[df['event_type']==event]

        filter_event_df.plot.scatter(x='longitude',y='latitude',ax=ax)
        ax.set_title(event)
        plt.show()
