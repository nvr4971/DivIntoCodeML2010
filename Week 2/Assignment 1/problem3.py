# Problem 3: Find the gradient

import numpy as np

x = np.arange(-50, 51, 1)
x = np.reshape(x, (-1, 1))

y = (1 / 2) * x + 1

lst = np.concatenate((x, y), axis = 1)

change_x = lst[:,0][1:] - lst[:,0][:-1]

change_y = lst[:,1][1:] - lst[:,1][:-1]

gradient = change_y / change_x

print(gradient)

# All positive, so the line moving up