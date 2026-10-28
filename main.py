import numpy as np
import matplotlib.pyplot as plt

from lagrange import calc_l1
from cr3bp import int_cr3bp

# Configs
M1 = 5.97217e24 # mass of earth (kg)
M2 = 7.3458e22  # mass of moon (kg)
R = 384400.0    # distance between earth and moom (km)

# Constants
MU = M2 / (M1 + M2) # mass ratio

# Procedure
# Locating L1
rl1 = calc_l1(M1, M2, R)
print(f"L1 position = {rl1} km from the Moon")

# Convert L1 to normalised CR3BP coordinates
xl1 = 1 - MU - rl1 / R
print(f"Normalised L1 position = {xl1}")

x0 = xl1 - 0.01 # Initial position slightly displaced from L1
t, s = int_cr3bp(x0, MU)

plt.plot(s[:, 0], s[:, 1])

plt.scatter(xl1, 0, label="L1")
plt.scatter(1 - MU, 0, label="Moon")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Trajectory near L1")
plt.axis("equal")
plt.grid()
plt.legend()

plt.show()