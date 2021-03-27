# [Problem 1] Data acquisition

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

X = pd.DataFrame(data = iris['data'], columns = iris['feature_names'])
print(X)

Y = pd.DataFrame(data = iris['target'], columns = ['target'])
print(Y)
