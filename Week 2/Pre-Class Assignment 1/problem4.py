# Problem 4: Heat map of the number of wheat

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

# Plot bar chart
plt.xlabel("Column")
plt.ylabel("Row")
plt.title("Heatmap")
plt.pcolor(board)

plt.show()


