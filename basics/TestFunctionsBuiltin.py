# ==================================================================
# TestFunctionsBuiltin.py: Exercise builtin functions in Python.
# ==================================================================
# 
# Catalogue of commonly used builtin functions:
# 
# 01. The abs() function returns the absolute value of integer,
#     floating point, and complex numbers. 
# 
# 02. The all() function takes a container as an argument and
#     and returns True if all value in a python iterable have a
#     Boolean value of True.
# 
# 03. The any() function takes one argument and returns True if,
#     even at least one value in the iterable has a Boolean value
#     of True.
# 
# 04. The dict() function creates a python dictionary.
# 
# 05. The float() function converts an integer or compatible value
#     to a float. 
# 
# 06. The format() function formats output of strings.
# 
# 07. The input() function reads input and returns as a string.
# 
# 08. The len() function returns the length of an object.
# 
# 09. The list() function creates a list from a sequence of values.
# 
# 10. The max() function returns the item in a list of values having
#     the maximum value. 
# 
# 10. The min() function returns the item in a list of values having
#     the minimum value. 
# 
# 11. The open() function opens a file.
# 
# 12. The print() function prints content to screen.
# 
# 13. The sorted() function prints a sorted version of an iterable.
# 
# 14. The tuple() function creates a tuple.
# 
# 15. The type() function checks the type of an object.
# ==================================================================

# main method ...

