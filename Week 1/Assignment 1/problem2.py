# Problem 2: Number of rice grains other than day 100

import matplotlib.pyplot as plt

# Function
def compute_sorori_shinzaemon(day = 100, first_day = 1):
    lst_current = [first_day]
    lst_total = [lst_current[0]]

    for i in range(day - 1):
        lst_current.append(lst_current[-1] * 2)
        lst_total.append(lst_total[-1] + lst_current[-1])

    return lst_current, lst_total

# Main
day = 10

lst_current, lst_total = compute_sorori_shinzaemon(day)

print("The number of rice grains at day {}:       {}".format(day, lst_current[-1]))
print("The total number of rice grains at day {}: {}".format(day, lst_total[-1]))

# Graph
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
