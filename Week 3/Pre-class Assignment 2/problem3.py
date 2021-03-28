# [Problem 3] Checking the data

import numpy as np
import pandas as pd

data = pd.read_csv('train.csv')

# See what each feature is about. (Numerical data or text data, etc.)
# print(data.info(verbose = True))

# Check which column is the target variable this time.


# Display the mean, standard deviation, and quartiles of the feature values at once.
# print(data.describe())