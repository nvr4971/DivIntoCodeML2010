# Problem 2: Array combination

import numpy as np

x = np.arange(-50, 51, 1)
x = np.reshape(x, (-1, 1))

y = (1 / 2) * x + 1

lst = np.concatenate((x, y), axis = 1)

print(lst)