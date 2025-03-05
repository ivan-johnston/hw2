# =========================================================================
# TestMajorStreetsNYC.py. Read data on NYC shoreline + main streets, then
# create plot ... 
# 
# Written by: Mark Austin                                        April 2024
# =========================================================================

from pandas import DataFrame
from pandas import Series
from pandas import read_csv

import numpy as np 
import pandas as pd
import geopandas as gpd

from shapely import wkt

import matplotlib.pyplot as plt

# ==============================
# main method ...
# ==============================

def main():
    print("--- Enter TestMajorStreetsNYC.main()         ... ");
    print("--- ======================================== ... ");

    # load dataset

    print("--- ");
    print("--- Part 01: Load nyc data files ... ");
    print("--- ");

    dfnycstreets   = pd.read_csv("../../../data/cities/nyc/dcm-nyc-major-streets.csv")
    dfnycshoreline = pd.read_csv("../../../data/cities/nyc/nyc-shoreline.csv")

    # Dataframe description ...

    print("--- ");
    print("--- Major streets in NYC ... ");
    print("--- ");

    print( dfnycstreets.describe() )

    # Dataframe info and shape ...

    print("--- ");
    print("--- Dataframe info and shape ... ");
    print("--- ");

    print( dfnycstreets.info() )
    print( dfnycstreets.shape )

    # Filter dataframe to keep only the "major streets in manhattan" entries ...

    print("--- ");
    print("--- Part 02: Filter dataframe to keep \"Major streets in Manhattan\" ... ")
    print("--- ");

    options = ['Manhattan'] 
    dfmanhattan = dfnycstreets [ dfnycstreets['Borough'].isin(options) ].copy()  
    
    print('--- Manhattan dataframe :\n', dfmanhattan )
    print("--- ");

    # Convert dataframe to a list ...

    manhattanlist = dfmanhattan.values.tolist();

    # Traverse list and extract and print individual items ...

    print("--- ");
    print("--- Item  Borough  Geometry ...");
    print("--- ================================================================================= ...");

    i = 1
    for row in manhattanlist:
        geometry  = row[0];
        borough   = row[1];
        routename = row[3];
        print("---");
        print("--- {:4d}:  {:s} ... ".format(i, borough ));
        print("---     :  {:s} ... ".format( routename ));
        print("---     :  {:s} ... ".format( geometry ));

        i = i + 1;

    print("--- ================================================================================= ...");
    print("--- ");

    # Geodataframe layer for nyc main streets ...

    dfmanhattan['the_geom'] = dfmanhattan['the_geom'].apply(wkt.loads)
    dfmanhattan.rename(columns={'the_geom': 'geometry'}, inplace=True)

    gdf01 = gpd.GeoDataFrame(dfmanhattan, crs='epsg:4326')
    gdf01.geometry

    # Geodataframe layer for nyc shoreline ...

    dfnycshoreline['the_geom'] = dfnycshoreline['the_geom'].apply(wkt.loads)
    dfnycshoreline.rename(columns={'the_geom': 'geometry'}, inplace=True)

    gdf02 = gpd.GeoDataFrame(dfnycshoreline, crs='epsg:4326')
    gdf02.geometry

    # Plot geodataframes for shoreline and street geometry ...

    ax = gdf01.plot( color='red', edgecolor='black')
    ax.set_aspect('equal')
    ax.set_xlim( -74.05, -73.90)
    ax.set_ylim(  40.70,  40.80)
    ax.set_title("Shoreline + Main Streets in Lower Manhattan")

    gdf01.plot(ax=ax, color='red',   linewidth=1 )
    gdf02.plot(ax=ax, color='green', linewidth=1 )

    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.grid(True)
    plt.show()

    print("--- ======================================== ... ");
    print("--- Enter TestMajorStreetsNYC.main()         ... ");

# ==================================================
# call the main method ...
# ==================================================

main()
