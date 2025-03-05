# ======================================================================================
# TestAirportMaryland01.py: Two purposes:
# 
# 1. Read, process and visualize data from data/airports-small.csv (3,300 entries) ...
# 2. Use geopandas to display airports in Maryland ...
# 
# Written by: Mark Austin                                                 February, 2024 
# ======================================================================================

import numpy as np
import pandas as pd
import geopandas

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from pandas import DataFrame
from pandas import Series
from pandas import read_csv

# ===============================================================
# Main function ...
# ===============================================================

def main():
    print("--- Enter TestAirportMaryland01.main()               ... ");
    print("--- ================================================ ... ");
    print("");

    # Load and print dataset

    print("");
    print("--- Part 01: Load airports data file ... ");
    print("");

    df = pd.read_csv('../../data/airports/airports-usa-small.csv')

    # Dataframe description ...

    print("");
    print("--- Airport dataframe, info, and shape description ... ");
    print("");

    print( df.describe() )
    print( df.info() )
    print( df.shape )

    # Filter dataframe to keep only airports located in Maryland ...

    print("");
    print("--- Part 02: Extract and print airports located in Maryland ... ");
    print("");

    options = ['MD'] 
    dfMDairports = df [ df['state'].isin(options) ].copy() 

    print(dfMDairports)

    # Dataframe info and shape ...

    print( dfMDairports.info() )
    print( dfMDairports.shape )

    print("");
    print("--- Part 03: Print individual rows of dfMD ... ");
    print("");

    print("");
    print("--- Item  Iata  Aiport Name                              City          Latitude/Longitude      ...");
    print("--- ========================================================================================== ... ");

    # Traverse rows of dataframe ...

    i = 1
    for index, row in dfMDairports.iterrows():
        iata   = str( row["iata"] );
        county = str( row["name"] );
        city   = str( row["city"] );
        lat    = row["latitude"];
        long   = row["longitude"];
        print("--- {:4d}:  {:3s}, {:39s}, {:13s} ({:f}, {:f}) ... ".format(i, iata, county, city, lat, long ));
        i = i + 1;

    print("--- ========================================================================================== ... ");
    print("--- ");

    print("");
    print("--- Part 04: Convert dfMD dataframe to list, then print ... ");
    print("");

    # Convert dfMD dataframe to list ...

    mdairportlist = dfMDairports.values.tolist();

    # Traverse list, print details of individual airports ...

    print("");
    print("--- Item  Iata  Aiport Name                              City          Latitude/Longitude      ...");
    print("--- ========================================================================================== ... ");

    i = 1
    for row in mdairportlist:
        iata   = str( row[0] );
        county = str( row[1] );
        city   = str( row[2] );
        lat    = row[5];
        long   = row[6];
        print("--- {:4d}:  {:3s}, {:39s}, {:13s} ({:f}, {:f}) ... ".format(i, iata, county, city, lat, long ));
        i = i + 1;

    print("--- ========================================================================================== ... ");
    print("--- ");

    print("");
    print("--- Part 05: Read Maryland boundary and coastline data files ... ")
    print("");

    datapath = "../../data/geography/maryland/BNDY_StateBoundary_DoIT.shp";
    mdboundarydata = geopandas.read_file( datapath )
    mdboundarydata = mdboundarydata.to_crs(4326)

    datapath = "../../data/geography/maryland/BNDY_Shoreline_MGS.shp";
    mdcoastlinedata = geopandas.read_file( datapath )
    mdcoastlinedata = mdcoastlinedata.to_crs(4326)

    print("--- MD boundary data ...");

    print(mdboundarydata.head())
    print(mdboundarydata.info())
    print(mdboundarydata.shape)

    print("--- MD coastline data ...");

    print(mdcoastlinedata.head())
    print(mdcoastlinedata.info())
    print(mdcoastlinedata.shape)

    print("--- ");
    print("--- Part 06: Define geopandas dataframes ... ")
    print("--- ");

    gdf01 = geopandas.GeoDataFrame(mdboundarydata)
    gdf02 = geopandas.GeoDataFrame(mdcoastlinedata)
    gdf03 = geopandas.GeoDataFrame( dfMDairports, geometry=geopandas.points_from_xy(dfMDairports.longitude, dfMDairports.latitude))

    print(gdf03)

    print("");
    print("--- Part 07: Create boundary map for Maryland, then add airports ... ")
    print("");

    # We can now plot our ``GeoDataFrame``.

    ax = gdf01.plot( color='white', edgecolor='black')
    ax.set_aspect('equal')
    ax.set_title("Airports in Maryland")

    gdf01.plot(ax=ax, color='white')
    gdf02.plot(ax=ax, edgecolor='green')
    gdf03.plot(ax=ax, color =  'red', markersize = 50, label= 'Airports')

    plt.legend('Airports:')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.grid(True)
    plt.show()

    print("--- ================================================ ... ");
    print("--- Leave TestAirportMaryland01.main()               ... ");

# call the main method ...

if __name__ == "__main__":
    main()
