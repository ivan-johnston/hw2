# ===================================================================
# TestDCMetroSystem01.py: Visualize stations and lines on the
#                         Washington DC Metro System. 
# 
# Written by: Mark Austin                             September, 2024 
# ===================================================================

import numpy as np
import pandas as pd

import math
import pprint;

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import json 
import geopandas as gpd
# from geopandas import GeoSeries

from pandas import DataFrame
from pandas import Series
from pandas import read_csv

import shapely
from shapely.geometry import Point, LineString, Polygon
from shapely import wkt

# ===============================================================
# Main function ...
# ===============================================================

def main():
    print("--- Enter TestDCMetroSystem01.main()                  ... ");
    print("--- ================================================= ... ");
    print("");

    print("");
    print("--- Part 01: Load data/cities/washingtondc/metro/metro-lines.geojson --> gdf01 ... ");
    print("");

    # Load and print dataset

    datapath = "../../../data/cities/washingtondc/metro/metro-lines.geojson";
    lines = gpd.read_file( datapath )
    gdf01 = gpd.GeoDataFrame ( lines )

    print( gdf01.info() )
    print( gdf01.head() )
    print( gdf01.shape )

    print("");
    print("--- Part 02: Load data/cities/washingtondc/metro/metro-stations.csv ... ");
    print("");

    # Metro station info ...

    datapath = '../../../data/cities/washingtondc/metro/metro-stations.csv'
    df = pd.read_csv( datapath )

    print( df.info() )
    print( df.head() )
    print( df.shape )

    print("");
    print("--- Part 03: Traverse stations, build lists, print details ... ");
    print("");

    StationNames = [];
    Latitude  = [];
    Longitude = [];

    i = 1
    for index, row in df.iterrows():
        station = str( row["NAME"] );
        address = str( row["ADDRESS"] );
        longitude = row[ "X"];
        latitude  = row[ "Y"];
        metroline = row[ "LINE"];

        # Assemble lists of station names, latitude, longitude ...

        StationNames.append(station);
        Latitude.append(latitude);
        Longitude.append(longitude);

        # Print metro station details ...

        print("--- ");
        print("--- Metro Station: {:2d}: {:20s} ... ".format(i, station ));
        print("--- -------------------------------------------------------------- ... ");
        print("---   Address: {:20s} ... ".format( address ));
        print("---   GeoLocation: (lat,long) = ({:10.6f}, {:10.6f}) ... ".format( latitude, longitude ));
        print("---   Ridership Lines: {:20s} ... ".format( metroline ));
        print("--- -------------------------------------------------------------- ... ");
        i = i + 1;

    print("");
    print("--- Part 04: Build gdf02 geodataframe ... ")
    print("");

    df = pd.DataFrame()
    df['Name'] = StationNames
    df['Lon']  = Longitude
    df['Lat']  = Latitude

    gdf02 = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Lon, df.Lat) )
    gdf02.set_crs("EPSG:4326", inplace=True)
    gdf02 = gdf02.to_crs(4326)

    print( gdf02.info() )
    print( gdf02.head() )

    print("");
    print("--- Part 05: Plot geodataframe layers ... ")
    print("");

    # Plot lines and stations 

    ax = gdf01.plot( color='red', edgecolor='black', label= 'metro lines')
    ax.set_aspect('equal')
    ax.set_title("Washington DC Metro System")

    gdf02.plot(ax=ax, color =  'blue', markersize = 20, label= 'metro stations')

    plt.legend(loc='best')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.grid(True)
    plt.show()

    print("--- ================================================= ... ");
    print("--- Leave TestDCMetroSystem01.main()                  ... ");

# call the main method ...

if __name__ == "__main__":
    main()
