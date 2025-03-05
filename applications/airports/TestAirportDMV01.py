# ===============================================================================
# TestAirportDMV01.py: Multiple purposes:
# 
# 1. Read, process, visualize data from data/airports-us.csv (31,500 entries) ...
# 2. Use geopandas to display airports in Maryland ...
# 3. Add flightpaths from BWI to Dulles, Roanoke and Norfolk ...
# 
# Written by: Mark Austin                                           October, 2024 
# ===============================================================================

import numpy as np
import pandas as pd
import geopandas

import math

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

from pandas import DataFrame
from pandas import Series
from pandas import read_csv

import shapely
from shapely.geometry import Point, LineString, Polygon
from shapely import wkt

from collections import OrderedDict

# ===============================================================
# Print dictionary ...
# ===============================================================

def printDictionary( title, dictionary ):
    print("Dictionary: {:s}:".format(title))
    print("--------------------------------------------------- ")

    sortedDictionary = OrderedDict( sorted( dictionary.items() ) )

    for key, value in sortedDictionary.items(): 
        print("key: {:s} --> value: {:s} ...".format( key, str(value) ))

    print("--------------------------------------------------- ")

# ===============================================================
# Main function ...
# ===============================================================

def main():
    print("--- Enter TestAirportsDMV01.main()                    ... ");
    print("--- ================================================= ... ");
    print("");

    print("");
    print("--- Part 01: Load data/airports/airports-usa.csv data file ... ");
    print("--- ------------------------------------------------------ ... ");
    print("");

    df = pd.read_csv('../../data/airports/airports-usa.csv')

    print( df.describe() )
    print( df.info() )
    print( df.shape )

    print("");
    print("--- Part 02: Iterate over dataframe columns ... ");
    print("--- --------------------------------------- ... ");
    print("");

    i = 0
    for col in df.columns:
       print("--- Col {:3d}: {:s} ...".format(i, col))
       i = i + 1;

    print("");
    print("--- Part 03: Filter dataframe to only keep airports in dmv list ...");
    print("--- ----------------------------------------------------------- ... ");
    print("");

    dmv_options = [ 'Maryland', 'Virginia', 'District of Columbia' ]
    dfDMV = df [ (df['region_name'].isin(dmv_options)) & (df['iata_code'].notnull()) ].copy() 

    print( dfDMV.shape )

    print("");
    print("--- Part 04: Filter data to find small, medium and large airports ... ")
    print("--- ------------------------------------------------------------- ... ");
    print("");

    dfDMVLarge  = dfDMV [ ( dfDMV['type'] == 'large_airport') ]
    dfDMVMedium = dfDMV [ ( dfDMV['type'] == 'medium_airport') ]
    dfDMVSmall  = dfDMV [ ( dfDMV['type'] == 'small_airport') ]

    # Traverse rows of large airports ...

    i = 1
    for index, row in dfDMVLarge.iterrows():
        region        = str( row["region_name"] );
        iata_code     = str( row["iata_code"] );
        airport_name  = str( row["name"] );
        airport_type  = str( row["type"] );
        country = str( row["country_name"] );
        lat     = row[ "latitude_deg"];
        long    = row["longitude_deg"];

        # Print details of airport ...

        print("--- ");
        print("--- Large Airport {:2d}: {:20s} ... ".format(i, airport_name ));
        print("--- --------------------------------------------------------- ... ");
        print("---       IATA Code: {:20s} ... ".format( iata_code ));
        print("---       Operational Status: {:20s} ... ".format( airport_type ));
        print("---       State: {:20s} ... ".format( region ));
        print("---       Country: {:20s} ... ".format( country ));
        print("---       GeoLocation: (lat,long) = ({:10.6f}, {:10.6f}) ... ".format( lat, long ));
        print("--- --------------------------------------------------------- ... ");
        i = i + 1;

    # Traverse rows of medium airports ...

    i = 1
    for index, row in dfDMVMedium.iterrows():
        region        = str( row["region_name"] );
        iata_code     = str( row["iata_code"] );
        airport_name  = str( row["name"] );
        airport_type  = str( row["type"] );
        country = str( row["country_name"] );
        lat     = row[ "latitude_deg"];
        long    = row["longitude_deg"];

        # Print details of airport ...

        print("--- ");
        print("--- Medium Airport {:2d}: {:20s} ... ".format(i, airport_name ));
        print("--- --------------------------------------------------------- ... ");
        print("---       IATA Code: {:20s} ... ".format( iata_code ));
        print("---       Operational Status: {:20s} ... ".format( airport_type ));
        print("---       State: {:20s} ... ".format( region ));
        print("---       Country: {:20s} ... ".format( country ));
        print("---       GeoLocation: (lat,long) = ({:10.6f}, {:10.6f}) ... ".format( lat, long ));
        print("--- --------------------------------------------------------- ... ");
        i = i + 1;

    # Traverse rows of small airports ...

    i = 1
    for index, row in dfDMVSmall.iterrows():
        region        = str( row["region_name"] );
        iata_code     = str( row["iata_code"] );
        airport_name  = str( row["name"] );
        airport_type  = str( row["type"] );
        country = str( row["country_name"] );
        lat     = row[ "latitude_deg"];
        long    = row["longitude_deg"];

        # Print details of airport ...

        print("--- ");
        print("--- Small Airport {:2d}: {:20s} ... ".format(i, airport_name ));
        print("--- --------------------------------------------------------- ... ");
        print("---       IATA Code: {:20s} ... ".format( iata_code ));
        print("---       Operational Status: {:20s} ... ".format( airport_type ));
        print("---       State: {:20s} ... ".format( region ));
        print("---       Country: {:20s} ... ".format( country ));
        print("---       GeoLocation: (lat,long) = ({:10.6f}, {:10.6f}) ... ".format( lat, long ));
        print("--- --------------------------------------------------------- ... ");
        i = i + 1;

    print("");
    print("--- Part 05: Create dictionary of large airport codes       ... ")
    print("--- ------------------------------------------------------- ... ");
    print("");

    items = [ 'iata_code', 'name', 'region_name', 'latitude_deg', 'longitude_deg' ]
    airportcompact01    = dfDMVLarge.filter( items )
    airportcompact01    = airportcompact01.set_index('iata_code').T
    airportdictionary01 = airportcompact01.to_dict('list')

    printDictionary( "Large Airport Codes", airportdictionary01 )

    print("");
    print("--- Part 06: Create dictionary of DMV airport codes         ... ")
    print("--- ------------------------------------------------------- ... ");
    print("");

    items = [ 'iata_code', 'name', 'region_name', 'latitude_deg', 'longitude_deg' ]
    airportcompact02    = dfDMV.filter( items )
    airportcompact02    = airportcompact02.set_index('iata_code').T
    airportdictionary02 = airportcompact02.to_dict('list')

    printDictionary( "DMV Airport Codes", airportdictionary02 )

    print("");
    print("--- Part 07: Read Maryland and Virginia boundary data files ... ")
    print("--- ------------------------------------------------------- ... ");
    print("");

    print("--- MD boundary data ...");

    datapath = "../../data/geography/maryland/BNDY_StateBoundary_DoIT.shp";
    mdboundarydata = geopandas.read_file( datapath )
    mdboundarydata = mdboundarydata.to_crs(4326)

    print("--- VA boundary data ...");

    datapath = "../../data/geography/virginia/VA_State_Generalized.shp";
    vaboundarydata = geopandas.read_file( datapath )
    vaboundarydata = vaboundarydata.to_crs(4326)

    print("--- Chesapeake Bay boundary data ...");

    datapath = "../../data/geography/chesapeakebay/Chesapeake_Bay_Shoreline_High_Resolution.shp";
    chesapeakebaydata = geopandas.read_file( datapath )
    chesapeakebaydata = chesapeakebaydata.to_crs(4326)

    print("--- MD boundary data ...");
    print(mdboundarydata.head())
    print(mdboundarydata.info())
    print(mdboundarydata.shape)

    print("--- Chesapeake Bay coastline data ...");
    print(chesapeakebaydata.head())
    print(chesapeakebaydata.info())
    print(chesapeakebaydata.shape)

    print("");
    print("--- Part 08: Define geopandas dataframes ... ")
    print("--- ------------------------------------ ... ");
    print("");

    gdf01 = geopandas.GeoDataFrame(mdboundarydata)
    gdf02 = geopandas.GeoDataFrame(vaboundarydata)
    gdf03 = geopandas.GeoDataFrame(chesapeakebaydata)

    # Geodataframe layers for large, medium and small airports ...

    gdf04 = geopandas.GeoDataFrame( dfDMVLarge,
                                    geometry=geopandas.points_from_xy(dfDMVLarge.longitude_deg, dfDMVLarge.latitude_deg))

    gdf05 = geopandas.GeoDataFrame( dfDMVMedium,
                                    geometry=geopandas.points_from_xy(dfDMVMedium.longitude_deg, dfDMVMedium.latitude_deg))

    gdf06 = geopandas.GeoDataFrame( dfDMVSmall,
                                    geometry=geopandas.points_from_xy(dfDMVSmall.longitude_deg, dfDMVSmall.latitude_deg))

    print("");
    print("--- Part 09: Manually assemble flightpaths from BWI ...")
    print("--- ------------------------------------------------------------- ...");
    print("--- BWI: GeoLocation: (long, lat)     = ( -76.668297, 39.175400 ) ...")
    print("--- IAD: GeoLocation: (long, lat)     = ( -77.455803, 38.944500 ) ...")
    print("--- Norfolk: GeoLocation: (long, lat) = ( -76.201000, 36.895341 ) ...")
    print("--- Roanoke: Geolocation: (long, lat) = ( -79.975403, 37.325500 ) ...")

    # Fly BWI --> IAD ...

    line01 = LineString( [ (-76.668297, 39.175400), (-77.455803,  38.944500 ) ] )

    # Fly BWI --> Nolfolk ...

    line02 = LineString( [ (-76.668297, 39.175400), (-76.201000, 36.895341 ) ] )

    # Fly BWI --> Roanoke ...

    line03 = LineString( [ (-76.668297, 39.175400), (-79.975403, 37.325500 ) ] )

    # Assemble geopandas dataframe ...

    gdf07 = geopandas.GeoDataFrame( geometry = [ line01, line02, line03 ] )
    gdf07['Airlines'] = [ 'United', 'Delta', 'American' ]
    gdf07.set_crs("EPSG:4326", inplace=True)

    print( gdf04.info() )
    print( gdf04.head() )

    print("");
    print("--- Part 10: Create boundary map for DMV, then add airports ... ")
    print("--- ------------------------------------------------------- ... ");
    print("");

    # We can now plot our ``GeoDataFrame``.

    ax = gdf01.plot( color='white', edgecolor='black')
    ax.set_aspect('equal')
    ax.set_title("Flights from BWI to Dulles, Roanoke, and Norfolk")

    gdf01.plot(ax=ax, color='white')
    gdf02.plot(ax=ax, color='white', edgecolor='black')
    gdf03.plot(ax=ax, color='cornflowerblue')

    gdf04.plot(ax=ax, color = 'maroon', markersize = 80, label= 'Large Airport')
    gdf05.plot(ax=ax, color =   'blue', markersize = 20, label= 'Medium Airport')
    gdf06.plot(ax=ax, color =  'black', markersize = 10, label= 'Small Airport')

    gdf07.plot(ax=ax, color = 'green', label= 'Flights from BWI')

    plt.legend(loc='best')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.grid(True)
    plt.show()

    print("--- ================================================= ... ");
    print("--- Leave TestAirportDMV01.main()                     ... ");

# call the main method ...

if __name__ == "__main__":
    main()
