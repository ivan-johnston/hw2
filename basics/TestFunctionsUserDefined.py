# ============================================================
# TestFunctionsUserDefined.py: Explore various ways of defining
# and using user-defined functions ...
# 
# November 2022. 
# ============================================================

# =======================================================
# Hello world function ....
# =======================================================

def hello_world_function():
  print("---    Hello World ...")

# =======================================================
# Function with a single argument ...
# =======================================================

def print_name01(firstName):
  print("---    Name:" + firstName + " Austin")

# =======================================================
# Function with two arguments ...
# =======================================================

def print_name02(firstName, familyName ):
    print("---    Name:" + firstName + " " + familyName )

# =======================================================
# Function with arbitrary number of keyword arguments ...
# =======================================================

def print_name03(**kid):
  print("---    First Name:" + kid["firstName"] )
  print("---    Family Name:" + kid["familyName"] )

# ===============================================
# Function with default parameter value ...
# ===============================================

def my_country(country = "USA"):
  print("---    I am from " + country)

# ===============================================
# Function to print list ...
# ===============================================

def print_shopping_list( food ):
  print("---    Shopping List ")
  print("---    -----------------------------------")

  for x in food:
    print("---    Item:" + x )

  print("---    -----------------------------------")

# ===============================================
# Function to return square of argument value ...
# ===============================================

def my_square_function(x):
  return x * x

# ==========================================
# Recursive Function ...
# ==========================================

def simple_recursion(k):
  if(k > 0):
    result = k + simple_recursion(k - 1)
    print("   --- Result: %.2f ..." % ( result ) )
  else:
    result = 0
  return result

# ==========================================
# main method ...
# ==========================================

def main():
    print("--- Enter TestFunctionsUserDefined.main()    ... ");
    print("--- ======================================== ... ");

    print("--- ")
    print("--- Exercise simplest function ...")
    print("--- ")

    hello_world_function();
    hello_world_function();

    print("--- ")
    print("--- Exercise function with an argument ...")
    print("--- ")

    print_name01("Nina");
    print_name01("Angela");

    print("--- ")
    print("--- Exercise function with two arguments ...")
    print("--- ")

    print_name02(  "Bart", "Simpson");
    print_name02( "Homer", "Simpson");

    print("--- ")
    print("--- Exercise functions with named arguments ...")
    print("--- ")

    print_name02(  firstName =    "Bart", familyName = "Simpson");
    print_name02( familyName = "Simpson",  firstName = "Bart" );

    print("--- ")
    print("--- Exercise function with arbitrary number of keyword arguments ...")
    print("--- ")

    print_name03( firstName = "Charlie", familyName = "Brown");
    print_name03( familyName =  "Bunny", firstName = "Bugs");

    print("--- ")
    print("--- Exercise function with default parameter value ...")
    print("--- ")

    my_country();
    my_country("Australia");

    print("--- ")
    print("--- Exercise function that passes list as argument ...")
    print("--- ")

    food = ["apples", "cheese", "crackers"];
    print_shopping_list( food );

    print("--- ")
    print("--- Exercise function with return value ...")
    print("--- ")

    x = 2.0;
    print("---    Input: {:.2f} --> squared: {:5.2f} ...".format( x, my_square_function(x)) )
    x = 3.0;
    print("---    Input: {:.2f} --> squared: {:5.2f} ...".format( x, my_square_function(x)) )
    x = 4.0;
    print("---    Input: {:.2f} --> squared: {:5.2f} ...".format( x, my_square_function(x)) )

    print("--- ")
    print("--- Exercise simple recursive function ...")
    print("--- ")

    simple_recursion(5);

    print("--- ======================================== ... ");
    print("--- Leave TestFunctionsUserDefined.main()    ... ");

if __name__ == "__main__":
    main()

