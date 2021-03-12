# Problem 3: Required paper length

import math

# Function from problem2.py
def number_of_folds(distance, initial_thickness = 0.00008):
    return math.log2(distance / initial_thickness)

def gallivan_paper_fold_length(fold_times, initial_thickness = 0.00008):
    return ((math.pi * initial_thickness) / 6) * (2 ** fold_times + 4) * (2 ** fold_times - 1)

# Moon distance: 384400 km (average distance) = 384400000 meters
# Source: https://www.space.com/18145-how-far-is-the-moon.html

print("Length of paper needed to reach the Moon:                 {} meters".format(gallivan_paper_fold_length(number_of_folds(384400000))))

# Mt. Fuji: 3776 meters

print("Length of paper needed to reach Mt. Fuji:                 {} meters".format(gallivan_paper_fold_length(number_of_folds(3776))))

# Proxima Centauri: 4.22 light years = 3.992428e+16 meters

print("Length of paper needed to reach the closest non-Sun star: {} meters".format(gallivan_paper_fold_length(number_of_folds(3.992428e+16))))