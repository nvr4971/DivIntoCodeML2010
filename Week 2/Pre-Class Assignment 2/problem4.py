# Problem 4: Addition of data

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

mean1 = (-3, 0)
cov = [[1.0, 0.8], [0.8, 1.0]]

lst1 = np.random.multivariate_normal(mean1, cov, 500)

x1 = lst1[:,0]
y1 = lst1[:,1]

mean2 = (0, -3)

lst2 = np.random.multivariate_normal(mean2, cov, 500)

x2 = lst2[:,0]
y2 = lst2[:,1]

plt.scatter(x1, y1, marker='+')
plt.scatter(x2, y2, marker='x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend([0, 1])

plt.show()