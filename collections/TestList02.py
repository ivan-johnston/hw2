# ===============================================================
# TestList02.py: Create a list of fictional cartoon characters.
# 
# Last Modified: August 2022. 
# ===============================================================

from Person import Person

# main method ...

def main():
    print("--- Enter TestList02.main()                  ... ");
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
    person03.setSSN(1230)

    person04 = Person( "Yogi", "Bear" )
    person04.setAge(65)
    person04.setSSN(1111)

    person05 = Person( "Charlie", "Brown" )
    person05.setAge(72)
    person05.setSSN(1111)

    print ("--- Part 02: Object sample ...")

    print("--- person01 --> {:s} ...".format ( person01.__str__() ))
    print("--- person02 --> {:s} ...".format ( person02.__str__() ))
    print("--- person03 --> {:s} ...".format ( person03.__str__() ))
    print("--- person04 --> {:s} ...".format ( person04.__str__() ))
    print("--- person05 --> {:s} ...".format ( person05.__str__() ))

    # Assemble list of cartoon characterse ...

    print ("--- Part 03: Assemble list of objects ...")

    list01 = []
    list01.append( person01 )
    list01.append( person02 )
    list01.append( person03 )
    list01.append( person04 )
    list01.append( person05 )

    # Traverse list ...

    print ("--- Part 04: Traverse list of cartoon characters ...")

    i = 0
    for person in list01:
       print ("---   list01[%d]: %s --> %s ..."
                 %( i, person.getFirstName(), person.getAge() ))
       i = i + 1

    print("--- ======================================== ... ");
    print("--- Leave TestList02.main()                  ... ");

# call the main method ...

main()
