# Understanding the Rayleigh-Plesset Equation
This is where I will document the code for visualizing and understanding the generalized Rayleigh-Plesset Equation. 

This project provides a set of Python tools for modeling bubble dynamics using the Rayleigh–Plesset equation, which governs the radius of a spherical bubble in an infinite body of liquid over time.

The repository includes a program [rp_bubble.py](rp_bubble.py) that:

  - Accepts fluid and bubble initial parameters.
  - Let's the user choose cavitation or expansion behavior.
  - Plots the resulting bubble radius R(t) for a visualization of bubble cavitation.

Parametric studys including: [rp_para_radius.py](rp_para_radius.py), [rp_para_pressure.py](rp_para_pressure.py), [rp_para_viscosity.py](rp_para_viscosity.py), [rp_para_velocity.py](rp_para_velocity.py), [rp_para_stension.py](rp_para_stension.py), [rp_para_density.py](rp_para_density.py), that explore changes in:

  - radius, pressure, viscosity, velocity,
  - surface tension, and density
  - affect bubble evolution.

Each parametric script calls a central helper module, [paraStudy.py](paraStudy.py), which runs the simulations and produces plots.

## Generalized Rayleigh–Plesset Equation

The Rayleigh–Plesset equation describes the radial dynamics of a spherical bubble in an incompressible fluid.  
It is given by:

$$
\frac{p_B(t) - p_\infty(t)}{\rho_L} = R\\ddot{R} + \frac{3}{2}\dot{R}^2 + \frac{4\nu_L}{R}\dot{R} + \frac{2S}{\rho_L R}
$$

### Where:
- $\( R(t) \)$ — bubble radius  
- $\( \dot{R} = \frac{dR}{dt} \)$ — bubble wall velocity  
- $\( \ddot{R} = \frac{d^2R}{dt^2} \)$ — bubble wall acceleration  
- $\( \rho_L \)$ — liquid density  
- $\( \nu_L \)$ — kinematic viscosity  
- $\( S \)$ — surface tension  
- $\( p_B(t) \)$ — pressure inside the bubble  
- $\( p_\infty(t) \)$ — far-field (ambient) pressure  


This 2nd Order nonlinear ODE governs cavitation, bubble growth, and collapse under varying physical conditions.
