## [rp_bubble.py](rp_bubble.py)
[Expansion Evoulition](Results/images/Screenshot%202025-11-16%20150917.png) [Collapse Evolution](Results/images/Screenshot%202025-11-16%20150937.png)
This file plots a single general solution of the Rayleigh–Plesset equation, providing a visualization for $R(t)$ in both expansion and collapse. 

## [rp_para_radius.py](rp_para_radius.py)
[Radius Expansion Parametric Study](Results/images/Screenshot%202025-11-16%20150102.png) [Radius Collapse Parametric Study](Results/images/Screenshot%202025-11-16%20152116.png)
This file tests different radii between a minimum and maximum and plots their behavior as $R(t)$. This tests the sensitivity of $R_0$. For the 1st plot (expansion) we can conclude that it takes longer for the bubble to evolve given a larger initial radius. For the 2nd plot (collapse) we can conclude that it takes longer for the bubble to collapse given a larger initial radius. Given static initial parameters of the fluid, increasing the radius will increase both evolution times of the bubble. 

## [rp_para_velocity.py](rp_para_velocity.py)
[Velocity Parametric Study]()
This file tests different initial velocities of a bubble to test the sensitivity of the velocity variable, $\dot{R}$. For the case tested here, from the spread of $R(t)$ plots we can conclude that the solution $R(t)$ is not sensitive to the velocity variable. However, if the pressure or viscosity are small for the fluid, the solution would be sensitive to the initial velocity.

## [rp_para_density.py](rp_para_density.py)
[Density Parametric Study]()
This file tests different initial densities of a bubble to test the sensitivity of the density variable, $\rho_l$. From the spread of $R(t)$ plots, we can conclude that the solution $R(t)$ is sensitive to the density variable. This is because the high density of the liquid makes it hard to accelerate the bubble. 

## [rp_para_pressure.py](rp_para_pressure.py)
[Pressure Parametric Study]()
This file tests different initial internal pressures of a bubble to test the sensitivity of the internal pressure variable $p_B$. From the spread of $R(t)$ plots, we can conclude that the solution $R(t)$ is highly sensitive to the internal pressure of the bubble, and can produce large differences in growth and collapse.

## [rp_para_stension.py](rp_para_stension.py)
[Surface Tension Parametric Study]()
This file tests different initial surface tensions of a bubble to test the sensitivity of the surface tension variable $S$. For the larger tested radii, from the spread of $R(t)$ plots we can conclude that the solution $R(t)$ is not sensitive to the surface tension variable. However, for much smaller bubbles, surface tension becomes more important because of the $\frac{2S}{R}$ scaling.

## [rp_para_viscosity.py](rp_para_viscosity.py)
[Viscosity Parametric Study]()
This file tests different initial viscosities of a bubble to test the sensitivity of the viscosity variable $\nu_l$. From the spread of $R(t)$ plots, we can conclude that the solution $R(t)$ is sensitive to the viscosity variable. Higher viscosity dissipates energy and reduces expansion and collapse amplitudes and speeds.
