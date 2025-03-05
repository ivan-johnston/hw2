# ===============================================================
# TestList01.py: A list is a collection that is ordered
# and changeable. Lists allow duplicate members.
# 
# Last Modified: February 2024. 
# ===============================================================

# main method ...

def main():
    print("--- Enter TestList01.main()                  ... ");
    print("--- ======================================== ... ");

    # Create working lists ...

    list01 = [ "apple", "orange", "avocado", "banana", "grape", "watermelon"]
    list02 = [ "apple", "avocado", "banana", "banana", "grape", "watermelon"]

    print ("--- List01: {:s} ...".format( str( list01) ))
    print ("--- List02: {:s} ...".format( str( list02) ))

    # Compute and print list length ...

    print ("--- Length List01: {:d} ...".format( len(list01) ))
    print ("--- Length List02: {:d} ...".format( len(list02) ))

    # Create list with mix of data types ...

    list03 = [ "apple", 40, True, 2.5 ]
    print ("--- List03 (with multiple data types): %s ..." %( list03 ))

    # Use constructor function to create a list ...

    list04 = list(( "apple", 40, True, 2.5, False ))
    print ("--- List04 (defined with constructor): %s ..." %( list04 ))

    # Access list items ...

    print ("--- Access list items ...")
    print ("---   list04[0]: %s ..." %( list04[0] ))
    print ("---   list04[1]: %s ..." %( list04[1] ))
    print ("---   list04[2]: %s ..." %( list04[2] ))
    print ("---   list04[3]: %s ..." %( list04[3] ))
    print ("---   list04[4]: %s ..." %( list04[4] ))

    # Change range of items in list ...

    print ("--- Replace second and third values ...")

    list04[1:3] = ["newfirst","newsecond"]
    print ("--- List04 (revised): %s ..." %( list04 ))

    # Append items to list ...

    list01.append("cherry")
    list01.append("strawberry")

    print ("--- List01 (extended): %s ..." %( list01 ))

    # Concatenate two lists ...

    print ("--- Concatenate list items ...")

    list05 = [ "A", "B", "C" ]
    list06 = [ "D", "E", "F" ]

    print ("--- List05: %s ..." %( list05 ))
    print ("--- List06: %s ..." %( list06 ))

    list05.extend(list06)

    print ("--- List05.extend(list06): %s ..." %( list05 ))

    # Remove item from list ...

    print ("--- Remove avocado and strawberry items from list01 ...")

    list01.remove("avocado")
    list01.remove("strawberry")

    print ("--- List01 (no avocado): %s ..." %( list01 ))

    # Use for loop to traverse items from a list ...

    print ("--- Traverse list with for loop ...")

    for i in range(len( list01 )):
       print ("---   list01[%d]: %s ..." %( i, list01[i] ))

    print ("--- Traverse list with while loop ...")

    i = 0
    while i < len(list01):
       print ("---   list01[%d]: %s ..." %( i, list01[i] ))
       i = i + 1

    print ("--- Sort items in list ...")

    list01.sort()

    i = 0
    while i < len(list01):
       print ("---   list01[%d]: %s ..." %( i, list01[i] ))
       i = i + 1

    print ("--- Sort items (descending order) ...")

    list01.sort(reverse = True )

    i = 0
    while i < len(list01):
       print ("---   list01[%d]: %s ..." %( i, list01[i] ))
       i = i + 1

    print("--- ======================================== ... ");
    print("--- Leave TestList01.main()                  ... ");

# call the main method ...

main()
