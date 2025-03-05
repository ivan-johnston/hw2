# ===============================================================
# TestStringFormatting.py: Demonstrate the use of formatting ...
# 
# ===============================================================

# main method ...

def main():
    print("--- Enter TestStringFormatting.main()        ... ");
    print("--- ======================================== ... ");

    # Initialize variable as a string 

    variable = '15'
    string = "Variable as string = %s" %(variable) 
    print( string )
   
    # Printing as raw data 
    # Thanks to Himanshu Pant for this 

    print ("Variable as raw data = %r" %(variable))
     
    # Convert the variable to integer 
    # And perform check other formatting options 
   
    variable = int(variable) # Without this the below statement 
                             # will give error. 
    string = "Variable as integer = %d" %(variable) 

    print (string)
    print ("Variable as float = %f" %(variable))

    print("--- ======================================== ... ");
    print("--- Leave TestStringFormatting.main()        ... ");

if __name__ == "__main__":
    main()

