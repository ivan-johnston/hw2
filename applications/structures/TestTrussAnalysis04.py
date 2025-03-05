# ===============================================================
# TestTrussAnalysis04.py: Compute distribution of element forces
# and support reactions in a 19-bar crane truss.
# 
# Written by: Mark Austin                              April 2024 
# ===============================================================

import math            
import numpy as np  
from numpy.linalg import matrix_rank

# ===============================================================
# Function to print one- and two-dimensional matrices ...
# ===============================================================

def PrintMatrix(name, matrix):
    NoColumns = 6;

    # Compute no of blocks of rows to be printed .....

    if matrix.ndim == 1:
       noMatrixRows = matrix.shape[0]
       noMatrixCols = 1

    if matrix.ndim == 2:
       noMatrixRows = matrix.shape[0]
       noMatrixCols = matrix.shape[1]

    #  Compute number of blocks to be printed ...

    if noMatrixCols % NoColumns == 0:
       iNoBlocks = noMatrixCols/NoColumns;
    else:
       iNoBlocks = noMatrixCols/NoColumns + 1;

    #  Loop over the number of blocks ...

    for ib in range( int(iNoBlocks) ):
        iFirstColumn = ib*NoColumns + 1
        iLastColumn  = min ( (ib+1)*NoColumns, noMatrixCols )

        # Print title of matrix at top of each block ....

        print("Matrix: {:s} ".format(name) );

        # Label row and column nos */

        print("row/col     ", end="")
        colList = range(iFirstColumn, iLastColumn + 1)
        for col in [ *colList ]:
            print("       {:3d}    ".format(col),end="")
        print("")

        # Loop over rows and print matrix elements ....

        ii = 1
        for row in matrix:
            print(" {:3d}     ".format(ii),end="")
            colList = range( iFirstColumn, iLastColumn + 1)
            for col in [ *colList ]:
                if matrix.ndim == 1:
                   print(" {:12.5e} ".format( matrix[ii-1] ), end="")
                else:
                   print(" {:12.5e} ".format(matrix[ii-1][col-1]), end="")
            print("")
            ii = ii + 1
        print("")


# ===============================================================
# Compute maximum and minumun of three numbers ...
# ===============================================================

def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

def minimum(a, b, c):
    list = [a, b, c]
    return min(list)

# ===============================================================
# Print element forces ...
# ===============================================================

def printElementForces(name, minF, maxF):
    if( minF < 0):
        print("---     Minimum {:s} = {:7.2f} (C) ... ".format( name, minF ) )
    else:
        print("---     Minimum {:s} = {:7.2f} (T) ... ".format( name, minF ) )

    if( maxF < 0):
        print("---     Maximum {:s} = {:7.2f} (C) ... ".format( name, maxF ) )
    else:
        print("---     Maximum {:s} = {:7.2f} (T) ... ".format( name, maxF ) )

# ===============================================================
# main method ...
# ===============================================================

