# =======================================================================
# Demonstrate capabilities of prettytable library ...
#
# Installation: pip3 install prettytable
#
# Written by: Mark Austin                                    January 2025
# =======================================================================

from prettytable import PrettyTable 

# main method ...

def main():

    print("--- Enter TestPrettyTable01.main()           ... ");
    print("--- ======================================== ... ");

    # Part 1: Row-wise assembly of a table ...

    print("--- ");
    print("--- Part 1: Row-wise assembly of table01 ... ");
    print("--- ");

    table01 = PrettyTable(["Student Name", "Student ID", "Class", "Total Score (%)", "Grade" ]) 

    # format table ...

    table01.float_format = ".2"          # format floating point numbers to 2 decimal places ...
    table01.align["Student Name"] = "r"  # alignment of student name column ...
  
    # Add rows 

    table01.add_row([    "Amy", "2456", "ENCE 201", 82.4,  "A-"  ]) 
    table01.add_row([    "Joe", "5602", "ENCE 201", 42.4,  "D"   ]) 
    table01.add_row([   "John", "2222", "ENCE 201", 51.0,  "C-"  ]) 
    table01.add_row(["Leonard", "1234", "ENCE 201", 81.2,  "A"   ]) 
    table01.add_row([  "Maria", "3434", "ENCE 201", 98.0,  "A+"  ])

    # Print table ...
  
    print( table01 )

    print("--- ");
    print("--- Part 2: Column-wise assembly of table02 ... ");
    print("--- ");

    columns = ["Student Name", "Student ID", "Class", "Total Score", "Grade" ]
  
    table02 = PrettyTable() 
  
    # Add Columns 

    table02.add_column( "Student Name", [     "Amy",      "Joe",     "John",  "Leonard",    "Maria" ]) 
    table02.add_column(   "Student ID", [      2456,       5602,       2222,       1234,       3434 ]) 
    table02.add_column(        "Class", ["ENCE 201", "ENCE 201", "ENCE 201", "ENCE 201", "ENCE 201" ]) 
  
    print(table02)

    print("--- ");
    print("--- Part 3: Delete Joe from table01 ... ");
    print("--- ");

    table01.del_row(1)
    print( table01 )

    print("--- ");
    print("--- Part 4: Sort rows by student ID ... ");
    print("--- ");

    print ( table01.get_string(sortby="Student ID", reversesort=False ) )

    print("--- ");
    print("--- Part 5: Only print second and third rows of table01 ... ");
    print("--- ");

    print ( table01.get_string(start=1,end=3) )

    print("--- ======================================== ... ");
    print("--- Leave TestPrettyTable01.main()           ... ");

# Main function ...

if __name__ == "__main__":
    main()
