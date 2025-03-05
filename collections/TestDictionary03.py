# ===============================================================
# TestDictionary03.py: Create dictionary of objects ...
# 
# Last Modified:                                    February 2023
# ===============================================================

from Person import Person

# main method ...

def main():
    print("--- Enter TestDictionary03.main()    ... ");
    print("--- ======================================== ... ");

    # Create cartoon characters ...

    print ("--- Part 01: Create cartoon character objects ...")

    person01 = Person( "Max", "Headroom" )
    person01.setAge(42)
    person01.setSSN(1980)

    person02 = Person( "Homer", "Simpson" )
    person02.setAge(55)
    person02.setSSN(1230)

    person03 = Person( "Bart", "Simpson" )
    person03.setAge(35)
    person03.setSSN(1231)

    person04 = Person( "Yogi", "Bear" )
    person04.setAge(65)
    person04.setSSN(1111)

    person05 = Person( "Charlie", "Brown" )
    person05.setAge(72)
    person05.setSSN(1012)

    print ("--- ")
    print ("--- Part 02: Print sample objects ...")
    print ("--- ")

    print("--- person01 --> {:s} ...".format(person01.__str__() ))
    print("--- person05 --> {:s} ...".format(person05.__str__() ))

    print ("--- ")
    print ("--- Part 03: Assemble dictionary of cartoon characters ...")

    cartoon = {}
    cartoon[ person01.getSSN() ] = person01
    cartoon[ person02.getSSN() ] = person02
    cartoon[ person03.getSSN() ] = person03
    cartoon[ person03.getSSN() ] = person03
    cartoon[ person04.getSSN() ] = person04
    cartoon[ person05.getSSN() ] = person05

    print ("--- ")
    print ("--- Part 04: Retrieve items from dictionary ...")
    print ("--- ")

    key = 1980
    personItem = cartoon.get(key)
    print("--- key = {:d} --> {:s} ...".format( key, personItem.__str__() ) )

    key = 1230
    personItem = cartoon.get(key)
    print("--- key = {:d} --> {:s} ...".format( key, personItem.__str__() ) )

    key = 1231
    personItem = cartoon.get(key)
    print("--- key = {:d} --> {:s} ...".format( key, personItem.__str__() ) )

    key = 1111
    personItem = cartoon.get(key)
    print("--- key = {:d} --> {:s} ...".format( key, personItem.__str__() ) )

    key = 1012
    personItem = cartoon.get(key)
    print("--- key = {:d} --> {:s} ...".format( key, personItem.__str__() ) )

    print ("--- ")
    print ("--- Part 04: Convert dictionary to list ...")

    keysList = list( cartoon.keys() )
    cartoonlist = [];
    for person in keysList:
       cartoonlist.append( cartoon.get(person) )

    print ("--- ")
    print ("--- Part 05: Sort list of cartoon items by age ...")
    print ("--- ")

    sorted_items = sorted( cartoonlist )

    i = 1
    for person in sorted_items:
       print ("---   person[%d]: %s --> %s ..." %( i, person.getFirstName(), person.getAge() ))
       i = i + 1

    print("--- ======================================== ... ");
    print("--- Leave TestDictionnary03.main()           ... ");

# call the main method ...

main()
