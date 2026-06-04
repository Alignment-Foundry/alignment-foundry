# Chartered Operations Workspace

ICM workspace for a long-running chartered agent that continuously monitors, improves,
and maintains a specific system in collaboration with human reviewers.

## Quick start

1. Fill in `_memory/constitutional/charter.md` completely before first use
2. Provide system documentation in `01-onboard/input/`
3. Open a conversation with Claude pointing to this workspace
4. Say: **"Begin onboarding"** (first time) or **"Start session"** (subsequent times)

## What makes this workspace different

Unlike a one-shot workspace, this one accumulates:
- **Constitutional memory**, the charter, immutable without human approval
- **Working memory**, session state, rebuilt each session from the persistent record
- **Episodic memory**, rolling history of what was tried and what worked
- **Semantic memory**, confirmed system knowledge, written only from verified outcomes

The agent deepens its understanding of your system over weeks and months.
The scope stays fixed. The depth grows.

## The charter is the boundary

Before the agent does anything, it reads the charter. The charter defines:
- What the agent can observe (observation scope)
- What it can change without asking (autonomous execution)
- What requires human approval (approval scope)
- What it can never touch (hard limits)

Do not skip filling out the charter. An agent without clear boundaries will either
under-perform (too cautious) or over-reach (too confident). The charter resolves both.

## Session workflow

Each session follows this pattern:
1. Agent reads charter + SESSION.md
2. Agent checks review queue and open findings
3. Agent runs Stage 02 (observe), monitors for new anomalies
4. If threshold met → drafts proposal in Stage 03
5. Proposal queued for human review in Stage 04
6. After human approves → Stage 05 deploys
7. After 24h → Stage 06 measures outcome and updates memory

## Trust curve

- **Weeks 1–2**: Agent proposes everything, human reviews everything
- **Month 2–3**: High-confidence, low-risk changes may be applied autonomously
- **Month 4+**: Human reviews summaries, not individual proposals for routine changes
- **Always**: Production deployments require human approval

---

**Created by**: Chartered Agent Architecture + ICM design session
**Framework**: Van Clief ICM v1.0 + Chartered Agent Pattern v1.0
