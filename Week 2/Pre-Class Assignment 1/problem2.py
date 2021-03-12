# Problem 2: Expansion to n x m mass

import numpy as np

np.set_printoptions(suppress = True)

def n_m_square_wheat(n, m):
    n_squares = n * m

    board_lst = [1]     
    for i in range(n_squares - 1):
        board_lst.append(board_lst[-1] * 2)

    board_array = np.array(board_lst)
    board_array = np.reshape(board_array, (n, m))

    return board_array

n = 8
m = 8

board = n_m_square_wheat(n, m)

print("Arrange wheat on a plate of {} x {} squares:".format(n, m))
print(board)