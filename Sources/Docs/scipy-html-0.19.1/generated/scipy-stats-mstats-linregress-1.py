import matplotlib.pyplot as plt
from scipy import stats
np.random.seed(12345678)
x = np.random.random(10)
y = np.random.random(10)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# To get coefficient of determination (r_squared)

print("r-squared:", r_value**2)
# ('r-squared:', 0.080402268539028335)

# Plot the data along with the fitted line

plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.legend()
plt.show()
