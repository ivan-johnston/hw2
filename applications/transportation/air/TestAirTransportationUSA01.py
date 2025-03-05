# ========================================================================
# TestAirTransportationUSA01.py. Visualize flights to/from BWI ....
# 
# Written by: Mark Austin                                    February 2023
# ========================================================================

from pandas import DataFrame
from pandas import Series
from pandas import read_csv

import numpy as np 
import pandas as pd
import geopandas

import matplotlib.pyplot as plt

import shapely
from shapely.geometry import Point, LineString, Polygon
from shapely import wkt

from collections import OrderedDict

# ===============================================================
# Print dictionary ...
# ===============================================================

def printDictionary( title, dictionary, sort = False ):
    print("Dictionary: {:s}:".format(title))
    print("--------------------------------------------------- ")

    if sort == True:
       sortedDictionary = OrderedDict( sorted( dictionary.items() ) )
       for key, value in sortedDictionary.items(): 
          print("key: {:s} --> value: {:s} ...".format( key, str(value) ))
    else:
       for key, value in dictionary.items(): 
          print("key: {:s} --> value: {:s} ...".format( key, str(value) ))

    print("--------------------------------------------------- ")

# ==============================
# main method ...
# ==============================

def main():
    print("--- Enter TestAirTransportationUSA01.main()   ... ");
    print("--- ========================================= ... ");

    print("");
    print("--- Part 01: Load data/airports/airports-usa.csv data file ... ");
    print("");

    datapath = '../../../data/airports/airports-usa.csv'
    dfAirports = pd.read_csv( datapath )

    print( dfAirports.describe() )
    print( dfAirports.info() )
    print( dfAirports.shape )

    print("");
    print("--- Part 02: Filter data to find large airports ... ")
    print("");

    # Filter data to only keep large airports ...

    dfLargeAirports = dfAirports [ ( dfAirports['type'] == 'large_airport' ) ]

    # Filter out airports that do not have well-defined iata_codes ...

    dfLargeAirports = dfLargeAirports [ ( dfLargeAirports['iata_code'].notnull() ) ]

    print( dfLargeAirports.describe() )
    print( dfLargeAirports.info() )
    print( dfLargeAirports.shape )

    print("");
    print("--- Part 03: Create compact representation of columns ... ")
    print("");

    items = [ 'iata_code', 'name', 'region_name', 'latitude_deg', 'longitude_deg' ]
    airportcompact01 = dfLargeAirports.filter( items )
    print(airportcompact01);

    print("");
    print("--- Part 04: Sort values by region, then iata code ... ")
    print("");

    # Sort values by region, then iata code ...

    airportcompact01 = airportcompact01.sort_values( by = [ 'region_name', 'iata_code' ] )
    print(airportcompact01);

    print("");
    print("--- Part 05: Create dictionary of large airport codes ... ")
    print("");

    # Set index to iata_code, then convert to dictionary ...

    airportcompact01    = airportcompact01.set_index('iata_code').T
    airportdictionary01 = airportcompact01.to_dict('list')

    # Sort items by key index, then print ...

    printDictionary( "Large Airports", airportdictionary01, sort = True );

    print("");
    print("--- Part 06: Manually assemble flight path ... ")
    print("");

    # Retrieve airport values ...

    bwi     = airportdictionary01.get("BWI")   # <-- Baltimore ...
    sfo     = airportdictionary01.get("SFO")   # <-- San Francisco ...
    chicago = airportdictionary01.get("ORD")   # <-- Chicago ...
    tpa     = airportdictionary01.get("TPA")   # <-- Tampa, FL ...
    atl     = airportdictionary01.get("ATL")   # <-- Atlanta, GA ...
    bos     = airportdictionary01.get("BOS")   # <-- Boston, MA ...
    aus     = airportdictionary01.get("AUS")   # <-- Austin, TX ...

    # Create point objects for cities ...

    city01 = Point( bwi[3], bwi[2] )
    city02 = Point( sfo[3], sfo[2] )
    city03 = Point( chicago[3], chicago[2] )
    city04 = Point( tpa[3], tpa[2] )
    city05 = Point( atl[3], atl[2] )
    city06 = Point( bos[3], bos[2] )
    city07 = Point( aus[3], aus[2] )

    # Assemble list of cities ...
 
    cities = []
    cities.append( city01 )
    cities.append( city02 )
    cities.append( city03 )
    cities.append( city04 )
    cities.append( city05 )
    cities.append( city06 )
    cities.append( city07 )

    # Create geopandas dataframe for city objects ...

    gdf02 = geopandas.GeoDataFrame( geometry = cities )
    gdf02.set_crs("EPSG:4326", inplace=True)

    # Create linestring objects for flights ...

    # Fly BWI --> SFO ...
    line01 = LineString( [ ( bwi[3], bwi[2] ), ( sfo[3],  sfo[2] ) ] )

    # Fly BWI --> ORD ...
    line02 = LineString( [ ( bwi[3], bwi[2] ), ( chicago[3],  chicago[2] ) ] )

    # Fly BWI --> TPA ...
    line03 = LineString( [ ( bwi[3], bwi[2] ), ( tpa[3],  tpa[2] ) ] )

    # Fly BWI --> ATL ...
    line04 = LineString( [ ( bwi[3], bwi[2] ), ( atl[3],  atl[2] ) ] )

    # Fly BWI --> BOS ...
    line05 = LineString( [ ( bwi[3], bwi[2] ), ( bos[3],  bos[2] ) ] )

    # Fly BWI --> AUS ...
    line06 = LineString( [ ( bwi[3], bwi[2] ), ( aus[3],  aus[2] ) ] )

    # Assemble geopandas dataframe for United flights ...

    gdf03 = geopandas.GeoDataFrame( geometry = [ line01, line02 ] )
    gdf03['Airlines'] = [ 'United', 'United', ]
    gdf03.set_crs("EPSG:4326", inplace=True)

    print( gdf03.info() )
    print( gdf03.head() )

    # Assemble geopandas dataframe for United flights ...

    gdf04 = geopandas.GeoDataFrame( geometry = [ line03, line05, line06 ] )
    gdf04['Airlines'] = [ 'SouthWest', 'SouthWest', 'SouthWest' ]
    gdf04.set_crs("EPSG:4326", inplace=True)

    print( gdf04.info() )
    print( gdf04.head() )

    # Assemble geopandas dataframe for Delta flights ...

    gdf05 = geopandas.GeoDataFrame( geometry = [ line04 ] )
    gdf05['Airlines'] = [ 'Delta' ]
    gdf05.set_crs("EPSG:4326", inplace=True)

    print( gdf05.info() )
    print( gdf05.head() )


    print("");
    print("--- Part 07: Read USA boundary shp file into geopandas ... ")
    print("");

    datapath    = "../../../data/geography/usa/USA_States_Generalized.shp";
    usaboundary = geopandas.read_file( datapath )
    print(usaboundary)

    gdf01 = geopandas.GeoDataFrame(usaboundary)

    print("");
    print("--- Part 08: Create USA boundary map ... ")
    print("");

    # We can now plot our ``GeoDataFrame``.

    ax = gdf01.plot( color='white', lw = 1, edgecolor='maroon')
    ax.set_aspect('equal')
    ax.set_title("Domestic Flights to/from BWI")

    gdf02.plot(ax=ax, color = 'blue', markersize = 40, label = 'Airports' )
    gdf03.plot(ax=ax, lw =  1, edgecolor =    'red', label = 'United' )
    gdf04.plot(ax=ax, lw =  1, edgecolor =  'green', label = 'Southwest' )
    gdf05.plot(ax=ax, lw =  1, edgecolor = 'orange', label = 'Delta' )

    plt.legend(loc='best')
    plt.xlabel('longitude')
    plt.ylabel('latitude')

    # Window for continental US ...

    plt.xlim( [ -125, -65 ] )
    plt.ylim( [   25,  50 ] )

    plt.grid(True)
    plt.show()
 
    print("--- ");
    print("--- ========================================== ... ");
    print("--- Finished TestAirTransportationUSA01.main() ... ");

# ==================================================
# call the main method ...
# ==================================================

main()
