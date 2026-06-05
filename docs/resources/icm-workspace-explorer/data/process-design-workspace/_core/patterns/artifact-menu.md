# Artifact Menu

Reference for Stage 01 artifact selection and Stage 05 assembly.

---

## The 10 Artifacts

| ID | Name | When to produce | Format | Approx size |
|----|------|----------------|--------|-------------|
| **A1** | SIPOC Summary | Always, first artifact | Markdown table | ~200 words |
| **A2** | Decomposition Tree | Always, core artifact | Indented markdown | ~500–2,000 words |
| **A3** | Flow Diagram | When flow complexity > 3 stages | Mermaid code | ~50–100 lines |
| **A4** | Automation Scorecard | When automation is the goal | Table per step | ~50 words/step |
| **A5** | Technology Fit Matrix | When technology selection is needed | Grouped table | ~300 words |
| **A6** | PACE Analysis | For each flagged critical step | Structured blocks | ~200 words/step |
| **A7** | RACI Matrix | When multiple stakeholders exist | Table | ~200 words |
| **A8** | Value Stream Summary | When efficiency/lean analysis needed | Table + metrics | ~300 words |
| **A9** | Implementation Roadmap | When planning a build | Phased plan | ~400 words |
| **A10** | Process Spec Sheet | When formal documentation is needed | Full document | ~1,500–3,000 words |

---

## Recommended combinations by goal

**Goal: Document an existing process**
→ A1, A2, A3, A7, A10

**Goal: Scope automation opportunities**
→ A1, A2, A4, A5, A9

**Goal: Full engineering analysis**
→ A1, A2, A3, A4, A5, A6, A7, A8, A9

**Goal: Lean/efficiency improvement**
→ A1, A2, A3, A7, A8

**Goal: Compliance/audit documentation**
→ A1, A2, A3, A6, A7, A10

**Goal: Agile/iterative (minimal viable)**
→ A1, A2, A4

---

## Artifact dependencies

A3 depends on A2 (uses decomposition stage names)
A5 depends on A4 (groups by technology, requires tier assignments)
A6 depends on A4 (PACE applied to Tier 1–2 steps)
A8 depends on A2 and A4 (cycle time + automation potential combined)
A9 depends on A4 (phases built from tier groupings)
A10 incorporates all other artifacts as sections
