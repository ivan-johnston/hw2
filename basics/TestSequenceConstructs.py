# ===================================================================
# TestSequenceConstructs.py: Test sequencing constructs ...
# 
# Notes: 
# 
# 1. A sequence is an ordered collection of items, meaning
#    that you can access individual items by their position
#    (index) in the sequence.  
#  
# 2. Key characteristics of sequences:
#   
#    -- Ordered: Items are stored in a specific order, and   
#       that order is maintained.   
#    -- Indexable: You can access items using integer indecies,   
#       starting from 0.   
#    -- Iterable: You can loop through the sequence using a for loop.   
#    -- Sliceable: You can extract a portion of the sequence using    
#       slicing.   
#    -- Length: You can determine the number of items in a sequence
#       by calling the len() function (a builtin function).   
#   
# 3. Common sequence types:   
#   
#    -- Strings: A sequence of characters enclosed by single or 
#       double quotes.   
#    -- Lists: A mutable sequence of any types of objects, enclosed
#       in square brackets.   
#    -- Tuples: An immutable sequence of any type of objects,
#       enclosed in parentheses.   
#   
# 4. Sequence Operations:
#   
#    -- The plus operator (+) joins two sequences in a process called    
#       concatenation.   
#    -- The operator (*) repeats a sequence an positive integer number
#       of times.   
#    -- mySeq[i] will return the i-th character of the sequence.
#   
# 5. Useful functions:
#   
#    -- mySeq.index(x) returns the index of the first of x in mySeq.   
#    -- min(mySeq) and max(mySeq) 
#    -- mySeq.count(x) returns the number of occurrences of x in mySeq.
#   
# 6. Definitions:
#   
#    -- Mutable sequences: Lists are mutable, meaning that you can 
#       change the elements after they have been created.   
#    -- Immutable sequences: Strings and tuples are immutable, meaning
#       that you cannot modify their elements.   
#   
# ===================================================================

# main method ...

def main():
    print("--- Enter TestSequenceConstructs.main()      ... ");
    print("--- ======================================== ... ");

    # Generate character strings ...

    stringA = "ABCDE";
    stringB = "The cat in the hat";
    stringC = "Dr Seuss";

    # Generate numerical lists ...

    listA = [1, 2, 3, 4];
    listB = [5, 6, 7, 8];

    # Exercise string statement ...

    print("--- ");
    print("--- Exercise string statements ... ");
    print("--- ");

    print(stringA)                                 # <--- basic print.
    print(stringB)                                 # <--- basic print.
    print("--- StringA: {:s} ...".format(stringA)) # <--- formatted print.
    print("--- StringB: {:s} ...".format(stringB)) # <--- formatted print.

    # Exercise list statements ...

    print("--- ");
    print("--- Build and print lists ... ");
    print("--- ");

    print(listA)                                        # <--- basic print.
    print(listB)                                        # <--- basic print.
    print("--- ListA: {:s} ...".format( str(listA) ))   # <--- formatted print.
    print("--- ListB: {:s} ...".format( str(listB) ))   # <--- formatted print.

    # Exercise slicing statement ...

    print("--- ");
    print("--- Demonstrate indexing of individual items ... ");
    print("--- ");

    print("--- listA[ 0] --> {:d} ...".format( listA[0] )) # <--- listA[0] ...
    print("--- listA[ 1] --> {:d} ...".format( listA[1] )) # <--- listA[1] ...
    print("--- listA[ 2] --> {:d} ...".format( listA[2] )) # <--- listA[2] ...
    print("--- listA[ 3] --> {:d} ...".format( listA[3] )) # <--- listA[3] ...

    print("--- listA[-1] --> {:d} ...".format( listA[-1] )) # <--- listA[-1] ...
    print("--- listA[-2] --> {:d} ...".format( listA[-2] )) # <--- listA[-2] ...
    print("--- listA[-3] --> {:d} ...".format( listA[-3] )) # <--- listA[-3] ...
    print("--- listA[-4] --> {:d} ...".format( listA[-4] )) # <--- listA[-4] ...

    print("--- ");
    print("--- Exercise slicing statement ... ");
    print("--- ");

    print("--- StringA[0:2]: {:s} ...".format(stringA[0:2])) # <--- slice [0:2] ...
    print("--- StringA[1:3]: {:s} ...".format(stringA[1:3])) # <--- slice [1:3] ...
    print("--- StringA[2:4]: {:s} ...".format(stringA[2:4])) # <--- slice [2:4] ...
    print("--- StringA[3:5]: {:s} ...".format(stringA[3:5])) # <--- slice [3:5] ...

    # Exercise concatenation statement ...

    print("--- ");
    print("--- Exercise list concatenation ... ");
    print("--- ");

    listC = listA + listB
    print("--- ListA + ListB: {:s} ...".format( str( listC ) ))

    stringD = stringB + " by " + stringC; 
    print("--- Concatenate: stringB and stringC: {:s} ...".format( str( stringD ) ))

    print("--- ");
    print("--- Exercise useful functions ... ");
    print("--- ");

    # Exercise useful functions ...

    print("--- StringB: --> no of c's = {:d} ...".format(stringB.count('c'))) 
    print("--- StringB: --> no of a's = {:d} ...".format(stringB.count('a'))) 
    print("--- StringB: --> no of t's = {:d} ...".format(stringB.count('t'))) 

    print("--- min(listC) --> {:d} ...".format( min(listC) )) 
    print("--- max(listC) --> {:d} ...".format( max(listC) )) 

    print("--- ======================================== ... ");
    print("--- Leave TestSequenceConstructs.main()      ... ");

if __name__ == "__main__":
    main()

