# Understanding-the-Rayleigh-Plesset-Equation
This is where I will document the code for visualizing understanding the generalized Rayleigh-Plesset Equation. 

This project provides a set of Python tools for modeling bubble dynamics using the Rayleigh–Plesset equation, which governs the radius of a spherical bubble in an infinite body of liquid over time.

The repository includes a program rp_bubble.py that:

  - Accepts fluid and bubble initial parameters.
  - Let's the user choose cavitation or expansion behavior.
  - Plots the resulting bubble radius R(t) for a visualization of bubble cavitation.

A parametric study suite that explores how changes in:

  - radius, pressure, viscosity, velocity,
  - surface tension, and density
  - affect bubble evolution.

Each parametric script calls a central helper module, paraStudy.py, which runs the simulations and produces plots.

## Generalized Rayleigh–Plesset Equation

The Rayleigh–Plesset equation describes the radial dynamics of a spherical bubble in an incompressible fluid.  
It is given by:

$$
\rho\!\left(R\ddot{R} + \tfrac{3}{2}\dot{R}^2\right)
= P_B(t) - P_\infty(t) - 4\mu \frac{\dot{R}}{R} - \frac{2\sigma}{R}
$$

Where:

- $\( R(t) \)$ = bubble radius  
- $\( \dot{R} \)$ = first time derivative (bubble wall velocity)  
- $\( \ddot{R} \)$ = second time derivative (bubble wall acceleration)  
- $\( \rho \)$ = liquid density  
- $\( \mu \)$ = dynamic viscosity  
- $\( \sigma \)$ = surface tension  
- $\( P_B(t) \)$ = pressure inside the bubble  
- $\( P_\infty(t) \)$ = far-field (ambient or driving) liquid pressure  

This nonlinear ODE governs cavitation, bubble growth, and collapse under varying physical conditions.
