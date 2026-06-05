# Process Design Workspace

Interpretable Context Methodology (ICM) workspace for decomposing any work process
into structured components and producing a complete set of process engineering artifacts.

## Quick start

1. Fill in `01-intake/input/process-brief.md` (or leave blank, the agent will ask)
2. Open a conversation with Claude pointing to this workspace
3. Say: **"Begin Stage 01"**
4. The agent reads `CLAUDE.md` and `01-intake/STAGE.md` and starts

## What you'll produce

After a full run (all 6 stages):
- SIPOC table
- Hierarchical decomposition tree (Stage/Step/Task)
- Mermaid flow diagram
- Automation scorecard (Tier 1–5 per step)
- Technology fit matrix
- PACE resilience analysis (critical steps)
- RACI ownership matrix
- Value stream summary
- Implementation roadmap
- Process spec sheet (formal document)

## How it works

Each numbered folder is one stage. The `STAGE.md` inside tells the agent exactly what
to do. Outputs go in `output/`. The human reviews and edits before the next stage starts.

## Skill files

`_core/skills/` contains four skill stubs. They are loaded on demand, one at a time,
only for the stage that needs them. This keeps the context window focused.

The full skill content lives in the `.skill` bundle files produced by the design session.
Copy the contents of `work-decomposition/SKILL.md` from that bundle into
`_core/skills/work-decomposition/SKILL.md` to activate the full skill.

## Stage 06 (monitor)

Stage 06 is the ongoing improvement loop. Activate it after the process has been
running in production for 2+ weeks. It captures exceptions and edge cases as findings,
proposes targeted model updates, and maintains a versioned changelog.

---

**Created by**: Work Decomposition + ICM design session
**Framework**: Van Clief ICM v1.0
**Skill**: work-decomposition.skill
