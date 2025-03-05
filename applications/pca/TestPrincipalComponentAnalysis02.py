# ===========================================================================
# TestPrincipalComponentAnalysis02.py: Compute PCA for iris data ...
# 
# Written by: Mark Austin                                          April 2021 
# ===========================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import random
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Main method ...

def main():
    print("--- Enter TestPrincipalComponentAnalysis02.main() ... ");
    print("--- ============================================= ... ");

    print("--- Load iris data ... ");

    iris = load_iris()

    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

    df['class'] = iris.target
    print(df);

    print("--- Get value of x and y ... ");

    x = df.drop(labels='class', axis=1).values
    y = df['class'].values
    
    print( x.shape, y.shape )

    print("--- Array: x ... ");

    print( x )

    print("--- Array: y ... ");

    print( y )

    print("--- Standardization ... ");

    std = StandardScaler()
    transformed = StandardScaler().fit_transform(x)

    print("--- Transformed data array: x ... ");

    print( transformed )

    print("--- Compute principal components (two dimensions)... ");

    pca = PCA(n_components=2)
    pca.fit(transformed)

    print("--- Print components ... ");

    print(pca.components_)

    print("--- Print explained variance ... ");

    print(pca.explained_variance_)

    print("--- Plot transformed results ... ");

    x_pca = pca.transform(x)
    print(x_pca)

    plt.figure()
    plt.scatter( x_pca[:, 0], x_pca[:, 1], c=y)
    plt.xlabel('Principal Component 1', fontsize = 12 )
    plt.ylabel('Principal Component 2', fontsize = 12 )
    plt.title('Iris Scatter Plot Example')
    plt.show()

    print("--- ============================================= ... ");
    print("--- Leave TestPrincipalComponentAnalysis02.main() ... ");

# call the main method ...

main()
