# [Problem 2] Combining data

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

X = pd.DataFrame(data = iris['data'], columns = iris['feature_names'])

Y = pd.DataFrame(data = iris['target'], columns = ['target'])

df = pd.concat([X, Y], axis = 1)
print(df)