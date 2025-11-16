# Roman Dial 
# Rayleigh-Plesset Bubble Evolution 

# --- Imports ---
from paraStudy import parametric_study
import numpy as np
from scipy.integrate import solve_ivp

# --- Parameters (water) ---
rhol = 998.0         # kg/m^3
nul = 1.004e-6       # m^2/s (kinematic viscosity)
S = 0.0728           # N/m (surface tension)
pb = 1.2e5           # Pa (bubble pressure)
p_inf = 1.0e5        # Pa (ambient pressure)
R0 = 1e-3         # m/s (initial radial velocity)
Rdot_range = [0, 1]        # m/s (range for inital velocities)
n_runs = 10                                            # number of runs
t_span = (0, 1e-4)   # s (time range)
title = 'Inital Velocity Parametric Study'

# --- System of Equations ---
def sys(t, y):
    R, Rdot = y
    dRdt = Rdot
    dRdotdt = (1/R) * ((pb - p_inf)/rhol - (3/2)*Rdot**2 - (4*nul*Rdot)/R - (2*S)/(rhol*R))
    return [dRdt, dRdotdt]

# --- Bubble solution ---
def bubble_solution(Rdot):
    Rdot0 = Rdot
    y0 = [R0, Rdot0]
    sol = solve_ivp(sys, t_span, y0, method='Radau', max_step=1e-8)
    return sol.t, sol.y[0]

# --- Parametric Study ---
parametric_study(
    n_runs=n_runs,
    min=Rdot_range[0],
    max=Rdot_range[1],
    func=bubble_solution,
    title=title,
    xlabel='Time (s)',
    ylabel='Radius (m)',
    skip_crit=False,
    critical_val=None,
    sweep_name='Rdot'
)
