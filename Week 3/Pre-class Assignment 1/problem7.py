# [Problem 7] Confirming the relationship between features

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

X = pd.DataFrame(data = iris['data'], columns = iris['feature_names'])

Y = pd.DataFrame(data = iris['target'], columns = ['target'])

df = pd.concat([X, Y], axis = 1)

sepal_length = df['sepal length (cm)']
sepal_width = df['sepal width (cm)']
petal_length = df['petal length (cm)']
petal_width = df['petal width (cm)']

np.random.seed(0)

# Take one feature for each of the vertical and horizontal axes and create a color-coded scatter plot for each type
"""
plt.title("Iris Scatterplot")
plt.scatter(sepal_length, sepal_width)
plt.scatter(petal_length, petal_width)
plt.xlabel("Length (cm)")
plt.ylabel("Width (cm)")
plt.legend(["Sepal", "Petal"])
plt.show()
"""

# Create a scatterplot matrix that displays all combinations of scatterplots at once




# Create a correlation coefficient matrix for 4 features




# Make a heat map of the correlation coefficient matrix

