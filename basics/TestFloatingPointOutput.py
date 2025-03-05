# ===============================================================
# TestFloatingPointOutput.py: Demo floating point output ...
# ===============================================================

import math

# main method ...

def main():
    print("--- Enter TestFloatingPointOutput.main()     ... ");
    print("--- ======================================== ... ");

    # Define approximate value of pi ....

    a = math.pi;

    # Demo floating point formats ...

    print("--- Part 1: Demo floating point formats ...");

    print("---   Maximum detail --> {:.16f}".format(a));
    print("---   Print 2 decimal places of accuracy --> {:.2f}".format(a));
    print("---   Print 3 decimal places of accuracy --> {:.3f}".format(a));
    print("---   Print 4 decimal places of accuracy --> {:.4f}".format(a));
    print("---   Print 5 decimal places of accuracy --> {:.5f}".format(a));

    # Round floating point numbers ...

    print("--- Part 2: Round floating point formats ...");
    print("---   Round number (1 decimal places) --> {:f}".format( round(a,1) ));
    print("---   Round number (2 decimal places) --> {:f}".format( round(a,2) ));
    print("---   Round number (3 decimal places) --> {:f}".format( round(a,3) ));
    print("---   Round number (4 decimal places) --> {:f}".format( round(a,4) ));
    print("---   Round number (5 decimal places) --> {:f}".format( round(a,5) ));

    # Demo exponential formats ...

    print("--- Part 3: Demo exponential formats ...");

    print("---   pi --> {:.2e}".format(a));
    print("---   pi --> {:.4e}".format(a));

    # Format array of numbers ...
    
    print("--- ");
    print("--- Part 4: Format array of numbers in exponential format ...");
    print("--- ");

    numbers = [34.23, -0.123334987, 1, 24.223, 3449685.1];

    for x in numbers:
       print ("--- {:14.6e}".format(x));

    print("--- ");
    print("--- Part 5: Print array of comma-separated numbers ...");
    print("--- ");

    for x in numbers:
       print ("--- {:14,.3f}".format(x));

    # Demo conversion of basis ...

    print("--- ");
    print("--- Part 6: Demo conversion of basis ...");
    print("--- ");

    b = 21;

    print("--- ");
    print("--- Print 21 in decimal, hexidecimal, octal and binary formats ...");
    print("--- {0:d} - {0:x} - {0:o} - {0:b} ".format(b))

    # Multiple substitution values ...

    print("--- ");
    print("--- Part 7: Demo multiple substitutions ...");
    print("--- ");

    s1 = "cats"
    s2 = "dogs"
    s3 = "%s and %s living together" % (s1, s2)
    s4 = "{} and {} living together ".format(s1, s2)

    print("--- %s " % s3);
    print("--- %s " % s4);

    print("--- ");
    print("--- Part 8: Format table data ...");
    print("--- ===================================== ...");

    # data

    starters = [
        [ 'Andre Iguodala', 4, 3,  7 ],
        [  'Klay Thompson', 5, 0, 21 ],
        [  'Stephen Curry', 5, 8, 36 ],
        [  'Draymon Green', 9, 4, 11 ],
        [   'Andrew Bogut', 3, 0,  2 ],
    ]

    # define format row

    row = "| {player:<16s} | {reb:2d} | {ast:2d} | {pts:2d} |".format

    for p in starters:
        print(row(player=p[0], reb=p[1], ast=p[2], pts=p[3]))

    print("--- ======================================== ... ");
    print("--- Leave TestFloatingPointOutput.main()     ... ");

if __name__ == "__main__":
    main()


