# Problem 1: Number of wheat on a 2x2 square chess board

import numpy as np

n = 2               # Number of squares of a side
n_squares = n ** 2  # Total number of squares on the board

# Generate data for the board list
board_lst = [1]     
for i in range(n_squares - 1):
    board_lst.append(board_lst[-1] * 2)

# Convert to numpy array
board = np.array(board_lst)
board = np.reshape(board, (n, n))

print("Arrange wheat on a plate of {} squares:".format(n_squares))
print(board)