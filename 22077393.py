import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# Step 1: Read data and calculate mean and standard deviation
data_file = 'data3-2.csv'
data = pd.read_csv(data_file, header=None, names=['Salary'])
mean_salary = data['Salary'].mean()
std_dev = data['Salary'].std()

# Step 2: Plot histogram and overlay with a normal distribution curve
plt.hist(data['Salary'], bins=30, density=True, alpha=0.7, color='orange', label='Empirical PDF')

# Plot the normal distribution curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
pdf = norm.pdf(x, mean_salary, std_dev)
plt.plot(x, pdf, 'k', linewidth=2, label='Normal Distribution Fit')

# Plot the mean salary
plt.axvline(mean_salary, color='red', linestyle='dashed',
            linewidth=2, label=f'Mean Salary: {mean_salary:.2f} Euros')

# Step 3: Calculate and visualize the required value X (percentile_below_X)
percentile_below_X = 33
X_value = np.percentile(data['Salary'], percentile_below_X)
plt.axvline(X_value, color='green', linestyle='dashed', linewidth=2,
            label=f'{percentile_below_X}% Below X='+str(X_value))

# Step 4: Add labels, titles, legend, etc.
plt.xlabel('Annual Salary (Euros)')
plt.ylabel('Probability Density')
plt.title('Salary Distribution Analysis with Normal Distribution Fit')
plt.legend()

# Step 5: Print and display results
print("Mean Salary:", mean_salary)
print(f'{percentile_below_X}% Below X Value: {X_value:.2f} Euros')

# Step 6: Display the plot
plt.show()
