# Problem 3: Create using for statement

THICKNESS = 0.00008
folded_thickness = THICKNESS

for i in range(43): 
    folded_thickness *= 2

print("Thickness: {} meters".format(folded_thickness))