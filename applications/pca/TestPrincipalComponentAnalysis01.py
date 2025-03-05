# ===========================================================================
# TestPrincipalComponentAnalysis01.py: Compute PCA for a noisy line function.
# 
# Written by: Mark Austin                                          April 2021 
# ===========================================================================

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import random
from sklearn.decomposition import PCA

# Define noisy line function ...

def NoisyLineFunction (a,b,x):
    return a + b*x + 5*(random.random() - 1.0)

# Function to print matrices ...

def PrintMatrix(a):
    for row in a:
        for col in row:
            print("{:8.2f}".format(col), end=" ")
        print("")

# Draw vector

def DrawVector(v0, v1, ax=None):
    print("--- In draw vector: v0 ... ");
    print(v0);
    print("--- In draw vector: v1 ... ");
    print(v1);
    # ax = ax or plt.gca()
    ax = plt.gca()
    arrowprops = dict(arrowstyle='->', linewidth=2, color='r', shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)

# Main method ...

def main():
    print("--- Enter TestPrincipalComponentAnalysis01.main() ... ");
    print("--- ============================================= ... ");

    print("--- Initialize random seed ... ");

    random.seed(21345);

    print("--- Create data along noisy line function: y = ax + b + noise ... ");

    xvalues = list( np.arange( 5.0, 20.0, 0.25 ) );
    yvalues = []
    for x in xvalues:
        yvalue = NoisyLineFunction(2,0.9,x)
        yvalues.append( yvalue );

    print("--- Transform x and y lists into 2d array ... ");

    X = np.transpose([xvalues,yvalues])
    PrintMatrix(X)

    print("--- Plot raw data ... ");
 
    plt.scatter(X[:,0], X[:,1]) 
    plt.xlim(0.0, 30.0 );
    plt.ylim(0.0, 30.0 );
    plt.title('Noisy Line Function');
    plt.xlabel('x');
    plt.ylabel('y');
    plt.show()

    print("--- Compute principal components (two dimensions)... ");

    pca = PCA(n_components=2)
    pca.fit(X)

    print("--- Print components ... ");

    print(pca.components_)

    print("--- Print variance ... ");

    print(pca.explained_variance_)

    print("--- Plot principal component vectors over data ... ");

    plt.scatter(X[:, 0], X[:, 1], alpha=1.0)
    for length, vector in zip(pca.explained_variance_, pca.components_):
       v = vector * 3 * np.sqrt(length)
       print("--- Eigenvector ... ");
       print(v)
       DrawVector(pca.mean_, pca.mean_ + v)
    plt.xlim(0.0, 30.0 );
    plt.ylim(0.0, 30.0 );
    plt.title('Principal Component Analysis (2-dimensions)');
    plt.xlabel('x');
    plt.ylabel('y');
    plt.show()

    print("--- Next: Use PCA as a dimensionality reduction platform (one dimension) ... ");

    pca = PCA(n_components=1)
    pca.fit(X)
    X_pca = pca.transform(X)

    print("--- Print components ... ");

    print(pca.components_)

    print("--- Print variance ... ");

    print(pca.explained_variance_)

    print("Original shape:   ", X.shape)

    PrintMatrix(X);

    print("Transformed shape:", X_pca.shape)

    PrintMatrix(X_pca);

    print("--- Compute inverse transform on reduced data ... ");

    X_new = pca.inverse_transform(X_pca)
    PrintMatrix(X_new);

    print("--- Plot 1-D transform ... ");

    plt.scatter(X[:, 0], X[:, 1], alpha=0.4)
    plt.scatter(X_new[:, 0], X_new[:, 1], alpha=1.0)
    plt.xlim(0.0, 30.0 );
    plt.ylim(0.0, 30.0 );
    plt.title('Principal Component Analysis (1-dimension)');
    plt.show()

    print("--- ============================================= ... ");
    print("--- Leave TestPrincipalComponentAnalysis01.main() ... ");

# call the main method ...

main()
