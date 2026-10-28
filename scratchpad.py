import numpy as np
import matplotlib.pyplot as plt

M1 = 5.97217e24
M2 = 7.3458e22
R = 384400.0

def f(r):
    lhs = M1 / (R - r)**2 - M2 / r**2
    rhs = (M1 / (M1 + M2) * R - r) * (M1 + M2) / R**3
    return lhs - rhs

# Plot around L1
r = np.linspace(50000, 65000, 1000)
y = f(r)

plt.plot(r, y)
plt.axhline(0, color="black", linewidth=0.8)

plt.xlabel("Distance from Moon, r (km)")
plt.ylabel("f(r)")
plt.title("Earth-Moon L1 Root")
plt.grid()

plt.show()