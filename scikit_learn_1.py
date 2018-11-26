"""
*******************

Sklearn

*******************
"""

### Dataset loading utilities (5)
from sklearn import datasets
iris = datasets.load_iris()
#Load and return the boston house-prices dataset (regression).
boston = datasets.load_boston()	
#Load and return the iris dataset (classification).
iris = datasets.load_iris() 	
#Load and return the diabetes dataset (regression).
diabest = datasets.load_diabetes()
#Load and return the digits dataset (classification). 	
digits = datasets.load_digits()	
#Load and return the linnerud dataset (multivariate regression).
linnerud = datasets.load_linnerud()	
#Load and return the wine dataset (classification).
wine = datasets.load_wine()	
#Load and return the breast cancer wisconsin dataset (classification).
breast_cancer = datasets.load_breast_cancer()	

#****************************************
#   Genarted datasets for classification
#****************************************
from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets import make_classification
X, y = make_blobs(n_samples=10, centers=3, n_features=2,random_state=0)
print(X.shape)

X, y = make_classification(n_samples=100, n_features=10, random_state=0)
print(X.shape)


#****************************************
#   Biclustering
#****************************************









  
