# Concept Card — Pullback‑mediated Context Alignment (LSC‑PB)

**Role.** Turn 'context alignment' into a structural, auditable object.

**Minimal scene.** Two domain traces (C, D) for the same task; search an intermediate context L.

**Structural claim (compact).** If the step‑graphs under C and D pull back along u: L→C and v: L→D to a shared core G★, count as aligned; else output a minimal counterexample.

**Gate & failure.** Fixed environment & seed; layered context tags present. Fail when no L satisfies residual ≤ ε.

**Mapping.**
- Deleuze: difference → productive variation; becoming → flow across strata; anti‑identity bias.
- Differential geometry: strata/flows/boundaries; L is the mediating chart where traces are compared.
- Category theory: pullback square witnesses alignment; residual computed on L‑normalized traces.

**Code hook.** metrics/lsc_pb.py (toy) → replace with graph‑level equivalence; expose a stable Python API.
