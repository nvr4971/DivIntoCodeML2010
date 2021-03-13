# Problem 6: Labeling

import numpy as np

np.random.seed(0)

mean1 = (-3, 0)
cov = [[1.0, 0.8], [0.8, 1.0]]

lst1 = np.random.multivariate_normal(mean1, cov, 500)
temp1 = np.zeros((500, 1))

mean2 = (0, -3)

lst2 = np.random.multivariate_normal(mean2, cov, 500)
temp2 = np.ones((500, 1))

lst = np.concatenate((lst1, lst2), axis = 0)
temp = np.concatenate((temp1, temp2), axis = 0)
lst = np.concatenate((lst, temp), axis = 1)

print(lst)
