from paraStudy import parametric_study
import numpy as np
from scipy.integrate import solve_ivp
"""
Takes parameters for composition of water and does a study to see how 
changing the inital internal pressure of the bubble affects the cavitation.
"""
# --- Parameters ---
rhol = 998.0
nul = 1.004e-6
S = 0.0728
R0 = 1e-3
Rdot0 = 0.0
t_span = (0, 1e-4)
p_inf = 1e5
p_range = [1.0e3, 1.0e7]
n_runs = 10
title='Pressure Parametric Study'

# --- System of Equations ---
def sys(t, y, pb):
    R, Rdot = y
    dRdt = Rdot
    dRdotdt = (1/R) * ((pb - p_inf)/rhol - (3/2)*Rdot**2 - (4*nul*Rdot)/R - (2*S)/(rhol*R))
    return [dRdt, dRdotdt]

# --- Bubble solution ---
def bubble_solution(pb):
    y0 = [R0, Rdot0]
    sol = solve_ivp(sys, t_span, y0, args=(pb,), method='Radau', max_step=1e-8)
    return sol.t, sol.y[0]

# --- Parametric Study ---
parametric_study(
    n_runs=n_runs,
    min=p_range[0],
    max=p_range[1],
    func=bubble_solution,
    title=title,
    xlabel='Time (s)',
    ylabel='Radius (m)',
    skip_crit=False,
    critical_val=None,
    sweep_name='Pb'
)
