# cg_run.py
# Side-by-side execution of structured vs unstructured conjugate gradient

import numpy as np
import cg_unstructured
import cg_structured


def create_test_problem(n=10, seed=42):
    """
    Create a small dense positive definite test problem.

    Returns A (positive definite matrix) and b (right-hand side).
    The true solution is x = [1, 2, 3, ..., n].
    """
    np.random.seed(seed)

    # Create a dense positive definite matrix
    # A = L @ L.T + diagonal dominance term
    L = np.eye(n) + 0.1 * np.triu(np.random.randn(n, n), 1)
    A = L @ L.T + np.eye(n)  # Ensures positive definiteness

    # True solution
    x_true = np.arange(1, n + 1, dtype=float)

    # Right-hand side
    b = A @ x_true

    return A, b, x_true


def main():
    print("Conjugate Gradient: Structure vs Control")
    print("=" * 50)

    # Create test problem
    A, b, x_true = create_test_problem(n=10)
    print(f"\nProblem size: {len(b)}x{len(b)}")
    print(f"Condition number: {np.linalg.cond(A):.2f}")

    # Run both solvers
    x0 = np.zeros(len(b))

    x_unstructured, iters_unstruct = cg_unstructured.solve(
        A, b, x0=x0.copy(), max_iter=50
    )
    x_structured, iters_struct = cg_structured.solve(
        A, b, x0=x0.copy(), max_iter=50
    )

    # Compute errors relative to true solution
    err_unstructured = np.linalg.norm(x_unstructured - x_true)
    err_structured = np.linalg.norm(x_structured - x_true)

    # Compute residuals
    res_unstructured = np.linalg.norm(b - A @ x_unstructured)
    res_structured = np.linalg.norm(b - A @ x_structured)

    # Results
    print("\nResults:")
    print("-" * 50)
    print(f"Unstructured iterations: {iters_unstruct}")
    print(f"Structured iterations:   {iters_struct}")
    print()
    print(f"Unstructured error:   {err_unstructured:.2e}")
    print(f"Structured error:     {err_structured:.2e}")
    print()
    print(f"Unstructured residual: {res_unstructured:.2e}")
    print(f"Structured residual:   {res_structured:.2e}")
    print()

    # Solution comparison
    diff = np.linalg.norm(x_unstructured - x_structured)
    print(f"Difference between solutions: {diff:.2e}")

    # Branch count
    print("\nBranch Analysis:")
    print("-" * 50)
    print(f"Unstructured conditionals: {cg_unstructured.count_branches()}")
    print(f"Structured conditionals:   {cg_structured.count_branches()}")

    print("\nKey insight:")
    print("-" * 50)
    print("The structured version has zero branches in the iteration loop.")
    print("Stability comes from bounded_div(), not runtime guards.")
    print("On GPU: no warp divergence, predictable memory access.")


if __name__ == "__main__":
    main()
