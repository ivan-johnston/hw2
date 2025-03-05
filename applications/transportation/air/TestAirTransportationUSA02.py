# ========================================================================
# TestAirTransportationUSA02.py. Visualize flight from BWI to SFO ...
# 
# Written by: Mark Austin                                     October 2024
# ========================================================================

from geographiclib.geodesic import Geodesic
from geojson import MultiLineString

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
# Geodesic calculation ...
# ===============================================================

def geodesic(lat1, lon1, lat2, lon2, steps):
    inverse = Geodesic.WGS84.Inverse(lat1, lon1, lat2, lon2)
    linestrings = []
    coordinates = []

    for i in range(0, steps + 1):
        direct = Geodesic.WGS84.Direct(inverse['lat1'], inverse['lon1'], inverse['azi1'],
                                      (i / float(steps)) * inverse['s12'])

        if len(coordinates) > 0:
            expression01 = (coordinates[-1][0] < -90 and direct['lon2'] >  90);
            expression02 = (coordinates[-1][0] >  90 and direct['lon2'] < -90);
            if (expression01 or expression02):
                linestrings.append(coordinates)
                coordinates = []
        coordinates.append((direct['lon2'], direct['lat2']))

    linestrings.append(coordinates)
    geojson = MultiLineString(linestrings)
    return geojson

# ==============================
# main method ...
# ==============================

def main():
    print("--- Enter TestAirTransportationUSA02.main()   ... ");
    print("--- ========================================= ... ");

    print("");
    print("--- Part 01: Load data/airports/airports-usa.csv data file ... ");
    print("");

    dfAirports = pd.read_csv('../../../data/airports/airports-usa.csv')

    # Filter data to only keep large airports with iata_codes ...

    dfLargeAirports = dfAirports [ ( dfAirports['type'] == 'large_airport' ) ]
    dfLargeAirports = dfLargeAirports [ ( dfLargeAirports['iata_code'].notnull() ) ]

    # Create compact representation of columns ...

    items = [ 'iata_code', 'name', 'region_name', 'latitude_deg', 'longitude_deg' ]
    airportcompact01 = dfLargeAirports.filter( items )

    # Set index to iata_code, then convert to dictionary ...

    airportcompact01    = airportcompact01.set_index('iata_code').T
    airportdictionary01 = airportcompact01.to_dict('list')

    print("");
    print("--- Part 02: Manually assemble flight path ... ")
    print("");

    # Retrieve BWI and SFO airport locations from dictionary ...

    bwi = airportdictionary01.get("BWI")   # <-- Baltimore ...
    sfo = airportdictionary01.get("SFO")   # <-- San Francisco ...

    print("");
    print("--- Part 03: Create point objects for cities ... ")
    print("");

    city01 = Point( bwi[3], bwi[2] )
    city02 = Point( sfo[3], sfo[2] )

    print( city01 );
    print( city02 );

    # Assemble list of cities ...

    cities = []
    cities.append( city01 )
    cities.append( city02 )

    print("");
    print("--- Part 04: Geodesic Calculation for BWI --> SFO flight ... ")
    print("");

    linestrings02 = []

    i = 1;
    nosegments = 10;
    for linestring in geodesic( bwi[2], bwi[3], sfo[2], sfo[3], nosegments )['coordinates']:
        linestrings02.append(linestring)
        print("--- {:d} ...".format(i));
        print(linestring);
        i = i + 1;

    # Textual description of flightpath segements ...

    print("--- Textual description of flightpath segments ...");

    print(linestrings02);

    print("--- Create MultiLineString( linestrings ) object ...");

    line02 = MultiLineString(linestrings02)
    print( line02 )

    print("");
    print("--- Part 05: Geodataframe for cities ... ")
    print("");

    gdf02 = geopandas.GeoDataFrame( geometry = cities )
    gdf02.set_crs("EPSG:4326", inplace=True)

    # Create linestring objects for flights ...

    print("");
    print("--- Part 06: Assemble geopandas dataframe for BWI --> SFO flight ...")
    print("");

    idarray       = [ 1 ]
    geometryarray = [ line02 ]

    # gdf03 = geopandas.GeoDataFrame( geometry = [ line03 ] )

    gdf03 = geopandas.GeoDataFrame({ 'id': idarray, 'geometry': geometryarray })
    gdf03['Airlines'] = [ 'United' ]
    gdf03.set_crs("EPSG:4326", inplace=True)

    print( gdf03.info() )
    print( gdf03.head() )

    print("");
    print("--- Part 07: Read USA boundary shp file into geopandas ... ")
    print("");

    datapath    = "../../../data/geography/usa/USA_States_Generalized.shp";
    usaboundary = geopandas.read_file( datapath )

    gdf01 = geopandas.GeoDataFrame(usaboundary)

    print("");
    print("--- Part 08: Create USA boundary map + flight layer ... ")
    print("");

    # We can now plot our ``GeoDataFrame``.

    ax = gdf01.plot( color='white', lw = 1, edgecolor='maroon')
    ax.set_aspect('equal')
    ax.set_title("Flying from BWI to the West Coast")

    # Add BWI --> SFO flight with United ...

    gdf02.plot(ax=ax, color = 'blue', markersize = 40, label = 'Airports' )
    gdf03.plot(ax=ax, lw =  1, edgecolor = 'red', label = 'United' )

    # Annotate plot with airport codes ...

    dlong = -0.7; dlat = 0.7;
    ax.annotate("BWI", xy=( bwi[3] + dlong, bwi[2] + dlat),
                xytext=(3, 3), textcoords="offset points",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="blue", lw=1))

    ax.annotate("SFO", xy=( sfo[3] + dlong, sfo[2] + dlat),
                xytext=(3, 3), textcoords="offset points",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="blue", lw=1))

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
