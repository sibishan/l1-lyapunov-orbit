import numpy as np
import matplotlib.pyplot as plt

from lagrange import calc_l1
from cr3bp import int_cr3bp
from crossing import find_crossing

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

# Integrate trajectory
t, s = int_cr3bp(x0, MU)

# Find next y = 0 crossing
tc, sc = find_crossing(t, s)

if sc is not None:
    print("\ny = 0 crossing")
    print(f"t  = {tc}")
    print(f"x  = {sc[0]}")
    print(f"y  = {sc[1]}")
    print(f"vx = {sc[2]}")
    print(f"vy = {sc[3]}")
else:
    print("No crossing found")

# Plot
plt.plot(s[:, 0], s[:, 1], label="Spacecraft")

plt.scatter(xl1, 0, label="L1")
plt.scatter(1 - MU, 0, label="Moon")

if sc is not None:
    plt.scatter(sc[0], sc[1], label="y = 0 crossing")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Trajectory near L1")
plt.axis("equal")
plt.grid()
plt.legend()

plt.show()