# Work Decomposition Skill

**Load at**: Stage 01 entry (Phases 0–1) and Stage 02 entry (Phase 2)
**Token budget**: ~900 tokens (this stub) | Full version: ~2,000 tokens

---

## Purpose

The parent methodology for this workspace. Classifies a process, frames it as a
SIPOC, and decomposes it into a Stage → Step → Task hierarchy. Phases 0–2 are
detailed here; later phases are delegated to their own skills and stages.

---

## The 8-phase framework

| Phase | Name | Stage | Skill / reference |
|-------|------|-------|-------------------|
| 0 | Classify the process | 01 | this skill |
| 1 | SIPOC & scope | 01 | this skill |
| 2 | Hierarchical decomposition (HTA) | 02 | this skill |
| 3 | Automation scoring | 03 | `automation-scoring/SKILL.md` |
| 4 | PACE resilience | 04 | `pace-design/SKILL.md` |
| 5 | RACI ownership | 04 | `04-pace-raci/STAGE.md` |
| 6 | Artifact assembly & value stream | 05 | `_core/patterns/artifact-menu.md` |
| 7 | Monitor & improve | 06 | `06-monitor/STAGE.md` |

Load only the phases named by the current STAGE.md. Do not work ahead.

---

## Phase 0, Classify the process

Assign the process to one of 8 categories. Classification sets decomposition
depth in Stage 02 and shapes how steps are scored in Stage 03.

| Category | Defining trait | Typical example |
|----------|----------------|-----------------|
| Operational / Transactional | High volume, repeatable, rule-bound | Invoice processing |
| Knowledge / Decision | Expertise-driven judgment | Credit underwriting |
| Creative | Novel output each run | Campaign design |
| Physical / Industrial | Material transformation, machinery | Assembly-line QA |
| Service / Customer-facing | Direct interaction, SLA-bound | Support ticket triage |
| Regulatory / Compliance | Mandated steps, audit trail | KYC verification |
| Strategic | Infrequent, high-stakes, ambiguous | Market-entry planning |
| Cross-functional | Spans 3+ teams with handoffs | Order-to-cash |

If two categories fit equally, pick the one that demands the *deeper*
decomposition and note the ambiguity. For a genuinely unclear type, load
`_core/skills/process-types/SKILL.md`.

---

## Phase 1, SIPOC & scope

SIPOC frames the process before it is decomposed. Build the five columns
right to left, start from the Customer and what they need.

| Column | Question it answers |
|--------|---------------------|
| Suppliers | Who or what provides the inputs? |
| Inputs | What is consumed to start the work? |
| Process | The 5–7 high-level steps (decomposition seeds) |
| Outputs | What the process produces |
| Customers | Who receives the output |

Rules:
- The Process column holds **5–7 steps**, no more. Each becomes a Stage 02 seed.
- Define the **start event** (trigger) and **end event** (definition of done).
- State what is **explicitly out of scope**, adjacent work this process does not own.
- Recommend artifacts (A1–A10) against the human's goal; see `_core/patterns/artifact-menu.md`.

---

## Phase 2, Hierarchical decomposition (HTA)

Break every SIPOC process step into a three-level tree:

```
PROCESS
└── STAGE   Named phase with a clear entry and exit condition; has an owner
    └── STEP    Discrete activity with one identifiable actor, tool, and output
        └── TASK    Atomic action, cannot split further without losing meaning
```

Sizing guide:
- **Stage**, 10–60 minutes of work, or a logical handoff point
- **Step**, one activity, one clear deliverable
- **Task**, one actor, one tool, one output

Decompose until every leaf is a Task. Go past three levels only when the
process type (Phase 0) warrants it, e.g., decision trees for Knowledge
processes, safety notes for Physical processes.

Annotate every Stage and Step with: `actor`, `trigger`, `output`,
`decision_point`, `data_in`, `data_out`, `tools`. Mark decision gateways (⊕),
parallel tracks (‖), and loops (↺) explicitly; they drive the Stage 03
scorecard and the flow diagram.

---

## Decomposition quality checks

- Every leaf is a Task, not a vague Step
- No Stage hides a handoff inside it, handoffs are explicit transitions
- Decision points are marked wherever the path branches on a condition
- Granularity is consistent, sibling units are roughly comparable in size
- An actor is named for every Stage and Step (never "someone")

---

## Reference

- Process classification edge cases: `_core/skills/process-types/SKILL.md`
- Artifact selection (Phase 1): `_core/patterns/artifact-menu.md`
- Later-phase skills: `_core/skills/automation-scoring/SKILL.md`, `_core/skills/pace-design/SKILL.md`
