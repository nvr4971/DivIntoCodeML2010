# Problem 1: Minimum number of folds over Mt. Fuji

import math 

# Constant value: thickness of a general copy paper (in meters (m))
THICKNESS = 0.00008

fold_times = math.log2(3776 / THICKNESS)

print("Number of folds for the thickness to exceed Mt. Fuji (3776m): {} folds".format(fold_times))