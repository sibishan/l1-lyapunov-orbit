import numpy as np

from methods.interpolate import lagint
from methods.roots import bracketing, bisection
from cr3bp import int_cr3bp

def find_crossing(t, s):
    for i in range(1, len(t) - 1): # we skip the initial point because the trajectory starts at y = 0
        y1 = s[i, 1]
        y2 = s[i + 1, 1]
        # detect a crossing of y = 0
        if y1 * y2 < 0: 
            # interpolate time as a function of y
            yp = np.array([[y1],[y2]])
            tp = np.array([[t[i]],[t[i + 1]]])

            tc = lagint(0.0, yp, tp)

            # interpolate the state at the crossing time
            times = np.array([[t[i]],[t[i + 1]]])

            sc = np.zeros(4)

            for j in range(4):
                values = np.array([[s[i, j]],[s[i + 1, j]]])
                sc[j] = lagint(tc, times, values)

            return tc, sc
    return None, None

# source: https://en.wikipedia.org/wiki/Shooting_method
def shooting_error(x0, mu, vy0):
    # Integrate using the trial initial y velocity
    t, s = int_cr3bp(x0, mu, vy0)

    # Find the next y = 0 crossing
    tc, sc = find_crossing(t, s)

    if sc is None:
        raise ValueError("[shooting_error] No y = 0 crossing found!")

    return sc[2] # for a symmetric periodic orbit, vx = 0 at the crossing

# Find the initial y-velocity that makes vx = 0 at the next y = 0 crossing
def find_initial_vy(x0, mu):
    def wrap(vy0):
        return shooting_error(x0, mu, vy0)

    brackets = bracketing(wrap, 0.05, 0.15, n=20)   # by trial and error, we searched around the initial vy guess of 0.1 
                                                    # for a sign change in the shooting error
    if brackets is None:
        raise ValueError("[find_initial_vy] no brackets found!")

    a, b = brackets[0] # we know that only 1 root is possible in this case
    vy0 = bisection(wrap, a, b, tol=1e-14)
    return vy0