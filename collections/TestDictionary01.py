# ===============================================================
# TestDictionary01.py: A dictionary is a collection which is
# unordered, changeable and indexed. No duplicate members.
# 
# Last Modified:                                       July, 2022
# ===============================================================

# main method ...

def main():
    print("--- Enter TestDictionary01.main()            ... ");
    print("--- ======================================== ... ");

    # Create and print simple dictionary ...

    print ("")
    print ("--- PART 01: Create and print simple dictionary ...")
    print ("")

    car01 = {  "brand": "Honda",
               "model": "Acura",
               "miles": 25000,
                 "new": False,
                "year": 2016
            }

    print ("--- Car01: {:s} ...".format( str( car01 ) ))

    # Duplicates not Allowed ...

    print ("")
    print ("--- PART 02: Create and print dictionary containing duplicates (miles) ...")
    print ("")

    car02 = {  "brand": "Honda",
               "model": "Acura",
               "miles": 50000,
               "miles": 60000,
                 "new": False,
                "year": 2016
            }

    print ("--- Car02: {:s} ...".format( str( car02 ) ))

    # Access items in dictionary ...

    print ("")
    print ("--- Access items in Car01 ...")
    print ("")

    print ("--- Car01: brand --> {:s} ...".format( str( car01.get("brand")) ))
    print ("---      : model --> {:s} ...".format( str( car01.get("model")) ))
    print ("---      : miles --> {:d} ...".format( car01.get("miles") ))
    print ("---      : new   --> {:s} ...".format( str ( car01.get("new")) ))
    print ("---      : year  --> {:d} ...".format( car01.get("year") ))

    # Retrieve keys from car01 ...

    print ("")
    print ("--- Retrieve keys from Car01 ...")
    print ("")

    print ("--- Car01 keys: {:s} ...".format( str( car01.keys()) ))

    # Add new key to car01 ...

    print ("")
    print ("--- Add new key to Car01 ...")
    print ("")

    car01["color"] = "white"

    print ("--- Car01 keys: {:s} ...".format( str( car01.keys() ) ))
    print ("--- Car01: color --> {:s} ...".format ( car01.get("color") ))

    # Update color of car01 ...

    print ("")
    print ("--- Paint car01 new color ...")
    print ("")

    car01["color"] = "blue"

    print ("--- Car01: color --> {:s} ...".format ( car01.get("color") ))

    # Check to see if a key is in dictionary ...

    print ("")
    print ("--- Check to see if a key is in dictionary ...")
    print ("")
    
    if "model" in car01:
       print("---   Yes, 'model' is one of the keys in car01 dictionary")
    else:
       print("---   No, 'model' is not a key in car01 dictionary")
    
    if "selfdriving" in car01:
       print("---   Yes, 'selfdriving' is one of the keys in car01 dictionary")
    else:
       print("---   No, 'selfdriving' is not a key in car01 dictionary")

    # Update dictionary items...

    print ("")
    print ("--- Update dictionary items ...")
    print ("")

    car01.update({"color":  "red"})
    car01.update({"miles": 100000})

    print ("--- Car01: {:s} ...".format( str( car01 ) ))

    print ("")
    print ("--- PART 03: Simple calculations with dictionaries ...")
    print ("")

    prices = {
       "AAPL": 165.00,
       "AMZN": 144.00,
       "GOOG": 125.55,
       "META": 178.49,
       "NVDA": 188.41,
       "TWTR":  44.70,
       "TSLA": 919.00
    }

    print(prices)

    # Find min and max stock price ...

    print ("")
    print ("--- Compute min/max stock price ...")
    print ("")

    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))

    print ("--- Min price: ", min_price )
    print ("--- Max price: ", max_price )

    print ("")
    print ("--- Sorted prices ...")
    print ("")

    prices_sorted = sorted( zip(prices.values(), prices.keys()) )
    for price, name in prices_sorted:
         print('    ', name, price)

    print ("")
    print ("--- PART 04: Create dictionary of word count ...")
    print ("")

    items = "Cat dog bird rabbit cat cat dog pig bird dog dog cat rabbit"

    # Convert to lower case, then Split list into words ...

    items = items.lower().split();
    print(items)

    stats = {}
    for i in items:
       if i in stats:
          stats[i] += 1
       else:
          stats[i] = 1

    # sort items, then print ...

    print ("")
    for i in sorted(stats, key=stats.get):
        print("--- pet: {:7s} --> count: {:2d} ...".format(i, stats[i]) )

    print("--- ======================================== ... ");
    print("--- Leave TestDictionnary01.main()           ... ");

# call the main method ...

main()
