# structure-vs-control

A minimal, runnable demonstration comparing control-based branching and structure-based invariants that produce the same numerical result.

## What this is
This repository contains two small Python programs that solve the *same* simple convergence problem and produce numerically equivalent outcomes.

- **Unstructured (control-based)**: uses conditionals, clamps, and guards to keep the system stable.
- **Structured (invariant-based)**: encodes stability directly into the update rule so invalid states are unreachable by construction.

The point is not performance or optimization. The point is to contrast **control** with **structure**.

## What this is not
- Not a framework
- Not an optimization benchmark
- Not a claim about novelty
- Not an explanation of theory

## Familiar structural precedents
The distinction illustrated here is not unique. Similar transitions from control-heavy logic to structure-first design have occurred repeatedly across engineering disciplines. The domains differ; the structural move is the same.

**Normalization instead of clamping**  
In many numerical systems, values were historically allowed to grow freely and then corrected using conditional clamps or bounds checks. Normalization replaces this pattern by constraining the state space itself (e.g., unit vectors or probability simplices), making invalid magnitudes unreachable rather than corrected after the fact.

**Bresenham’s line algorithm**  
Early line-drawing approaches relied on floating-point arithmetic, rounding, and branching to decide which pixel to activate next. Bresenham’s algorithm encodes the geometry of the line directly using an invariant error term, eliminating decision-making and correction logic inside the loop.

**Symplectic integration**  
Basic time integration methods often require damping, thresholds, or renormalization to manage accumulated error such as energy drift. Symplectic integrators preserve conservation laws structurally, removing the need for corrective logic during evolution.

In each case, stability is not *enforced* through control; it *emerges* from the structure of the system itself.

## How to run
Requires Python 3. No dependencies.

```bash
python run.py
```

## Output

The file `output.txt` shows the result of running `run.py`:

```
Unstructured result: 9.261387130997869e-06
Structured result:   1.680645434348696e-47
Difference:          9.261387130997869e-06
```

Both approaches converge toward the target value (0.0). The structured version reaches a value 41 orders of magnitude closer to zero—not because it's "better optimized," but because the projection operator `x / (1 + |x|)` compounds stability at every step rather than merely bounding the result after the fact

