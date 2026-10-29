import numpy as np

from methods.roots import bracketing, bisection
from methods.interpolate import lagint
from methods.ode import rk4solve

def test_bisection():
    def f(x):
        return x**2 - 4 
    
    actual = 2 # we already know that roots are +2 / -2

    # we are going to check for +2, and only 1 root is possible in [1,3]
    brackets = bracketing(f, 1, 3, 50)
    calculated = bisection(f, brackets[0][0], brackets[0][1], tol=1e-10)

    error = abs(calculated - actual)

    assert error < 1e-14

    print("[Bracketing & Bisection Root Finding] Passed\n")

def test_lagrange():
    # we know these points come from f(x) = x^2
    xp = np.array([[-1], [0], [1]])
    yp = np.array([[1], [0], [1]])

    actual = 0.25  # because f(0.5) = 0.5^2 = 0.25

    # use Lagrange interpolation to estimate the value at x = 0.5
    calculated = lagint(0.5, xp, yp)

    error = abs(calculated - actual)

    assert error < 1e-14

    print("[Lagrange Interpolation] Passed\n")

def test_rk4():
    # we know the exact solution to y'' + 4y = 0 is y = cos(2t)
    def f(s):
        y, v = s

        dydt = v
        dvdt = -4 * y

        return np.array([dydt, dvdt])

    # initial conditions: y(0) = 1 and y'(0) = 0
    s0 = np.array([1.0, 0.0])

    # solve from t = 0 to t = 1 using RK4
    t, s = rk4solve(f, 0.0, s0, 1.0, 0.01)

    # get the numerical values at t = 1
    calculated_y = s[-1, 0]
    calculated_v = s[-1, 1]

    # exact values at t = 1
    actual_y = np.cos(2)
    actual_v = -2 * np.sin(2)

    error_y = abs(calculated_y - actual_y)
    error_v = abs(calculated_v - actual_v)

    assert error_y < 1e-6
    assert error_v < 1e-6

    print("[4th-order Runge-Kutta] Passed\n")


test_bisection()
test_lagrange()
test_rk4()