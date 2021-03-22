# Problem 6: Find the minimum value

import numpy as np
import matplotlib.pyplot as plt

def compute_gradient(function, x_range = (-50, 50.1, 0.1)):
    x = np.arange(x_range[0], x_range[1], x_range[2]).astype(float)
    x = np.reshape(x, (-1, 1))

    y = function(x)
    
    lst = np.concatenate((x, y), axis = 1)

    change_x = x[1:] - x[:-1]
    change_y = y[1:] - y[:-1]

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

print(lst2)

# Find the minimum value and index
min1 = np.min(lst1[:,1])
min_idx1 = np.argmin(lst1[:,1])
print("Minimum value of y of function 1 is {} at index {}".format(min1, min_idx1))

min2 = np.min(lst2[:,1])
min_idx2 = np.argmin(lst2[:,1])
print("Minimum value of y of function 2 is {} at index {}".format(min2, min_idx2))

min3 = np.min(lst3[:,1])
min_idx3 = np.argmin(lst3[:,1])
print("Minimum value of y of function 3 is {} at index {}".format(min3, min_idx3))

# Display the slope before and after taking the minimum y
plt.plot(lst1[:,0][0:min_idx1], lst1[:,1][0:min_idx1])
plt.title(r"$y = x^2$ before minimum y")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

plt.plot(lst1[:,0][min_idx1:-1], lst1[:,1][min_idx1:-1])
plt.title(r"$y = x^2$ after minimum y")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

plt.plot(lst2[:,0][0:min_idx2], lst2[:,1][0:min_idx2])
plt.title(r"$y = 2x^2 + 2^x$ before minimum y")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

plt.plot(lst2[:,0][min_idx2:-1], lst2[:,1][min_idx2:-1])
plt.title(r"$y = 2x^2 + 2^x$ after minimum y")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

plt.plot(lst3[:,0][0:min_idx3], lst3[:,1][0:min_idx3])
plt.title(r"$y = sin(x^{\frac{1}{2}})$ before minimum y")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

plt.plot(lst3[:,0][min_idx3:-1], lst3[:,1][min_idx3:-1])
plt.title(r"$y = sin(x^{\frac{1}{2}})$ after minimum y")
plt.xlabel("x")
plt.ylabel("y")

plt.show()