# structured.py
# Structure-based convergence using invariants

def project(x):
    """
    Smooth projection into a bounded domain.
    Invalid states are unreachable by construction.
    """
    return x / (1.0 + abs(x))


def run(
    x0=2.5,
    target=0.0,
    dt=0.1,
    max_steps=1000,
):
    x = project(x0)

    for _ in range(max_steps):
        # Invariant-preserving update
        x = project(x - dt * (x - target))

    return x

