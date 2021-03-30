# [Problem 4] Dealing with missing values

import numpy as np
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')

# Check for missing values ​​for each feature.
"""
msno.heatmap(data)
plt.show()
"""

# Check what percentage of missing values ​​are included.
missing = data.isnull().sum() / len(data)
# print(missing)

# Delete features (columns) that have 5 or more missing values.
data = data[data.columns[data.isnull().sum() < 5]]

# Samples (rows) with missing values ​​are deleted from the data from which features with 5 or more missing values ​​have been deleted
data = data[data.isnull().sum(axis = 1) < 5]
