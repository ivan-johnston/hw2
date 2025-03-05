# ===============================================================
# TestDictionary02.py: Demonstrate nesting of dictionaries.
# 
# Last Modified:                                        July 2022
# ===============================================================

from collections import OrderedDict
from operator import getitem

# main method ...

def main():
    print("--- Enter TestDictionary02.main()    ... ");
    print("--- ======================================== ... ");

    # Manually assemble and print a nested dictionary ...

    print ("--- PART 01: Manually assemble and print nested dictionary ...")

    cars = { 'car01': {  "brand": "Acura", "model": "ILX",
                        "miles": 50000, "new": False, "year": 2016 },
             'car02': {  "brand": "Acura", "model": "RDX",
                        "miles":    10, "new": True, "year": 2022 }}

    print ("--- Cars %s ..." %( cars ))

    # Access elements of nested dictionary ...

    print ("--- Access items in cars 1 and 2 ...")

    print ("---   Car01: brand --> %s ..." %( cars['car01']['brand'] ))
    print ("---        : model --> %s ..." %( cars['car01']['model'] ))
    print ("---        : miles --> %d ..." %( cars['car01']['miles'] ))
    print ("---        : new   --> %s ..." %( cars['car01']['new'] ))
    print ("---        : year  --> %d ..." %( cars['car01']['year']  ))
    print ("---   Car02: brand --> %s ..." %( cars['car02']['brand'] ))
    print ("---        : model --> %s ..." %( cars['car02']['model'] ))
    print ("---        : miles --> %d ..." %( cars['car02']['miles'] ))
    print ("---        : new   --> %s ..." %( cars['car02']['new'] ))
    print ("---        : year  --> %d ..." %( cars['car02']['year']  ))

    # Iterate through dictionary elements ...

    print ("--- Iterate through dictionary elements ...")

    for car_id, car_info in cars.items():
       print ("--- Car ID: %s ..." %( car_id ))
       for key in car_info:
           print ("---    %5s : %s ..." %( key, car_info[key]))

    # Incrementally assemble dictionary elements ...

    print ("--- ")
    print ("--- PART 02: Incrementally assemble nested dictionary ...")

    city01 = {  "name":       "Seattle", "state": "WA", "population":  1000 }
    city02 = {  "name": "San Francisco", "state": "CA", "population":  2000 }
    city03 = {  "name":        "Boston", "state": "MA", "population":  1500 }
    city04 = {  "name":     "Baltimore", "state": "MD", "population":  1200 }
    city05 = {  "name":  "Philadelphia", "state": "PA", "population":  1000 }
    city06 = {  "name":         "Miami", "state": "FL", "population":   500 }

    # Assembly Method 1 ....

    westcoastcity = { "city01":city01, "city02":city02 }

    # Assembly Method 2 ....

    eastcoastcity = {}
    eastcoastcity['city03'] = city03
    eastcoastcity['city04'] = city04
    eastcoastcity['city05'] = city05
    eastcoastcity['city06'] = city06

    print ("--- ")
    print ("--- West Coast Cities ...")
    print ("--- ")

    for city_id, city_info in westcoastcity.items():
       print ("--- City: %s ..." %( city_id ))
       for key in city_info:
           print ("---    %10s : %s ..." %( key, city_info[key]))

    print ("--- ")
    print ("--- East Coast Cities ...")
    print ("--- ")

    for city_id, city_info in eastcoastcity.items():
       print ("--- City: %s ..." %( city_id ))
       for key in city_info:
           print ("---    %10s : %s ..." %( key, city_info[key]))

    print ("--- ")
    print ("--- Sort East Coast Cities by Population ...")
    print ("--- ")

    sort_values = OrderedDict( sorted(eastcoastcity.items(), key = lambda x: getitem(x[1], 'population')) )

    for city_id, city_info in sort_values.items():
       print ("--- City: %s ..." %( city_id ))
       for key in city_info:
           print ("---    %10s : %s ..." %( key, city_info[key]))

    print ("--- ")
    print ("--- Sort East Coast Cities by State ...")
    print ("--- ")

    sort_values = OrderedDict( sorted(eastcoastcity.items(), key = lambda x: getitem(x[1], 'state')) )

    for city_id, city_info in sort_values.items():
       print ("--- City: %s ..." %( city_id ))
       for key in city_info:
           print ("---    %10s : %s ..." %( key, city_info[key]))

    print("--- ======================================== ... ");
    print("--- Leave TestDictionnary02.main()           ... ");

# call the main method ...

main()
