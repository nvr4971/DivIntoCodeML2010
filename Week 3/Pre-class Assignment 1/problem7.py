# [Problem 7] Confirming the relationship between features

import itertools
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

X = pd.DataFrame(data = iris['data'], columns = iris['feature_names'])

Y = pd.DataFrame(data = iris['target'], columns = ['target'])

df = pd.concat([X, Y], axis = 1)

# Take one feature for each of the vertical and horizontal axes and create a color-coded scatter plot for each type
"""
sns.scatterplot(
    data = df, 
    x = 'sepal length (cm)',
    y = 'sepal width (cm)',
    hue = 'target'
)
plt.show()

sns.scatterplot(
    data = df, 
    x = 'sepal length (cm)',
    y = 'petal length (cm)',
    hue = 'target'
)
plt.show()

sns.scatterplot(
    data = df, 
    x = 'sepal length (cm)',
    y = 'petal width (cm)',
    hue = 'target'
)
plt.show()

sns.scatterplot(
    data = df, 
    x = 'sepal width (cm)',
    y = 'petal length (cm)',
    hue = 'target'
)
plt.show()

sns.scatterplot(
    data = df, 
    x = 'sepal width (cm)',
    y = 'petal width (cm)',
    hue = 'target'
)
plt.show()

sns.scatterplot(
    data = df, 
    x = 'petal length (cm)',
    y = 'petal width (cm)',
    hue = 'target'
)
plt.show()
"""

# Create a scatterplot matrix that displays all combinations of scatterplots at once
"""
sns.pairplot(df, hue = 'target')
plt.show()
"""

# Create a correlation coefficient matrix for 4 features
# print(X.corr())

# Make a heat map of the correlation coefficient matrix
"""
coef = X.corr()
sns.heatmap(coef)
plt.plot()
"""