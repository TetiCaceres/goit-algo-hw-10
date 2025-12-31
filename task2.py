import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# -------------------------------
# Function and integration limits
# -------------------------------
def f(x):
    return x**2

a, b = 0, 2
N = 100000  # Number of random points

# -------------------------------
# Monte Carlo Method
# -------------------------------
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, b**2, N)

under_curve = y_random <= f(x_random)
points_under_curve = np.sum(under_curve)

area_rectangle = (b - a) * (b**2)
integral_monte_carlo = area_rectangle * points_under_curve / N
print("Integral using Monte Carlo:", integral_monte_carlo)

# -------------------------------
# Verification using scipy.quad
# -------------------------------
result_quad, error_quad = spi.quad(f, a, b)
print("Integral using quad:", result_quad, "with error:", error_quad)

# -------------------------------
# Graphical visualization
# -------------------------------
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(np.linspace(a, b, 200), f(np.linspace(a, b, 200)), color='gray', alpha=0.3)

# Monte Carlo points
ax.scatter(x_random[under_curve], y_random[under_curve], color='green', s=5, label='Under the curve')
ax.scatter(x_random[~under_curve], y_random[~under_curve], color='red', s=5, label='Above the curve')

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Monte Carlo Method for f(x) = x^2')
ax.legend()
plt.grid()
plt.show()
