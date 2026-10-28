import numpy as np

def rk4solve(f, t0, s0, tmax, h, mu):
    t = np.array([t0])
    s = np.array([s0], dtype=float)

    while t0 < tmax:
        # Shorten the final step so we finish exactly at tmax
        step = min(h, tmax - t0)

        k1 = f(s0, mu)
        k2 = f(s0 + (step / 2) * k1, mu)
        k3 = f(s0 + (step / 2) * k2, mu)
        k4 = f(s0 + step * k3, mu)

        s0 = s0 + (step / 6) * (k1 + 2*k2 + 2*k3 + k4)
        t0 += step

        t = np.append(t, t0)
        s = np.vstack([s, s0])

    return t, s