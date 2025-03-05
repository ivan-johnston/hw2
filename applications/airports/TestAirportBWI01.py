# ===================================================================================
# TestAirportBWI01.py: Two purposes:
# 
# 1. Read, process and visualize geojson data from data/airports/bwi/ ...
# 2. Use geopandas to display objects associated with BWI.
# 
# Written by: Mark Austin                                             September, 2024 
# ===================================================================================

import numpy as np
import pandas as pd

import math

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import geopandas as gpd

from pandas import DataFrame

# ===============================================================
# Main function ...
# ===============================================================

def main():
    print("--- Enter TestAirportBWI01.main()                     ... ");
    print("--- ================================================= ... ");
    print("");

    # Load and print dataset

    print("");
    print("--- Part 01: Load /data/airports/bwi/bwi-roads.geojson ... ");
    print("--- -------------------------------------------------- ... ");
    print("");

    # GeoDataframe for roads ...

    roads = gpd.read_file( "../../data/airports/bwi/bwi-roads.geojson" )
    gdf01 = gpd.GeoDataFrame ( roads )

    # Dataframe info and shape ...

    print( gdf01.info() )
    print( gdf01.shape )

    print("");
    print("--- Part 02: Load data/airports/bwi/bwi-buildings.geojson ... ");
    print("--- ----------------------------------------------------- ... ");
    print("");

    # GeoDataframe for buildings ...

    buildings = gpd.read_file( "../../data/airports/bwi/bwi-buildings.geojson" )
    gdf02 = gpd.GeoDataFrame ( buildings )

    # Dataframe info and shape ...

    print( gdf02.info() )
    print( gdf02.shape )

    print("");
    print("--- Part 03: Load data/airports/bwi/bwi-stations.geojson ... ");
    print("--- ---------------------------------------------------- ... ");
    print("");

    # GeoDataframe for buildings ...

    stations = gpd.read_file( "../../data/airports/bwi/bwi-stations.geojson" )
    gdf03 = gpd.GeoDataFrame ( stations )

    # Dataframe info and shape ...

    print( gdf03.info() )
    print( gdf03.shape )

    print("");
    print("--- Part 04: Load data/airports/bwi/bwi-amenity-polygons.geojson ... ");
    print("--- ------------------------------------------------------------ ... ");
    print("");

    # GeoDataframe for amenity polygons ...

    amenity01 = gpd.read_file( "../../data/airports/bwi/bwi-amenity-polygons.geojson" )
    gdf04     = gpd.GeoDataFrame ( amenity01 )

    # Dataframe info and shape ...

    print( gdf04.info() )
    print( gdf04.shape )

    print("");
    print("--- Part 05: Load data/airports/bwi/bwi-amenity-points.geojson ... ");
    print("--- ---------------------------------------------------------- ... ");
    print("");

    # GeoDataframe for amenity points ...

    addresses01 = gpd.read_file( "../../data/airports/bwi/bwi-addresses.geojson" )
    gdf05       = gpd.GeoDataFrame ( addresses01 )

    # Dataframe info and shape ...

    print( gdf05.info() )
    print( gdf05.shape )

    print("");
    print("--- Part 06: Load data/airports/bwi/bwi-forests.geojson ... ");
    print("--- --------------------------------------------------- ... ");
    print("");

    # GeoDataframe for amenity points ...

    forests01 = gpd.read_file( "../../data/airports/bwi/bwi-forests.geojson" )
    gdf06     = gpd.GeoDataFrame ( forests01 )

    # Dataframe info and shape ...

    print( gdf06.info() )
    print( gdf06.shape )

    print("");
    print("--- Part 07: Iterate over road dataframe columns ... ");
    print("--- -------------------------------------------- ... ");
    print("");

    i = 0
    for col in gdf01.columns:
       print("--- Col {:3d}: {:s} ...".format(i, col))
       i = i + 1;

    print("");
    print("--- Part 08: Plot geodataframe layers ... ")
    print("--- -------------------------------------------- ... ");
    print("");

    # We can now plot 

    ax = gdf01.plot( color='gray', edgecolor='black', label= 'roads')
    ax.set_aspect('equal')
    ax.set_title("BWI Airport")

    gdf04.plot(ax=ax, color = 'beige',  edgecolor='black', label= 'amenity')
    gdf02.plot(ax=ax, color = 'blue',   label= 'buildings')
    gdf03.plot(ax=ax, color = 'black',  label= 'stations')
    gdf05.plot(ax=ax, color = 'red',    label= 'addresses')
    gdf06.plot(ax=ax, color = 'green',  label= 'forests')

    plt.legend(fontsize="10", loc="upper left")
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.grid(True)
    plt.show()

    print("--- ===================================== ... ");
    print("--- Leave TestAirportBWI01.main()         ... ");

# call the main method ...

if __name__ == "__main__":
    main()
