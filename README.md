# Pullback‑Mediated Context Alignment (MCSR × Deleuze × MEE)

**One‑line claim.** Turn cross‑domain “context alignment” from rhetoric into a structural, auditable object: if two domain‑specific reasoning traces pull back along an intermediate context **L** to a shared core structure, they align; otherwise we output a minimal counterexample.

**Method (compact).** Philosophical base in **Deleuze** (difference and becoming); technical field via **differential geometry** to model strata, flows, and boundaries; structural implementation by **category‑theoretic pullbacks** as the alignment criterion. We expose a minimal, model‑agnostic metric **LSC‑PB** (Layered Step Consistency — Pullback mediated).

## Quickstart
```bash
# 1) Run the demo (no external deps; uses stdlib only)
python3 scripts/run_demo.py

# 2) Inspect the generated report
cat artifacts/report.json
```
Expected: a deterministic score `s` and a `PASS` flag if `s ≥ 0.92`, plus environment, data checksum, and provenance.

## What the demo does (toy)
- Loads two tiny “domain” traces (C and D) and an intermediate context **L** from `data/example.json`.
- Normalizes both traces via L, computes a structural residual Δ and score `s = 1 − Δ`.
- Emits `artifacts/report.json` with: score, threshold, PASS/FAIL, SHA256 of data, and runtime info.

## Repository layout
- `scripts/run_demo.py` — one‑command demo; emits `artifacts/report.json`.
- `metrics/lsc_pb.py` — the minimal metric implementation (toy).
- `data/example.json` — two domain traces + the intermediate context L.
- `docs/overview.md` — 1‑page mapping: Deleuze → Diff‑Geo → Pullback.
- `LICENSE`, `.gitignore`.

## License
MIT
