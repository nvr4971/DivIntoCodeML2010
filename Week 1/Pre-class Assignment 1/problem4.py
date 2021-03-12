# Problem 4: Comparison of calculation time

import time

# Change the number of times to clarify the difference

N_TIMES = 43

# Calculate time for the arithmetic implementation

start1 = time.time()

THICKNESS = 0.00008
folded_thickness = THICKNESS * (2 ** N_TIMES)

print("Thickness: {} meters".format(folded_thickness))

elapsed_time1 = time.time() - start1
print("Time of arithmetic implementation: {}[s]".format(elapsed_time1))

# Calculate time for the loop implementation

start2 = time.time()

THICKNESS = 0.00008
folded_thickness = THICKNESS

for i in range(N_TIMES): 
    folded_thickness *= 2

print("Thickness: {} meters".format(folded_thickness))

elapsed_time2 = time.time() - start2
print("Time of for implementation       : {}[s]".format(elapsed_time2))