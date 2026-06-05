# Automation Scoring Skill

**Load at**: Stage 03 entry
**Token budget**: ~800 tokens (this stub) | Full version: ~1,500 tokens

---

## Purpose

Score each Step in the decomposition for automation potential across 7 dimensions.
Assign an Automation Tier (1–5) and recommend a technology category.

---

## 7-Dimension Scoring Matrix

Score each Step 1–5 per dimension. Sum for composite score out of 35.

| # | Dimension | 1, Hard to automate | 5, Easy to automate |
|---|-----------|---------------------|---------------------|
| 1 | Repeatability | Unique each time | Identical every time |
| 2 | Rule Clarity | Requires deep expertise | Fully rule-specifiable |
| 3 | Data Availability | Physical / tacit knowledge | All digital & structured |
| 4 | Volume | Rare (< weekly) | High frequency (> 100/day) |
| 5 | Error Tolerance | Zero tolerance, high stakes | Errors easily caught/corrected |
| 6 | Integration Feasibility | No APIs / legacy / physical | Modern APIs / open systems |
| 7 | Change Frequency | Changes constantly | Stable for 1+ year |

---

## Tier Assignment

| Score | Tier | Label | Recommended action |
|-------|------|-------|--------------------|
| 28–35 | 1 | Automate Now | Build first, strong ROI, low risk |
| 20–27 | 2 | Automate with AI | Use LLM/ML for judgment gaps |
| 12–19 | 3 | Human-in-Loop | Automate scaffolding, human decides |
| 5–11 | 4 | Assist / Augment | Tools to support humans, not replace |
| 1–4 | 5 | Keep Human | Automation not appropriate |

---

## Technology Category Map

| Category | Best fit for |
|----------|-------------|
| RPA / Scripting | Deterministic steps, UI automation, file/data movement |
| Rule Engine | Classification, routing, eligibility, decision tables |
| Generative AI (LLM) | Text extraction, summarization, drafting, reasoning |
| Classical ML | Prediction from structured data, classification |
| Computer Vision | Document OCR, image inspection, defect detection |
| Workflow Orchestration | Multi-step coordination, DAGs, retry logic |
| API Integration | System-to-system calls, webhooks, event-driven |
| IoT / Machinery | Physical automation, sensors, PLC, robotics |
| Human + AI Hybrid | Steps needing judgment backed by AI speed/recall |

---

## Scoring heuristics

**Decision point = true → reduce Rule Clarity by 1**
**External dependency present → reduce Integration Feasibility by 1**
**Compliance-regulated step → reduce Error Tolerance to max 3**
**First time running this process type → note uncertainty in rationale**

---

## Reference

For detailed technology design patterns per category, see:
`_core/patterns/automation-patterns.md`
