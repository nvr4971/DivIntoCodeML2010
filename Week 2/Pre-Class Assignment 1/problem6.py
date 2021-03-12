# Problem 6: Expansion to n x m mass by another calculation method

import numpy as np

def n_m_square_wheat_append(n, m):
    n_squares = n * m
    board = np.array([1])

    for i in range(n_squares - 1):
        board = np.append(board, 2 * board[-1])

    board = np.reshape(board, (n, m))

    return board

def n_m_square_wheat_broadcast(n, m):
    n_squares = n * m
    index = np.arange(n_squares).astype(np.uint64)

    board = 2 ** index

    board = np.reshape(board, (n, m))

    return board

n = 8
m = 8

board_append = n_m_square_wheat_append(n, m)

print("Arrange wheat on a plate of {} x {} squares:".format(n, m))
print(board_append)

board_broadcast = n_m_square_wheat_broadcast(n, m)

print("Arrange wheat on a plate of {} x {} squares:".format(n, m))
print(board_broadcast)