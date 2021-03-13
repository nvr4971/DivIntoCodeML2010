# Problem 3: Total number of wheat

import numpy as np
import matplotlib.pyplot as plt

n = 8            
n_squares = n ** 2

# Generate data for the board list
board_lst = [1]     
for i in range(n_squares - 1):
    board_lst.append(board_lst[-1] * 2)

# Total number of wheat
board = np.array(board_lst)
board = np.reshape(board, (n, n))
print("Total number of wheat on a chessboard of {} x {} squares: {}".format(n, n, board.sum()))

# Average of each column array
avg = board.sum(axis=0)
avg = avg / n

# Plot bar chart
plt.xlabel("Column")
plt.ylabel("Number")
plt.title("Number in each column")
plt.bar(np.arange(1, n + 1), avg)

plt.show()


