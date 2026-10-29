from methods.roots import bracketing, bisection

def calc_l1(M1, M2, R):
    # source: https://en.wikipedia.org/wiki/Lagrange_point
    def f(r):
        lhs = M1 / (R - r) ** 2 - M2 / r ** 2
        rhs = (M1 / (M1 + M2) * R - r) * (M1 + M2) / R ** 3
        return lhs - rhs

    brackets = bracketing(f,50000,60000, n=100) # we know what range to pick by graphing f(r)

    if len(brackets) != 1: # there can be only 1 root
        raise ValueError(f"[calc_l1] expected 1 root, found {len(brackets)}")

    root = bisection(f,brackets[0][0], brackets[0][1], tol=1e-14)
    return root
