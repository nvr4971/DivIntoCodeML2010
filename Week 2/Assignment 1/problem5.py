# Problem 5: Python functionalization

import numpy as np
import matplotlib.pyplot as plt

def compute_gradient(function, x_range = (-50, 50.1, 0.1)):
    x = np.arange(x_range[0], x_range[1], x_range[2]).astype(float)
    x = np.reshape(x, (-1, 1))

    y = function(x)
    
    lst = np.concatenate((x, y), axis = 1)

    change_x = lst[:,0][1:] - lst[:,0][:-1]
    change_y = lst[:,1][1:] - lst[:,1][:-1]

    gradient = change_y / change_x

    return lst, gradient

def function1(x):
    y = pow(x, 2)
    return y

def function2(x):
    y = 2 * pow(x, 2) + pow(2, x)
    return y

def function3(x):
    y = np.sin(pow(x, 1 / 2))
    return y

lst1, gradient1 = compute_gradient(function1)
lst2, gradient2 = compute_gradient(function2)
lst3, gradient3 = compute_gradient(function3, (0, 100.1, 0.1))

# Print out the gradients
print("Function 1 gradient: {}".format(gradient1))
print("Function 2 gradient: {}".format(gradient2))
print("Function 3 gradient: {}".format(gradient3))

# Plot the graphs
plt.plot(lst1[:,0], lst1[:,1])
plt.title(r"$y = x^2$")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

plt.plot(lst1[:,0][:-1], gradient1)
plt.title(r"Gradient of $y = x^2$")
plt.xlabel("x")
plt.ylabel("Gradient")

plt.show()

plt.plot(lst2[:,0], lst2[:,1])
plt.title(r"$y = 2x^2 + 2^x$")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

plt.plot(lst2[:,0][:-1], gradient2)
plt.title(r"Gradient of $y = 2x^2 + 2^x$")
plt.xlabel("x")
plt.ylabel("Gradient")

plt.show()

plt.plot(lst3[:,0], lst3[:,1])
plt.title(r"$y = sin(x^{\frac{1}{2}})$")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

plt.plot(lst3[:,0][:-1], gradient3)
plt.title(r"Gradient of $y = sin(x^{\frac{1}{2}})$")
plt.xlabel("x")
plt.ylabel("Gradient")

plt.show()