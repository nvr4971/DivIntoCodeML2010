# Create a function to calculate the slope of a point

import numpy as np

# Load csv data
csv_path = "mtfuji_data.csv"
np.set_printoptions(suppress = True)
fuji = np.loadtxt(csv_path, delimiter = ",", skiprows = 1)

# Function to get radient at pos (pos > 0)
def gradient_calculate(pos):
    change_x = fuji[:,0][1:] - fuji[:,0][:-1]
    change_y = fuji[:,3][1:] - fuji[:,3][:-1]
    gradient = change_y / change_x
    return gradient[pos]

print(gradient_calculate(10))