def main():

    print("--- Enter TestFunctionsBuiltin.main()        ... ");
    print("--- ======================================== ... ");

    # Exercise abs() function ....

    print("--- ");
    print("--- Exercise abs() function ...");
    print("--- ");

    # Integer number

    num = -10
    print('---   Absolute value of -10 is:', abs(num))

    # Floating-point number

    fnum = -3.141
    print('---   Absolute value of -3.141 is:', abs(fnum))

    # Complex number

    cnum = 1 + 2j
    print('---   Absolute value of 1 + 2j is:', abs(cnum))

    # Exercise all() function ....

    print("--- ");
    print("--- Exercise all() function ...");
    print("--- ");

    testlist01 = [True, True, True, True]
    testlist02 = [True, False, True]

    print ("---   Testlist01: %s ..." %( testlist01 ))
    print ("---   all(testlist01) --> %s ..." %( all(testlist01) ))
    print ("---   Testlist02: %s ..." %( testlist02 ))
    print ("---   all(testlist02) --> %s ..." %( all(testlist02) ))

    # Exercise any() function ....

    print("--- ");
    print("--- Exercise any() function ...");
    print("--- ");

    testlist01 = [False, False, False, False]
    testlist02 = [False,  True,  True, False]

    print ("---   Testlist01: %s ..." %( testlist01 ))
    print ("---   Testlist02: %s ..." %( testlist02 ))
    print ("---   any(testlist01) --> %s ..." %( any(testlist01) ))
    print ("---   any(testlist02) --> %s ..." %( any(testlist02) ))

    # Exercise dict() function ....

    print("--- ");
    print("--- Exercise dict() function ...");
    print("--- ");

    city01 = dict( name = "Baltimore",
                   latitude  = 39.299,
                   longitude = -76.609,
                   state   = "Maryland",
                   country = "USA")

    print ("---    city01: %s ..." %( city01 ))

    # Access items in dictionary ...

    print ("---    Access items in city01 ...")
    print ("---    Name      --> %s ..." %( city01.get("name") ))
    print ("---    State     --> %s ..." %( city01.get("state") ))
    print ("---    Country   --> %s ..." %( city01.get("country") ))
    print ("---    Latitude  --> %8.3f ..." %( city01.get("latitude") ))
    print ("---    Longitude --> %8.3f ..." %( city01.get("longitude") ))

    # Exercise float() function ....

    print("--- ");
    print("--- Exercise float() function ...");
    print("--- ");

    x01 = 3; x02 = 3.141; x03 = "3.141"

    print ("---    Integer to float: %d --> %.3f ..." %( x01, float(x01) ))
    print ("---    Float to float: %.2f --> %.3f ..." %( x02, float(x02) ))
    print ("---    String to float: %s --> %.3f ..." %( x03, float(x03) ))

    # Exercise format() function ....

    print("--- ");
    print("--- Exercise format() function ...");
    print("--- ");

    x01 = 3; x02 = 3.1415926; x03 = "3.1415926"

    # Integer, floating point and exponential formats ...

    print("---    Integer format: {:d}".format(x01));
    print("---    Integer format: {:5d}".format(x01));
    print("---    Floating point format: {:.2f}".format(x02));
    print("---    Floating point format: {:.4f}".format(x02));
    print("---    Floating point format: {:.6f}".format(x02));
    print("---    Exponential format: {:.2e}".format(x02));
    print("---    String format: {:s}".format(x03));

    # Use precision variable ...

    print("--- ");
    print("---    Use of precision variable ...");
    print("--- ");

    precision = 5
    print("---    Floating point format: {:.{}f}".format(x02, precision));
    print("---    Exponential format: {:.{}e}".format(x02, precision));
    print("---    String format: {:.{}s}".format(x03, precision));

    # Exercise input() function ....

    print("--- ");
    print("--- Exercise input() function ...");
    print("--- ");

    x = input('---    Enter your name:')
    print('---    Hello, ' + x)

    # Exercise len() function ....

    print("--- ");
    print("--- Exercise len() function ...");
    print("--- ");

    testlist03 = ["apple", "banana", "cherry", "grape" ]
    print ("---   Testlist03: %s ..." %( testlist03 ))
    print ("---   len(testlist03) --> %d ..." %( len(testlist03) ))

    # Exercise list() function ....

    print("--- ");
    print("--- Exercise list() function ...");
    print("--- ");

    list01 = list(( "apple", 40, True, 2.5, False ))
    print ("---    List01 (defined with constructor): %s ..." %( list01 ))

    # Exercise max() and min() functions ....

    print("--- ");
    print("--- Exercise max() and min() functions ...");
    print("--- ");

    list02 = list(( "apple", "banana", "cherry", "avacado" ))
    print("---    List02: %s ..." %( list02 ))
    print("---    max(list02) --> %s ..." %( max(list02) ))
    print("---    min(list02) --> %s ..." %( min(list02) ))

    list03 = list(( 0.0, 6.0, 12.0, -120.0, 13.0, 100.0 ))
    print("---    List03: %s ..." %( list03 ))
    print("---    max(list03) --> {:8.2f} ...".format( max(list03) ))
    print("---    min(list03) --> {:8.2f} ...".format( min(list03) ))

    # Exercise sorted() function ....

    print("--- ");
    print("--- Exercise sorted() function ...");
    print("--- ");

    print("---    sorted(list02) --> %s ..." %( sorted(list02) ))
    print("---    sorted(list03) --> %s ..." %( sorted(list03) ))

    # Exercise tuple() function ....

    print("--- ");
    print("--- Exercise tuple() function ...");
    print("--- ");

    tuple01 = ( "apple", "banana", "avacado" );
    tuple02 = ( "cheese", "bread", "milk" );

    print('---    Tuple01: {}'.format(tuple01) )
    print('---    Tuple02: {}'.format(tuple02) )
    print('---    Concatenate: tuple01 + tuple02 --> {}'.format(tuple01 + tuple02) )

    tuple03 = ( 1, 2, 3 );
    tuple04 = ( 4, 5, 6 );
    print('---    Tuple03: {}'.format(tuple03) )
    print('---    Tuple04: {}'.format(tuple04) )
    print('---    Concatenate: tuple03 + tuple04 --> {}'.format(tuple03 + tuple04) )

    # Exercise type() function ....

    print("--- ");
    print("--- Exercise type() function ...");
    print("--- ");

    print("---    type(x01)     --> %s ..." %( type(x01) ))
    print("---    type(x02)     --> %s ..." %( type(x02) ))
    print("---    type(x03)     --> %s ..." %( type(x03) ))
    print("---    type(list01)  --> %s ..." %( type(list01) ))
    print("---    type(tuple01) --> %s ..." %( type(tuple01) ))

    print("--- ======================================== ... ");
    print("--- Leave TestFunctionsBuiltin.main()        ... ");

if __name__ == "__main__":
    main()
