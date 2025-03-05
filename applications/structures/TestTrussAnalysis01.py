# ===============================================================
# TestTrussAnalysis01.py: Compute distribution of element forces
# and support reactions in a small three-bar truss.
# 
# Written by: Mark Austin                           November 2023 
# ===============================================================

import math            
import numpy as np  
from numpy.linalg import matrix_rank

# ===============================================================
# Function to print two-dimensional matrices ...
# ===============================================================

def PrintMatrix(name, a):
    print("Matrix: {:s} ".format(name) );
    for row in a:
        for col in row:
            print("{:8.4f}".format(col), end=" ")
        print("")

# ===============================================================
# main method ...
# ===============================================================

def main():
    print("--- Enter TestTrussAnalysis01.main()         ... ");
    print("--- ======================================== ... ");

    print("--- ");
    print("--- Part 1: Initialize coefficients for matrix equations ... ");

    # Node A ...

    a11 =  1      # < --- equilibrium in x direction ...
    a14 =  1
    a22 =  1      # < --- equilibrium in y direction ...
    a25 =  1

    # Node B ...

    a31 = 1              # < --- equilibrium in x direction ...
    a33 = 1/math.sqrt(2) 
    a43 = 1/math.sqrt(2) # < --- equilibrium in y direction ...
    a46 = 1

    # Node C ...

    a53 = -1/math.sqrt(2)  # < --- equilibrium in x direction ...
    a62 =  1               # < --- equilibrium in y direction ...
    a63 =  1/math.sqrt(2) 

    # Load Vector B ...

    print("--- ");
    print("--- Part 2: Initialize load vector ... ");

    b5 = 10
    b6 =  0

    print("--- ");
    print("--- Part 3: Create test matrices ... ");
    print("--- ");

    A = np.array([ [ a11,   0,   0, a14,   0,   0 ],
                   [   0, a22,   0,   0, a25,   0 ],
                   [ a31,   0, a33,   0,   0,   0 ],
                   [   0,   0, a43,   0,   0, a46 ],
                   [   0,   0, a53,   0,   0,   0 ],
                   [   0, a62, a63,   0,   0,   0 ] ]);
    PrintMatrix("A", A);

    B = np.array([ [0], [0], [0], [0], [b5], [b6] ]);
    PrintMatrix("B", B);

    print("--- ");
    print("--- Part 4: Check properties of matrix A ... ");
    print("--- ");

    rank = matrix_rank(A)
    det  = np.linalg.det(A)

    print("--- Matrix A: rank = {:f}, det = {:f}  ...".format(rank, det) );

    print("--- ");
    print("--- Part 5: Solve A.x = B ... ");
    print("--- ");

    x = np.linalg.solve(A, B)
    PrintMatrix("x", x);

    print("--- ");
    print("--- Part 6: Print support reactions and element-level forces ... ");
    print("--- ");

    print("--- Support A: R_ax = {:7.2f} ... ".format( x[3][0] ) );
    print("---          : R_ay = {:7.2f} ... ".format( x[4][0] ) );
    print("--- Support B: R_by = {:7.2f} ... ".format( x[5][0] ) );
    print("--- ");
    print("--- Element A-B: F1 = {:7.2f} ... ".format( x[0][0] ) );
    print("--- Element A-C: F2 = {:7.2f} ... ".format( x[1][0] ) );
    print("--- Element B-C: F3 = {:7.2f} ... ".format( x[2][0] ) );

    print("--- ======================================== ... ");
    print("--- Leave TestTrussAnalysis01.main()         ... ");

# call the main method ...

main()
