# cg_unstructured.py
# Control-based conjugate gradient with explicit runtime guards

import numpy as np


def solve(A, b, x0=None, max_iter=100, tol=1e-10):
    """
    Conjugate gradient solver with runtime guards.

    Uses conditional checks to handle edge cases:
    - NaN/Inf detection
    - Convergence test with early exit
    - Divergence detection
    - Division safety checks
    """
    n = len(b)
    x = x0 if x0 is not None else np.zeros(n)

    r = b - A @ x
    p = r.copy()
    rs_old = np.dot(r, r)

    # Guard: check for already converged
    if rs_old < tol:
        return x, 0

    for i in range(max_iter):
        Ap = A @ p
        pAp = np.dot(p, Ap)

        # Guard: division safety check
        if abs(pAp) < 1e-15:
            break

        alpha = rs_old / pAp

        # Guard: NaN/Inf check on alpha
        if not np.isfinite(alpha):
            break

        x = x + alpha * p
        r = r - alpha * Ap

        rs_new = np.dot(r, r)

        # Guard: convergence test with early exit
        if rs_new < tol:
            return x, i + 1

        # Guard: divergence detection
        if rs_new > 1e10 * rs_old:
            break

        # Guard: division safety for beta
        if abs(rs_old) < 1e-15:
            break

        beta = rs_new / rs_old

        # Guard: NaN/Inf check on beta
        if not np.isfinite(beta):
            break

        p = r + beta * p
        rs_old = rs_new

    return x, i + 1


def count_branches():
    """Count conditional statements in this implementation."""
    return 8  # if/break statements in the algorithm
