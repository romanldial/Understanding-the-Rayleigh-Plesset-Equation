# Understanding the Rayleigh–Plesset Equation

This repository contains Python tools for visualizing and analyzing the generalized Rayleigh–Plesset equation (RPE), which governs the radius of a spherical bubble in an infinite liquid.

The main script **[`RPEbubbleEvo.py`](Python%20Files/RPEbubbleEvo.py)** plots the non-dimensional bubble radius $R(t)/R_0$ against the non-dimensional time $U_{\rm ref} t / R_0$.

The simulation also computes the Reynolds and Weber numbers exactly as implemented in the code:

$Re = \rho_L U_{\rm ref} R_0 / \mu$  
$We = \rho_L U_{\rm ref}^2 R_0 / S$

Where:   $\mu = \rho_L \nu_L$

The quantification of the dimensionless Reynalds Number $(Re)$ and the dimensionless Weber Number $(We)$ allow us to coralate inner term dominance to bubble evolution behavior. The results and observations are available here: **[`Results.md`](Results/Results.md)**

---

# Generalized Rayleigh–Plesset Equation

Under adiabatic or polytropic gas compression, the Rayleigh–Plesset equation is:

$$
\frac{p_B(t)-p_\infty(t)}{\rho_L} + \frac{p_{G0}}{\rho_L}\left(\frac{R_0}{R}\right)^{3k} = R\ddot{R} + \frac{3}{2}\dot{R}^2 + \frac{4\nu_L}{R}\dot{R} + \frac{2S}{\rho_L R}.
$$

### Where:
- $R(t)$ — bubble radius  
- $\dot{R}$ — bubble wall velocity  
- $\ddot{R}$ — bubble wall acceleration  
- $R_0$ — initial bubble radius  
- $k$ — polytropic exponent  
- $p_{G0}$ — initial gas pressure  
- $\rho_L$ — liquid density  
- $\nu_L$ — kinematic viscosity  
- $S$ — surface tension  
- $p_B(T)$ — bubble internal pressure  
- $p_\infty(t)$ — far-field liquid pressure  

This nonlinear second-order ODE governs bubble growth, collapse, and cavitation behavior.

---

# Using **[`RPEbubbleEvo.py`](Python%20Files/RPEbubbleEvo.py)**

To use this simulation, simply choose a test case and input values from the [Inputs](Results/Results.md#Table-of-Inputs) data table. There will be a couple simulation options, feel free to either use the simulation data or input your own values; the script does the work!
