# =======================================================================
# Test arithmetic operators ...
# =======================================================================
# 
# Remarks:  
# 
# 1. Python supports three types of number: integers, floats and complex.
# 
# 2. Standard arithetic operators work as expected. 
# 
# 3. The modulo "%" operator returns the remainder after the first 
#    argument is divided by the second. Both args need to be integer 
#    values. For example, 7%3 = 2*3 + 1 --> return 1.
# 
# 4. The integer division “//” operator return the closest integer value
#    which is less than or equal to a specified expression or value. 
# 
# 5. Divide by zero and numerical overflow conditions need to be caught 
#    and processed as exceptions. 
# =======================================================================

# main method ...

def main():

    print("--- Enter TestArithmeticOperators.main()     ... ");
    print("--- ======================================== ... ");

    # Define three types of number ...

    print("--- ");
    print("--- Define three types of numbers ... ");
    print("--- ");

    x = 1          # int
    y = 3.1315936  # float
    z = 1 + 2j     # complex

    print(x)
    print(y)
    print(z)

    # Arithmetic with integers ...

    print("--- ");
    print("--- Arithmetic with Integers Results ... ");
    print("--- ");

    x = 1; y = 3; z = 7;
    print("--- x = {:2d}, y = {:2d}, z = {:2d}  ... ".format(x,y,z) );

    result = x + y;
    print("--- Addition: x + y --> {:2d} ... ".format(result) );
    result = x - y;
    print("--- Subtraction: x - y --> {:2d} ... ".format(result) );
    result = x * y;
    print("--- Multiplication: x * y --> {:2d} ... ".format(result) );
    result = x / y;
    print("--- Division: x / y --> {:.2f} ... ".format(result) );
    result = y**y;
    print("--- Power: y**y --> {:2d} ... ".format(result) );
    result = y**z;
    print("--- Power: y**z --> {:2d} ... ".format(result) );
    result = z**y;
    print("--- Power: z**y --> {:2d} ... ".format(result) );
    result = x % y;
    print("--- Modulo: x % y --> {:2d} ... ".format(result) );
    result = z % y;
    print("--- Modulo: z % y --> {:2d} ... ".format(result) );

    # Simulate Integer Division ...

    print("--- ");
    print("--- Simulate Integer Division ... ");
    print("--- ");

    result = x // y;
    print("--- Integer Division: x // y --> {:.2f} ... ".format(result) );
    result = y // z;
    print("--- Integer Division: y // z --> {:.2f} ... ".format(result) );
    result = z // y;
    print("--- Integer Division: z // y --> {:.2f} ... ".format(result) );

    # Floating-point Arithmetic ...

    print("--- ");
    print("--- Floating-point Arithmetic ... ");
    print("--- ");

    x = 1.5; y = 3.6; z = 5.0;
    print("--- x = {:.2f}, y = {:.2f}, z = {:.2f}  ... ".format(x,y,z) );

    result = x + y;
    print("--- Addition: x + y --> {:.2f} ... ".format(result) );
    result = x - y;
    print("--- Subtraction: x - y --> {:.2f} ... ".format(result) );
    result = x * y;
    print("--- Multiplication: x * y --> {:.2f} ... ".format(result) );
    result = x / y;
    print("--- Division: x / y --> {:.2f} ... ".format(result) );
    result = x**x;
    print("--- Power: x**x --> {:.5f} ... ".format(result) );
    esult = y**y;
    print("--- Power: y**y --> {:.2f} ... ".format(result) );
    result = z**z;
    print("--- Power: z**z --> {:.2f} ... ".format(result) );

    print("--- ");
    print("--- Simulate and catch divide-by-zero error condition ... ");
    print("--- ");

    x = 0.0; y = 3.6; z = 5.0;
    print("--- x = {:.2f}, y = {:.2f}, z = {:.2f}  ... ".format(x,y,z) );

    try:
       result = y / x;
       print("--- Division: y / x --> {:.2f} ... ".format(result) );
    except ZeroDivisionError:
       print("--- Division: y / x --> Error: divide by zero ... ");

    print("--- ");
    print("--- Simulate and catch numerical overflow error condition ... ");
    print("--- ");

    i=1
    f = 3.0**i
    for i in range(10):
        print("--- i = {:3d}, f = {:.2e} ".format(i,f) );
        try:
            f = f ** 2
        except OverflowError as err:
            print("--- Numerical Overflow error ... ");

    # Complex number Arithmetic ...

    print("--- ");
    print("--- Complex number arithmetic ... ");
    print("--- ");

    a = 1 + 3j  # complex number
    b = 1 - 2j  # complex number
   
    print('--- a: {:.2f}'.format(a))
    print('--- b: {:.2f}'.format(b))

    result = a + b;
    print("--- Addition: a + b --> {:.2f} ... ".format(result) );
    result = a - b;
    print("--- Subtraction: a - b --> {:.2f} ... ".format(result) );
    result = a * b;
    print("--- Multiplication: a * b --> {:.2f} ... ".format(result) );
    result = a / b;
    print("--- Division: a / b --> {:.2f} ... ".format(result) );

    print("--- ======================================== ... ");
    print("--- Leave TestArithmeticOperators.main()     ... ");

if __name__ == "__main__":
    main()
