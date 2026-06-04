# Stage 03, Automation Analysis

**One job**: Score every Step for automation potential. Assign tiers. Recommend technology.

**Skill to load**: `_core/skills/automation-scoring/SKILL.md`
**Reference**: `_core/patterns/automation-patterns.md` (load if tech recommendations are needed)

**Input**: `02-decompose/output/decomposition.md` and `actors.md`

---

## Read before starting

Open and read:
- `02-decompose/output/decomposition.md`, every Step is a scoring candidate
- `01-intake/output/scope.md`, process type affects scoring interpretation
- `01-intake/output/artifact-selection.md`, if A4/A5 not selected, this stage is lightweight

---

## Automation scoring, 7 dimensions

Score each **Step** (not Task) on a 1–5 scale across 7 dimensions.
Sum the scores for a composite out of 35.

| Dimension | 1 (Hard) | 3 (Mixed) | 5 (Easy) |
|-----------|----------|-----------|----------|
| **Repeatability** | Unique each time | Mostly repeatable | Identical every time |
| **Rule Clarity** | Requires deep expertise | Semi-structured judgment | Fully rule-specifiable |
| **Data Availability** | Physical presence / tacit knowledge | Mixed digital/physical | All digital, structured |
| **Volume** | Rare (< weekly) | Medium (daily) | High (> 100/day) |
| **Error Tolerance** | Zero tolerance, high stakes | Errors caught within hours | Errors easily caught/corrected |
| **Integration Feasibility** | No APIs, legacy/physical | Some APIs, partial | Modern APIs, open systems |
| **Change Frequency** | Changes constantly | Changes quarterly | Stable for 1+ year |

---

## Tier assignment

| Score | Tier | Label | Action |
|-------|------|-------|--------|
| 28–35 | 1 | Automate Now | Strong ROI, low risk, build this first |
| 20–27 | 2 | Automate with AI | Use LLM/ML for judgment gaps |
| 12–19 | 3 | Human-in-Loop | Automate scaffolding, human decides |
| 5–11 | 4 | Assist/Augment | Tooling to support humans, not replace |
| 1–4 | 5 | Keep Human | Automation not appropriate |

---

## Technology mapping (for Tier 1–3 steps)

Assign the best-fit category from:

| Category | Best for |
|----------|---------|
| RPA / Scripting | Deterministic, UI-based, data movement |
| Rule Engine | Classification, routing, eligibility decisions |
| Generative AI (LLM) | Text generation, extraction, summarization, reasoning |
| Classical ML | Prediction from structured data |
| Computer Vision | Document processing, visual inspection |
| Workflow Orchestration | Multi-step process coordination |
| API Integration | System-to-system data flow |
| IoT / Machinery | Physical process automation |
| Human + AI Hybrid | Steps needing human judgment + AI speed |

---

## Output files, write to `output/`

| File | Contents | Required |
|------|----------|----------|
| `automation-scorecard.md` | Step-by-step scores across 7 dimensions + tier | Yes |
| `tech-fit-matrix.md` | Step → recommended technology category | If A5 selected |
| `tier-summary.md` | Grouped by tier, Tier 1 list, Tier 2 list, etc. | Yes |
| `automation-notes.md` | Scoring rationale for non-obvious decisions | If questions arose |

---

## Scorecard format

```markdown
## Step: [Step name] (Stage [N] / Step [N.N])
Actor: [current actor]
Decision point: [yes/no]

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Repeatability | [1-5] | [brief reason] |
| Rule Clarity | [1-5] | [brief reason] |
| Data Availability | [1-5] | [brief reason] |
| Volume | [1-5] | [brief reason] |
| Error Tolerance | [1-5] | [brief reason] |
| Integration Feasibility | [1-5] | [brief reason] |
| Change Frequency | [1-5] | [brief reason] |
| **TOTAL** | **[sum]/35** | |

**Tier**: [1–5], [label]
**Recommended tech**: [category]
**Notes**: [anything unusual]
```

---

## Human edit window

Tell the human:
> "Stage 03 complete. Automation scorecard is in `03-analyze/output/automation-scorecard.md`.
> The scoring is based on observable characteristics; you may know things about these steps
> that change the scores (e.g., a 'simple' step that's actually regulated, or a step that
> looks complex but has a perfect existing API). Edit scores and tier assignments freely.
> Say **proceed to stage 04** when ready."

---

## Done checklist

- [ ] Every Step in the decomposition has a score row in the scorecard
- [ ] Every Tier 1–2 step has a recommended technology assigned
- [ ] `output/tier-summary.md` groups steps by tier
- [ ] `_state.md` updated: Stage 03 → complete, awaiting human review
