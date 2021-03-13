# Problem 1: Create random numbers

import numpy as np

np.random.seed(0)

mean = (-3, 0)
cov = [[1.0, 0.8], [0.8, 1.0]]

lst = np.random.multivariate_normal(mean, cov, (500, 2))