# Problem 3: How many people can live for how many days with the rice they receive

# References for calculation (we assume that it's normal white rice)

# Weight of 1 grain of rice: 0.021 grams (g)
# Source: https://www.bluebulbprojects.com/measureofthings/results.php?comp=weight&unit=gms&amt=0.021

# Note that white rice triples in both volume and weight after cooking
# Essentially, 1 cup of uncooked rice would yeild 3 cups of cooked rice
# Source: https://www.cooksinfo.com/rice

# Number of calories in 1 cup of cooked rice (158g): 205 calories
# Source: https://www.nutritionix.com/food/rice

# Therefore we can conclude the following formula to calculate how much calories from a given number of rice grains:
# Calories = ((Number of grain * 0.021 * 3) / 158) * 205

# Average person calories need in a day: 2000 calories
# https://www.news-medical.net/health/How-Many-Calories-Should-You-Eat-Per-Day.aspx

# Therefore: Days = Calories / (2000 * Number of people)

def how_many_days_compute(rice_grains, people):
    calories = ((rice_grains * 0.021 * 3) / 158) * 205
    return calories / (2000 * people)

test = how_many_days_compute(100000, 2)

print("Number of days that {} people would live with the given number of rice grains: {}".format(100, test))


