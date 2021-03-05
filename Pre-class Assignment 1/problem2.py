# Problem 2: Unit conversion

THICKNESS = 0.00008
folded_thickness = THICKNESS * (2 ** 43)

print("Thickness: {: .2f} kilometers".format(folded_thickness/1000))