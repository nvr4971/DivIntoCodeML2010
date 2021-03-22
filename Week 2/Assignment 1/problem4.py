# Problem 4: Draw a graph

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-50, 51, 1)
x = np.reshape(x, (-1, 1))

y = (1 / 2) * x + 1

lst = np.concatenate((x, y), axis = 1)

plt.plot(lst[:,0], lst[:,1])
plt.title(r"$y = \frac{1}{2}x + 1$")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

plt.plot(lst[:,0][:-1], gradient)
plt.title(r"Gradient of $y = \frac{1}{2}x + 1$")
plt.xlabel("x")
plt.ylabel("Gradient")

plt.show()