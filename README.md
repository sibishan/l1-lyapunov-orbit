# L1 Lyapunov Orbit

Author: Sibishan Ravindran

This project numerically computes a planar Lyapunov orbit, a periodic orbit around the Earth–Moon L1 Lagrange point. The spacecraft's motion is modelled with the Circular Restricted Three-Body Problem (CR3BP) in normalised, rotating coordinates. All numerical methods (root finding, interpolation, ODE integration and the shooting method) are implemented from scratch.

## How a orbit is found

1. **Locate L1:** Solve the L1 force-balance equation for the distance from the Moon, using bracketing and then bisection.
2. **Normalise:** Convert L1 to CR3BP coordinates and start the spacecraft slightly displaced from it (`x0 = xL1 - 0.01`, `y0 = 0`, `vx0 = 0`).
3. **Shooting method:** A symmetric periodic orbit must cross `y = 0` with `vx = 0`. For each trial `vy0`, integrate the CR3BP equations with 4th-order Runge–Kutta (RK4), find the next `y = 0` crossing, and use Lagrange interpolation to estimate `vx` there. Bracketing and bisection on `vy0` drive this `vx` to zero.
4. **Integrate with the correct `vy0`:** Find the half-period `y = 0` crossing again, which gives the period (`T = 2 * t_crossing`).
5. **Verify:** Integrate one full period, check the closing error between the initial and final states, and plot the orbit.

## File structure

```
lyapunov-orbits/
├── main.py              # Runs the full procedure: finds the orbit, prints results, plots it
├── lagrange.py          # calc_l1: locates the Earth–Moon L1 point
├── cr3bp.py             # CR3BP equations of motion and integrator wrapper
├── shooting.py          # y = 0 crossing detection and shooting method for vy0
├── tests.py             # Tests for the numerical methods
└── methods/
    ├── roots.py         # Bracketing and bisection root finding
    ├── interpolate.py   # Lagrange interpolation
    └── ode.py           # RK4 ODE solver
```

## Running

Requires Python 3 with `numpy` and `matplotlib`:

```bash
pip install numpy matplotlib
```

Run the orbit computation (the shooting step takes around 30 seconds; a plot window opens at the end):

```bash
python3 main.py
```

Run the tests for bracketing, bisection, Lagrange interpolation and 4th-order Runge-Kutta methods:

```bash
python3 tests.py
```