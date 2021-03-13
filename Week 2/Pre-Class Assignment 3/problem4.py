# Problem 4: Creating a function that performs matrix multiplication

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

def matrix_mul(A, B):
    result = np.zeros((len(A), len(B[0])))

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B[0])):
                result[i][j] += A[i][k] * B[k][j]

    return result

result = matrix_mul(A, B)
print(result)