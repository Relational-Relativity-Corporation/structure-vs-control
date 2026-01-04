
# unstructured.py
# Control-based convergence with explicit branching and guards

def run(
    x0=2.5,
    target=0.0,
    dt=0.1,
    max_steps=1000,
    max_bound=1.0,
    epsilon=1e-6,
):
    x = x0

    for _ in range(max_steps):
        # Naive update step
        x_new = x - dt * (x - target)

        # Explicit control logic
        if x_new > max_bound:
            x_new = max_bound
        elif x_new < -max_bound:
            x_new = -max_bound

        # Convergence guard
        if abs(x_new - x) < epsilon:
            break

        # Numerical safety
        if x_new != x_new:  # NaN check
            x_new = 0.0

        x = x_new

    return x
