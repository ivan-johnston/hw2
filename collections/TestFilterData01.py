# ===============================================================
# TestFilterData01.py: Explore different ways to filter data ...
# 
# Last Modified:                                       July, 2022
# ===============================================================

from itertools import compress

# main method ...

def main():
    print("--- Enter TestFilterData01.main()            ... ");
    print("--- ======================================== ... ");

    # Create and print simple dictionary ...

    print ("--- Assemble numerical list ...")
  
    list01 = [1, 4, -5, 10, -7, 2, 3, -1]
    print ("--- List01: %s ..." %( list01 ))

    # All positive values

    print ("--- Filter positive values...")

    list02 = [n for n in list01 if n > 0]
    print ("--- List (positive values): %s ..." %( list02 ))

    # All negative values

    print ("--- Filter negative values...")

    list03 = [n for n in list01 if n < 0]
    print ("--- List (negative values): %s ..." %( list03 ))

    # Replace negative values by 0

    print ("--- Replace negative values with zero ...")

    list04 = [n if n > 0 else 0 for n in list01]
    print ("--- List (negative values --> 0): %s ..." %( list04 ))

    # Compressing example

    print ("--- Demostrate list compression ...")

    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]

    counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

    print ("--- Addresses: %s ..." %( addresses ))
    print ("--- Counts: %s ..." %( counts ))

    list05 = [ n > 5 for n in counts ]
    list06 = list(compress(addresses, list05))

    print ("--- Compression Indices: %s ..." %( list05 ))
    print ("--- Filtered List: %s ..." %( list06 ))

    # Filter subset from a dictionary ...

    print ("--- ")
    print ("--- Filter dictionary of stock prices ...")

    prices = {
       "AAPL": 165.00,
       "AMZN": 144.00,
       "GOOG": 125.55,
       "META": 178.49,
       "NVDA": 188.41,
       "TWTR":  44.70,
       "TSLA": 919.00
    }

    print ("--- Stocks: %s ..." %( prices ))

    # Make a dictionary of all prices over 150

    p1 = { key:value for key, value in prices.items() if value > 150 }

    print("--- All prices over 150: %s ..." %( p1 ))

    print("--- ======================================== ... ");
    print("--- Enter TestFilterData01.main()            ... ");

# call the main method ...

main()
