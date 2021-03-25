# Create a function to go down the mountain

import numpy as np
import matplotlib.pyplot as plt

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

# Function to get next destination
def next_destination(pos):
    # Destination point
    hyper_parameter = 0.2
    destination_point = fuji[:,0][pos] - hyper_parameter * gradient_calculate(pos)
    # Check if value is negative
    if (destination_point < 0):
        return np.nan
    else:
        # Round value
        return round(destination_point)

# First current point is the 136th location
def go_down():
    visited = np.zeros(fuji[:,0].size, dtype = int)
    pos = fuji[:,0][136]
    while (pos != np.nan and visited[int(pos)] != 1):
        visited[int(pos)] = 1
        print("Move from position {} to position {}".format(pos, next_destination(int(pos))))
        pos = next_destination(int(pos))

go_down()

