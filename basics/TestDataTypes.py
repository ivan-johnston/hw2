# =======================================================================
# Test builtin data types ...
# =======================================================================
# 
#   Data type        Description
# 
#   Text Type:       str
#   Numeric Types:   int, float, complex
#   Sequence Types:  list, tuple, range
#   Mapping Type:    dict
#   Set Types:       set, frozenset
#   Boolean Type:    bool
#   Binary Types:    bytes, bytearray, memoryview
#   None Type:       NoneType
# 
# =======================================================================

import sys
import math

# main method ...

def main():
    print("--- Enter TestDataTypes.main()               ... ");
    print("--- ======================================== ... ");

    # Create instances of basic data types ...

    print("--- ");
    print("--- Part 1: Create and print instances of builtin data types ... ");
    print("--- ");

    a = 1                    # <-- define integer ...
    b = 1.5                  # <-- define float ...
    c = 1.0 + 1.5j           # <-- define complex ...
    d = True                 # <-- define boolean ...
    e = "this is a string"   # <-- define string ...
    f = ["A", "B", "C", "D"] # <-- define list ...

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

    print("--- ");
    print("--- Part 2: Details of builtin data types and size ... ");
    print("--- ");

    print ( type(a) )
    print ( sys.getsizeof(a) )
    print ( type(b) )
    print ( sys.getsizeof(b) )
    print ( type(c) )
    print ( sys.getsizeof(c) )
    print ( type(d) )
    print ( sys.getsizeof(d) )
    print ( type(e) )
    print ( sys.getsizeof(e) )
    print ( type(f) )
    print ( sys.getsizeof(f) )

    print("--- ");
    print("--- Part 3: Formatting output ... ");
    print("--- ");

    print("--- a = {:2d} ... ".format(a) );       # <-- Format integer output.
    print("--- b = {:.2f} ... ".format(b) );      # <-- two-decimal places of accuracy.
    print('--- c = {:.2f}'.format(c))
    print("--- d = {:.5s} ... ".format( str(d) ))
    print("--- e = {:15s} ... ".format(e) )

    # convert list to string ...

    output = ["%.5s" % elem for elem in f ]
    print("--- f = ", output )

    print("--- ");
    print("--- Part 4: Import PI from the math library ... ");
    print("--- ");

    PI = math.pi;

    print("--- PI = {:.2f} ... ".format(PI) );     # <-- two decimal places of accuracy.
    print("--- PI = {:.15f} ... ".format(PI) );    # <-- fifteen decimal places of accuracy.
    print("--- PI = {:8.2f} ... ".format(PI) );    # <-- output 8 characters wide and
                                                   #     two-decimal places of accuracy.
    print("--- PI = {:16.12f} ... ".format(PI) );  # <-- output 16 characters wide and
                                                   #     12 decimal places of accuracy.
    print("--- PI = {:16.6e} ... ".format(PI) );   # <-- output exponential format.

    # Use precision variable ...

    print("--- ");
    print("--- Part 5: Use of precision variable ...");
    print("--- ");

    precision = 2
    print("--- PI = {:.{}f} ... ".format(PI, precision ) ); 
    precision = 5
    print("--- PI = {:.{}f} ... ".format(PI, precision ) ); 
    precision = 5
    print("--- PI = {:.{}e} ... ".format(PI, precision ) ); 

    print("--- ");
    print("--- Part 6: Format output of complex numbers ... ");
    print("--- ");

    c1 = 1 + 3j  # complex number
    c2 = 1 - 2j  # complex number
   
    print('--- c1: {:.2f}'.format(c1))
    print('--- c2: {:.2f}'.format(c2))

    print("--- ======================================== ... ");
    print("--- Leave TestDataTypes.main()               ... ");

if __name__ == "__main__":
    main()

