# Results
---
### Oscilation, Frequency, and Damping Considerations
| ![Screenshot 2025-11-25 163211.png](images/Screenshot%202025-11-25%20163211.png) | ![Screenshot 2025-11-25 163810.png](images/Screenshot%202025-11-25%20163810.png) |
|---|---|
| ![Screenshot 2025-11-25 163058.png](images/Screenshot%202025-11-25%20163058.png) | ![Screenshot 2025-11-25 162936.png](images/Screenshot%202025-11-25%20162936.png) |

_The below assumptions are made in scale with the magnitudes of $Re$ and $We$ tested._

When considering the Reynalds Number $(Re)$, we can conclude that the trends show that decreasing $Re$ by an order of magnitude visually **increases** the frequency of the bubble oscilation, and the amplitude of the dimensionless radius **decreases** throughout the oscilation. This is because in lowering $Re$ the viscous forces become more prominent, in turn they damp the system more. The opposite is shown in the high $Re$ where the inertial forces dominate and the bubble continues to oscilate. Hence, **we can see a trend in the bubbles evolution lasting longer with a higher $Re$**.

When considering the Weber Number $(We)$, we can conclude that the trends show that larger values of $We$ reduce the restoring force of the surface tension hence making the amplitude of the oscilations grow **larger** and more violent. Because the inertial forces dominate in a high $We$, we can also say that a higher $We$ can result in **more** oscilations. When this surface tension restoring force is high, the bubble does **not** oscilate very much as damps out quickly.

---

### Magnitude and Evolution Considerations
| ![Screenshot 2025-11-25 163136.png](images/Screenshot%202025-11-25%20163136.png) | ![Screenshot 2025-11-25 165651.png](images/Screenshot%202025-11-25%20165651.png) |
|---|---|

When considering these trends in addition to those above, we can conclude two things. One: with a **low** $Re$ and a **low** $We$, the bubble trends to collapse once and damp out quickly. Two: with a **high** $Re$ and a **high** $We$ the bubble ocilates many times before settling. 

---

# Table of Inputs
Here is a collection of tables for input values used to generate the images above. 

|        | Re= 1.3e4; We=9.6e5 | Re= 4.4 ; We= 1.3e2 | Re= 6.2e2; We= 5.2e4 | Re=3e-2 ; We= 8e1 | Re= 7.5e3; We=1.2e6 | Re= 2.3e-1; We=5.8 |
| ------ | ------------------- | ------------------- | -------------------- | ----------------- | ------------------- | ------------------ |
| rhoL   | 1000                | 1000                | 1000                 | 1000              | 1000                | 100                |
| nuL    | 2.00E-05            | 7.00E-04            | 1.00E-04             | 8.00E-03          | 4.00E-05            | 9.00E-03           |
| S      | 0.0728              | 0.0728              | 0.0728               | 0.0728            | 0.0728              | 0.0728             |
| R0     | 1.00E-03            | 1.00E-03            | 1.00E-03             | 1.00E-03          | 1.00E-03            | 1.00E-03           |
| k      | 1.4                 | 1.4                 | 1.4                  | 1.4               | 1.4                 | 1.4                |
| p_v    | 2300                | 2300                | 2300                 | 2300              | 2300                | 2300               |
| pG0    | 8.00E-03            | 8.00E-03            | 8.00E-03             | 8.00E-03          | 8.00E-03            | 8.00E-03           |
| p0     | 1.00E+05            | 1.00E+05            | 1.00E+05             | 1.00E+05          | 1.00E+05            | 1.00E+05           |
| dp     | 9.00E+04            | 9.00E+04            | 9.00E+04             | 9.00E+04          | 9.00E+04            | 9.00E+04           |
| t_span | 0, 0.004            | 0, 0.004            | 0, 0.004             | 0, 0.004          | 0, 0.004            | 0, 0.004           |
| t_eval | t_span, 2000        | t_span, 2000        | t_span, 2000         | t_span, 2000      | t_span, 2000        | t_span, 2000       |
