# FAQ (Public)

**Q1. Why not just compare final answers or CoT strings?**  
They miss layered contexts and polysemy. We compare structures under an intermediate context L.

**Q2. Is this model‑specific?**  
No. The metric is model‑agnostic; only the traces and context tags matter.

**Q3. Can I plug my own tracer?**  
Yes. Expose your steps as a list of strings or a graph; keep seeds + environment fixed.

**Q4. What does a 'pass' mean?**  
Score ≥ threshold and low variance across reruns; otherwise we emit a minimal counterexample.
