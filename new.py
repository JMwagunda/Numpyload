import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load the CSV file
data = np.loadtxt('city_temperature.csv', delimiter=',', unpack=True, dtype=None)

# Define the function to fit
def f(t, a, b, c):
    return a * np.cos(2 * np.pi * t + b) + c

# Fit the data to the function
x = data[:, 0]
y = data[:, 1]
popt, pcov = curve_fit(f, x, y)

# Print the parameters
print('a =', popt[0])
print('b =', popt[1])
print('c =', popt[2])

# Filter the rows with temperature values above 90 degrees
temp_threshold = 90
data = data[data[:, 1] > temp_threshold]

# Fit the data to the function
x = data[:, 0]
y = data[:, 1]
popt, pcov = curve_fit(f, x, y)

# Plot the data and the line of best fit
plt.scatter(x, y, label='Data')
plt.plot(x, f(x, *popt), color='red', label='Line of best fit')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.legend()
plt.show()

