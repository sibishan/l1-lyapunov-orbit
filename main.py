from lagrange import calc_l1, calc_l2

# Configs
M1 = 5.97217e24 # mass of earth (kg)
M2 = 7.3458e22  # mass of moon (kg)
R = 384400.0    # distance between earth and moom (km)

# Constants
MU = M2 / (M1 + M2) # mass ratio

# Procedure
# Locating L1 & L2
rl1 = calc_l1(M1, M2, R)
print(f"L1 position = {rl1}km from the Moon")
rl2 = calc_l2(M1, M2, R)
print(f"L2 position = {rl2}km from the Moon")

# Rotating-frame position: origin at the barycentre, distances in units of R
xl1 = 1 - MU - rl1 / R
xl2 = 1 - MU + rl2 / R

