# [Problem 6] Creating a diagram

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

X = pd.DataFrame(data = iris['data'], columns = iris['feature_names'])

Y = pd.DataFrame(data = iris['target'], columns = ['target'])

df = pd.concat([X, Y], axis = 1)

# print(df)

# Make a pie chart of the number of samples per label (while showing percentages)
"""
labels_count = df['target'].value_counts()
labels = '0', '1', '2'

plt.pie(labels_count, 
        labels = labels, 
        autopct = '%1.1f%%', 
        shadow = False, 
        startangle = 90)
plt.axis('equal')

plt.show()
"""

# Select features one by one and visualize the distribution of data for each label using a box plot

sepal_length = df['sepal length (cm)']
sepal_width = df['sepal width (cm)']
petal_length = df['petal length (cm)']
petal_width = df['petal width (cm)']

np.random.seed(0)

"""
plt.title("sepal length (cm)")
plt.boxplot(sepal_length)
plt.show()

plt.title("sepal width (cm)")
plt.boxplot(sepal_width)
plt.show()

plt.title("petal length (cm)")
plt.boxplot(petal_length)
plt.show()

plt.title("petal width (cm)")
plt.boxplot(petal_width)
plt.show()
"""

# Select features one by one and visualize the distribution of data for each label using a violin plot
"""
plt.title("sepal length (cm)")
plt.violinplot(sepal_length)
plt.show()

plt.title("sepal width (cm)")
plt.violinplot(sepal_width)
plt.show()

plt.title("petal length (cm)")
plt.violinplot(petal_length)
plt.show()

plt.title("petal width (cm)")
plt.violinplot(petal_width)
plt.show()
"""

# Difference between box plot and violin plot
# Violin plot give more detail about distribution 