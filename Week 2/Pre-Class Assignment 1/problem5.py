# Problem 5: How many times is the second half as long as the first half

import numpy as np

n = 8
n_squares = n ** 2

# Generate data for the board list
board_lst = [1]     
for i in range(n_squares - 1):
    board_lst.append(board_lst[-1] * 2)

# Total number of wheat
board = np.array(board_lst)
board = np.reshape(board, (n, n))

# First half, second half calculation
row_sum = board.sum(axis=1)
first_half = row_sum[0:4].sum()
second_half = row_sum[4:n].sum()
print("The second half is {} times longer than the first half".format(second_half / first_half))
