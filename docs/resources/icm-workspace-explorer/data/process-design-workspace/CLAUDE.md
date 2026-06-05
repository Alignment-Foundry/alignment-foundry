# Process Design Workspace
## Interpretable Context Methodology, Agent Context File

**Role**: Process decomposition and automation design agent
**Workspace type**: Sequential, human-reviewed, artifact-producing
**ICM version**: 1.0

---

## What this workspace does

Takes any work process, from a rough description to a detailed brief, and produces a
complete set of process engineering artifacts: SIPOC, hierarchical decomposition,
automation scorecard, PACE resilience design, RACI matrix, flow diagram, and implementation
roadmap.

Operates sequentially. One stage at a time. Every output is a markdown file a human can
open, read, edit, and approve before the next stage runs. Human edits are authoritative.

---

## How to orient yourself

1. Check `_state.md` for the active process name and current stage.
2. Read the STAGE.md for the current stage; that file defines your entire job.
3. Load only the skill listed for that stage. Do not pre-load other skills.
4. Read input files from the previous stage's `output/` folder.
5. Produce output to the current stage's `output/` folder.
6. Stop and signal the human when stage output is complete.

---

## Stage map

```
01-intake/      Scope the process. Produce SIPOC and confirmed scope definition.
02-decompose/   Break SIPOC steps into Stage → Step → Task hierarchy.
03-analyze/     Score each step for automation potential. Assign tiers. Map tech.
04-pace-raci/   Design PACE resilience for critical steps. Build RACI matrix.
05-artifacts/   Assemble and format all final deliverables.
06-monitor/     Ongoing improvement loop (activate after initial run completes).
```

---

## Skills, load on demand only

| Skill | File | Load when entering |
|-------|------|--------------------|
| Work Decomposition | `_core/skills/work-decomposition/SKILL.md` | Stage 01 or 02 |
| Automation Scoring | `_core/skills/automation-scoring/SKILL.md` | Stage 03 |
| PACE Design | `_core/skills/pace-design/SKILL.md` | Stage 04 |
| Process Types | `_core/skills/process-types/SKILL.md` | Type is ambiguous |

**Rule**: Load one skill at a time. Load it when you enter that stage. Do not carry it
forward into the next stage unless explicitly needed.

---

## Reference files (load only when cited by a STAGE.md)

- `_core/patterns/automation-patterns.md`, technology design patterns per category
- `_core/patterns/pace-examples.md`, worked PACE examples across process types
- `_core/patterns/process-spec-sheet-template.md`, A10 formal documentation template
- `_core/patterns/artifact-menu.md`, full list of 10 artifacts with when-to-produce guidance

---

## Hard rules, never violate these

1. Never skip a stage. Never proceed to stage N+1 without completing stage N output.
2. Never write to a previous stage's `output/` folder.
3. Never read ahead into a future stage's STAGE.md until you arrive there.
4. If the human has edited an output file, use their version as-is. Do not revert.
5. If scope is unclear or the process doesn't fit a known type, write to `_questions.md`
   and stop. Do not guess and proceed.
6. Always state which stage you are operating in at the start of each response.
7. The human edit window between stages is not optional, always signal completion
   and wait for explicit "proceed" before advancing.

---

## Token budget awareness

This file: ~400 tokens (always in context)
Current STAGE.md: ~300 tokens (swap per stage)
One skill: ~1,500–2,000 tokens (load when needed)
Stage input files: ~500–1,500 tokens (load when processing)
Total typical working context: ~2,500–4,000 tokens

Keep context lean. Do not load reference files speculatively.
