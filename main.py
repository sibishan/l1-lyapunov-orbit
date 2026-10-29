import numpy as np
import matplotlib.pyplot as plt

from lagrange import calc_l1
from cr3bp import int_cr3bp
from shooting import find_initial_vy, find_crossing

# CONSTANTS
M1 = 5.97217e24 # mass of earth (kg)
M2 = 7.3458e22  # mass of moon (kg)
R = 384400.0    # distance between earth and moom (km)
MU = M2 / (M1 + M2) # mass ratio
UNIT_TIME = 4.34837740 # earth moon cr3bp time unit

# PROCEDURE
# Locate L1
rl1 = calc_l1(M1, M2, R)
print(f"L1 position = {rl1} km from the Moon")

# Convert L1 to normalised CR3BP coordinates
xl1 = 1 - MU - rl1 / R
print(f"Normalised L1 position = {xl1}")

x0 = xl1 - 0.01 # we displace slightly from L1, because starting exactly at L1 would remain at equilibrium

# Find the initial y-velocity that makes the orbit symmetric and periodic
print("\nFinding the correct initial y-velocity using the shooting method...")
print("Please wait around 30 seconds\n")
vy0 = find_initial_vy(x0, MU)
print("Correct initial vy = ", vy0)

# Integrate with the corrected initial velocity
t, s = int_cr3bp(x0, MU, vy0=vy0)

# and find the half-period y = 0 crossing
tc, sc = find_crossing(t, s)

if sc is None:
    raise ValueError("[main] no y = 0 crossing found!")

print("\nAt half-period crossing,")
print("t =", tc)
print("x =", sc[0])
print("y =", sc[1])
print("vx =", sc[2])
print("vy =", sc[3])

# The next y = 0 crossing corresponds to half of the orbit
period = 2 * tc
days = period * UNIT_TIME
print(f"\nEstimated period {period} ({days} days)")

# Integrate for one complete orbit
t, s = int_cr3bp(x0, MU, vy0=vy0, tmax=period)
initial_state = s[0]
final_state = s[-1]

print("\nInitial state =", initial_state)
print("Final state   =", final_state)
print("Difference    =", final_state - initial_state)

closing_error = np.linalg.norm(final_state - initial_state)
print("Closing error =", closing_error)

# Plot
plt.plot(s[:, 0], s[:, 1], label="Orbit")

plt.scatter(xl1, 0, label="L1")
plt.scatter(1 - MU, 0, label="Moon")

plt.xlabel("x (normalised)")
plt.ylabel("y (normalised)")
plt.title(f"A planar Lyapunov orbit about Earth-Moon L1 point\nwith period = {days:.4f} days")
plt.axis("equal")
plt.grid()
plt.legend()

plt.show()