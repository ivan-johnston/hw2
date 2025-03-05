# =================================================================================
# TestStateBoundaryDictionary01.py. Create dictionary of state boundary geometries.
# 
# Written by: Mark Austin                                              October 2024
# =================================================================================

from pandas import DataFrame
from pandas import Series
from pandas import read_csv

import numpy as np 
import pandas as pd
import geopandas

from collections import OrderedDict

import matplotlib.pyplot as plt

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

# ==============================
# main method ...
# ==============================

def main():
    print("--- Enter TestStateBoundaryDictionary01.main() ... ");
    print("--- ========================================== ... ");

    # load dataset

    print("");
    print("--- Part 01: Read USA boundary shp file into geopandas ... ")
    print("");

    usaboundary = geopandas.read_file("../../data/geography/usa/USA_States_Generalized.shp")

    print( usaboundary.describe() )
    print( usaboundary.info() )
    print( usaboundary.shape )

    print("");
    print("--- Part 02: Filter to only keep state names/abbreviations and geometry ...");
    print("");

    items = [ 'STATE_NAME', 'STATE_ABBR', 'geometry' ]
    dfStateBoundaries = usaboundary.filter(items)
    dfStateBoundaries = dfStateBoundaries.set_index('STATE_ABBR').T

    print("");
    print("--- Part 03: Convert dataframe to dictionary ... ")
    print("");

    dictionary01 = dfStateBoundaries.to_dict('list')
    printDictionary( "State Boundaries", dictionary01 )

    print("");
    print("--- Part 04: Plot US boundaries dataframe ... ")
    print("");

    # Create geopandas dataframe ...

    gdf01 = geopandas.GeoDataFrame(usaboundary)

    # We can now plot our ``GeoDataFrame``.

    ax = gdf01.plot( color='white', edgecolor='maroon')
    ax.set_aspect('equal')
    ax.set_title("US State Boundaries")

    gdf01.plot(ax=ax, color='white')

    plt.legend('US State Boundaries:')
    plt.xlabel('longitude')
    plt.ylabel('latitude')

    # Window for continental US ...

    plt.xlim( [ -125, -65 ] ) 
    plt.ylim( [   25,  50 ] )

    # Window for North-East Corridor ...

    # plt.xlim( [  -80, -65 ] ) 
    # plt.ylim( [   35,  48 ] )

    plt.grid(True)
    plt.show()
 
    print("--- ");
    print("--- ========================================== ... ");
    print("--- Leave TestStateBoundaryDictionary01.main() ... ");

# ==================================================
# call the main method ...
# ==================================================

main()
