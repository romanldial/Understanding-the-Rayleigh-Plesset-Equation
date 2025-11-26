import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# -----------------------------
# Physical constants (SI units)
# -----------------------------
rhoL  = 1000.0      # kg/m^3
nuL   = 9e-3        # m^2/s     (kinematic viscosity)
S     = 0.0728       # N/m       (surface tension)
R0    = 1e-3       # m
k     = 1.4         # polytropic exponent
p_v   = 2300        # Pa  (vapor pressure of liquid)
pG0  =  8e-3         # Pa  (gas pressure at R0)           # run at  = 0

# External pressure function:
def p_inf(t): 
    p0 = 1e5 # Pa
    dp = 9e4  #Pa
    freq = 450 # 1/s
    #return (p0 - dp)*np.sin(2*np.pi*freq*t)
    return p0 - dp 

# -----------------------------
# Rayleigh–Plesset RHS
# -----------------------------
def RPE(t, y):
    R, Rdot = y
    
    # avoid divide-by-zero
    if R <= 0:  # numerical safety
        R = 1e-12
    
    term1 = (p_v - p_inf(t)) / rhoL
    term2 = (pG0 / rhoL) * (R0 / R)**(3*k)
    
    acc = ( term1 + term2
            - 1.5*Rdot**2
            - 4*nuL*Rdot/R
            - 2*S/(rhoL*R)
          ) / R
    
    return [Rdot, acc] # returns velocity and acceleration

# -----------------------------
# Solve ODE
# -----------------------------
t_span = (0, 0.004)        # 1 s window
t_eval = np.linspace(*t_span, 2000)

y0 = [R0, 0.0]             # initial radius and initial velocity

sol = solve_ivp(RPE, t_span, y0, t_eval=t_eval, max_step=1e-6)
t = sol.t
R = sol.y[0]
Rdot = sol.y[1]

# -----------------------------
# Choose characteristic velocity U_ref
# -----------------------------
U_ref = np.max(np.abs(Rdot))      # MAXIMUM refrence velosity for Re and We

# Alternative:
# We = 10.0
# U_ref = np.sqrt(We * S / (rhoL * R0))

# nondimensional axes
t_nd = U_ref * t / R0
R_nd = R / R0

# -----------------------------
# Compute Re and We for legend
# -----------------------------
# dynamic viscosity mu = rho * nu
mu = rhoL * nuL

Re = rhoL * U_ref * R0 / mu
We = rhoL * U_ref**2 * R0 / S 
# Alternative:
#We = We

plt.figure(figsize=(6,4))
plt.plot(t_nd, R_nd, lw=2,
         label=f"Re={Re:.1e},  We={We:.1e}")

plt.xlabel(r"$U_{\rm ref} t / R_0$")
plt.ylabel(r"$R/R_0$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
