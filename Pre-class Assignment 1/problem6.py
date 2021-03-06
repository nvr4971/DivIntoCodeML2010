# Problem 6: DIsplaying a line graph

import matplotlib.pyplot as plt

THICKNESS = 0.00008
folded_thickness = THICKNESS

lst = []

for i in range(43): 
    lst.append(folded_thickness)
    folded_thickness *= 2

plt.title("Thickness of folded paper")
plt.xlabel("Number of folds")
plt.ylabel("Thicness [m]")

# Customization
plt.tick_params(labelsize = 20)
plt.plot(lst, 
    color = 'green',
    linestyle = 'dashed', 
    marker = 'x', 
    markersize = 6)
    
plt.show()