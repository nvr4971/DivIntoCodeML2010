# Problem 5: Judge the input whose calculation is not defined

import numpy as np

D = np.array([
            [-1, 2, 3],
            [4, -5, 6]
            ])

E = np.array([
            [-9, 8, 7],
            [6, -5, 4]
            ])

def matrix_mul(A, B):
    if (len(A) != len(B[0])):
        print("The number of columns in the first matrix must be equal to the number of rows in the second matrix")
        return

    result = np.zeros((len(A), len(B[0])))

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B[0])):
                result[i][j] += A[i][k] * B[k][j]

    return result

result = matrix_mul(D, E)
print(result)