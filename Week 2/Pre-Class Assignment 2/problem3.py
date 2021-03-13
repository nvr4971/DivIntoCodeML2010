# Problem 3: Visualization by histogram

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

mean = (-3, 0)
cov = [[1.0, 0.8], [0.8, 1.0]]

lst = np.random.multivariate_normal(mean, cov, 500)

x = lst[:,0]
y = lst[:,1]

