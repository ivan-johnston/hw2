# ====================================================================
# TestDictionary04.py: Four steps:
# 
# 1. Read data from data/airports-us.csv (31,500 entries) ...
# 2. Filter data to isolate large airports in MD, VA and DC ...
# 3. Extract data columns for airport name, region, lat and long ...
# 4. Transform dataframe into a dictionary ...
# 
# Written by: Mark Austin                                October, 2024 
# ====================================================================

import numpy as np
import pandas as pd
import geopandas

from pandas import DataFrame
from pandas import Series
from pandas import read_csv

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
    print("--- Enter TestDictionary04.main()         ... ");
    print("--- ===================================== ... ");

    print("");
    print("--- Part 01: Load data/airports/airports-usa.csv data file ... ");
    print("--- ------------------------------------------------------ ... ");
    print("");

    df = pd.read_csv('../data/airports/airports-usa.csv')

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
    print("--- Part 04: Filter data to find large airports ... ")
    print("--- ------------------------------------------- ... ");
    print("");

    dfDMVLarge  = dfDMV [ ( dfDMV['type'] == 'large_airport') ]

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
        print("--- Airport {:2d}: {:20s} ... ".format(i, airport_name ));
        print("--- --------------------------------------------------------- ... ");
        print("---       IATA Code: {:20s} ... ".format( iata_code ));
        print("---       Operational Status: {:20s} ... ".format( airport_type ));
        print("---       State: {:20s} ... ".format( region ));
        print("---       Country: {:20s} ... ".format( country ));
        print("---       GeoLocation: (lat,long) = ({:10.6f}, {:10.6f}) ... ".format( lat, long ));
        print("--- --------------------------------------------------------- ... ");
        i = i + 1;

    print("");
    print("--- Part 05: Extract four columns from airport dataframe    ... ")
    print("--- ------------------------------------------------------- ... ");
    print("");

    items = [ 'iata_code', 'name', 'region_name', 'latitude_deg', 'longitude_deg' ]
    airportcompact01    = dfDMVLarge.filter( items )
    airportcompact01    = airportcompact01.set_index('iata_code').T

    print("");
    print("--- Part 06: Convert dataframe to dictionary ... ")
    print("--- ---------------------------------------- ... ");
    print("");

    dictionary01 = airportcompact01.to_dict('list')
    printDictionary( "Large Airport Codes", dictionary01 )

    print("");
    print("--- ===================================== ... ");
    print("--- Leave TestDictionary04.main()         ... ");

# call the main method ...

if __name__ == "__main__":
    main()
