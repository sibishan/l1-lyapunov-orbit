import numpy as np

from methods.ode import rk4solve

def f(s, mu):
    # source: https://ntrs.nasa.gov/api/citations/20160010593/downloads/20160010593.pdf
    x, y, vx, vy = s

    r1 = np.sqrt((x + mu)**2 + y**2)        # distance from spacecraft to earth
    r2 = np.sqrt((x - 1 + mu)**2 + y**2)    # distance from spacecraft to moon

    # accelerations
    ax = 2 * vy + x - (1 - mu) * (x + mu) / r1**3 - mu * (x - 1 + mu) / r2**3
    ay = -2 * vx + y - (1 - mu) * y / r1**3 - mu * y / r2**3

    return np.array([vx, vy, ax, ay])

def int_cr3bp(x0, mu, vy0=0.1, tmax=10.0, h=0.001):
    s0 = np.array([
        x0,     # x
        0.0,    # y
        0.0,    # vx
        vy0     # vy (our intial guess)
        ])

    t, s = rk4solve(f, 0.0, s0, tmax, h, mu)

    return t, s
