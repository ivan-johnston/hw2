# ===============================================================
# TestTrussAnalysis03.py: Compute distribution of element forces
# and support reactions in a nine-bar truss.
# 
# --- Use lists for nodal equilibria and term destinations ...
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
    print("--- Enter TestTrussAnalysis02.main()         ... ");
    print("--- ======================================== ... ");

    print("--- ");
    print("--- Part 1: Initialize coefficients for matrix equations ... ");

    # Element and destination arrays ...

    nonodes  = 6;   # <-- number of nodes in structure ....
    maxterms = 3;
    equilibrium = np.zeros(( 2*nonodes, maxterms ))
    destination = np.zeros(( 2*nonodes, maxterms ))

    PrintMatrix("Equilibrium", equilibrium );
    PrintMatrix("Destination", destination );

    # Node A ...

    equilibrium[0][0] = 1               # < --- equilibrium in x direction ...
    equilibrium[0][1] = 1/math.sqrt(2) 
    equilibrium[0][2] = 1

    destination[0][0] = 1;
    destination[0][1] = 4;
    destination[0][2] = 10;

    equilibrium[1][0] = 1/math.sqrt(2)  # < --- equilibrium in y direction ...
    equilibrium[1][1] = 1

    destination[1][0] =  4;
    destination[1][1] = 11;
    destination[1][2] =  0;

    # Node B ...

    equilibrium[2][0] =  1       # < --- equilibrium in x direction ...
    equilibrium[2][1] = -1      

    destination[2][0] =  1;
    destination[2][1] =  2;

    equilibrium[3][0] = -1       # < --- equilibrium in y direction ...

    destination[3][0] =  5;

    # Node C ...

    equilibrium[4][0]  =  1       # < --- equilibrium in x direction ...
    equilibrium[4][1]  = -1    
    equilibrium[4][2]  =  1/math.sqrt(2)    

    destination[4][0] =  2;
    destination[4][1] =  3;
    destination[4][2] =  6;

    equilibrium[5][0] = -1/math.sqrt(2) # < --- equilibrium in y direction ...
    equilibrium[5][1] = -1              

    destination[5][0] =  6;
    destination[5][1] =  7;

    # Node D ...

    equilibrium[6][0] = 1               # < --- equilibrium in x direction ...
    equilibrium[6][1] = 1/math.sqrt(2) 

    destination[6][0] =  3;
    destination[6][1] =  8;

    equilibrium[7][0] = 1/math.sqrt(2)  # < --- equilibrium in y direction ...
    equilibrium[7][1] = 1

    destination[7][0] =  8;
    destination[7][1] = 12;

    # Node E ...

    equilibrium[8][0] =  1              # < --- equilibrium in x direction ...
    equilibrium[8][1] =  1/math.sqrt(2) 
    equilibrium[8][2] = -1/math.sqrt(2) 

    destination[8][0] =  9;
    destination[8][1] =  6;
    destination[8][2] =  4;

    equilibrium[9][0] =  1/math.sqrt(2) # < --- equilibrium in y direction ...
    equilibrium[9][1] =  1
    equilibrium[9][2] =  1/math.sqrt(2) 

    destination[9][0] =  4;
    destination[9][1] =  5;
    destination[9][2] =  6;

    # Node F ...

    equilibrium[10][0] = -1/math.sqrt(2)  # < --- equilibrium in x direction ...
    equilibrium[10][1] =  1

    destination[10][0] =  8;
    destination[10][1] =  9;

    equilibrium[11][0] = 1               # < --- equilibrium in y direction ...
    equilibrium[11][1] = 1/math.sqrt(2) 

    destination[11][0] =  7;
    destination[11][1] =  8;

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
    print("--- Part 2: Initialize load vectors ... ");
    print("--- ");

    print("--- Load Case 1: b4 = -10, b6 = 0 ...");

    B1 = np.zeros(( 2*nonodes, 1 ))
    B1[3][0] = -10.0
    B1[5][0] =   0.0

    PrintMatrix("Load Case 1: B", B1);

    print("--- Load Case 2: b4 = -5, b6 = -5 ...");

    B2 = np.zeros(( 2*nonodes, 1 ))
    B2[3][0] =  -5.0
    B2[5][0] =  -5.0

    PrintMatrix("Load Case 2: B", B2);

    print("--- Load Case 3: b4 = 0, b6 = -10 ...");

    B3 = np.zeros(( 2*nonodes, 1 ))
    B3[3][0] =  -0.0
    B3[5][0] = -10.0

    PrintMatrix("Load Case 3: B", B3);

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
    print("---   Reaction A: R_ax = {:7.2f} ... ".format( F1[9][0] ) );
    print("---             : R_ay = {:7.2f} ... ".format( F1[10][0] ) );
    print("---   Reaction D: R_dy = {:7.2f} ... ".format( F1[11][0] ) );
    print("--- ");
    print("--- Element Level Forces:");
    print("--- ");
    print("---   Element A-B: F1 = {:7.2f} ... ".format( F1[0][0] ) );
    print("---   Element B-C: F2 = {:7.2f} ... ".format( F1[1][0] ) );
    print("---   Element C-D: F3 = {:7.2f} ... ".format( F1[2][0] ) );
    print("---   Element A-E: F4 = {:7.2f} ... ".format( F1[3][0] ) );
    print("---   Element B-E: F5 = {:7.2f} ... ".format( F1[4][0] ) );
    print("---   Element C-E: F6 = {:7.2f} ... ".format( F1[5][0] ) );
    print("---   Element C-F: F7 = {:7.2f} ... ".format( F1[6][0] ) );
    print("---   Element D-F: F8 = {:7.2f} ... ".format( F1[7][0] ) );
    print("---   Element E-F: F9 = {:7.2f} ... ".format( F1[8][0] ) );

    print("--- ");
    print("--- Support Reactions and Element-Level Forces: Load Case 2:");
    print("--- ");
    print("---   Reaction A: R_ax = {:7.2f} ... ".format( F2[9][0] ) );
    print("---             : R_ay = {:7.2f} ... ".format( F2[10][0] ) );
    print("---   Reaction D: R_dy = {:7.2f} ... ".format( F2[11][0] ) );
    print("--- ");
    print("--- Element Level Forces:");
    print("--- ");
    print("---   Element A-B: F1 = {:7.2f} ... ".format( F2[0][0] ) );
    print("---   Element B-C: F2 = {:7.2f} ... ".format( F2[1][0] ) );
    print("---   Element C-D: F3 = {:7.2f} ... ".format( F2[2][0] ) );
    print("---   Element A-E: F4 = {:7.2f} ... ".format( F2[3][0] ) );
    print("---   Element B-E: F5 = {:7.2f} ... ".format( F2[4][0] ) );
    print("---   Element C-E: F6 = {:7.2f} ... ".format( F2[5][0] ) );
    print("---   Element C-F: F7 = {:7.2f} ... ".format( F2[6][0] ) );
    print("---   Element D-F: F8 = {:7.2f} ... ".format( F2[7][0] ) );
    print("---   Element E-F: F9 = {:7.2f} ... ".format( F2[8][0] ) );

    print("--- ");
    print("--- Support Reactions and Element-Level Forces: Load Case 3:");
    print("--- ");
    print("---   Reaction A: R_ax = {:7.2f} ... ".format( F3[9][0] ) );
    print("---             : R_ay = {:7.2f} ... ".format( F3[10][0] ) );
    print("---   Reaction D: R_dy = {:7.2f} ... ".format( F3[11][0] ) );
    print("--- ");
    print("--- Element Level Forces:");
    print("--- ");
    print("---   Element A-B: F1 = {:7.2f} ... ".format( F3[0][0] ) );
    print("---   Element B-C: F2 = {:7.2f} ... ".format( F3[1][0] ) );
    print("---   Element C-D: F3 = {:7.2f} ... ".format( F3[2][0] ) );
    print("---   Element A-E: F4 = {:7.2f} ... ".format( F3[3][0] ) );
    print("---   Element B-E: F5 = {:7.2f} ... ".format( F3[4][0] ) );
    print("---   Element C-E: F6 = {:7.2f} ... ".format( F3[5][0] ) );
    print("---   Element C-F: F7 = {:7.2f} ... ".format( F3[6][0] ) );
    print("---   Element D-F: F8 = {:7.2f} ... ".format( F3[7][0] ) );
    print("---   Element E-F: F9 = {:7.2f} ... ".format( F3[8][0] ) );

    print("--- ");
    print("--- Summary of Max/Min Reactions and Element-Level Forces ...");
    print("--- ----------------------------------------------------- ...");

    MinRax = minimum( F1[9][0], F2[9][0], F3[9][0] )
    MaxRax = maximum( F1[9][0], F2[9][0], F3[9][0] )

    MinRay = minimum( F1[10][0], F2[10][0], F3[10][0] )
    MaxRay = maximum( F1[10][0], F2[10][0], F3[10][0] )

    MinRdy = minimum( F1[11][0], F2[11][0], F3[11][0] )
    MaxRdy = maximum( F1[11][0], F2[11][0], F3[11][0] )

    print("--- ");
    print("---   Reaction A: Minimum R_ax = {:7.2f}, Maximum R_ax = {:7.2f} ... ".format( MinRax, MaxRax) )
    print("---             : Minimum R_ay = {:7.2f}, Maximum R_ay = {:7.2f} ... ".format( MinRay, MaxRay) )
    print("--- ");
    print("---   Reaction D: Minimum R_dy = {:7.2f}, Maximum R_dy = {:7.2f} ... ".format( MinRdy, MaxRdy) )

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

    print("--- ");
    print("---   Element A-B: ")
    printElementForces( "F1", MinF1, MaxF1)

    print("---   Element B-C: ")
    printElementForces( "F2", MinF2, MaxF2)

    print("---   Element C-D: ")
    printElementForces( "F3", MinF3, MaxF3)

    print("---   Element A-E: ")
    printElementForces( "F4", MinF4, MaxF4)
 
    print("---   Element B-E: ")
    printElementForces( "F5", MinF5, MaxF5)

    print("---   Element C-E: ")
    printElementForces( "F6", MinF6, MaxF6)

    print("---   Element C-F: ")
    printElementForces( "F7", MinF7, MaxF7)

    print("---   Element D-F: ")
    printElementForces( "F8", MinF8, MaxF8)

    print("---   Element E-F: ")
    printElementForces( "F9", MinF9, MaxF9)

    print("--- ======================================== ... ");
    print("--- Leave TestTrussAnalysis02.main()         ... ");

# call the main method ...

main()
