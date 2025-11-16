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
Rdot0 = 0.0          # m/s (initial radial velocity)
t_span = (0, 1e-4)   # s (time range)
title = 'Radius Parametric Study'

# --- Critical Radius ---
def R_crit(S, pb, p_inf):
    return (2 * S) / (pb - p_inf)
Rcrit = R_crit(S, pb, p_inf)

# --- Expansion and Collapse from Critical Initial Radius ---
Ro = Rcrit * 10       # Expansion
Ru = Rcrit / 10        # Collapse
R_L = np.array([Ro, Ru])

# --- System of Equations (Rayleigh–Plesset Simplified) ---
def sys(t,y):
    R, Rdot = y
    dRdt = Rdot
    dRdotdt = (1/R) * ( (pb - p_inf)/rhol - (3/2)*Rdot**2 - (4*nul*Rdot)/R - (2*S)/(rhol*R) )
    return [dRdt, dRdotdt]
   
# --- Calculations ---
def bubble_solution(p):
    y0 = [p, Rdot0]       # <-- here p becomes the initial radius for the ODE
    sol = solve_ivp(sys, t_span, y0, method='Radau', max_step=1e-8)
    return sol.t, sol.y[0]
        
        
# --- Loop over Radii ---
for i in range(len(R_L)):
    R0 = R_L[i]

    if R0 > Rcrit:
        # Expansion: R0 is max
        start = Rcrit 
        end = R0
        title = f"Expansion Sweep: R0 = {R0:.3e} m"
    else:
        # Collapse: R0 is min
        start = R0
        end = Rcrit 
        title = f"Collapse Sweep: R0 = {R0:.3e} m"

    # Call parametric study
    parametric_study(
        n_runs = 8,
        min = start,
        max = end,
        func = bubble_solution,
        title = title,
        xlabel = 'Radius (m)',
        ylabel = 'Time (s)',
        skip_crit = True,
        critical_val = Rcrit,
        sweep_name = 'R0'
    )
    
