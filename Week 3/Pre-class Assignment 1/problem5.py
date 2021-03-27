# [Problem 5] Extracting the required data

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

X = pd.DataFrame(data = iris['data'], columns = iris['feature_names'])

Y = pd.DataFrame(data = iris['target'], columns = ['target'])

df = pd.concat([X, Y], axis = 1)

# loc gets rows (or columns) with particular labels from the index
# iloc gets rows (or columns) at integers positions in the index

# Extract sepal_width column in three different ways
print(df['sepal width (cm)'])
print(df.loc[: , 'sepal width (cm)'])
print(df.iloc[: , 1])

# Extract the 50th to 99th data
print(df.iloc[49:99, :])

# Extract the 50th to 99th data of the petal_length column
print(df.loc[49:99, 'petal length (cm)'])

# Extract data with a petal_width value of 0.2
print(df.loc[df['petal width (cm)'] == 0.2])