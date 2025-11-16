from paraStudy import parametric_study
import numpy as np
from scipy.integrate import solve_ivp
"""
Takes parameters for composition of water and does a study to see how 
changing the inital Viscosity of the bubble affects the cavitation.
"""
# --- Parameters ---
rhol = 998.0                                             # kg/m^3
S = 0.0728                                               # N/m (surface tension)
R0 = 1e-3                                                 # m (inital radius)
Rdot0 = 0.0                                            # m/s (inital velocity)
t_span = (0, 1e-4)                                    # time span
pb = 1.2e5                                             # Pa (bubble pressure)
p_inf = 1e5                                            # Pa (ambient pressure)
nul_range = [-1.0e3, 1.0e3]                     # N/m (range of Surface tension values)
n_runs = 10                                            # number of runs
title='Viscosity Parametric Study'     #title

# --- System of Equations ---
def sys(t, y, nul):
    R, Rdot = y
    dRdt = Rdot
    dRdotdt = (1/R) * ((pb - p_inf)/rhol - (3/2)*Rdot**2 - (4*nul*Rdot)/R - (2*S)/(rhol*R))
    return [dRdt, dRdotdt]

# --- Bubble solution ---
def bubble_solution(nul):
    y0 = [R0, Rdot0]
    sol = solve_ivp(sys, t_span, y0, args=(nul,), method='Radau', max_step=1e-8)
    return sol.t, sol.y[0]

# --- Parametric Study ---
parametric_study(
    n_runs=n_runs,
    min=nul_range[0],
    max=nul_range[1],
    func=bubble_solution,
    title=title,
    xlabel='Time (s)',
    ylabel='Radius (m)',
    skip_crit=False,
    critical_val=None,
    sweep_name='nul'
)
