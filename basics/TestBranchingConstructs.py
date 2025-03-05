# =========================================================
# TestBranchingConstructs.py: Test branching constructs ...
# 
# Notes: 
# 
# 1. The break statement is used to break out of a loop.
#    It is used inside for and while loops to affect normal
#    behavior.
# 
# 2. The continue keyword is used to end the current
#    iteration in a for loop or a while loop, and
#    continues to the next iteration. Continue statements
#    are a temporary break in a loop.
# 
# =========================================================

# main method ...

def main():
    print("--- Enter TestBranchingConstructs.main()     ... ");
    print("--- ======================================== ... ");

    # Exercise if-else statement ...

    print("--- ");
    print("--- Exercise if-else statement ... ");
    print("--- ");

    for i in range(1, 5):
        if i%2 == 1:
           print("---    i = {:3d} --> odd number ...".format(i) );
        else:
           print("---    i = {:3d} --> even number ...".format(i) );

    # Exercise if-elif-else statement ...

    print("--- ");
    print("--- Exercise if-elif-else statement ... ");
    print("--- ");

    for age in range(2, 21, 2):
        if age <= 5:
           print("---    age = {:3d} --> too young for school ...".format(age) );
        elif age > 5 and age < 10:
           print("---    age = {:3d} --> elementary school ...".format(age) );
        elif age >= 10 and age < 14:
           print("---    age = {:3d} --> middle school ...".format(age) );
        elif age >= 14 and age <= 18:
           print("---    age = {:3d} --> high school ...".format(age) );
        else:
           print("---    age = {:3d} --> tertiary education ...".format(age) );

    # Exercise break statement ...

    print("--- ");
    print("--- Exercise break statement ... ");
    print("--- ");

    for i in range(1, 10):
        if i == 4:
           break
        print("---    i = {:3d} ...".format(i) );

    # Exercise continue statement ...

    print("--- ");
    print("--- Exercise continue statement (skip odd numbers) ... ");
    print("--- ");

    for i in range(1, 10):
        if i%2 == 1:
           continue
        print("---    i = {:3d} ...".format(i) );

    print("--- ");
    print("--- Exercise continue statement (skip even numbers) ... ");
    print("--- ");

    for i in range(1, 10):
        if i%2 == 0:
           continue
        print("---    i = {:3d} ...".format(i) );


    print("--- ======================================== ... ");
    print("--- Leave TestBranchingConstructs.main()     ... ");

if __name__ == "__main__":
    main()

