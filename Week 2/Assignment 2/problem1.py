# Visualization of data

import numpy as np
import matplotlib.pyplot as plt

# Load csv data
csv_path = "mtfuji_data.csv"
np.set_printoptions(suppress = True)
fuji = np.loadtxt(csv_path, delimiter = ",", skiprows = 1)

plt.plot(fuji[:,0], fuji[:,3])
plt.title("Mt. Fuji")
plt.xlabel("Position")
plt.ylabel("Elevation[m]")

plt.show()