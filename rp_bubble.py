#Roman Dial 
#Rayleigh-Plesset Bubble Evolution 


# Import
import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp


# Parameters
rhol = 998.0         # kg/m^3
nul = 1.004e-6       # m^2/s
S = 0.0728           # N/m
pb = 1.2e5           # Pa
p_inf = 1.0e5        # Pa


# Critical R - - for inital value - - R0 < R_crit = collapse, R0 > R_crit = expand
def R_crit(S, pb, p_inf):
    return ( 2 * S ) / ( pb - p_inf) 
# print(R_crit(S, pb, p_inf))


# Prompt for initial conditions
variable = input('Do you want to see bubble expansion or collapse? Enter E for expansion and C for collapse: ').strip().lower()
if variable == 'e':
    R0 = R_crit(S, pb, p_inf) * 10
elif variable == 'c':
    R0 = R_crit(S, pb, p_inf) / 10

Rdot0 = 0.0  # (m/s)
y0 = np.array([R0, Rdot0]) 
 
  
# System of Equations
def sys(t,y):
    R, Rdot = y
    dRdt = Rdot
    dRdotdt = (1/R) * ( (pb - p_inf)/rhol - (3/2)*Rdot**2 - (4*nul*Rdot)/R - (2*S)/(rhol*R) )
    return [dRdt, dRdotdt]


# Numerically Solve 
sol = solve_ivp(sys, [0, 0.0001], y0 = y0, method = 'Radau', max_step = 1e-8)


# Figure
fig, ax = plt.subplots(figsize=(8,5))
ax.plot(sol.t, sol.y[0], color='royalblue', linewidth=2)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Bubble Radius (m)')
ax.set_title('Rayleigh–Plesset Bubble Evolution')
ax.ticklabel_format(style='sci', scilimits=(0,0), axis='both')
ax.grid(True, linestyle='--', alpha=0.6)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.show()
