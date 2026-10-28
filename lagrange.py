from methods.roots import bracketing, bisection

M1 = 5.97217e24
M2 = 7.3458e22
R = 384400.0

def calc_l1(M1, M2, R):
    def f(r):
        lhs = M1 / (R - r) ** 2 - M2 / r ** 2
        rhs = (M1 / (M1 + M2) * R - r) * (M1 + M2) / R ** 3
        return lhs - rhs

    brackets = bracketing(f,50000,60000, n=100)
    print("Roots are with in",brackets)

    roots = []
    for bracket in brackets:
        roots.append(bisection(f,bracket[0], bracket[1], tol=1e-10))

    print(roots)

calc_l1(M1, M2, R)