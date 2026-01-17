# structure-vs-control

A minimal, runnable demonstration comparing control-based branching and structure-based invariants that produce the same numerical result.

This repository is intentionally small. It is meant to be *experienced*, not adopted.

---

## What this is

This repository contains two small Python programs that solve the *same* simple convergence problem and produce numerically equivalent outcomes.

- **Unstructured (control-based)**  
  Uses conditionals, clamps, and guards to keep the system stable.

- **Structured (invariant-based)**  
  Encodes stability directly into the update rule so invalid states are unreachable by construction.

The point is not performance, optimization, or cleverness.  
The point is to contrast **control** with **structure** in the most direct way possible.

If the distinction matters, you’ll feel it immediately.  
If it doesn’t, no argument here will convince you.

---

## What this is not

- Not a framework  
- Not a library  
- Not a benchmark  
- Not a claim about novelty  
- Not a tutorial  
- Not a theory exposition  

This repository does not try to teach you *how* to think this way.

It exists to show that a different structural choice is possible — and to let you decide whether it resonates.

---

## Familiar structural precedents

The distinction illustrated here is not unique. Similar transitions from control-heavy logic to structure-first design have occurred repeatedly across engineering disciplines. The domains differ; the structural move is the same.

### Normalization instead of clamping
In many numerical systems, values were historically allowed to grow freely and then corrected using conditional clamps or bounds checks. Normalization replaces this pattern by constraining the state space itself (e.g., unit vectors or probability simplices), making invalid magnitudes unreachable rather than corrected after the fact.

### Bresenham’s line algorithm
Early line-drawing approaches relied on floating-point arithmetic, rounding, and branching to decide which pixel to activate next. Bresenham’s algorithm encodes the geometry of the line directly using an invariant error term, eliminating decision-making and correction logic inside the loop.

### Symplectic integration
Basic time integration methods often require damping, thresholds, or renormalization to manage accumulated error such as energy drift. Symplectic integrators preserve conservation laws structurally, removing the need for corrective logic during evolution.

In each case, stability is not *enforced* through control; it *emerges* from the structure of the system itself.

---

## What is intentionally missing

This repository stops short on purpose.

It does **not** include:
- broader mappings to real-world systems
- guidance on organizational or architectural application
- criteria for when structure-first design is appropriate
- prescriptions for adoption

Those pieces are contextual and relational.  
They do not survive abstraction well.

This work advances through dialogue, not documentation.

---

## How to run

Requires Python 3. No dependencies.

```bash
python run.py
