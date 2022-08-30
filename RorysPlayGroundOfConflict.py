
# Standard modules
import pandas as pd
import geopandas as gpd
from pprint import pprint
import matplotlib.pyplot as plt

def addEventsToMap():

    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    fig,ax=plt.subplots(1,1,figsize=[20,20])
    base = world.plot(ax=ax,color='white', edgecolor='black')
    ax.set_aspect('equal')
    ax.set_xlabel("longitude")
    ax.set_ylabel("latitude")
    plt.show()

df=pd.read_csv("TeamConflict/conflict_data_acled_2018_2021.csv")
print(df.columns)

addEventsToMap()
