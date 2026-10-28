import numpy as np

from methods.interpolate import lagint

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