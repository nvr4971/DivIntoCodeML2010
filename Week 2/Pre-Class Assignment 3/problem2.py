# Problem 2: Calculation by NumPy function

import numpy as np

A = np.array([
            [-1, 2, 3], 
            [4, -5, 6], 
            [7, 8, -9]
            ])
B = np.array([
            [0, 2, 1], 
            [0, 2, -8], 
            [2, 9, -1]
            ])

print(np.dot(A, B))