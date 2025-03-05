# =======================================================================
# Test relational and logical operators ...
# 
# Written by: Mark Austin                                       July 2023 
# =======================================================================

# main method ...

def main():
    print("--- Enter TestConditionalOperators.main()    ... ");
    print("--- ======================================== ... ");

    print("--- Part 1: Data for conditional operators test ... ");

    a = True; b = False
    print("--- a = {:s}, b = {:s} ...".format( str(a), str(b)))
    x = 4; y = 5; z = 6
    print("--- x = {:2d}, y = {:2d}, z = {:2d} ...".format(x,y,z))
    list = [1, 2, 3, 4, 5 ];
    print( list )

    # Exercise relational operators ...

    print("--- Part 2: Exercise relational operators ... ");
    print('--- x > y   is', x > y )
    print('--- x >= y  is', x >= y )
    print('--- x < y   is', x < y )
    print('--- x <= y  is', x <= y )

    # Exercise logical operators ...

    print("--- Part 3: Exercise logical operators (with a and b) ... ");

    print("--- a and b is {:s} ...".format(str( a and b )))
    print("--- a or b  is {:s} ...".format(str( a or b )))
    print("--- not a   is {:s} ...".format(str( not a )))

    print("--- Part 4: Exercise logical operators (with x and y) ... ");

    print('--- x == y   is', x == y )
    print('--- x != y   is', x != y )

    print("--- Part 5: Evaluate compound expressions ... ");

    print("--- x > y and y <= z --> {:s} ...".format(str( x > y and y <= z )))
    print("--- x >= y or y <= z --> {:s} ...".format(str( x >= y or y <= z )))

    # Membership Operators

    print("--- Part 6: Membership operators ... ");

    if ( x in list ):
       print("--- Line 1 - x is available in the given list")
    else:
       print("--- Line 1 - x is not available in the given list")

    if ( y not in list ):
       print("--- Line 2 - y is not available in the given list")
    else:
       print("--- Line 2 - y is available in the given list")

    # Identity Operators

    print("--- Part 7: Identity operators ... ");

    if ( x is y ):
       print("--- x & y SAME identity")
    if ( x is not y ):
       print("--- x & y have DIFFERENT identity")

    print("--- ======================================== ... ");
    print("--- Leave TestConditionalOperators.main()    ... ");

if __name__ == "__main__":
    main()


