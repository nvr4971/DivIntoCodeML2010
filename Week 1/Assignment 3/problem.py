# Problem: The day when chestnut buns cover the solar system

import math

# Volume of a normal chestnut bun

# This is quite tricky, so in this case I'll just assume based on the pictures from the source link
# More specifically in the pic at step 9, we could assume that the chestnut bun is an upper half of a sphere 
# and that the circumference is the size of the palm, which is 10 cm, or 0.1 m
# So the volume of the half sphere (or hemisphere) would be:
# V = 2/3 * pi * (r ** 3) in which r is the diameter

# Thus: 

chestnut_volume = (2 / 3) * math.pi * (0.05 ** 3)

# Source: https://cookpad.com/uk/recipes/155252-chestnut-buns

# Volume of the solar system

# According the the source article, the Solar System diameter assumption is 287.46 billion km
# We will use the full sphere volume formula to calculate, which is:
# V = 4/3 * pi * (r ** 3) in which r is the diameter

# Thus:

solar_system_volume = (4 /3) * math.pi * ((287.46 * (10 ** 12)) ** 3)

# Source: https://www.universetoday.com/15585/diameter-of-the-solar-system/

# The number of multiply times for the chestnut buns to multiply to the size of the solar system

mul_times = solar_system_volume / chestnut_volume

# Since the object would double every 5 minutes

time_taken = math.log2(mul_times) * 5

print("Time taken: {} minutes".format(time_taken))