def main():
    print("--- Enter TestTrussAnalysis04.main()         ... ");
    print("--- ======================================== ... ");

    print("--- ");
    print("--- Part 1: Initialize coefficients for matrix equations ... ");

    nonodes  = 11;  # <--- no of nodes in crane structure ...
    maxterms =  4;  # <--- max no terms in an equation of equilibrium ...

    # Equilibrium and destination arrays ...

    equilibrium = np.zeros(( 2*nonodes, maxterms ))
    destination = np.zeros(( 2*nonodes, maxterms ))

    PrintMatrix("Equilibrium", equilibrium );
    PrintMatrix("Destination", destination );

    # Node A ...

    equilibrium[0][0] = 1   # < --- equilibrium in x direction ...
    equilibrium[0][1] = 1

    destination[0][0] =  8;
    destination[0][1] = 20;

    equilibrium[1][0] = 1   # < --- equilibrium in y direction ...
    equilibrium[1][1] = 1           

    destination[1][0] =  1;
    destination[1][1] = 21;

    # Node B ...

    equilibrium[2][0] = 1    # < --- equilibrium in x direction ...
    equilibrium[2][1] = 1/math.sqrt(2)           

    destination[2][0] = 8;
    destination[2][1] = 9;

    equilibrium[3][0] = 1    # < --- equilibrium in y direction ...
    equilibrium[3][1] = 1/math.sqrt(2)           
    equilibrium[3][2] = 1

    destination[3][0] =  2;
    destination[3][1] =  9;
    destination[3][2] = 22;

    # Node C ...

    equilibrium[4][0] = 1/math.sqrt(2) # <--- equilibrium in x direction ...
    equilibrium[4][1] = 1
    equilibrium[4][2] = 1/math.sqrt(2)           

    destination[4][0] =  9;
    destination[4][1] = 10;
    destination[4][2] = 11;

    equilibrium[5][0] =  1              # <--- equilibrium in y direction ...
    equilibrium[5][1] = -1
    equilibrium[5][2] =  1/math.sqrt(2)           
    equilibrium[5][3] = -1/math.sqrt(2)           

    destination[5][0] =  1;
    destination[5][1] =  3;
    destination[5][2] =  9;
    destination[5][3] = 11;

    # Node D ...

    equilibrium[6][0] =  1; # <--- equilibrium in x direction ...
    destination[6][0] = 10;

    equilibrium[7][0] =  1; # <--- equilibrium in y direction ...
    equilibrium[7][1] = -1;

    destination[7][0] = 2;
    destination[7][1] = 4;

    # Node E ...

    equilibrium[8][0] = 1                 # <--- equilibrium in x direction ...
    equilibrium[8][1] = 2/math.sqrt(5)

    destination[8][0] = 12;
    destination[8][1] = 16;

    equilibrium[9][0] = -1/math.sqrt(5)   # <--- equilibrium in y direction ...
    destination[9][0] = 16;

    # Node F ...

    equilibrium[10][0] =  1     # <--- equilibrium in x direction ...
    equilibrium[10][1] = -1  

    destination[10][0] = 12;
    destination[10][1] = 13;

    equilibrium[11][0] = -1     # <--- equilibrium in y direction ...
    destination[11][0] =  5;

    # Node G ...

    equilibrium[12][0] =  1     # <--- equilibrium in x direction ...
    equilibrium[12][1] = -1
    equilibrium[12][2] =  2/math.sqrt(5)

    destination[12][0] = 13;
    destination[12][1] = 14;
    destination[12][2] = 18;

    equilibrium[13][0] = -1;     # <--- equilibrium in y direction ...
    equilibrium[13][1] =  1;
    equilibrium[13][2] =  1/math.sqrt(5);

    destination[13][0] =  3;
    destination[13][1] =  6;
    destination[13][2] = 18;

    # Node H ...

    equilibrium[14][0] =  1/math.sqrt(2);  # <--- equilibrium in x direction ...
    equilibrium[14][1] =  1;
    equilibrium[14][2] =  1/math.sqrt(2);

    destination[14][0] = 11;
    destination[14][1] = 14;
    destination[14][2] = 19;

    equilibrium[15][0] =   1               # <--- equilibrium in y direction ...
    equilibrium[15][1] =   1/math.sqrt(2);
    equilibrium[15][2] =  -1
    equilibrium[15][3] =  -1/math.sqrt(2);

    destination[15][0] =   4;
    destination[15][1] =  11;
    destination[15][2] =   7;
    destination[15][3] =  19;
   
    # Node I ...

    equilibrium[16][0] =  2/math.sqrt(5);  # <--- equilibrium in x direction ...
    equilibrium[16][1] = -2/math.sqrt(5); 
    equilibrium[16][2] = -2/math.sqrt(5); 

    destination[16][0] = 16;
    destination[16][1] = 17;
    destination[16][2] = 18;

    equilibrium[17][0] =  1;               # <--- equilibrium in y direction ...
    equilibrium[17][1] =  1/math.sqrt(5); 
    equilibrium[17][2] = -1/math.sqrt(5); 
    equilibrium[17][3] =  1/math.sqrt(5); 

    destination[17][0] =  5;
    destination[17][1] = 16;
    destination[17][2] = 17;
    destination[17][3] = 18;

    # Node J ...

    equilibrium[18][0] =  1;               # <--- equilibrium in x direction ...
    equilibrium[18][1] = -2/math.sqrt(5); 
    equilibrium[18][2] =  1/math.sqrt(2); 

    destination[18][0] = 15;
    destination[18][1] = 17;
    destination[18][2] = 19;

    equilibrium[19][0] =  1;               # <--- equilibrium in y direction ...
    equilibrium[19][1] =  1/math.sqrt(5); 
    equilibrium[19][2] =  1/math.sqrt(2); 

    destination[19][0] =  6;
    destination[19][1] = 17;
    destination[19][2] = 19;

    # Node K ...

    equilibrium[20][0] =  1;               # <--- equilibrium in x direction ...
    destination[20][0] = 15;

    equilibrium[21][0] =  1;               # <--- equilibrium in y direction ...
    destination[21][0] =  7;

    PrintMatrix("Equilibrium", equilibrium );
    PrintMatrix("Destination", destination );

    print("--- ");
    print("--- Part 2: Systematically Assemble Matrix A ... ");
    print("--- ");

    # Allocate memory for A matrix ...

    A = np.zeros(( 2*nonodes, 2*nonodes ))

    # Systematically assemble A matrix from equilibrium and destination arrays ...

    for row in range(2*nonodes):
        print("--- ");
        for col in range(maxterms):
            eitem = equilibrium[row][col];
            ditem = int( destination[row][col] );
            if eitem != 0 or ditem != 0:
                print("--- (row,col) --> {:2d}, {:d}: eitem --> {:9.5f}, ditem --> {:3d} ...".format( row, col, eitem, ditem ) );
                A[row][ditem-1] = eitem;

    PrintMatrix("A", A);

    print("--- ");
    print("--- Part 2: Initialize 22x1 load vectors ... ");
    print("--- ");

    print("--- Load Case 1: Node e_y = -15 ...");

    B1 = np.zeros(( 2*nonodes, 1 ))
    B1[ 9][0] = -15.0;
    B1[11][0] =   0.0;

    PrintMatrix("Load Case 1:", B1);

    print("--- Load Case 2: Node e_y = -10, node f_y = -10 ...");

    B2 = np.zeros(( 2*nonodes, 1 ))
    B2[ 9][0] = -10.0;
    B2[11][0] = -10.0;

    PrintMatrix("Load Case 2:", B2);

    print("--- Load Case 5: Node f_y = -25 ...");

    B3 = np.zeros(( 2*nonodes, 1 ))
    B3[ 9][0] =   0.0;
    B3[11][0] = -25.0;

    PrintMatrix("Load Case 3:", B3);

    print("--- ");
    print("--- Part 4: Check properties of matrix A ... ");
    print("--- ");

    rank = matrix_rank(A)
    det  = np.linalg.det(A)

    print("--- Matrix A: rank = {:f}, det = {:f}  ...".format(rank, det) );

    print("--- ");
    print("--- Part 5: Solve A.F = B for three load cases ... ");
    print("--- ");

    F1 = np.linalg.solve(A, B1)
    PrintMatrix("Load Case 1: Forces ...", F1);

    F2 = np.linalg.solve(A, B2)
    PrintMatrix("Load Case 2: Forces ...", F2);

    F3 = np.linalg.solve(A, B3)
    PrintMatrix("Load Case 3: Forces ...", F3);

    print("--- ");
    print("--- Part 6: Print support reactions and element-level forces ... ");

    print("--- ");
    print("--- Support Reactions and Element-Level Forces: Load Case 1:");
    print("--- ");
    print("---   Reaction A: R_ax = {:7.2f} ... ".format( F1[19][0] ) );
    print("---             : R_ay = {:7.2f} ... ".format( F1[20][0] ) );
    print("---   Reaction D: R_dy = {:7.2f} ... ".format( F1[21][0] ) );
    print("--- ");
    print("--- Element Level Forces:");
    print("--- ");
    print("---   Element A-C: F1  = {:7.2f} ... ".format( F1[0][0] ) );
    print("---   Element B-D: F2  = {:7.2f} ... ".format( F1[1][0] ) );
    print("---   Element C-G: F3  = {:7.2f} ... ".format( F1[2][0] ) );
    print("---   Element D-H: F4  = {:7.2f} ... ".format( F1[3][0] ) );
    print("---   Element F-I: F5  = {:7.2f} ... ".format( F1[4][0] ) );
    print("---   Element G-J: F6  = {:7.2f} ... ".format( F1[5][0] ) );
    print("---   Element H-K: F7  = {:7.2f} ... ".format( F1[6][0] ) );
    print("---   Element A-B: F8  = {:7.2f} ... ".format( F1[7][0] ) );
    print("---   Element B-C: F09 = {:7.2f} ... ".format( F1[8][0] ) );
    print("---   Element C-D: F10 = {:7.2f} ... ".format( F1[9][0] ) );
    print("---   Element C-H: F11 = {:7.2f} ... ".format( F1[10][0] ) );
    print("---   Element E-F: F12 = {:7.2f} ... ".format( F1[11][0] ) );
    print("---   Element F-G: F13 = {:7.2f} ... ".format( F1[12][0] ) );
    print("---   Element G-H: F14 = {:7.2f} ... ".format( F1[13][0] ) );
    print("---   Element J-K: F15 = {:7.2f} ... ".format( F1[14][0] ) );
    print("---   Element E-I: F16 = {:7.2f} ... ".format( F1[15][0] ) );
    print("---   Element I-J: F17 = {:7.2f} ... ".format( F1[16][0] ) );
    print("---   Element G-I: F18 = {:7.2f} ... ".format( F1[17][0] ) );
    print("---   Element H-J: F19 = {:7.2f} ... ".format( F1[18][0] ) );

    print("--- ");
    print("--- Support Reactions and Element-Level Forces: Load Case 2:");
    print("--- ");
    print("---   Reaction A: R_ax = {:7.2f} ... ".format( F2[19][0] ) );
    print("---             : R_ay = {:7.2f} ... ".format( F2[20][0] ) );
    print("---   Reaction D: R_dy = {:7.2f} ... ".format( F2[21][0] ) );
    print("--- ");
    print("--- Element Level Forces:");
    print("--- ");
    print("---   Element A-C: F1  = {:7.2f} ... ".format( F2[0][0] ) );
    print("---   Element B-D: F2  = {:7.2f} ... ".format( F2[1][0] ) );
    print("---   Element C-G: F3  = {:7.2f} ... ".format( F2[2][0] ) );
    print("---   Element D-H: F4  = {:7.2f} ... ".format( F2[3][0] ) );
    print("---   Element F-I: F5  = {:7.2f} ... ".format( F2[4][0] ) );
    print("---   Element G-J: F6  = {:7.2f} ... ".format( F2[5][0] ) );
    print("---   Element H-K: F7  = {:7.2f} ... ".format( F2[6][0] ) );
    print("---   Element A-B: F8  = {:7.2f} ... ".format( F2[7][0] ) );
    print("---   Element B-C: F09 = {:7.2f} ... ".format( F2[8][0] ) );
    print("---   Element C-D: F10 = {:7.2f} ... ".format( F2[9][0] ) );
    print("---   Element C-H: F11 = {:7.2f} ... ".format( F2[10][0] ) );
    print("---   Element E-F: F12 = {:7.2f} ... ".format( F2[11][0] ) );
    print("---   Element F-G: F13 = {:7.2f} ... ".format( F2[12][0] ) );
    print("---   Element G-H: F14 = {:7.2f} ... ".format( F2[13][0] ) );
    print("---   Element J-K: F15 = {:7.2f} ... ".format( F2[14][0] ) );
    print("---   Element E-I: F16 = {:7.2f} ... ".format( F2[15][0] ) );
    print("---   Element I-J: F17 = {:7.2f} ... ".format( F2[16][0] ) );
    print("---   Element G-I: F18 = {:7.2f} ... ".format( F2[17][0] ) );
    print("---   Element H-J: F19 = {:7.2f} ... ".format( F2[18][0] ) );

    print("--- ");
    print("--- Support Reactions and Element-Level Forces: Load Case 3:");
    print("--- ");
    print("---   Reaction A: R_ax = {:7.2f} ... ".format( F3[19][0] ) );
    print("---             : R_ay = {:7.2f} ... ".format( F3[20][0] ) );
    print("---   Reaction D: R_dy = {:7.2f} ... ".format( F3[21][0] ) );
    print("--- ");
    print("--- Element Level Forces:");
    print("--- ");
    print("---   Element A-C: F1  = {:7.2f} ... ".format( F3[0][0] ) );
    print("---   Element B-D: F2  = {:7.2f} ... ".format( F3[1][0] ) );
    print("---   Element C-G: F3  = {:7.2f} ... ".format( F3[2][0] ) );
    print("---   Element D-H: F4  = {:7.2f} ... ".format( F3[3][0] ) );
    print("---   Element F-I: F5  = {:7.2f} ... ".format( F3[4][0] ) );
    print("---   Element G-J: F6  = {:7.2f} ... ".format( F3[5][0] ) );
    print("---   Element H-K: F7  = {:7.2f} ... ".format( F3[6][0] ) );
    print("---   Element A-B: F8  = {:7.2f} ... ".format( F3[7][0] ) );
    print("---   Element B-C: F09 = {:7.2f} ... ".format( F3[8][0] ) );
    print("---   Element C-D: F10 = {:7.2f} ... ".format( F3[9][0] ) );
    print("---   Element C-H: F11 = {:7.2f} ... ".format( F3[10][0] ) );
    print("---   Element E-F: F12 = {:7.2f} ... ".format( F3[11][0] ) );
    print("---   Element F-G: F13 = {:7.2f} ... ".format( F3[12][0] ) );
    print("---   Element G-H: F14 = {:7.2f} ... ".format( F3[13][0] ) );
    print("---   Element J-K: F15 = {:7.2f} ... ".format( F3[14][0] ) );
    print("---   Element E-I: F16 = {:7.2f} ... ".format( F3[15][0] ) );
    print("---   Element I-J: F17 = {:7.2f} ... ".format( F3[16][0] ) );
    print("---   Element G-I: F18 = {:7.2f} ... ".format( F3[17][0] ) );
    print("---   Element H-J: F19 = {:7.2f} ... ".format( F3[18][0] ) );

    print("--- ");
    print("--- Summary of Max/Min Reactions and Element-Level Forces ...");
    print("--- ----------------------------------------------------- ...");

    MinRax = minimum( F1[19][0], F2[19][0], F3[19][0] )
    MaxRax = maximum( F1[19][0], F2[19][0], F3[19][0] )

    MinRay = minimum( F1[20][0], F2[20][0], F3[20][0] )
    MaxRay = maximum( F1[20][0], F2[20][0], F3[20][0] )

    MinRby = minimum( F1[21][0], F2[21][0], F3[21][0] )
    MaxRby = maximum( F1[21][0], F2[21][0], F3[21][0] )

    print("--- ");
    print("---   Reaction A: Minimum R_ax = {:7.2f}, Maximum R_ax = {:7.2f} ... ".format( MinRax, MaxRax) )
    print("---             : Minimum R_ay = {:7.2f}, Maximum R_ay = {:7.2f} ... ".format( MinRay, MaxRay) )
    print("--- ");
    print("---   Reaction B: Minimum R_by = {:7.2f}, Maximum R_by = {:7.2f} ... ".format( MinRby, MaxRby) )

    MinF1 = minimum( F1[0][0], F2[0][0], F3[0][0] )
    MaxF1 = maximum( F1[0][0], F2[0][0], F3[0][0] )

    MinF2 = minimum( F1[1][0], F2[1][0], F3[1][0] )
    MaxF2 = maximum( F1[1][0], F2[1][0], F3[1][0] )

    MinF3 = minimum( F1[2][0], F2[2][0], F3[2][0] )
    MaxF3 = maximum( F1[2][0], F2[2][0], F3[2][0] )

    MinF4 = minimum( F1[3][0], F2[3][0], F3[3][0] )
    MaxF4 = maximum( F1[3][0], F2[3][0], F3[3][0] )

    MinF5 = minimum( F1[4][0], F2[4][0], F3[4][0] )
    MaxF5 = maximum( F1[4][0], F2[4][0], F3[4][0] )

    MinF6 = minimum( F1[5][0], F2[5][0], F3[5][0] )
    MaxF6 = maximum( F1[5][0], F2[5][0], F3[5][0] )

    MinF7 = minimum( F1[6][0], F2[6][0], F3[6][0] )
    MaxF7 = maximum( F1[6][0], F2[6][0], F3[6][0] )

    MinF8 = minimum( F1[7][0], F2[7][0], F3[7][0] )
    MaxF8 = maximum( F1[7][0], F2[7][0], F3[7][0] )

    MinF9 = minimum( F1[8][0], F2[8][0], F3[8][0] )
    MaxF9 = maximum( F1[8][0], F2[8][0], F3[8][0] )

    MinF10 = minimum( F1[9][0], F2[9][0], F3[9][0] )
    MaxF10 = maximum( F1[9][0], F2[9][0], F3[9][0] )

    MinF11 = minimum( F1[10][0], F2[10][0], F3[10][0] )
    MaxF11 = maximum( F1[10][0], F2[10][0], F3[10][0] )

    MinF12 = minimum( F1[11][0], F2[11][0], F3[11][0] )
    MaxF12 = maximum( F1[11][0], F2[11][0], F3[11][0] )

    MinF13 = minimum( F1[12][0], F2[12][0], F3[12][0] )
    MaxF13 = maximum( F1[12][0], F2[12][0], F3[12][0] )

    MinF14 = minimum( F1[13][0], F2[13][0], F3[13][0] )
    MaxF14 = maximum( F1[13][0], F2[13][0], F3[13][0] )

    MinF15 = minimum( F1[14][0], F2[14][0], F3[14][0] )
    MaxF15 = maximum( F1[14][0], F2[14][0], F3[14][0] )

    MinF16 = minimum( F1[15][0], F2[15][0], F3[15][0] )
    MaxF16 = maximum( F1[15][0], F2[15][0], F3[15][0] )

    MinF17 = minimum( F1[16][0], F2[16][0], F3[16][0] )
    MaxF17 = maximum( F1[16][0], F2[16][0], F3[16][0] )

    MinF18 = minimum( F1[17][0], F2[17][0], F3[17][0] )
    MaxF18 = maximum( F1[17][0], F2[17][0], F3[17][0] )

    MinF19 = minimum( F1[18][0], F2[18][0], F3[18][0] )
    MaxF19 = maximum( F1[18][0], F2[18][0], F3[18][0] )

    print("--- ");
    print("---   Element A-C: ")
    printElementForces( "F1", MinF1, MaxF1)

    print("---   Element B-D: ")
    printElementForces( "F2", MinF2, MaxF2)

    print("---   Element C-G: ")
    printElementForces( "F3", MinF3, MaxF3)

    print("---   Element D-H: ")
    printElementForces( "F4", MinF4, MaxF4)
 
    print("---   Element F-I: ")
    printElementForces( "F5", MinF5, MaxF5)

    print("---   Element G-J: ")
    printElementForces( "F6", MinF6, MaxF6)

    print("---   Element H-K: ")
    printElementForces( "F7", MinF7, MaxF7)

    print("---   Element A-B: ")
    printElementForces( "F8", MinF8, MaxF8)

    print("---   Element B-C: ")
    printElementForces( "F9", MinF9, MaxF9)

    print("---   Element C-D: ")
    printElementForces( "F10", MinF10, MaxF10)

    print("---   Element C-H: ")
    printElementForces( "F11", MinF11, MaxF11)

    print("---   Element E-F: ")
    printElementForces( "F12", MinF12, MaxF12)

    print("---   Element F-G: ")
    printElementForces( "F13", MinF13, MaxF13)

    print("---   Element G-H: ")
    printElementForces( "F14", MinF14, MaxF14)

    print("---   Element J-K: ")
    printElementForces( "F15", MinF15, MaxF15)

    print("---   Element E-I: ")
    printElementForces( "F16", MinF16, MaxF16)

    print("---   Element I-J: ")
    printElementForces( "F17", MinF17, MaxF17)

    print("---   Element G-I: ")
    printElementForces( "F18", MinF18, MaxF18)

    print("---   Element H-J: ")
    printElementForces( "F19", MinF19, MaxF19)

    print("--- ======================================== ... ");
    print("--- Leave TestTrussAnalysis02.main()         ... ");

# call the main method ...

main()
