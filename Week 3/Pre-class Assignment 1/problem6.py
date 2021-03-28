# [Problem 6] Creating a diagram

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()

X = pd.DataFrame(data = iris['data'], columns = iris['feature_names'])

Y = pd.DataFrame(data = iris['target'], columns = ['target'])

df = pd.concat([X, Y], axis = 1)

# print(df)

# Make a pie chart of the number of samples per label (while showing percentages)
"""
labels_count = df['target'].value_counts()
labels_count.plot.pie( 
    autopct = '%1.1f%%',
    startangle = 90,
    shadow = False,
    legend = True)
plt.show()
"""

# Select features one by one and visualize the distribution of data for each label using a box plot
"""
sns.boxplot(
    x = df['target'],
    y = df['sepal length (cm)']
)
plt.show()

sns.boxplot(
    x = df['target'],
    y = df['sepal width (cm)']
)
plt.show()

sns.boxplot(
    x = df['target'],
    y = df['petal length (cm)']
)
plt.show()

sns.boxplot(
    x = df['target'],
    y = df['petal width (cm)']
)
plt.show()
"""

# Select features one by one and visualize the distribution of data for each label using a violin plot
"""
sns.violinplot(
    x = df['target'],
    y = df['sepal length (cm)']
)
plt.show()

sns.violinplot(
    x = df['target'],
    y = df['sepal width (cm)']
)
plt.show()

sns.violinplot(
    x = df['target'],
    y = df['petal length (cm)']
)
plt.show()

sns.violinplot(
    x = df['target'],
    y = df['petal width (cm)']
)
plt.show()
"""

# Difference between box plot and violin plot
# Violin plot give more detail about distribution 