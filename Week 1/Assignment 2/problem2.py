# Problem 2: Creating a function corresponding to an arbitrary thickness

import math

def number_of_folds(distance, initial_thickness = 0.00008):
    return math.log2(distance / initial_thickness)

# Closest non-Sun star: Proxima Centauri
# Source: https://www.space.com/18090-alpha-centauri-nearest-star-system.html#:~:text=The%20two%20main%20stars%20are,star%20other%20than%20the%20sun.

# The distance is 4.22 light years, which is 3.992428e+16 meters

fold_times = number_of_folds(3.992428e+16)

print("Number of folds to reach the closest non-Sun star: {} folds".format(fold_times))