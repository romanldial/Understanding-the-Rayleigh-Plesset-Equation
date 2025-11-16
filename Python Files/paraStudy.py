import matplotlib.pyplot as plt
import numpy as np

def parametric_study(
    n_runs, min, max, func, title, xlabel, ylabel,
    sweep_name="param", skip_crit=False, critical_val=None
):
    """
    Runs a parametric study plotting multiple curves between min and max.
    
    - - - Parameters - - -
        n_runs : int
            Number of intermediate curves.
        min, max : float
            Sweep range.
        func : callable
            Function taking a single sweep parameter p and returning (x, y).
        sweep_name : str
            Name of the parameter being swept (used in legend labels).
        skip_crit : bool, optional
            If True, do not plot the curve where p == critical_val.
        critical_val : float, optional
            Critical value to skip if skip_crit is True.

    Automatically switches to logarithmic spacing if the range spans several
    orders of magnitude and both min and max are positive.
    """

    plt.figure(figsize=(8,5))

    # Decide whether to use log spacing
    # Conditions:
    #   * both bounds > 0
    #   * log-span exceeds ~3 decades
    use_log = (min > 0) and ((max / min) > 1e3)

    if use_log:
        # Logarithmic spacing (min and max must be > 0)
        p_values = np.logspace(np.log10(min), np.log10(max), n_runs + 1)
    else:
        # Linear spacing (original method)
        p_values = np.linspace(min, max, n_runs + 1)

    for p in p_values:

        # Skip the critical value if requested
        if skip_crit and (critical_val is not None):
            if abs(p - critical_val) / abs(critical_val) < 1e-6:
                continue

        x, y = func(p)
        plt.plot(x, y, label=f"{sweep_name} = {p:.3e}")

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
