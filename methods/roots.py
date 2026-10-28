import numpy as np

def bracketing(f, a, b, n=20):
    range = np.linspace(a, b, n)
    
    brackets = []
    
    idx = 0
    while idx < len(range) - 1:
        p1 = f(range[idx])
        p2 = f(range[idx + 1])
        if (p1 > 0 and p2 < 0) or (p1 < 0 and p2 > 0):
            brackets.append([range[idx], range[idx + 1]])
        
        idx += 1
    
    return brackets

def bisection(f, a, b, tol=1e-10):
    while True:
        f_a = f(a)
        f_b = f(b)
        
        if (f_a > 0 and f_b < 0) or (f_a < 0 and f_b > 0):
            c = (a + b) / 2
            f_c = f(c)
            
            if f_c == 0:
                return c
            elif abs(f_c - f_a) < tol:
                return c
            elif f_c > 0:
                if f_a > 0:
                    a = c
                else:
                    b = c
            elif f_c < 0:
                if f_a > 0:
                    b = c
                else:
                    a = c
        
        # edge cases
        elif f_a == 0:
            return a
        elif f_b == 0:
            return b
        else:
            raise ValueError("a and b have the same sign")