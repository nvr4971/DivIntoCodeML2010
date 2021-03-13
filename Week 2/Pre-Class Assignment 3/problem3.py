# Problem 3: Implementation of calculation of a certain element

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

result = np.zeros((3, 3))

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B[0])):
            result[i][j] += A[i][k] * B[k][j]

print(result)