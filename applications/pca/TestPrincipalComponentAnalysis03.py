# ===============================================================
# TestPrincipalComponentAnalysis03.py: PCA on Iris data.
# 
# The original data has four dimensions. Here we project the 
# 4D data to two principal dimensions of variation.
# 
# Written by: Mark Austin                              April 2021 
# ===============================================================

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# Class for Principal Component Analysis ...

class PrincipalComponentAnalysis():
    def __init__(self, no_of_components):
        self.no_of_components = no_of_components
        self.eigen_values  = None
        self.eigen_vectors = None
        
    def transform(self, x):
        return np.dot(x - self.mean, self.projection_matrix.T)
    
    def inverse_transform(self, x):
        return np.dot(x, self.projection_matrix) + self.mean
    
    def fit(self, x):
        self.no_of_components = x.shape[1] if self.no_of_components is None else self.no_of_components
        self.mean  = np.mean(x, axis=0)
        cov_matrix = np.cov(x - self.mean, rowvar=False)
        
        self.eigen_values, self.eigen_vectors = np.linalg.eig(cov_matrix)
        self.eigen_vectors = self.eigen_vectors.T
        
        self.sorted_components = np.argsort(self.eigen_values)[::-1]
        self.projection_matrix = self.eigen_vectors[self.sorted_components[:self.no_of_components]]

        self.explained_variance = self.eigen_values[self.sorted_components]
        self.explained_variance_ratio = self.explained_variance / self.eigen_values.sum()

    # get methods ...

    def getMean(self): 
        return self.mean 

    def getEigenvalues(self): 
        return self.eigen_values 

    def getEigenvectors(self): 
        return self.eigen_vectors 

    def getSortedComponents(self): 
        return self.sorted_components 

    def getExplainedVariance(self): 
        return self.explained_variance 

    def getExplainedVarianceRatio(self): 
        return self.explained_variance_ratio

    def getProjectionMatrix(self): 
        return self.projection_matrix

# main method ...

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

    print("--- Standardization ... ");

    std = StandardScaler()
    transformed = StandardScaler().fit_transform(x)

    print("--- Principal Component Analysis: Projection to 2D ... ");

    pca = PrincipalComponentAnalysis(no_of_components=2)
    pca.fit(transformed)

    print("--- Print mean ... ");

    mean = pca.getMean()
    print(mean);

    print("--- Print eigenvectors ... ");

    eigenvectors = pca.getEigenvectors()
    print(eigenvectors);

    print("--- Print variance ... ");

    variance = pca.getExplainedVariance()
    print(variance);

    print("--- Print variance ratio ... ");

    varianceRatio = pca.getExplainedVarianceRatio()
    print(varianceRatio);

    print("--- Print projection matrix ... ");

    projectionMatrix = pca.getProjectionMatrix()
    print(projectionMatrix);

    print("--- Plot transformed results ... ");

    x_std = pca.transform( transformed )

    plt.figure()
    plt.scatter( x_std[:, 0], x_std[:, 1], c=y)
    plt.xlim(-4.0, 4.0 );
    plt.ylim(-4.0, 4.0 );
    plt.xlabel('Principal Component 1', fontsize = 12 )
    plt.ylabel('Principal Component 2', fontsize = 12 )
    plt.title('Iris Scatter Plot Example')
    plt.show()

    print("--- ============================================= ... ");
    print("--- Leave TestPrincipalComponentAnalysis02.main() ... ");

# call the main method ...

main()
