# ===============================================================
# TestSet01.py: A set is a collection that is unordered
# and unindexed. Duplicates are not permitted.
# 
# Set Methods: 
# 
# ===============================================================

# main method ...

def main():
    print("--- Enter TestSet01.main()                                 ... ");
    print("--- ====================================================== ... ");

    # Create working sets ...

    print ("--- Create working sets ...")

    set01 = { 1, 2, 3, 4, 5, 6, 7 }
    set02 = { 6, 7, 8, 9, 10 }
    set03 = {"apple", "banana", "cherry"}
    set04 = {True, False, False}

    print ("--- Set01: %s ..." %( set01 ))
    print ("--- Set02: %s ..." %( set02 ))
    print ("--- Set03: %s ..." %( set03 ))
    print ("--- Set04: %s ..." %( set04 ))

    # Create set with set constructor ...

    print ("--- ")
    print ("--- Create list with set constructor method ...")

    list01 = ("apple", "banana", "cherry")
    set05  = set( list01 ) # note the double round-brackets
    print ("--- Set05: %s ..." %( set05 ))

    # Check that duplicates are prevented ...

    print ("--- ")
    print ("--- Check that duplicates are prevented ...")

    set06 = { 1, 2, 3, 4, 5, 4, 3, 2 }
    print ("--- Set06: %s ..." %( set06 ))

    # Access items in set. Note: You cannot access items
    # in a set by referring to an index or a key.

    print ("--- Access items in set ...")
    print ("--- Set06: ...")
    for x in set06:
        print ("---   %s ..." %(x))

    # Add items to set, then print ...

    print ("--- ")
    print ("--- Add items to set, then print ...")

    set03.add("strawberry")
    set03.add("kiwi")
    print ("--- Set03 (appended): ...")
    for x in set03:
        print ("---   %s ..." %(x))

    # Remove items from set with pop() method ...

    print ("--- ")
    print ("--- Remove items from set with pop() method ...")

    print ("--- Set03.pop(): %s ..." %( set03.pop() ))
    print ("--- Set03.pop(): %s ..." %( set03.pop() ))
    print ("--- Set03.pop(): %s ..." %( set03.pop() ))
    print ("--- Set03.pop(): %s ..." %( set03.pop() ))
    print ("--- Set03.pop(): %s ..." %( set03.pop() ))

    # Set operations (union, intersection and difference) ...

    print ("--- ")
    print ("--- Set operation (union) ...")

    print ("--- Set01.union(Set02) : %s ..." %( set01.union(set02) ))
    print ("--- Set operation (intersection) ...")
    print ("--- Set01.intersection(Set02) : %s ..." %( set01.intersection(set02) ))
    print ("--- Set operation (difference) ...")
    print ("--- Set01.difference(Set02) : %s ..." %( set01.difference(set02) ))
    print ("--- Set02.difference(Set01) : %s ..." %( set02.difference(set01) ))

    # Check if Set01 and Set02 are disjoint sets

    print ("--- ")
    print ("--- Check if set01 and set02 are disjoint? ...")

    if set01.isdisjoint(set02):
       print("--- Set01 and Set02 have nothing in common ...")
    else:
       print("--- Set01 and Set02 are not disjoint ...")

    print("--- ====================================================== ... ");
    print("--- Leave TestSet01.main()                                 ... ");


# call the main method ...

main()
