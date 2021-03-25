import numpy as np
import matplotlib.pyplot as plt

# Load csv data
csv_path = "mtfuji_data.csv"
np.set_printoptions(suppress = True)
fuji = np.loadtxt(csv_path, delimiter = ",", skiprows = 1)

# Function to get radient at pos (pos > 0)
def gradient_calculate(pos):
    change_x = fuji[:,0][pos] - fuji[:,0][pos - 1]
    change_y = fuji[:,3][pos] - fuji[:,3][pos - 1]
    return change_y / change_x

# Function to get next destination
def next_destination(pos, hyper_parameter = 0.2):
    # Destination point
    destination_point = fuji[:,0][pos] - hyper_parameter * gradient_calculate(pos)
    # Check if value is negative
    if (destination_point < 0):
        return np.nan
    else:
        # Round value
        return round(destination_point)

# Go down function
def go_down(start_pos, hyper_parameter = 0.2):
    visited = np.zeros(fuji[:,0].size, dtype = int)
    pos = fuji[:,0][start_pos]

    plt.plot(fuji[:,0], fuji[:,3])

    while (pos != np.nan and visited[int(pos)] != 1):
        visited[int(pos)] = 1
        plt.plot(fuji[:,0][int(pos)], fuji[:,3][int(pos)], 'rx')
        print("Move from position {} to position {}".format(pos, next_destination(int(pos))))
        pos = next_destination(int(pos), hyper_parameter)

    plt.title("Mt. Fuji")
    plt.xlabel("Position")
    plt.ylabel("Elevation[m]")

    plt.show()

go_down(142, 0.1)