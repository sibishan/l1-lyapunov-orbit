from lagrange import calc_l1, calc_l2

# Configs
M1 = 5.97217e24 # mass of earth (kg)
M2 = 7.3458e22  # mass of moon (kg)
R = 384400.0    # distance between earth and moom (km)

xl1 = calc_l1(M1, M2, R)
print(f"L1 position = {xl1} from the Moon")
xl2 = calc_l2(M1, M2, R)
print(f"L2 position = {xl2} from the Moon")



