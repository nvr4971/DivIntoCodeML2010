# [Problem 3] Checking the data

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

X = pd.DataFrame(data = iris['data'], columns = iris['feature_names'])

Y = pd.DataFrame(data = iris['target'], columns = ['target'])

df = pd.concat([X, Y], axis = 1)

# Display the 4th sample from the beginning and see what each feature is like. (Numerical data or character data, etc.)
sample = df.head(4)
print(sample)
print(sample.info(verbose = True))

# Output the total number of samples for each label.
print(df['target'].value_counts())

# Check if there is a missing value in the feature quantity.
print(df.isnull().sum())

# Display the mean, standard deviation, and quartiles of the feature values at once.
print(df.describe())