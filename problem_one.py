"""
Problem 1: Shape up or ship out
"""

# Importing libraries
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import SVC
import numpy as np
from scipy.optimize import curve_fit

# Preparing variables and constants
data_file = pd.read_excel(r'data.xlsx')
data = {}
yr = range(2007, 2019)

# Loads files into memory in the form of a dictionary
for count in range(len(data_file['Year'])):
    year = data_file['Year'][count]
    data[year] = {"op_cost": data_file['Operational Cost'][count],
    \"elec_price": data_file['Electricity Price'][count], "prod_average": data_file['Production Average'][count],
    \"prod_nums": data_file['Production Numbers'][count]}

# Transforms data into feature-layout format
features, labels = [], []
for year in yr:
    yr_data = data[year]
    labels.append([float(yr_data["prod_nums"])])
    features.append([yr_data["op_cost"], yr_data["elec_price"], yr_data["prod_average"]])


# Fits the multi-linear regression model
lin_reg = LinearRegression()
lin_reg.fit(features, labels)
yr_encoded = []
for n in range(2007, 2041):
    yr_encoded.append(n)
pred_input = []
for year in yr_encoded:
    yr_data = data[year]
    pred_input.append([yr_data["op_cost"], yr_data["elec_price"], yr_data["prod_average"]])
encoded = lin_reg.predict(pred_input)

# Creates the multi-linear regression graph
plt.plot(yr_encoded, encoded, "r", label="Regression Predictions")
plt.plot(yr, labels, "o", label="Historical data")
plt.legend(loc="lower right", borderaxespad=1)
plt.xlabel("Year", weight="bold", size=14)
plt.ylabel("Number of Diesel Trucks", weight="bold", size=14)
plt.title("Historical Data and Regression Predictions for Number of Diesel Trucks", weight="bold", size=18)
plt.savefig('figures/figure1.png', bbox_inches='tight')


# Generates the logarithmic approximation
yr_encoded = [x-2000 for x in yr_encoded]
a, b = np.polyfit(np.log(yr_encoded), encoded, 1)
x = np.linspace(2001, 2040, 40)
y = a*np.log(x-2000) + b
print("y = " + str(a) + "*log(x-2000) + " + str(b))
yr_encoded = [c+2000 for c in yr_encoded]

# Creates logarithmic approximation graph
plt.plot(x, y, 'y', label="Logarithmic Approximation")
plt.plot(yr_encoded, encoded, 'r', label="Regression Predictions")
plt.legend(loc="lower right", borderaxespad=1)
plt.xlabel("Year", weight="bold", size=14)
plt.ylabel("Number of Diesel Trucks", weight="bold", size=14)
plt.title("Predicted Number of Diesel Trucks and Approximation Function", weight="bold", size=18)
plt.savefig('figures/figure2.png', bbox_inches='tight')


# Calculates the number of projected electric trucks
num_electric = 0
num_arr = []
for n in range(2020, 2041):
    num_electric += ((8.11*a)/(n - 2000))
    num_arr.append(num_electric)

# Plotting the number of projected electric trucks
plt.plot(range(2020, 2041), num_arr, 'g', label="Electric")
plt.plot(x, y, 'y', label="Diesel")
plt.legend(loc="lower right", borderaxespad=1)
plt.xlabel("Year", weight="bold", size=14)
plt.ylabel("Number of Trucks", weight="bold", size=14)
plt.title("Projected Number of Electric Trucks and Diesel Trucks", weight="bold", size=18)
plt.savefig('figures/figure3.png', bbox_inches='tight')


#Calculating the number of electric trucks relative to total trucks
total_trucks = []
for n in range(0, 40):
    if n < 20:
        total_trucks.append(y[n])
    else:
        total_trucks.append(y[n] + num_arr[n-20])
        print(2000+n, num_arr[n-20] / (y[n] + num_arr[n-20]))

# Plotting the number of electric trucks relative to total trucks
plt.plot(range(2001, 2041), total_trucks, color="black", label="Total")
plt.plot(range(2020, 2041), num_arr, 'g', label="Electric")
plt.legend(loc="lower right", borderaxespad=1)
plt.xlabel("Year", weight="bold", size=14)
plt.ylabel("Number of Trucks", weight="bold", size=14)
plt.title("Projected Number of Electric Trucks and Total Trucks", weight="bold", size=18)
plt.savefig('figures/figure4.png', bbox_inches='tight')
