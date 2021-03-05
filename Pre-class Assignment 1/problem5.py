# Problem 5: Saving to a list

THICKNESS = 0.00008
folded_thickness = THICKNESS

lst = []

for i in range(43): 
    lst.append(folded_thickness)
    folded_thickness *= 2

print("List len: {} items".format(len(lst)))