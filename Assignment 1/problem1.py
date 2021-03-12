# Problem 1: Number of rice grains on the 100th day

import matplotlib.pyplot as plt

day = 100       # The number of days

FIRST_DAY = 1   # The number of rice on day 1

# List for graph plotting
lst_current = [FIRST_DAY]
lst_total = [lst_current[0]]

# Generate list data
for i in range(day - 1):
    lst_current.append(lst_current[-1] * 2)
    lst_total.append(lst_total[-1] + lst_current[-1])

# Print out results
print("The number of rice grains at day {}:       {}".format(day, lst_current[-1]))
print("The total number of rice grains at day {}: {}".format(day, lst_total[-1]))

# Graph plotting
plt.title("Sorori Shinzaemon Problem")
plt.xlabel("Days")
plt.ylabel("Number of rice grain received")

plt.plot(range(1, day + 1),
    lst_current,
    label = "One day",
    color = 'green')

plt.plot(range(1, day + 1),
    lst_total,
    label = "Total",
    color = 'red')

plt.legend()
plt.show()
