# [Problem 6] Confirmation of distribution

import numpy as np
import pandas as pd
import missingno as msno
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')

# Display the sns.distplot() distribution of the objective variable using seaborn, and calculate the "kurtosis" and "skewness".
